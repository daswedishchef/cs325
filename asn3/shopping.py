import sys
import random

def optimize(F,P, outputfile):
    P.sort(key=lambda x:x[0])
    P.reverse()
    cart = []
    outputfile.write("Member Items\n")
    index = 0
    total = 0
    for person in F:
        ptemp = int(person[0])
        index += 1
        for product in range(0,len(P)):
            #print ptemp
            if(int(ptemp)>int(P[product][1])):
                ptemp -= int(P[product][1])
                total += int(P[product][0])
                cart.append(P[product][2])
        outputfile.write(str(index))
        outputfile.write(": ")
        for i in cart:
            outputfile.write(str(i+1))
            outputfile.write(" ")
        outputfile.write("\n")
        cart = []
    outputfile.write("Total cost: ")
    outputfile.write(str(total))
    outputfile.write("\n")
    
        
                
        
        


def main():
    myfile = open("shopping.txt","r")
    outputfile = open("results.txt","w")
    fileline = myfile.readlines()
    index = 0
    P = []
    F = []
    t = int(fileline[index])
    index += 1
    for i in range(0,t):
        outputfile.write("Test case: ")
        outputfile.write(str(i+1))
        outputfile.write("\n")
        prods = int(fileline[index])
        index += 1
        for j in range(0,prods):
            P.append(fileline[index].split())
            index += 1
        pers = int(fileline[index])
        index += 1
        for k in range(0,pers):
            F.append(fileline[index].split())
            index += 1
        for c in range(0,len(P)):
            P[c].append(c)
        optimize(F,P,outputfile)
        F = []
        P = []
    myfile.close()
    outputfile.close()


if __name__ == '__main__':
    main()