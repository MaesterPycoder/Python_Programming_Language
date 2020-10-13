def make_bricks(small, big, goal):
  c=1
  if((small*1+big*5)==goal and c==1):
    c=0
    print("True")
    return True
  elif(small*1==goal and c==1):
    c=0
    print("True")
    return True
  if(big*5==goal and c==1):
    c=0
    print("True")
    return True
  else:
      print("False")
      return False
make_bricks(3,1,9)
make_bricks(3,1,8)
make_bricks(3,2,10)
