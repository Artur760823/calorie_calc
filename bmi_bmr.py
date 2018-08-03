waga = int(input("Podaj swoją wagę: "))
wzrost = int(input("Podaj swój wzrost: "))
wiek = int(input("Podaj swój wiek: "))
s = input("Podaj swoją płeć w formacie M lub K: ")
S = 0
if s == "M":
    S = 5
else:
    S = -161

           
BMI = waga/((wzrost/100)**2)

aktywność = {"a":1.2, "b":1.4, "c":1.6, "d":1.8, "e":2.0}
p = input("""Jaką pracę wykonujesz? Podaj porszę odpowiednią literę:
              \na:Praca siedząca, brak dodatkowej aktywności fizycznej.
              \nb:Praca niefizyczna, mało aktywny tryb życia.
              \nc:Lekka praca fizyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu.
              \nd:Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu.
              \ne:Praca fizyczna ciężka, regularne ćwiczenia 7razy w tygodniu
              \n\n Podaj a lub b lub c lub d lub e: """)
ap = aktywność[p]
#print(S) - tylko kontrolnie, aby mieć pewność że warunek działa
PPM = 10 * waga + 6.25 * wzrost - 5 * wiek + S
print("///////////////////////////////////////////////////")
kalorie = PPM * ap
print("""Masa ciała BMI to: {};
\nTwoja podstawowa przemiana materii to około: {};
\nTwoje dzienne zapotrzebowanie na kalorie to: {}. """ .format(round(BMI,2), PPM, kalorie))
