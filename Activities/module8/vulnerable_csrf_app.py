from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/')
def home():
    return '''
        <form action="/change-email" method="post">
            <input type="email" name="email" placeholder="Enter new email">
            <input type="submit" value="Change Email">
        </form>
    '''
@app.route('/change-email', methods=['POST'])
def change_email():
    new_email = request.form['email']
    # Here, you would normally update the user's email in the database.
    # This example simply returns a success message.
    return make_response(f'Email changed to: {new_email}')
if __name__ == '__main__':
    app.run(debug=True)
