import json

import pika
from pika.exchange_type import ExchangeType

HOST = 'localhost'
USERNAME = ''
PASSWORD = ''
VIRTUAL_HOST = ''
QUEUE_NAME = ''
EXCHANGE_NAME = ''
EXCHANGE_TYPE = ExchangeType.topic
ROUTING_KEY = ''
DURABLE = True
EXCLUSIVE = False
AUTO_DELETE = False

credentials = pika.PlainCredentials(USERNAME, PASSWORD)
connection_parameters = pika.ConnectionParameters(host=HOST, port=5672, virtual_host=VIRTUAL_HOST,
                                                  credentials=credentials, heartbeat=0)
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE, durable=DURABLE,
                         auto_delete=AUTO_DELETE)

# channel.queue_declare(queue=QUEUE_NAME, durable=DURABLE, exclusive=EXCLUSIVE, auto_delete=AUTO_DELETE)

message = {''}
encode_data = json.dumps(message, indent=2).encode('utf-8')
channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=ROUTING_KEY, body=encode_data)
print(f" [x] Sent {message}")

connection.close()
