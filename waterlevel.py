
water=int(input("enter the no"))
min=1
max=10
if water<min:
    print("more water to be filled")
elif water>min and water<=max:
    print("no need to fill water")
elif water>max:
    print("water will overflow")
else:
    print("none")
