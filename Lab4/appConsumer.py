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

def callback(ch, method, properties, body):
    print(f'{body.decode()} is received')


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)


while True:
    try:
        channel.start_consuming()

    except KeyboardInterrupt:
        print('Keyboard Interrupt bye bye... Shutting Down')
        channel.stop_consuming
        sys.exit()
