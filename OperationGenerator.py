import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2): continue
        line = aline
    return(line)

print("Operation {0} {1}".format(
    random_line(open("adj.txt")).strip().capitalize(), 
    random_line(open("noun.txt")).strip().capitalize()))
