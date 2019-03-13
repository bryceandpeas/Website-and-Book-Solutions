speed_x = 0.7
speed_y = 0.9

cells = 2000

px = []
py = []
radii_x = []
radii_y = []
angle = []
frequency = []
cell_radius = []

def setup():
    
    global radii_x, radii_y, angle, frequency, cell_radius
    global head_x, head_y
    
    size(400, 400)
    frameRate(30)

    head_x = width / 2
    head_y = height / 2
    
    for i in range(0, cells):
        radii_x.append(random(-7, 7))
        radii_y.append(random(-4, 4))
        frequency.append(random(-9, 9))
        cell_radius.append(random(16, 40))
        angle.append(random(cells))
    
def draw():
    
    global speed_x, speed_y, cells, px, py
    global radii_x, radii_y, angle, frequency, cell_radius
    global head_x, head_y
    
    background(0)
    noStroke()
    fill(255, 255, 255, 5)
  
    for i in range(0, cells):
        if i == 0:
            px.append(head_x + sin(radians(angle[i])) * radii_x[i])
            py.append(head_y + cos(radians(angle[i])) * radii_y[i])
        else:
            px.append(px[i-1] + cos(radians(angle[i])) * radii_x[i])
            py.append(py[i-1] + sin(radians(angle[i])) * radii_y[i])

            if (px[i] >= width - cell_radius[i] / 2) or (px[i] <= cell_radius[i] / 2):
                radii_x[i] *= -1
                cell_radius[i] = random(1, 40)
                frequency[i]= random(-13, 13)
    
            if (py[i] >= height - cell_radius[i] / 2) or (py[i] <= cell_radius[i] / 2):
                radii_y[i] *= -1
                cell_radius[i] = random(1, 40)
                frequency[i] = random(-9, 9)
 
        ellipse(px[i],  py[i],  cell_radius[i],  cell_radius[i])
        angle[i] += frequency[i]

    head_x += speed_x
    head_y += speed_y

    if (head_x >= width - cell_radius[0] / 2) or (head_x <= cell_radius[0] / 2):
        speed_x *= -1

    if (head_y >= height - cell_radius[0] / 2) or (head_y <= cell_radius[0] / 2):
        speed_y *= -1
 
