**Plant Blog**

***Sovelluksen tarkoitus:***

Kasviblogi, jossa voi pitää kirjaa omista kasveista ja niiden hoidosta.

Käyttäjä voi luoda tunnukset sivuille ja kirjautua sisään ja ulos
- Kirjautumisessa on pieniä rajoituksia käyttäjänimen ja salasanan pituudessa
- Tietoturvallinen toteutus

Käyttäjä voi lisätä pääsivullensa kasvin lomakkeen kautta.
- Kasvin luonnille on lomake, johon voi täytää esimerkiksi latinankielisen nimen, veden ja valon tarpeen sekä lisätä hyödyllistä tietoa. 
- Lomakkeen täytön jälkeen tiedot tallentuvat kasvin omalle sivulle, johon voi lisätä muistiinpanoja ja lisätietoa.
- Pääsivun vasempaan laitaan tulee luettelo kaikista lisäämistäsi kasveista ja linkit niihin.
- Voit hakea tiettyä kasvia nimellä hakukoneesta.
- Kasvi on mahdollista poistaa.
- Erilaisista kasveista löytyy sivun ylälaidassa lisätietoa. 


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

```
flask run
```


Jos käynnistyksessä ilmenee ongelmia, voit testata psql pyörimisen komennolla: start-pg.sh
