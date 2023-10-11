**Plant Blog**

***Sovelluksen tarkoitus:***

Kasviblogi, jossa voi pitää kirjaa omista kasveista ja niiden hoidosta.

Käyttäjä voi luoda tunnukset sivuille ja kirjautua sisään ja ulos
- Kirjautumisessa on pieniä rajoituksia käyttäjänimen ja salasanan pituudessa
- Tietoturvallinen toteutus

Käyttäjä voi lisätä pääsivullensa kasvin lomakkeen kautta.
- Kasvin luonnille on lomake, johon voi täytää esimerkiksi latinankielisen nimen, veden ja valon tarpeen sekä lisätä hyödyllistä tietoa. 
- Lomakkeen täytön jälkeen tiedot tallentuvat kasvin omalle sivulle, johon voi lisätä muistiinpanoja ja lisätietoa.
- Pääsivun vasempaan litaan tulee luettelo kaikista lisäämistäsi kasveista ja linkit niihin. 


***Sovelluksen tämänhetkinen tilanne (Välipalautus 3):***

Käyttäjä voi luoda omat tunnukset sivustolle ja kirjautua sisään ja ulos.

Käyttäjä voi kirjautuneena lisätä kasvin täyttämällä kyselyn kohdasta "Add".

Tietokantaan tallennettujen kasvien lukumäärä näkyy käyttäjälle. 

Kasvin tietoja voi tarkastella klikkaamalla muodostuneita linkkejä.

Kasville voi antaa lisäohjeita kasvin omalla sivulla. 

***Sovelluksen käynnistysohjeet***

Ohjeet otettu tämän kurssin materiaaleista!

Kloonaa repositorio koneellesi -> siirry juurikansioon -> luo .env -tiedosto
Lisää tiedostoon:

DATABASE_URL = < tietokannan-paikallinen-osoite >

SECRET_KEY = < salainen-avain >

Asenna terminaaliin:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r ./requirements.txt
```

```
psql < schema.sql
```

Käynnistä ohjelma komennolla: flask run
 
