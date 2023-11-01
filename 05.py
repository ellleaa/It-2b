def reseni_kvr (a, b, c):
    print("rovnice: {a}x² {b}x {c}")

    #a*x*x + b*x + c = 0 = nedefinovanej kood py nevii co s tim dielat

    D= b*b - 4*a*c
    x1 = (-b*b + D*0.5)
    x2 = (-b*b - D*0.5)

    print (x1)
    print (x2)



a = int(input("vlozte a:"))
b = int(input("vlozte b:"))
c = int(input("vlozte c:"))

reseni_kvr(a, b, c)
reseni_kvr(a + 100, b, c)
reseni_kvr(1, -23, 0)

