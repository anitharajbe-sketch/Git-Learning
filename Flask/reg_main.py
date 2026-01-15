from flask import *
from db_logic import reg_users_with_address
import datetime as dt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'i-love-flask-dev'

@app.route('/', methods=['GET', 'POST'])
def welcome():
	return render_template('welcome.html')

@app.route('/register_form')
def add_details():
	return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def register_user():
	if request.method == 'POST':
		name = request.form['name']
		date_of_birth = request.form['date_of_birth']
		date_of_birth_db = dt.datetime.strptime(date_of_birth, '%Y-%m-%d').date()
		phone = int(request.form['phone'])
		gender = request.form['gender']
		nationality = request.form['nationality']

		address_line = request.form['address_line']
		zip_code = int(request.form['zip_code'])
		city = request.form['city']
		state = request.form['state']
		country = request.form['country']

		email = request.form['email']
		password = request.form['password']

		success = reg_users_with_address(name=name,
		                                 date_of_birth=date_of_birth_db,
		                                 gender=gender,
		                                 phone=phone,
		                                 nationality=nationality,
		                                 address_line=address_line,
		                                 zip_code=zip_code,
		                                 city=city,
		                                 state=state,
		                                 country=country,
		                                 email=email,
		                                 password=password)
		if success:
			return render_template('success.html')
		else:
			return render_template('failure.html')
	return redirect(url_for('register_user'))


if __name__ == '__main__':
	app.run(debug=True)