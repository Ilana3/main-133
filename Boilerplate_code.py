#Importando o módulo flask no projeto
from flask import Flask, render_template

#Crie um objeto da classe Flask
app = Flask(__name__)

#A função route() da classe  Flask
@app.route("/Student_Activity2")

# A URL ‘/’ é ligada à função first_flask.
def student_webpage():
    name = "Ilana"
    return render_template('Student_Activity2.html', student_name = name)

# Execute a aplicação no servidor local
app.run()
