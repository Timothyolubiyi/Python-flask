from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/home')
def home():
    return "Welcome to Assignment webpage"

@app.route('/career')
def career():
    careers=["This is the result Important Notice: Please be mindful of fake sites run by fraudulent parties posing as Electric Gigs Technologies or its affiliates. Do not disclose your personal information and financial details to anyone online or anywhere else"]
    return render_template("career.html", career=careers)

 

@app.route('/multiply')
def multiply():
    a=100
    b=50
    c=90
    d=a*b*c
    return "This is the result " + str(d)


@app.route('/mountain')
def mountain():
    mountains=["kilimanjaro", "everest", "idanre hills", "zuma rock", "olumo rock"]
    return render_template("index.html", mountain=mountains)

 






if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5009, debug =True)
