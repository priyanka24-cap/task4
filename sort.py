name=input("enter the name:")
dictionary={}
for i in name:
    dictionary[i] = name.count(i)
print(dictionary)
print("\n after sorting in descending order:")
print(sorted(dictionary.items(), key=lambda kv:kv[1], reverse=True))


