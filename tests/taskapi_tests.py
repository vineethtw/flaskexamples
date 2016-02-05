from flask.ext.testing import TestCase
from flask import jsonify

import unittest
import json
from api.simulation import app


class SimulationTests(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_cannned_get_simulation(self):
        response = self.client.get('/simulation')
        self.assert200(response)
        self.assertEquals({"task_id": 1001}, json.loads(response.data))

    def test_should_be_able_to_create_a_simulation(self):
        """And the task does a callback"""
        response = self.client.post('/simulation',
                                    headers={},
                                    data=dict(simulation_id=400))

        self.assertEquals(response.json, dict(simulation_id=400))


if __name__ == '__main__':
    unittest.main()
