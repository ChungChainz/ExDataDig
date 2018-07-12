#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Mon Jun 18 08:07:07 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((863, 300))
        self.button_15 = wx.Button(self, wx.ID_ANY, "button_15", style=wx.BU_BOTTOM | wx.BU_LEFT | wx.BU_RIGHT | wx.BU_TOP)
        self.list_box_2 = wx.ListBox(self, wx.ID_ANY, choices=["c"])
        self.combo_box_2 = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, "")
        self.window_1 = wx.SplitterWindow(self, wx.ID_ANY)
        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)
        self.slider_1 = wx.Slider(self, wx.ID_ANY, 0, 0, 10)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        self.list_box_2.SetMinSize((100, 25))
        self.window_1.SetMinimumPaneSize(20)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.FlexGridSizer(1, 1, 0, 0)
        grid_sizer_2 = wx.FlexGridSizer(0, 1, 0, 0)
        grid_sizer_4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "grid_sizer_4"), wx.VERTICAL)
        grid_sizer_3 = wx.GridSizer(0, 5, 0, 0)
        grid_sizer_2.Add((0, 0), 0, 0, 0)
        grid_sizer_3.Add(self.button_15, 0, wx.ALIGN_CENTER | wx.LEFT, 0)
        grid_sizer_3.Add(self.list_box_2, 0, 0, 0)
        grid_sizer_3.Add(self.combo_box_2, 0, 0, 0)
        grid_sizer_3.Add(self.checkbox_1, 0, 0, 0)
        self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2)
        grid_sizer_3.Add(self.window_1, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_4.Add(self.slider_1, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_2, 2, wx.ALL | wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()