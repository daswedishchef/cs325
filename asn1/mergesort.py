def mergesort(mylist):
    if len(mylist) >= 2:
        M = len(mylist) / 2
        L = mylist[:M]
        R = mylist[M:]
        mergesort(L)
        mergesort(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                mylist[k] = L[i]
                i += 1
            else:
                mylist[k] = R[j]
                j += 1
            k += 1
        for l1 in range(i,len(L)):
            mylist[k] = L[l1]
            k += 1
        for r1 in range(j,len(R)):
            mylist[k] = R[r1]
            k += 1
    return mylist



def main():
    #init files
    outputfile = open("merge.out","w")
    myfile = open("data.txt","r")
    fileline = myfile.readlines()
    #read each line
    for line in fileline:
        mylist = line.split()
        mylist.pop(0)
        #sort it
        mylist = mergesort(mylist)
        #print it
        for i in mylist:
            outputfile.write(i)
            outputfile.write(" ")
        outputfile.write("\n")
    myfile.close()
    outputfile.close()

if __name__ == '__main__':
    main()