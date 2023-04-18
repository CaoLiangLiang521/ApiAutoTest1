import allure
from jsonpath_rw import parse

from data.apiurl import HOST_URL
from data.variable import var
from util.log import logger
from util.requestUtil import RquestUtll
from util.yamlUtil import YamlUtil


class SceneRquestUtil:
    def __init__(self,ymlFileName,requestUtil):
        self.yamlUtil = YamlUtil('../config/ChangJing/'+ymlFileName+'.yml')
        self.requestUtil = requestUtil

    def yamAndRequestl(self):
        for dict in self.yamlUtil.getYamlData():  #一个dict表示一个请求
            with allure.step('发送请求：'+dict['name']):

                logger.info('发送请求:'+dict['name'])
                #拼接url路径
                depend = dict['depend']
                if depend != None:
                    #判断请求依赖
                    headers = depend['headers']
                    if headers != None:
                         for key, value in headers.items():
                             if dict['headers'] == None:
                                 dict['headers'] = { }
                             #把依赖添加到请求头上
                             dict ['headers'][key] = var.get(value)


                    #判断params 依赖
                    params = depend['params']
                    if params != None:
                        for key, value in params.items():
                            if dict['params'] == None:
                                dict['params'] = { }

                            # 把参数添加到params 上
                            dict['headers'][key] = var.get(value)

                    #判断data 依赖
                    data = depend['data']
                    if data != None:
                        for key, value in data.items():
                            if dict['data'] == None:
                                dict['data'] = { }

                            # 把参数添加到params 上
                            dict['data'][key] = var.get(value)
                    #判断json 依赖
                    json = depend['json']
                    if json != None:
                        for key, value in json.items():
                            if dict['json'] == None:
                                dict['json '] = {}

                            # 把参数添加到params 上
                            dict['json'][key] = var.get(value)
                #发送请求
                result = self.requestUtil.doRequest(method=dict['method'], url=dict['url'], params=dict['params'],
                                      data=dict['data'],
                                      json=dict['json'], headers=dict['headers'], )
                self.requestUtil.assertResult(result, dict['vaildate']['statudata'], dict['vaildate']['errorcode'],
                                dict['vaildate']['masg'])
                #判断是否导出数据extract
                extract = dict['extract']
                if extract != None:
                    body = extract
                    if body != None:
                        for key,value in body.iteems():
                            #存储健值对
                            var.set(key,self.getDeptParmas(result.json(),value))
                    # 判断是否导出响应头
                    headers= dict['headers']
                    if extract != None:
                        body = extract
                        if body != None:
                            for key, value in headers.iteems():
                                # 存储健值对
                                var.set(key, self.getDeptParmas(result.headers,value))



        # jsonpath-rw 提出数据函数，dict给一个字典对象 regex提取规则(data.code)
        def getDeptParmas(self, dict, regex):
                json_exe = parse(regex)
                result = json_exe.find(dict)
                params = [match.value for match in result][0]
                logger.info('源数据:' + str(dict) + ',提取规则:' + str(regex) + ',提取结果:' + str(params))
                return params







if __name__ == '__main__':
    ru = RquestUtll()

    cjru = SceneRquestUtil('changjing_01','ru')
    cjru .yamAndRequestl()

