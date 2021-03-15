import pytest
from hw0307.testcase.calculator import Calculator
import yaml
import pytest_assume
from hw0307 import get_datas


class TestCal:
    def setup_class(self):
        self.cal=Calculator()
        print("\n开始测试！\n")

    def teardown_class(self):
        print("\n结束测试！")

    @pytest.mark.parametrize("a,b,expected",get_datas.get_datas()[0],
                         ids=get_datas.get_datas()[4])
    def test_add(self,a,b,expected):
        assert expected == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[1],
                         ids=get_datas.get_datas()[4])
    def test_sub(self,a,b,expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expected", get_datas.get_datas()[2],
                         ids=get_datas.get_datas()[4])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expected",get_datas.get_datas()[3],
                         ids=get_datas.get_datas()[4])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)

