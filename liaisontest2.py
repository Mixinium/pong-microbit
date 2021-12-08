import serial, time

import tkinter as tk

port = "COM3"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud


def demande_temperature():
    s.write(b'temperature')
    data = s.readline()
    data = int(data[0:4])
    print(data)
    texte_temperature.set("Température : "+str(data))

def envoie_message():
    message_bytes = bytes(texte_message.get(), 'utf-8')
    s.write(message_bytes)

def quitter():
    s.close()
    ma_fenetre.destroy()



# Fenêtre principale
ma_fenetre = tk.Tk()

ma_fenetre.title("Titre de la fenetre")
ma_fenetre.geometry("300x200")

# Création d'un bouton pour recuperer la temperature
button_temperature = tk.Button(ma_fenetre, text="Temperature", command=demande_temperature)
button_temperature.grid(row=1, column=0, padx=5, pady=5)

# Creation d'un label pour afficher la temperature
texte_temperature = tk.StringVar()
texte_temperature.set("Température : ")
label_temperature = tk.Label(ma_fenetre, textvariable=texte_temperature , bg="grey")
label_temperature.grid(row=1, column=1, padx=5, pady=5)

# Création d'un bouton pour envoyer un message
button_message = tk.Button(ma_fenetre, text ="Envoyer", command=envoie_message)
button_message.grid(row=2, column=1, padx=5, pady=50)

# Création d'un champ de saisie d'un message
texte_message = tk.StringVar()
texte_message.set('coucou')
champ_message = tk.Entry(ma_fenetre, textvariable=texte_message, bg="bisque", fg="maroon", width="20")
champ_message.focus_set()
champ_message.grid(row=2, column=0, padx=5, pady=5)

# Création d'un bouton Quitter
button_quitter = tk.Button(ma_fenetre, text="Quitter", command=quitter)
button_quitter.grid(row=3,column=0, padx=5, pady=5)

ma_fenetre.mainloop()
