import pika

# Conecta ao RabbitMQ (localhost)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declara fila para garantir que existe
channel.queue_declare(queue='fila_pedidos')

# Função callback chamada quando chega uma mensagem
def callback(ch, method, properties, body):
    print(f" [x] Mensagem recebida: {body.decode()}")

# Consome mensagens da fila (auto_ack=True confirma mensagem automaticamente)
channel.basic_consume(queue='fila_pedidos', on_message_callback=callback, auto_ack=True)

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
channel.start_consuming()
