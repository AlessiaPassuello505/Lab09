import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analisi(self, e):
        distanza = self._view.txt_dist.value
        try:
            x_soglia = float(distanza)
        except ValueError:
            self._view.create_alert("Inserire un valore numerico per la distanza")
            return

        self._model.buildGraphPesato(x_soglia)
        # Recupero statistiche dal modello
        n_nodi, n_archi = self._model.get_info_grafo()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con successo!"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {n_nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {n_archi}"))

        # Elenco di tutti gli archi con distanza
        self._view.txt_result.controls.append(ft.Text("\nElenco delle rotte e distanze medie:"))
        archi = self._model._grafo.edges(data=True)  #PRENDO TUTTE LE INFO
        for u, v, data in archi:
            distanza = data['weight']  # chiave del dizionario
            # u e v sono oggetti Aeroporto, usiamo i loro attributi per la stampa
            self._view.txt_result.controls.append(
                ft.Text(f"{u.AIRPORT} -- {v.AIRPORT} | Distanza media: {distanza:.2f}")
                )
        self._view.update_page()

