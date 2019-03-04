def mezcla(A,B):
    C = dict()
    for key, value in A.items():
        C[key]=value
    for key, value in B.items():
        if key in C:
            C[key] = (C[key], value)
        else:
            C[key]=value        
    return C


# A = {'x': 1, 'y': 2, 'z': 3} 
# B = {'x': 2, 's': 6, 't': 4} 

# print(mezcla(A,B))