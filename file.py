
f=open("filehandling.txt","+a")
f.write("hello")
f.close()
f=open("filehandling.txt","r")
print(f.read())
f.close()