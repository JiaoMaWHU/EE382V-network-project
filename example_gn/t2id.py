import random
from math import sqrt
from e2id_gn import max_business, max_user

# rate 0-5: 1-11
# friend 12

f = open("train2id.txt", 'w')
count = 0
b_kind = [ [0, 1, 2, 3],[4, 5, 6, 7],  [8, 9, 10, 11]]

for b in range(1, max_business + 1):
    user_num = random.randint(1, max_user)
    random_num = user_num // 3

    for _ in range(random_num):
        user = random.randint(1, max_user)
        f.write("{} {} {}\n".format(user, b, random.randint(1, 11)))
        count += 1

    b_kind_ratings = b_kind[b % 3]
    for _ in range(user_num - random_num):
        user = random.randint(1, max_user)
        f.write("{} {} {}\n".format(user, b, random.choice(b_kind_ratings)))
        count += 1

users = [i for i in range(1, max_user + 1)]
for i in range(int(sqrt(max_user))):
    user1 = random.choice(users)

    users.remove(user1)
    user2 = random.choice(users)
    users.append(user1)

    f.write("{} {} {}\n".format(user1, user2, 12))
    count += 1

f.write(str(count))