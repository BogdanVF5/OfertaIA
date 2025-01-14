from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def generate_offer(client_request):
    offer_template = f"""
    Oferta pentru firma - Test 1

    I. Scopul documentului:

    Această ofertă preliminară este bazată pe informațiile pe care ni le-ați furnizat. Înainte de a începe efectiv dezvoltarea și de a vă putea oferi o estimare exactă a costurilor și timpului necesar, va fi necesar să parcurgem câteva etape esențiale de planificare:

    1. Elaborarea unei diagrame logice pentru a defini arhitectura aplicației.
    2. Crearea unei diagrame ER pentru a structura baza de date.
    3. Realizarea unui design inițial în Figma pentru a elimina orice ambiguitate legată de interfața grafică.

    Pentru începerea etapelor de mai sus, va fi necesar să semnăm un contract de colaborare și să achitați în avans prețul acestora:

    Diagrama logică și diagrama ER: X Euro + TVA
    Proiectul în Figma: X Euro + TVA
    Acești bani se vor scădea din prețul total de dezvoltare odată acceptată oferta fermă.

    Oferta de mai jos este doar orientativă și urmărește să vă ofere o perspectivă asupra modului în care operăm și a costurilor probabile. Pentru o ofertă și un timp de implementare exact, va fi necesar să completăm etapele de planificare menționate

    Definiții:
    ● React:
    ○ React este o bibliotecă JavaScript pentru construirea interfețelor de utilizator. Este utilizată pentru crearea unor interfețe de utilizator reactive și eficiente din punct de vedere al performanței.

    ● Ionic:
    ○ Ionic este un framework open-source pentru dezvoltarea de aplicații mobile hibride. Utilizează tehnologii web precum JavaScript/React/Angular pentru a construi aplicații pentru platforme mobile, cum ar fi iOS și Android.

    ● NestJS:
    ○ NestJS este un framework pentru dezvoltarea de aplicații server-side cu Node.js. Este construit pe baza arhitecturii modulare și utilizează TypeScript pentru a oferi un cod bine structurat și ușor de întreținut.

    ● Firebase:
    ○ Firebase este o platformă de dezvoltare a aplicațiilor mobile. Furnizează servicii precum bază de date în timp real, autentificare, stocare și hosting, facilitând dezvoltarea rapidă și scalabilă a aplicațiilor.

    ● MongoDB:
    ○ MongoDB este un sistem de gestionare a bazelor de date NoSQL, orientat pe documente. În loc de tabele, MongoDB folosește colecții și documente JSON-like, oferind flexibilitate și scalabilitate în stocarea datelor.

    ● API (Interfață de Programare a Aplicațiilor):
    ○ API reprezintă un set de reguli și protocoale care permit comunicarea între diferite componente ale software-ului/aplicației. Este folosit pentru a permite integrarea între diferite aplicații sau servicii, facilitând schimbul de informații și funcționalități între ele.

    II. Propunere structură (335 Ore - 2 Programatori):

    1. Dezvoltarea de bază:
    a. Dezvoltarea aplicațiilor folosind tehnologii moderne, cum ar fi React cu Ionic pentru interfața utilizatorului și MongoDB/Firebase pentru baza de date si NestJs pentru back-end.
    b. Conectare utilizatori cu autentificare OTP prin SMS/email pentru securitate sporită.

    2. Aplicație Client (iOS și Android):
    a. Căutare Restaurante: Utilizatorii pot căuta restaurante pe baza locației, tipului de bucătărie.
    b. Plasare Comenzi: Interfață intuitivă pentru a selecta articole din meniul restaurantului și plasa comanda cu opțiuni precum adăugarea în coș și gestionarea comenzilor anterioare.
    c. Urmărire Livrare: Funcționalitate de monitorizare a comenzilor în timp real, cu notificări și informații despre stadiul livrării.
    d. Recenzii și Evaluări: Utilizatorii pot lăsa recenzii și evaluări pentru restaurantele și livrările lor.
    e. Legare API Stripe pentru Plata cu Cardul: Implementarea unei interfețe de plată folosind API-ul Stripe pentru a permite utilizatorilor să plătească cu cardul.
    f. Stocare Carduri: Opțiunea pentru utilizatori de a salva informațiile cardului pentru a facilita plățile ulterioare și a oferi o experiență de plată mai rapidă.
    g. Opțiune de Plată Ramburs: Posibilitatea pentru utilizatori de a alege opțiunea de plată la livrare.

    3. Aplicație Rider (iOS și Android):
    a. Acceptare Comenzi: Interfață pentru a accepta sau refuza comenzile, cu informații detaliate despre adresa de livrare și conținutul comenzii.
    b. Gestionare Livrări: Funcționalitate cu informații în timp real despre stadiul comenzii.
    c. Raportare Financiară: Funcționalitate pentru a genera rapoarte financiare, inclusiv livrari zilnice și lunare.
    d. Interfață de Navigare: Integrare cu sisteme de navigare pentru a ajuta riderul în timpul livrării (Legare API Google Maps).

    4. Aplicație Restaurant (iOS și Android):
    a. Gestionare Meniu: Interfață pentru a adăuga, șterge sau modifica articolele din meniu, inclusiv prețuri și disponibilitate.
    b. Confirmare Livrări: Posibilitatea de a confirma comenzile și de a oferi informații despre timpul de pregătire și de livrare.
    c. Raportare Financiară: Funcționalitate pentru a genera rapoarte financiare, inclusiv vânzări zilnice și lunare.

    5. Aplicație Admin (Doar Browser):
    a. Gestionare Utilizatori: Crearea și gestionarea conturilor de utilizator, inclusiv drepturile de acces.
    b. Gestionare Restaurante: Crearea și gestionarea restaurantelor.
    c. Gestionare Rider: Crearea și gestionarea riderilor.
    d. Monitorizare Comenzi: Interfață pentru a monitoriza comenzile în timp real și a rezolva problemele semnalate de utilizatori.
    e. Rapoarte și Analize: Generarea de rapoarte și analize financiare, inclusiv vânzări zilnice și lunare.

    III. Sugestii suplimentare (24 ore de munca * 2 programatori):
    1. Generarea automată a facturilor: Legare la API SmartBill pentru a genera automat facturile pentru rideri, restaurante și clienți.

    IV. Pret și timp de implementare:

    *Fiecare punct poate fi supus modificării, editării sau realizării într-un mod mai sumar, cu reducerea funcționalităților, în vederea obținerii unei costuri mai reduse.

    *Prețul este orientativ și nu trebuie să fie limitativ; în cazul în care bugetul beneficiarului este mai restrâns decât oferta noastră în faza de proiectare, putem identifica alternative la costuri inferioare prin integrarea unui număr redus de funcționalități.

    Timp estimat de livrare:
    - Dezvoltare de bază împreună cu aplicațiile Client, Rider, Restaurant și Admin (355 Ore cu 2 Programatori): X Euro + TVA

    - Dezvoltare de bază împreună cu aplicațiile Client, Rider, Restaurant și Admin și sugestii suplimentare (379 Ore cu 2 Programatori): X Euro + TVA

    Timpul de livrare este influențat de complexitatea proiectului și cerințele dumneavoastră. Vom lucra în strânsă colaborare cu dumneavoastră pentru a respecta termenele stabilite.

    *În cadrul actualei oferte, beneficiați de serviciile a doi programatori specializați în limbajul de programare necesar pentru proiectul dumneavoastră, un manager de proiect care va concepe și coordona proiectul, precum și un grafician responsabil de conceperea interfeței utilizatorului/aplicației. Fiecare echipă din cadrul societății noastre dispune de suportul unui mentor, responsabil de supravegherea și asistarea programatorilor. Prețul pentru această echipă este de X de euro pe oră.

    Termeni de achiziție:

    1. Această ofertă este strict confidențială. Veziv IT Services SRL nu oferă permisiunea de a împărtăși detalii cu terțe părți.
    2. Prețurile sunt fără TVA.

    Data ofertei: {datetime.datetime.now().strftime('%d %B %Y')}
    """

    return offer_template

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        client_request = request.form['client_request']
        offer = generate_offer(client_request)
        return render_template('index.html', offer=offer, client_request=client_request)
    return render_template('index.html', offer=None)

if __name__ == '__main__':
    app.run(debug=True)
