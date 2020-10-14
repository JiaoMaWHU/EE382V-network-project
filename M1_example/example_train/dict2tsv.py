import pickle
import csv

with open('C:\\Users\\chen\\Desktop\\s_emb.pkl', 'rb') as f:
    emb = pickle.load(f)

rel_emb = emb["rel_embeddings"]
ent_emb = emb["ent_embeddings"]


with open("./s_rel_emb.tsv", 'w') as f:
    tsv_w = csv.writer(f, delimiter='\t')
    tsv_w.writerows(rel_emb)
    # for e in rel_emb:
    #     f.write("\t".join([str(n) for n in e]))
    # f.write("\n")

with open("./s_ent_emb.tsv", 'w') as f:
    # for e in ent_emb:
    #     f.write("\t".join([str(n) for n in e]))
    # f.write("\n")
    tsv_w = csv.writer(f, delimiter='\t')
    tsv_w.writerows(ent_emb)
