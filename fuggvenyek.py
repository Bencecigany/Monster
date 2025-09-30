import random

def szornyekesfegyverek():
    # Játékos adatai
    harcos_neve = input("Add meg a harcos nevét: ")
    eletpont = 5
    
    print(f"\n🗡️  Üdvözöllek, {harcos_neve}! Készen állsz a harcra? 🗡️")
    print("=" * 50)
    
    # Három harc
    for harc_szam in range(1, 4):
        print(f"\n⚔️  {harc_szam}. HARC ⚔️")
        print("-" * 30)
        
        # Szörny kiválasztása
        szörnyek = ["sárkány", "troll", "boszorkány"]
        szörny = random.choice(szörnyek)
        print(f"🐉 Megjelent egy {szörny}!")
        
        # Fegyver választás
        fegyver = input("⚡ Válaszd ki a fegyvert (varázspálca, íj, kard): ")
        
        # Harc eredménye
        gyozott = False
        if szörny == "troll" and fegyver == "kard":
            gyozott = True
        elif szörny == "boszorkány" and fegyver == "íj":
            gyozott = True
        elif szörny == "sárkány" and fegyver == "varázspálca":
            gyozott = True
        
        # Életpont változás
        if gyozott:
            print("🎉 GYŐZELEM! +1 életpont")
            eletpont += 1
        else:
            print("💀 VERESÉG! -2 életpont")
            eletpont -= 2
        
        # Tulajdonságlap megjelenítése
        print("\n" + "=" * 50)
        print("📋           TULAJDONSÁGLAP           📋")
        print("=" * 50)
        print(f"🏆 Harcos neve:      {harcos_neve}")
        print(f"⚔️  Választott fegyver: {fegyver}")
        print(f"❤️  Életpont:        {eletpont}")
        print("=" * 50)
        
        # Ellenőrzés, hogy él-e még
        if eletpont <= 0:
            print(f"\n💀 {harcos_neve} meghalt! Játék vége! 💀")
            return
        
        if harc_szam < 3:
            input("\nNyomj Enter-t a következő harchoz...")
    
    # Végeredmény
    print(f"\n🎊 Gratulálok {harcos_neve}! Túlélted mind a 3 harcot!")
    print(f"🏆 Végső életpontjaid: {eletpont}")
    
    if eletpont >= 5:
        print("🌟 Kiváló teljesítmény! Igazi harcos vagy!")
    elif eletpont >= 3:
        print("👍 Jól harcoltál!")
    else:
        print("😅 Szerencséd volt, hogy túlélted!")

# Játék indítása
szornyekesfegyverek()




