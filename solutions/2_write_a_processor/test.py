import main
import pytest
import structlog


@pytest.fixture(name="log_output")
def fixture_log_output():
    return structlog.testing.LogCapture()


@pytest.fixture(autouse=True)
def fixture_configure_structlog(log_output):
    structlog.configure(processors=[log_output])


def test_logging(log_output):
    main.main()
    actual = log_output.entries
    expected = [
        {
            "server": "lsrv0023",
            "user": "fu00234",
            "password": "D034kGkds",
            "status": "succes",
            "event": "calling ssh on linux virtual machine",
            "log_level": "debug",
        },
        {
            "user": "python programmer",
            "password": "Pyth0n!s@maz1ng",
            "event": "user logged in",
            "log_level": "info",
        },
        {
            "user": "user/u003353",
            "attemps": 5,
            "event": "wrong password attempts over threshold for user last 30 minutes",
            "log_level": "warning",
        },
        {
            "service": "Azure Functions",
            "tenantId": "a4dio49-38d8-0d94-4kkh-n3l3i90ga992",
            "secret": "dad41cc536b1c3a58af8542e43fbe9f6",
            "event": "Unable to connect to azure service",
            "log_level": "error",
        },
        {
            "status": "unable to start system",
            "event": "cannot read config file",
            "log_level": "critical",
        },
        {
            "exception": ZeroDivisionError("division by zero"),
            "exc_info": True,
            "event": "fatal exception occurred",
            "log_level": "error",
        },
    ]
    assert str(actual) == str(expected)
