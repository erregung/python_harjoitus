import sqlite3
import time

db = sqlite3.connect("testi.db")
db.isolation_level = None

c = db.cursor()

print("1. Luo sovelluksen tarvitsemat taulut tyhjään tietokantaan (tätä toimintoa voidaan käyttää, kun tietokantaa ei ole vielä olemassa).\n2. Lisää uusi paikka tietokantaan, kun annetaan paikan nimi.\n3. Lisää uusi asiakas tietokantaan, kun annetaan asiakkaan nimi.\n4.  Lisää uusi paketti tietokantaan, kun annetaan paketin seurantakoodi ja asiakkaan nimi. Asiakkaan tulee olla valmiiksi tietokannassa.\n5. Lisää uusi tapahtuma tietokantaan, kun annetaan paketin seurantakoodi, tapahtuman paikka sekä kuvaus. Paketin ja paikan tulee olla valmiiksi tietokannassa.\n6. Hae kaikki paketin tapahtumat seurantakoodin perusteella.\n7. Hae kaikki asiakkaan paketit ja niihin liittyvien tapahtumien määrä.\n8. Hae annetusta paikasta tapahtumien määrä tiettynä päivänä.\n9. Suorita tietokannan tehokkuustesti (tästä lisää alempana).")
while True:
    syote = input("Syötä komento (1-9):")

    if syote == "1":
        #Luodaan taulukot
        try:
            c.execute("CREATE TABLE Paikat (id INTEGER PRIMARY KEY, osoite TEXT UNIQUE)")
            c.execute("CREATE TABLE Asiakkaat (id INTEGER PRIMARY KEY, nimi TEXT UNIQUE, osoite_id INTEGER)")
            c.execute("CREATE TABLE Paketit (id INTEGER PRIMARY KEY, koodi TEXT UNIQUE, asiakas_id INTEGER)")
            c.execute("CREATE TABLE Tapahtumat (id INTEGER PRIMARY KEY, paketti_id INTEGER, paikka_id INTEGER, paiva TEXT, aika TEXT, kuvaus TEXT)")
            print("Tietokanta luotu")
        except:
            print("Tietokanta on jo olemassa.")
    elif syote == "2":
        #Lisätään syöte taulukkoon Paikat
        try:
            paikka = input("Anna paikan nimi:")
            c.execute("INSERT INTO Paikat (osoite) Values (?)",[paikka])
            print("Paikka lisätty")
        except: 
            print("Virhe. Paikka on jo olemassa tai tietokantaa ei ole luotu.")
    elif syote == "3":
        #Lisätään syöte taulukkoon Asiakkaat
        try:
            nimi = input("Anna asiakkaan nimi:")
            c.execute("INSERT INTO Asiakkaat (nimi) Values (?)", [nimi])
            print("Asiakas lisätty")
        except:
            print("Virhe. Asiakas on jo olemassa tai tietokantaa ei ole luotu.")
    elif syote == "4":
        #try:
            #Lisätään syöte taulukkoon Paketit
            koodi = input("Anna paketin seurantakoodi:")
            nimi = input("Anna asiakkaan nimi:")
            c.execute("INSERT INTO Paketit (koodi, asiakas_id) VALUES ('%s', (SELECT B.asiakas_id FROM Paketit B LEFT JOIN Asiakkaat A ON A.id = B.asiakas_id WHERE A.nimi = '%s'));" % (koodi, nimi)) 
            print("Paketti lisätty")
       #except:
            print("Virhe. Koodi on jo lisätty tai asiakasta ei ole.")
    elif syote == "5":
        #Lisätään syöte taulukkoon Tapahtumat
        koodi = input("Anna paketin seurantakoodi:")
        paikka = input("Anna tapahtuman paikka")
        kuvaus = input("Anna tapahtuman kuvaus")
        #SQL-kysely tähän
        print("Tapahtuma lisätty")
    elif syote == "6":
        #Hae kaikki paketin tapahtumat seurantakoodin perusteella
        koodi = input("Anna paketin seurantakoodi:")
        #SQL-kysely tähän (tulostaa tapahtumat)
    elif syote == "7":
        #Hae asiakkaan paketit ja niiden tapahtumamäärä
        nimi = input("Anna asiakkaan nimi")
        #SQL-kysely, tulosta "KOODI + n tapahtumaa"
    elif syote == "8":
        #Paikan tapahtumat tiettynä päivänä
        paikka = ("Anna paikan nimi:")
        aika = ("Anna päivämäärä:")
        #SQL-kysely, joka printtaa tapahtumien määrän kys. ajankohta
    elif syote == "9":
        #Testi suoritettava kahdesti: ensin ilman indeksointia, sitten sen kanssa
        #Suoritettava vaiheet 1 - 4 yhden transaktion sisällä!
        #Vaihe 1
        print("Lisätään 1000 paikkaa")
        start_time = time.time()
        for x in range (1, 1001):
            c.execute("INSERT INTO Paikat (osoite) Values (?)",["P" + str(x)]) 
        #tehokkuustesti
        print("--- %s sekuntia ---" % (time.time() - start_time))
        #Vaihe 2
        print("Lisätään 1000 asiakasta")
        start_time = time.time()
        for x in range (1, 1001):
            c.execute("INSERT INTO Asiakkaat (nimi) Values (?)",["A" + str(x)])
        print("--- %s sekuntia ---" % (time.time() - start_time))
    else:
        break

print("Ohjelman suoritus loppuu.")


