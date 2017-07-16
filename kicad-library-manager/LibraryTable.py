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

import wx
import wx.grid

from collections import OrderedDict


class LibraryTableModel(object):
    def __init__(self):
        self.libraries = []

    def add_library(self, library):
        self.libraries.append(library)

    def remove_library(self, library):
        return self.libraries.remove(library)

    def get_libraries(self):
        return self.libraries

    def __str__(self):
        library_strings = []

        # construct library strings
        for library in self.libraries:
            library_strings.append(library.__str__())

        return '\n'.join(library_strings)


class LibraryTableWidget(wx.grid.Grid):
    def __init__(self, parent, **kwargs):
        wx.grid.Grid.__init__(self, parent, -1, **kwargs)
        # Create a wxGrid object
        #grid = wx.grid.Grid(self, -1, size=(800,600))

        # Then we call CreateGrid to set the dimensions of the grid
        # (100 rows and 10 columns in this example)
        self.CreateGrid(100, 10)

        # We can set the sizes of individual rows and columns
        # in pixels
        self.SetRowSize(0, 60)
        self.SetColSize(0, 120)

        # And set grid cell contents as strings
        self.SetCellValue(0, 0, 'wxGrid is good')

        # We can specify that some cells are read.only
        self.SetCellValue(0, 3, 'This is read.only')
        self.SetReadOnly(0, 3)

        # Colours can be specified for grid cell contents
        self.SetCellValue(3, 3, 'green on grey')
        self.SetCellTextColour(3, 3, wx.GREEN)
        self.SetCellBackgroundColour(3, 3, wx.LIGHT_GREY)

        # We can specify the some cells will store numeric
        # values rather than strings. Here we set grid column 5
        # to hold floating point values displayed with width of 6
        # and precision of 2
        self.SetColFormatFloat(5, 6, 2)
        self.SetCellValue(0, 6, '3.1415')