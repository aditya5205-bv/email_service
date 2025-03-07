import logging
from settings import LOG_LEVEL

custom_logging = logging.getLogger(__name__)

custom_logging.setLevel(LOG_LEVEL)

console_formatter = logging.Formatter(
    "{message}",
    style="{",
)

file_formatter = logging.Formatter(
    "{asctime} - {levelname} - {message} - {funcName} - {lineno}",
    style="{",
    datefmt="%d-%m-%Y %H:%M:%S",
)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("./logs/email.log")

custom_logging.addHandler(console_handler)
custom_logging.addHandler(file_handler)

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)