from flask import Flask

app = Flask(__name__)

desenvolvedores = [

    {"nome":"Matheus",
     "habilidades":["Python", "Flask"]},
    {"nome":"Azevedo",
     "habilidades":["Python", "Django"]}
]
@app.route("/dev")
def desenvolvedor():
    return jsonify({"name":"Matheus"})
if __name__ == '__main__':
    app.run(debug=True)