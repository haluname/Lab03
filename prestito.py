class Prestito:
    def __init__(self, codice_prestito, data, id_strumento, cognome_allievo):
        self.codice_prestito = codice_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.codice_prestito}: Strumento {self.id_strumento} all'allievo {self.cognome_allievo} in data {self.data}"
