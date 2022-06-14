# Run this python script continuously on a computer connected to arduino via usb
import serial
import psycopg2

# Same port that arduino opens for serial 
SERIAL_PORT = 9600
# path to arduino
SERIAL_PATH = "/dev/cu.usbmodem144201"

ser = serial.Serial(SERIAL_PATH, SERIAL_PORT)

# Database user and login info
database = "xxx"
user = "xxx"
password = "xxx"
host = "xxx"
port = "xxx"
table_name = "xxx"

conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

def main():
    while True:
        try:
            cc=str(ser.readline().decode("utf-8")).strip()
            print(cc)

            if check_sql(cc):
                print("ACCEPTED")
                ser.write('G'.encode());
                # send back 
            else:
                print("DENIED")
        except UnicodeDecodeError as ex:
            print("EX: {}".format(ex))
    ser.close()

def check_sql(number):
    # Open cursor for queries
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM {} where number = \'{}\'".format(table_name, number))
        # fetch all data of nodes
        valid_cards = cur.fetchall()
        if valid_cards:
            # we good!
            return True
        else:
            return False  

if __name__ == "__main__":
    main()
