#Implement zip function

# x = [1,2,3,4]
# y = [11,12,13]

# z = list(zip(x,y))
# print(z)


x = [1,2,3,4]
y = [11,12,13]
res = []
for i in range (len(x)-1):
    t1 = (x[i], y[i])
    res.append(t1)
print(res)
