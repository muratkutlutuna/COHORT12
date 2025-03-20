names = ['Alice','Andrew','Robert','Bruce']
years = [1998, 2000, 1998, 1987]

# 1- Add the name "Hans" to the end of the list.
names.append('Hans')
print(names)
#2 - Add the value "Zeynep" to the beginning of the list.
names.insert(0,'Zeynep')
print(names)
# 3- Delete the name "Bruce" from the list.
del names[3]
print(names)
# 4- What is the index of the name "Bruce"?
print("""Bruce is at index {}""".format(names.index('Bruce')) ) #print(names.index('Bruce')) #names.index('Bruce')

# 5- Is "Alice" an element of the list?
print("Alice is an element of the list: {}".format('Alice' in names))
print("Alice is an element of the list: {}".format(names.count('Alice')>0))

#6- Invert the list elements.
print(names[::-1])
print(names)
names.reverse()
print(names)
# 8- Sort the list of years by numerical size.
years.sort()
print(years)
# 9- Convert str = "Ford,Tesla" string to list.
str = "Ford,Tesla"
print([str])
print(str.split(','))

# 10- What is the largest and smallest element of the years list?
years.sort()
print(years[0],years[-1])
# 11- How many 1998 values are there in the years list?
print(years.count(1998))

# 12- Delete all elements of years list.
years.clear()
print(years)
# 13- store 3 brand names in a list, receive brand names from the user.
brand_names = []
for i in range(3):
    brand_names.append(input("Enter a brand name: "))
print(brand_names)
