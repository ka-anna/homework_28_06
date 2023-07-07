#Implement filter function

# price = [47, 56, 10, 45, 115, 17, 7, 89]
# min_p = filter(lambda i: i >20, price)
# print (list(min_p))


price = [47, 56, 10, 45, 115, 17, 7, 89]
min_p = []
for i in range(len(price)):
    if price[i] > 20:
        min_p.append(price[i])
print(min_p)
