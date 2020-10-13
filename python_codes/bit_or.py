
# import itertools as it
# a=99999
# b=100000
# lst=list(range(a,b+1))
# st=list(it.combinations_with_replacement(lst,2))
# res=set()
# for ele in st:
#     res.add(ele[0]|ele[1])
# print(len(res))
a,b= 840847689,876655801
s=set()
def num():
    num = a
    while num<=b:
        yield num
        num += 1
gen1=num()
while True:
    try:
        p=next(gen1)
        gen2=num()
        while True:
            try:
                q=next(gen2)
                s.add(p|q)
            except StopIteration:
                break
    except StopIteration:
        break
print(len(s))
