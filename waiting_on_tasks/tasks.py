from engine.celery import app
import time

@app.task
def run_simulation(simulation_id):
    print "starting"
    time.sleep(10)
    print "end sleep"
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


def success(simulation_id):
    return {'id': simulation_id, 'STATUS': 'PASS'}


def failed(simulation_id):
    return {'id': simulation_id, 'STATUS': 'FAIL'}
