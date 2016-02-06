from engine.celery import app
import time

@app.task
def run_simulation(simulation_id):
    print "starting {}".format(simulation_id)
    if simulation_id != 1:
        time.sleep(10)
    print "end sleep {}".format(simulation_id)
    if simulation_id % 2 == 0:
        result = success(simulation_id)
    else:
        result = failed(simulation_id)
    return result


@app.task
def gather_results(results):
    consolidated_results = {
        'PASS':  [],
        'FAIL': []
    }
    for result in results:
        consolidated_results[result['STATUS']].append(result['id']);
    return consolidated_results

@app.task
def callback(results, url, batch_id):
    print "Task : Going to callback {}".format(batch_id)



def success(simulation_id):
    return {'id': simulation_id, 'STATUS': 'PASS'}


def failed(simulation_id):
    return {'id': simulation_id, 'STATUS': 'FAIL'}
