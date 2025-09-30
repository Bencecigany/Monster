import random 

def szornyekesfegyverek():
    szörnyek=["sárkány", "troll", "boszorkány"]
    szörny=random.choice(szörnyek)
    print(f"Szörny: {szörny}")
    fegyver=input("Válaszd ki a fegyvert (varázspálca, íj, kard): ")

    if szörny=="troll" and fegyver=="kard":
        print(f"Nyertél! ")
    elif szörny=="troll" and fegyver=="íj":
        print(f"Vesztettél ")
    elif szörny=="troll" and fegyver=="varázspálca":
        print(f"Vesztettél ")
    elif szörny=="boszorkány" and fegyver=="kard":
        print(f"Vesztettél ")
    elif szörny=="boszorkány" and fegyver=="íj":
        print(f"Nyertél! ")
    elif szörny=="boszorkány" and fegyver=="varázspálca":
        print(f"Vesztettél ")
    elif szörny=="sárkány" and fegyver=="kard":
        print(f"Vesztettél ")
    elif szörny=="sárkány" and fegyver=="íj":
        print(f"Vesztettél ")
    elif szörny=="sárkány" and fegyver=="varázspálca":
        print(f"Nyertél ")
    else:
        print("Nincs ilyen szörny vagy fegyver!")

