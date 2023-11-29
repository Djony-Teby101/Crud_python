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

def update_items(data, id, updated_item):
    for i in range(len(data)):
        if data[i]['id']==id:
            data[i]=updated_item
            break
    return data

# => Modifier une data.

updated_item={
        "id": 1,
        "name": "Day-teby",
        "age": 24
    }

data=update_items(data, 1, updated_item)
save_data(file_name, data)
print("modifié!")
