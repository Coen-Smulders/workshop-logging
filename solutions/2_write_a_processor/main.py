import structlog
from structlog.typing import EventDict


class SecretHider:
    def __init__(self, password_fields=("password", "secret")):
        self.password_fields = password_fields

    def __call__(self, logger, method_name, event_dict: EventDict):
        keys_to_hide = event_dict.keys() & self.password_fields
        if keys_to_hide:
            event_dict.update(
                {key: "*******" for key in (event_dict.keys() & self.password_fields)}
            )
        return event_dict


structlog.configure(
    processors=[
        SecretHider(),
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(),
        structlog.dev.ConsoleRenderer(),
    ],
)

logger = structlog.get_logger()


def main():
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
