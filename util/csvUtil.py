import csv

from util.log import logger


class CsvUtil:
    def __init__(self,file):
        self.file = file

    # 读取csv数据 返回字典格式 字典键为第一行
    def getCsvData(self):
        f = open(file = self.file,mode= 'r',encoding='utf-8-sig')
        # 读取的数据
        reader = list(csv.reader(f))
        #print(reader)
        dictList = []
        for i in range(1,len(reader)):
            dict = {}   #一条数据的字典
            data = reader[i]    #一条csv数据
            keys = reader[0]     #  key数据
            for j in range(len(keys)):
                dict[keys[j]] = data[j]   #组装一条字段
            #print(dict)


            dictList.append(dict)    #添加到dictlist列表里


        logger.info("读取csv里面的内容" + str(dictList))
        #print(dictList)

        return dictList




if __name__ == '__main__':
    yu = CsvUtil('../data/projects.csv')
    yu.getCsvData()