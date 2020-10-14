import sys
sys.path.append('./OpenKE')

import pickle
import json
import numpy as np
import config
import models
con = config.Config()
con.set_in_path("./s_train/")
con.set_work_threads(4)
con.set_dimension(50)
con.init()
con.set_model(models.TransE)
f = open("./s_train/s_emb.vec.json", "r")

with open('./s_emb.pkl', 'wb') as fs:
    pickle.dump(embeddings, fs, pickle.HIGHEST_PROTOCOL)
f.close()
