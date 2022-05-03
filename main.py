import wx
import main_form


class MainFrame(main_form.MyFrame3):

    def __init__(self, parent, title):
        main_form.MyFrame3.__init__(self, parent)

    def fermer(self, event):
        print(event)


class MainApp(wx.App):

    def OnInit(self):
        self.frame = MainFrame(None, "Un test de plus")

        self.SetTopWindow(self.frame)

        self.frame.Show(True)

        return True


if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()
