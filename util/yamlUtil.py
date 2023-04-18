import yaml

from util.log import logger


class YamlUtil:
    def __init__(self,file):
        self.file = file

    def getYamlData(self):
        # 读取yaml配置数据
        f = open(file=self.file, mode='r', encoding='utf-8')
        # yaml.load()函数转成字典格式 stream操作的文件对象 Loader指定加载器对象
        j = yaml.load(stream=f, Loader=yaml.FullLoader)
        logger.info('读取yaml配置内容:'+str(j))
        return j

