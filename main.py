import wx
import main_form
from switchcase import switch

currentmovie = None


class MainFrame2(main_form.MyFrame2):

    def __init__(self, parent, title):
        main_form.MyFrame2.__init__(self, parent)
        self.m_textCtrl8.SetMaxLength(3)


class MainFrame(main_form.MyFrame1):

    def __init__(self, parent, title):
        main_form.MyFrame1.__init__(self, parent)

    def fermer(self, event):
        print(event)

    def imgchange(self, event):
        imgselection = self.m_comboBox2.GetSelection()

        for case in switch(imgselection):
            if case(0):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/avengers.bmp'))
                currentmovie = "Avengers"
            if case(1):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/chihiro.bmp'))
                currentmovie = "Chihiro"
            if case(2):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/spiderman.bmp'))
                currentmovie = "Spiderman No Way Home"
            if case(3):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/batman.bmp'))
                currentmovie = "The Batman"
            if case(4):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/collini.bmp'))
                currentmovie = "L'Affaire Collini"
            if case(5):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/morbius.bmp'))
                currentmovie = "Morbius"
            if case(6):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/ogre.bmp'))
                currentmovie = "Ogre"
            if case(7):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/abuela.bmp'))
                currentmovie = "Abuela"
            if case(8):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/sonic.bmp'))
                currentmovie = "Sonic 2"
            if case(9):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/secret.bmp'))
                currentmovie = "Le secret de la cité perdu"
            if case(10):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/jujutsu.bmp'))
                currentmovie = "Jujutsu Kaisen 0"
            if case(11):
                self.m_bitmap4.SetBitmap(wx.Bitmap('img/barbapapa.bmp'))
                currentmovie = "Les Barbapapa"

    def changeframe(self, event):
        self.Destroy()
        self.MyFrame2 = MainFrame2(None, 'test')
        self.MyFrame2.Show()


class MainApp(wx.App):

    def OnInit(self):
        self.frame = MainFrame(None, "Un test de plus")

        self.SetTopWindow(self.frame)

        self.frame.Show(True)

        return True


if __name__ == "__main__":
    app = MainApp(redirect=False)
    app.MainLoop()
