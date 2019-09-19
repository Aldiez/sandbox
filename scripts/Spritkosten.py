"""
Ein Programm entstanden aus Faulheit und Notwendigkeit an Spritkostenrechnern in Python und dem tk Modul.

Autor: Aldiez
Datum: 11.12.18
Version: 0.01
"""

# tkinter GUI
from tkinter import *
from tkinter import messagebox


# die komplexe Mathematik

def Spritkostenrechner(cost,consumption,distance,n_person):
    Verbrauch = (cost * consumption * distance) / 100
    abnutzung = distance/50 #sonst /20
    Verbrauch_abnutzung = Verbrauch + abnutzung
    Verbrauch_person = Verbrauch / n_person
    abnutz_person = Verbrauch_abnutzung / n_person
    return Verbrauch, Verbrauch_abnutzung, Verbrauch_person, abnutz_person


#Eingabefunktion
def click():
    te_kosten = texteingabe_kosten.get() #sammelt den Text aus dem Text-Feld ein
    te_spritverbrauch = texteingabe_spritverbrauch.get()
    te_entfernung_strecke = texteingabe_entfernung_strecke.get()
    te_anzahl_personen = texteingabe_anzahl_personen.get()

    try:
        te_kosten = float(te_kosten.replace(",","."))
        te_spritverbrauch = float(te_spritverbrauch.replace(",","."))
        te_entfernung_strecke = float(te_entfernung_strecke.replace(",","."))
        te_anzahl_personen = float(te_anzahl_personen.replace(",","."))
    except:
        te_kosten = float(0)
        te_spritverbrauch = float(0)
        te_entfernung_strecke = float(0)
        te_anzahl_personen = float(1)
        messagebox.showerror("Falsche Eingabe","Bitte nur Zahlen eingeben")

    Rechnung = Spritkostenrechner(te_kosten,te_spritverbrauch,te_entfernung_strecke,te_anzahl_personen)

    output_Gesamtverbrauch.delete(0.0, END)
    output_Gesamtverbrauch.insert(END, str(Rechnung[0]))
    output_VerbrauchPerson.delete(0.0, END)
    output_VerbrauchPerson.insert(END, str(Rechnung[2]))
    output_VerbrauchAbnutzung.delete(0.0, END)
    output_VerbrauchAbnutzung.insert(END, str(Rechnung[1]))
    output_VerbrauchPA.delete(0.0, END)
    output_VerbrauchPA.insert(END, str(Rechnung[3]))

## Hauptfenster
gui = Tk()
gui.title("Spritkostenrechner")
gui.configure(background="black")


# erstelle Label
Label(gui, text="Kosten Benzin/Diesel in Euro: ", bg="black", fg="white").grid(row=1, column=0, sticky=W)
Label(gui, text="Spritverbrauch deines Autos in Liter: ", bg="black", fg="white").grid(row=2, column=0, sticky=W)
Label(gui, text="Entfernung der Strecke in km: ", bg="black", fg="white").grid(row=3, column=0, sticky=W)
Label(gui, text="Gesamtzahl mitfahrender Personen in ... Ganz: ", bg="black", fg="white").grid(row=4, column=0, sticky=W)


# erstelle Texteingabebox
texteingabe_kosten = Entry(gui, width=15, bg="white")
texteingabe_kosten.grid(row=1,column=1,sticky=W)
texteingabe_spritverbrauch = Entry(gui, width=15, bg="white")
texteingabe_spritverbrauch.grid(row=2,column=1,sticky=W)
texteingabe_entfernung_strecke = Entry(gui, width=15, bg="white")
texteingabe_entfernung_strecke.grid(row=3,column=1,sticky=W)
texteingabe_anzahl_personen = Entry(gui, width=15, bg="white")
texteingabe_anzahl_personen.grid(row=4,column=1,sticky=W)

# Zusätzlich submit-Button
Button(gui, text="Berechne", width=6, command=click).grid(row=5, column=2, sticky=W)


# Antwortfeld
Label(gui, text="Gesamtverbrauch in Euro: ", bg="black", fg="white").grid(row=7, column=0, sticky=W)
output_Gesamtverbrauch = Text(gui, width=30, height=1, wrap=WORD, bg="white", fg="red")
output_Gesamtverbrauch.grid(row=8, column=0, sticky=W)

Label(gui, text="Verbrauch pro Person: ", bg="black", fg="white").grid(row=7, column=1, sticky=W)
output_VerbrauchPerson = Text(gui, width=30, height=1, wrap=WORD, bg="white", fg="red")
output_VerbrauchPerson.grid(row=8, column=1, sticky=W)

Label(gui, text="Verbrauch mit Abnutzung: ", bg="black", fg="white").grid(row=10, column=0, sticky=W)
output_VerbrauchAbnutzung = Text(gui, width=30, height=1, wrap=WORD, bg="white", fg="red")
output_VerbrauchAbnutzung.grid(row=11, column=0, sticky=W)

Label(gui, text="Verbrauch pro Person mit Abnutzung: ", bg="black", fg="white").grid(row=10, column=1, sticky=W)
output_VerbrauchPA = Text(gui, width=30, height=1, wrap=WORD, bg="white", fg="red")
output_VerbrauchPA.grid(row=11, column=1, sticky=W)

### starte die Hauptschleife
gui.mainloop()
