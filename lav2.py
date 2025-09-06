import tkinter as tk
from tkinter import messagebox
bandas_db = {}
import random
id = random.randint(1000,9999)

#.
#---------------------------------------------------------------------------------------------------------------------
class Participante:
    def __init__(self, name, institution):
        super().__init__()
        self.name = name
        self.institution = institution

    def mostrar_info(self):
        return f"Nombre: {self.name}, Institución: {self.institution}"


class BandaEscolar(Participante):
    def __init__(self, name, institution, categoria):
        super().__init__(name, institution)
        self._category = categoria


        self._points_ritmo = 0
        self._points_uniformidad = 0
        self._points_coreografia = 0
        self._points_alineacion = 0
        self._points_puntualidad = 0

        self.total = 0
        self.avg = 0

    @property
    def categoria(self):
        return self._category
    @categoria.setter
    def categoria(self, new_cat):
        if new_cat.lower() != "basico" or new_cat.lower() != "diversificado" or new_cat.lower() != "primaria":
            print("No es una categoria válida...")
        else:
            self._category = new_cat

    @property
    def puntaje_rit(self):
        return self._points_ritmo
    @puntaje_rit.setter
    def puntaje_rit(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje>10:
            print("Puntaje no válido")
        else:
            self._points_ritmo = nuevo_puntaje

    @property
    def puntaje_unifor(self):
        return self._points_uniformidad
    @puntaje_unifor.setter
    def puntaje_unifor(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje > 10:
            print("Puntaje no válido")
        else:
            self._points_uniformidad = nuevo_puntaje

    @property
    def puntaje_coreo(self):
        return self._points_coreografia
    @puntaje_coreo.setter
    def puntaje_coreo(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje > 10:
            print("Puntaje no válido")
        else:
            self._points_coreografia = nuevo_puntaje

    @property
    def puntaje_ali(self):
        return self._points_alineacion
    @puntaje_ali.setter
    def puntaje_ali(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje > 10:
            print("Puntaje no válido")
        else:
            self._points_alineacion = nuevo_puntaje

    @property
    def puntaje_punt(self):
        return self._points_puntualidad
    @puntaje_punt.setter
    def puntaje_punt(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje > 10:
            print("Puntaje no válido")
        else:
            self._points_puntualidad = nuevo_puntaje


    def mostrar_info(self):
        return f"Nombre: {self.name}| Institución: {self.institution}|Categoría: {self._category}"



class Concurso:
    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Toplevel(ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x300")

        etiqueta1 = tk.Label(ventana_inscribir, text="Escribe el nombre de tu banda: ")
        etiqueta1.pack(pady=5)
        entrada1 = tk.Entry(ventana_inscribir)
        entrada1.pack(pady=5)

        etiqueta2 = tk.Label(ventana_inscribir, text="Escribe la institución: ")
        etiqueta2.pack(pady=5)
        entrada2 = tk.Entry(ventana_inscribir)
        entrada2.pack(pady=5)

        etiqueta3 = tk.Label(ventana_inscribir, text="Escribe la categoría (Basico/Diversificado/Primaria): ")
        etiqueta3.pack(pady=5)
        entrada3 = tk.Entry(ventana_inscribir)
        entrada3.pack(pady=5)

        def guardar_banda():
            nombre = entrada1.get()
            institucion = entrada2.get()
            categoria = entrada3.get()

            if nombre in bandas_db:
                print(" Ya existe una banda con ese nombre")
            else:
                nuevo_id = random.randint(1000, 9999)

                nueva_banda = BandaEscolar(nombre, institucion, categoria)
                bandas_db[nuevo_id] = nueva_banda
            messagebox.showinfo(
                "Banda Inscrita",
                f"Banda '{nombre}' registrada con éxito.Su ID es: {nuevo_id}"
            )

            ventana_inscribir.destroy()

        boton_guardar = tk.Button(ventana_inscribir, text="Guardar Banda", command=guardar_banda)
        boton_guardar.pack(pady=10)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_eval = tk.Toplevel(ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("500x600")

        tk.Label(ventana_eval, text="ID de la Banda:").pack(pady=5)
        entrada_id = tk.Entry(ventana_eval)
        entrada_id.pack(pady=5)

        labels = ["Ritmo", "Uniformidad", "Coreografía", "Alineación", "Puntualidad"]
        entradas = {}

        for label in labels:
            tk.Label(ventana_eval, text=f"Ingrese puntaje de {label} (0-10):").pack(pady=2)
            entry = tk.Entry(ventana_eval)
            entry.pack(pady=2)
            entradas[label.lower()] = entry

        def guardar_evaluacion():
            try:
                id_banda = int(entrada_id.get())  # convertir texto a número
            except ValueError:
                messagebox.showerror("Error", "El ID debe ser un número")
                return
            if id_banda not in bandas_db:
                messagebox.showerror("Error", "No existe una banda con ese ID")
                return
            banda = bandas_db[id_banda]

            banda.puntaje_rit = int(entradas["ritmo"].get())
            banda.puntaje_unifor = int(entradas["uniformidad"].get())
            banda.puntaje_coreo = int(entradas["coreografía"].get())
            banda.puntaje_ali = int(entradas["alineación"].get())
            banda.puntaje_punt = int(entradas["puntualidad"].get())

            banda.total = (banda.puntaje_rit + banda.puntaje_unifor +
                           banda.puntaje_coreo + banda.puntaje_ali +
                           banda.puntaje_punt)
            banda.avg = banda.total / 5
            messagebox.showinfo(
                "Evaluación Registrada",
                f"Evaluación guardada para {banda.name} (ID: {id_banda})\n"
                f"Total: {banda.total}, Promedio: {banda.avg:.2f}"
            )
            ventana_eval.destroy()

        tk.Button(ventana_eval, text="Guardar Evaluación", command=guardar_evaluacion).pack(pady=15)

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("400x300")

        lista = tk.Listbox(ventana_listado, width=50, height=15)
        lista.pack(pady=10)

        if not bandas_db:
            lista.insert(tk.END, "No hay bandas registradas aún.")
        else:
            for id_banda, banda in bandas_db.items():
                promedio = f"{banda.avg:.2f}" if banda.avg > 0 else "N/A"
                lista.insert(tk.END, f"ID:{id_banda} | {banda.name} | Promedio:{promedio}")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("500x600")

        lista = tk.Listbox(ventana_ranking, width=50, height=15)
        lista.pack(pady=10)

        if not bandas_db:
            lista.insert(tk.END, "No hay bandas para rankear aún.")
        else:
            ordered_list = sorted(bandas_db.items(), key=lambda x:x[1].avg, reverse=True)
            for id_banda, banda in ordered_list:
                promedio = f"{banda.avg:.2f}" if banda.avg > 0 else "N/A"
                lista.insert(tk.END, f"ID:{id_banda} | {banda.name} | Promedio:{promedio}")

    def salir(self):
        print("Aplicación cerrada")
        ventana.quit()


#---------------------------------------------------------------------------------------------------------------
concurso_septiembre = Concurso()

ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=concurso_septiembre.inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=concurso_septiembre.registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=concurso_septiembre.listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=concurso_septiembre.ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=concurso_septiembre.salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
