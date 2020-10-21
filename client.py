from celery import Celery

app = Celery('client', broker='amqp://guest:guest@localhost/celeryhost')

@app.task
def sumarConPrint(a1, a2):
    print(f'Mi mama me mando a sumar {a1} con {a2}')