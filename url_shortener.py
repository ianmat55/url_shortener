#takes url and shortens it to look nice. Using Flask, sqlite
from flask import Flask, render_template, request, flash, redirect, url_for
from hashids import Hashids
import sqlite3

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn


app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

@app.route('/')
def index():
	return render_template('index.html')
