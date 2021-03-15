import random

import pytest


@pytest.fixture(scope='module')
def random_int():
    return random.randint(0, 1000)
