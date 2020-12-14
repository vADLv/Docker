#!/usr/bin/env python
import pika, sys, os, time, random

def main():
    credentials = pika.PlainCredentials('vad', 'vad')

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbit',credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='John')
    channel.queue_declare(queue='Vad')

    channel.exchange_declare(exchange='V', exchange_type='direct')

    channel.queue_bind(exchange='V',
                   queue='John',
                   routing_key='black')

    channel.queue_bind(exchange='V',
                   queue='Vad',
                   routing_key='white')

    print(' [*] Waiting for messages. To exit press CTRL+C')

    i=0
    while i<10:
        value = random.randint(0, 1)
        if value:
            channel.basic_publish(exchange='V', routing_key='black', body='Hello! I like virtualization! Skill = '+str(i))
        else:
            channel.basic_publish(exchange='V', routing_key='white', body='Good afternoon! Clouds forever! Skill = '+str(i))
        time.sleep(3)
        i=i+1

    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        connection.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
