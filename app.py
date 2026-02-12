from flask import Flask, render_template, request, session
import json

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'  # Nécessaire pour utiliser session

# ------------------------------------------------------------
# Données des établissements (Université de l'Itasy)
# ------------------------------------------------------------
ecoles = [
    {
        "nom": "Institut Supérieur des Arts, des Lettres et des Sciences Humaines",
        "filières": [
            {"nom": "Communication écotourisme", "bac_requis": "toutes séries"},
            {"nom": "Communication territoriale", "bac_requis": "toutes séries"}
        ]
    },
    {
        "nom": "Institut Supérieur des Sciences et Technologies",
        "filières": [
            {"nom": "Sciences et techniques de l'eau", "bac_requis": ["D","C","OSE","Technique agricole"]},
            {"nom": "Gestion et valorisation des ressources naturelles", "bac_requis": ["D","C","OSE","A2","Technique"]},
            {"nom": "Gestion de l'environnement", "bac_requis": ["D","C","OSE","A2","Technique"]}
        ]
    },
    {
        "nom": "Institut Supérieur Paramédical de Soavinandriana Itasy",
        "filières": [
            {"nom": "Sage femme", "bac_requis": ["D","C","S","A1"]},
            {"nom": "Infirmier généraliste", "bac_requis": ["D","C","S","A1"]}
        ]
    },
    {
        "nom": "École Supérieure d'Économie, de Droit et de Gestion",
        "filières": [
            {"nom": "Economie", "bac_requis": "toutes séries"},
            {"nom": "Droit", "bac_requis": "toutes séries"},
            {"nom": "Gestion", "bac_requis": "toutes séries"}
        ]
    },
    {
        "nom": "École Supérieure d'Ingénierie de l'Itasy",
        "filières": [
            {"nom": "Agro-écologie", "bac_requis": ["D","C","S","Technique agricole"]},
            {"nom": "Bâtiments et travaux publics", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Élevage", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Énergie renouvelable", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Informatique", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Mécanisation agricole", "bac_requis": ["D","C","S","Technique agricole", "industriel"]},
            {"nom": "Mines et environnement", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Sciences et techniques des matériaux", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Télécommunications", "bac_requis": ["D","C","S","Technique"]},
            {"nom": "Transformation agroalimentaire", "bac_requis": ["D","C","S","Technique agricole", "industriel"]}
        ]
    }
]

# ------------------------------------------------------------
# Routes
# ------------------------------------------------------------
@app.route('/')
def orientation():
    """Page principale avec les 6 catégories."""
    return render_template('orientation.html')

@app.route('/resultats', methods=['POST'])
def resultats():
    """Calcule les filières accessibles en fonction de la série de bac."""
    # Récupération des données du formulaire
    bac_type = request.form.get('bac_type')
    serie = request.form.get('serie')
    
    # Si "toutes séries" est coché ou série non précisée, on passe en revue
    eligible_filieres = []
    
    for ecole in ecoles:
        for filiere in ecole["filières"]:
            requis = filiere["bac_requis"]
            if requis == "toutes séries":
                eligible_filieres.append((ecole["nom"], filiere["nom"]))
            elif isinstance(requis, list):
                if serie in requis:
                    eligible_filieres.append((ecole["nom"], filiere["nom"]))
    
    return render_template('resultats.html', 
                         filieres=eligible_filieres,
                         bac_choisi=f"{bac_type} - {serie}" if serie else bac_type)

if __name__ == '__main__':
    app.run(debug=True)