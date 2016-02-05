from subprocess import Popen
from engine import celery, tasks
from celery import group


'''
Runner file for the example project
'''

pid = Popen(['celery', 'worker', '--app=engine', '-q'])

print "***************************"
print "Running one simple task"
add_task = tasks.add.delay(50, 10)
print "Status {", add_task.state, "} Result {", add_task.get(), "}"
print "***************************"


result = (group(tasks.add.s(i, i) for i in xrange(10)) | tasks.add(1000, 4000)).delay()
print result.get()




pid.terminate()


