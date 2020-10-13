import itertools
def combinations(s,mn_st):
    lst=[]
    for i in range(1,len(s)+1):
        lst+=list(set(list(itertools.combinations(s,i))))
    lst1=list(map(list,lst))
    lst2=[]
    for i in lst1:
        lst2.append("".join(i))
    for i in lst2:
        if i not in mn_st:
            lst2.remove(i)
    return lst2
def countSubstrings(s, queries):
    for ar in queries:
        l,r=ar
        lst=combinations(s[l:r+1],s)
        print(len(lst))



if __name__ == '__main__':
    n = 100
    q = 10
    s = "ccccccccccgdgddgdgddgddgdgddgdgddgddgdgddgddgdgddgdgddgddgdgddwbwbbwbwbbwbbwbwbbwbkgkggwyomdjdbevunm"
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input("Enter:").rstrip().split())))
    countSubstrings(s, queries)
