import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Basic Tkinter App")
root.geometry("300x200")

# Function to update label text
def on_click():
    label.config(text="Button Clicked!")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()  #how we fit our elements in that parent gui

# Run the Tkinter event loop
root.mainloop()  

# root = main loop = event handler = put it in loop