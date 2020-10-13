def brick(a,b):
      return a+b*5
def br(p,i,j,y,x):
      if(j==0):
          j=n
          i-=1
      t=brick(x[i],y[j])
      print(t)
      if(t==p):
          f+=1
          j-=1
      elif(i==1 and j==0):
          if(f>0):
              return True
          else:
              return False
      else:
          j-=1
          br(p)
def make_bricks(m,n,p):
    x=list(range(1,m+1))
    y=list(range(1,n+1))
    i=len(x)
    j=len(y)
    f=0
    br(p,i,j,y,x)
make_bricks(3,1,8)
