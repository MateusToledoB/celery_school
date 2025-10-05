# Celery School

Este projeto foi criado para estudos de funções assíncronas utilizando **Celery**.

## Objetivo

Explorar e aprender como implementar tarefas assíncronas em Python usando Celery, incluindo conceitos como filas, workers e brokers.

## Principais tópicos abordados

- Instalação e configuração do Celery
- Criação de tarefas assíncronas
- Execução de workers
- Integração com brokers neste caso o Redis
- Monitoramento de tarefas

## Requisitos

- Python 3.12.6
- Celery
- Broker Redis

## Como executar

1. Instale as dependências:
    ```bash
    pip install celery redis
    ```
2. Inicie o broker (exemplo com Redis):
    ```bash
    redis-server
    ```
3. Execute o worker do Celery:
    ```bash
    celery -A <nome_do_app> worker --loglevel=info
    ```
4. Dispare tarefas assíncronas pelo seu código Python.

## Referências

- [Documentação oficial do Celery](https://docs.celeryq.dev/en/stable/)
- [Tutorial Celery com Python](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

---

Este projeto é apenas para fins de estudo e experimentação.