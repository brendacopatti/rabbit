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
