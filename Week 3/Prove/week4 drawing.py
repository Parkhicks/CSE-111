import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas)
    draw_ground(canvas)
    draw_trees(canvas)
    draw_fence(canvas)
    finish_drawing(canvas)
    

def draw_cloud(canvas):
        for i in range (1,5):
            x0 = random.randint(0,800)
            y0 =random.randint(200,450)
            draw_oval(canvas, x0, y0, (x0+100),(y0+75),width =0, fill="white")

def draw_sky(canvas):
    draw_rectangle(canvas,0,0,800,500,width=0,fill="skyblue")
    draw_cloud(canvas)
    draw_cloud(canvas)

def draw_ground(canvas):
    draw_rectangle(canvas,0,0,800,150,width=1,fill="tan2")

def draw_trees(canvas):
    draw_rectangle(canvas,30,50,50,400,width=0,fill="brown")
    y0=60
    y1=200
    x0 =-40
    x1 = 120

    for i in range(1,7):
        draw_polygon(canvas,x0,y0,40,y1,x1,y0,width=0,fill="dark green")
        y0 += 50
        y1 += 50
        x0 += 10
        x1 -= 10
    
    draw_rectangle(canvas,130,50,150,460,width=0,fill="brown")
    y0=60
    y1=200
    x0 =60
    x1 = 220

    for i in range(1,7):
        draw_polygon(canvas,x0,y0,140,y1,x1,y0,width=0,fill="dark green")
        y0 += 65
        y1 += 65
        x0 += 10
        x1 -= 10

def draw_fence(canvas):
    x0=0
    x2=10
    x1=20
    y0=0
    for i in range (1,14):
        draw_rectangle(canvas,x0,y0,x1,125,width=0,fill="white")
        draw_polygon(canvas,x0,125,x2,140,x1,125,width=0, fill="white")
        x0 +=30
        x1 +=30
        x2 +=30
    draw_rectangle(canvas,0,40,x0,60,width=0, fill="white")
    draw_rectangle(canvas,0,80,x0,100,width=0, fill="white")

main()