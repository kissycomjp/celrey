import os
import time
import celery
import celeryconfig

CELERY_BROKER = os.environ.get('CELERY_BROKER')
CELERY_BACKEND = os.environ.get('CELERY_BACKEND')

app = celery.Celery(
  'tasks',
  broker=CELERY_BROKER,
  backend=CELERY_BACKEND
)
app.config_from_object(celeryconfig)

@app.task
def run():
   time.sleep(10)
   print('Process has finished!')
   return 'Process has just finished!'

@app.task
def calc(a, b):
   return a+b
