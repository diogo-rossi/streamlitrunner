import os
import sys
import warnings
from pathlib import Path
from typing import Literal, TypedDict, overload

import psutil
import pyautogui
import pygetwindow
import webview
from streamlit import session_state
from streamlit.runtime.scriptrunner import get_script_run_ctx


class SessionState:
    def __contains__(self, name: str) -> bool:
        return hasattr(self, name)


gettrace = getattr(sys, "gettrace", None)
debugging = gettrace is not None and gettrace()
interactively_debugging = sys.flags.interactive or sys.flags.quiet or debugging
inside_streamlit_app = get_script_run_ctx()

session = SessionState()
if inside_streamlit_app:
    session = session_state


class RuntimeConfig(TypedDict, total=False):
    CLOSE_OPENED_WINDOW: bool
    OPEN_AS_APP: bool
    BROWSER: Literal["chrome", "msedge"]
    PRINT_COMMAND: bool
    STREAMLIT_GLOBAL_DISABLE_WATCHDOG_WARNING: bool
    STREAMLIT_GLOBAL_DISABLE_WIDGET_STATE_DUPLICATION_WARNING: bool
    STREAMLIT_GLOBAL_SHOW_WARNING_ON_DIRECT_EXECUTION: bool
    STREAMLIT_GLOBAL_DEVELOPMENT_MODE: bool
    STREAMLIT_GLOBAL_LOG_LEVEL: Literal["error", "warning", "info", "debug"]
    STREAMLIT_GLOBAL_UNIT_TEST: bool
    STREAMLIT_GLOBAL_APP_TEST: bool
    STREAMLIT_GLOBAL_SUPPRESS_DEPRECATION_WARNINGS: bool
    STREAMLIT_GLOBAL_MIN_CACHED_MESSAGE_SIZE: float
    STREAMLIT_GLOBAL_MAX_CACHED_MESSAGE_AGE: int
    STREAMLIT_GLOBAL_STORE_CACHED_FORWARD_MESSAGES_IN_MEMORY: bool
    STREAMLIT_GLOBAL_DATA_FRAME_SERIALIZATION: Literal["legacy", "arrow"]
    STREAMLIT_LOGGER_LEVEL: Literal["error", "warning", "info", "debug"]
    STREAMLIT_LOGGER_MESSAGE_FORMAT: str
    STREAMLIT_LOGGER_ENABLE_RICH: bool
    STREAMLIT_CLIENT_CACHING: bool
    STREAMLIT_CLIENT_DISPLAY_ENABLED: bool
    STREAMLIT_CLIENT_SHOW_ERROR_DETAILS: bool
    STREAMLIT_CLIENT_TOOLBAR_MODE: Literal["auto", "developer", "viewer", "minimal"]
    STREAMLIT_CLIENT_SHOW_SIDEBAR_NAVIGATION: bool
    STREAMLIT_RUNNER_MAGIC_ENABLED: bool
    STREAMLIT_RUNNER_INSTALL_TRACER: bool
    STREAMLIT_RUNNER_FIX_MATPLOTLIB: bool
    STREAMLIT_RUNNER_POST_SCRIPT_GC: bool
    STREAMLIT_RUNNER_FAST_RERUNS: bool
    STREAMLIT_RUNNER_ENFORCE_SERIALIZABLE_SESSION_STATE: bool
    STREAMLIT_RUNNER_ENUM_COERCION: Literal["off", "nameOnly", "nameAndValue"]
    STREAMLIT_SERVER_FOLDER_WATCH_BLACKLIST: str
    STREAMLIT_SERVER_FILE_WATCHER_TYPE: Literal["auto", "watchdog", "poll", "none"]
    STREAMLIT_SERVER_HEADLESS: bool
    STREAMLIT_SERVER_RUN_ON_SAVE: bool
    STREAMLIT_SERVER_ALLOW_RUN_ON_SAVE: bool
    STREAMLIT_SERVER_ADDRESS: str
    STREAMLIT_SERVER_PORT: int
    STREAMLIT_SERVER_SCRIPT_HEALTH_CHECK_ENABLED: bool
    STREAMLIT_SERVER_BASE_URL_PATH: str
    STREAMLIT_SERVER_ENABLE_CORS: bool
    STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION: bool
    STREAMLIT_SERVER_MAX_UPLOAD_SIZE: int
    STREAMLIT_SERVER_MAX_MESSAGE_SIZE: int
    STREAMLIT_SERVER_ENABLE_ARROW_TRUNCATION: bool
    STREAMLIT_SERVER_ENABLE_WEBSOCKET_COMPRESSION: bool
    STREAMLIT_SERVER_ENABLE_STATIC_SERVING: bool
    STREAMLIT_BROWSER_SERVER_ADDRESS: str
    STREAMLIT_BROWSER_GATHER_USAGE_STATS: bool
    STREAMLIT_BROWSER_SERVER_PORT: int
    STREAMLIT_SERVER_SSL_CERT_FILE: str
    STREAMLIT_SERVER_SSL_KEY_FILE: str
    STREAMLIT_UI_HIDE_TOP_BAR: bool
    STREAMLIT_UI_HIDE_SIDEBAR_NAV: bool
    STREAMLIT_MAGIC_DISPLAY_ROOT_DOC_STRING: bool
    STREAMLIT_MAGIC_DISPLAY_LAST_EXPR_IF_NO_SEMICOLON: bool
    STREAMLIT_DEPRECATION_SHOWFILE_UPLOADER_ENCODING: bool
    STREAMLIT_DEPRECATION_SHOW_IMAGE_FORMAT: bool
    STREAMLIT_DEPRECATION_SHOW_PYPLOT_GLOBAL_USE: bool
    STREAMLIT_THEME_BASE: Literal["dark", "light"]
    STREAMLIT_THEME_PRIMARY_COLOR: str
    STREAMLIT_THEME_BACKGROUND_COLOR: str
    STREAMLIT_THEME_SECONDARY_BACKGROUND_COLOR: str
    STREAMLIT_THEME_TEXT_COLOR: str
    STREAMLIT_THEME_FONT: Literal["sans serif", "serif", "monospace"]


rc: RuntimeConfig = {
    "OPEN_AS_APP": True,
    "BROWSER": "msedge",
    "CLOSE_OPENED_WINDOW": True,
    "PRINT_COMMAND": True,
    "STREAMLIT_CLIENT_TOOLBAR_MODE": "minimal",
    "STREAMLIT_SERVER_RUN_ON_SAVE": True,
    "STREAMLIT_SERVER_PORT": 8501,
    "STREAMLIT_THEME_BASE": "light",
}

for key in rc:
    if key.startswith("STREAMLIT_") and key in os.environ:
        rc[key] = os.environ[key]


def close_app():
    pyautogui.hotkey("alt", "f4")
    psutil.Process(os.getpid()).terminate()


@overload
def run(
    *,
    open_as_app: bool = True,
    browser: Literal["chrome", "msedge"] = "msedge",
    close_opened_window: bool = True,
    print_command: bool = True,
    **kwargs,
): ...


@overload
def run(**kwargs): ...


def run(
    **kwargs,
):
    """Run the script file as a streamlit app and exits.

    Executes the command `streamlit run <script.py>` before exit the program.

    The parameters of this function have preference over the runtime config variable `streamlitrunner.rc`

    Parameters
    ----------
        - `open_as_app` (`bool`, optional): Defaults to `True`.

            Whether to open the chromium based browser launching the url in "application mode" with `--app=` argument (separate window).
            If `True`, the option `STREAMLIT_SERVER_HEADLESS` is set to `True`.

        - `browser` (`Literal["chrome", "msedge"]`, optional): Defaults to `"msedge"`.

            The chromium based browser in which to run the streamlit app.

        - `close_opened_window` (`bool`, optional): Defaults to `True`.

            Whether to close a previously opened browser window with the same streamlit app name.

        - `print_command` (`bool`, optional): Defaults to `True`.

            Whether to print the command executed by this function.

        - `**kwargs`: Additional keyword arguments passed as options to the `streamlit run` command.

            These keyword arguments have the same names as the environment variables, but passed with
            lower case and without the prefix `streamlit_`. Use `streamlit run --help` to get a list.

            Some values are predefined, if not given. Namely:

                + `client_toolbar_mode` (`STREAMLIT_CLIENT_TOOLBAR_MODE`) = `"minimal"`

                + `server_headless` (`STREAMLIT_SERVER_HEADLESS`): `True` if `open_as_app=True`

                + `server_run_on_save` (`STREAMLIT_SERVER_RUN_ON_SAVE`) = `True`

                + `server_port` (`STREAMLIT_SERVER_PORT`) = `8501`

                + `theme_base` (`STREAMLIT_THEME_BASE`) = `"light"`

    """
    if not inside_streamlit_app and not interactively_debugging:

        if kwargs.get("open_as_app", True) and kwargs.get("browser", "msedge") not in ["chrome", "msedge"]:
            warnings.warn("`open_as_app` option only currently supported for chromium web browsers: 'chrome' and 'msedge'", Warning)
            kwargs["open_as_app"] = False

        if "STREAMLIT_SERVER_HEADLESS" not in rc:
            if "STREAMLIT_SERVER_HEADLESS" in os.environ:
                rc["STREAMLIT_SERVER_HEADLESS"] = bool(os.environ["STREAMLIT_SERVER_HEADLESS"])
            else:
                if kwargs.get("open_as_app", True):
                    rc["STREAMLIT_SERVER_HEADLESS"] = True
                else:
                    rc["STREAMLIT_SERVER_HEADLESS"] = False

        spec_args = ["open_as_app", "browser", "close_opened_window", "print_command"]

        for key in kwargs:
            rc[(key if key in spec_args else f"streamlit_{key}").upper()] = kwargs[key]

        for option in rc:
            if option.startswith("STREAMLIT_"):
                os.environ[option] = str(rc[option])

        server_headless: bool = rc["STREAMLIT_SERVER_HEADLESS"]
        close_opened_window: bool = rc.get("CLOSE_OPENED_WINDOW", True)
        print_command: bool = rc.get("PRINT_COMMAND", True)
        open_as_app: bool = rc.get("OPEN_AS_APP", True)
        browser: str = rc.get("BROWSER", "msedge")
        server_port: int = rc.get("STREAMLIT_SERVER_PORT", 8501)

        if close_opened_window:
            windows1 = pygetwindow.getWindowsWithTitle("streamlit")
            windows2 = pygetwindow.getWindowsWithTitle(Path(sys.argv[0]).stem)
            for window in windows1:
                if window in windows2 and " Streamlit" in window.title:
                    window.close()

        print()

        def run_streamlit():
            command = f'streamlit run --server.headless {server_headless} --server.port {server_port} {sys.argv[0]} -- {" ".join(sys.argv[1:])}'
            if print_command:
                print(command)
            os.system(command)

        try:
            if open_as_app:
                webview.create_window("Hello world", f"http://localhost:{server_port}/")
                webview.start(run_streamlit)
            else:
                run_streamlit()

        except KeyboardInterrupt:
            sys.exit()
        sys.exit()
