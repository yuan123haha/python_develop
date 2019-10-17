# Author:haha

import logging
from ..conf import setting


def logger(log_type):
    '''
    处理所有日志工作
    :param log_type:
    :return:
    '''
    logger=logging.getLogger(log_type)
    logger.setLevel(setting.LOG_LEVEL)

# create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(setting.LOG_LEVEL)

    # create file handler and set level to warning
    log_file = "%s/log/%s" %(setting.base_dir, setting.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(setting.LOG_LEVEL)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch and fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger