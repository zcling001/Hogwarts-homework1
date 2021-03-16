import pytest


class TestFixture01:

    # 开始
    def setup_class(self):
        print("\n****开始测试****")

    # 结束
    def teardown_class(self):
        print("****结束测试****")

    # 参数引用
    def test_a(self, random_int):
        print("随机数测试结果为：", random_int)


if __name__ == '__main__':
    pytest.main(['-s', 'test_fixture_01.py'])
    # 测试网络提交
