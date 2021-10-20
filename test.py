# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:33:13 2021

@author: Taslima Diallo
"""

import matplotlib.pyplot as plt
import socket 

hote = "localhost"
port = 12800

serverconnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Création d'une socket.
serverconnexion.connect((hote, port))  # Connexion au serveur

print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = ""
while msg_a_envoyer != "fin":
    dico = {"messi": 1, "cristiano": 1, "mbappe": 1, "neymar": 1}
    msg = ""
    for i in range(0, 100):
        recv = serverconnexion.recv(1024) # reception du message du server avec une taille de 1024 bytes.
        msg += recv.decode("utf-8") # décode les textes
        
    for key in dico.keys():
        dico[key] += msg.count(key)
    playerLists = []
    playerStatics = []

    for key in dico.keys():
        playerLists.append(key)
        playerStatics.append(dico[key])
    
    fig, ax = plt.subplots()
    ax.axis("equal")
    ax.pie([float(v) / sum(playerStatics) for v in playerStatics],
            labels = playerLists,
            autopct="%1.1f pourcents")
    plt.title("Tendance des stars")
    plt.show()
    msg_a_envoyer = input("\nTapez fin pour arreter et entrer pour continuer> ").strip(" ")

print("Fermeture de la connexion")
serverconnexion.close()