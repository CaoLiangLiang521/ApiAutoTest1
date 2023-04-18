import allure
import pytest

from util.requestDataUtil import RequestDataUtil
from util.requestUtil import RquestUtll

ru = RquestUtll()
#获取请求书记对象
login = RequestDataUtil('login')
list = login.getRequestData()


@pytest.fixture(scope='function',params=list)
def getData(request):
    return request.param


@allure.feature('登陆模块')
class TestLogin:
    @allure.story('login')  
    def test_login(self,getData):
        #发送请求
        result = ru.doRequest(method=getData['method'],url=getData['url'],params=getData['params'],data=getData['data'],
                     json=getData['json'],headers=getData['headers'])

        print('result.set-Cookie')
        #ru.assertResult(result,getData['validate']['statusCode'],getData['validate']['errorCode'],
                        #getData['validate']['msg'])


