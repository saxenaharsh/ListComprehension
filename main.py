num = [1,2,3,4,5]
num_list = []
for item in num:
    item = item + 1
    num_list.append(item)
print(num_list)

## Running the same loop using list comprehension
new_list = [item + 1 for item in num]
print(new_list)