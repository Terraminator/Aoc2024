with open("2.data") as f:
    lines=f.readlines()
reports=[l.split(" ") for l in lines]


def is_safe(report):
    report=list(map(int, report))
    if sum([report[i]<report[i+1] for i in range(len(report)-1)])==len(report)-1 or sum([report[i]>report[i+1] for i in range(len(report)-1)])==len(report)-1:
        if sum([1<=abs(report[i+1]-report[i])<=3 for i in range(len(report)-1)])==len(report)-1:
            return(1)
    return(0)
    

def main():
    print(sum(map(is_safe, reports)), "reports are safe!")

if __name__=="__main__":
    main()
