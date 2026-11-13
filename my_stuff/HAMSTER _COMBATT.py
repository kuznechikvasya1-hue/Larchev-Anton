import tkinter as tk
hamsters = 0
root = tk.Tk()
root.title("ХАМСТЕР КОМБАТ")
root.geometry(f"{250}x{250}")
label = tk.Canvas(root, width=250, height=100, bg="white")
label.pack(pady=25)
button_one = tk.Button(root, height=5, width=600, text="ХОМЯК", command=lambda: hamster(1))
button_one.pack(pady=20)

def hamster(plus):
    global hamsters
    hamsters += plus
    label.delete("all")
    label.create_text(125, 50, text=f"ХОМЯКОВ: {hamsters}")

hamster(0)

root.mainloop()