
def cleanFiles(currentMem, exMem):
    with open(currentMem,'r+') as writefile:
        with open(exMem,'a+') as appendfile:

            writefile.seek(0)
            members=writefile.readlines()
            
            header=members[0]
            members.pop(0)
            

            inactive = [member for member in members if ('no' in member)]

           

            writefile.seek(0) # move 0 bytes from beginning.
            writefile.write(header)
            for member in members:
                if (member in inactive):
                    appendfile.write(member)
                else:
                    writefile.write(member)
            writefile.truncate()
        

# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())