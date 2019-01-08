stak=[] #lista z orginalami
pun = [] #lista z punktami dla oryginalow
liczb = [] #lista z puntami ogolnie
etr=0
a=0 #Indeks wszystkich
b=0 #Indeks oryginalnych
c=0 #Indeks printa
def multi_input():
    try:
        while True:
            data=raw_input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return

pelen = list(multi_input()) ##Wprowadzenie danych z ankiety, wszystkie odpowiedzi


stak = [item for item in pelen if item not in stak] ##tworzy liste z oryginalami
stak = [e[2:] for e in stak]  ##usuwa z listy 2 dwa znaki(punkty i spacje)

for i in stak:
    pun.append(0)

for i in pelen:
    liczb.append(int(pelen[etr][0]))  ##tworzy tablice liczb, skladajaca sie z pierwszych liter tablicy pelen, skonwertowanych na inta
    etr=etr+1



for i in pun:
    for i in pelen:
        if stak[b]==pelen[a][2:]:
            pun[b] = liczb[a] + pun[b]  ##Dodaje punkty do tablicy z wynikami
        a=a+1
    b=b+1
    a=0




for i in stak:
    print(stak[c], "dostalo", pun[c], "punktow" )
    c+=1












