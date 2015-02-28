from flask import reader_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Fashionista'} #placeholder
	return render_template('index.html', title='Home', user=user)
