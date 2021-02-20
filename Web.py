from flask  import Flask, render_template,request,redirect
import json
from flask.helpers import url_for

app = Flask(__name__)
from imagenes import *

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/cursos')
def Cursos():
    return render_template('cursos.html',imagenes=caragar_imagenes().get_imagenes())

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        return redirect(url_for('singin'))
    return render_template('login.html')


@app.route('/ajax-login',methods=['POST'])
def ajax_login():
    aux= request.form["username"]
    if aux== "Johan Aguirre":
        print("si entra")
        """
        direccion='/singin'
        return json.dumps(direccion) """      
        return json.dumps("/singin") 

@app.route('/singin')
def singin():
    return render_template('singin.html',imagenes=caragar_imagenes().get_imagenes())


if __name__ == "__main__":
    app.run(port=8000, debug=True )