import random
import time

def clear_screen():
    """Törli a képernyőt a jobb élmény érdekében"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slowly(text, delay=0.03):
    """Lassan írja ki a szöveget drámai hatásért"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_title():
    """Megjeleníti a játék címét"""
    clear_screen()
    title = """
    ⚔️ ═══════════════════════════════════════════════════════════ ⚔️
    ║                                                             ║
    ║               🐉 SZÖRNYEK ÉS FEGYVEREK 🗡️                   ║
    ║                                                             ║
    ║              Egy epikus kaland vár rád!                     ║
    ║                                                             ║
    ⚔️ ═══════════════════════════════════════════════════════════ ⚔️
    """
    print(title)
    time.sleep(2)

def get_player_stats():
    """Bekéri a játékos adatait"""
    show_title()
    print("🌟 Üdvözöllek a Szörnyek és Fegyverek világában! 🌟\n")
    
    harcos_neve = input("⚡ Add meg a harcos nevét: ").strip()
    while not harcos_neve:
        harcos_neve = input("❌ A név nem lehet üres! Add meg a harcos nevét: ").strip()
    
    print(f"\n🎯 Válassz nehézségi szintet, {harcos_neve}!")
    print("1. 🟢 Könnyű (7 életpont)")
    print("2. 🟡 Közepes (5 életpont)")
    print("3. 🔴 Nehéz (3 életpont)")
    
    while True:
        try:
            szint = int(input("\nVálasztás (1-3): "))
            if szint == 1:
                eletpont = 7
                break
            elif szint == 2:
                eletpont = 5
                break
            elif szint == 3:
                eletpont = 3
                break
            else:
                print("❌ Kérlek válassz 1, 2 vagy 3-at!")
        except ValueError:
            print("❌ Kérlek számot adj meg!")
    
    return harcos_neve, eletpont

def show_monster_info(szorny):
    """Megjeleníti a szörny részletes információit"""
    monster_info = {
        "sárkány": {
            "emoji": "🐲",
            "description": "Egy ősi, tűzokádó sárkány! Pikkelyei acélként kemények.",
            "weakness": "varázspálca",
            "strength": "Tűzlehelet és repülés"
        },
        "troll": {
            "emoji": "👹", 
            "description": "Egy brutális, kőkemény bőrű troll! Óriási buzogánnyal támad.",
            "weakness": "kard",
            "strength": "Brutális erő és regeneráció"
        },
        "boszorkány": {
            "emoji": "🧙‍♀️",
            "description": "Egy gonosz boszorkány sötét mágiával! Átkokat szór.",
            "weakness": "íj",
            "strength": "Sötét mágia és illúziók"
        }
    }
    
    info = monster_info[szorny]
    print(f"\n{info['emoji']} ═══ {szorny.upper()} MEGJELENT! ═══ {info['emoji']}")
    print_slowly(info['description'])
    print(f" Erőssége: {info['strength']}")
    print("⚠️  Gondold át jól, melyik fegyvert választod! ⚠️")

def get_weapon_choice():
    """Fegyver választás részletes leírásokkal"""
    print("\n🛡️  FEGYVERTÁR 🛡️")
    print("=" * 40)
    print("1. ⚡ Varázspálca - Mágikus energia, hatásos sárkányok ellen")
    print("2. 🏹 Íj - Gyors és precíz, távoli támadás")  
    print("3. ⚔️  Kard - Közelharc mestere, éles penge")
    
    weapons = {"1": "varázspálca", "2": "íj", "3": "kard"}
    
    while True:
        choice = input("\nVálaszd ki a fegyvered (1-3): ").strip()
        if choice in weapons:
            return weapons[choice]
        else:
            print("❌ Kérlek válassz 1, 2 vagy 3-at! ❌")

def battle_sequence(szorny, fegyver):
    """Drámai harci szekvencia"""
    print(f"\n⚔️  HARC KEZDŐDIK! ⚔️")
    print("=" * 50)
    
    print_slowly(f" Előreszáladsz a {fegyver}oddal...")
    time.sleep(1)
    
    
    battle_events = [
        f" A szörny váratlanul támad!",
        f" Villámgyors mozdulattal reagálsz!",
        f" Célzol a gyenge pontjára...",
        f" Hatalmas csapás!"
    ]
    
    for event in battle_events:
        print_slowly(event)
        time.sleep(0.8)

def szornyekesfegyverek():
    """Főjáték függvény"""
    show_title()
    harcos_neve, eletpont = get_player_stats()
    max_eletpont = eletpont
    ossz_gyozelem = 0
    
    clear_screen()
    print_slowly(f"\n🗡️  Üdvözöllek, {harcos_neve}! Készen állsz a harcra? 🗡️")
    print("=" * 60)
    input("\n📖 Nyomj Enter-t a kaland kezdéséhez...")
    
    
    
    for harc_szam in range(1, 4):
        clear_screen()
        print(f"\n⚔️ ═══════ {harc_szam}. HARC ═══════ ⚔️")
        print(f"💖 Jelenlegi életpontjaid: {eletpont}")
        print("-" * 50)
        
       
        szörnyek = ["sárkány", "troll", "boszorkány"]
        szörny = random.choice(szörnyek)
        
        
        show_monster_info(szörny)
        input("\n⏳ Nyomj Enter-t a felkészüléshez...")
        
      
        fegyver = get_weapon_choice()
        
       
        battle_sequence(szörny, fegyver)
        
        
        gyozott = False
        if szörny == "troll" and fegyver == "kard":
            gyozott = True
            print_slowly("🎯 KRITIKUS TALÁLAT! A kard áthatolt a troll kemény bőrén!")
        elif szörny == "boszorkány" and fegyver == "íj":
            gyozott = True
            print_slowly("🏹 HEADSHOT! A nyíl eltalálta a boszorkány szívét!")
        elif szörny == "sárkány" and fegyver == "varázspálca":
            gyozott = True
            print_slowly("⚡ MÁGIKUS ROBBANÁS! A varázspálca megsemmisítette a sárkányt!")
        else:
            veresg_uzenetek = [
                f"💀 A {szörny} túl erős volt a {fegyver}hoz képest!",
                f"😵 A {fegyver} nem volt elég hatásos!",
                f"🩸 A {szörny} súlyosan megsebesített!"
            ]
            print_slowly(random.choice(veresg_uzenetek))
        
        time.sleep(2)
        

        if gyozott:
            print("\n🎉 ═══ GYŐZELEM! ═══ 🎉")
            gyozelem_bonus = random.randint(1, 2)
            eletpont += gyozelem_bonus
            ossz_gyozelem += 1
            print(f"💚 +{gyozelem_bonus} életpont szerzett!")
            
        
            if gyozelem_bonus == 2:
                print("🌟 DUPLA BÓNUSZ! Tökéletes harci technika!")
        else:
            print("\n💀 ═══ VERESÉG! ═══ 💀")
            sebzes = random.randint(1, 3)
            eletpont -= sebzes
            print(f"❤️‍🩹 -{sebzes} életpont elveszett!")
        
      
        print("\n" + "=" * 60)
        print("📋                TULAJDONSÁGLAP                📋")
        print("=" * 60)
        print(f"🏆 Harcos neve:        {harcos_neve}")
        print(f"⚔️  Választott fegyver:   {fegyver}")
        print(f"❤️  Életpont:          {eletpont}/{max_eletpont}")
        print(f"🏅 Győzelmek száma:    {ossz_gyozelem}")
        
       
        if eletpont >= max_eletpont * 0.8:
            print(" Állapot: Kiváló")
        elif eletpont >= max_eletpont * 0.5:
            print(" Állapot: Jó")
        elif eletpont >= max_eletpont * 0.3:
            print(" Állapot: Gyenge")
        else:
            print("💀 Állapot: Kritikus")
        
        print("=" * 60)
        
        
        if eletpont <= 0:
            print(f"\n💀 ═══ JÁTÉK VÉGE ═══ 💀")
            print_slowly(f"{harcos_neve} hősiesen harcolt, de legyőzték...")
            print(f"🏆 Győzelmek száma: {ossz_gyozelem}/3")
            return
        
        if harc_szam < 3:
            input("\n⏭️  Nyomj Enter-t a következő harchoz...")
    
    
    clear_screen()
    print("🎊 ═══════════════════════════════════════ 🎊")
    print("║                                         ║")
    print("║           KALAND TELJESÍTVE!            ║") 
    print("║                                         ║")
    print("🎊 ═══════════════════════════════════════ 🎊")
    
    print_slowly(f"\n� Gratulálok {harcos_neve}! Túlélted mind a 3 harcot!")
    print(f"🏆 Végső életpontjaid: {eletpont}")
    print(f"🥇 Győzelmek száma: {ossz_gyozelem}/3")
    
  
    if ossz_gyozelem == 3:
        print("👑 TÖKÉLETES TELJESÍTMÉNY! Minden szörnyet legyőztél!")
        rang = "Legenda"
    elif ossz_gyozelem == 2:
        print("🌟 KIVÁLÓ! Majdnem tökéletes volt!")
        rang = "Mester"
    elif ossz_gyozelem == 1:
        print("👍 JÓL HARCOLTÁL! Van még mit fejleszteni.")
        rang = "Harcos"
    else:
        print("😅 SZERENCSÉD VOLT! Gyakorolj még!")
        rang = "Túlélő"
    
    print(f"\n🎖️  Elért rang: {rang}")
    
    
    print("\n" + "=" * 50)
    ujra = input("� Szeretnél újra játszani? (i/n): ").lower().strip()
    if ujra == 'i' or ujra == 'igen':
        szornyekesfegyverek()
    else:
        print_slowly("\n👋 Köszönöm, hogy játszottál! Viszlát!")

if __name__ == "__main__":
    try:
        szornyekesfegyverek()
    except KeyboardInterrupt:
        print("\n\n👋 Játék megszakítva. Viszlát!")
    except Exception as e:
        print(f"\n❌ Hiba történt: {e}")
        print("Kérlek indítsd újra a játékot!")




