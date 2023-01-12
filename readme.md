# Setting up a logger

<p>
setting up a logger using pythons native logging module can be done fast. 
Using the following lines of code, will give you a logger that can be used:

```python
import logging

logger = logging.getLogger()
```
This however will give you a logger with limit setup, lets have a look at it.
</p>

**All exercises can be done in main.py, unless stated different.**

## Exercise 1

Run main in exercise 1, this file has 5 lines of logging. 
Which of those will be printed to the console and why?

<details><summary>Awnser</summary>
<p>
The default logging level is set to warning, when no logging level is set. 
As a result info and debug will not be printed
</p>
</details>

## Exercise 2

Change the logging level so show print all the logging lines to the console
<details><summary>Hint</summary>
<p>
Just setting the loglevel on the logger is not enough, it also has to be set on the handler.
add a StreamHandler to the logger and set the correct level on this handler.
</p></details>

## Exercise 3

Out of the box without additional set up the logging library only prints the string given as input.
To enhance the use for the logger, it is possible to add formatters to enrich the output.

Add a formatter that adds the following information to the output:
* a timestamp when the log has been recorded
* the name of the logger recording the log-rule
* the level of the log-rule given by the logger

<details><summary>Hint</summary>
<p>
this formatter is set on the handler, not on the logger.
</p></details>

## Bonus: Exercise 4
In the exercises before the logger has been configured in the code. 
Instead of doing the configuration in the cde, it is also possible to load loggers from a config file.
Change the setup of your logger to use the simple logger from logging.conf

## Exercise 5
Change python logging for structlog without additional configuration. 

## Exercise 6
add a key with the name "action" and value "create incident" to the critical log message

## Bonus: Exercise 7
Setup structlog to directly write to a file instead of stdout

# Write a Processor

One of the strengths of structlog is the relative ease it can be customised with. 
This ranges from writing custom handlers to write to logs away to where you want 
them to be (e.g. log arrogation tooling). 

Structlog also offers the possibility to make what is custom wrapper loggers. 
These can help to establish uniform ways of logging use-cases. A few hypothetical 
use cases could be methods with required parameters that will log:
* call request on an API endpoint
* data access requests
* checkpoint that have been reached in a proces

When considering to use a sematic logger for this always keep in mind if it adds 
benefit over using regular logging calls. Benefits can be more consistent logging 
in the application, clarifying what exactly is logged or adding some custom logic 
for this type of logging (if extremely specific to that one use-case, otherwise use processors)

This exercise covers how to write a processor. Processors are small functions 
working on the log before writing. Example form the exercises before are:
* adding a timestamp
* add the log level to the output
* converting the log input to a printable string

Beside those use case other use cases that can be used are:
* filtering data that is not allowed in the logs
* make a ticket for all logging that is critical
* write your own string formatter (e.g. json dump to get a json as output)


## Exercise 8
In the main.py there are logging rules written. Those logging rules contain 
information that should not be visible in the logs. To ensure this is not visible 
write a filter that masks any values with the key password or secret.

<details><summary>Hint</summary>
<p>

[Structlog documentation on how to write a processor](https://www.structlog.org/en/stable/processors.html)
</p></details>

## Bonus: Exercise 9
The default output of structlog helps to make logging more human-readable, 
however exceptions in logging add quite a bit of text which are not always nicely formatted.
There are a couple of libraries that can enhance the readability. One of them is rich, try to install this
(if you are using poetry you can uncomment the line in pyproject.toml). After installing Rich you can rerun the 
previous exercises and see the result. More information can be found 
[here](https://www.structlog.org/en/stable/console-output.html)

# Testing your logging

## Exercise 10
Stuctlog allows you to test your logging. This can be very useful, both to ensure your logging is working as intended. 
Try to write a unit test, that test the logging output of the main function found in main.py

documentation on testing of logging can be found [here](https://www.structlog.org/en/stable/testing.html)

# Bonus: Full customization

Structlog is highly customizable. This bonus exercise will allow you to create an understanding how to do this.
Multiple components are to be used for this exercise, including:
* Configuration of structlog
* Writing a custom logging api
* Writing your own processors
* Defining your own log level

## Bonus: Exercise 11
Make custom components for structlog that will allow the follow line of code to work:
```python
import structlog

logger = structlog.get_logger()
logger.debug("debug message")
logger.info("info message")
logger.warning("warn message")
logger.error("error message")
logger.critical("critical message")
logger.login_attempt("user tried to log in on the system", True, user="pythoneer")
```
resulting in the following output on the console (where the timestamp is using ISO 8601 format)
```json
{"event": "error message", "level": "error", "timestamp": "YYYY-MM-DDTHH:mm:SS±HHMM"}
{"event": "critical message", "level": "critical", "timestamp": "YYYY-MM-DDTHH:mm:SS±HHMM"}
{"event": "user tried to log in on the system", "level": "audit", "login_successful": true, "timestamp": "YYYY-MM-DDTHH:mm:SS±HHMM", "user": "pythoneer"}
```