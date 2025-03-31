from flask import Flask, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a_very_secret_key'
csrf = CSRFProtect(app)
class EmailForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Change Email')
@app.route('/', methods=['GET', 'POST'])
def home():
    form = EmailForm()
    if form.validate_on_submit():
        new_email = form.email.data
        # Here, you would normally update the user's email in the database.
        # This example simply returns a success message.
        return f'Email changed to: {new_email}'
    return render_template_string('''
        <form method="post">
            {{ form.hidden_tag() }}
            <input type="email" name="email" placeholder="Enter new email">
            <input type="submit" value="Change Email">
        </form>
    ''', form=form)
if __name__ == '__main__':
    app.run(debug=True)
