from socket import *
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
host = "0.0.0.0"

print host

port = 7777

s = socket(AF_INET, SOCK_STREAM)

print "Socket Made"

s.bind((host,port))

print "Socket Bound"

s.listen(5)

print "Listening for connections..."

check = True
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   data = c.recv(1024)
   if(check):
        GPIO.output(7,True)
        check = False
   else:
        check = True
        GPIO.output(7,False)
   print data
   c.close() 
