def swap(t1,t2):
    t1,t2=t2,t1
    return t1,t2
tuple1=(1,2,3)
tuple2=(4,5,6)
print("original tuple1",tuple1)
print("original tuple2",tuple2)
tuple1,tuple2=swap(tuple1,tuple2)
print("edited tuple1",tuple1)
print("edited tuple2",tuple2)