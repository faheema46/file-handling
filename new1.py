new=open("./file.txt","r")
counter=0
content=new.read()
content1=content.split(" ")



for i in content1:
    if i:
        counter+=1

print("The number of lines is:")
print(counter)
