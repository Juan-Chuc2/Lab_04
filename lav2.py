import tkinter as tk

from Demos.SystemParametersInfo import new_w


class Participante:
    def __init__(self, name, institution):
        super().__init__()
        self.name = name
        self.institution = institution

    def mostrar_info(self):
        return f"Nombre: {self.name}, Instituciom: {self.institution}"


class BandaEscolar(Participante):
    def __init__(self, name, institution, categoria, puntaje):
        super().__init__(name, institution)
        self._category = categoria
        self._points = puntaje

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
    def puntaje(self):
        return self._points
    @puntaje.setter
    def puntaje(self, nuevo_puntaje):
        if nuevo_puntaje < 0 or nuevo_puntaje>10:
            print("Puntaje no válido")
        else:
            self._points = nuevo_puntaje


class Concurso:
    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Toplevel(ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x300")

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_eval = tk.Toplevel(ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("400x300")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("400x300")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("400x300")

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
