# making plantes
mercury = Planet("Mercury",40, 'grey')
venus = Planet("Venus",80, 'orange')
earth=Planet("Earth",100,'blue')
mars = Planet("Mars",150, 'red')
jupiter=Planet("Jupiter",180, 'brown')
saturn=Planet("Saturn",230, 'pink')
uranus=Planet("Uranus",250, 'light blue')
neptune=Planet("Neptune",280, 'black')
 
#adding planets to a list
myList = [ mercury, venus,earth, mars,jupiter,saturn,uranus,neptune]
 
 
while True:#while statement
    screen.update()#updating the screen
    for i in myList:
        i.move()#moving the elements of the list
 
    # Increase the angle by 0.0x radians
   
    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005
