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


class BaseLibrary(object):
    def __init__(self):
        self.type = None
        self.description = ''
        self.libraries = []

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

    def get_path(self):
        raise NotImplementedError

    def get_libraries(self):
        return self.libraries

    def __str__(self):
        ret_str = '* {type}:(\'{path}\')'.format(type=self.get_type(), path=self.get_path())
        for lib in self.get_libraries():
            ret_str += '\n  - ' + lib.__str__()
        return ret_str


def is_repository_dir(directory):
    return str(directory).endswith('.pretty') or\
           str(directory).endswith('.3dshapes') or\
           str(directory).endswith('.sweet')