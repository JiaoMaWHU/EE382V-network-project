import os
import random
import numpy as np


def rank(embeddings, sucessful_b_id):
    centroid = np.sum(embeddings, axis=0) / len(embeddings)

    # sample a business network with the same size as the successful network, then join
    all_ids = set()
    for id in sucessful_b_id:
        all_ids.add(id)
    for i in range(len(sucessful_b_id)):
        while True:
            new_id = random.randint(0, len(embeddings)-1)
            if new_id not in all_ids:
                all_ids.add(new_id)
                break
    ranks = {}
    for i in all_ids:
        ranks[i] = np.sum(np.square(embeddings[i] - centroid))
    sorted_list = sorted(ranks.items(), key=lambda kv: kv[1])
    count = 0
    for i in range(int(len(all_ids)/2)):
        if sorted_list[i][0] in sucessful_b_id:
            count += 1
    print('size of success businesses: {}, total sample size: {}, recall rate = {}/{} = {}'.format(
        len(sucessful_b_id), len(sorted_list), count, len(sucessful_b_id), count/len(sucessful_b_id)
    ))

def recall(citypath):
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
    rank(embeddings, success_id)

if __name__ == '__main__':
    recall("./cities/folder")
