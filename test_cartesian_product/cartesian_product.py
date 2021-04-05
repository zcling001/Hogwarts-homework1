#笛卡尔积

import itertools
import pytest


@pytest.mark.parametrize('array0,array1', [([1, 3, 5, 7, 9], [2, 4, 6, 8]), ([1, 3, 5, 7], [2, 4, 6, 8, 10, 12, 14])],
                         ids=['长乘短', '短乘长'])
def test_runfunc(array0, array1):
    # 判断哪个是长数组
    result = []
    if len(array0) >= len(array1):
        for i in range(0, len(array0)):
            result.append([array0[i], array1[i % len(array1)]])
    else:
        for i in range(0, len(array1)):
            result.append([array1[i], array0[i % len(array0)]])
    print(result)


if __name__ == "__main__":
    pytest.main(['-sv', 'cartesian_product.py'])
