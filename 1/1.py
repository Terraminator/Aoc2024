with open("1.data") as f:
    lines=f.readlines()
l1=[int(l.split("   ")[0]) for l in lines]
l2=[int(l.split("   ")[1]) for l in lines]

def distance(a, b):
    return(abs(b-a))

def main():
    la=sorted(l1)
    lb=sorted(l2)
    lc=zip(la, lb)
    
    print("total distance:", sum([distance(a, b) for a, b in lc]))


if __name__=="__main__":
    main()
