Web VPython 3.2
import random


scene.camera.axis = vec(0, -5, -30)
scene.camera.pos = vec(100, 100, 30)
scene.range = 15


play_button = box(pos=vec(50, 50, -30), length=10, height=5, width=0.1, color=color.green)
mines_button = box(pos=vec(75, 60, -30), length=10, height=5, width=0.1, color=color.black)
play_text = label(pos=play_button.pos + vec(0, 0, 5), text='Play', height=10, color=color.white, box=False)
board = cylinder(pos=vec(0, 0, 0), axis=vec(0, 0, 1), radius=25,texture="https://t4.ftcdn.net/jpg/01/04/42/77/360_F_104427763_JSbO5zUYbfKI4xwG5YGadfu1mGcirNz1.jpg", color=color.white)
background = box(pos=vec(0,0,-5), axis=vec(0,0,0), length = 110, height = 90, width = 0.1, texture = 'https://t3.ftcdn.net/jpg/02/81/17/66/360_F_281176674_ozBsmkE0E0AD38vfM7YoamOoXYcgWTGB.jpg', color=color.white)
reset_button = box(pos=vec(25,25,0), length = 10, height = 5, width = 0.1, color=color.white)
lose_message = text(text='You hit a mine!', pos=vec(122, 134,10), color=color.red, visible=False)
reset_text = label(pos=reset_button.pos+vec(-2,-2,5), text='reset', height = 10, color=color.white, box=False)
home_button = box(pos=reset_button.pos+vec(15,0,0), length = 10, height=5, width=0.1, color=color.yellow)
home_text=label(pos=home_button.pos+vec(-4,-2,5),text='home',height=10, color=color.white, box=False)
blue_win_message = text(text='Blue wins', pos=vec(-20,0,10), color=color.blue, visible=False, box=True, height = 7)
orange_win_message = text(text='Orange wins', pos=vec(-25,0,10), color=color.orange, visible=False, box=True, height = 7)



p1 = sphere(pos=vec(-5, 5, 2), radius=2, texture="https://i.imgur.com/KsZWwkQ.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(-5, 5, 2))
p2 = sphere(pos=vec(-5, 0, 2), radius=2, texture="https://i.imgur.com/KsZWwkQ.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(-5, 0, 2))
p3 = sphere(pos=vec(-5, -5, 2), radius=2, texture="https://i.imgur.com/KsZWwkQ.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(-5, -5, 2))
p4 = sphere(pos=vec(5, 5, 2), radius=2, texture="https://i.imgur.com/cDeqrfx.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(5, 5, 2))
p5 = sphere(pos=vec(5, 0, 2), radius=2, texture="https://i.imgur.com/cDeqrfx.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(5, 0, 2))
p6 = sphere(pos=vec(5, -5, 2), radius=2, texture="https://i.imgur.com/cDeqrfx.png", v=vec(0, 0, 0), m=1, alive=True, original_pos=vec(5, -5, 2))
penguins = [p1, p2, p3, p4, p5, p6]


a1 = arrow(pos=p1.pos, axis=vec(0, 0, 0), color=color.orange)
a2 = arrow(pos=p2.pos, axis=vec(0, 0, 0), color=color.orange)
a3 = arrow(pos=p3.pos, axis=vec(0, 0, 0), color=color.orange)
a4 = arrow(pos=p4.pos, axis=vec(0, 0, 0), color=color.blue)
a5 = arrow(pos=p5.pos, axis=vec(0, 0, 0), color=color.blue)
a6 = arrow(pos=p6.pos, axis=vec(0, 0, 0), color=color.blue)
arrows = [a1, a2, a3, a4, a5, a6]


slots = []
buttons = []
items = []
for y in range(100, 145, 11):  
    for x in range(100, 145, 11): 
        pos = vec(x, y, 0)
        slots.append(box(pos=pos, size=vec(9, 9, 2), color=color.white))
        buttons.append(box(pos=pos, size=vec(9, 9, 2), color=color.white, visible=False))
        items.append(box(pos=pos + vec(0, 0, 1), size=vec(6, 6, 2), color=color.green, visible=False))

# VARIBLES 🧖🏿
current_turn = 'orange'
maxForce = 10
is_dragging = False
selectedIndex = 2
prepPhase = True
board_radius=25
mine_chance = 1/25
number_of_mines = 24
multiplier=1

gambling=False
distribute_mines()

def go_home():
    scene.camera.pos = vec(50, 50, 0)
    play_button.visible = True
    play_text.visible = True
    mines_button.visible = True

def distribute_mines():
    global number_of_mines
    number_of_mines = 24
    mine_indices = set() 
    while number_of_mines > 0:
        index = random.randint(0, len(items)-1)
        if index not in mine_indices:
            items[index].color = color.red
            mine_indices.add(index)
            number_of_mines -= 1


def on_play_button_click():
    global gambling, penguins, arrows
    
    scene.camera.pos = vec(0, 0, 0)
    scene.camera.axis = vec(0, 0, -1)
    scene.range = 30
    play_button.visible = False
    play_text.visible = False
    mines_button.visible = False

    mines=False
    prepPhase = True
    for p in penguins:
        p.alive=True
        p.pos=p.original_pos
        p.visible=True
    for i in range(6):
        arrows[i].visible=True
        arrows[i].pos=penguins[i].pos
        arrows[i].axis=vec(0,0,0)
    
def on_mine_button_click():
    global mines
    
    scene.camera.pos = vec(140, 122, 0)
    scene.camera.axis = vec(0, 0, -1)
    scene.range = 30
    play_button.visible = False
    play_text.visible = False
    mines_button.visible = False
    mines=True

def on_mousedown(evt):
    global selectedIndex, is_dragging, current_turn, mines
    
    mouse_pos = scene.mouse.pos
    selectedIndex=-1
    
    
    if play_button.pos.x - play_button.length / 2 < mouse_pos.x < play_button.pos.x + play_button.length / 2 and \
       play_button.pos.y - play_button.height / 2 < mouse_pos.y < play_button.pos.y + play_button.height / 2:
        on_play_button_click()
        return
    
    if mines_button.pos.x - mines_button.length / 2 < mouse_pos.x < mines_button.pos.x + mines_button.length / 2 and \
       mines_button.pos.y - mines_button.height / 2 < mouse_pos.y < mines_button.pos.y + mines_button.height / 2:
        on_mine_button_click()
        return
    
    if reset_button.pos.x - reset_button.length / 2 < mouse_pos.x < reset_button.pos.x + reset_button.length / 2 and \
       reset_button.pos.y - reset_button.height / 2 < mouse_pos.y < reset_button.pos.y + reset_button.height / 2:
        on_play_button_click()
        return
    
    if home_button.pos.x - home_button.length / 2 < mouse_pos.x < home_button.pos.x + home_button.length / 2 and \
       home_button.pos.y - home_button.height / 2 < mouse_pos.y < home_button.pos.y + home_button.height / 2:
        go_home()
        return
    
    if mines:
        closest_mag = 1e6  
    
        select_index = -1
        for i, btn in enumerate(buttons):
            distance = mag(btn.pos - mouse_pos)
            if distance < closest_mag:
                closest_mag = distance
                select_index = i
        if select_index != -1:
            items[select_index].visible = True
            if items[select_index].color == color.red:
                rate(1)
                reset_board()
    else:
        closestMag = 999999
        for curr in range(6):
            if ((current_turn == 'orange' and curr < 3) or (current_turn == 'blue' and curr >= 3)) and penguins[curr].alive:
                if mag(penguins[curr].pos - evt.pos) < closestMag:
                    closestIndex = curr
                    closestMag = mag(penguins[curr].pos - evt.pos)
                    selectedIndex = closestIndex
                    arrows[selectedIndex].visible = True
                    is_dragging = True
    
    
    
    #if current_turn == 'orange' and selectedIndex < 3:
    #    arrows[selectedIndex].visible = True
    #elif current_turn == 'blue' and 3 <= selectedIndex < 6:
    #    arrows[selectedIndex].visible = True

def on_mouseup(evt):
    global is_dragging, selectedIndex, current_turn
    
    if current_turn == 'orange' and selectedIndex < 3:
        arrows[selectedIndex].visible = True
    
    is_dragging = False

def on_mousemove(evt):
    global is_dragging
    if is_dragging and prepPhase:
        arrows[selectedIndex].axis = penguins[selectedIndex].pos - evt.pos
        arrows[selectedIndex].axis.z = 0
        if mag(arrows[selectedIndex].axis) > maxForce:
            arrows[selectedIndex].axis = arrows[selectedIndex].axis / mag(arrows[selectedIndex].axis) * maxForce

dt = 0.01

def check_penguin_positions():
    global penguins, arrows, dt
    for i in range(len(penguins) - 1, -1, -1):
        if mag(penguins[i].pos) > board_radius:  
            arrows[i].visible = False 
            accel = -5
            velo = 0
            t=0
            penguins[i].alive=False
            
            penguins[i].pos = vec(1000,1000,1000)
            penguins[i].visible = False 
            

def keyInput(evt):
    global prepPhase, current_turn, arrows, penguins
    
    penguinSpeed = 3
    Af = 10
    k = 100
    
    s = evt.key
    if s == " ":
        if current_turn == 'orange':
            for arrow in arrows[:3]:
                arrow.visible = False
            current_turn = 'blue'
        elif current_turn == 'blue':
            for arrow in arrows[3:]:
                arrow.visible = False
            current_turn = 'nobody'
            for i, penguin in enumerate(penguins):
                penguin.v = arrows[i].axis
                arrows[i].axis = vec(0, 0, 0)
            for i, arrow in enumerate(arrows):
                arrow.pos = penguins[i].pos
        elif current_turn == 'nobody':
            prepPhase = False
            while not prepPhase:
                rate(100)
                any_movement = False
                for p in penguins:
                    if mag(p.v) > 0.1 and p.alive:
                        any_movement = True
                        p.pos += p.v * penguinSpeed * dt
                        p.v += (-p.v / mag(p.v)) * Af * dt
                        for other in penguins:
                            if p == other:
                                continue
                            if mag(other.pos - p.pos) < p.radius + other.radius:
                                dir = other.pos - p.pos
                                FOtherP = k * (mag(dir) - (p.radius + other.radius)) * norm(dir)
                                FPOther = -FOtherP
                                p.v += FOtherP * dt / p.m
                                other.v += FPOther * dt / other.m
                check_penguin_positions()
                if not any_movement:
                    prepPhase = True
                    for i, arrow in enumerate(arrows):
                        arrow.pos = penguins[i].pos
                    current_turn = 'orange'
                    if not(penguins[0].alive or penguins[1].alive or penguins[2].alive):
                        blue_message_win()
                    elif not(penguins[3].alive or penguins[4].alive or penguins[5].alive):
                        orange_message_win()
        
            


def reset_board():
    for item in items:
        item.color = color.green
        item.visible = False
    distribute_mines()
    display_lose_message()

def display_lose_message():
    lose_message.visible = True
    rate(1/3)  
    lose_message.visible = False
    
def orange_message_win():
    orange_win_message.visible=True
    rate(1/3)  
    orange_win_message.visible = False
    
def blue_message_win():
    blue_win_message.visible=True
    rate(1/3)  
    blue_win_message.visible=False


scene.bind('keydown', keyInput)
scene.bind('mousedown', on_mousedown)
scene.bind('mouseup', on_mouseup)
scene.bind('mousemove', on_mousemove)

# COMERA

scene.camera.pos = vec(50, 50, 0)