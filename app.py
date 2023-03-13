from flask import Flask, redirect, url_for, render_template
from data import lottonr
app = Flask(__name__)
app.config.from_object('config')



@app.route('/')
def landingpage():
    return render_template('home.html')

# if back to main page
@app.route('/home')
def home():
    return redirect('http://127.0.0.1:5000/')

# route only login 
@app.route('/login')
def login():
    return render_template('login.html')

#only underconstruktion
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# jinja templating first example
@app.route('/eurojackpot')
def lotto():
    return render_template('eurojackpot.html', lottonr=lottonr)


# das klappt aber nicht innerhalb eine page...
@app.route('/eurojackpot/<day>')
def eurojackpot(day): 

    return render_template(
        'eurojackpotresult.html', 
        mainnr=(lottonr[day]['main']),
        supernr=(lottonr[day]['super']),
        day1 = day
        )

if __name__ == '__main__':
    app.run()

    