file1=open("demo.txt","w")
file1.write("this is assignment 6 .this project is to open ,read write a file. ")
file1.close()


file2=open("demo.txt","r")
a=file2.read()
print(a)
file2.close

file3=open("demo.txt","a")
file3.write("\n this topic name is file handling")
file3.close()