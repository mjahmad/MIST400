from flask import Flask, request, render_template_string
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
    # Auto-escape user input by rendering through a template
    return render_template_string('<p>Your input was: {{ user_input }}</p>', user_input=user_input)
if __name__ == '__main__':
    app.run(debug=True)
