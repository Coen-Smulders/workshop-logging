import structlog

# # create logger
logger = structlog.getLogger("simpleLogger")

# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
