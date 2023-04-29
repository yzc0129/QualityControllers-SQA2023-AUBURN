import logging 

#creates a logging object and returns it
def giveMeLoggingObject():
    format_str = '%(name)s-%(asctime)s - %(process)d -%(levelname)s- %(message)s'
    file_name  = 'logger.log' #logs are stored in this file
    logging.basicConfig(format=format_str, filename=file_name, level=logging.INFO)
    loggerObj = logging.getLogger('logger')
    return loggerObj