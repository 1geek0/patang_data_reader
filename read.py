import serial
import csv
import time

# Open the serial port
ser = serial.Serial('/dev/cu.usbserial-210', 115200)

# Open the CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    while True:
        try:
            # Read a line from the serial port
            line = ser.readline()
            try:
                line = line.decode('utf-8', errors='ignore').rstrip()
                print(line)
            except UnicodeDecodeError:
                print("Unexpected decoding error, skipping line...")
                continue

            # Write the line to the CSV file
            writer.writerow([time.time(), line])
        except KeyboardInterrupt:
            break
