f = open('./train2id.txt', 'r')

b_ratings = {}

_ = f.readline()
line = f.readline()
while line:

    u, b, rating = line.split()

    b = int(b)
    rating = int(rating)
    if rating == 12:
        break

    if b not in b_ratings:
        b_ratings[b] = [0, 0, 0]
    else:
        if 0 <= rating <=3:
            b_ratings[b][0] += 1
        elif 4 <= rating <= 7:
            b_ratings[b][1] += 1
        elif 8 <= rating <= 11:
            b_ratings[b][2] += 1


    line = f.readline()
f.close()

for b_rating in b_ratings.items():
    print(b_rating)