import tkinter as tk
from tkinter import ttk

# Conversion factors for different units
conversion_factors = {
    'length': {
        'meters': 1,
        'kilometers': 0.001,
        'feet': 3.28084,
        'miles': 0.000621371
    },
    'mass': {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274
    },
    'volume': {
        'liters': 1,
        'milliliters': 1000,
        'cubic meters': 0.001,
        'cubic feet': 0.0353147
    }
}


def convert(unit_type):
    try:
        value = float(entry_value[unit_type].get())
        from_unit = combo_from[unit_type].get()
        to_unit = combo_to[unit_type].get()
        result = value * conversion_factors[unit_type][to_unit] / conversion_factors[unit_type][from_unit]
        label_result[unit_type].config(text=f'{value} {from_unit} = {result:.4f} {to_unit}', foreground='blue')
    except ValueError:
        label_result[unit_type].config(text='Invalid input', foreground='red')


# Create the main window
root = tk.Tk()
root.title('Unit Converter')
root.geometry("400x350")
root.resizable(False, False)

# Style configuration
style = ttk.Style()

style.configure('TFrame', background='#e0f7fa')
style.configure('TNotebook', background='#e0f7fa', borderwidth=0)
style.configure('TNotebook.Tab', background='#00796b', foreground='black', padding=[10, 5])
style.map('TNotebook.Tab', background=[('selected', '#004d40')])

style.configure('TLabel', background='#e0f7fa', foreground='black', font=('Arial', 10))
style.configure('TEntry', padding=5)
style.configure('TButton', background='#00796b', foreground='black', padding=[5, 5], borderwidth=0)
style.map('TButton', background=[('active', '#004d40')])

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True, fill='both')

# Create frames for each tab
frames = {}
entry_value = {}
combo_from = {}
combo_to = {}
label_result = {}

unit_types = ['length', 'mass', 'volume']

for unit_type in unit_types:
    frames[unit_type] = ttk.Frame(notebook, padding=10)
    notebook.add(frames[unit_type], text=unit_type.capitalize())

    # Create and place widgets within each frame
    label_value = ttk.Label(frames[unit_type], text='Value:')
    label_value.grid(column=0, row=0, padx=5, pady=5, sticky='E')

    entry_value[unit_type] = ttk.Entry(frames[unit_type], width=20)
    entry_value[unit_type].grid(column=1, row=0, padx=5, pady=5)

    label_from = ttk.Label(frames[unit_type], text='From:')
    label_from.grid(column=0, row=1, padx=5, pady=5, sticky='E')

    combo_from[unit_type] = ttk.Combobox(frames[unit_type], values=list(conversion_factors[unit_type].keys()),
                                         state='readonly', width=17)
    combo_from[unit_type].grid(column=1, row=1, padx=5, pady=5)
    combo_from[unit_type].set(list(conversion_factors[unit_type].keys())[0])

    label_to = ttk.Label(frames[unit_type], text='To:')
    label_to.grid(column=0, row=2, padx=5, pady=5, sticky='E')

    combo_to[unit_type] = ttk.Combobox(frames[unit_type], values=list(conversion_factors[unit_type].keys()),
                                       state='readonly', width=17)
    combo_to[unit_type].grid(column=1, row=2, padx=5, pady=5)
    combo_to[unit_type].set(list(conversion_factors[unit_type].keys())[1])

    button_convert = ttk.Button(frames[unit_type], text='Convert', command=lambda u=unit_type: convert(u))
    button_convert.grid(column=0, row=3, columnspan=2, padx=5, pady=15)

    label_result[unit_type] = ttk.Label(frames[unit_type], text='', font=('Arial', 12, 'bold'))
    label_result[unit_type].grid(column=0, row=4, columnspan=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()