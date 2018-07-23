
# Read text file
def readheaders(filename):
    with open(filename,'r') as f:
        for line in f:
            if(line.startswith('@')):
                line = line[1:]
                print(line, end='')
    

    f.close()


            









