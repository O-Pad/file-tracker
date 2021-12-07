### Steps to run File Tracker

1. Clone the repository
```bash
git clone git@github.com:O-Pad/file-tracker.git
```

2. cd into the repository and run the following commands:
```bash
docker-compose up
```

### Rabbitmq 
Full send and receive source code - https://github.com/O-Pad/experiments/tree/main/rabbitmq-fanout

Code to create a new fanout exchange with the name "logs":
```python3
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')
```
Code to publish to created exchange
```python3
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
```

Code to subscribe to the created exchange and listen to the messages
```python3
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
```