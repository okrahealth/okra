import os
import logging

def enable_log(log_name):
    """ Enable logs written to file """
    logging.basicConfig(filename= log_name,
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')

def enable_cloud_log(level='INFO'):
    """ Enable logs using default StreamHandler """
    levels = {'INFO': logging.INFO, 'DEBUG': logging.DEBUG}
    logging.basicConfig(level=levels[level],
                        format='%(asctime)s %(levelname)s %(message)s')

