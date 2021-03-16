import allure
import pytest


@allure.feature('我是测试用例类上面的描述信息')
class TestFixture01:

    # 开始
    @allure.story('setup_class方法开始')
    def setup_class(self):
        print("\n****开始测试****")

    # 结束
    @allure.story('teardown_class方法结束')
    def teardown_class(self):
        print("****结束测试****")

    @pytest.mark.run(order=2)
    def test_zhong(self, random_int):
        print("随机数测试结果为：", random_int)

    @pytest.mark.run(order=1)
    def test_use_params(self, use_params):
        self.login
        print("use_params：测试完成")

    @allure.step('测试步骤方法')
    def login(self):
        print("我是一个测试步骤方法")
        # pytest --alluredir ./report
        # allure generate ./report/ -o ./result --clean


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture_01.py'])
    # 测试网络提交
