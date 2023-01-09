import logging

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Logging level also has to be set for the handeler, since the handler also has WARNING as default level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# add formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

logger.addHandler(ch)

# 'application' code
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
