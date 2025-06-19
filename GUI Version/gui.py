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
tk.Label(root, text="Dice (e.g. 2d6):").grid(row = 0, column = 0)
entry_dice = tk.Entry(root)
entry_dice.grid(row = 0, column = 1)
tk.Label(root, text="Target number:").grid(row = 1, column = 0)
entry_target = tk.Entry(root)
entry_target.grid(row = 1, column = 1)
tk.Button(root, text="Calculate", command = calculate).grid(row = 2, columnspan = 2)
result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).grid(row = 3, columnspan = 2)
root.mainloop()
