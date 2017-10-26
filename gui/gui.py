# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import requests
from bs4 import BeautifulSoup as bs
import lxml

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 232,169 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter Phone Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Find name", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, '', wx.DefaultPosition, wx.DefaultSize, 0 )
		#self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.findName )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def findName( self, event ):
            #print self.m_textCtrl1.GetValue()
	    r=requests.post('http://site21.way2sms.com/LocateMobile/'+self.m_textCtrl1.GetValue())
            s=bs(r.content,'html.parser')
            st=s.find('div',attrs={"id":"info"})
            data=st.find_all('p')
            list=[]
            for details in data[:len(data)-1]:
                list.append(details.text)
            self.m_staticText2.SetLabel(list[0])
app = wx.App(False) 
frame = MyFrame1(None) 
frame.SetTitle('Name Finder for Phone Number')
frame.Show(True) 
#start the applications 
app.MainLoop() 
