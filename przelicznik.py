import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def km_to_miles():
    km = float(entry_km.get())
    miles = km * 0.621371
    label_result.config(text=f"{km} kilometrów to {miles} mil.")

def miles_to_km():
    miles = float(entry_miles.get())
    km = miles / 0.621371
    label_result.config(text=f"{miles} mil to {km} kilometrów.")

def celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit = (celsius * 9/5) + 32
    label_result.config(text=f"{celsius} stopni Celsjusza to {fahrenheit} stopni Fahrenheita.")

def fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius = (fahrenheit - 32) * 5/9
    label_result.config(text=f"{fahrenheit} stopni Fahrenheita to {celsius} stopni Celsjusza.")

def pounds_to_kg():
    pounds = float(entry_pounds.get())
    kg = pounds * 0.453592
    label_result.config(text=f"{pounds} funtów to {kg} kilogramów.")

def kg_to_pounds():
    kg = float(entry_kg.get())
    pounds = kg / 0.453592
    label_result.config(text=f"{kg} kilogramów to {pounds} funtów.")

def meters_to_yards():
    meters = float(entry_meters.get())
    yards = meters * 1.09361
    label_result.config(text=f"{meters} metrów to {yards} jardów.")

def yards_to_meters():
    yards = float(entry_yards.get())
    meters = yards / 1.09361
    label_result.config(text=f"{yards} jardów to {meters} metrów.")

def exit_program():
    if messagebox.askokcancel("Wyjście", "Czy na pewno chcesz zamknąć aplikację?"):
        window.destroy()

window = tk.Tk()
window.title("Przelicznik jednostek")

style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                padding=10)

style.configure("TLabel",
                font=("Helvetica", 14),
                padding=10)

style.configure("TFrame",
                background="#f0f0f0")

style.configure("TLabel",
                background="#f0f0f0",
                foreground="#333333")

style.configure("TEntry",
                fieldbackground="#ffffff")

frame_main = ttk.Frame(window)
frame_main.pack(expand=True, fill=tk.BOTH, padx=50, pady=50)

label_km = ttk.Label(frame_main, text="Kilometry:")
label_km.grid(row=0, column=0, padx=(0, 10))
entry_km = ttk.Entry(frame_main)
entry_km.grid(row=0, column=1)

label_miles = ttk.Label(frame_main, text="Mile:")
label_miles.grid(row=1, column=0, padx=(0, 37))
entry_miles = ttk.Entry(frame_main)
entry_miles.grid(row=1, column=1)

label_celsius = ttk.Label(frame_main, text="Celsjusze:")
label_celsius.grid(row=2, column=0, padx=(0, 15))
entry_celsius = ttk.Entry(frame_main)
entry_celsius.grid(row=2, column=1)

label_fahrenheit = ttk.Label(frame_main, text="Fahrenheity:")
label_fahrenheit.grid(row=3, column=0, padx=(0, 5))
entry_fahrenheit = ttk.Entry(frame_main)
entry_fahrenheit.grid(row=3, column=1)

label_pounds = ttk.Label(frame_main, text="Funty:")
label_pounds.grid(row=4, column=0, padx=(0, 26))
entry_pounds = ttk.Entry(frame_main)
entry_pounds.grid(row=4, column=1)

label_kg = ttk.Label(frame_main, text="Kilogramy:")
label_kg.grid(row=5, column=0, padx=(0, 10))
entry_kg = ttk.Entry(frame_main)
entry_kg.grid(row=5, column=1)

label_meters = ttk.Label(frame_main, text="Metry:")
label_meters.grid(row=6, column=0, padx=(0, 33))
entry_meters = ttk.Entry(frame_main)
entry_meters.grid(row=6, column=1)

label_yards = ttk.Label(frame_main, text="Jardy:")
label_yards.grid(row=7, column=0, padx=(0, 30))
entry_yards = ttk.Entry(frame_main)
entry_yards.grid(row=7, column=1)

button_km_to_miles = ttk.Button(frame_main, text="Przelicz Kilometry na Mile", command=km_to_miles)
button_km_to_miles.grid(row=8, column=0, columnspan=2, pady=5)

button_miles_to_km = ttk.Button(frame_main, text="Przelicz Mile na Kilometry", command=miles_to_km)
button_miles_to_km.grid(row=9, column=0, columnspan=2, pady=5)

button_celsius_to_fahrenheit = ttk.Button(frame_main, text="Przelicz Celsjusze na Fahrenheity", command=celsius_to_fahrenheit)
button_celsius_to_fahrenheit.grid(row=10, column=0, columnspan=2, pady=5)

button_fahrenheit_to_celsius = ttk.Button(frame_main, text="Przelicz Fahrenheity na Celsjusze", command=fahrenheit_to_celsius)
button_fahrenheit_to_celsius.grid(row=11, column=0, columnspan=2, pady=5)

button_pounds_to_kg = ttk.Button(frame_main, text="Przelicz funty na kilogramy", command=pounds_to_kg)
button_pounds_to_kg.grid(row=12, column=0, columnspan=2, pady=5)

button_kg_to_pounds = ttk.Button(frame_main, text="Przelicz kilogramy na funty", command=kg_to_pounds)
button_kg_to_pounds.grid(row=13, column=0, columnspan=2, pady=5)

button_meters_to_yards = ttk.Button(frame_main, text="Przelicz Metry na Jardy", command=meters_to_yards)
button_meters_to_yards.grid(row=14, column=0, columnspan=2, pady=5)

button_yards_to_meters = ttk.Button(frame_main, text="Przelicz Jardy na Metry", command=yards_to_meters)
button_yards_to_meters.grid(row=15, column=0, columnspan=2, pady=5)

button_exit = ttk.Button(frame_main, text="Wyjdź", command=exit_program)
button_exit.grid(row=16, column=0, columnspan=2, pady=5)

label_result = ttk.Label(frame_main, text="", font=("Helvetica", 12), anchor="center")
label_result.grid(row=17, column=0, columnspan=2, pady=10)

label_copyright = ttk.Label(frame_main, text="© 2023 Szymon Wasik. Wersja 1.0.3", font=("Helvetica", 10), anchor="center")
label_copyright.grid(row=18, column=0, columnspan=2)

window.mainloop()
