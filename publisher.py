import pika

credentials = pika.PlainCredentials(username='master', password='m45t3r')
parameters = pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.basic_publish(exchange='', routing_key='python queue', body='Hello World!')
print('[x] Sent "Hello World!"')
connection.close()
