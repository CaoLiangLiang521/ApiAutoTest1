import logging

# 设置日志打印模块
class Logger(logging.Logger):
    # 初始化函数 cmd_level控制台打印时日志默认级别 file_level写入日志文件默认级别
    def __init__(self, name='Dash',cmd_level=logging.DEBUG, file_level=logging.DEBUG):
        # 调用父类初始化函数
        super().__init__(name)
        try:
            self.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
            # 日志输出格式
            fmt = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
            # 日志文件路径及名称...手动创建logs文件夹
            self.log_file = '../logs/runlog.txt'
            # 设置控制台输出
            sh = logging.StreamHandler()
            sh.setFormatter(fmt) # 设置控制台输出格式
            sh.setLevel(cmd_level) #设置控制台输出的默认级别
            # 设置文件输出
            fh = logging.FileHandler(self.log_file,'a', encoding='utf-8')
            fh.setFormatter(fmt)
            fh.setLevel(file_level)
            # 添加日志输出方式
            self.addHandler(sh)
            self.addHandler(fh)
        except Exception as e:
            raise e

# 初始化logger对象 供外面使用
logger = Logger()