# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul 15 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview


###########################################################################
## Class MainFrameView
###########################################################################

class MainFrameView(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Kicad Library Manager", pos=wx.DefaultPosition,
                          size=wx.Size(751, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_libraries = wx.dataview.DataViewTreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_libraries, 1, wx.ALL | wx.EXPAND, 5)

        bSizer2.AddSpacer((0, 0), 0, wx.FIXED_MINSIZE, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer4.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_append_lib = wx.Button(self, wx.ID_ANY, u"Append Library", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_append_lib, 0, wx.ALL, 5)

        self.m_remove_lib = wx.Button(self, wx.ID_ANY, u"Remove Library", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_remove_lib, 0, wx.ALL, 5)

        self.m_toggle_visibility = wx.Button(self, wx.ID_ANY, u"Disable Library", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_toggle_visibility, 0, wx.ALL, 5)

        self.m_update_lib = wx.Button(self, wx.ID_ANY, u"Update Library", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_update_lib, 0, wx.ALL, 5)

        bSizer4.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        bSizer2.Add(bSizer4, 0, wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        bSizer2.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_import_table = wx.Button(self, wx.ID_ANY, u"Import fp-lib-table", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_import_table, 0, wx.ALL, 5)

        self.m_export_table = wx.Button(self, wx.ID_ANY, u"Export fp-lib-table", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_export_table, 0, wx.ALL, 5)

        bSizer5.AddSpacer((0, 0), 1, wx.EXPAND, 5)

        self.m_cancle = wx.Button(self, wx.ID_ANY, u"Cancle", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_cancle, 0, wx.ALL, 5)

        self.m_ok = wx.Button(self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_ok, 0, wx.ALL, 5)

        bSizer2.Add(bSizer5, 0, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_append_lib.Bind(wx.EVT_BUTTON, self.btn_append_lib)
        self.m_remove_lib.Bind(wx.EVT_BUTTON, self.btn_remove_lib)
        self.m_toggle_visibility.Bind(wx.EVT_BUTTON, self.btn_toggle_visibility)
        self.m_update_lib.Bind(wx.EVT_BUTTON, self.btn_update_lib)
        self.m_import_table.Bind(wx.EVT_BUTTON, self.btn_import_table)
        self.m_export_table.Bind(wx.EVT_BUTTON, self.btn_export_table)
        self.m_cancle.Bind(wx.EVT_BUTTON, self.btn_cancle)
        self.m_ok.Bind(wx.EVT_BUTTON, self.btn_ok)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def btn_append_lib(self, event):
        event.Skip()

    def btn_remove_lib(self, event):
        event.Skip()

    def btn_toggle_visibility(self, event):
        event.Skip()

    def btn_update_lib(self, event):
        event.Skip()

    def btn_import_table(self, event):
        event.Skip()

    def btn_export_table(self, event):
        event.Skip()

    def btn_cancle(self, event):
        event.Skip()

    def btn_ok(self, event):
        event.Skip()


