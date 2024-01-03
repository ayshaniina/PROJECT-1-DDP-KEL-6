import tkinter 
from tkinter import *
from tkinter import ttk  # Import the ttk module

root = Tk()
root.title("Kalkulator Nilai")
root.geometry("500x400")
root.configure(bg="#ADD8E6")

def Calculation():
    mapel = str(mata_pelajaran_combobox.get())  # Use the ComboBox get method to get the selected value
    nilai = int(nilaientry.get())
    skills = int(analytical_skillentry.get())
    general = int(generalentry.get())
    total = nilai + skills + general
    Label(text=f"{total}", font="arial 15 bold").place(x=250, y=170)

    average = int(total / 3)
    Label(text=f"{average}", font="arial 15 bold", fg="blue").place(x=250, y=210)

    if average > 70:
        grade = "LULUS"
    else:
        grade = "GAGAL"

    Label(text=f"{grade}", font="arial 15 bold").place(x=250, y=250)

# subject
sub1 = Label(root, text="Mata Pelajaran:", font="arial 10")
sub2 = Label(root, text="Nilai Ujian:", font="arial 10")
sub3 = Label(root, text="Keterampilan:", font="arial 10")
sub4 = Label(root, text="Pengetahuan:", font="arial 10")
total = Label(root, text="Total:", font="arial 10")
avg = Label(root, text="Rata-rata:", font="arial 10")
grade = Label(root, text="Keterangan:", font="arial 10")

sub1.place(x=50, y=10)
sub2.place(x=50, y=50)
sub3.place(x=50, y=90)
sub4.place(x=50, y=130)
total.place(x=50, y=170)
avg.place(x=50, y=210)
grade.place(x=50, y=250)

# Create a list of subjects for the ComboBox
subjects = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Pendidikan Agama","Pendidikan Kewarganegaraan","Ilmu Pengetahuan Sosial","Ilmu Pengetahuan Alam"]

# Use StringVar to store the selected subject
mata_pelajaranvalue = StringVar()

# Create a Combobox and set its values
mata_pelajaran_combobox = ttk.Combobox(root, textvariable=mata_pelajaranvalue, values=subjects, font="arial 15", state="readonly")
mata_pelajaran_combobox.place(x=250, y=10)

nilaivalue = StringVar()
analytical_skillvalue = StringVar()
generalvalue = StringVar()

nilaientry = Entry(root, textvariable=nilaivalue, font="arial 15", width=15)
analytical_skillentry = Entry(root, textvariable=analytical_skillvalue, font="arial 15", width=15)
generalentry = Entry(root, textvariable=generalvalue, font="arial 15", width=15)

nilaientry.place(x=250, y=50)
analytical_skillentry.place(x=250, y=90)
generalentry.place(x=250, y=130)

Button(text="Hitung", font="arial 15", bg="#ADD8E6", bd=10, command=Calculation).place(x=50, y=300)
Button(text="Keluar", font="arial 15", bg="#ADD8E6", bd=10, width=8, command=lambda: exit()).place(x=350, y=300)

root.mainloop()