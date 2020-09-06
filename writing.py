def writefile(l):
    file=open("python.txt","w")
    for row in l:
            file.write('     '.join([str(elem) for elem in row]))
            file.write("\n")
    file.close()        
    return file
