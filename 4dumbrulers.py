import tkinter as tk
import random
import time

SIZE = 20
CELL = 35
COLORS = ["white", "red", "purple", "orange", "lime"]
rulerlands = {}

redr = {
    "name": "redr",
    "number": 1,
    "food": 6,
    "agression" : random.random(),
    "territory" : 1,
    "army" : 5,
    "cx": 0,
    "cy": SIZE-1,
    "color": COLORS[1]
}

blur = {
    "name": "blur",
    "number": 2,
    "food": 5,
    "agression" : random.random(),
    "territory" : 1,
    "army" : 4,
    "cx" : 0,
    "cy" : 0,
    "color": COLORS[2]
}

grer = {
    "name": "grer",
    "number": 4,
    "food": 10,
    "agression" : random.random(),
    "territory" : 1,
    "army" : 1,
    "cx" : SIZE-1,
    "cy" : SIZE-1,
    "color": COLORS[4]
}

yelr = {
    "name": "yelr",
    "number": 3,
    "food": 6,
    "agression" : random.random(),
    "territory" : 1,
    "army" : 5,
    "cx" : SIZE-1,
    "cy" : 0,
    "color": COLORS[3]
}

rulers = [redr, blur, grer, yelr]

map_data = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

root = tk.Tk()
root.title("4 dumb rulers")
root.geometry(f"{400+CELL*SIZE}x{300+CELL*SIZE}")  # Width x Height

canvas = tk.Canvas(root, width=SIZE*CELL, height=SIZE*CELL, bg="white")
canvas.pack(pady=25)  # Top-center with 50px margin
txtcanvas = tk.Canvas(root, width=SIZE*CELL+200, height=100, bg="white")
txtcanvas.pack()
def movement(id, attack):
    cx = id['cx']
    cy = id['cy']
    num = id['number']
    direc = random.randint(1,4)
    if direc == 1 and cy-1 >= 0:
        if map_data[cx][cy-1] == 0 or map_data[cx][cy-1] == num or (attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx][cy-1] != num): # если кто-то посмотрит этот код - не спрашивайте.
            id['cy'] -= 1
            cy -= 1
            map_data[cx][cy] = num
            if attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx][cy-1] != num:
                id['army'] -= 2
    if direc == 2 and cx-1 >= 0:
        if map_data[cx-1][cy] == 0 or map_data[cx-1][cy] == num or (attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx-1][cy] != num):
            id['cx'] -= 1
            cx -= 1
            map_data[cx][cy] = num
            if attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx][cy-1] != num:
                id['army'] -= 2
    if direc == 3 and cy+1 <= SIZE - 1:
        if map_data[cx][cy+1] == 0 or map_data[cx][cy+1] == num or (attack == True and id['army']-2 >= 0  and map_data[cx][cy+1] != 0 and map_data[cx][cy+1] != num):
            id['cy'] += 1
            cy += 1
            map_data[cx][cy] = num
            if attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx][cy-1] != num:
                id['army'] -= 2
    if direc == 4 and cx+1 <= SIZE-1:
        if map_data[cx+1][cy] == 0 or map_data[cx+1][cy] == num or (attack == True and id['army']-2 >= 0 and map_data[cx+1][cy] != 0 and map_data[cx+1][cy] != num):
            id['cx'] += 1
            cx += 1
            map_data[cx][cy] = num
            if attack == True and id['army']-2 >= 0 and map_data[cx][cy-1] != 0 and map_data[cx][cy-1] != num:
                id['army'] -= 2
    else:
        pass

def ai_of_the_ruler(id):
    global rulers
    agr = id['agression']
    num = id['number']
    count = sum(row.count(num) for row in map_data)
    if count == 0:
        rulers.remove(id)
    
    if count > 0:
        if random.random() <= agr:
            attack = True
            movement(id, attack)
        else:
            attack = False
            movement(id, attack)
            if id['army'] < 10:
                id['army'] += 1


def on_click(event):

    x = event.x // CELL
    y = event.y // CELL
    if 0 <= x < SIZE and 0 <= y < SIZE:
        print(f"Clicked tile ({x}, {y})")
    

canvas.bind("<Button-1>", on_click)

# Draw grid
def draw_map(map_data):
    canvas.delete("all")
    
    for x in range(SIZE):
        for y in range(SIZE):
            color = COLORS[map_data[x][y]]
            canvas.create_rectangle(
                x*CELL, y*CELL,
                (x+1)*CELL, (y+1)*CELL,
                fill=color, outline="black"
            )
            canvas.create_rectangle(2, 2, CELL*SIZE, CELL*SIZE, outline="black")
    global rulers
    for ruler in rulers:
        x = ruler['cx']
        y = ruler['cy']
        canvas.create_oval(x*CELL + 3, y * CELL + 3, (x+1)*CELL -3, (y+1)*CELL -3, outline = "white", fill=ruler["color"], width = 2)

map_data[0][len(map_data)-1] = 1
map_data[0][0] = 2
map_data[len(map_data[1])-1][0] = 3
map_data[len(map_data[1])-1][len(map_data)-1] = 4

draw_map(map_data)

def zalooper():
    for ruler in rulers:
        ai_of_the_ruler(ruler)
    txtcanvas.delete("all")
    txtcanvas.create_text(10, 10, text=' '.join(['redr army:', str(redr['army']), 'aggression:', str(int(redr['agression']*100))]), fill=COLORS[redr['number']], font=("Arial", 14), anchor="nw")
    txtcanvas.create_text(10, 90, text=' '.join(['blur army:', str(blur['army']), 'aggression:', str(int(blur['agression']*100))]), fill=COLORS[blur['number']], font=("Arial", 14), anchor="sw")
    txtcanvas.create_text(SIZE*CELL+200-10, 90, text=' '.join(['yelr army:', str(yelr['army']), 'aggression:', str(int(yelr['agression']*100))]), fill=COLORS[yelr['number']], font=("Arial", 14), anchor="se")
    txtcanvas.create_text(SIZE*CELL+200-10, 10, text=' '.join(['grer army:', str(grer['army']), 'aggression:', str(int(grer['agression']*100))]), fill=COLORS[grer['number']], font=("Arial", 14), anchor="ne")

    draw_map(map_data)
    if sum(row.count(0) for row in map_data) == 0:
        for ruler in rulers:
            rulerlands[ruler['name']] = sum(row.count(ruler['number']) for row in map_data)
        top = max(rulerlands, key=rulerlands.get)
        mr = rulerlands[top]
        txtcanvas.delete("all")
        txtcanvas.create_text((SIZE*CELL+200)/2, 0, text=' '.join(["THE DUMB RULER", top.upper(), "WON WITH", str(mr), "IN LAND"]), fill='black', font=("Arial", 14), anchor="n") 
        print(rulerlands)
    else:
        root.after(20, zalooper)

zalooper()

root.mainloop()