import json

class Perkenalan:
    def __init__(self, nama, kampus):
        self.nama = nama
        self.kampus = kampus

def untuk_menambah():
    nama = input("Masukkan Nama: ")
    kampus = input("Masukkan Asal kampus: ")
    return Perkenalan(nama, kampus)

