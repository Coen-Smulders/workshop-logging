import structlog


def main():
    logger = structlog.get_logger()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
    logger.critical("critical message")
    logger.login_attempt("user tried to log in on the system", True, user="pythoneer")


if __name__ == "__main__":
    main()
