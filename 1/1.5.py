with open("1.data") as f:
    lines=f.readlines()
l1=[int(l.split("   ")[0]) for l in lines]
l2=[int(l.split("   ")[1]) for l in lines]

def sim_num(num, l2):
    return(num*l2.count(num))

def main():
    sim_score=sum([sim_num(num, l2) for num in l1])
    print("similarity_score:", sim_score)


if __name__=="__main__":
    main()
