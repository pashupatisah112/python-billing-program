from reading import readfile
ans="y"
while ans=="y":
    print(readfile("python.txt"))
    from listing import putinlist
    l=putinlist("python.txt")
    import datetime
    dateandtime=datetime.datetime.now()
    z=1
    p=[]
    x=1
    num1=0
    num2=0
    num3=0
    mp1=0
    mp2=0
    mp3=0
    d1=0
    d2=0
    d3=0
    t1=0
    t2=0
    t3=0
    name=input("enter customer name:")
    ask="y"
    while ask=="y":
        product=input("enter product name:")
        success=False
        while success==False:
            try:
                n=int(input("number of items:"))
                p.append(product)
                s=" ".join(p)
                if product=="iphone":
                   num1=n
                   mp1=int(l[1][1])
                   d1=(5/100)*mp1*num1
                   t1=(num1*mp1)-d1
                   l[1][2]=int(l[1][2])-n
                elif product=="laptop":
                   num2=n
                   mp2=int(l[2][1])
                   d2=(5/100)*mp2*num2
                   t2=(num2*mp2)-d2
                   l[2][2]=int(l[2][2])-n
                elif product=="camera":
                   num3=n
                   mp3=int(l[3][1])
                   d3=(5/100)*mp3*num3
                   t3=(num3*mp3)-d3
                   l[3][2]=int(l[3][2])-n
                else:
                   print("product not availiable")
                success=True
            except:
                print("invalid value for number")
        ask=input("buy another product?y/n:")
        z=z+1
    file=open("invoice.txt","w")
    file.write("BIJULI ELECTRONICS KTM NEPAL")
    file.write("\n")
    file.write("INVOICE b100"+str(z))
    file.write("\n")
    file.write("date and time"+str(dateandtime))
    file.write("\n")
    file.write("------------------------------------------")
    file.write("\n")
    file.write("customer Name:"+name)
    file.write("\n")
    file.write("product:"+s)
    file.write("\n")
    file.write("number of items:"+str(num1+num2+num3))
    file.write("\n")
    file.write("gross amount"+str((num1*mp1)+(num2*mp2)+(num3*mp3)))
    file.write("\n")
    file.write("discount:"+str(d1+d2+d3))
    file.write("\n")
    file.write("net amount:"+str(t1+t2+t3))
    file.write("\n")
    file.write("------------------------------------------")
    file.write("\n")
    file.write("THANK YOU...PLEASE VISIT AGAIN")
    file.close()
    ans=input("continue?y/n:")
    from writing import writefile
    
    
    
    
