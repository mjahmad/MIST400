from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def home():
    return '''
        <form action="/echo" method="post">
            <input type="text" name="data" placeholder="Enter some text">
            <input type="submit">
        </form>
    '''
@app.route('/echo', methods=['POST'])
def echo():
    user_input = request.form['data']
    # Directly returning user input without escaping
    return f'<p>Your input was: {user_input}</p>'
if __name__ == '__main__':
    app.run(debug=True)
