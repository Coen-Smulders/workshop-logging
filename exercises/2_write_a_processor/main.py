import structlog
import logging

structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(),
        structlog.dev.ConsoleRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=False,
)


def main():
    logger = structlog.get_logger()

    logger.debug(
        "calling ssh on linux virtual machine",
        server="lsrv0023",
        user="fu00234",
        password="D034kGkds",
        status="succes",
    )
    logger.info("user logged in", user="python programmer", password="Pyth0n!s@maz1ng")
    logger.warning(
        "wrong password attempts over threshold for user last 30 minutes",
        user="user/u003353",
        attemps=5,
    )
    logger.error(
        "Unable to connect to azure service",
        service="Azure Functions",
        tenantId="a4dio49-38d8-0d94-4kkh-n3l3i90ga992",
        secret="dad41cc536b1c3a58af8542e43fbe9f6",
    )
    logger.critical("cannot read config file", status="unable to start system")
    try:
        result = 1 / 0
    except Exception as exc:
        logger.exception("fatal exception occurred", exception=exc)


if __name__ == "__main__":
    main()
