# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:44:54 2021

@author: Taslima Diallo
"""

from tweepy import Stream
import socket
import json
import re

# =============================================================================
# Définition des clées authentication twitter.
# =============================================================================
consumer_key = "jRAWxv1Bday8V8HxBfxfOeWB3"
consumer_secret = "veTeonC8U5rfBMVKcoZMWYUXNDZlVrx9rpS9iSaMDQmwdIwYjy"
access_token = "2180188204-fbEaNGt7MGpxO7ds4P7JFHdpoCuYRkLAYVKp3Hl"
access_token_secret = "amU8B0wNNIHew5r0nUpoa2k2nUBF1KndSAzp80x3BjGiE"

class TweetsListener(Stream):
    def __init__(self, csocket, keyword):
        self.client_socket = csocket # création d'un attribut qui reçoit la socket.
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret) # connexion au flux de twitter.
        super().filter(track = keyword, languages = ["en"]) # filtrer les tweets qui nous intéresses.
        
    def on_data(self, data): # Methode redefini de la class Stream qui est déclenché à chaque tweet publier.
        try:
            msg = json.loads( data ) # chargement au format json
            msg = " ".join(re.findall("[a-zA-Z0-9]+", msg["text"])).lower() # utilisation des expressions regulières pour faire enlever les caractères spéciaux.
            print(msg)
            self.client_socket.send(str(msg).encode(encoding= "utf-8")) # envoi du message aux clientq connecter à travers la socket ouverte.
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            
        return True

    def on_error(self, status):
        print(status)
        return True
    
if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Création d'une socket.
    host = ""  # Adresse ip de la la machine
    port = 12800 # Reserver un port pour le service.
    s.bind((host, port)) # Ajouter l'adr et le port au socket.
    
    print("Listening on port: %s" % str(port))
    
    s.listen(5)  # Le nombre de client qui peuvent se connecter au port d'ecoute.
    c_socket, addr = s.accept() # Etablissement de la connexion avec les clients.

    print("Received request from: " + str(addr))

    # Initialisation de la classe d'écoute des streamings.
    TweetsListener(c_socket, keyword = ['football', 'messi', 'cristiano', 'mbappe', 'neymar'])