from flask import Flask, render_template, request, flash, redirect, url_for
from hashids import Hashids
import sqlite3

#connect to database, set name based access to columns
def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite3.Row
	return conn

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Ysnr2io3ie'

#note: a salt is a random string that is provided to the hashing function which the encryption is based
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

@app.route('/', methods=('GET', 'POST'))
def index():
	conn = get_db_connection()
	
	if request.method == 'POST':
		url = request.form['url']

		if not url:
			flash('The url is required!')
			return redirect(url_for('index'))
		
		url_data = conn.execute('INSERT INTO urls (original_url VALUES (?)',
					(url,))
		conn.commit()
		conn.close()

		url_id = url_data.lastrowid
		hashid = hashids.encode(url_id)
		short_url = request.host_url + hashid

		return render_template('index.html', short_url=short_url)
		
	return render_template('index.html')