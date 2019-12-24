import MySQLdb
import serial                                       # import serial library
from serial import Serial
import paho.mqtt.publish as publish

ser = serial.Serial('/dev/ttyACM0', 9600)       # create serial object named arduino

#while True:                                         # create loop
#    command = str(input ("Servo position: "))       # query servo position
#    arduino.write(command)                          # write position to serial port
#    reachedPos = str(arduino.readline())            # read serial port for arduino echo
#    print(reachedPos) 
counter = 1 
while True:
    # Open database connection
    
    db = MySQLdb.connect("localhost","Wei","0523","db1" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT DATA FROM signals where VALUE = '0'"
     
    try:
        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        
        for row in results:
            print(row[0])
            if row[0]=='Forward':
                ser.write('f')
                try:
                    cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'Forward'")
                except:
                    print("update fails")
            elif row[0]=="Backward":
                ser.write('b')
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'Backward'")

            elif row[0]=="left":
                ser.write('l')
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'left'")

            elif row[0]=="right":
                ser.write('r')
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'right'")

            elif row[0]=="Stop":
                ser.write('s')
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'Stop'")
 
            elif row[0]=="Publish":
                ser.write('s')    #make the robot stop then shutter
                publish.single("Camera/shutter", "World", hostname="192.168.86.24")
                print "Publish", counter, "Done"
                counter=counter+1
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'Publish'")
            elif row[0]=="Degree":
                #command = str(30)
                ser.write('t')
                cursor.execute("UPDATE signals SET VALUE = '1' where DATA = 'Degree'")
            else:
                break

    except:
        print "Error: unable to fecth data"
    db.commit()
    cursor.close()
# disconnect from server
db.close()
