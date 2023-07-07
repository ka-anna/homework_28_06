#Implement enumerate function

# x = ['a', 'b', 'c']
# z = dict(enumerate(x,97))
# print(z)



x = ['a', 'b', 'c']
y = 97
res = []
for i in range(len(x)):
    t = (y,x[i]) 
    res.append(t)
print(res)
    
