def insertsort(mylist,outputfile):
    mylist.pop(0)
    for i in range(1,len(mylist)):
        temp = mylist[i]
        itemp = i-1
        while itemp>=0 and mylist[itemp]>temp:
            mylist[itemp+1] = mylist[itemp]
            itemp -= 1
        mylist[itemp+1] = temp
    #print sorted list to file
    for i in mylist:
        outputfile.write(i)
        outputfile.write(" ")
    outputfile.write("\n")

def main():
    #init files
    outputfile = open("insert.out","w")
    myfile = open("data.txt","r")
    fileline = myfile.readlines()
    #read each line
    for line in fileline:
        #split and sort it
        mylist = line.split()
        insertsort(mylist,outputfile)
    myfile.close()
    outputfile.close()

if __name__ == "__main__":
    main()