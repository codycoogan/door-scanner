import serial
import psycopg2

ser = serial.Serial("/dev/cu.usbmodem144201", 9600)

#Database user and login info
database = "cards"
user = "cody"
password = "password"
host = "localhost"
port = "5432"

conn = psycopg2.connect(database = database, user = user,password = password, host = host,port = port)

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
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards_numbers where number = \'{}\'".format(number))
    #f etch all data of nodes
    valid_cards = cur.fetchall()
    if valid_cards:
        # we good!
        return True
    else:
        return False  

if __name__ == "__main__":
    main()
