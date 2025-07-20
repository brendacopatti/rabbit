# rabbit
Hands-on study and exploration of RabbitMQ message broker.



# 🐰 RabbitMQ com Python – Guia Prático (Dia 1)

## 📘 Conceitos Básicos

### O que é RabbitMQ?

RabbitMQ é um **message broker**, ou seja, um sistema intermediário responsável por receber, armazenar e entregar mensagens entre diferentes aplicações ou serviços. Ele é muito usado em arquiteturas de **microserviços** para desacoplar partes do sistema e permitir comunicação assíncrona.

### Principais Termos

| Termo             | Significado                                                                 |
|------------------|------------------------------------------------------------------------------|
| **Broker**       | Sistema que gerencia filas e entrega mensagens (RabbitMQ é um broker).       |
| **Producer**     | Quem envia mensagens.                                                        |
| **Consumer**     | Quem consome mensagens.                                                      |
| **Queue**        | Fila onde a mensagem fica até ser processada.                                |
| **Exchange**     | Controla o roteamento das mensagens para as filas.                           |
| **Routing Key**  | Chave usada para rotear mensagens via exchanges do tipo `direct`, `topic`.   |

### Por que usar RabbitMQ?

- Permite que partes do sistema se comuniquem mesmo que uma delas esteja offline.
- Reduz acoplamento entre serviços.
- Garante entrega confiável e escalabilidade.
- Ideal para processamentos em background, filas de tarefas, eventos de sistema, etc.

---

## 🛠️ Setup Local com Docker

Para iniciar o RabbitMQ localmente com painel de gerenciamento:

### Pré-requisitos:
- Docker instalado (https://www.docker.com/products/docker-desktop)

### Comando para rodar:

```bash
docker run -d --hostname rabbit-host --name rabbit \
-p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
# 🐰 RabbitMQ com Python – Guia Prático (Dia 2)

## Objetivo

Foi criado um **Producer** e um **Consumer** em Python para enviar e receber mensagens usando RabbitMQ.

## O que foi feito

- Foi criado um Producer que envia uma mensagem para uma fila chamada `fila_pedidos`.
- Foi criado um Consumer que escuta essa mesma fila e processa as mensagens recebidas.
- Foi utilizado o `queue_declare` para garantir que a fila existisse antes de ser usada.
- No Consumer, foi aplicada a confirmação automática (`auto_ack=True`) para simplificar o fluxo neste primeiro teste.

## Como testar

- Primeiramente, o Consumer deve ser executado para escutar as mensagens.
- Em seguida, o Producer é executado para enviar uma mensagem para a fila.
- Quando a mensagem é enviada, o Consumer exibe a mensagem no console.

## O que foi aprendido

- É importante declarar a fila antes de usá-la para evitar erros.
- A confirmação automática facilita testes rápidos, mas para produção é recomendado usar confirmação manual para garantir segurança no processamento.
- Essa prática ajudou a entender o fluxo básico de mensageria com RabbitMQ e Python.
