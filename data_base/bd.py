import sqlite3
from tkinter import END

class ConnectBd:

    def __init__(self):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        print('Conexión con la base de datos exitosa.')
        try:
            self.c.execute("""
                    CREATE TABLE if not exists Regist (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Farm INTEGER,
                        Hour TEXT,
                        Date TEXT
                    )
                    """)
        except Exception as e:
            print(e)
        self.conexion.commit()
        self.conexion.close()
    
    def insert(self, Farm, Hour, Date):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute('INSERT INTO Regist (Farm, Hour, Date) VALUES (?,?,?)', (Farm, Hour, Date))
        self.conexion.commit()
        self.conexion.close()

    def show(self, box, position):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute('SELECT * FROM Regist')
        regist_save = self.c.fetchall() 
        for row in regist_save:
            box.insert('',position,text=row[0], values=(row[1], row[2], row[3]))
        self.conexion.commit()
        self.conexion.close() 

    def show_in_filter(self, box, position, column, value):
        if column == 'Id':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Id = {value}')
            regist_save = self.c.fetchall() 
            for row in regist_save:
                box.insert('',position,text=row[0], values=(row[1], row[2], row[3]))
            self.conexion.commit()
            self.conexion.close() 
        elif column == 'Farmeo':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Farm = {value}')
            regist_save = self.c.fetchall() 
            for row in regist_save:
                box.insert('',position,text=row[0], values=(row[1], row[2], row[3]))
            self.conexion.commit()
            self.conexion.close() 
        elif column == 'Tiempo/h':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Hour = {value}')
            regist_save = self.c.fetchall() 
            for row in regist_save:
                box.insert('',position,text=row[0], values=(row[1], row[2], row[3]))
            self.conexion.commit()
            self.conexion.close() 

    def allow_filter(self, column, value):
        
        if column == 'Id':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Id= {value}')
            self.regist_save = self.c.fetchall()
            if len(self.regist_save) > 0:
                return True
            else:
                return False

        elif column == 'Farmeo':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Farm LIKE "{value}%"')
            self.regist_save = self.c.fetchall()
            if len(self.regist_save) > 0:
                return True
            else:
                return False

        elif column == 'Tiempo/h':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Hour LIKE "{value}%"')
            self.regist_save = self.c.fetchall()
            if len(self.regist_save) > 0:
                return True
            else:
                return False

    def filter_regist(self, column, box, value):

        if column == 'Id':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Id= {value}')
            self.regist_save = self.c.fetchall()
            for regist in self.regist_save:
                box.insert('', END, text=regist[0], values=(regist[1], regist[2], regist[3]))
            self.conexion.commit()
            self.conexion.close() 

        elif column == 'Farmeo':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Farm LIKE "{value}%"')
            self.regist_save = self.c.fetchall()
            for regist in self.regist_save:
                box.insert('', END, text=regist[0], values=(regist[1], regist[2], regist[3]))
            self.conexion.commit()
            self.conexion.close()
           
        elif column == 'Tiempo/h':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT * FROM Regist WHERE Hour LIKE "{value}%"')
            self.regist_save = self.c.fetchall()
            for regist in self.regist_save:
                box.insert('', END, text=regist[0], values=(regist[1], regist[2], regist[3]))
            self.conexion.commit()
            self.conexion.close()

    def edit(self, Id_selected, Farm, Hour, Date):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute(f'UPDATE Regist SET Farm ={Farm}, Hour ="{Hour}", Date ="{Date}" WHERE Id = {Id_selected}')
        self.conexion.commit()
        self.conexion.close()

    def delete(self, Id_selected):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute(f'DELETE FROM Regist WHERE Id = {Id_selected}')
        self.c.execute('DELETE FROM sqlite_sequence WHERE NAME="Regist"')
        self.conexion.commit()
        self.conexion.close()

    def delete_all(self):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute('DELETE FROM Regist')
        self.c.execute('DELETE FROM sqlite_sequence WHERE NAME="Regist"')
        self.conexion.commit()
        self.conexion.close()

    def delete_all_filter_box(self, column, value):
        if column == 'Id':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'DELETE FROM Regist WHERE Id = {value}')
            self.c.execute('DELETE FROM sqlite_sequence WHERE NAME="Regist"')
            self.conexion.commit()
            self.conexion.close()
        elif column == 'Farmeo':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'DELETE FROM Regist WHERE Farm = {value}')
            self.c.execute('DELETE FROM sqlite_sequence WHERE NAME="Regist"')
            self.conexion.commit()
            self.conexion.close()
        elif column == 'Tiempo/h':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'DELETE FROM Regist WHERE Hour = {value}')
            self.c.execute('DELETE FROM sqlite_sequence WHERE NAME="Regist"')
            self.conexion.commit()
            self.conexion.close()

    def sum_farm_filter(self, var, column, value):
        if column == 'Id':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT SUM (Farm) FROM Regist WHERE Id = {value}')
            amount = self.c.fetchone()
            amount_list = list(amount)
            if amount_list[0] == None:
                amount_list[0] = 0
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()
            else:
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()
        elif column == 'Farmeo':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT SUM (Farm) FROM Regist WHERE Farm = {value}')
            amount = self.c.fetchone()
            amount_list = list(amount)
            if amount_list[0] == None:
                amount_list[0] = 0
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()
            else:
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()
        elif column == 'Tiempo/h':
            self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
            self.c = self.conexion.cursor()
            self.c.execute(f'SELECT SUM (Farm) FROM Regist WHERE Hour = {value}')
            amount = self.c.fetchone()
            amount_list = list(amount)
            if amount_list[0] == None:
                amount_list[0] = 0
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()
            else:
                var.insert(END,amount_list)
                self.conexion.commit()
                self.conexion.close()

    def sum_farm(self, var):
        self.conexion = sqlite3.connect('data_base/data_base_regist.bd')
        self.c = self.conexion.cursor()
        self.c.execute('SELECT SUM (Farm) FROM Regist')
        amount = self.c.fetchone()
        amount_list = list(amount)
        if amount_list[0] == None:
            amount_list[0] = 0
            var.insert(END,amount_list)
            self.conexion.commit()
            self.conexion.close()
        else:
            var.insert(END,amount_list)
            self.conexion.commit()
            self.conexion.close()
    
    

    
        
