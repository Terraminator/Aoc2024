import re


with open("3.data", "r") as f:
    mem2=f.read().replace("\n", "")


def main(mem2):
    npat=re.compile(r"don't\(\).*?do\(\)")
    npat2=re.compile(r"don't\(\).*")
    mem=re.sub(npat, "", mem2)
    mem2=re.sub(npat2, "", mem)
    mem=mem2
    print(mem)
    pat=re.compile(r"mul\((\d+),(\d+)\)")
    terms=re.findall(pat, mem)
    print("sum of multiplications:", sum([int(a)*int(b) for a, b in terms]))



if __name__=="__main__":
    main(mem2)
