
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


unique_items = (set1 - set2) | (set2 - set1)

print("Unique items from both sets:", unique_items)
