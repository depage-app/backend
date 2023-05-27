import logging

log_format = '%(asctime)s | %(levelname)s | %(message)s'
formatter = logging.Formatter(log_format)
ch = logging.StreamHandler()
ch.setFormatter(formatter)

log = logging.Logger('logger')
log.addHandler(ch)
