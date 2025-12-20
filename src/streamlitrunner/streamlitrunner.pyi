import os
import sys
from pathlib import Path
from typing import Literal, TypedDict, overload

from streamlit.runtime.scriptrunner import get_script_run_ctx

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

def run(
    *,
    open_as_app: bool = True,
    print_command: bool = True,
    client_toolbar_mode: Literal["auto", "developer", "viewer", "minimal"] = "minimal",
    fill_page_content: bool = False,
    theme_base: Literal["dark", "light"] = "light",
    server_port: int = 8501,
    server_run_on_save: bool = True,
    server_headless: bool = ...,
    global_disable_watchdog_warning: bool = ...,
    global_disable_widget_state_duplication_warning: bool = ...,
    global_show_warning_on_direct_execution: bool = ...,
    global_development_mode: bool = ...,
    global_log_level: Literal["error", "warning", "info", "debug"] = ...,
    global_unit_test: bool = ...,
    global_app_test: bool = ...,
    global_suppress_deprecation_warnings: bool = ...,
    global_min_cached_message_size: float = ...,
    global_max_cached_message_age: int = ...,
    global_store_cached_forward_messages_in_memory: bool = ...,
    global_data_frame_serialization: Literal["legacy", "arrow"] = ...,
    logger_level: Literal["error", "warning", "info", "debug"] = ...,
    logger_message_format: str = ...,
    logger_enable_rich: bool = ...,
    client_caching: bool = ...,
    client_display_enabled: bool = ...,
    client_show_error_details: bool = ...,
    client_show_sidebar_navigation: bool = ...,
    runner_magic_enabled: bool = ...,
    runner_install_tracer: bool = ...,
    runner_fix_matplotlib: bool = ...,
    runner_post_script_gc: bool = ...,
    runner_fast_reruns: bool = ...,
    runner_enforce_serializable_session_state: bool = ...,
    runner_enum_coercion: Literal["off", "nameOnly", "nameAndValue"] = ...,
    server_folder_watch_blacklist: str = ...,
    server_file_watcher_type: Literal["auto", "watchdog", "poll", "none"] = ...,
    server_allow_run_on_save: bool = ...,
    server_address: str = ...,
    server_script_health_check_enabled: bool = ...,
    server_base_url_path: str = ...,
    server_enable_cors: bool = ...,
    server_enable_xsrf_protection: bool = ...,
    server_max_upload_size: int = ...,
    server_max_message_size: int = ...,
    server_enable_arrow_truncation: bool = ...,
    server_enable_websocket_compression: bool = ...,
    server_enable_static_serving: bool = ...,
    browser_server_address: str = ...,
    browser_gather_usage_stats: bool = ...,
    browser_server_port: int = ...,
    server_ssl_cert_file: str = ...,
    server_ssl_key_file: str = ...,
    ui_hide_top_bar: bool = ...,
    ui_hide_sidebar_nav: bool = ...,
    magic_display_root_doc_string: bool = ...,
    magic_display_last_expr_if_no_semicolon: bool = ...,
    deprecation_showfile_uploader_encoding: bool = ...,
    deprecation_show_image_format: bool = ...,
    deprecation_show_pyplot_global_use: bool = ...,
    theme_primary_color: str = ...,
    theme_background_color: str = ...,
    theme_secondary_background_color: str = ...,
    theme_text_color: str = ...,
    theme_font: Literal["sans serif", "serif", "monospace"] = ...,
) -> None: ...
def fill_page_content(
    remove_pad: bool = True,
    remove_header_footer: bool = True,
    wide_layout: bool = True,
) -> None: ...
