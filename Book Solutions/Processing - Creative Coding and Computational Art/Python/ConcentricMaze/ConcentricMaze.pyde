size(400, 400)
background(0)
strokeWeight(1)
stroke(255)
smooth()
x = width - 1
y = height - 1
y2 = 0
x2 = 0
h = 0
w = 0

wStep = 10.0
hStep = 10.0
noFill()
beginShape()
vertex(x - w, y2 + h)
for i in range((min(width, height)), (min(width, height) / 2), -int((max(wStep, hStep)))):
    vertex(x - w, y - h)
    vertex(x2 + w, y - h)
    vertex(x2 + w, y2 + h)
    w += wStep
    vertex(x - w, y2 + h)
    h += hStep
endShape()