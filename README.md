# Telefonszám Ellenőrző
Ez a project a gyvakk által kiadott feladat megoldása!
## Alap működés
A program **konzol**, és bevitt parancsok alapján működik. A program célja a megadott telefonszám kategorizálása. Ez többféle képpen lehetséges benne: Fájl beolvasás, a beépített generátor használata, vagy kézzel által megadott bevitel.
A bevitt telefonszámokat a program tárolja mindaddig amíg leállítjuk, vagy kitöröljük a __clear__ parancs használával. A tárolt, feldolgozott telenszámokat bármikor el lehet érni formázott alakban, illetve képes exportálni egy TXT fileba.
> [!CAUTION]
> A program **kizárólag** magyar telefonszámokat ismer fel, ha ez nem felel meg akkor a program **INVALID**-nak nyílvánítja!
## Parancsok / Bevitel
A program indítása után egyből lehet parancsokat beírni neki.
```
Kérem a parancsot > 
```
> [!NOTE]
> Ha nem emlékezik a parancsokra a **help** parancsal a program a konzolba is kiírja!

| Parancs | Leírás |
| --- | --- |
| `txt` | A programot **txt** módba rakja. Ebben a módban hozzá lehet férni az fájl beolvasáshoz és a random generáláshoz! |
| `input` | A programot **beviteli** módba rakja. Ide írhatja az ellenőrizni kívánt telefonszámot! |
| `stats` | Táblázatban kiírja a program az eddig tárolt telefonszámokat! |
| `clear` | Törli a tárolt telefonszámokat! |
| `exit` | Kilépés a programból! |
### TXT Mód
Ezek a parancsok **TXT módban** használhatóak!
| Parancs | Paraméter | Leírás |
| --- | --- | --- |
| `random` | \<valid\> \<invalid\> | Generál egy TXT file-t amiben random telefonszámok vannak. Az első szám valid telefonszámok mennyiségét, a másik az invalid telefonszámok mennyiségét határozza meg! (Space elválasztás)

> [!NOTE]
> Ha **TXT** módban nem parancsot írunk akkor egy file-t fog keresni a bevitt értékre.
