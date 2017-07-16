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

from BaseLibrary import BaseLibrary, is_repository_dir
from LibraryNode import LibraryNode

class DirectoryLibrary(BaseLibrary):
    """Manages libraries located inside a directory"""
    def __init__(self, path):
        BaseLibrary.__init__(self)
        self.type = 'directory'

        self.path = os.path.normpath(path)  # TODO: support environment variables
        if not os.path.isdir(self.path):
            raise RuntimeError("\'{path}\' is not a directory!".format(path=self.path))

    def get_path(self):
        return self.path

    def find_libraries(self):
        # check if directory is already a library
        base_path = os.path.basename(os.path.normpath(self.path))
        if is_repository_dir(base_path):
            self.libraries.append(LibraryNode(self, '.', base_path, True))
            return

        # check if child directories are libraries
        for dir in sorted(os.walk(self.path).next()[1]):
            if is_repository_dir(dir):
                self.libraries.append(LibraryNode(self, dir, dir, True))