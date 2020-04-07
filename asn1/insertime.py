import time
import sys
import random
def insertsort(mylist,outputfile):
    time0 = time.time()
    for i in range(1,len(mylist)):
        temp = mylist[i]
        itemp = i-1
        while itemp>=0 and mylist[itemp]>temp:
            mylist[itemp+1] = mylist[itemp]
            itemp -= 1
        mylist[itemp+1] = temp
    extime = time.time()-time0
    for i in mylist:
        outputfile.write(str(i))
        outputfile.write(" ")
    outputfile.write("\n")
    return extime

def main():
    #init time and files
    time1 = time.time()
    times = open("insertime.out","w")
    outputfile = open("insert.out","w")
    #generate random list of numbers
    fileline = []
    size = int(sys.argv[1])
    for i in range(0,size):
        fileline.append(random.randint(0,10000))
    #print the results
    times.write("Sample size: ")
    times.write(str(size))
    times.write("\nTime: ")
    extime = insertsort(fileline,outputfile)
    times.write(str(extime))
    times.write("\n")
    outputfile.close()
    times.close()


if __name__ == "__main__":
    main()