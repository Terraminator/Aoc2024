with open("2.data") as f:
    lines=f.readlines()
reports=[l.split(" ") for l in lines]


def is_safe(report):
    report = list(map(int, report))
    
    def check_safety(r):
        return (all(r[i] < r[i + 1] for i in range(len(r) - 1)) or 
                all(r[i] > r[i + 1] for i in range(len(r) - 1))) and \
               all(1 <= abs(r[i + 1] - r[i]) <= 3 for i in range(len(r) - 1))
    
    if check_safety(report):
        return 1
    
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if check_safety(modified_report):
            return 1
    
    return 0

def main():
    print(sum(map(is_safe, reports)), "reports are safe!")

if __name__=="__main__":
    main()
