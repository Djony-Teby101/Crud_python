# travaux pratique realisation d'un crud
# etape 1: Lire le fichier json
import json

#fonction de traitement
def load_data(file_name):
    with open(file_name, 'r') as file:
        data=json.load(file)
    return data


#definir le path
file_name='data.json'

#application de la fonction de traitement

data=load_data(file_name)

#Verification du resultat
if data != None:
    print('requete succesfull')
    #display la data
    print(data)
    