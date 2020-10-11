r2id = open("relation2id.txt", 'w')

id = 1
rate = 0
count = 0

for i in range(0, 5 * 2 + 1):
    r2id.write("rate{} {}\n".format(rate, id))
    count += 1
    rate += 0.5
    id += 1

r2id.write("friend {}\n".format(id))
r2id.write(str(count))