import sys

sys.path.append("./OpenKE")

import config
import models
import json
import numpy as np

con = config.Config()
#Input training files from benchmarks/FB15K/ folder.
con.set_in_path("./s_train/")
con.set_work_threads(4)
con.set_train_times(500)
con.set_nbatches(100)
con.set_alpha(0.001)
con.set_margin(1.0)
con.set_bern(0)
con.set_dimension(50)
con.set_ent_neg_rate(1)
con.set_rel_neg_rate(0)
con.set_opt_method("SGD")

#Models will be exported via tf.Saver() automatically.
con.set_export_files("./s_train/s_model.vec.tf", 0)
#Model parameters will be exported to json files automatically.
con.set_out_files("./s_train/s_emb.vec.json")
#Initialize experimental settings.
con.init()
#Set the knowledge embedding model
con.set_model(models.TransE)
#Train the model.
con.run()