import tkinter as tk
from tkinter import messagebox
from dice_probability import chance_to_hit_target

def parse_dice_input(dice_str):
    try:
        num, sides = dice_str.lower().split("d")
        return int(num), int(sides)
    except ValueError:
        raise ValueError("Invalid format. Use something like 2d6.")

def calculate():
    try:
        num_dice, sides = parse_dice_input(entry_dice.get())
        target = int(entry_target.get())
        chance = chance_to_hit_target(num_dice, sides, target)
        result_var.set(f"Chance of {target}+ is {chance:.2f}%")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Dice Probability Calculator")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

#____________________Styling____________________
font_label = ("Arial", 10)
font_result = ("Arial", 12, "bold")

#____________________Centre Frame____________________
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True)

#____________________Dice Row____________________
row1 = tk.Frame(frame, bg="#f0f0f0")
tk.Label(row1, text="Dice (e.g. 2d6):", font=font_label, bg="#f0f0f0").pack(side="left", padx=10, pady=5)
entry_dice = tk.Entry(row1, width=10)
entry_dice.pack(side="left", padx=10, pady=5)
row1.pack()

#____________________Target Row____________________
row2 = tk.Frame(frame, bg="#f0f0f0")
tk.Label(row2, text="Target number:", font=font_label, bg="#f0f0f0").pack(side="left", padx=10, pady=5)
entry_target = tk.Entry(row2, width=10)
entry_target.pack(side="left", padx=10, pady=5)
row2.pack()

#____________________Calculate Button____________________
tk.Button(frame, text="Calculate", command=calculate).pack(pady=10)

#____________________Result Label____________________
result_var = tk.StringVar()
tk.Label(frame, textvariable=result_var, font=font_result, bg="#f0f0f0").pack(pady=5)

#____________________Centre Window____________________
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f"+{x}+{y}")

root.mainloop()
