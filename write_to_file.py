#!/usr/bin/env python3
##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
import serial, sys

num_args = 3
baud_rate = 115200

def write(write_to_file_path, serial_port):
	output_file = open(write_to_file_path, "w+")
	ser = serial.Serial(serial_port, baud_rate)
	while True:
	    line = ser.readline()
	    line = line.decode("utf-8")
	    print(line)
	    output_file.write(line)

def main():
	if len(sys.argv) < num_args:
		print("Please provide the name of the serial port and the output file")
	else:
		serial_port = sys.argv[1]
		write_to_file_path = sys.argv[2]

		write(write_to_file_path, serial_port)

if __name__ == '__main__':
	main()


