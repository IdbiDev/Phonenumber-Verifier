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
> Ha nem emlékeszik a parancsokra, a **help** paranccsal a program a konzolba kiírja!

| Parancs | Leírás |
| --- | --- |
| `file` | A programot **txt** módba rakja. Ebben a módban lehet fájlt beolvasni! |
| `random <valid> <invalid>` | A program generál random telefonszámokat, a megadott paraméterek alapján! (Space elválasztás!) |
| `input` | A programot **beviteli** módba rakja. Ide írhatja az ellenőrizni kívánt telefonszámot! |
| `export` | Az eddigi tárolt telefonszámokat kiírja egy txt fileba (*phonenumbers_export.txt*) |
| `stats` | Táblázatban kiírja a program az eddig tárolt telefonszámokat! |
| `clear` | Törli a tárolt telefonszámokat! |
| `exit` | Kilépés a programból! |
