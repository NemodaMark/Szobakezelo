import ctypes

# Beállítások
cim = "Ádám és Csaba - Beadandó dráma"

# Történet elmesélése függvény
def MeseldEl(szoveg):
    ctypes.windll.user32.MessageBoxW(0, szoveg, cim, 0)

# Döntés megjelenítése függvény
def KeprezzDontest(szoveg1, szoveg2):
    valasztottGombok = ctypes.windll.user32.MessageBoxW(0, szoveg1 + "\n\n" + szoveg2, cim + " - Döntés", 36)
    if valasztottGombok == 6:  # Igen
        MeseldEl("Rendben.")
        Wert = 1
    else:  # Nem
        MeseldEl("Rendben.")
        Wert = 2
    return Wert

# Játék kezdése
MeseldEl("Te vagy Ádám, informatika szakos diák.\n" +
         "Közeledik a programozási beadandó határideje, és a legjobb barátod/párod, Csaba mellett dolgozol a projekten.\n" +
         "Csaba aggódik a kód tisztasága és karbantarthatósága miatt, te pedig egy elegánsabb megoldást javasolsz.")

# Első döntési pont
valasztottKimenet = KeprezzDontest("Egyetértesz Csaba aggályaival, és közösen dolgoztok egy kompromisszumos megoldáson.",
                                   "Ragaszkodsz az eredeti ötletedhez, és meggyőzöd Csaba-t az előnyeiről.")

# Elágazás a döntés alapján
if valasztottKimenet == 1:  # Kompromisszumos megoldás
    MeseldEl("Rendben, leültök és kidolgoztok egy olyan megoldást, amely mindkettőtök igényeit kielégíti.\n" +
             "A kód hatékony és elegáns lesz, ugyanakkor könnyen olvasható és karbantartható.\n" +
             "A beadandót időben befejezzitek, és mindketten jó jegyet kaptok.")
    MeseldEl("Gratulálok! A csapatmunka sikert hozott.")
else:  # Ragaszkodás az ötlethez
    MeseldEl("Megpróbálod meggyőzni Csaba-t az ötleted előnyeiről, de ő szkeptikus marad.\n" +
             "Végül úgy döntötök, hogy megosztjátok a feladatot. Te megírod a kód magját, Csaba pedig a dokumentációt és a teszteket készíti el.\n" +
             "Sikerül befejezni a beadandót a határidő előtt, de a kód kissé kusza lesz Csaba aggodalmai miatt.\n" +
             "A tanár értékeli az ötletet, de levon pontot a kód tisztaságáért. Végül átlagos jegyet kaptok.")
    MeseldEl("A konfliktus miatt ugyan nem lett tökéletes a beadandó, de azért teljesítettétek.")

# Játék vége
MeseldEl("A beadandó leadása után Csaba bocsánatot kér a makacsságáért. Te is belátod, hogy jobb lett volna együtt dolgozni.\n" +
         "Elhatározzátok, hogy a következő projekten elejétől fogva együttműködtök.")
