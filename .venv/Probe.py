
name = 'data_item_id.txt'

data_item_id = list
with open(name, 'r', encoding='utf-8') as file:
    data_item_id = file.readlines()
    print(len(data_item_id), type(data_item_id))

