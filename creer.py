import json
file_name='data.json'

def load_data(file_name):
    with open(file_name, 'r') as file:
        data=json.load(file)
    return data

def add_item(data, item):
    data.append(item)
    return data

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data,file, indent=4)


data=load_data(file_name)


#Ajouter un items
new_item={"id":3,'name':'Payrolle-teby','age':19}
data=add_item(data, new_item)
save_data(file_name, data)
print("operation d'ajout effectué")

