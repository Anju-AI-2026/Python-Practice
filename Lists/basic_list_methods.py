# List Operations Demo Program

# Step 1: Create a list
numbers = [5, 10, 15]

# Step 2: Add an element at the end
numbers.append(20)

# Step 3: Insert 7 at index 1
numbers.insert(1, 7)

# Step 4: Remove a specific value (10)
numbers.remove(10)

# Step 5: Remove last element and store it
popped = numbers.pop()

# Step 6: Add multiple elements at once
numbers.extend([100, 200])

# Step 7: Sort the list in ascending order
numbers.sort()

# Step 8: Reverse the list
numbers.reverse()

# Step 9: Print final list
print("Final list:", numbers)

# Step 10: Print popped value
print("Popped value:", popped)
