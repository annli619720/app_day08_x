import pytest

import allure

class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title='第一个测试')
    def test_001_1(self):
        allure.attach('描述', '尝试登录')
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title='第二一个测试')
    def test_001_2(self):
        allure.attach('描述', '输入用户名')
        allure.attach('描述', '输入密码')
        allure.attach('描述', '点击登录')
        assert 1


