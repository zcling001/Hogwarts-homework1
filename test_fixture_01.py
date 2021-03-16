import pytest


class TestFixture01:

    # 开始
    def setup_class(self):
        print("\n****开始测试****")

    # 结束
    def teardown_class(self):
        print("****结束测试****")

    @pytest.mark.run(order=2)
    def test_zhong(self, random_int):
        print("随机数测试结果为：", random_int)

    @pytest.mark.run(order=1)
    def test_use_params(self, use_params):
        print("use_params：测试完成")


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture_01.py'])
    # 测试网络提交
