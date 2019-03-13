size(500, 500)
background(0)

interval = 255/5

gradient_width = gradient_height = width

xpos = width / 2
ypos = height / 2

noStroke()

fill(interval)
ellipse(xpos, ypos, gradient_width, gradient_height)

fill(interval * 2)
ellipse(xpos, ypos, (gradient_width-interval), (gradient_height-interval))

fill(interval * 3)
ellipse(xpos, ypos, (gradient_width - (interval * 2)), (gradient_height - (interval * 2)))
        
fill(interval * 4)
ellipse(xpos, ypos, (gradient_width - (interval * 3)), (gradient_height - (interval * 3)))

fill(interval * 5)
ellipse(xpos, ypos, (gradient_width - (interval * 4)), (gradient_height - (interval * 4))) 