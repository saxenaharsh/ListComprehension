num = [1,2,3,4,5]
num_list = []
for item in num:
    item = item + 1
    num_list.append(item)
print(num_list)

## Running the same loop using list comprehension
new_list = [item + 1 for item in num]
print(new_list)

## list comprehension with condition
names = ["Kaju", "Tim", "Johnny", "Jill", "Jack", "Danny", "Jonathan"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)

long_names = [name.lower() for name in names if len(name) > 4]
print(long_names)
