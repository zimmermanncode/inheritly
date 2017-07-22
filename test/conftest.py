from functools import lru_cache

import inheritly

import pytest


@pytest.fixture
def method():

    def method(cls):  # pragma: no cover
        pass

    return method


@pytest.fixture
def decorators():
    return lru_cache(),


@pytest.fixture
def inheritly_class(method, decorators):

    class Test(inheritly.object):

        method = inheritly(*decorators)(method)

    return Test


@pytest.fixture
def inheritly_subclass(inheritly_class):

    class Test(inheritly_class):

        def method(cls):  # pragma: no cover
            pass

    return Test
