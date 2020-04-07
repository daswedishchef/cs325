def insertsort(mylist,outputfile):
    mylist.pop(0)
    for i in range(1,len(mylist)):
        temp = mylist[i]
        itemp = i-1
        while itemp>=0 and mylist[itemp]>temp:
            mylist[itemp+1] = mylist[itemp]
            itemp -= 1
        mylist[itemp+1] = temp
    for i in mylist:
        outputfile.write(i)
        outputfile.write(" ")
    outputfile.write("\n")

def main():
    outputfile = open("insert.out","w")
    myfile = open("data.txt","r")
    fileline = myfile.readlines()
    for line in fileline:
        mylist = line.split()
        insertsort(mylist,outputfile)
    myfile.close()
    outputfile.close()

if __name__ == "__main__":
    main()