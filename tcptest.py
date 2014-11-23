from socket import *

## Import GPIO library
import RPi.GPIO as GPIO 

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up header pin 7 (GPIO7) as an output
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

while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   data = c.recv(1024)
   if(data == "on" ):

        print 'pin 7 on'
        GPIO.output(7,True) ## Turn on GPIO pin 7
        
   elif(data == 'off' ):
        print 'pin 7 off'        
        GPIO.output(7,False) ## Turn off GPIO pin 7
   elif(data == 'close' ):
        print 'closing connection'
        break
   c.close() 
GPIO.cleanup()  
