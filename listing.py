def putinlist(rec):
    a=[]
    file=open(rec,"r")
    for line in file:
        a.append(line.split())
    file.close()
    return a
