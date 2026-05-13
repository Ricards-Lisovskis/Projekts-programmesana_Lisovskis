from tkinter import *
from math import *
import datetime
import time
import dateutil
import tkinter as tk
from tkinter import messagebox
import threading
import resend
I=1
L=1
Zinas=[]
Laiki=[]
Izpildits=[]
Labelsaraksts=[]
#Daramo darbinu saraksts: vajag settings [], pogu pievienot ierakstu, to uzspiezot paradas teksta lodzins, togglojams atgadinajuma lodzins (default on), poga postot, togglojams atgadinajuma teksta lodzins, togglojams cik reizu un cik pirms/pec laika atgadinat; galvenaja menu ir rindina visi sobrideji atgadinajumi un piezimes, var ieslegt ari rezimus kuros ir tikai viens vai otrs
#Uztaisi lai nevar uzspiest pogu ja nav nekas ievadits
#Oki guys tatad parveido to par unixu un atnem no sobrideja un tad lai programma gul lidz tam laikam, izmet pazinojumu un nem nakamo
#Jauna top ideja ir ka checku uztaisa ik pa minutei, lai nesanak ta ka kamer programma ir aizmigusi tiek pievienots jauns pazinojums kas ir drizak bet netiek piefiksets
#Multithreadingu vrbt vajag? nvm ir jau
#Pievieno checku vai ir pilns viss pirms saglabasanas, default vertibas varbut
#Poga sobridejo laiku panemt, labeli, settingi, epasts, labaka laika izvelne
def IevadeJauns():
    global I
    print("tests")
    if I==1:
        pogaPo.grid(row=2, column=1, padx=10, pady=10)
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
def IevadeJauns2():
    global L
    if L==1:
        c1.grid(row=1, column=2, padx=10, pady=10)
        c2.grid(row=2, column=2, padx=10, pady=10)
        birkaEpasts.grid(row=3, column=2, padx=10, pady=10)
        laucinsEpasts.grid(row=4, column=2, padx=10, pady=10)
        birkaParole.grid(row=5, column=2, padx=10, pady=10)
        laucinsParole.grid(row=6, column=2, padx=10, pady=10)
        L=2
    else:
        c1.grid_remove()
        c2.grid_remove()
        birkaEpasts.grid_remove()
        laucinsEpasts.grid_remove()
        birkaParole.grid_remove()
        laucinsParole.grid_remove()
        L=1
def Saglabat2():
    #for i in (len(Laiki)):
        #print("1")
    now=datetime.datetime.now()
    nowUnix=now.timestamp()
    #print(now)
    #print(nowUnix)
    if int(gads.get()) != "" and int(menesis.get()) != "" and int(diena.get()) != "" and int(stunda.get()) != "" and int(minute.get()) != "" and laucinsZina.get() != "":
        dtJaunaisLaiks=datetime.datetime(int(gads.get()), int(menesis.get()), int(diena.get()), int(stunda.get()), int(minute.get()))
        unixJaunaisLaiks=dtJaunaisLaiks.timestamp()
        tekstsI=laucinsZina.get()
        Laiki.append(unixJaunaisLaiks)
        Zinas.append(tekstsI)
        Izpildits.append(1)
        print(Zinas)
        print(Laiki)
    else:
        print("Aizpildi visus laucinus")

#Cikls laikam
def PatiesamPatiesamSeko():
    while 1+1==2:
        time.sleep(60)
        #for i in range(len(Laiki)):
            #if Izpildits[i]==1:
                #Laiki[i]=Laiki[i]-60
                #if Laiki[i]<=0:
                    #Izpildits[i]=0
        now=datetime.datetime.now()
        nowUnix=now.timestamp()
        print(nowUnix)
        print(Laiki)
        for i in range(len(Laiki)):
            print(Laiki[i])
            if Izpildits[i]==1:
                if Laiki[i]<=nowUnix:
                    if int(varc1.get()) == 1:
                        messagebox.showinfo("Atgadinajums: ", Zinas[i])
                    if int(varc2.get()) == 1:
                        if laucinsEpasts.get() != "" and laucinsParole.get() != "":
                            resend.api_key = laucinsParole.get() 
                            params: resend.Emails.SendParams = {
                                "from": "Acme <onboarding@resend.dev>",
                                "to": [laucinsEpasts.get()],
                                "subject": "Atgadinajums",
                                "html": "Atgadinajums:" + Zinas[i],
                            }
                            email = resend.Emails.send(params)
                            print("Nosutits")
                    Izpildits[i]=0

#messagebox.showinfo("")
#VisiLabeli=[]
LabeluSkaitsKopa=int(1)
#Atseviski labeli piefikse zinas kas pending un izpilditas
                #Un seit te ari notifikacija, un pec tam kaut kur citur iespraud labelus
cikls=threading.Thread(target=PatiesamPatiesamSeko, args=())
cikls.start()

def updateLabel():
    global LabeluSkaitsKopa
    if len(Labelsaraksts)>=1:
        for l in range(len(Labelsaraksts)):
            Labelsaraksts[l].destroy()
            LabeluSkaitsKopa = LabeluSkaitsKopa - 1
    if str(izveletaisFiltrs.get()) == "visas":
        for i in range(len(Zinas)):
            Uzraksts=str("Zina: ") + str(Zinas[i]) + str(" Laiks: ") + str(datetime.datetime.fromtimestamp(Laiki[i]))
            PazinojumaLabelis=Label(window, text=Uzraksts)
            LabeluSkaitsKopa=LabeluSkaitsKopa+1
            PazinojumaLabelis.grid(row=LabeluSkaitsKopa+1, column=0, padx=10, pady=10)
            Labelsaraksts.insert(0, PazinojumaLabelis)
    elif str(izveletaisFiltrs.get()) == "pienakusas":
        for i in range(len(Zinas)):
            if Izpildits[i]==0:
                Uzraksts=str("Zina: ") + str(Zinas[i]) + str(" Laiks: ") + str(datetime.datetime.fromtimestamp(Laiki[i]))
                PazinojumaLabelis=Label(window, text=Uzraksts)
                LabeluSkaitsKopa=LabeluSkaitsKopa+1
                PazinojumaLabelis.grid(row=LabeluSkaitsKopa+1, column=0, padx=10, pady=10)
                Labelsaraksts.insert(0, PazinojumaLabelis)
    elif str(izveletaisFiltrs.get()) == "nepienakusas":
        for i in range(len(Zinas)):
            if Izpildits[i]==1:
                Uzraksts=str("Zina: ") + str(Zinas[i]) + str(" Laiks: ") + str(datetime.datetime.fromtimestamp(Laiki[i]))
                PazinojumaLabelis=Label(window, text=Uzraksts)
                LabeluSkaitsKopa=LabeluSkaitsKopa+1
                PazinojumaLabelis.grid(row=LabeluSkaitsKopa+1, column=0, padx=10, pady=10)
                Labelsaraksts.insert(0, PazinojumaLabelis)
    else:
        print("error3")
tagadne=datetime.datetime.now()
days = [str(d) for d in range(1, 32)]
months = [str(m) for m in range(1, 13)]
years = [str(tagadne.year + i) for i in range(3)]
hours = [str(h).zfill(2) for h in range(24)]
minutes = [str(m).zfill(2) for m in range(60)]
#Minutem varbut saliec lai ir ik pa 5 tikai
print(days)
filtri = ["visas", "pienakusas", "nepienakusas"]
window = Tk()
window.geometry("1000x1000")
minute=tk.StringVar()
stunda=tk.StringVar()
diena=tk.StringVar()
menesis=tk.StringVar()
gads=tk.StringVar()
izveletaisFiltrs=tk.StringVar()
varc1 = tk.IntVar()
varc2 = tk.IntVar()
pogaP = Button(window, text="Pievienot zinu", command=IevadeJauns)
pogaPo = Button(window, text="Saglabat", command=Saglabat2)
pogaS = Button(window, text="Iestatijumi", command=IevadeJauns2)
pogaTemp = Button(window, text="Atjauninat sarakstu", command=updateLabel)
izvelneFiltri=OptionMenu(window, izveletaisFiltrs, *filtri)
laucinsZina=Entry(window)
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
c1 = tk.Checkbutton(window, text="Pop-up lodzins",variable=varc1, onvalue=1, offvalue=0)
c2 = tk.Checkbutton(window, text="E-pasts",variable=varc2, onvalue=1, offvalue=0)
birkaEpasts=Label(window, text="E-pasta adrese:")
laucinsEpasts=Entry(window)
birkaParole=Label(window, text="Resend API key:")
laucinsParole=Entry(window)
pogaP.grid(row=0, column=1, padx=10, pady=10)
pogaS.grid(row=0, column=2, padx=10, pady=10)
pogaTemp.grid(row=0, column=0, padx=10, pady=10)
izvelneFiltri.grid(row=1, column=0, padx=10, pady=10)
window.mainloop()
