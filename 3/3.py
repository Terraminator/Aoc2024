import re


with open("3.data", "r") as f:
    mem=f.read().replace("\n", "")


def main():
    pat=re.compile(r"mul\((\d+),(\d+)\)")
    terms=re.findall(pat, mem)
    print("sum of multiplications:", sum([int(a)*int(b) for a, b in terms]))



if __name__=="__main__":
    main()
