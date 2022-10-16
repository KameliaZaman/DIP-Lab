name = "Max"
def hello_you(person):
    sentence = "Hello " + person
    return sentence
hello_you("Max")

def plotter(x, y):
    instructions = "Plot a course through " + str(x) + " and " + str(y)
    return instructions
plotter(3, 5)

def absolute_value(num):
    if num >= 0:
        return num
    else:
        return num * -1
absolute_value(-4)

def favorite(category, thing):
    sentence = "My favorite " + category + " is the " + thing
    return sentence
favorite("snake", "Python")
