from flask import Flask, request, jsonify
from flask.ext.restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)


class Simulation(Resource):
    def get(self):
        return {'task_id': 1001}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('simulation_id', type=int,
                            help='Simulation Id')
        args = parser.parse_args()

        return jsonify(simulation_id=args["simulation_id"])

    def delete(self):
        pass


api.add_resource(Simulation, '/simulation', endpoint="tasks")
