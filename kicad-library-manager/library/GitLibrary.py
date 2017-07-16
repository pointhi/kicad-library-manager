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
import pygit2

from DirectoryLibrary import DirectoryLibrary


class GitLibrary(DirectoryLibrary):
    """Manages libraries located inside a git repository"""
    def __init__(self, path):
        DirectoryLibrary.__init__(self, path)
        self.type = 'git'

        # check if given path contains a git repository
        try:
            self.repository_path = pygit2.discover_repository(self.path)
        except KeyError:
            raise RuntimeError("\'{path}\' doesn't seem to be a git repository!".format(path=self.path))

        # create repository field
        self.repo = pygit2.Repository(self.repository_path)

        # check if given path equals with the working dir of the git repo
        if not os.path.samefile(self.path, self.repo.workdir):
            raise RuntimeError("\'{path}\' does not point into the working directory of the git repository!".format(path=self.path))

    def get_repo(self):
        return self.repo
