al=list(str(x) for x in input().split(" "))
min_base=float("infinity")
for a in al:
    sa=list(a)
    lst=['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A','9','8','7','6','5','4','3','2','1','0']              
    base=36
    for i in lst:
        if i in sa:
            ma=int(a,base)
            break
        base-=1
    if min_base>ma:
        min_base=ma
print(min_base)
    

        
        
