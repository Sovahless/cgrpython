# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 771,688 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Cinéma CGR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject1/img/avengers.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		m_comboBox2Choices = [ u"Avengers Endame", u"Voyage de Chihiro", u"Spiderman No Way Home", u"The Batman", u"L'affaire Collini", u"Morbius", u"Ogre", u"Abuela", u"Sonic 2", u"Le secret de la cité perdu", u"Jujutsu Kaisen 0", u"Les Barbapapa" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"Choissisez un Film", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		gSizer1.Add( self.m_comboBox2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Choisir ce Film", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.imgchange )
		self.m_button2.Bind( wx.EVT_BUTTON, self.changeframe )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def imgchange( self, event ):
		event.Skip()

	def changeframe( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Ticket pour", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Titulaire de la Carte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		fgSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_textCtrl4, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Numéro de la Carte", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.SetMaxLength( 18 )
		fgSizer2.Add( self.m_textCtrl6, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Date D'Expiration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		fgSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 12, 1 )
		fgSizer2.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrl2 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 22 )
		fgSizer2.Add( self.m_spinCtrl2, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Cryptogramme", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl8.SetMaxLength( 3 )
		fgSizer2.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"8,50€", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer2.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Payer", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button5, 0, wx.ALIGN_BOTTOM|wx.LEFT, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.saveticket )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def saveticket( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 514,504 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Merci de votre achat !\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer6.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u" Vous pouver trouver votre ticket au format pdf dans le meme dossier que le programme", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer6.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Bon Film", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer6.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject1/img/cgr.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_bitmap6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


