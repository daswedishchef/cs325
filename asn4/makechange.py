def change(mylist,outputfile):
    #setting things up and printing initial stuff
    c = int(mylist[0])
    k = int(mylist[1])
    n = int(mylist[2])
    outputfile.write("Data input: c = " + str(c) + ", k = " + str(k) + ", n = " + str(n) + "\n")
    coins = []
    quant = []
    #generating coin denominations
    for i in range(0,k+1):
        coins.append(c**i)
        quant.append(0)
    coins.reverse()
    #actual algorithm
    for j in range(0,k+1):
        while n >= coins[j]:
            n -= coins[j]
            quant[j] += 1
    #printing results
    for k in range(0,k+1):
        outputfile.write("Denomination: " + str(coins[k]) + " Quantity: " + str(quant[k]) + "\n")
    outputfile.write("\n")


def main():
    #init files
    outputfile = open("change.txt","w")
    myfile = open("data.txt","r")
    fileline = myfile.readlines()
    myfile.close()
    #read each line
    for line in fileline:
        mylist = line.split()
        #make it
        change(mylist,outputfile)
    outputfile.close()

if __name__ == '__main__':
    main()