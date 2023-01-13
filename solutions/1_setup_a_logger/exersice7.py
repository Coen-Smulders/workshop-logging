import os.path
import structlog

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "exercise.log")
print(path)

# Do not use a with construction in production code to pass the file to the logging.
# Here is it used to ensure the log file is properly closed without boilerplate
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
