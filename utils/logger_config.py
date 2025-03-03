import logging

def setup_logger(name):
    logger = logging.getLogger("selenium_logger")
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    if logger.hasHandlers():
        logger.handlers.clear()
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("reports/test_log.log")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    return logger