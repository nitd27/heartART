#word for drawing
characters = ".kishmish."

#range
x_range = range(-30, 30)
y_range = range(15, -15, -1)

#empty list to store lines of output
outputLines = []

#main
for y in y_range:
    
    line = ""
    
    
    for x in x_range:
        
        eq = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
        
        
        charIndex = (x - y) % 10 if eq <= 0 else 0
        
        
        line += characters[charIndex]
    
    
    outputLines.append(line)


print('\n'.join(outputLines))
