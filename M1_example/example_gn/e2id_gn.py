f = open("entity2id.txt", 'w')

user = 1
business = 1
max_user = 100
max_business = 9

for i in range(user, max_user + 1):
    f.write("user{} {}\n".format(i, i))

for i in range(business, max_business + 1):
    f.write("b{} {}\n".format(i, max_user + i))

f.write(str(max_user + max_business))