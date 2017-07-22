from functools import lru_cache

import inheritly

import pytest


class TestInheritly:

    def test_non_inheritly_object(self):

        class Error:

            @inheritly(lru_cache())
            def method(self):  # pragma: no cover
                pass

        with pytest.raises(TypeError) as exc:
            Error().method
        exc.match(r"^can't access <inheritly.member 'method'>"
                  r" from non-inheritly <class '[^']*Error'>$")
