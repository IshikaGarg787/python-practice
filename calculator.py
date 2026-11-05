import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry field
entry = tk.Entry(root, width=16, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create buttons
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2,
                           command=lambda text=button_text: on_click(text))
        button.grid(row=i+1, column=j, padx=5, pady=5)

# Run the application
root.mainloop()

