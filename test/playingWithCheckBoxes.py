import wx
import wx.lib.scrolledpanel
import wx.grid as grd


output_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
colLabels = {"machine 1", "machine 2", "machine 3", "machine 4", "machine 5", "machine 6", "machine 7",
             "machine 8", "machine 9", "machine 10", "machine 11", "machine 12", "machine 13", "machine 14"}


class GUI(wx.Frame):

    def __init__(self, parent, id, title):
        # Create a frame
        self.main_panel = wx.Frame.__init__(self, parent, id, size=(1200, 650))
        self.the_panel = wx.lib.scrolledpanel.ScrolledPanel(self.main_panel, -1)
        the_box = wx.BoxSizer(wx.VERTICAL)
        self.main_panel.SetSizer(the_box)
        self.main_panel.SetupScrolling()

        panel4 = wx.Panel(self, -1, size=(250, 460), pos=(840, 140), style=wx.SIMPLE_BORDER)

############################################
        # checkboxpanel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(250, 400), pos=(840, 200),
        #                                                    style=wx.SIMPLE_BORDER)
        # bSizer3 = wx.BoxSizer(wx.VERTICAL)
        # bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        # panel4.SetBackgroundColour('#FFFFFF')
        # panel4.SetSizer(bSizer3)
        # panel4.SetupScrolling()
        # y = 0
        # y1 = 0
        # for i in range(0, (len(output_list))):
        #     self.checkbox_1 = wx.CheckBox(panel4, label='', pos=(23 + y, 10))
        #
        #     # bSizer3.Add(checkbox_1, 0, wx.ALL, 25)
        #     y = y + 50
        #
        # for i in range(0, (len(output_list))):
        #     self.checkbox_2 = wx.CheckBox(panel4, label='', pos=(23, 40 + y1))
        #     # bSizer4.Add(checkbox_2, 0, wx.ALL, 25)
        #     y1 = y1 + 30
#############################################
        panel2 = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(800, 400), pos=(20, 200),
                                                    style=wx.SIMPLE_BORDER)
        bSizer = wx.BoxSizer(wx.VERTICAL)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
        panel2.SetSizer(bSizer)
        sampleList = ["Glyphworks", "PDF", "Random 1", "Random 2"]
        x = 0
        for i in range(0, (len(output_list))):
            remove_btn1 = wx.Button(panel2, label="Remove", pos=(20, 20 + x), size=(80, 30))
            official_list1 = wx.ListBox(panel2, -1, (110, 10 + x), (500, 30), output_list, wx.LB_SINGLE)
            wx.Choice(panel2, -1, (650, 10 + x), (90, 40), choices=sampleList)  # pos , then size
            x = x + 40
            bSizer.Add(remove_btn1, 0, wx.ALL, 5)
        official_list1
#############################################
        panel1 = wx.lib.scrolledpanel.ScrolledPanel(self, size=(800, 150), pos=(20, 50),
                                                    style=wx.SIMPLE_BORDER)
        panel1.SetBackgroundColour('#FFFFFF')
        process_button = wx.Button(panel1, label="Process", pos=(225, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.process_button, process_button)

        done_button = wx.Button(panel1, label="Done", pos=(400, 30), size=(150, 40))
        self.Bind(wx.EVT_BUTTON, self.done_button, done_button)
        text_process = wx.StaticText(panel1, -1, "Process", pos=(50, 100), size=(260, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_process.SetFont(font)
        text_processor = wx.StaticText(panel1, -1, "Processor", pos=(600, 100), size=(240, -1))
        font = wx.Font(18, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        text_processor.SetFont(font)

    def close_button(self, event):
        self.Close(True)

    def close_window(self, event):
        self.Destroy()

    def process_button(self, event):
        """#something awesome happens here"""

    def done_button(self, event: object) -> object:
        """pretty much self evident, what do you think it means?"""


if __name__ == '__main__':
    app = wx.App()
    frame = GUI(parent=None, id=-1, title="Test")
    frame.Show()
    app.MainLoop()