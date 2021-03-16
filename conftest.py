import random

import pytest


@pytest.fixture(scope='module')
def random_int():
    return random.randint(0, 1000)


@pytest.fixture(scope='session', params=["666", "爱我中华"])
def use_params(request):
    print(request.param)


def pytest_collection_modifyitems(session, config, items):
    print(type(items))
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)
