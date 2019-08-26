#! /usr/bin/python

import sys,time, httplib, urllib ##In Python 2.7 httplib. From Python 3 http.client
from serial import Serial


   
def read_serial(s):
    i = 0
    
    while True:
        if s.inWaiting() != 0:
            line = s.readline()
            line = line.decode('ascii').strip("\r\n")
            print(line, time.time(), i)
            i = i + 1
            bpm=line[8:11]
            #Quoting key and value from my data and encode it into an URL
            params=urllib.urlencode({'field1': bpm,'key':'H0FG30RP6DSQCUNF'}) ##In Python 2.7 urllib.urlencode. From Python 3 urllib.parse.urlencode
            #Associated headers to param
            headers={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            #Implementation of the HTTP client side to connect to thingspeak
            conn= httplib.HTTPConnection("api.thingspeak.com:80") ##In Python 2.7 httplib. From Python 3 http.client
            #Sends a request to the server(conn) to post the information of our bpm 
            conn.request("POST", "/update", params, headers)
            #Gets the response of the server
            response=conn.getresponse()
            #Gets the response body
            data=response.read()
            #Closes the connection with the server
            conn.close()
            
            
        time.sleep(0.001) #Execution suspension
    f.close()
    


def main(args = None):
    if args is None:
        args = sys.argv
    port,baudrate = 'COM4', 115200
    if len(args) > 1:
        port = args[1]
    if len(args) > 2:
        baudrate = int(args[2])

    s = Serial(port, baudrate)
    read_serial(s)

    return 0

if __name__ == '__main__':
    sys.exit(main())
