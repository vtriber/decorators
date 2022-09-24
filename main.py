from utils.logger import logger

@logger('loglog.txt')
def summator(a, b):
    return a + b



summator(1, 2)
