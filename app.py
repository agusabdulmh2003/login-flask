from flask import Flask, url_for, render_template, request, redirect, session
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


# @app.route('/', methods=['GET'])
# def index():
#     if session.get('logged_in'):
#         return render_template('home.html')
#     else:
#         return render_template('index.html', message="Hello!")


# @app.route('/register/', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         try:
#             db.session.add(User(username=request.form['username'], password=request.form['password']))
#             db.session.commit()
#             return redirect(url_for('login'))
#         except:
#             return render_template('index.html', message="User Already Exists")
#     else:
#         return render_template('register.html')


# @app.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         u = request.form['username']
#         p = request.form['password']
#         data = User.query.filter_by(username=u, password=p).first()
#         if data is not None:
#             session['logged_in'] = True
#             return redirect(url_for('index'))
#         return render_template('index.html', message="Incorrect Details")


# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     session['logged_in'] = False
#     return redirect(url_for('index'))

# if(__name__ == '__main__'):
#     app.secret_key = "ThisIsNotASecret:p"
#     # db.create_all()
#     app.run()


from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def transliterate_to_javanese(text):
    javanese_mapping = {
        'a': 'ꦲ', 'b': 'ꦧ', 'c': 'ꦕ', 'd': 'ꦢ',
        'e': 'ꦲꦺ', 'f': 'ꦥ꦳', 'g': 'ꦒ', 'h': 'ꦲ',
        'i': 'ꦲꦶ', 'j': 'ꦗ', 'k': 'ꦏ', 'l': 'ꦭ',
        'm': 'ꦩ', 'n': 'ꦤ', 'o': 'ꦲꦺꦴ', 'p': 'ꦥ',
        'q': '꧀', 'r': 'ꦂ', 's': 'ꦱ', 't': 'ꦠ',
        'u': 'ꦲꦸ', 'v': 'ꦮ', 'w': 'ꦮ', 'x': 'ꦼꦏ꧀ꦱ',
        'y': 'ꦪ', 'z': 'ꦗ꦳'
    }
    translated_text = ''.join(javanese_mapping.get(char, char) for char in text.lower())
    return translated_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    translated_text = transliterate_to_javanese(text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
