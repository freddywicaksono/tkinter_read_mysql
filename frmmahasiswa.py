import tkinter as tk
from tkinter import ttk
from turtle import width
import mysql.connector as mc
from tkinter.messagebox import showinfo
from Mahasiswa import Mahasiswa

root = tk.Tk()
root.title('Treeview demo')
root.geometry('420x200')

# define columns
columns = ('idmhs', 'nim', 'nama','jk','kode_prodi')

tree = ttk.Treeview(root, columns=columns, show='headings')

# define headings
tree.heading('idmhs', text='ID')
tree.column('idmhs', width="30")
tree.heading('nim', text='NIM')
tree.column('nim', width="60")
tree.heading('nama', text='Nama')
tree.column('nama', width="200")
tree.heading('jk', text='JK')
tree.column('jk', width="30")
tree.heading('kode_prodi', text='Kode Prodi')
tree.column('kode_prodi', width="100")
# generate sample data
mhs = Mahasiswa()
result = mhs.getAllData()

students=[]
for row_data in result:
    students.append(row_data)

for student in students:
    tree.insert('',tk.END, values=student)

# set tree position
tree.grid(row=1, column=0, sticky='nsew')

# add a scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='ns')

# run the app
root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         