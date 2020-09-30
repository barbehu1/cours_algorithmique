liste = [1, 2, 3, 4, 5]

def inverse(a):
    print(a)
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            print(a)

inverse(liste)