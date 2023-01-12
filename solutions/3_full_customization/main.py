from typing import Any, TextIO

import structlog
from structlog.typing import EventDict

AUDIT = 100
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_NAME_TO_LEVEL = {
    "audit": AUDIT,
    "critical": CRITICAL,
    "exception": ERROR,
    "error": ERROR,
    "warn": WARNING,
    "warning": WARNING,
    "info": INFO,
    "debug": DEBUG,
    "notset": NOTSET,
}

_LEVEL_TO_NAME = {
    v: k for k, v in _NAME_TO_LEVEL.items() if k not in ("warn", "exception", "notset")
}


class SematicLogger(structlog.BoundLogger):
    def login_attempt(self, event, login_successful, **kwargs):
        return self._proxy_to_logger(
            "audit", event, login_successful=login_successful, **kwargs
        )


class CustomPrintLogger(structlog.PrintLogger):
    audit = structlog.PrintLogger.msg


class CustomPrintLoggerFactory:
    def __init__(self, file: TextIO | None = None):
        self._file = file

    def __call__(self, *args: Any) -> CustomPrintLogger:
        return CustomPrintLogger(self._file)


class FilterLogLevel:
    def __init__(self, min_level=0):
        self.min_level = min_level

    def __call__(self, logger, method_name, event_dict: EventDict):
        if _NAME_TO_LEVEL.get(method_name, 0) < self.min_level:
            raise structlog.DropEvent
        return event_dict


structlog.configure(
    processors=[
        FilterLogLevel(ERROR),
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper("iso"),
        structlog.processors.JSONRenderer(sort_keys=True),
    ],
    wrapper_class=SematicLogger,
    context_class=dict,
    logger_factory=CustomPrintLoggerFactory(),
    cache_logger_on_first_use=False,
)

logger = structlog.get_logger()
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
logger.login_attempt("user tried to log in on the system", True, user="pythoneer")
