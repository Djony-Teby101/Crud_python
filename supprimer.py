import json

file_name='data.json'

def load_data(file_name):
    with open(file_name, 'r') as file:
        data=json.load(file)
    return data

data=load_data(file_name)



def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data,file, indent=4)

def Delete_item(data, id):
    for i in range(len(data)):
        if data[i]['id']==id:
            del data[i]
            break
    return data



# => Supprimer un element.
data=Delete_item(data, 2)
save_data(file_name, data)
print("utilisateur supprimé")