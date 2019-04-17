from flask import Flask, render_template, request
from peewee import *

from models import database_proxy, History

app = Flask(__name__)

database = SqliteDatabase('test.db')
database_proxy.initialize(database)

database.create_tables([History])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    # TODO: do conversion of currency
    amount = request.form['amount']
    src_currency = request.form['src_currency']
    tgt_currency = request.form['tgt_currency']

    result = 0.0

    return render_template('convert.html', result=result)

@app.route('/history')
def history(limit=25, offset=0):
    history = History.select().limit(limit).offset(offset)

    return render_template('history.html', history=history)

app.run(debug=True)
