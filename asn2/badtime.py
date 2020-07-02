import time
import sys
import random

badsortnum = 0

def badsort(myline,n):
    global badsortnum
    badsortnum += 1
    if len(myline) == 2 and myline[0] > myline[1]:
        temp = myline[0]
        myline[0] = myline[1]
        myline[1] = temp
    elif len(myline) > 2:
        m = n*len(myline)
        #print(str(m))
        #bad1 = badsort(myline[0:int(m-1)],n)
        #bad1.extend(myline[int(m):len(myline)])
        #myline = bad1
        #print(myline)
        #bad2 = myline[0:int(len(myline)-m-1)]
        #bad2.extend(badsort(myline[int(len(myline)-m):len(myline)-1],n))
        #myline = bad2
        #print(myline)
        #bad3 = badsort(myline[0:int(m-1)],n)
        #bad3.extend(myline[int(m):len(myline)])
        #myline = bad3
        badsort(myline[0:int(m-1)],n)
        badsort(myline[int(len(myline)-m):len(myline)-1],n)
        badsort(myline[0:int(m-1)],n)
    return myline

def brutesort(myline):
    maxsum = 0
    for i in range(0,len(myline)):
        mysum = 0
        for j in range(i,len(myline)):
            mysum += myline[j]
            if mysum > maxsum:
                maxsum = mysum
                low = i
                high = j
    high += 1
    return myline[low:high]
    

def main():
    #init files
    global badsortnum
    outputfile = open("badsort.out","w")
    times = open("badtime.out","w")
    #generate random list of numbers
    myline = list()
    size = int(sys.argv[1])
    for i in range(0,size):
        myline.append(random.randint(0,10000))
    #run test
    #print(myline)
    time0 = time.time()
    #mylist = brutesort(myline)
    mylist = badsort(myline,0.66)
    time1 = time.time() - time0
    print(str(badsortnum))
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