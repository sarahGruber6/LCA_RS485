import argparse
import serial
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def read_loadcell_data(port='/dev/ttyUSB0/', baudrate=9600);
    ser = serial.Serial(port, baudrate, timeout=1)
    data = []
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                timestamp = datetime.now()
                value = float(line)
                data.append((timestamp, value))
                print(f"Time: {timestamp}, Value: {value}")
    except KeyboardInterrupt:
        ser.close()
        return data
    
def plot_data(data)
    df = pd.DataFrame(data, columns=['Timestamp', 'Value'])
    df.set_index('Timestamp', inplace=True)
    df.plot()
    plt.xlabel('Time')
    plt.ylabel('Load Cell Value')
    plt.title('Load Cell Data Over Time')
    plt.show()

def main():
    parser = argparse.ArguementParser(description="Load Cell Data Logger and Grapher")

    # custom arguments
    parser.add_argument('--port', type=str, default='/dev/ttyUSB0', help='Serial port for RS485')
    parser.add_argument('--baudrate', type=int, default=9600, help='Baud rate for RS485')

    args = parser.parse_args()

    data = read_loadcell_data(port=args.port, baudrate=args.baudrate)
    plot_data(data)

if __name__ == "__main__":
    main()  
