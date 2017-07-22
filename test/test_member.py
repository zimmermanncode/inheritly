from functools import lru_cache

import inheritly

import pytest


class TestMember:

    def test_target(self, inheritly_class):
        assert inheritly_class.method.target \
            is inheritly_class().method.__func__

    def test_decorators(self, inheritly_class, inheritly_subclass,
                        decorators):
        assert inheritly_class.method.decorators \
            == inheritly_subclass.method.decorators \
            == decorators

    def test_lru_cache(self, inheritly_class, inheritly_subclass):
        # check that sample lru_cache() decorator was really applied, and that
        # it was applied a second time in subclass
        assert inheritly_class().method.cache_clear \
            is not inheritly_subclass().method.cache_clear
