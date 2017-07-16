# kicad-library-manager is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kicad-library-manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kicad-library-manager. If not, see < http://www.gnu.org/licenses/ >.
#
# (C) 2017 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>

import os


class LibraryNode(object):
    """Represents a single library as it is managed by Kicad"""
    def __init__(self, parent, path, nickname, enabled):
        self.parent = parent
        self.path = path
        self.nickname = nickname
        self.enabled = enabled

    def __str__(self):
        lib_path = os.path.normpath(os.path.join(self.parent.get_path(), self.path))
        return '{name} (\'{path}\')'.format(name=self.nickname, path=lib_path)