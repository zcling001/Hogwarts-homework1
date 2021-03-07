import pytest
from hw0307.testcase.calculator import Calculator

class TestCal:
    def setup_class(self):
        self.cal=Calculator()
        print("\n开始测试！\n")

    def teardown_class(self):
        print("\n结束测试！")

    @pytest.mark.parametrize("a,b,expected",[(3,5,8),(-1,-2,-3),(3000,1000,4000),],
                         ids=["int","minus","bigint"])
    def test_add(self,a,b,expected):
        assert expected == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expected", [(9, 5, 4), (-3, -2, -1), (4000, 1000, 3000), ],
                             ids=["int", "minus", "bigint"])
    def test_sub(self,a,b,expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.parametrize("a,b,expected", [(2, 3, 6), (-3, -2, 6), (400, 100, 40000), ],
                             ids=["int", "minus", "bigint"])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.parametrize("a,b,expected", [(10, 5, 2), (-6, -2, 3), (400, 100, 4), ],
                             ids=["int", "minus", "bigint"])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)

