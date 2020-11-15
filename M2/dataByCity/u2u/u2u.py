from textblob import TextBlob
import json
import statistics
import numpy as np
import time

reviews_file = "../../../yelp_dataset/yelp_academic_dataset_review.json"


def build_u2u(city_file, output):
    start = time.time()
    city_b_u = {}
    user_id_set = set()
    with open(city_file, 'r') as cf:
        line = cf.readline()
        for i in range(int(line)):
            line = cf.readline()
            res = line.strip().split()
            bs = res[1]
            user = res[0]
            if bs not in city_b_u:
                city_b_u[bs] = []
            city_b_u[bs].append(user)
            user_id_set.add(user)

    print("Started...")

    b_md5_id = {}
    b_md5_set = set()
    with open('bs_entity2id.txt', 'r') as bs_e2i:
        line = bs_e2i.readline()
        for i in range(int(line)):
            line = bs_e2i.readline()
            res = line.strip().split()
            if res[1] in city_b_u:
                b_md5_id[res[0]] = res[1]
                b_md5_set.add(res[0])

    u_md5_id = {}
    with open('user_entity2id.txt', 'r') as ur_e2i:
        line = ur_e2i.readline()
        for i in range(int(line)):
            line = ur_e2i.readline()
            res = line.strip().split()
            if res[1] in user_id_set:
                u_md5_id[res[0]] = res[1]

    b_u_polarity_map = {}
    with open(reviews_file, 'r', encoding='utf-8') as reviews:
        line = reviews.readline()
        while line:
            review = json.loads(line)
            if review['business_id'] in b_md5_set:
                b_id = b_md5_id[review['business_id']]
                u_id = u_md5_id[review['user_id']]
                if not b_id or not u_id:
                    raise ValueError("id not found")
                if b_id not in b_u_polarity_map:
                    b_u_polarity_map[b_id] = {}
                if not b_u_polarity_map[b_id][u_id]:
                    b_u_polarity_map[b_id][u_id] = TextBlob(review['text']).sentiment.polarity
            line = reviews.readline()

    print("finish metadata processing, start generation")

    count = 0
    c1 = 0
    c2 = 0
    c3 = 0
    with open(output, 'w') as u2uf:
        for b_id in city_b_u:
            u_list = city_b_u[b_id]
            for i in range(len(u_list)):
                for j in range(i + 1, len(u_list)):
                    sp1 = b_u_polarity_map[b_id][u_list[i]]
                    sp2 = b_u_polarity_map[b_id][u_list[j]]
                    if not sp1 or not sp2:
                        print(u_list[i] + " " + u_list[j])
                        raise ValueError('no such review')
                    if sp1 * sp2 < 0:
                        u2uf.write("{} {} {}\n".format(
                            u_list[i],
                            u_list[j],
                            7
                        ))  # negative correlation
                        count += 1
                        c3 += 1
                    elif abs(sp1 - sp2) < 0.1:
                        u2uf.write("{} {} {}\n".format(
                            u_list[i],
                            u_list[j],
                            6
                        ))  # positive correlation
                        count += 1
                        c2 += 1

    end = time.time()
    print("finish generation, {} relations are actually generated".format(count))
    print("irrelevant: {}, positive: {}, negative: {}".format(c1, c2, c3))
    print("time elapsed: {} mins".format((end - start) / 60))

    with open(output, "r+") as f:
        s = f.read()
        f.seek(0)
        f.write("{}\n".format(count) + s)


def sentence_similarity(s1, s2):
    stdev = 0.24
    sp1 = TextBlob(s1).sentiment.polarity
    sp2 = TextBlob(s2).sentiment.polarity
    if sp1 * sp2 < 0:
        return 7  # negative correlation
    dis = abs(sp1 - sp2)
    if dis < 0.1:
        return 6  # positive correlation
    return 8  # irrelevant


def analysis_reviews():
    count = 0
    with open(reviews_file, 'r', encoding='utf-8') as reviews:
        scores = []
        for i in range(100000):
            line = reviews.readline()
        while line:
            review = json.loads(line)
            scores.append(TextBlob(review["text"]).sentiment.polarity)
            line = reviews.readline()
            if count % 1000 == 0:
                print("Loading: {}%".format(count / 1000 + 1))
            count += 1
            if count == 100000:
                break
    print("list size: {}".format(len(scores)))
    print("mean: {}\tmedian: {}\tstdev: {}".format(statistics.mean(scores), statistics.median(scores),
                                                   statistics.stdev(scores)))
    print("0.2 quantile of arr : ", np.quantile(scores, .20))
    print("0.4 quantile of arr : ", np.quantile(scores, .40))
    print("0.6 quantile of arr : ", np.quantile(scores, .60))
    print("0.8 quantile of arr : ", np.quantile(scores, .80))
    print("1.0 quantile of arr : ", np.quantile(scores, .99))
    print("{} in 100000 scores are negative values".format(sum(1 for i in scores if i < 0)))

    # top 100000
    # mean: 0.24501029707124072	median: 0.24956140350877196	stdev: 0.23427056365322568
    # 0.2 quantile of arr :  0.07099911816578487
    # 0.4 quantile of arr :  0.19861111111111115
    # 0.6 quantile of arr :  0.3
    # 0.8 quantile of arr :  0.42291666666666666
    # 1.0 quantile of arr :  0.8125
    # 12152 in 100000 scores are negative values

    # 100001 200000
    # mean: 0.2436863189904404	median: 0.24791666666666667	stdev: 0.23510115586492283
    # 0.2 quantile of arr :  0.06760398860398864
    # 0.4 quantile of arr :  0.1972358276643993
    # 0.6 quantile of arr :  0.2995641148325358
    # 0.8 quantile of arr :  0.42333333333333334
    # 1.0 quantile of arr :  0.82
    # 12406 in 100000 scores are negative values


def generate_u2u(folder):
    pass


if __name__ == "__main__":
    build_u2u('../cities/cleveland/train2id.txt', "../cities/cleveland/userrelations.txt")
    # print(sentence_similarity("this restaurant is good", "love this place"))
