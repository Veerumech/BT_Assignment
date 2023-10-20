import logging
from datetime import datetime

d = datetime.now().strftime("%d-%m-%Y %H-%M-%S")

def logg(level, message):
    logging.basicConfig(filename=f"../log_files/{d}", level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')
    if level == 'debug':
        logging.debug(message)
    elif level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    elif level == 'critical':
        logging.critical(message)
    else:
        raise ValueError(f"Invalid logging level: {level}")

logg("info", "")
