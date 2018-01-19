#!/usr/bin/env python2

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

import wx
import wx.dataview

from LibraryTable import LibraryTableModel, LibraryTableWidget
from library.GitLibrary import GitLibrary
from library.DirectoryLibrary import DirectoryLibrary

from gui.MainFrameView import MainFrameView


class MainFrame(MainFrameView):
    """ Show the main window of our library manager """
    def __init__(self, parent):
        MainFrameView.__init__(self, parent)

        #self.m_libraries.AppendToggleColumn("Toggle", 0)
        #self.m_libraries.AppendTextColumn("Text", 1)

        data = [True, "row 1"]
        data = wx.dataview.DataViewItem()
        self.m_libraries.AppendItem(data, "row 1")
        self.m_libraries.AppendItem(data, "row 2")

        #data = [False, "row 3"]
        #self.m_libraries.AppendItem(self.m_libraries, data)

        #self.m_libraries.AssociateModel(LibraryTableModel())

    # event handlers
    def btn_append_lib(self, event):
        item = wx.dataview.Item("asdf")
        self.m_libraries.AppendItem(self, item)


    def btn_remove_lib(self, event):
        event.Skip()

    def btn_toggle_visibility(self, event):
        event.Skip()

    def btn_update_lib(self, event):
        event.Skip()

    def btn_import_table(self, event):
        dialog = wx.FileDialog(self, "Import fp-lib-table", "", "fp-lib-table", "fp-lib-table (fp-lib-table)|fp-lib-table",
                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return  # the user changed idea...

    def btn_export_table(self, event):
        dialog = wx.FileDialog(self, "Import fp-lib-table", "", "fp-lib-table", "fp-lib-table (fp-lib-table)|fp-lib-table",
                               wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return  # the user changed idea...

    def btn_cancle(self, event):
        self.Close(True)

    def btn_ok(self, event):
        self.Close(True)


def start():
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    model = LibraryTableModel()
    print(model)

    lib = DirectoryLibrary("/home/thomas/Projekte/Kicad/packages3D/")
    lib.find_libraries()
    model.add_library(lib)

    lib = GitLibrary("/home/thomas/Projekte/Kicad/packages3D/")
    lib.find_libraries()
    model.add_library(lib)

    print(model)

    start()
