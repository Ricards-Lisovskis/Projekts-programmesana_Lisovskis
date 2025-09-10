from tkinter import *
from math import *
import datetime
import time
import dateutil
import tkinter as tk
from tkinter import messagebox
import threading
I=1
Zinas=[]
Laiki=[]
Izpildits=[]
#Daramo darbinu saraksts: vajag settings [], pogu pievienot ierakstu, to uzspiezot paradas teksta lodzins, togglojams atgadinajuma lodzins (default on), poga postot, togglojams atgadinajuma teksta lodzins, togglojams cik reizu un cik pirms/pec laika atgadinat; galvenaja menu ir rindina visi sobrideji atgadinajumi un piezimes, var ieslegt ari rezimus kuros ir tikai viens vai otrs
#Uztaisi lai nevar uzspiest pogu ja nav nekas ievadits
#Oki guys tatad parveido to par unixu un atnem no sobrideja un tad lai programma gul lidz tam laikam, izmet pazinojumu un nem nakamo
#Jauna top ideja ir ka checku uztaisa ik pa minutei, lai nesanak ta ka kamer programma ir aizmigusi tiek pievienots jauns pazinojums kas ir drizak bet netiek piefiksets
def IevadeJauns():
    global I
    print("tests")
    if I==1:
        pogaPo.grid(row=2, column=1, padx=10, pady=10)
        laucinsLaiks.grid(row=3, column=1, padx=10, pady=10)
        laucinsZina.grid(row=4, column=1, padx=10, pady=10)
        birkaMinutes.grid(row=5, column=1, padx=10, pady=10)
        izvelneMinutes.grid(row=6, column=1, padx=10, pady=10)
        birkaStundas.grid(row=7, column=1, padx=10, pady=10)
        izvelneStundas.grid(row=8, column=1, padx=10, pady=10)
        birkaDienas.grid(row=9, column=1, padx=10, pady=10)
        izvelneDienas.grid(row=10, column=1, padx=10, pady=10)
        birkaMenesi.grid(row=11, column=1, padx=10, pady=10)
        izvelneMenesi.grid(row=12, column=1, padx=10, pady=10)
        birkaGadi.grid(row=13, column=1, padx=10, pady=10)
        izvelneGadi.grid(row=14, column=1, padx=10, pady=10)
        I=2
    else:
        pogaPo.grid_remove()
        laucinsLaiks.grid_remove()
        laucinsZina.grid_remove()
        birkaMinutes.grid_remove()
        izvelneMinutes.grid_remove()
        birkaStundas.grid_remove()
        izvelneStundas.grid_remove()
        birkaDienas.grid_remove()
        izvelneDienas.grid_remove()
        birkaMenesi.grid_remove()
        izvelneMenesi.grid_remove()
        birkaGadi.grid_remove()
        izvelneGadi.grid_remove()
        I=1
def Postot():
    print("wahoo")
def Saglabat():
    tekstsI=laucinsZina.get()
    laiksI=laucinsLaiks.get()
    print("Zina:", tekstsI, "Laiks:", laiksI)
    laiksI2=1
    #Zinas.append(tekstsI)
    #Laiki.append(laiksI2)
    print(Zinas)
    print(Laiki)
def Saglabat2():
    #for i in (len(Laiki)):
        #print("1")
    now=datetime.datetime.now()
    nowUnix=now.timestamp()
    print(now)
    print(nowUnix)
#Logika
    #for i in----------



    dtJaunaisLaiks=datetime.datetime(int(gads.get()), int(menesis.get()), int(diena.get()), int(stunda.get()), int(minute.get()))
    unixJaunaisLaiks=dtJaunaisLaiks.timestamp()
    tekstsI=laucinsZina.get()
    Laiki.append(unixJaunaisLaiks)
    Zinas.append(tekstsI)
    Izpildits.append(1)
    print(Zinas)
    print(Laiki)

    Mazakais=min(Laiki)
    for i in range(len(Laiki)):
        if Laiki[i]==Mazakais:
            Rit=i
    print(Rit)

#Cikls laikam
def PatiesamPatiesamSeko():
    time.sleep(60)
    #for i in range(len(Laiki)):
        #if Izpildits[i]==1:
            #Laiki[i]=Laiki[i]-60
            #if Laiki[i]<=0:
                #Izpildits[i]=0
    now=datetime.datetime.now()
    nowUnix=now.timestamp()
    for i in range(len(Laiki)):
        if Izpildits[i]==1:
            if Laiki[i]<=nowUnix:
                print("Es esmu debug zina")
                #IzveidotLabeli()
                global LabeluSkaitsKopa
                Uzraksts=("Zina:", Zinas[i], "Laiks:", Laiki[i])
                PazinojumaLabelis=Label(window, text=Uzraksts)
                LabeluSkaitsKopa=LabeluSkaitsKopa+1
                PazinojumaLabelis.grid(row=LabeluSkaitsKopa, column=0, padx=10, pady=10)
                messagebox.showinfo("Atgadinajums:", Zinas[i])

#messagebox.showinfo("")
#VisiLabeli=[]
LabeluSkaitsKopa=int(1)
def IzveidotLabeli():
    global LabeluSkaitsKopa
    #if Izpildits[i]==1 tad nomaini tekstu prieksa zinai
    Uzraksts=str("Zina:", Zinas[i], "Laiks:", Laiki[i])
    #Varbut vajadzetu parveidot uz parasto no Unix atpakal
    PazinojumaLabelis=label(window, text=Uzraksts)
    LabeluSkaitsKopa=LabeluSkaitsKopa+1
    PazinojumaLabelis.grid(row=LabeluSkaitsKopa, column=0, padx=10, pady=10)
#    VisiLabeli.insert(0, PazinojumaLabelis)
#    for row, n in enumerate 
#Atseviski labeli piefikse zinas kas pending un izpilditas
                #Un seit te ari notifikacija, un pec tam kaut kur citur iespraud labelus
#Parraksti programmu lai laiki paliek nemainigi un gettaims ir saja cikla ieksa
cikls=threading.Thread(target=PatiesamPatiesamSeko, args=())
cikls.start()

def PatiesamSeko():
    Skaititajs=((Rit)-(now))
    time.sleep(Skaititajs)
    print("Ludzu strada")
def Settings():
    print("Settings")
def wahoo():
    print("Wahoo")
tagadne=datetime.datetime.now()
days = [str(d) for d in range(1, 32)]
months = [str(m) for m in range(1, 13)]
years = [str(tagadne.year + i) for i in range(3)]
hours = [str(h).zfill(2) for h in range(24)]
minutes = [str(m).zfill(2) for m in range(60)]
#Minutem saliec lai ir ik pa 5 tikai
print(days)
window = Tk()
window.geometry("1000x1000")
minute=tk.StringVar()
stunda=tk.StringVar()
diena=tk.StringVar()
menesis=tk.StringVar()
gads=tk.StringVar()
pogaP = Button(window, text="Pievienot zinu", command=IevadeJauns)
pogaPo = Button(window, text="Saglabat", command=Postot)
pogaI = Button(window, text="Ievadi zinu", command=Saglabat)
pogaS = Button(window, text="Iestatijumi", command=Settings)
pogaTemp = Button(window, text="Vietas aiznemejs", command=Saglabat2)
laucinsLaiks=Entry(window)
laucinsZina=Entry(window)
birka1=Label(window, text="tests")
birkaMinutes=Label(window, text="Minute")
izvelneMinutes=OptionMenu(window, minute, *minutes)
birkaStundas=Label(window, text="Stunda")
izvelneStundas=OptionMenu(window, stunda, *hours)
birkaDienas=Label(window, text="Diena")
izvelneDienas=OptionMenu(window, diena, *days)
birkaMenesi=Label(window, text="Menesis")
izvelneMenesi=OptionMenu(window, menesis, *months)
birkaGadi=Label(window, text="Gads")
izvelneGadi=OptionMenu(window, gads, *years)
pogaP.grid(row=0, column=1, padx=10, pady=10)
pogaI.grid(row=1, column=1, padx=10, pady=10)
pogaS.grid(row=0, column=2, padx=10, pady=10)
birka1.grid(row=1, column=0, columnspan=1, padx=10, pady=10)
pogaTemp.grid(row=0, column=0, padx=10, pady=10)
window.mainloop()
