import pika
import sys

if len(sys.argv) != 5:
    print ("Correct usage: script, IP address, PORT number, RabbitMQ User and Password")
    exit()
else:
    IP = str(sys.argv[1])
    PORT = str(sys.argv[2])
    user = str(sys.argv[3])
    pswd = str(sys.argv[4])

connection = pika.BlockingConnection(pika.ConnectionParameters(IP, PORT, '/', pika.PlainCredentials(user, pswd)))
channel = connection.channel()

t = ''

print("Runnning Producer Application...")
print("Type task to be send")


while True:
    try:
        t = sys.stdin.readline()
        if (t != ''):
            channel.basic_publish(exchange='my_exchange', routing_key='test', body=t)
            print('Taks send succesfully!')
            
    except KeyboardInterrupt:
        print('Keyboard Interrupt bye bye... Shutting Down')
        connection.close()
        sys.exit()
