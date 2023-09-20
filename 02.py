# https://automatetheboringstuff.com/2e/

print(2**10)

for promena in [1, 2, 3, 4, 5]:
    print (promena)

for promena in range (5):
    print(promena)        

#mocneni pomoci for cyklu
zaklad = 2

for x in range(10):
    zaklad =zaklad * 2

print(zaklad)

soucet = 0

for cislo in range(1, 101):
    soucet = soucet + cislo

print(soucet)

socet = 0
for cislo in range(1, 51):
    prvni = cislo
    druhe = 101 - cislo
    celkem_pricteme = prvni + druhe
    soucet = soucet + celkem_pricteme

print(soucet)