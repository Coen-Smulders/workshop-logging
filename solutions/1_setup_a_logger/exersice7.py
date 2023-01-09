import structlog
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "exercise.log")
print(path)
with open(path, "a+") as logfile:
    structlog.configure(
        logger_factory=structlog.PrintLoggerFactory(file=logfile),
    )

    # # create logger
    logger = structlog.getLogger("simpleLogger")

    # 'application' code
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message", action="create incident")
