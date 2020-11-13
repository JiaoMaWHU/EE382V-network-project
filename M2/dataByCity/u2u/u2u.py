from textblob import TextBlob
import json
import statistics
import numpy as np

file = "../../../yelp_dataset/yelp_academic_dataset_review.json"


def sentence_similarity(s1, s2):
    stdev = 0.24
    sp1 = TextBlob(s1).sentiment.polarity
    sp2 = TextBlob(s2).sentiment.polarity
    print("sp1: {}, sp2: {}".format(sp1, sp2))
    if sp1 * sp2 < 0:
        return 8  # negative correlation
    dis = abs(sp1 - sp2)
    if dis < stdev:
        return 7  # positive correlation
    return 6  # irrelevant


def analysis_reviews():
    count = 0
    with open(file, 'r', encoding='utf-8') as reviews:
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
    print(sentence_similarity("this restaurant is good", "love this place"))
