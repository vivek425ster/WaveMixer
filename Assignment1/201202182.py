#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
from Tkinter import Canvas, Frame, Tk, BOTH, Text, Menu, END,W,Button,FLAT,TOP
import tkFileDialog 
import pyaudio
import wave 
import struct
import sys
import os
import signal
class Example(Frame):
    chunk=1024 
    def __init__(self, parent):
        Frame.__init__(self, parent)    
        self.parent = parent        
        self.makeui(self.parent)
	  
    def makeui(self,root):
	self.pid1 = 0		# wave 1
	self.pid2 = 0		# wave 2
	self.pid3 = 0		# wave 3
	self.pid4 = 0           # modulate
	self.pid5 = 0		# mix
	self.pause_flag1 = 0
	self.pause_flag2 = 0
	self.pause_flag3 = 0
	self.pause_flag4 = 0
	self.pause_flag5 = 0

        self.parent.title("Wave Mixture")
        self.pack(fill=BOTH, expand=1)
	
	#CANVAS
	canvas=Canvas(self,width=800,height=50)

       	#main heading
	canvas.create_text(200, 30, anchor=W, font=("Purisa",50),
            text="Wave Mixer")

	#create line
	canvas.create_line(0,50,800,50)
	#close canvas
	canvas.pack(fill=BOTH)

	#----------------------------------------First Frame ---------------------------#
	frame=LabelFrame(self,text="Wave1",fg="blue",bg="green",font=("Pursia",15)) 
	frame.pack(side=LEFT,fill=None,expand=True)  



	#Select Button 
	self.button = Button(frame, text="Select File", fg="white",bg="black",command=self.onopen1) 
	self.button.pack(side=TOP)  

	self.name1=Label(frame,text='No File',bg="green",fg="black") 
	self.name1.pack(side=TOP)


	#Amplitude Scale 
	amp1=DoubleVar() 
	self.amp11=Scale(frame,label="Amplitude",from_=0,to=5,resolution=0.1,variable=amp1,orient=HORIZONTAL) 
	self.amp11.set(1)
	self.amp11.pack(side=TOP)
 
	#timeshift Scale 
	time1=DoubleVar() 
	self.time11=Scale(frame,label="Time Shift",from_=-1,to=1,resolution=0.1,variable=time1,orient=HORIZONTAL) 
	self.time11.pack(side=TOP) 

	#timescale Scale 
	time_scale1=DoubleVar() 
	self.time_scale11=Scale(frame,label="Time Scaling",from_=0,to=8,resolution=0.01,variable=time_scale1,orient=HORIZONTAL) 
	self.time_scale11.pack(side=TOP)
 
	#Time Reversal 
	self.time_reversal1=IntVar()
#	print self..get()
	self.time_reversal11=Checkbutton(frame,text="Time Reversal",bg="grey",variable=self.time_reversal1,onvalue=1,offvalue=0,height=3,width=20) 	
	self.time_reversal11.pack(side=TOP) 

	#Modulation 
	self.mod1=IntVar() 
	self.mod11=Checkbutton(frame,text="Select for Modulation",bg="grey",variable=self.mod1,onvalue=1,offvalue=0,height=3,width=20) 
	self.mod11.pack(side=TOP) 


	#Mixing 
	self.mix1=IntVar() 
	self.mix11=Checkbutton(frame,text="Select for Mixing",bg="grey",variable=self.mix1,onvalue=1,offvalue=0,height=3,width=20) 
	self.mix11.pack(side=TOP)

	self.button = Button(frame, text="Play", fg="white",bg="red",command=self.readfile1) 
	self.button.pack(side=TOP) 

	self.button = Button(frame, text="Pause", fg="white",bg="brown",command=self.pause_1) 
	self.button.pack(side=TOP)
 



	
	#-----------------------------_Second Frame --------------------------------------#
	
	frame=LabelFrame(self,width=300,height=300,text="Wave2",fg="Blue",bg="green",font=("Pursia",15)) 
	frame.pack(side=LEFT,fill=None,expand=True)  



	#Select Button 
	self.button = Button(frame, text="Select File", fg="white",bg="black",command=self.onopen2) 
	self.button.pack(side=TOP) 

	self.name2=Label(frame,text='No File',bg="green",fg="black") 
	self.name2.pack(side=TOP)		
	
	#Amplitude Scale 
	amp2=DoubleVar()
	self.amp22=Scale(frame,label="Amplitude",from_=0,to=5,resolution=0.1,variable=amp2,orient=HORIZONTAL) 
	self.amp22.set(1)
	self.amp22.pack(side=TOP) 
	
	#timeshift Scale 
	time2=DoubleVar() 
	self.time22=Scale(frame,label="Time Shift",from_=-1,to=1,resolution=0.1,variable=time2,orient=HORIZONTAL) 
	self.time22.pack(side=TOP) 
	
	#timescale Scale 
	time_scale2=DoubleVar() 
	self.time_scale22=Scale(frame,label="Time Scaling",from_=0,to=8,resolution=0.01,variable=time_scale2,orient=HORIZONTAL) 	    
	self.time_scale22.pack(side=TOP) 
	
	#Time Reversal 
	self.time_reversal2=IntVar() 
	self.time_reversal22=Checkbutton(frame,text="Time Reversal",bg="grey",variable=self.time_reversal2,onvalue=1,offvalue=0,height=3,width=20) 
	self.time_reversal22.pack(side=TOP) 
	
	#Modulation 
	self.mod2=IntVar() 
	self.mod22=Checkbutton(frame,text="Select for Modulation",bg="grey",variable=self.mod2,onvalue=1,offvalue=0,height=3,width=20) 
	self.mod22.pack(side=TOP) 

	#Mixing 
	self.mix2=IntVar() 
	self.mix22=Checkbutton(frame,text="Select for Mixing",bg="grey",variable=self.mix2,onvalue=1,offvalue=0,height=3,width=20) 
	self.mix22.pack(side=TOP)

	self.button = Button(frame, text="Play", fg="white",bg="red",command=self.readfile2) 
	self.button.pack(side=TOP) 

	self.button = Button(frame, text="Pause", fg="white",bg="brown",command=self.pause_2) 
	self.button.pack(side=TOP)

	#----------------------------------------Third Frame ---------------------------#
	frame=LabelFrame(self,width=300,height=300,text="Wave3",fg="blue",bg="green",font=("Pursia",15)) 
	frame.pack(side=LEFT,fill=None,expand=True)  


	#Select File Button 
	self.button = Button(frame, text="Select File", fg="white",bg="black",command=self.onopen3) 
	self.button.pack(side=TOP) 

	self.name3=Label(frame,text='No File',bg="green",fg="black") 
	self.name3.pack(side=TOP)

	#Amplitude Scale 
	amp3=DoubleVar() 
	self.amp33=Scale(frame,label="Amplitude",variable=amp3,from_=0,to=5,resolution=0.1,orient=HORIZONTAL)
 
	self.amp33.set(1)
	self.amp33.pack(side=TOP) 

	#timeshift Scale 
	time3=DoubleVar() 
	self.time33=Scale(frame,label="Time Shift",variable=time3,from_=-1,to=1,resolution=0.1,orient=HORIZONTAL) 
	self.time33.pack(side=TOP) 

	#timescale Scale 
	time_scale3=DoubleVar() 
	self.time_scale33=Scale(frame,label="Time Scaling",variable=time_scale3,from_=0,to=8,resolution=0.01,orient=HORIZONTAL) 
	self.time_scale33.pack(side=TOP) 

	#Time Reversal 
	self.time_reversal3=IntVar() 
	self.time_reversal33=Checkbutton(frame,text="Time Reversal",bg="grey",variable=self.time_reversal3,onvalue=1,offvalue=0,height=3,width=20) 
	self.time_reversal33.pack(side=TOP) 

	#Modulation 
	self.mod3=IntVar() 
	self.mod33=Checkbutton(frame,text="Select for Modulation",bg="grey",variable=self.mod3,onvalue=1,offvalue=0,height=3,width=20) 
	self.mod33.pack(side=TOP) 

	#Mixing 
	self.mix3=IntVar() 
	self.mix33=Checkbutton(frame,text="Select for Mixing",bg="grey",variable=self.mix3,onvalue=1,offvalue=0,height=3,width=20) 
	self.mix33.pack(side=TOP)
	
	self.button = Button(frame, text="Play", fg="white",bg="red",command=self.readfile3) 
	self.button.pack(side=TOP) 

	self.button = Button(frame, text="Pause", fg="white",bg="brown",command=self.pause_3) 
	self.button.pack(side=TOP)

	self.mix_but=Button(self,text="Mix",bg="gold",command=self.mix) 
	self.mix_but.pack() 
	self.mix_but.place(x=260,y=680)

	self.button=Button(self,text="Pause",bg="green",command=self.pause_4) 
	self.button.pack() 
	self.button.place(x=320,y=680)

	self.mod_but=Button(self,text="Modulate",bg="gold",command=self.modulate) 
	self.mod_but.pack() 
	self.mod_but.place(x=460,y=680)
	
	self.button=Button(self,text="Pause",bg="green",command=self.pause_5) 
	self.button.pack() 
	self.button.place(x=550,y=680)

	self.mod_but=Button(self,text="Record",bg="blue",command=self.record) 
	self.mod_but.pack() 
	self.mod_but.place(x=390,y=720)

	self.pl1=0
	self.pl2=0
	self.pl3=0
        
###-----------------------function to be called when we click on select file------------------------####

## this function is called when we click on the first select button ##
    def onopen1(self):
        ftypes = [('Wave files', '*.wav'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
        self.fl1 = dlg.show()
	self.name1['text']=os.path.basename(self.fl1)

## this function is called when we click on the second select button ##
    def onopen2(self):
        ftypes = [('Wave files', '*.wav'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
	self.fl2 = dlg.show()
	self.name2['text']=os.path.basename(self.fl2)


## this function is called when we click on the second select button ##
    def onopen3(self):
        ftypes = [('Wave files', '*.wav'), ('All files', '*')]
        dlg = tkFileDialog.Open(self, filetypes = ftypes)
	self.fl3 = dlg.show()
	self.name3['text']=os.path.basename(self.fl3)


##  this function converts the 1st file into list   ##
    def readfile1(self):
        file_input = wave.open(self.fl1, 'rb')
	self.channel1 = file_input.getnchannels()
	self.rate1 = file_input.getframerate()
	self.width1 = file_input.getsampwidth()
	self.frames1 = file_input.getnframes()

	self.data = file_input.readframes( self.frames1 ) # Returns byte data
	file_input.close()
	self.samples1 = self.frames1 * self.channel1
	if self.width1 == 1: 
       		fmt = "%iB" % self.samples1 # read unsigned chars
    	elif self.width1 == 2:
        	fmt = "%ih" % self.samples1 # read signed 2 byte shorts
    	else:
       	 	raise ValueError("Only supports 8 and 16 bit audio formats.")
	self.list_data = list(struct.unpack(fmt, self.data))

	self.max_amp = 32767
	self.min_amp = -32768
	self.new=[]
	for i  in xrange(len(self.list_data)):
		self.new.append(self.list_data[i])
	self.amplify_1()
	self.shift_1()
	self.scaling_1()
	if self.time_reversal1.get()==1:
		self.reverse_1()
	self.pack1()


##  this function converts the 2nd file into list   ##
    def readfile2(self):
        file_input = wave.open(self.fl2, 'rb')
	self.channel2 = file_input.getnchannels()
	self.rate2 = file_input.getframerate()
	self.width2 = file_input.getsampwidth()
	self.frames2 = file_input.getnframes()

	self.data = file_input.readframes( self.frames2 ) # Returns byte data
	file_input.close()
	self.samples2 = self.frames2 * self.channel2
	if self.width2 == 1: 
       		fmt = "%iB" % self.samples2 # read unsigned chars
    	elif self.width2 == 2:
        	fmt = "%ih" % self.samples2 # read signed 2 byte shorts
    	else:
       	 	raise ValueError("Only supports 8 and 16 bit audio formats.")
	self.list_data = list(struct.unpack(fmt, self.data))

	self.max_amp = 32767
	self.min_amp = -32768
	self.new2=[]
	for i  in xrange(len(self.list_data)):
		self.new2.append(self.list_data[i])
	self.amplify_2()
	self.shift_2()
	self.scaling_2()
	if self.time_reversal2.get()==1:
		self.reverse_2()
	self.pack2()

##  this function converts the 3rd file into list   ##
    def readfile3(self):
        file_input = wave.open(self.fl3, 'rb')
	self.channel3 = file_input.getnchannels()
	self.rate3 = file_input.getframerate()
	self.width3 = file_input.getsampwidth()
	self.frames3 = file_input.getnframes()

	self.data = file_input.readframes( self.frames3 ) # Returns byte data
	file_input.close()
	self.samples3 = self.frames3 * self.channel3
	if self.width3 == 1: 
       		fmt = "%iB" % self.samples3 # read unsigned chars
    	elif self.width3 == 2:
        	fmt = "%ih" % self.samples3 # read signed 2 byte shorts
    	else:
       	 	raise ValueError("Only supports 8 and 16 bit audio formats.")
	self.list_data = list(struct.unpack(fmt, self.data))

	self.max_amp = 32767
	self.min_amp = -32768
	self.new3=[]
	for i  in xrange(len(self.list_data)):
		self.new3.append(self.list_data[i])
	self.amplify_3()
	self.shift_3()
	self.scaling_3()
	if self.time_reversal3.get()==1:
		self.reverse_3()
	self.pack3()



## this function changes the amplitude of the given file selected in case1 ##
    def amplify_1(self):	
	#print self.scale11.get()
	for i in xrange(len(self.list_data)):
		k=self.list_data[i]*self.amp11.get()
		if k > self.max_amp:
			self.new[i] = self.max_amp
		elif k < self.min_amp:
			self.new[i] = self.min_amp
		else:
			self.new[i] = k


## this function is called for reversal of 1st wave ## 
    def reverse_1(self):
	if self.channel1 == 1:
		self.new.reverse()
	else:
		self.new.reverse()
		for i in xrange(len(self.new) - 1):
			t = self.new[i+1]
			self.new[i+1] = self.new[i]
			self.new[i] = t

## this function is called for shifting of 1st wave ##
    def shift_1(self):
		fact=self.time11.get()
		fra_shift = int(abs(fact) * self.rate1)
		a=[]
		if(fact > 0):
			if(self.channel1 == 1):
				for i in range(fra_shift):
					a.append(0)
				self.new=a+self.new
			else:
				for i in range(2*fra_shift):
					a.append(0)
				self.new=a+self.new
				
		else:
			if(self.channel1 == 1):
				self.new=self.new[fra_shift::1]
			else:
				self.new=self.new[2*fra_shift::1]

		self.frames1 = len(self.new)/self.channel1

## this function is called for scaling of 1st wave ##
    def scaling_1(self):
		a=[]
		
		fact=self.time_scale11.get()
		print self.time_scale11.get()
		if(self.time_scale11.get() == 0):
			fact=1
		
		if self.channel1 == 1:	
			k=int(len(self.new)/fact)
			for i in range(k):
				a.append(self.new[int(fact*i) ])
		else:
			e_li=[]
			o_li=[]
			for i in range( len(self.new) ):
				if(i%2 == 0):
					e_li.append(self.new[i])
				else:
					o_li.append(self.new[i])
			k=int(len(e_li)/fact)
			for i in range(k):
				a.append(e_li[ int(fact*i) ])
				a.append(o_li[ int(fact*i) ])
		
		self.new = a			
		self.frames1 = len(self.new)/self.channel1


## this function creates the new file with the given changes ##
    def pack1(self):
	if self.width1==1: 
		fmt="%iB" % self.frames1*self.channel1 
	else: 
		fmt="%ih" % self.frames1*self.channel1

	out=struct.pack(fmt,*(self.new))
	
	if self.pl1==0 or self.pl1==3:
		out_file=wave.open("ampli.wav",'w')
	elif self.pl1==1:
		out_file=wave.open("wave_mix1.wav","w")
	elif self.pl1==2:
		out_file=wave.open("wave_mod1.wav",'w')
	out_file.setframerate(self.rate1) 
	out_file.setnframes(self.frames1) 
	out_file.setsampwidth(self.width1) 
	out_file.setnchannels(self.channel1) 
	out_file.writeframes(out) 

	out_file.close()
	if self.pl1==0:
		self.read_new("ampli.wav",0)
	elif self.pl1==1:	
		self.read_new("wave_mix1.wav",4)
		self.pl1=0
	elif self.pl1==2:
		self.read_new("wave_mod1.wav",3)
		self.pl1=0
	else:
		self.pl1=0

    def amplify_2(self):	
	#print self.scale11.get()
	for i in xrange(len(self.new2)):
		k=self.new2[i]*self.amp22.get()
		if k > self.max_amp:
			self.new2[i] = self.max_amp
		elif k < self.min_amp:
			self.new2[i] = self.min_amp
		else:
			self.new2[i] = k


## this function is called for reversal of 1st wave ## 
    def reverse_2(self):
	if self.channel2 == 1:
		self.new2.reverse()
	else:
		self.new2.reverse()
		for i in xrange(len(self.new2) - 1):
			t = self.new2[i+1]
			self.new2[i+1] = self.new2[i]
			self.new2[i] = t

## this function is called for shifting of 1st wave ##
    def shift_2(self):
		fact=self.time22.get()
		fra_shift = int(abs(fact) * self.rate2)
		
		if(fact > 0):
			if(self.channel2 == 1):
				for i in range(fra_shift):
					self.new2.insert(0,0)
			else:
				for i in range(2*fra_shift):
					self.new2.insert(0,0)
				
		else:
			if(self.channel2 == 1):
				self.new2=self.new2[fra_shift::1]
			else:
				self.new2=self.new2[2*fra_shift::1]

		self.frames2 = len(self.new2)/self.channel2

## this function is called for scaling of 1st wave ##
    def scaling_2(self):
		a=[]
		
		fact=self.time_scale22.get()
		print self.time_scale22.get()
		if(self.time_scale22.get() == 0):
			fact=1
		
		if self.channel2 == 1:	
			k=int(len(self.new2)/fact)
			for i in range(k):
				a.append(self.new2[int(fact*i) ])
		else:
			e_li=[]
			o_li=[]
			for i in range( len(self.new2) ):
				if(i%2 == 0):
					e_li.append(self.new2[i])
				else:
					o_li.append(self.new2[i])
			k=int(len(e_li)/fact)
			for i in range(k):
				a.append(e_li[ int(fact*i) ])
				a.append(o_li[ int(fact*i) ])
		
		self.new2 = a			
		self.frames2 = len(self.new2)/self.channel2


## this function creates the new file with the given changes ##
    def pack2(self):
	if self.width2==1: 
		fmt="%iB" % self.frames2*self.channel2 
	else: 
		fmt="%ih" % self.frames2*self.channel2

	out=struct.pack(fmt,*(self.new2))
	if self.pl2==0 or self.pl2==3:
		out_file=wave.open("ampli2.wav",'w')
	elif self.pl2==1:
		out_file=wave.open("wave_mix2.wav",'w')
	elif self.pl2==2:
		out_file=wave.open("wave_mod2.wav",'w')

	out_file.setframerate(self.rate2) 
	out_file.setnframes(self.frames2) 
	out_file.setsampwidth(self.width2) 
	out_file.setnchannels(self.channel2) 
	out_file.writeframes(out) 

	out_file.close()
	if self.pl2==0:
		self.read_new("ampli2.wav",1)
	elif self.pl2==1:
		self.read_new("wave_mix2.wav",4)
		self.pl2=0
	elif self.pl2==2:
		self.read_new("wave_mod2.wav",3)
		self.pl2=0
	else:
		self.pl2=0


    def amplify_3(self):	
	#print self.scale11.get()
	for i in xrange(len(self.new3)):
		k=self.new3[i]*self.amp33.get()
		if k > self.max_amp:
			self.new3[i] = self.max_amp
		elif k < self.min_amp:
			self.new3[i] = self.min_amp
		else:
			self.new3[i] = k


## this function is called for reversal of 1st wave ## 
    def reverse_3(self):
	if self.channel3 == 1:
		self.new3.reverse()
	else:
		self.new3.reverse()
		for i in xrange(len(self.new3) - 1):
			t = self.new3[i+1]
			self.new3[i+1] = self.new3[i]
			self.new3[i] = t

## this function is called for shifting of 1st wave ##
    def shift_3(self):
		fact=self.time33.get()
		fra_shift = int(abs(fact) * self.rate3)
		
		if(fact > 0):
			if(self.channel3 == 1):
				for i in range(fra_shift):
					self.new3.insert(0,0)
			else:
				for i in range(2*fra_shift):
					self.new3.insert(0,0)
				
		else:
			if(self.channel3 == 1):
				self.new3=self.new3[fra_shift::1]
			else:
				self.new3=self.new3[2*fra_shift::1]

		self.frames3 = len(self.new3)/self.channel3

## this function is called for scaling of 3rd wave ##
    def scaling_3(self):
		a=[]
		
		fact=self.time_scale33.get()
		print self.time_scale33.get()
		if(self.time_scale33.get() == 0):
			fact=1
		
		if self.channel3 == 1:	
			k=int(len(self.new3)/fact)
			for i in range(k):
				a.append(self.new3[int(fact*i) ])
		else:
			e_li=[]
			o_li=[]
			for i in range( len(self.new3) ):
				if(i%2 == 0):
					e_li.append(self.new3[i])
				else:
					o_li.append(self.new3[i])
			k=int(len(e_li)/fact)
			for i in range(k):
				a.append(e_li[ int(fact*i) ])
				a.append(o_li[ int(fact*i) ])
		
		self.new3 = a			
		self.frames3 = len(self.new3)/self.channel3


## this function creates the new file with the given changes ##
    def pack3(self):
	if self.width3==1: 
		fmt="%iB" % self.frames3*self.channel3 
	else: 
		fmt="%ih" % self.frames3*self.channel3

	out=struct.pack(fmt,*(self.new3))
	if self.pl3==0 or self.pl3==3:
		out_file=wave.open("ampli3.wav",'w')
	elif self.pl3==1:
		out_file=wave.open("wave_mix3.wav",'w')
	elif self.pl3==2:
		out_file=wave.open("wave_mod3.wav",'w')
	print self.pl3

	out_file.setframerate(self.rate3) 
	out_file.setnframes(self.frames3) 
	out_file.setsampwidth(self.width3) 
	out_file.setnchannels(self.channel3) 
	out_file.writeframes(out) 

	out_file.close()
	if self.pl3==0 :
		self.read_new("ampli3.wav",2)
	elif self.pl3==1:
		self.read_new("wave_mix3.wav",4)
		self.pl3=0
	elif self.pl3==2:
		self.read_new("wave_mod3.wav",3)
		self.pl3=0
	else:
		self.pl3=0

    def mix(self):
	print self.mix1.get()
	m_len=0	
	wave_1=0
	wave_2=0
	wave_3=0
	which=0
	if(self.mix1.get()==1):
		self.pl1=3
		self.readfile1()
		if m_len<len(self.new):
			m_len=len(self.new)
			which=1
		wave_1=1
	if(self.mix2.get()==1):
		self.pl2=3
		self.readfile2()
		if m_len < len(self.new2):
			m_len=len(self.new2)
			which=2
		wave_2=1
	if(self.mix3.get()==1):
		self.pl3=3
		self.readfile3()
		if m_len < len(self.new3):
			m_len=len(self.new3)
			which=3
		wave_3=1

	if wave_1==1:
		for i in range(m_len - len(self.new)):
			self.new.append(0)
	if wave_2==1:
		for i in range(m_len - len(self.new2)):
			self.new2.append(0)

	if wave_3==1:
		for i in range(m_len - len(self.new3)):
			self.new3.append(0)
	
	self.max_amp = 32767
	self.min_amp = -32768
	self.mix_wave=[]
	for i in range(m_len):
		self.mix_wave.append(0)
	
	for i in range(m_len):
		if wave_1==1:
			self.mix_wave[i]=self.mix_wave[i]+self.new[i]
		if wave_2==1:
			self.mix_wave[i]=self.mix_wave[i]+self.new2[i]
		if wave_3==1:
			self.mix_wave[i]=self.mix_wave[i]+self.new3[i]
		if self.mix_wave[i]>self.max_amp:
			self.mix_wave[i]=self.max_amp
		if self.mix_wave[i]<self.min_amp:
			self.mix_wave[i]=self.min_amp
	if which==1:
		self.new=self.mix_wave
		self.pl1=1
		self.pack1()
	elif which==2:
		self.new2=self.mix_wave
		self.pl2=1
		self.pack2()
	elif which==3:
		self.new3=self.mix_wave
		self.pl3=1
		self.pack3()


## this function is called to modulate the 3 waves and play ##
		
    def modulate(self):
	m_len=999999	
	wave_1=0
	wave_2=0
	wave_3=0
	which=0	
	
	if self.mod1.get()==1:
		self.pl1=3
		self.readfile1() 
		if m_len>len(self.new):
			m_len=len(self.new)
			which=1
		wave_1=1
	if self.mod2.get()==1:
		self.pl2=3
		self.readfile2()
		if m_len>len(self.new2):
			m_len=len(self.new2)
			which=2
		wave_2=1
	if self.mod3.get()==1:
		self.pl3=3
		self.readfile3()
		if m_len>len(self.new3):
			m_len=len(self.new3)
			which=3
		wave_3=1
	self.mod_wave=[]
	for i in range(m_len):
		self.mod_wave.append(1)

	self.max_amp=32767
	self.min_amp=-32768
	for i in range(m_len):
		if wave_1==1:
			self.mod_wave[i]=self.mod_wave[i]*self.new[i]
		if wave_2==1:
			self.mod_wave[i]=self.mod_wave[i]*self.new2[i]
		if wave_3==1:
			self.mod_wave[i]=self.mod_wave[i]*self.new3[i]
		
		if self.mod_wave[i]>self.max_amp:
			self.mod_wave[i]=self.max_amp
		if self.mod_wave[i]<self.min_amp:
			self.mod_wave[i]=self.min_amp

	if which==1:
		self.new=self.mod_wave
		self.pl1=2
		self.pack1()						
	elif which==2:
		self.new2=self.mod_wave
		self.pl2=2
		self.pack2()
	elif which==3:
		self.new3=self.mod_wave
		self.pl3=2
		self.pack3()

## this function is called to play the file ## 
    def read_new(self,filename,value):
	if value==0:
		if(self.pause_flag1 == 2):
			os.kill(self.pid1,signal.SIGCONT)
			self.pause_flag1 = 1
		else:
			self.pid1 = os.fork()
			if(self.pid1 == 0):
				self.pause_flag1 = 1
				self.wf = wave.open(filename, 'rb')
        			self.p = pyaudio.PyAudio()
        			self.stream = self.p.open(
            			format = self.p.get_format_from_width(self.wf.getsampwidth()),
            				channels = self.wf.getnchannels(),
            				rate = self.wf.getframerate(),
            				output = True,
        				)
				self.play(filename)
				self.close()
				exit(0)
	if value==1:
		if(self.pause_flag2 == 2):
			os.kill(self.pid2,signal.SIGCONT)
			self.pause_flag2 = 1
		else:
			self.pid2 = os.fork()
			if(self.pid2 == 0):
				self.pause_flag2 = 1
				self.wf = wave.open(filename, 'rb')
        			self.p = pyaudio.PyAudio()
        			self.stream = self.p.open(
            			format = self.p.get_format_from_width(self.wf.getsampwidth()),
            				channels = self.wf.getnchannels(),
            				rate = self.wf.getframerate(),
            				output = True,
        				)
				self.play(filename)
				self.close()
				exit(0)
	if value==2:
		if(self.pause_flag3 == 2):
			os.kill(self.pid3,signal.SIGCONT)
			self.pause_flag3 = 1
		else:
			self.pid3 = os.fork()
			if(self.pid3 == 0):
				self.pause_flag3 = 1
				self.wf = wave.open(filename, 'rb')
        			self.p = pyaudio.PyAudio()
        			self.stream = self.p.open(
            			format = self.p.get_format_from_width(self.wf.getsampwidth()),
            				channels = self.wf.getnchannels(),
            				rate = self.wf.getframerate(),
            				output = True,
        				)
				self.play(filename)
				self.close()
				exit(0)
	if value==3:
		if(self.pause_flag4 == 2):
			os.kill(self.pid4,signal.SIGCONT)
			self.pause_flag4 = 1
		else:
			self.pid4 = os.fork()
			if(self.pid4 == 0):
				self.pause_flag4 = 1
				self.wf = wave.open(filename, 'rb')
        			self.p = pyaudio.PyAudio()
        			self.stream = self.p.open(
            			format = self.p.get_format_from_width(self.wf.getsampwidth()),
            				channels = self.wf.getnchannels(),
            				rate = self.wf.getframerate(),
            				output = True,
        				)
				self.play(filename)
				self.close()
				exit(0)
	if value==4:
		if(self.pause_flag5 == 2):
			os.kill(self.pid5,signal.SIGCONT)
			self.pause_flag5 = 1
		else:
			self.pid5 = os.fork()
			if(self.pid5 == 0):
				self.pause_flag5 = 1
				self.wf = wave.open(filename, 'rb')
        			self.p = pyaudio.PyAudio()
        			self.stream = self.p.open(
            			format = self.p.get_format_from_width(self.wf.getsampwidth()),
            				channels = self.wf.getnchannels(),
            				rate = self.wf.getframerate(),
            				output = True,
        				)
				self.play(filename)
				self.close()
				exit(0)	
## this function is called to play the new file ##
    """
    def read_new(self,filename):
	self.wf = wave.open(filename, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True,
        )
	self.play(filename)
	self.close()
    """
    def play(self,file_name):
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        self.stream.close()
        self.p.terminate()

    def pause_1(self):
	self.pause_func(0)

    def pause_2(self):
	self.pause_func(1)

    def pause_3(self):
	self.pause_func(2)

    def pause_4(self):
	self.pause_func(4)

    def pause_5(self):
	self.pause_func(3)


    def pause_func(self,value):
	if(value == 0):
		os.kill(self.pid1,signal.SIGSTOP) 
		self.pause_flag1 = 2
	if(value == 1):
		os.kill(self.pid2,signal.SIGSTOP) 
		self.pause_flag2 = 2
	if(value == 2):
		os.kill(self.pid3,signal.SIGSTOP) 
		self.pause_flag3 = 2
	if(value == 3):
		os.kill(self.pid4,signal.SIGSTOP) 
		self.pause_flag4 = 2

	if(value == 4):
		os.kill(self.pid5,signal.SIGSTOP) 
		self.pause_flag5 = 2
	
    def record(self):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS =4
	WAVE_OUTPUT_FILENAME = "recorded_file.wav"
	print "asdasd"
	k=sys.platform
	if sys.platform == k:
		CHANNELS = 1
		print "asdasdas"
		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
			        channels=CHANNELS,
			        rate=RATE,
			        input=True,
			        frames_per_buffer=CHUNK)

		print("* recording")

		frames = []
		x=int(RATE / CHUNK * RECORD_SECONDS)

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		#	self.pgbar_2.set_fraction(i*1.0/x)
			  data = stream.read(CHUNK)
			  frames.append(data)

		print("* done recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
        

def main():
    root = Tk()
    ex = Example(root)
    root.geometry("800x800+300+300")
    root.resizable(width=False,height=False)
    root.mainloop()  

if __name__ == '__main__':
    main()  
