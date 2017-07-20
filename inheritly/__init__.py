# @inheritly >>> make MORE stuff inheritable in Python classes
#
# Copyright (C) 2017 Stefan Zimmermann <user@zimmermann.co>
#
# @inheritly is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# @inheritly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with @inheritly.  If not, see <http://www.gnu.org/licenses/>.

"""
``inheritly`` top-level

.. moduleauthor:: Stefan Zimmermann <user@zimmermann.co>
"""

import sys
from functools import partial
from types import ModuleType

from .meta import meta
from .member import member

__all__ = ['object', 'meta', 'member']

__version__ = '0.1.0.dev'


class object(metaclass=meta):
    """
    Base class for ``inheritly`` classes

    Allows use of ``@inheritly(*decorators)`` for method definitions to
    make override methods of derived classes automagically inherit the given
    ``decorators``

    See :class:`inheritly.Module` for more details and usage examples
    """


#: Store original module
ORIGIN = sys.modules[__name__]


class Module(ModuleType):
    """
    Wrapper for ``inheritly`` top-level module

    Makes it directly usable as ``@inheritly`` decorator:

    >>> import inheritly

    Which takes a variable argument list of actual decorators to apply:

    >>> from functools import lru_cache

    >>> class Base(inheritly.object):
    ...
    ...     @inheritly(lru_cache())
    ...     def method(self, x):
    ...         return x * 3

    >>> Base.method
    <inheritly.member 'method'>

    The :class:`inheritly.member` instance behaves like the original member
    ...:

    >>> Base().method(5)
    15

    ... but turns every override method into a :class:`inheritly.member`
    instance again, and auto-applies all decorators given to `@inheritly(...)`
    in the base class:

    >>> class Sub(Base):
    ...
    ...     def method(self, x):
    ...         return x * 7

    >>> Sub.method.decorators
    (<function lru_cache... at ...>,)

    >>> Sub().method(5)
    35

    If you should forget the :class:`inheritly.object` base, you will get
    warned when trying to use any :class:`inheritly.member` instance:

    >>> class Bad:
    ...
    ...     @inheritly(property)
    ...     def useless(self):
    ...         pass

    >>> Bad().useless
    Traceback (most recent call last):
      ...
    TypeError: can't access <inheritly.member 'useless'> ...
    """

    def __init__(self):
        super().__init__(__name__)
        self.__dict__.update(ORIGIN.__dict__)

    def __getattr__(self, name):
        return getattr(ORIGIN, name)

    def __call__(self, *decorators):
        return partial(member, decorators=decorators)


sys.modules[__name__] = Module()
