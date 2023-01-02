from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
liste=[]
valider=[]

@app.route('/')
def page_index():
    return render_template('index.html')

@app.route('/saisiecommande',methods=['GET','POST'])
def page_saisiecommande():
    if request.method=='POST':
        global liste
        data = request.form.to_dict()
        if 'enregistrer' in data:
            liste.append(data)
            premierecommande=liste[0]
            print(premierecommande)
            return redirect(url_for('page_livraison'))
    return render_template('saisiecommande.html')

@app.route('/livraison')
def page_livraison():
    return render_template('livraison.html',commande=liste)