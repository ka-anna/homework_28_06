#Implement map function

# price = [47, 56, 10, 45, 115, 17, 7, 89]
# min_p = map(lambda i: i >20, price)
# print (list(min_p))

price = [47, 56, 10, 45, 115, 17, 7, 89]
for i in range(len(price)):
    price[i] *=2
print(price)
