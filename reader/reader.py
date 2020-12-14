#!/usr/bin/env python
import pika, sys, os, psycopg2, time

def main():

    time.sleep(20)

    credentials = pika.PlainCredentials('vad', 'vad')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbit',credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='John')
    channel.queue_declare(queue='Vad')

    con = psycopg2.connect(
      database="vad",
      user="vad",
      password="vad",
      host="db",
      port="5432"
    )

    cur = con.cursor()

    body = "test"

    def callback1(ch, method, properties, body):
        cur.execute("""INSERT INTO table1 (message) VALUES (%s);""",(str(body),))
        con.commit()
        print(" [x] (John) Received %r" % body)
    channel.basic_consume(queue='John', on_message_callback=callback1, auto_ack=True)

    def callback2(ch, method, properties, body):
        cur.execute("""INSERT INTO table2 (message) VALUES (%s);""",(str(body),))
        con.commit()
        print(" [x] (Vad) Received %r" % body)
    channel.basic_consume(queue='Vad', on_message_callback=callback2, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    #connection.close()
    #con.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
