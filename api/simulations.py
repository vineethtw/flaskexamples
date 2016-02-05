from flask import Flask, request, jsonify
from flask.ext.restful import Api, Resource, reqparse
from celery import chord
from waiting_on_tasks import tasks

app = Flask(__name__)
api = Api(app)


class Simulations(Resource):
    def post(self):
        print request.json
        ids = request.json['ids']

        chord(
            (tasks.run_simulation.s(s_id) for s_id in ids),
            tasks.gather_results.s())()

        return 201

api.add_resource(Simulations, '/simulations', endpoint="simulations")
