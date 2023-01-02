from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def page_index():
    return render_template('index.html')

@app.route('/saisiecommande')
def page_saisiecommande():
    return render_template('saisiecommande.html')

@app.route('/livraison')
def page_livraison():
    return render_template('livraison.html')