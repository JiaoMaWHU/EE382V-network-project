import numpy as np
import random
import os


def inertia(embeddings):
    # using the inertia definition as k-means
    # refer here https://scikit-learn.org/stable/modules/clustering.html
    # 1. find centroid
    centroid = np.sum(embeddings, axis=0) / len(embeddings)
    # 2. compute distance
    dis = 0
    count = 0
    for v in embeddings:
        dis += np.sum(np.square(v - centroid))
        count += 1
    return dis/count


def evaluation(embeddings, sucessful_b_id):
    # according to the "curse of dimensionality" in high dimension
    # we need to do PCA first

    # total
    inertia_v_total = inertia(embeddings)
    print("distance metric of total network: {}".format(inertia_v_total))

    # success
    inertia_v_suc = inertia([embeddings[i] for i in sucessful_b_id])
    print("distance metric of success businesses network: {}".format(inertia_v_suc))

    # random
    ids = [i for i in range(len(embeddings))]
    for i in range(5):
        random.shuffle(ids)
        inertia_v = inertia([embeddings[i] for i in ids[:len(sucessful_b_id)]])
        print("distance metric of random businesses network {}: {}".format(i, inertia_v))


def pre_evaluation(citypath):
    # find successful business in a city
    with open(os.path.join(citypath, 'embedding_id.txt'), 'r') as f:
        lines = f.readlines()
        id_lines = [id.strip() for id in lines]
    with open(os.path.join(citypath, 's_ent_emb.tsv'), 'r') as f:
        lines = f.readlines()
        embeddings = []
        for line in lines:
            if line == '\n':
                continue
            res = line.strip().split()
            embeddings.append([float(num) for num in res])
    with open(os.path.join(citypath, 'success_id.txt'), 'r') as f:
        success_id = []
        lines = f.readlines()
        for line in lines:
            success_id.append(id_lines.index(line.strip().split()[0]))
    evaluation(embeddings, success_id)


if __name__ == "__main__":
    pre_evaluation("./cities/folder")
