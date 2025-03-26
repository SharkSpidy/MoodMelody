from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JJ@07092005'

class NameForm(FlaskForm):
    name = StringField("Enter Your Name:", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/form', methods = ['GET', 'POST'])
def form():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return f"Hello, {name}!"
    return render_template('form.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
