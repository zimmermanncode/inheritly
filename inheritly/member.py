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
``inheritly.member`` class definition

.. moduleauthor:: Stefan Zimmermann <user@zimmermann.co>
"""

import inheritly

__all__ = ['member']


class member:
    """
    The result type of the ``@inheritly`` decorator
    """

    def __init__(self, func, decorators):
        """
        Decorates method `func` with all given `decorators`

        Order is from last to first, like when specifying multiple
        ``@decorator``s
        """
        #: Name of original method function
        self.__name__ = func.__name__
        for deco in reversed(decorators):
            func = deco(func)
        #: Result of applying all given decorators to original function
        self.target = func
        #: Store tuple of given decorators that were applied to original
        #  method  function, to make them get inherited by override methods
        #  in derived inheritly.object classes
        self.decorators = decorators

    def __get__(self, obj, owner):
        """
        Get :class:`member` instance from :class:`inheritly.object` classes
        and the decorated targets from and bound to their instances

        :raises TypeError: if accessed from an instance of a
                           non-``inheritly.object``-derived class
        """
        if obj is None:
            return self

        if not isinstance(owner, inheritly.meta):
            raise TypeError("can't access {!r} from non-inheritly {!r}"
                            .format(self, owner))

        return self.target.__get__(obj, owner)

    def __repr__(self):
        """
        ``<inheritly.member 'name'>``
        """
        return "<inheritly.member {!r}>".format(self.__name__)
