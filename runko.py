import sqlite3
import time

db = sqlite3.connect("testi.db")
db.isolation_level = None

c = db.cursor()

print("1. Luo sovelluksen tarvitsemat taulut tyhjään tietokantaan (tätä toimintoa voidaan käyttää, kun tietokantaa ei ole vielä olemassa).\n2. Lisää uusi paikka tietokantaan, kun annetaan paikan nimi.\n3. Lisää uusi asiakas tietokantaan, kun annetaan asiakkaan nimi.\n4.  Lisää uusi paketti tietokantaan, kun annetaan paketin seurantakoodi ja asiakkaan nimi. Asiakkaan tulee olla valmiiksi tietokannassa.\n. Lisää uusi tapahtuma tietokantaan, kun annetaan paketin seurantakoodi, tapahtuman paikka sekä kuvaus. Paketin ja paikan tulee olla valmiiksi tietokannassa.\n6. Hae kaikki paketin tapahtumat seurantakoodin perusteella.\n7. Hae kaikki asiakkaan paketit ja niihin liittyvien tapahtumien määrä.\n8. Hae annetusta paikasta tapahtumien määrä tiettynä päivänä.\n9. Suorita tietokannan tehokkuustesti (tästä lisää alempana).")
while True:
    syote = input("Syötä komento (1-9):")

    if syote == "1":
        try:
            c.execute("CREATE TABLE Paikat (id INTEGER PRIMARY KEY, osoite TEXT)")
            c.execute("CREATE TABLE Asiakkaat (id INTEGER PRIMARY KEY, nimi TEXT, osoite_id INTEGER)")
            c.execute("CREATE TABLE Paketit (id INTEGER PRIMARY KEY, seurantatunnus TEXT, asiakas_id INTEGER)")
            c.execute("CREATE TABLE Tapahtumat (id INTEGER PRIMARY KEY, paketti_id INTEGER, paikka_id INTEGER, kuvaus TEXT)")
            print("Tietokanta luotu")
        except:
            print("Tietokanta on jo olemassa.")
    elif syote == "2":
        paikka = input("Anna paikan nimi:")
        c.execute("INSERT INTO Paikat (osoite) Values (?)",[paikka])
        print("Paikka lisätty")
    elif syote == "3":
        nimi = input("Anna asiakkaan nimi:")
        c.execute("INSERT INTO Asiakkaat (nimi) Values (?)", [nimi])
        print("Asiakas lisätty")
    elif syote == "4":
        koodi = input("Anna paketin seurantakoodi:")
        nimi = input("Anna asiakkaan nimi")
        #SQL-kysely tähän
        print("Paketti lisätty")
    elif syote == "5":
        koodi = input("Anna paketin seurantakoodi:")
        paikka = input("Anna tapahtuman paikka")
        kuvaus = input("Anna tapahtuman kuvaus")
        #SQL-kysely tähän
        print("Tapahtuma lisätty")
    elif syote == "6":
        koodi = input("Anna paketin seurantakoodi:")
        #SQL-kysely tähän (tulostaa tapahtumat)
    elif syote == "7":
        nimi = input("Anna asiakkaan nimi")
        #SQL-kysely, tulosta "KOODI + n tapahtumaa"
    elif syote == "8":
        paikka = ("Anna paikan nimi:")
        aika = ("Anna päivämäärä:")
        #SQL-kysely, joka printtaa tapahtumien määrän kys. ajankohta
    elif syote == "9":
        #tehokkuustesti
        print("Tehokkuustesti")
    else:
        break

print("Ohjelman suoritus loppuu.")

