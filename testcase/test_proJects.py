import allure
import pytest

from util.requestDataUtil import RequestDataUtil
from util.requestUtil import RquestUtll
#获取网络请求工具
ru = RquestUtll()

login = RequestDataUtil('projects')
list = login.getRequestData()

@pytest.fixture(scope="function",params=list)
def getData(request):
    return request.param

@allure.feature("创建项目")
class TestProJects:
    @allure.story('projects')
    def test_projects(self,getData):
        # 发送请求
        result = ru.doRequest(method=getData['method'], url=getData['url'], params=getData['params'],
                              data=getData['data'],
                              json=getData['json'], headers=getData['headers'])
        print(result)
        ru.assertResult(result,getData['validate']['statusCode'],getData['validate']['errorcode'],getData['validate']['msg'])

