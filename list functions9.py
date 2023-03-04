fruits=["apple","apple", "bananas","jack fruit","papaya","lemon"]
vegetables=["tomatoes","potatoes","brinjals","cucumbers"]
fruits.extend(vegetables)#extend fn is used to add 2 lists together
print(fruits)
vegetables.append("drumstick")#appending an individual element
print(vegetables)
vegetables.insert(2,"onions")
print(vegetables)
vegetables.remove("potatoes")
print(vegetables)
vegetables.pop()#last element gets popped out
print(vegetables)
vegetables.clear()
print(vegetables)
print(fruits.index("potatoes"))#to find whether that value is there in that list
print(fruits.count("apple"))#to count how many such repetitions are there
fruits.sort()#sorts according to alphabetical order
print(fruits)
fruits.reverse()
print(fruits)
navya=fruits.copy()
print(navya)
