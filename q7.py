obj = open("newfile.txt","w")
obj.write("This is a new text file. This contains the solution of question number 7 of lab assignment 2")
line=["1","2","3"]
obj.writelines(line)
obj.close()
obj = open("newfile.txt","r")
print(obj.read())
print(obj.readline(3))
obj.close()
