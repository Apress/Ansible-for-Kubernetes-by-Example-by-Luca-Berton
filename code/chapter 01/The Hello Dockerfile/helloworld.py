#!/usr/bin/env python3
from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class Hello (Resource):
    def get(self):
        return 'Hello World'
api.add_resource(Hello, '/') # Route_1
if __name__ == '__main__':
    app.run('0.0.0.0','8080')
