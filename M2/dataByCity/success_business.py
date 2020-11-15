import os
import statistics
import numpy as np

def listdirs(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]


def generate_success_business(citypath):
    for city in listdirs(citypath):
        b2rate_sum = {}
        b2rate_count = {}
        dir = os.path.join(citypath, city)
        fname = os.path.join(dir, 'train2id.txt')
        with open(fname, 'r') as f:
            line = f.readline()
            for i in range(int(line)):
                line = f.readline()
                res = line.strip().split()
                bs = res[1]
                rate = int(res[2])
                if rate <= 5:
                    if bs not in b2rate_sum:
                        b2rate_sum[bs] = 0
                        b2rate_count[bs] = 0
                    b2rate_sum[bs] += rate
                    b2rate_count[bs] += 1

        # print("mean: {}\tmedian: {}\tstdev: {}".format(statistics.mean(rates), statistics.median(rates),
        #                                                statistics.stdev(rates)))
        # print("0.2 quantile of arr : ", np.quantile(rates, .20))
        # print("0.4 quantile of arr : ", np.quantile(rates, .40))
        # print("0.6 quantile of arr : ", np.quantile(rates, .60))
        # print("0.8 quantile of arr : ", np.quantile(rates, .80))
        # print("1.0 quantile of arr : ", np.quantile(rates, .99))
        # print("{} in 100000 scores are negative values".format(sum(1 for i in rates if i < 0)))

        rates = list(b2rate_count.values())
        mean = statistics.mean(rates)
        for bs in b2rate_sum:
            b2rate_sum[bs] = b2rate_sum[bs] / b2rate_count[bs]
            if b2rate_count[bs] < mean:
                b2rate_sum[bs] = 0
        sorted_list = sorted(b2rate_sum.items(), key=lambda kv: kv[1], reverse=True)
        size = int(len(sorted_list) * 0.2)
        with open(os.path.join(dir, 'success_id.txt'), 'w') as succ:
            count = 0
            while count < size:
                if sorted_list[count][1] < 4:
                    break
                succ.write('{} {}\n'.format(sorted_list[count][0], sorted_list[count][1]))
                count += 1
        print('{} city size of top 20% businesses is: {}'.format(city, count))


if __name__ == '__main__':
    generate_success_business('./cities')
