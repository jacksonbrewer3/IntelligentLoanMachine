import tkinter as tk

def show_selection():
    selected_option = tk.StringVar.get(selected_var)
    new_label = tk.Label(root, text=selected_option, font=("Arial", 12, "bold"))
    new_label.grid(row=len(labels) + 1, column=0, pady=5)
    labels.append(new_label)
    dropdown.grid_forget()
    button.config(state="disabled")

root = tk.Tk()
root.geometry("300x200")

options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected_var = tk.StringVar()
selected_var.set(options[0])

dropdown = tk.OptionMenu(root, selected_var, *options)
dropdown.grid(row=0, column=0, pady=5)

button = tk.Button(root, text="Select Option", command=show_selection)
button.grid(row=1, column=0, pady=5)

labels = []

root.mainloop()
