import allure

from util.requestUtil import RquestUtll
from util.sceneRquestUtil import SceneRquestUtil

@allure.feature('场景')
class TestChangJing:
    @allure.story('场景测试一 ')
    def test_changjing_01(self):
        ru = RquestUtll()
        print(RquestUtll)

        cjru = SceneRquestUtil('changjing_01', 'ru')
        cjru.yamAndRequestl()

