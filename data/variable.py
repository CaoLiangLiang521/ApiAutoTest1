from util.log import logger


class Variable:

    def set(self, key, value):
        # 保存键值对
        logger.info('存键值对:'+str(key)+'='+str(value))
        setattr(self, key, value)

    def get(self, key):
        logger.info('取键值对:key='+str(key))
        if hasattr(self,key): #是否有这个键
            return getattr(self, key)
        else:
            return None

# 初始化全局变量对象
var = Variable()
 
if __name__ == '__main__':
    var.set('name', 'zhangsnan')
    print(var.get('name'))