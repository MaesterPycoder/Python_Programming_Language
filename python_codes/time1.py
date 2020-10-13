import time
t=time.localtime()
print(t)
d=t.tm_mday
m=t.tm_mon
y=t.tm_year
day=t.tm_wday
print("week day=%d"%(day))
print("DATE=%d-%d-%d"%(d,m,y))
h=t.tm_hour
mi=t.tm_min
s=t.tm_sec
print("time=%d: %d: %d"%(h,mi,s))
