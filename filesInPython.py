def myList(listItems):
    f=open("demoFile.txt","a")
    f.write("\n"+listItems)
    f.close()

def readFile():
    f=open("demoFile.txt","r")
    print(f.read())


i=0
while i<=1000:
    readFile()

