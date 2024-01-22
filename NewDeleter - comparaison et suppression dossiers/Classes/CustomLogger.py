import logging


class CustomLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = self._setup_logger()

    def _setup_logger(self):
        logger = logging.getLogger('custom_logger')
        logger.setLevel(logging.DEBUG)

        # %(asctime)s - %(levelname)s -
        formatter = logging.Formatter('%(message)s')

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger

    def log_message(self, message, log_level=logging.INFO):
        if log_level == logging.DEBUG:
            self.logger.debug(message)
        elif log_level == logging.INFO:
            self.logger.info(message)
        elif log_level == logging.WARNING:
            self.logger.warning(message)
        elif log_level == logging.ERROR:
            self.logger.error(message)
        elif log_level == logging.CRITICAL:
            self.logger.critical(message)