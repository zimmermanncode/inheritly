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
``inheritly.meta`` class definition

.. moduleauthor:: Stefan Zimmermann <user@zimmermann.co>
"""

from inspect import getmembers

from .member import member as inheritly_member

__all__ = ['meta']


class meta(type):
    """
    Metaclass for basic :class:`inheritly.object`
    """

    def __new__(mcs, clsname, bases, clsattrs):
        """
        Looks for :class:`inheritly.member` instances in `bases` and applies
        their decorators to override functions
        """
        # make sure to always get the wrapped module object
        import inheritly

        inheritly_members = dict(set(
            (name, m) for b in bases for name, m in getmembers(b)
            if isinstance(m, inheritly_member)))

        for name, member in list(clsattrs.items()):
            base_m = inheritly_members.get(name)
            if base_m is not None:
                clsattrs[name] = inheritly(*base_m.decorators)(member)

        return type.__new__(mcs, clsname, bases, clsattrs)
