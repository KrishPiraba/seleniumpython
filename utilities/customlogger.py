import logging
class LogGen:
    @staticmethodc
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",format='%(asctime)s:%(message)s',datefmt="%m/%d/%y %I:%M:%S %p")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger