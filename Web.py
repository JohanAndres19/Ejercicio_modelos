from flask  import Flask, render_template,request
import json
app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/cursos')
def Cursos():
    imagenes=['/static/img/baloncesto.jfif','/static/img/futbol.jfif','/static/img/karate.jfif','/static/img/natacion.jfif','/static/img/patinaje.jfif','/static/img/squash.webp','/static/img/Taekwondo.jfif','/static/img/Tenis_campo.jfif','/static/img/ultimate.jfif']
    return render_template('cursos.html',imagenes=imagenes)

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/ajax-login',methods=['POST'])
def ajax_login():
    aux= "hola mundo"
    print(request.form)
    return json.dumps(aux)

@app.route('/singin')
def singin():
    return "hola mundo"

if __name__ == "__main__":
    app.run(port=8000, debug=True )