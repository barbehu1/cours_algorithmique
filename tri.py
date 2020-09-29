liste = [1, 2, 3, 4, 5]

def inverse(a):
    a.reverse()
    return a

print(inverse(liste))

print(liste)


liste = [1, 2, 3, 4, 5]
b = []

def inverse(a):
    global b
    b = a.reverse()
    return b

print(inverse(liste))

print(liste)