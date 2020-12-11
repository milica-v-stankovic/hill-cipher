UPUTSTVO ZA RAD SA PROGRAMIMA ZA ŠIFRIRANJE I DEŠIFROVANJE POMOĆU HILOVOG ŠIFRATORA

U okviru direktorijuma "hill-cipher" se nalaze skripte koje vrše šifriranje i dešifrovanje reči korišćenjem Hilovog šifratora.

Za pokretanje programa za šifriranje, nephodno je imati python3 interpreter, kao i instaliranu numpy biblioteku.
Ukoliko nemate instaliranu numpy biblioteku, potebno je uraditi sledeće u terminalu:

```
pip3 install numpy
```

Pokretanje programa za šifriranje se vrši na sledeći način:


```
python3 cipher.py
```

Pokretanje programa za dešifriranje se vrši na sledeći način:

```
python3 decipher.py
```

Kada je pokrenut, zatražiće putanju do fajla koji sadrži ključ. Ukoliko se ne unese ništa, podrazumevaće da je ključ na putanji "keys/key.txt". Format ključa mora biti kao što je dat u primeru na toj putanji.

Program za šifriranje je ograničen na rad sa velikim slovima engleskog alfabeta (A-Z) i u slučaju reči koja ima druge karaktere, tražiće ponovan unos. Za razliku od programa za šifriranje, program za dešifriranje će prihvatiti velika slova engleskog alfabeta, kao i karaktere <, =, >, ? i @. Takođe, kod programa za dešifrovanje, dužina reči mora biti deljiva sa 3.

Oba programa će vršiti proveru ključa. Ukoliko je ključ neodgovarajući, odnosno nemoguće je naći inverznu matricu, program će prestati sa radom i prijaviti poruku da ključ nije validan. Ukoliko je ključ validan, prikazaće se rezujtujuća reč.

