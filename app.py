from flask import Flask,render_template,request
app = Flask(__name__) 

@app.route('/hello')
def helloworld():
    return "Hello world"

@app.route('/index')
def indexRoute():
    return render_template("index.html")


@app.route('/add')
def addition():
    n1= int(request.args.get("num1"))
    n2= int(request.args.get("num2"))
    return str(n1+n2)

@app.route('/sub')
def sub():
    n1= int(request.args.get("num1"))
    n2= int(request.args.get("num2"))
    return str(n1-n2)

@app.route('/Multiplication')
def Multiplication():
    n1= int(request.args.get("num1"))
    n2= int(request.args.get("num2"))
    return str(n1*n2)


if __name__ == "__main__":
     app.run(debug=True,port=80)
