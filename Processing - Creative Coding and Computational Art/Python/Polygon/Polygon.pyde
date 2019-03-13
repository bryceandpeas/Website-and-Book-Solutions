sides = 8
angle = 90
radius = 100
pts_x = []
pts_y = []

def setup():
    
    global sides, angle, radius, pts_x, pts_y

    
    size(200, 200, JAVA2D)
    cx = width / 2
    cy = height / 2
    background(255)
 
    for i in range(0, sides):
        px = cx + cos(radians(angle)) * radius
        py = cy + sin(radians(angle)) * radius
        pts_x.append(px)
        pts_y.append(py)
        angle += 360 / sides
        
    draw_shape()

def draw_shape():
    noFill()
    
    for i in range(0, sides):
        if (i == sides - 1):
             line(pts_x[i], pts_y[i], pts_x[0], pts_y[0])
        else:
            line(pts_x[i], pts_y[i], pts_x[i+1], pts_y[i+1])
