import tkinter as tk

# Function to update the display when buttons are pressed
def button_click(value):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + str(value))

# Function to clear the display
def clear_display():
    entry_field.delete(0, tk.END)

# Function to evaluate the expression in the display
def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception as e:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field to display the input and output
entry_field = tk.Entry(window, width=20, borderwidth=5, font=('Arial', 18), justify='right')
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
button_layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Create buttons using loops
for r, row in enumerate(button_layout):
    for c, btn_text in enumerate(row):
        if btn_text == 'C':
            button = tk.Button(window, text=btn_text, padx=40, pady=20, font=('Arial', 14),
                               command=clear_display)
        elif btn_text == '=':
            button = tk.Button(window, text=btn_text, padx=40, pady=20, font=('Arial', 14),
                               command=calculate)
        else:
            button = tk.Button(window, text=btn_text, padx=40, pady=20, font=('Arial', 14),
                               command=lambda val=btn_text: button_click(val))

        button.grid(row=r + 1, column=c)

# Run the main loop
window.mainloop()
