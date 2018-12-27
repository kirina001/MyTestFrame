# coding:utf8
import logging


"""
        powered by Mr Will
           at 2018-12-21
        用来格式化打印日志到文件和控制台
"""
path = '..'
logger = None
# create logger
# 这里可以修改开源模块的日志等级
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                filename=path + "/lib/logs/all.log",
                level=logging.ERROR)
logger = logging.getLogger('frame log')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# # add formatter to ch
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

# 打印debug级别日志
def debug(ss):
    global logger
    try:
        logger.debug(ss)
    except:
        return

# 打印info级别日志
def info(str):
    global logger
    try:
        logger.info(str)
    except:
        return

# 打印debug级别日志
def warn(ss):
    global logger
    try:
        logger.warning(ss)
    except:
        return

# 打印error级别日志
def error(self, ss):
    global logger
    try:
        logger.error(ss)
    except:
        return

# 打印异常日志
def exception(self, e):
    global logger
    try:
        logger.exception(e)
    except:
        return


# 调试
if __name__ == '__main__':
    info('test')
