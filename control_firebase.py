#!/usr/bin/python
import serial                                       # import serial library
from serial import Serial
import paho.mqtt.publish as publish		    # import mqtt

#import firebase
from firebase import firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

ser = serial.Serial('/dev/ttyACM0', 9600)       # create serial object named arduino

cred = credentials.Certificate('JSON_FILE_PATH')
firebase_admin.initialize_app(cred,{
	'databaseURL':'https://serverdatabase-53b8f.firebaseio.com/'
})

firebase = firebase.FirebaseApplication('https://serverdatabase-53b8f.firebaseio.com/', None)
#firebase.put('/user','Degree','20')
#print(degree)
#print(firebase.get('/user','Command'))

counter = 1 
while True:
    try:
        #fetch the Command and Degree data from the Firebase
        command = firebase.get('/user','Command')
        degree = firebase.get('/user','Degree')
        command_flag = firebase.get('/user','Command_flag')
        degree_flag = firebase.get('/user','Degree_flag')
        if command_flag == '0':
		if command =='Forward':
		    ser.write('f')
		    
		    #command_flag = firebase.put('/user','Command_flag','1')
		elif command == "Backward":
		    ser.write('b')
		    
		    #command_flag = firebase.put('/user','Command_flag','1')
		elif command == "Left":
		    ser.write('l')
		    #command_flag = firebase.put('/user','Command_flag','1')
		elif command == "Right":
		    ser.write('r')
		    #command_flag = firebase.put('/user','Command_flag','1')
		elif command == "Stop":
		    ser.write('s')
		    #command_flag = firebase.put('/user','Command_flag','1')
		elif command == "Publish":
		    ser.write('s')    #make the robot stop then shutter
		    publish.single("Camera/shutter", "World", hostname="192.168.86.24")
		    print "Publish", counter, "Done"
		    counter = counter + 1
		    command_flag = firebase.put('/user','Command_flag','1')
		else:
		    break
	if degree != '0' and degree_flag=='0':
	    if degree == '30':
	        ser.write('t')
	        print("write servo")
	        command_flag = firebase.put('/user','Degree_flag','1')
            elif degree == '60':		
		ser.write('u')
	        print("write servo")
	        command_flag = firebase.put('/user','Degree_flag','1')
            else :
                ser.write('t')
	print("Servo rotate angle : "+degree)
	print("Command : "+command)
    except:
        print "Error: unable to fecth data"
	break
