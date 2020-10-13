def move_tower(N,from_tower,to_tower,with_tower):
    if(N>=1):
        move_tower(N-1,from_tower,with_tower,to_tower)
        move_disk(N-1,from_tower,to_tower)
        move_tower(N-1,with_tower,to_tower,from_tower)
def move_disk(p,from_tower,to_tower):
    print("Moving Disk ",p+1," from",from_tower," to ",to_tower)
n=int(input("No. of Disks:"))
move_tower(n,"Source","Destination","Auxilary")
