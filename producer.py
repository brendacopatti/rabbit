import pika

# Conecta ao RabbitMQ (localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara fila chamada 'fila_pedidos' (será criada se não existir)
channel.queue_declare(queue='fila_pedidos')

# Envia mensagem para fila
channel.basic_publish(exchange='', routing_key='fila_pedidos', body='Novo pedido criado!')

print(" [x] Mensagem enviada para a fila 'fila_pedidos'")

# Fecha conexão
connection.close()
