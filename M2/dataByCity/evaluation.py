import numpy as np
import random

def inertia(embeddings):
    # using the inertia definition as k-means
    # refer here https://scikit-learn.org/stable/modules/clustering.html
    # 1. find centroid
    centroid = np.sum(embeddings, axis=0)/len(embeddings)
    # 2. compute distance
    dis = 0
    for v in embeddings:
        dis += np.sum(np.square(v - centroid))
    return dis

def evaluation(embeddings, sucessful_b_id):
    # according to the "curse of dimensionality" in high dimension
    # we need to do PCA first
    pca_embeddings = pca(embeddings)

    # total
    inertia_v_total = inertia(pca_embeddings)
    print("distance metric of total network: {}".format(inertia_v_total))

    # success
    inertia_v_suc = inertia([pca_embeddings[i] for i in sucessful_b_id])
    print("distance metric of success businesses network: {}".format(inertia_v_suc))

    # random
    ids = range(len(embeddings))
    for i in range(5):
        ids = random.shuffle(ids)
        inertia_v = inertia([pca_embeddings[i] for i in ids[:len(sucessful_b_id)]])
        print("distance metric of random businesses network {}: {}".format(i, inertia_v))


def pca(embeddings):
    pass

def pre_evaluation(city):
    # find successful business in a city
    pass

if __name__ == "__main__":
    pre_evaluation("test")