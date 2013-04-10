#!/usr/bin/env python
from bottle import Bottle, run, template, redirect, view
from pymongo import MongoClient

conn = MongoClient()
DATABASE = 'GeneralBuy'

app = Bottle()

@app.route('/')
def home():
    db = conn[DATABASE]
    return 'It\'s working'


run(app, host='0.0.0.0', port=8095, reloader=True)

