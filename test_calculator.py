import pytest
from hw0307.testcase.calculator import Calculator
import yaml
import pytest_assume
from hw0307 import get_datas


class TestCal:
    def setup_class(self):
        self.cal = Calculator()
        print("\n开始测试！\n")

    def teardown_class(self):
        print("\n结束测试！")

    @pytest.mark.run(order=1)
    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[0], ids=get_datas.get_datas()[4])
    def test_add(self, a, b, expected):
        pytest.assume(expected == self.cal.add(a, b))
        pytest.assume(3 == 1 + 2)
        # pytest.assume(False)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[1], ids=get_datas.get_datas()[4])
    def test_sub(self, a, b, expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[2], ids=get_datas.get_datas()[4])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[3],
                             ids=get_datas.get_datas()[4])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)

    #测试随机数
    @pytest.mark.run(order=5)
    def test_random(self, random_int):
        print("随机数测试结果为：", random_int)
