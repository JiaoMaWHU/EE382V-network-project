## Setup
* git clone this repo
* cd into this repo
* ```git clone -b OpenKE-Tensorflow1.0 https://github.com/thunlp/OpenKE```
* compile OpenKE as specified here: https://github.com/thunlp/OpenKE/tree/OpenKE-Tensorflow1.0
* ```python3 -m pip install tensorflow==1.15```
* To konw if everything works fine, run ```python3 test.py```.

## working together
* login tacc
* cd $WORK, you will see the project
* ```module load gcc python3```
* To konw if everything works fine, run ```python3 test.py```
* you shold process the dataset using the `json_to_csv_converter.py`, as explained here: https://github.com/Yelp/dataset-examples