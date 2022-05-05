import wx
import main_form
import mysql.connector
from fpdf import FPDF
from switchcase import switch

#connection a la db
dbcgr = mysql.connector.connect(user='root', password='',
                                host='127.0.0.1',
                                database='cgr')
dbcgr.autocommit = True
cgrcursor = dbcgr.cursor()

cgrcursor.execute("SELECT idTickets FROM tickets")
fetchticket = cgrcursor.fetchall()

cgrcursor.execute("SELECT place_Prise FROM salle")
fetchplace = cgrcursor.fetchall()
placesalle1 = fetchplace[0]
placesalle2 = fetchplace[1]
placesalle3 = fetchplace[2]
placesalle4 = fetchplace[3]
placesalle5 = fetchplace[4]
placesalle6 = fetchplace[5]
placesalle7 = fetchplace[6]
placesalle8 = fetchplace[7]
placesalle9 = fetchplace[8]
placesalle10 = fetchplace[9]
placesalle11 = fetchplace[10]
placesalle12 = fetchplace[11]
placesalle1 = int(placesalle1[0])
placesalle2 = int(placesalle2[0])
placesalle3 = int(placesalle3[0])
placesalle4 = int(placesalle4[0])
placesalle5 = int(placesalle5[0])
placesalle6 = int(placesalle6[0])
placesalle7 = int(placesalle7[0])
placesalle8 = int(placesalle8[0])
placesalle9 = int(placesalle9[0])
placesalle10 = int(placesalle10[0])
placesalle11 = int(placesalle11[0])
placesalle12 = int(placesalle12[0])

currentmovie = None

class MainFrame3(main_form.MyFrame1):

    def __init__(self, parent, title):
        main_form.MyFrame3.__init__(self, parent)


class MainFrame2(main_form.MyFrame2):

    def __init__(self, parent, title):
        main_form.MyFrame2.__init__(self, parent)
        self.m_staticText11.SetLabel("Ticket pour " + currentmovie)

    # Enregistre le ticket du client dans la db, le crée le ticket en pdf et affiche la prochaine frame
    def saveticket(self, event):
        ticketname = self.m_textCtrl4.GetValue()
        sql = f"INSERT INTO tickets (Prix, idSalle, idFilm, Nom) VALUES (8.50, {currentmovieid}, {currentmovieid}, '{ticketname}')"
        val = (max(fetchticket), 8.50, currentmovieid, currentmovieid, self.m_textCtrl4.GetValue())
        cgrcursor.execute(sql)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, ticketname, 0, 1)
        pdf.cell(40, 10, "Ticket pour voir " + currentmovie, 0, 1)
        pdf.image('img/cgr2.png', 20, 40, 40)
        pdf.output('Ticket.pdf', 'F')
        self.Destroy()
        self.MyFrame3 = MainFrame3(None, 'test')
        self.MyFrame3.Show()


class MainFrame(main_form.MyFrame1):

    def __init__(self, parent, title):
        main_form.MyFrame1.__init__(self, parent)

    def fermer(self, event):
        print(event)

    #Verifie la selection du combobox et change l'image, verifie si la salle est pleine et empeche de continuer si c'est le cas
    def imgchange(self, event):
        imgselection = self.m_comboBox2.GetSelection()
        global currentmovie
        global currentmovieid

        for case in switch(imgselection):
            if case(0):
                if placesalle1 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/avengers.bmp'))
                    currentmovie = "Avengers Endgame"
                    currentmovieid = 1
            if case(1):
                if placesalle2 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/chihiro.bmp'))
                    currentmovie = "Le Voyage de Chihiro"
                    currentmovieid = 2
            if case(2):
                if placesalle3 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/spiderman.bmp'))
                    currentmovie = "Spiderman No Way Home"
                    currentmovieid = 3
            if case(3):
                if placesalle4 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/batman.bmp'))
                    currentmovie = "The Batman"
                    currentmovieid = 4
            if case(4):
                if placesalle5 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/collini.bmp'))
                    currentmovie = "L'Affaire Collini"
                    currentmovieid = 5
            if case(5):
                if placesalle6 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/morbius.bmp'))
                    currentmovie = "Morbius"
                    currentmovieid = 6
            if case(6):
                if placesalle7 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/ogre.bmp'))
                    currentmovie = "Ogre"
                    currentmovieid = 7
            if case(7):
                if placesalle8 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/abuela.bmp'))
                    currentmovie = "Abuela"
                    currentmovieid = 8
            if case(8):
                if placesalle9 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/sonic.bmp'))
                    currentmovie = "Sonic 2"
                    currentmovieid = 9
            if case(9):
                if placesalle10 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/secret.bmp'))
                    currentmovie = "Le secret de la cité perdu"
                    currentmovieid = 10
            if case(10):
                if placesalle11 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/jujutsu.bmp'))
                    currentmovie = "Jujutsu Kaisen 0"
                    currentmovieid = 11
            if case(11):
                if placesalle12 >= 300:
                    wx.MessageBox("Seance Pleine", 'Info', wx.OK | wx.ICON_INFORMATION)
                    print(currentmovie)
                else:
                    self.m_bitmap4.SetBitmap(wx.Bitmap('img/barbapapa.bmp'))
                    currentmovie = "Les Barbapapa"
                    currentmovieid = 12

#Verifie qu'un film a etait selectionner et passe a la fenetre suivante
    def changeframe(self, event):
        if currentmovie == None:
            pass
        else:
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
