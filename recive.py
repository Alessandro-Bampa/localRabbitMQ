import json

import pika
from pika.exchange_type import ExchangeType

HOST = 'localhost'
PORT = 5672
USERNAME = ''
PASSWORD = ''
VIRTUAL_HOST = ''
QUEUE_NAME = ''
EXCHANGE_NAME = ''
EXCHANGE_TYPE = ExchangeType.topic
DURABLE = True
EXCLUSIVE = False
AUTO_DELETE = False

credentials = pika.PlainCredentials(USERNAME, PASSWORD)
connection_parameters = pika.ConnectionParameters(host=HOST, port=PORT, virtual_host=VIRTUAL_HOST,
                                                  credentials=credentials, heartbeat=0)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE, durable=DURABLE,
                         auto_delete=AUTO_DELETE)


def callback(ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")


channel.basic_consume(
    queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
