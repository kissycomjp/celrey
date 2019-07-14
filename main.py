import tasks
print('<first task>')
worker = tasks.run.delay()

while not worker.ready():
   pass
print(worker.result)

print('<second task>')
worker = tasks.calc.delay(100, 200)
while not worker.ready():
   pass
print(worker.result)
