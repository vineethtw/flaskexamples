from waiting_on_tasks import tasks
from subprocess import Popen
from celery import chord

pid = Popen(['celery', 'worker', '--app=engine', '-q'])

simulation_ids = (100, 101, 102, 107, 110)

results = chord(
    (
        tasks.run_simulation.s(s_id) for s_id in simulation_ids),
        tasks.gather_results.s())()


print results.get()

pid.terminate()