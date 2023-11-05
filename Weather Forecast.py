import requests
import tkinter as tk
from PIL import ImageTk, Image
import time
import datetime


#listeler
celcius="°C"
pngleme=".png"
tempratures_list=[]
icon_list=[]

#api bölumu
cities=["Istanbul","Ankara","izmir","bursa"]
api_key = 'c160bd87213475bec91107907348edb8'
for city in cities:
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {
            'q': city,
            'appid': api_key,
            'cnt' : 1
        }
    response = requests.get(base_url, params=params)
    x = dict(response.json())
    k = x.get("list")
    c = k[0]
    t = c["main"]
    K = t['temp']
    s=c["weather"]
    Ş=s[0]
    R=Ş["icon"]
    C = K - 273.15
    tempratures_list.append(int(C))
    icon_list.append(f"{R}{pngleme}")



def buttonclicked():
    x=entry1.get()
    params = {
        'q': x,
        'appid': api_key,
        'cnt': 5

    }
    response = requests.get(base_url, params=params)
    f = dict(response.json())
    ü = f.get("message")
    k = f.get("list")

    if x=="SEHİR GİRİNİZ" or x=="" :
        message_box = tk.Toplevel(windows_1)

        message_box.geometry("200x200")
        message_box.configure(bg="red")
        canvas = tk.Canvas(message_box, width=300, height=200, bg="black",)
        canvas.place(x=0,y=0)

        canvas.create_image(0, 0, anchor=tk.NW, image=image_messagebox)

        message_label = tk.Label(message_box, text="Hiçbir giriş yapmadınız!!", font=('Helvetica bold', 12))
        message_label.place(x=15, y=140)

        custom_button = tk.Button(message_box, text="Tamam", command=message_box.destroy, bg="blue")
        custom_button.place(x=75, y=170)
    elif ü=="city not found":
        message_box = tk.Toplevel(windows_1)

        message_box.geometry("200x200")
        message_box.configure(bg="red")
        canvas = tk.Canvas(message_box, width=300, height=200, bg="black", )
        canvas.place(x=0, y=0)

        canvas.create_image(0, 0, anchor=tk.NW, image=image_messagebox)

        message_label = tk.Label(message_box, text="Yanlış şehir ismi!!", font=('Helvetica bold', 12))
        message_label.place(x=40,y=140)

        custom_button = tk.Button(message_box, text="Tamam", command=message_box.destroy, bg="blue")
        custom_button.place(x=75, y=170)

    else:
        tem_list=[]
        ic_list=[]
        for q in list(range(5)):
            ıı = k[q]
            ee = ıı["main"]
            zz = ee["temp"]
            sa = ıı["weather"]
            Şa = sa[0]
            Ra = Şa["icon"]+pngleme
            Ct = zz - 273.15
            sonderece=int(Ct)
            tem_list.append(sonderece)
            ic_list.append(Ra)

        windows_1.destroy()
        windows_2 = tk.Tk()
        windows_2.configure(bg="black")
        windows_2.geometry("400x720")
        windows_2.title("WEATHER FORECAST")
        windows_2.resizable(False, False)

        def backbutton_clicked():
            windows_2.destroy()


        #button

        my_pick7 = Image.open("uzay.jpg")
        resized7 = my_pick7.resize((400, 720), Image.Resampling.LANCZOS)
        resim7 = ImageTk.PhotoImage(resized7)
        my_canvas22 = tk.Canvas(windows_2, width=400, height=720)
        my_canvas22.pack(fill="both", expand=True)
        my_canvas22.create_image(0, 0, image=resim7, anchor="nw")
        my_pickbutton = Image.open("sonnnnnnn.png")
        resizedbutton = my_pickbutton.resize((40, 40), Image.Resampling.LANCZOS)
        resimbutton = ImageTk.PhotoImage(resizedbutton)
        ev_dugmesi = tk.Button(windows_2, image=resimbutton, bg="black",command=backbutton_clicked)
        ev_dugmesi.place(x=10, y=10)

        translation = {"Monday": "PAZARTESİ", "Tuesday": "SALI", "Wednesday": "ÇARŞAMBA", "Thursday": "PERŞEMBE",
                       "Friday": "CUMA", "Saturday": "CUMARTESİ", "Sunday": "PAZAR"}
        # günler
        bügun = tk.Message(master=windows_2, text="BUGÜN", font=("Helvetica", 20), width=400, bg="black", fg="blue")
        bügun.place(x=140, y=200)
        gun_2 = tk.Message(master=windows_2,
                           text=translation[(datetime.date.today() + datetime.timedelta(days=1)).strftime("%A")],
                           font=("Helvetica", 11), width=400, bg="black", fg="blue")
        gun_3 = tk.Message(master=windows_2,
                           text=translation[(datetime.date.today() + datetime.timedelta(days=2)).strftime("%A")],
                           font=("Helvetica", 11), width=400, bg="black", fg="blue")
        gun_4 = tk.Message(master=windows_2,
                           text=translation[(datetime.date.today() + datetime.timedelta(days=3)).strftime("%A")],
                           font=("Helvetica", 11), width=400, bg="black", fg="blue")
        gun_5 = tk.Message(master=windows_2,
                           text=translation[(datetime.date.today() + datetime.timedelta(days=4)).strftime("%A")],
                           font=("Helvetica", 11), width=400, bg="black", fg="blue")
        gun_2.place(x=40, y=330)
        gun_3.place(x=40, y=428)
        gun_4.place(x=40, y=520)
        gun_5.place(x=40, y=620)
        # sehir adı
        sehir_adı = tk.Message(master=windows_2, text=x.upper(), font=("Helvetica", 30), width=400, bg="black", fg="red")
        sehir_adı.place(x=100, y=70)
        # iconlar
        bügün_derece = tk.Message(text=f"{tem_list[0]}{celcius}", font=("Helvetica", 17), width=400, bg="black",
                                  fg="yellow")
        sonraki_1_derece = tk.Message(text=f"{tem_list[1]}{celcius}", font=("Helvetica", 17), width=400, bg="black",
                                      fg="yellow")
        sonraki_2_derece = tk.Message(text=f"{tem_list[2]}{celcius}", font=("Helvetica", 17), width=400, bg="black",
                                      fg="yellow")
        sonraki_3_derece = tk.Message(text=f"{tem_list[3]}{celcius}", font=("Helvetica", 17), width=400, bg="black",
                                      fg="yellow")
        sonraki_4_derece = tk.Message(text=f"{tem_list[4]}{celcius}", font=("Helvetica", 17), width=400, bg="black",
                                      fg="yellow")
        bügün_derece.place(x=210, y=265)
        sonraki_1_derece.place(x=165, y=375)
        sonraki_2_derece.place(x=165, y=465)
        sonraki_3_derece.place(x=165, y=560)
        sonraki_4_derece.place(x=165, y=660)
        # 1

        my_pickbugun = Image.open(ic_list[0])
        resizednugun = my_pickbugun.resize((80, 40), Image.Resampling.LANCZOS)
        resimbugun = ImageTk.PhotoImage(resizednugun)
        LABEL_bugun = tk.Label(image=resimbugun, state="normal", master=windows_2)
        LABEL_bugun.config(highlightthickness=0, borderwidth=0, )
        LABEL_bugun.place(x=130, y=265)
        # 2

        my_pickgun_2 = Image.open(ic_list[1])
        resizedgun_2 = my_pickgun_2.resize((80, 40), Image.Resampling.LANCZOS)
        resimgun_2 = ImageTk.PhotoImage(resizedgun_2)
        LABEL_gun_2 = tk.Label(image=resimgun_2, fg="#FFE8A3", state="normal", master=windows_2)
        LABEL_gun_2.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
        LABEL_gun_2.place(x=90, y=375)
        # 3
        my_pickgun_3 = Image.open(ic_list[2])
        resizedgun_3 = my_pickgun_3.resize((80, 40), Image.Resampling.LANCZOS)
        resimgun_3 = ImageTk.PhotoImage(resizedgun_3)
        LABEL_gun_3 = tk.Label(image=resimgun_3, fg="#FFE8A3", state="normal", master=windows_2)
        LABEL_gun_3.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
        LABEL_gun_3.place(x=90, y=465)
        # 4
        my_pickgun_4 = Image.open(ic_list[3])
        resizedgun_4 = my_pickgun_4.resize((80, 40), Image.Resampling.LANCZOS)
        resimgun_4 = ImageTk.PhotoImage(resizedgun_4)
        LABEL_gun_4 = tk.Label(image=resimgun_4, fg="#FFE8A3", state="normal", master=windows_2)
        LABEL_gun_4.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
        LABEL_gun_4.place(x=90, y=560)
        # 5
        my_pickgun_5 = Image.open(ic_list[0])
        resizedgun_5 = my_pickgun_5.resize((80, 40), Image.Resampling.LANCZOS)
        resimgun_5 = ImageTk.PhotoImage(resizedgun_5)
        LABEL_gun_5 = tk.Label(image=resimgun_5, state="normal", master=windows_2)
        LABEL_gun_5.config(highlightthickness=0, borderwidth=0, )
        LABEL_gun_5.place(x=90, y=660)

        windows_2.mainloop()





windows_1=tk.Tk()
image_messagebox = tk.PhotoImage(file="C:\\Users\\sertf\\Downloads\\imagesss.png")
windows_1.configure(bg="black")
windows_1.geometry("400x720")
windows_1.title("WEATHER FORECAST")
windows_1.resizable(False,False)



#Resim ekleme alanı
my_pick=Image.open("../pythonProject1/sunnaaa.jpeg")
my_pick2=Image.open("uzay.jpg")
resized2=my_pick2.resize((400,720),Image.Resampling.LANCZOS)
resized=my_pick.resize((200,150),Image.Resampling.LANCZOS)
resim=ImageTk.PhotoImage(resized)
resim2=ImageTk.PhotoImage(resized2)
my_canvas=tk.Canvas(windows_1,width=400,height=720)
my_canvas.pack(fill="both",expand=True)
my_canvas.create_image(0,0, image=resim2,anchor="nw")
LABEL_1=tk.Label(image=resim,fg="#FFE8A3",state="normal",master=my_canvas)
LABEL_1.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
LABEL_1.pack(pady=40)
#fonksiyonlar
def on_entry_click(event):
    if entry1.get() == "SEHİR GİRİNİZ":
        entry1.delete(0, "end")  # Varsayılan metni temizle
        entry1.config(fg="black")  # Metin rengini siyah yap

def on_entry_leave(event):
    if entry1.get() == "":
        entry1.insert(0, "SEHİR GİRİNİZ")
        entry1.config(fg="gray")

def update_date():
    current_time = datetime.datetime.now()
    translation={"Monday":"PAZARTESİ","Tuesday":"SALI","Wednesday":"ÇARŞAMBA","Thursday":"PERŞEMBE","Friday":"CUMA","Saturday":"CUMARTESİ","Sunday":"PAZAR"}
    day_of_week = current_time.strftime("%A")
    current_saat = time.localtime().tm_hour
    current_dakika = time.localtime().tm_min
    nebilem=translation[day_of_week]

    date_message.config(text=f"{nebilem} {current_saat}:{current_dakika}")
    windows_1.after(1000, update_date)

#ARAYÜZ DEGİSMEZLERİ
#messages
message1=tk.Message(text="BUGÜN İÇİN BAZI SEHİRLERİN HAVA DURUMU",font=("Helvetica",13),width=400,bg="black",fg="red")
date_message=tk.Message(text="",fg="blue",bg="black",font=("Helvetica",16),width=200)
date_message.place(y=215,x=105)
entry1=tk.Entry(master=my_canvas,width=30,bg="#211F91",)
entry1.insert(0, "SEHİR GİRİNİZ")
entry1.bind("<FocusIn>", on_entry_click)  # Tıklanınca temizle
entry1.bind("<FocusOut>", on_entry_leave)  # Odak dışına çıkınca geri yükle
entry1.place(x=106,y=275)
button1=tk.Button(master=my_canvas,width=5,bg="#211F91",height=1,text="ARA",command=buttonclicked)
button1.place(x=172,y=300)
message1.place(x=13,y=350)
#giris ekrani ilk 4 sehir entrysi
istanbul_adı=tk.Message(text="İSTANBUL",font=("Helvetica",13),width=400,bg="blue",fg="black")
ankara_adı=tk.Message(text="ANKARA",font=("Helvetica",13),width=400,bg="blue",fg="black")
izmir_adı=tk.Message(text="İZMİR",font=("Helvetica",13),width=400,bg="blue",fg="black")
bursa_adı=tk.Message(text="BURSA",font=("Helvetica",13),width=400,bg="blue",fg="black")
istanbul_adı.place(x=153,y=400)
ankara_adı.place(x=160,y=475)
izmir_adı.place(x=168,y=550)
bursa_adı.place(x=162,y=625)
istanbul_derece=tk.Message(text=f"{tempratures_list[0]}{celcius}" ,font=("Helvetica",13),width=400,bg="black",fg="yellow")
ankara_derece=tk.Message(text=f"{tempratures_list[1]}{celcius}",font=("Helvetica",13),width=400,bg="black",fg="yellow")
izmir_derece=tk.Message(text=f"{tempratures_list[2]}{celcius}",font=("Helvetica",13),width=400,bg="black",fg="yellow")
bursa_derece=tk.Message(text=f"{tempratures_list[3]}{celcius}",font=("Helvetica",13),width=400,bg="black",fg="yellow")
istanbul_derece.place(x=240,y=438)
ankara_derece.place(x=240,y=515)
izmir_derece.place(x=240,y=590)
bursa_derece.place(x=240,y=665)
#1

my_pickist=Image.open(icon_list[0])
resizedist=my_pickist.resize((80,40),Image.Resampling.LANCZOS)
resimist=ImageTk.PhotoImage(resizedist)
LABEL_ist=tk.Label(image=resimist,state="normal",master=my_canvas)
LABEL_ist.config(highlightthickness=0, borderwidth=0,)
LABEL_ist.place(x=160,y=431)
#2

my_pickank=Image.open(icon_list[1])
resizedank=my_pickank.resize((80,40),Image.Resampling.LANCZOS)
resimank=ImageTk.PhotoImage(resizedank)
LABEL_ank=tk.Label(image=resimank,fg="#FFE8A3",state="normal",master=my_canvas)
LABEL_ank.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
LABEL_ank.place(x=160,y=508)
#3
my_pickizr=Image.open(icon_list[2])
resizedizr=my_pickizr.resize((80,40),Image.Resampling.LANCZOS)
resimizr=ImageTk.PhotoImage(resizedizr)
LABEL_izr=tk.Label(image=resimizr,fg="#FFE8A3",state="normal",master=my_canvas)
LABEL_izr.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
LABEL_izr.place(x=160,y=582)
    #4
my_pickbur=Image.open(icon_list[3])
resized3=my_pickbur.resize((80,40),Image.Resampling.LANCZOS)
resimbur=ImageTk.PhotoImage(resized3)
LABEL_bur=tk.Label(image=resimbur,fg="#FFE8A3",state="normal",master=my_canvas)
LABEL_bur.config(highlightthickness=0, borderwidth=0, highlightbackground="#FFE8A3")
LABEL_bur.place(x=160,y=660)
update_date()
windows_1.mainloop()







