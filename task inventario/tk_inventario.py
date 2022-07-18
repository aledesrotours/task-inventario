import tkinter as tk
from tkinter import Button, Entry, Label, ttk
from tkinter import font
from sys import *


class Window():

    def __init__(self, window):
        self.root = window
        window.geometry('400x250')
        window.title('NoName CO')

        # Opciones del primer OptionMenu
        self.type = ('Mesa', 'Silla', 'Alacena', 'Cajonera')

        self.type_option = tk.StringVar()
        self.model_option = tk.StringVar()
        self.color_option = tk.StringVar()

        # Pestañas

        tabControl = ttk.Notebook(window)

        self.add_tab = ttk.Frame(tabControl)
        self.del_tab = ttk.Frame(tabControl)
        self.modif_tab = ttk.Frame(tabControl)

        tabControl.add(self.add_tab, text='Añadir')
        tabControl.add(self.modif_tab, text='Modficar')
        tabControl.add(self.del_tab, text='Eliminar')

        tabControl.pack(expand=1, fill=tk.BOTH)

        # Primer Pestaña (Añadir)

        # Labels

        self.l_type = Label(
            self.add_tab, text='Ingrese el tipo: ', font=(10)).place(x=20, y=50)
        self.l_model = Label(
            self.add_tab, text='Ingrese el modelo: ', font=(10)).place(x=20, y=95)
        self.l_color = Label(
            self.add_tab, text='Ingrese el color: ', font=(10)).place(x=20, y=140)

        # Button

        self.b_add = Button(self.add_tab, text="Subir datos",  padx=10,
                            pady=3, activebackground="green", activeforeground="white")
        self.b_add.place(x=150, y=190)

        # Primer OptionMenu

        self.style = ttk.Style()
        self.style.configure('TLabel', font=(6))
        type_menu = ttk.OptionMenu(
            self.add_tab, self.type_option, self.type[0], *self.type, command=self.type_to_model, style='TLabel')
        type_menu.place(x=200, y=53)
        type_menu['menu'].configure(font=(12))

        # Segunda pestaña (Modificar)

        # Labels

        self.l_id_modif = Label(self.modif_tab, text='ID',
                                font=(10)).place(x=20, y=50)
        self.l_cant_modif = Label(
            self.modif_tab, text='Cantidad', font=(10)).place(x=20, y=95)

        # Entry

        self.e_id_modif = Entry(self.modif_tab).place(x=150, y=50)
        self.e_cant_modfi = Entry(self.modif_tab).place(x=150, y=95)

        # Button

        self.b_modif = Button(self.modif_tab, text='Modificar datos', padx=10,
                              pady=3, activebackground='green', activeforeground='white')
        self.b_modif.place(x=150, y=150)

        # Tercer pestaña (Eliminar)

        # Label

        self.l_id_del = Label(self.del_tab, text='ID',
                              font=(10)).place(x=20, y=50)

        # Entry
        self.e_id_del = Entry(self.del_tab).place(x=150, y=50)

        # Button

        self.b_modif = Button(self.del_tab, text='Eliminar dato', padx=10,
                              pady=3, activebackground='green', activeforeground='white')
        self.b_modif.place(x=150, y=150)

    def type_to_model(self, *args):
        modelo = self.retornar_modelos(self.type_option.get())
        option_model = ttk.OptionMenu(
            self.add_tab, self.model_option, modelo[0], *modelo, command=self.model_to_color, style='TLabel')
        option_model.place(x=200, y=98)

    def model_to_color(self, *args):
        color = self.retornar_colores(
            self.type_option.get(), self.model_option.get())
        option_color = ttk.OptionMenu(
            self.add_tab, self.color_option, color[0], *color, command=self.saludar(), style='TLabel')
        option_color.place(x=200, y=143)

    def saludar(self, *args):
        print(self.type_option.get())

    def retornar_modelos(self, tipo):
        tipos = {'Alacena': {'Doble': ['Beige', 'Gris', 'Roble'], 'Familiar': ['Beige', 'Gris', 'Roble']}, 'Mesa': {'Redonda': [None, 'Castaño', 'Natural'], 'Cuadrada': [
            None, 'Castaño', 'Natural']}, 'Cajonera': {'Cuádruple': ['Beige', 'Gris']}, 'Silla': {'Vintage': ['Natural'], 'Retro': ['Fresno']}}
        modelos = tipos[tipo]
        return tuple(modelos.keys())

    def retornar_colores(self, tipo, modelo):
        tipos = {'Alacena': {'Doble': ['Beige', 'Gris', 'Roble'], 'Familiar': ['Beige', 'Gris', 'Roble']}, 'Mesa': {'Redonda': [None, 'Castaño', 'Natural'], 'Cuadrada': [
            None, 'Castaño', 'Natural']}, 'Cajonera': {'Cuádruple': ['Beige', 'Gris']}, 'Silla': {'Vintage': ['Natural'], 'Retro': ['Fresno']}}
        modelos = tipos[tipo]
        return modelos[modelo]


class Principal():

    def __init__(self, windows):
        self.root_principal = windows
        Window(self.root_principal)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Principal(root)
    root.mainloop()
