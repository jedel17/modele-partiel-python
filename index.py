from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
liste=[]
premiereCommande=[]
commandesuivante=1
commandeSuivante=[]

@app.route('/')
def page_index():
    return render_template('index.html')

@app.route('/saisiecommande',methods=['GET','POST'])
def page_saisiecommande():
    if request.method=='POST':
        global liste
        data = request.form.to_dict()
        liste.append(data)
        premierecommande=liste[0]
        premiereCommande.append(premierecommande)
        for commandesuivante in liste:
            commandesuivante=len(liste)-1
            commandesuivante=liste[commandesuivante]
            commandeSuivante.append(commandesuivante)
            print(commandesuivante)
        if 'enregistrer' in data:
            return redirect(url_for('page_livraison'))
    return render_template('saisiecommande.html')

@app.route('/livraison',methods=['GET','POST'])
def page_livraison():
    if request.method == 'POST':
        global liste
        data = request.form.to_dict()
        if 'button_terminer' in data:
            premierecommande = liste[0]
            premierecommande = premierecommande + 1
            premiereCommande.append(premierecommande)
            commandesuivante = commandesuivante - premierecommande
            for commandesuivante in liste:
                commandesuivante = len(liste) - 1
                commandesuivante = liste[commandesuivante]
                commandeSuivante.append(commandesuivante)
                print(commandesuivante)
    return render_template('livraison.html',premierecommande=premiereCommande,commandesuivante=commandeSuivante)