from flask import Flask, request, jsonify, render_template
from users import users_blue
app = Flask(__name__)
app.register_blueprint(users_blue)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html',content={"GET": 'args'})
    else:
        form = request.form
        return jsonify({"POST": form})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=10086, debug=True)
