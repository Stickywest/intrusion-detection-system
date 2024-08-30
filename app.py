import serial
import time
from playsound import playsound

# Set up the serial connection (adjust COM port and baud rate)
try:
    ser = serial.Serial('COM6', 9600)  # Replace 'COM3' with the correct port on your laptop
    print("Serial port opened successfully.")
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()

time.sleep(2)  # Wait for the connection to establish

print("Listening for incoming data...")

try:
    while True:
        if ser.in_waiting > 0:  # Check if there's any data waiting in the serial buffer
            line = ser.readline().decode('utf-8').strip()  # Read the incoming data
            print(f"Received: {line}")  # Print the received data for debugging
            
            if "Intrusion Detected" in line:  # Check if the message contains "Intrusion Detected"
                print("Intrusion detected! Playing sound...")
                playsound('alarm.mp3')  # Replace with the path to your sound file
except KeyboardInterrupt:
    print("\nScript interrupted by user. Exiting...")
except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()  # Ensure the serial connection is closed when exiting
    print("Serial connection closed.")
