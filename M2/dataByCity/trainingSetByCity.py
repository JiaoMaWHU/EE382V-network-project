import json
import time
import os
import shutil

start = time.time()

fo = open("D:\yelp_dataset\yelp_academic_dataset_business.json", encoding='utf-8')

f_b = open("bs_entity2id.txt")

line = fo.readline()

city2ids = {}
citynum = 0
_bcount = 0

while line:

    bs = json.loads(line)

    city = bs["city"].strip()
    id = bs["business_id"]

    if city not in city2ids:
        city2ids[city] = [id]
    else:
        city2ids[city].append(id)

    line = fo.readline()
    _bcount += 1

fo.close()

print("city num: " + str(len(city2ids.items())))
print("business num: {}".format(_bcount))

fcitynum = open("citynum.txt", "w", encoding="utf-8")

if not os.path.exists("./city"):
    os.mkdir("./city")

for city, ids in city2ids.items():
    if city == "":
        continue

    bcount = len(ids)
    ucount = 1968703

    enums = []

    dir = "./city/" + city

    if not os.path.exists(dir):
        os.mkdir(dir)

    f = open(dir + "/entity2id.txt", "w", encoding="utf-8")

    f.write("{}\n".format(bcount + ucount))

    # write user entity
    fu = open("user_entity2id.txt")

    fu.readline()
    l = fu.readline()
    while l:
        f.write(l)
        l = fu.readline()

    fu.close()
    # finish user data

    print("generate entity data for {}".format(city))

    for id in ids:
        found = False

        fe = open("bs_entity2id.txt")
        fe.readline()

        line = fe.readline().strip()
        while line:
            eid, enum = line.split(" ")

            if id == eid:
                enums.append(enum)
                f.write(line)
                found = True
                break

            line = fe.readline().strip()

        if not found:
            print("business {} not found!".format(id))

        fe.close()  # should close in proper posision
    f.close()

    print("finish city: {}".format(city))
    print("ids: {}".format(ids))
    fcitynum.write("{} {}\n".format(city, len(ids)))

    # generate train data by city
    print("generate train data for {}".format(city))

    ft = open("train2id.txt")
    ftrain = open(dir + "/train2id.txt", "w", encoding="utf-8")

    trains = []

    ft.readline()
    ll = ft.readline().strip()
    while ll:
        uid, bid, rid = ll.split()

        for enum in enums:
            if enum == bid:
                trains.append(ll)

        ll = ft.readline().strip()


    ft.close()

    ftrain.write("{}\n".format(len(trains)))
    for t in trains:
        ftrain.write(t + "\n")

    ftrain.close()

    shutil.copy("relation2id.txt", dir + "/relation2id.txt")

fcitynum.close()

end = time.time()

print("time cost: {}min".format((end - start) / 60))
