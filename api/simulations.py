from flask import Flask, request, jsonify
from flask.ext.restful import Api, Resource, reqparse
from celery import chord, chain
from waiting_on_tasks import tasks

app = Flask(__name__)
api = Api(app)


class Simulations(Resource):
    def post(self, batch_id):
        ids = request.json['ids']

        chain(chord(
            (tasks.run_simulation.s(s_id) for s_id in ids),
            tasks.gather_results.s()),
            tasks.callback.s("http://www.google.com", batch_id))()

        return 201

    def put(self, batch_id):
        print "callback_received {}".format(batch_id)
        return jsonify({'status': 'success', 'retval': batch_id})


api.add_resource(Simulations, '/simulations/<batch_id>',
                 endpoint="simulations")
