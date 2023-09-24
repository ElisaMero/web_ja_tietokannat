**Plant Blog**

***Sovelluksen tarkoitus:***

Kasviblogi, jossa voi pitää kirjaa omista kasveista ja kasteluaikatauluista.

Käyttäjä voi luoda tunnukset sivuille ja kirjautua sisään ja ulos
- Kirjautumisessa on rajoitukset käyttäjänimen ja salasanan pituudessa
- Tietoturvallinen toteutus

Käyttäjä voi lisätä pääsivullensa kasvin, jossa linkki kasvin tietosivulle
- Kasvin luonnille on lomake, johon voi täytää esimerkiksi latinankielinen nimi, kasteluaikaväli, mullan koostumus sekä kasvin hankintapäivämäärä
- Lomakkeen täytön jälkeen tiedot tallentuvat kasvin omalle sivulle, johon voi lisätä muistiinpanoja ja lisätietoa
- Lisäksi sivulle ilmestyy kohta, johon voi liittää kuvan kasvista

Ulkopuoliset käyttäjät voivat tarkastella muiden käyttäjien kasvisivuja, muttei voi muokata muiden tietoja. 

***Sovelluksen tämänhetkinen tilanne (Välipalautus 2):***

Käyttäjä voi luoda omat tunnukset sivustolle ja kirjautua sisään ja ulos.

Käyttäjä voi kirjautuneena lisätä kasvin täyttämällä kyselyn kohdasta "Add".

Tietokantaan tallennettujen kasvien lukumäärä näkyy käyttäjälle. 

***Sovelluksen käynnistysohjeet***

Ohjeet otettu tämän kurssin materiaaleista!

Kloonaa repositorio koneellesi -> siirry juurikansioon -> luo .env -tiedosto
Lisää tiedostoon:

DATABASE_URL = < tietokannan-paikallinen-osoite >

SECRET_KEY = < salainen-avain >

Asenna terminaaliin:

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

$ psql < schema.sql

Käynnistä ohjelma komennolla: flask run
 
