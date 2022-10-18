import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from app.version import Version
from data_base.bd import ConnectBd
from datetime import date

class Main_register():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x550')
        self.window.resizable(0,0)
        self.window.title('World Of Warcraft Register')
        self.icon_wow = ImageTk.PhotoImage(Image.open('images/logo.ico'))
        self.window.iconphoto(False, self.icon_wow)
        self.widgets()
        self.button_selected = IntVar()
        self.result = IntVar()
        ConnectBd()
        ConnectBd.show(self, self.tree, END)
        ConnectBd.sum_farm(self, self.entry_total_farm)
        self.calculate_total()
        self.current_date = date.today()
        self.current_day = str(self.current_date)[8:10]
        self.current_month = str(self.current_date)[5:7]
        self.current_year = str(self.current_date)[0:4]
        self.search_var = StringVar()
        self.date_selected = False
        self.window.mainloop()
        
    ######## WIDGETS #########
        
    def widgets(self):
        # TABS

        tabs_window = ttk.Notebook(self.window)
        tabs_window.pack(fill='both', expand='no')
        p1 = Frame(tabs_window, bg='#10223a', width=500, height=550)
        p2 = Frame(tabs_window, bg='#10223a', width=500, height=550)
        p3 = Frame(tabs_window, bg='#10223a', width=500, height=550)
        tabs_window.add(p1, text='Registros')
        tabs_window.add(p2, text='Calculadora')
        tabs_window.add(p3, text='Version')

        # WIDGETS TAB1
        
        label_tittle_regist = Label(p1, text='REGISTROS', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=215, y=20)
        self.tree = ttk.Treeview(p1, columns=('Farmeo', 'Tiempo', 'Fecha'))
        
        self.search_var = StringVar()

        self.label_filter = Label(p1, text='Filtrar:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=40, y=60)
        self.filter_box = ttk.Combobox(p1, values=['Id','Farmeo', 'Tiempo/h'], state='readonly', width=15)
        self.filter_box.place(x=100, y=63)
        
        self.label_search = Label(p1, text='Buscar:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=220, y=60)
        self.entry_search = Entry(p1, textvariable=self.search_var, borderwidth=2, relief=SOLID)
        self.entry_search.place(x=300, y=63)

        self.tree.column('#0', width=80)
        self.tree.column('Farmeo', width=117, anchor=CENTER)
        self.tree.column('Tiempo', width=117, anchor=CENTER)
        self.tree.column('Fecha', width=117, anchor=CENTER)

        self.tree.heading('#0', text= 'ID', anchor=CENTER)
        self.tree.heading('Farmeo', text= 'Farmeo', anchor=CENTER)
        self.tree.heading('Tiempo', text= 'Tiempo/h', anchor=CENTER)
        self.tree.heading('Fecha', text= 'Fecha', anchor=CENTER)

        self.tree.place(x=30, y=105)

        self.frame_total = Frame(p1, bg='#ffbb00')
        self.frame_total.place(x=87, y=340)

        self.total_farm = Label(self.frame_total, text=' Total ', font='Bahnschrift', bg='#ffbb00').grid(row=0, column=0)
        self.entry_total_farm = Entry(self.frame_total, text='', font='Bahnschrift', width=10, justify=CENTER, state='readonly')
        self.entry_total_farm.grid(row=0, column=1)
        self.total_farm2 = Label(p1, text=' de Oro ', font='Bahnschrift', foreground='#ffbb00', bg='#10223a').place(x=230, y=340)
        
        self.button_add_regist = Button(p1, text='Agregar Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.add_regist, state=NORMAL, borderwidth=2, relief=SOLID)
        self.button_add_regist.place(x=40, y=375)
        self.button_edit_regist = Button(p1, text='Editar Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.edit_regist, borderwidth=2, relief=SOLID).place(x=190, y=375)
        self.button_delete_regist = Button(p1, text='Borrar Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.delete_regist, borderwidth=2, relief=SOLID).place(x=325, y=375)
        self.button_delete_all_regist = Button(p1, text='Borrar Todos los Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.delete_all_regist, borderwidth=2, relief=SOLID).place(x=80, y=423)
        self.button_filter = Button(p1, text='Filtrar', font='Bahnschrift', activebackground='#ffbb00', command=self.filter_regist, width=12, borderwidth=2, relief=SOLID).place(x=295, y=423)

        self.change_label = Label(p1, text='', bg='#10223a', foreground='#ffcc00', font='Bahnschrift', anchor=CENTER)
        
        # WIDGETS TAB2

        # ORE TO USD

        label_tittle_calculator = Label(p2, text='CALCULADORA', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=200, y=30)

        self.frame_to_dollar = LabelFrame(p2, text='ORO -> USD', bg='#10223a', foreground='#ffcc00', bd=5, font='Bahnschrift', height=170,width=455)
        self.frame_to_dollar.place(x=20, y=70)
        
        label_price = Label(p2, text=f'Precio del Oro:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=100)
        self.entry_price = Entry(p2, bd=2, borderwidth=2, relief=SOLID)
        self.entry_price.place(x=190, y=103)

        label_dollar_sing = Label(p2, text='$ x 1000 de Oro', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=320, y=100)

        label_quanty = Label(p2, text='Cantidad:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=140)
        self.entry_quanty = Entry(p2, bd=2, borderwidth=2, relief=SOLID)
        self.entry_quanty.place(x=190, y=143)

        label_diOr = Label(p2, text='de Oro', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=320, y=143)

        button_calculate = Button(p2, text='Calcular', font='Bahnschrift', command=self.calculate, activebackground='#ffbb00', borderwidth=2, relief=SOLID).place(x=370, y=180)

        label_result = Label(p2, text='Resultado:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=183)
        self.label_digit = Label(p2, text='0 $', bg='#10223a', foreground='#ffcc00', font='Bahnschrift')
        self.label_digit.place(x=140, y=183)

        # USD TO DOLAR

        self.frame_to_dollar2 = LabelFrame(p2, text='USD -> ORO', bg='#10223a', foreground='#ffcc00', bd=5, font='Bahnschrift', height=170,width=455)
        self.frame_to_dollar2.place(x=20, y=300)

        label_price2 = Label(p2, text=f'Precio del Oro:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=330)
        self.entry_price2 = Entry(p2, bd=2, borderwidth=2, relief=SOLID)
        self.entry_price2.place(x=190, y=333)

        label_dollar_sing2 = Label(p2, text='$ x 1000 de Oro', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=320, y=330)

        label_quanty2 = Label(p2, text='Cantidad:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=370)
        self.entry_quanty2 = Entry(p2, bd=2, borderwidth=2, relief=SOLID)
        self.entry_quanty2.place(x=190, y=373)

        label_diOr2 = Label(p2, text='$', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=320, y=370)

        button_calculate2 = Button(p2, text='Calcular', font='Bahnschrift', command=self.calculate2, activebackground='#ffbb00', borderwidth=2, relief=SOLID).place(x=370, y=410)

        label_result2 = Label(p2, text='Resultado:', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=50, y=410)
        self.label_digit2 = Label(p2, text='0 de Oro', bg='#10223a', foreground='#ffcc00', font='Bahnschrift')
        self.label_digit2.place(x=140, y=410)

        # WIDGETS TAB3

        label_tittle_version = Label(p3, text='VERSION', bg='#10223a', foreground='#ffcc00', font='Bahnschrift').place(x=215, y=50)
        text_box = Text(p3, height=12, width=48, font=('Bahnschrift',12), bg='#f4ffa1')
        text_box.place(x=30, y=94)
        text_box.insert('end', Version.version_info(self))
        text_box.config(state='disabled')

        self.logo_jiz = PhotoImage(file='images/logo_jiz.png')
        put_logo_jiz = Label(p3, image=self.logo_jiz, bg='#10223a')
        put_logo_jiz.place(x=170, y=350)
    
    ######## FUNCTIONS #########

    def show_filter(self, column, value):
        self.window_filter = tk.Toplevel(self.window)
        self.window_filter.resizable(0,0)
        self.window_filter.title('Filtros')
        self.window_filter.iconphoto(False, self.icon_wow)
        self.window_filter.config(bg='#1f1236')
        self.window_filter.grab_set()
        self.window_filter.geometry('500x550')

        self.tree2 = ttk.Treeview(self.window_filter, columns=('Farmeo', 'Tiempo', 'Fecha'))
        self.tree2.column('#0', width=80)
        self.tree2.column('Farmeo', width=117, anchor=CENTER)
        self.tree2.column('Tiempo', width=117, anchor=CENTER)
        self.tree2.column('Fecha', width=117, anchor=CENTER)

        self.tree2.heading('#0', text= 'ID', anchor=CENTER)
        self.tree2.heading('Farmeo', text= 'Farmeo', anchor=CENTER)
        self.tree2.heading('Tiempo', text= 'Tiempo/h', anchor=CENTER)
        self.tree2.heading('Fecha', text= 'Fecha', anchor=CENTER)

        self.change_label2 = Label(self.window_filter, text='', bg='#1f1236', foreground='#ffcc00', font='Bahnschrift', anchor=CENTER)
        self.filter_label = Label(self.window_filter, text='', bg='#1f1236', foreground='#ffcc00', font='Bahnschrift', anchor=CENTER)

        if column == 'Id':
            self.filter_label.config(text='Filtro = Id')
            self.filter_label.place(x=210, y=70)
        elif column == 'Farmeo':
            self.filter_label.config(text='Filtro = Farmeo')
            self.filter_label.place(x=190, y=70)
        elif column == 'Tiempo/h':
            self.filter_label.config(text='Filtro = Tiempo/h')
            self.filter_label.place(x=180, y=70)

        self.tree2.place(x=30, y=110)

        tittle_filter = Label(self.window_filter, text='REGISTROS FILTRADOS', bg='#1f1236', foreground='#ffcc00', font='Bahnschrift')
        tittle_filter.place(x=160, y=37)

        self.frame_total2 = Frame(self.window_filter, bg='#ffbb00')
        self.frame_total2.place(x=87, y=346)

        self.total_farm2 = Label(self.frame_total2, text=' Total ', font='Bahnschrift', bg='#ffbb00').grid(row=0, column=0)
        self.entry_total_farm2 = Entry(self.frame_total2, text='', font='Bahnschrift', width=10, justify=CENTER, state='readonly')
        self.entry_total_farm2.grid(row=0, column=1)
        self.total_farm2 = Label(self.window_filter, text=' de Oro ', font='Bahnschrift', foreground='#ffbb00', bg='#1f1236').place(x=230, y=346)

        self.calculate_total2()
        
        self.button_edit_regist2 = Button(self.window_filter, text='Editar Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.edit_filter, borderwidth=2, relief=SOLID).place(x=117, y=380)
        self.button_delete_regist2 = Button(self.window_filter, text='Borrar Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.delete_filter, borderwidth=2, relief=SOLID).place(x=260, y=380)
        self.button_delete_all_regist2 = Button(self.window_filter, text='Borrar Todos los Registro', font='Bahnschrift', activebackground='#ffbb00', command=self.delete_all_filter, borderwidth=2, relief=SOLID).place(x=150, y=420)
        self.button_exit = Button(self.window_filter, text='Salir', font='Bahnschrift', activebackground='#ffbb00', command=self.window_filter.destroy, borderwidth=2, relief=SOLID, width=10).place(x=200, y=460)

        ConnectBd.filter_regist(self, column, self.tree2, value)

        self.window_filter.mainloop()

    def edit_filter(self):
        self.selection2 = self.tree2.focus()
        self.row2 = self.tree2.item(self.selection2, 'text')
        if self.row2 == '':
            messagebox.showinfo('Error', 'Debe seleccionar algún registro.')
        else:
            self.change_label2.config(text=' ')
            self.selection2 = self.tree2.focus()
            self.row2 = self.tree2.item(self.selection2, 'text')

            self.window_edit2 = tk.Toplevel(self.window_filter)
            self.window_edit2.grab_set()
            self.window_edit2.resizable(0,0)
            self.window_edit2.geometry('300x300')
            self.window_edit2.title('Editar Registro')
            self.window_edit2.iconphoto(False, self.icon_wow)
            self.window_edit2.config(bg='#1f1236')

            label_tittle = Label(self.window_edit2, text='EDITAR REGISTRO', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=82, y=30)
            label_regist_number = Label(self.window_edit2, text='Registro N° = ' + str(self.row2), font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=92, y=50)
            label_ore_farm = Label(self.window_edit2, text='Oro farmeado:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=90)
            label_time_perHour = Label(self.window_edit2, text='Tiempo/H:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=130)
            label_date = Label(self.window_edit2, text='Fecha=', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=170)
            label_day = Label(self.window_edit2, text='Día:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            label_month = Label(self.window_edit2, text='Mes:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            label_year = Label(self.window_edit2, text='Año:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')

            self.entry_ore_farm2 = Entry(self.window_edit2, borderwidth=2, relief=SOLID)
            self.values2 = self.tree2.item(self.selection2, 'values')
            self.entry_ore_farm2.insert(0, self.values2[0])
            self.entry_ore_farm2.place(x=130, y=95)
            self.entry_time_perHour2 = Entry(self.window_edit2, borderwidth=2, relief=SOLID)
            self.entry_time_perHour2.insert(0, self.values2[1])
            self.entry_time_perHour2.place(x=130, y=135)
    
            self.check_date_personalized = Radiobutton(self.window_edit2, text='Personalizada', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=1, selectcolor='Purple', command=self.get_button_edit2)
            self.check_date_personalized.place(x=15, y=200)
            self.check_date_personalized.select()
            self.check_date_actual = Radiobutton(self.window_edit2, text='Actual', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=2, selectcolor='Purple', command=self.get_button_edit2)
            self.check_date_actual.place(x=15, y=230)
            self.check_date_actual.deselect()
        
            self.label_day2 = Label(self.window_edit2, text='Día:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.label_month2 = Label(self.window_edit2, text='Mes:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.label_year2 = Label(self.window_edit2, text='Año:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.entry_day2 = Entry(self.window_edit2, width=5, borderwidth=2, relief=SOLID)
            self.entry_day2.insert(0, self.values2[2][0:2])
            self.entry_month2 = Entry(self.window_edit2, width=5, borderwidth=2, relief=SOLID)
            self.entry_month2.insert(0, self.values2[2][3:5])
            self.entry_year2 = Entry(self.window_edit2, width=5, borderwidth=2, relief=SOLID)
            self.entry_year2.insert(0, self.values2[2][6:10])

            self.window_edit2.geometry('300x400')
            self.label_day2.place(x=40, y=280)
            self.label_month2.place(x=40, y=315)
            self.label_year2.place(x=40, y=350)
            self.entry_day2.place(x=100,y=283)
            self.entry_month2.place(x=100,y=318)
            self.entry_year2.place(x=100,y=353)

            add_button = Button(self.window_edit2, text='Guardar', font='Bahnschrift', activebackground='#ffbb00', command=self.edit_filter_process, borderwidth=2, relief=SOLID)
            add_button.place(x=190, y= 180)
            add_button = Button(self.window_edit2, text='Cerrar', font='Bahnschrift', activebackground='#ffbb00', command=self.window_edit2.destroy, borderwidth=2, relief=SOLID)
            add_button.place(x=195, y= 230)

            self.window_edit2.mainloop()

    def edit_filter_process(self):
        self.farm2 = self.entry_ore_farm2.get()
        self.time2 = self.entry_time_perHour2.get()
        self.day2 = self.entry_day2.get()
        self.month2 = self.entry_month2.get()
        self.year2 = self.entry_year2.get()
        if self.button_selected.get() == 1:
            if self.farm2.isdigit() and self.time2.isdigit() and self.day2.isdigit() and self.month2.isdigit() and self.year2.isdigit():
                if len(self.day2) != 2 or len(self.month2) != 2 or len(self.year2) != 4:
                    messagebox.showerror('Error','Se requieren 2 dígitos para "Día" y "Mes" y 4 para "Año".')
                elif len(self.farm2) == 0 or len(self.time2) == 0 or len(self.day2) == 0 or len(self.month2) == 0 or len(self.year2) == 0:
                    messagebox.showerror('Error', 'No debe dejar campos vacíos.')
                elif int(self.day2) > 31 or int(self.month2) > 12:
                    messagebox.showerror('Error','Día máximo = 31. Mes máximo = 12.')
                elif len(self.farm2) > 10 or len(self.time2) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time2) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.edit(self, self.row2, self.farm2, self.time2, (f'{self.day2}/{self.month2}/{self.year2}'))
                    registros1 = self.tree.get_children()
                    for registro1 in registros1:
                        self.tree.delete(registro1)
                    registros2 = self.tree2.get_children()
                    for registro2 in registros2:
                        self.tree2.delete(registro2)
                    ConnectBd.show(self, self.tree, END)
                    if self.filter_selected == 'Id':
                        ConnectBd.show_in_filter(self, self.tree2, END, self.filter_selected, self.search)
                        self.entry_ore_farm2.delete(0, END)
                        self.entry_time_perHour2.delete(0, END)
                        self.entry_day2.delete(0, END)
                        self.entry_month2.delete(0, END)
                        self.entry_year2.delete(0, END)
                        self.change_label2.config(text='Registro Editado con Éxito.')
                        self.change_label2.place(x=153,y=500)
                        self.window_edit2.destroy()
                        self.window_filter.grab_set()
                        self.calculate_total()
                        self.calculate_total2()
                    elif self.filter_selected == 'Farmeo':
                        ConnectBd.show_in_filter(self, self.tree2, END, self.filter_selected, self.search)
                        self.entry_ore_farm2.delete(0, END)
                        self.entry_time_perHour2.delete(0, END)
                        self.entry_day2.delete(0, END)
                        self.entry_month2.delete(0, END)
                        self.entry_year2.delete(0, END)
                        self.change_label2.config(text='Registro Editado con Éxito.')
                        self.change_label2.place(x=153,y=500)
                        self.window_edit2.destroy()
                        self.window_filter.grab_set()
                        self.calculate_total()
                        self.calculate_total2()
                    elif self.filter_selected == 'Tiempo/h':
                        ConnectBd.show_in_filter(self, self.tree2, END, self.filter_selected, self.search)
                        self.entry_ore_farm2.delete(0, END)
                        self.entry_time_perHour2.delete(0, END)
                        self.entry_day2.delete(0, END)
                        self.entry_month2.delete(0, END)
                        self.entry_year2.delete(0, END)
                        self.change_label2.config(text='Registro Editado con Éxito.')
                        self.change_label2.place(x=153,y=500)
                        self.window_edit2.destroy()
                        self.window_filter.grab_set()
                        self.calculate_total()
                        self.calculate_total2()
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos enteros.')
        elif self.button_selected.get() == 2:
            if self.farm2.isdigit() and self.time2.isdigit():
                if len(self.farm) > 10 or len(self.time) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.edit(self, self.row2, self.farm2, self.time2, (f'{self.current_day}/{self.current_month}/{self.current_year}'))
                    registros = self.tree2.get_children()
                    for registro in registros:
                        self.tree2.delete(registro)
                    ConnectBd.show(self, self.tree, END)
                    self.entry_ore_farm2.delete(0, END)
                    self.entry_time_perHour2.delete(0, END)
                    self.entry_day2.delete(0, END)
                    self.entry_month2.delete(0, END)
                    self.entry_year2.delete(0, END)
                    self.change_label2.config(text='Registro Editado con Éxito.')
                    self.change_label2.place(x=153,y=500)
                    self.window_edit2.destroy()
                    self.calculate_total()
                    self.calculate_total2()
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos enteros.')

    def delete_filter(self):
        self.selection2 = self.tree2.focus()
        self.row2 = self.tree2.item(self.selection2, 'text')
        if self.row2 == '':
            messagebox.showinfo('Error', 'Debe seleccionar algún registro.')
        else:
            ConnectBd.delete(self, self.row2)
            registros1 = self.tree.get_children()
            for registro1 in registros1:
                self.tree.delete(registro1)
            registros2 = self.tree2.get_children()
            for registro2 in registros2:
                self.tree2.delete(registro2)
            ConnectBd.show(self, self.tree, END)
            ConnectBd.show_in_filter(self, self.tree2, END, self.filter_selected, self.search)
            self.change_label2.config(text='Registro Borrado con Éxito.')
            self.change_label2.place(x=145,y=500)
            self.calculate_total()
            self.calculate_total2()

    def delete_all_filter(self):
        advertise_box = messagebox.askyesno('Advertencia','¿Está seguro de que desea borrar todos los registros?')
        if advertise_box:
            ConnectBd.delete_all_filter_box(self, self.filter_selected, self.search)
            registros1 = self.tree.get_children()
            for registro1 in registros1:
                self.tree.delete(registro1)
            registros2 = self.tree2.get_children()
            for registro2 in registros2:
                self.tree2.delete(registro2)
            ConnectBd.show(self, self.tree, END)
            ConnectBd.show_in_filter(self, self.tree2, END, self.filter_selected, self.search)
            self.change_label2.config(text='Todos los Registros Han Sido Eliminados.')
            self.change_label2.place(x=90,y=500)
            self.calculate_total()
            self.calculate_total2()
        else:
            messagebox.showinfo('Advertencia', 'Borrar Todos los Registros Cancelado.')

    def calculate_total2(self):
        self.entry_total_farm2.config(state=NORMAL)
        self.entry_total_farm2.delete(0, END)
        ConnectBd.sum_farm_filter(self, self.entry_total_farm2, self.filter_selected, self.search)
        self.entry_total_farm2.config(state='readonly')

    def filter_regist(self):
        self.change_label.place_forget()
        self.search = self.entry_search.get()
        self.filter_selected = self.filter_box.get()

        if self.filter_selected == 'Id':
            if len(self.search) == 0:
                messagebox.showerror('Error', 'Debe ingresar el valor a buscar.')
            else:
                is_number = False
                is_digit = False
                for i in self.search: 
                    if i.isalpha(): 
                        is_digit = True
                    if i.isdigit(): 
                        is_number = True
                if is_number == True and is_digit == False:
                    allow = ConnectBd.allow_filter(self, self.filter_selected, self.search)
                    if allow == True:
                        self.show_filter(self.filter_selected, self.search)
                    else:
                        self.change_label.config(text='Su búsqueda no coincide con ningún registro.')
                        self.change_label.place(x=85,y=475)
                else:
                    messagebox.showerror('Error', 'Para filtrar Id solo se permiten valores numéricos enteros.')

        elif self.filter_selected == 'Farmeo':
            if len(self.search) == 0:
                messagebox.showerror('Error', 'Debe ingresar el valor a buscar.')
            else:
                is_number = False
                is_digit = False
                for i in self.search: 
                    if i.isalpha(): 
                        is_digit = True
                    if i.isdigit(): 
                        is_number = True
                if is_number == True and is_digit == False:
                    allow = ConnectBd.allow_filter(self, self.filter_selected, self.search)
                    if allow == True:
                        self.show_filter(self.filter_selected, self.search)
                    else:
                        self.change_label.config(text='Su búsqueda no coincide con ningún registro.')
                        self.change_label.place(x=85,y=475)
                else:
                    messagebox.showerror('Error', 'Para filtrar Farmeo solo se permiten valores numéricos enteros.')

        elif self.filter_selected == 'Tiempo/h':
            if len(self.search) == 0:
                messagebox.showerror('Error', 'Debe ingresar el valor a buscar.')
            else:
                is_number = False
                is_digit = False
                for i in self.search: 
                    if i.isalpha(): 
                        is_digit = True
                    if i.isdigit(): 
                        is_number = True
                if is_number == True and is_digit == False:
                    allow = ConnectBd.allow_filter(self, self.filter_selected, self.search)
                    if allow == True:
                        self.show_filter(self.filter_selected, self.search)
                    else:
                        self.change_label.config(text='Su búsqueda no coincide con ningún registro.')
                        self.change_label.place(x=85,y=475)
                else:
                    messagebox.showerror('Error', 'Para filtrar Tiempo/h solo se permiten valores numéricos enteros.')
                
        else:
            messagebox.showerror('Error','Debe seleccionar un filtro.')

    def get_button_add(self):
        if self.button_selected.get() == 1:
            self.window_add.geometry('300x400')
            self.label_day.place(x=40, y=280)
            self.label_month.place(x=40, y=315)
            self.label_year.place(x=40, y=350)
            self.entry_day.place(x=100,y=283)
            self.entry_month.place(x=100,y=318)
            self.entry_year.place(x=100,y=353)
        elif self.button_selected.get() == 2:
            self.window_add.geometry('300x300')
            self.label_day.place_forget()
            self.label_month.place_forget()
            self.label_year.place_forget()
            self.entry_day.place_forget()
            self.entry_month.place_forget()
            self.entry_year.place_forget()

    def get_button_edit2(self):
        if self.button_selected.get() == 1:
            self.window_edit2.geometry('300x400')
            self.label_day2.place(x=40, y=280)
            self.label_month2.place(x=40, y=315)
            self.label_year2.place(x=40, y=350)
            self.entry_day2.place(x=100,y=283)
            self.entry_month2.place(x=100,y=318)
            self.entry_year2.place(x=100,y=353)
        elif self.button_selected.get() == 2:
            self.window_edit2.geometry('300x300')
            self.label_day2.place_forget()
            self.label_month2.place_forget()
            self.label_year2.place_forget()
            self.entry_day2.place_forget()
            self.entry_month2.place_forget()
            self.entry_year2.place_forget()        

    def get_button_edit(self):
        if self.button_selected.get() == 1:
            self.window_edit.geometry('300x400')
            self.label_day.place(x=40, y=280)
            self.label_month.place(x=40, y=315)
            self.label_year.place(x=40, y=350)
            self.entry_day.place(x=100,y=283)
            self.entry_month.place(x=100,y=318)
            self.entry_year.place(x=100,y=353)
        elif self.button_selected.get() == 2:
            self.window_edit.geometry('300x300')
            self.label_day.place_forget()
            self.label_month.place_forget()
            self.label_year.place_forget()
            self.entry_day.place_forget()
            self.entry_month.place_forget()
            self.entry_year.place_forget()

    def calculate(self):
        self.ore_price = self.entry_price.get()
        self.quanty = self.entry_quanty.get()

        if self.ore_price.isdigit() and self.quanty.isdigit():
            if len(self.ore_price) == 0 and len(self.quanty) == 0:
                messagebox.showerror('Error', 'Debe ingresar la cantidad y el precio.')
            else:
                self.result = (int(self.ore_price) * int(self.quanty)) / 1000
                self.label_digit.config(text=f'{self.result:.2f} $')
            
        elif isinstance(self.ore_price, str) or isinstance(self.quanty, str):
            if len(self.ore_price) == 0 and len(self.quanty) == 0:
                messagebox.showerror('Error', 'Debe ingresar la cantidad y el precio.')
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos enteros.')

    def calculate2(self):
        self.ore_price2 = self.entry_price2.get()
        self.quanty2 = self.entry_quanty2.get()
        
        if self.ore_price2.isdigit() and self.quanty2.isdigit():
            if len(self.ore_price2) == 0 and len(self.quanty2) == 0:
                messagebox.showerror('Error', 'Debe ingresar la cantidad y el precio.')
            else:
                self.result = (int(self.quanty2) * 1000) / int(self.ore_price2)
                self.label_digit2.config(text=f'{self.result:.2f} de Oro')
        elif isinstance(self.ore_price2, str) or isinstance(self.quanty2, str):
            if len(self.ore_price2) == 0 and len(self.quanty2) == 0:
                messagebox.showerror('Error', 'Debe ingresar la cantidad y el precio.')
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos enteros.')

    def calculate_total(self):
        self.entry_total_farm.config(state=NORMAL)
        self.entry_total_farm.delete(0, END)
        ConnectBd.sum_farm(self, self.entry_total_farm)
        self.entry_total_farm.config(state='readonly')

    def add_regist(self):
        self.change_label.config(text=' ')
        self.window_add = tk.Toplevel(self.window)
        self.window_add.grab_set()
        self.window_add.resizable(0,0)
        self.window_add.geometry('300x300')
        self.window_add.title('Añadir Registro')
        self.window_add.iconphoto(False, self.icon_wow)
        self.window_add.config(bg='#1f1236')

        label_tittle = Label(self.window_add, text='AÑADIR REGISTRO', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=82, y=30)
        label_ore_farm = Label(self.window_add, text='Oro farmeado:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=90)
        label_time_perHour = Label(self.window_add, text='Tiempo/H:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=130)
        label_date = Label(self.window_add, text='Fecha=', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=170)

        self.check_date_personalized = Radiobutton(self.window_add, text='Personalizada', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=1, selectcolor='Purple', command=self.get_button_add)
        self.check_date_personalized.place(x=15, y=200)
        self.check_date_personalized.deselect()
        self.check_date_actual = Radiobutton(self.window_add, text='Actual', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=2, selectcolor='Purple', command=self.get_button_add)
        self.check_date_actual.place(x=15, y=230)
        self.check_date_actual.select()
    
        self.label_day = Label(self.window_add, text='Día:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
        self.label_month = Label(self.window_add, text='Mes:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
        self.label_year = Label(self.window_add, text='Año:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
        self.entry_day = Entry(self.window_add, width=5, borderwidth=2, relief=SOLID)
        self.entry_month = Entry(self.window_add, width=5, borderwidth=2, relief=SOLID)
        self.entry_year = Entry(self.window_add, width=5, borderwidth=2, relief=SOLID)
        
        self.entry_ore_farm = Entry(self.window_add, borderwidth=2, relief=SOLID)
        self.entry_ore_farm.place(x=130, y=95)
        self.entry_time_perHour = Entry(self.window_add, borderwidth=2, relief=SOLID)
        self.entry_time_perHour.place(x=130, y=135)

        add_button = Button(self.window_add, text='Guardar', font='Bahnschrift', activebackground='#ffbb00', command=self.add_regist_process, borderwidth=2, relief=SOLID)
        add_button.place(x=190, y= 180)
        add_button = Button(self.window_add, text='Cerrar', font='Bahnschrift', activebackground='#ffbb00', command=self.window_add.destroy, borderwidth=2, relief=SOLID)
        add_button.place(x=195, y= 230)

        self.window_add.mainloop()

    def add_regist_process(self):
        self.farm = self.entry_ore_farm.get()
        self.time = self.entry_time_perHour.get()
        self.day = self.entry_day.get()
        self.month = self.entry_month.get()
        self.year = self.entry_year.get()

        if self.button_selected.get() == 1:

            if self.farm.isdigit() and self.time.isdigit() and self.day.isdigit() and self.month.isdigit() and self.year.isdigit():
                if len(self.day) != 2 or len(self.month) != 2 or len(self.year) != 4:
                    messagebox.showerror('Error','Se requieren 2 dígitos para "Día" y "Mes" y 4 para "Año".')
                elif len(self.farm) == 0 or len(self.time) == 0 or len(self.day) == 0 or len(self.month) == 0 or len(self.year) == 0:
                    messagebox.showerror('Error', 'No debe dejar campos vacíos.')
                elif int(self.day) > 31 or int(self.month) > 12:
                    messagebox.showerror('Error','Día máximo = 31. Mes máximo = 12.')
                elif len(self.farm) > 10 or len(self.time) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.insert(self, self.farm, self.time, (f'{self.day}/{self.month}/{self.year}'))
                    registros = self.tree.get_children()
                    for registro in registros:
                        self.tree.delete(registro)
                    ConnectBd.show(self, self.tree, END)
                    self.entry_ore_farm.delete(0, END)
                    self.entry_time_perHour.delete(0, END)
                    self.entry_day.delete(0, END)
                    self.entry_month.delete(0, END)
                    self.entry_year.delete(0, END)
                    self.change_label.config(text='Registro Añadido con Éxito.')
                    self.change_label.place(x=145,y=475)
                    self.calculate_total()

        elif self.button_selected.get() == 2:

            if self.farm.isdigit() and self.time.isdigit():
                if len(self.farm) > 10 or len(self.time) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.insert(self, self.farm, self.time, (f'{self.current_day}/{self.current_month}/{self.current_year}'))
                    registros = self.tree.get_children()
                    for registro in registros:
                        self.tree.delete(registro)
                    ConnectBd.show(self, self.tree, END)
                    self.entry_ore_farm.delete(0, END)
                    self.entry_time_perHour.delete(0, END)
                    self.entry_day.delete(0, END)
                    self.entry_month.delete(0, END)
                    self.entry_year.delete(0, END)
                    self.change_label.config(text='Registro Añadido con Éxito.')
                    self.change_label.place(x=145,y=475)
                    self.calculate_total()
            else: 
                messagebox.showerror('Error', 'Solo se permiten valores numéricos.')
        else:
            messagebox.showerror('Error', 'Solo se permiten valores numéricos.')

    def edit_regist(self):
        self.selection = self.tree.focus()
        self.row = self.tree.item(self.selection, 'text')
        if self.row == '':
            messagebox.showinfo('Error', 'Debe seleccionar algún registro.')
        else:
            self.change_label.config(text=' ')
            self.selection = self.tree.focus()
            self.row = self.tree.item(self.selection, 'text')

            self.window_edit = tk.Toplevel(self.window)
            self.window_edit.grab_set()
            self.window_edit.resizable(0,0)
            self.window_edit.geometry('300x300')
            self.window_edit.title('Editar Registro')
            self.window_edit.iconphoto(False, self.icon_wow)
            self.window_edit.config(bg='#1f1236')

            label_tittle = Label(self.window_edit, text='EDITAR REGISTRO', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=82, y=30)
            label_regist_number = Label(self.window_edit, text='Registro N° = ' + str(self.row), font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=92, y=50)
            label_ore_farm = Label(self.window_edit, text='Oro farmeado:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=90)
            label_time_perHour = Label(self.window_edit, text='Tiempo/H:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=130)
            label_date = Label(self.window_edit, text='Fecha=', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236').place(x=15, y=170)
            label_day = Label(self.window_edit, text='Día:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            label_month = Label(self.window_edit, text='Mes:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            label_year = Label(self.window_edit, text='Año:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')

            self.entry_ore_farm = Entry(self.window_edit, borderwidth=2, relief=SOLID)
            self.values = self.tree.item(self.selection, 'values')
            self.entry_ore_farm.insert(0, self.values[0])
            self.entry_ore_farm.place(x=130, y=95)
            self.entry_time_perHour = Entry(self.window_edit, borderwidth=2, relief=SOLID)
            self.entry_time_perHour.insert(0, self.values[1])
            self.entry_time_perHour.place(x=130, y=135)
    
            self.check_date_personalized = Radiobutton(self.window_edit, text='Personalizada', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=1, selectcolor='Purple', command=self.get_button_edit)
            self.check_date_personalized.place(x=15, y=200)
            self.check_date_personalized.select()
            self.check_date_actual = Radiobutton(self.window_edit, text='Actual', bg='#1f1236', font='Bahnschrift', foreground='#ffcc00', variable=self.button_selected, value=2, selectcolor='Purple', command=self.get_button_edit)
            self.check_date_actual.place(x=15, y=230)
            self.check_date_actual.deselect()
        
            self.label_day = Label(self.window_edit, text='Día:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.label_month = Label(self.window_edit, text='Mes:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.label_year = Label(self.window_edit, text='Año:', font='Bahnschrift', foreground='#ffcc00', bg='#1f1236')
            self.entry_day = Entry(self.window_edit, width=5, borderwidth=2, relief=SOLID)
            self.entry_day.insert(0, self.values[2][0:2])
            self.entry_month = Entry(self.window_edit, width=5, borderwidth=2, relief=SOLID)
            self.entry_month.insert(0, self.values[2][3:5])
            self.entry_year = Entry(self.window_edit, width=5, borderwidth=2, relief=SOLID)
            self.entry_year.insert(0, self.values[2][6:10])

            self.window_edit.geometry('300x400')
            self.label_day.place(x=40, y=280)
            self.label_month.place(x=40, y=315)
            self.label_year.place(x=40, y=350)
            self.entry_day.place(x=100,y=283)
            self.entry_month.place(x=100,y=318)
            self.entry_year.place(x=100,y=353)

            add_button = Button(self.window_edit, text='Guardar', font='Bahnschrift', activebackground='#ffbb00', command=self.edit_regist_process, borderwidth=2, relief=SOLID)
            add_button.place(x=190, y= 180)
            add_button = Button(self.window_edit, text='Cerrar', font='Bahnschrift', activebackground='#ffbb00', command=self.window_edit.destroy, borderwidth=2, relief=SOLID)
            add_button.place(x=195, y= 230)

            self.window_edit.mainloop()
    
    def edit_regist_process(self):
        self.farm = self.entry_ore_farm.get()
        self.time = self.entry_time_perHour.get()
        self.day = self.entry_day.get()
        self.month = self.entry_month.get()
        self.year = self.entry_year.get()
        if self.button_selected.get() == 1:
            if self.farm.isdigit() and self.time.isdigit() and self.day.isdigit() and self.month.isdigit() and self.year.isdigit():
                if len(self.day) != 2 or len(self.month) != 2 or len(self.year) != 4:
                    messagebox.showerror('Error','Se requieren 2 dígitos para "Día" y "Mes" y 4 para "Año".')
                elif len(self.farm) == 0 or len(self.time) == 0 or len(self.day) == 0 or len(self.month) == 0 or len(self.year) == 0:
                    messagebox.showerror('Error', 'No debe dejar campos vacíos.')
                elif int(self.day) > 31 or int(self.month) > 12:
                    messagebox.showerror('Error','Día máximo = 31. Mes máximo = 12.')
                elif len(self.farm) > 10 or len(self.time) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.edit(self, self.row, self.farm, self.time, (f'{self.day}/{self.month}/{self.year}'))
                    registros = self.tree.get_children()
                    for registro in registros:
                        self.tree.delete(registro)
                    ConnectBd.show(self, self.tree, END)
                    self.entry_ore_farm.delete(0, END)
                    self.entry_time_perHour.delete(0, END)
                    self.entry_day.delete(0, END)
                    self.entry_month.delete(0, END)
                    self.entry_year.delete(0, END)
                    self.change_label.config(text='Registro Editado con Éxito.')
                    self.change_label.place(x=145,y=475)
                    self.window_edit.destroy()
                    self.calculate_total()
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos.')
        elif self.button_selected.get() == 2:
            if self.farm.isdigit() and self.time.isdigit():
                if len(self.farm) > 10 or len(self.time) > 2:
                    messagebox.showerror('Error', 'Máximo de caracteres: Farmeo = 10. Tiempo/h = 2.')
                elif int(self.time) > 24:
                    messagebox.showerror('Error', 'Horas máximas = 24h')
                else:
                    ConnectBd.edit(self, self.row, self.farm, self.time, (f'{self.current_day}/{self.current_month}/{self.current_year}'))
                    registros = self.tree.get_children()
                    for registro in registros:
                        self.tree.delete(registro)
                    ConnectBd.show(self, self.tree, END)
                    self.entry_ore_farm.delete(0, END)
                    self.entry_time_perHour.delete(0, END)
                    self.entry_day.delete(0, END)
                    self.entry_month.delete(0, END)
                    self.entry_year.delete(0, END)
                    self.change_label.config(text='Registro Editado con Éxito.')
                    self.change_label.place(x=145,y=475)
                    self.window_edit.destroy()
                    self.calculate_total()
            else:
                messagebox.showerror('Error', 'Solo se permiten valores numéricos.')
            
    def delete_regist(self):
        self.selection = self.tree.focus()
        self.row = self.tree.item(self.selection, 'text')
        if self.row == '':
            messagebox.showinfo('Error', 'Debe seleccionar algún registro.')
        else:
            ConnectBd.delete(self, self.row)
            self.tree.delete(self.selection)
            self.change_label.config(text='Registro Borrado con Éxito.')
            self.change_label.place(x=145,y=475)
            self.calculate_total()

    def delete_all_regist(self):
        advertise_box = messagebox.askyesno('Advertencia','¿Está seguro de que desea borrar todos los registros?')
        if advertise_box:
            ConnectBd.delete_all(self)
            registros = self.tree.get_children()
            for registro in registros:
                self.tree.delete(registro)
                ConnectBd.show(self, self.tree, END)
            ConnectBd.show(self, self.tree, END)
            self.change_label.config(text='Todos los Registros Han Sido Eliminados.')
            self.change_label.place(x=90,y=475)
            self.calculate_total()
        else:
            messagebox.showinfo('Advertencia', 'Borrar Todos los Registros Cancelado.')

        
        
