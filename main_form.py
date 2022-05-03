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

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def imgchange( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

