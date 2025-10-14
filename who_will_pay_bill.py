import random

friend = ["p", "a", "s", "k"]

#option 1

# random_num = random.randint(0,3)
# if random_num == 0:
#     print(friend[0])
# elif random_num == 1:
#     print(friend[1])
# elif random_num == 2:
#     print(friend[2])
# else:
#     print(friend[3])

#option 2

# print(random.choice(friend))


#option 3

random_index = random.randint(0,3)
print(friend[random_index])


