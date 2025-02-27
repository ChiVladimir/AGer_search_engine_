def root_cleaning(root):
    hook_1 = root.find("/")
    hook_2 = root.find("&")

    return f'@{root[(hook_1 + 1):hook_2]}$'

'''
То есть вместо
да/да1/даж&дать
должно быть 
@да1/даж$

'''

print (root_cleaning("да/да1/даж&дать"))