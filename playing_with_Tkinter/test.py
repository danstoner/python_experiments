## Code from SandMan874
## https://www.raspberrypi.org/forums/viewtopic.php?t=112356&p=771268

import time
import threading
import Queue
#import serial
#import RPi.GPIO as GPIO
from Tkinter import *

#GPIO Configuration
#GPIO.setmode(GPIO.BCM)

#GPIO Setup
#GPIO.setup(22, GPIO.OUT)
#GPIO.output(22, 0)

#Serialport variables
#SERIALPORT = "/dev/ttyUSB0"
#BAUDRATE = 19200

#Serialport configuration
#ser = serial.Serial(SERIALPORT, BAUDRATE, timeout=4)

#Flush the buffers
#ser.flushInput()
#ser.flushOutput()

#Variable for Celcius
#a = u'\u2103'

class GuiPart:
   def __init__(self, master, queue):
      self.queue = queue

      root.wm_title("Project Valkyrie")
      root.config(background = "#FFFFFF")

      root.leftFrame = Frame(root, width=350, height=660)
      root.leftFrame.grid(row=1, column=0)

      root.circleCanvas = Canvas(root.leftFrame, width=350, height=660, bg='white')
      root.circleCanvas.grid(row=1, column=0)

      self.elements = [root.circleCanvas.create_oval(30, 30, 90, 90, width=2, fill='red'), 
      root.circleCanvas.create_oval(30, 120, 90, 180, width=2, fill='gray'),
      root.circleCanvas.create_oval(30, 210, 90, 270, width=2, fill='gray'),
      root.circleCanvas.create_oval(30, 300, 90, 360, width=2, fill='gray'),
      root.circleCanvas.create_oval(30, 390, 90, 450, width=2, fill='gray'),
      root.circleCanvas.create_text(125, 60, font='TkHeadingFont 12 bold', anchor=W, text='Uplink Status'),
      root.circleCanvas.create_text(125, 150, font='TkHeadingFont 12 bold', anchor=W, text='Bilge Level High'),
      root.circleCanvas.create_text(125, 240, font='TkHeadingFont 12 bold', anchor=W, text='Bilge Level High High'),
      root.circleCanvas.create_text(125, 330, font='TkHeadingFont 12 bold', anchor=W, text='Battery Alarm'),
      root.circleCanvas.create_text(125, 420, font='TkHeadingFont 12 bold', anchor=W, text='Fire Alarm'),
      root.circleCanvas.create_text(125, 495, font='TkHeadingFont 12 bold', anchor=W, text='Onboard temperature'),
      root.circleCanvas.create_rectangle(20, 480, 100, 510, width=2),
      root.circleCanvas.create_text(60, 495, font='TkHeadingFont 12 bold', text='0.00 C'),
      root.circleCanvas.create_image(175, 600, image=logoISE)]

      root.firstLabel = Label(root.leftFrame, text="Alarm Status", font='TkHeadingFont 15 bold')
      root.firstLabel.grid(row=0, column=0, padx=10, pady=2)
   
   def processIncoming(self):
      while self.queue.qsize():
         try:
            alarms = self.queue.get(0)

            if alarms[0] == '0':
               fills = ['red', 'gray', 'gray', 'gray', 'gray']
               for i in range(5):
                  root.circleCanvas.itemconfigure(self.elements[i], fill=fills[i])
            else:
               root.circleCanvas.itemconfigure(self.elements[0], fill='green')
               for i in range(1, 5):
                  fill='red' if alarms[i] == '0' else 'green'
                  root.circleCanvas.itemconfigure(self.elements[i], fill=fill)
               temp = float(alarms[7:].rstrip('\r\n'))/1000
               root.circleCanvas.itemconfigure(self.elements[12], text='%.2f' % temp + a)

         except Queue.Empty:
            pass

class ThreadedClient:
   def __init__(self, master):
      self.master = master

      self.queue = Queue.Queue()

      self.gui = GuiPart(master, self.queue)

      self.running = 1
      self.thread1 = threading.Thread(target=self.workerThread1)
      self.thread1.start()

      self.periodicCall()

   def periodicCall(self):

      self.gui.processIncoming()
      if not self.running:
         import sys
         sys.exit(1)
      self.master.after(100, self.periodicCall)

   def workerThread1(self):
      while self.running:
         pass
 #           msg = ser.readline()
 #           if msg != '':
 #              if (msg[1] == '0') or (msg[2] == '0') or (msg[4] == '0'):
 #                 GPIO.output(22, 1)
 #              else:
 #                 GPIO.output(22, 0)
 #              self.queue.put(msg)
 #           else:
 #              noConn = '00000t=00000\n'
 #              self.queue.put(noConn)

   def endApplication(self):
      self.running = 0

root = Tk()

logoISE = PhotoImage(file='/usr/share/pixmaps/pidgin/emotes/default/umbrella.png')

client = ThreadedClient(root)


# This _should_ be run on Window close but it seems to run immediately
#root.protocol("WM_DELETE_WINDOW", root.destroy())

root.mainloop()



