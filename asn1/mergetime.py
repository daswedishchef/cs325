import time
import sys
import random
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
    times = open("mergetime.out","w")
    #generate random list of numbers
    myline = []
    size = int(sys.argv[1])
    for i in range(0,size):
        myline.append(random.randint(0,10000))
    #run test
    time0 = time.time()
    mylist = mergesort(myline)
    time1 = time.time() - time0
    #print the results to file
    for i in mylist:
        outputfile.write(str(i))
        outputfile.write(" ")
    outputfile.write("\n")
    times.write("Sample size: ")
    times.write(str(size))
    times.write("\nTime: ")
    times.write(str(time1))
    times.write("\n")
    times.close()
    outputfile.close()

if __name__ == '__main__':
    main()