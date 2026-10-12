from strumento import Strumento
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile
        self.strumenti = [] 
        self.prestiti = [] 

    def carica_file_strumenti(self, file_path):
        file = open(file_path, "r", encoding="utf-8")
        for riga in file:
            riga = riga.strip()
            if riga != "":
                pezzi = riga.split(",")
                codice = pezzi[0]
                tipo = pezzi[1]
                marca = pezzi[2]
                anno = int(pezzi[3])
                valore = float(pezzi[4])
                
                strumento = Strumento(codice, tipo, marca, anno, valore)
                self.strumenti.append(strumento)
        file.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        numero = len(self.strumenti) + 1
        codice = "S" + str(numero)
        strumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.strumenti.append(strumento)
        return strumento

    def strumenti_ordinati_per_marca(self):
        return sorted(self.strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        strumento_trovato = None
        for s in self.strumenti:
            if s.codice == id_strumento:
                strumento_trovato = s
                break
                
        if strumento_trovato is None:
            raise Exception(f"Errore: Lo strumento {id_strumento} non esiste.")

        for p in self.prestiti:
            if p.id_strumento == id_strumento:
                raise Exception(f"Errore: Lo strumento {id_strumento} è già in prestito.")

        numero = len(self.prestiti) + 1
        id_prestito = "P" + str(numero)
        
        prestito = Prestito(id_prestito, data, id_strumento, cognome_allievo)
        self.prestiti.append(prestito)
        return prestito

    def termina_prestito(self, id_prestito):
        prestito_trovato = None
        for p in self.prestiti:
            if p.codice_prestito == id_prestito:
                prestito_trovato = p
                break
                
        if prestito_trovato is None:
            raise Exception(f"Errore: Il prestito {id_prestito} non esiste.")
            
        self.prestiti.remove(prestito_trovato)