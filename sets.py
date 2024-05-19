
# Practice Task 1: Set Operations
# o Create two sets, set1 and set2, with some arbitrary elements.
# o Print both sets.
# o Add anew element to set1 and print the updated set.
# o Remove an element from set2 and print the updated set.
# o Check if a specific element is present in each set and print the result.
# o Find the union of set1 and set2 and print the result.
# o Find the intersection of set1 and set2 and print the result.
# o Find the difference between set1 and set2 and print the result.
 #Code:
 set1 = {1, 2, 3, 4, 5}
 set2 = {4, 5, 6, 7, 8}
 print("Set1:", set1)
 print("Set2:", set2)
 set1.add(6)
 print("Updated Set1:", set1)
 set2.remove(7)
 print("Updated Set2:", set2)
 num1=10
 if num1 in set1:
 print("Element",num1, "exists in set1")
 else:
 print("Element",num1, "not exists in set1")
 num2=8
 if num2 in set2:
 print("Element",num2, "exists in set2")
 else:
 print("Element",num2, "not exists in set2")
 union_set = set1.union(set2)
 print("Union of Set1 and Set2:", union_set)
 intersection_set = set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)
 difference_set = set1.difference(set2)
 print("Difference between Set1 and Set2:", difference_set)
 #Output:
 #Practice Task 2: Tuple Operations
 #o Create a tuple named tuple1 containing some integer values.
 #o Print the tuple.
 #o Access and print the element at index 2 of the tuple.
 #o Slice the tuple from index 1 to index 4 and print the result.
 #o Find and print the length of the tuple.
 #o Count the number of occurrences of a specific element in the tuple and print the
 #result.
 #o Find the index of a specific element in the tuple and print the result.
 #Code:
 tuple1 = (10, 30, 30, 30, 20, 30, 40, 50, 60)
 print(tuple1)
 #slicing
 print(tuple1[1:4])
 #length of tuple
 print(len(tuple1))
 #count of an element
print(tuple1.count(30))
 #count of index of an element
 print(tuple1.index(30))
 #Output:
 #Practice Task 3: Mixed Operations
 #o Create a set named set3 containing some elements.
 #o Create a tuple named tuple2 containing some elements.
 #o Print both the set and the tuple.
 #o Convert set3 to a tuple named tuple3.
 #o Print the converted tuple.
 #o Convert tuple2 to a set named set4.
 #o Print the converted set.
 #Code:
 set3 = {10, 20, 30, 40, 50}
 tuple2 = (1, 2, 3, 4, 5)
 print("Set3:", set3)
 print("Tuple2:", tuple2)
 tuple3 = tuple(set3)
 print("Converted Tuple3:", tuple3)
 set4 = set(tuple2)
 print("Converted Set4:", set4)
 #Output:
