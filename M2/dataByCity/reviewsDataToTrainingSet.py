import json
import time

start = time.time()

fo = open("D:\yelp_dataset\yelp_academic_dataset_review.json",  encoding='utf-8')

f_entity = open("./entity2id.txt", 'w', encoding='utf-8')
f_train_raw = open("./raw_train2id.txt", 'w', encoding='utf-8')

ucount = 0
bcount = 0

umap = {}
bmap = {}

count = 0
line = fo.readline()

while line:

    review = json.loads(line)

    # print(review)
    count += 1
    us = review["user_id"]
    uid = 0
    if us not in umap:
        umap[us] = ucount
        uid = ucount
        ucount += 1
    else:
        uid = umap[us]

    bs = review["business_id"]
    bid = 0
    if bs not in bmap:
        bmap[bs] = bcount
        bid = bcount
        bcount += 1
    else:
        bid = bmap[bs]

    stars = review["stars"]
    rid = int(stars)

    f_train_raw.write("{} {} {}\n".format(uid, bid, rid))

    line = fo.readline()

    if count % 100 == 0:
        # break
        print("write {} lines".format(count))

uids = sorted(umap.items(), key=lambda x: x[1])
bids = sorted(bmap.items(), key=lambda x: x[1])

lines = len(uids) + len(bids)

f_entity.write("{}\n".format(lines))

for k, v in uids:
    f_entity.write("{} {}\n".format(k, v))

for k, v in bids:
    f_entity.write("{} {}\n".format(k, v))

fo.close()
f_train_raw.close()

# add total line count to first line
f_train_raw = open("./raw_train2id.txt", 'r', encoding='utf-8')
f_train= open("./train2id.txt", 'w', encoding='utf-8')

f_train.write("{}\n".format(count))

line = f_train_raw.readline()

while line:

    f_train.write(line)
    line = f_train_raw.readline()

f_train.close()
f_train_raw.close()

end = time.time()

print("relation total lines: {}".format(count))
print("time cost: {}min".format((end - start) / 60))