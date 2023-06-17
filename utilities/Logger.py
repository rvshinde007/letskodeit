import logging
import inspect

class LogGen:
    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler("C:\\Users\\HP\\OneDrive\\Desktop\\letskodeit\\Logs\\logfile.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s: %(message)s")
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger


#--> Level Set

# DEBUG
# INFO
# WARNING
# ERROR
# CRICTICAL
