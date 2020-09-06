def readfile(rec):
    file=open(rec,"r")
    stock=file.read()
    file.close()
    return stock
