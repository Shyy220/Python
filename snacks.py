
box_a = {"apple", "chips", "granola"}
box_b = {"chips", "cookies", "juice"}

box_a.add("pretzel")
print("Box A after adding pretzel:", box_a)

shared_snacks = box_a.intersection(box_b)
print("Shared snacks:", shared_snacks)


snack_counts = [2, 5, 3]
snack_counts.append(4) 
snack_counts.append(5) 
print("Snack counts array:", snack_counts)

count_of_fives = snack_counts.count(5)
print("Number of times 5 appears:", count_of_fives)

snack_counts.reverse()
print("Final reversed snack counts array:", snack_counts)
