import allure
import pytest
from hw0307.testcase.calculator import Calculator
import yaml
import pytest_assume
from hw0307 import get_datas


# 执行测试用例，把结果保存到result文件夹下（./result可自定义）
# pytest --alluredir ./result
# result中的测试结果生成测试报告
# allure generate ./result/ -o ./report --clean

@allure.feature('计算器测试报告')
class TestCal:
    def setup_class(self):
        self.cal = Calculator()
        # print("\n开始测试！\n")

    #
    # def teardown_class(self):
    #     print("\n结束测试！")

    @allure.story('开始测试加法')
    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas('data.yml')["add_datas"],
                             ids=get_datas.get_datas('data.yml')["myid"])
    def test_add(self, a, b, expected):
        pytest.assume(expected == self.cal.add(a, b))
        pytest.assume(3 == 1 + 2)
        # pytest.assume(False)

    @allure.story('开始测试减法')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas('data.yml')["sub_datas"],
                             ids=get_datas.get_datas('data.yml')["myid"])
    def test_sub(self, a, b, expected):
        assert expected == self.cal.sub(a, b)

    @allure.story('开始测试乘法')
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas('data.yml')["mul_datas"],
                             ids=get_datas.get_datas('data.yml')["myid"])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @allure.story('开始测试除法')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas('data.yml')["div_datas"],
                             ids=get_datas.get_datas('data.yml')["myid"])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)

    # 测试随机数
    @allure.story('随机数')
    @pytest.mark.run(order=5)
    def test_random(self, random_int):
        print("随机数测试结果为：", random_int)
