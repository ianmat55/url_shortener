#takes url and shortens it to look nice. Using Flask, sqlite
from flask import Flask, render_template
import requests, sqlite3

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
