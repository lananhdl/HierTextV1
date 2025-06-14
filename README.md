<<<<<<< HEAD
# The HierText Dataset

## Getting Started

First clone the project:

```
git clone https://github.com/google-research-datasets/hiertext.git
```

(Optional but recommended) Create and enter a virtual environment:

```
sudo pip install virtualenv
virtualenv -p python3 hiertext_env
source ./hiertext_env/bin/activate
```

Then install the required dependencies using:

```
cd hiertext
pip install -r requirements.txt
```

### Dataset downloading & processing

The ground-truth annotations of `train` / `validation` / `test` sets are stored in
`gt/train.jsonl.gz`, `gt/validation.jsonl.gz`, `gt/test.jsonl.gz` respectively. Use the following
command to decompress the two files:

```
gzip -d gt/*.jsonl.gz
```

The images are hosted by [CVDF](http://www.cvdfoundation.org/). To download them
one needs to install
[AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
and run the following:

```
aws s3 --no-sign-request cp s3://open-images-dataset/ocr/train.tgz .
aws s3 --no-sign-request cp s3://open-images-dataset/ocr/validation.tgz .
aws s3 --no-sign-request cp s3://open-images-dataset/ocr/test.tgz .
tar -xzvf train.tgz
tar -xzvf validation.tgz
tar -xzvf test.tgz
```

### Dataset inspection and visualization

Run the visualization notebook locally to inspect the data using:

```
jupyter notebook HierText_Visualization.ipynb
```

Run the following command to visualize and evaluation the dataset in a colab:
[hiertext.ipynb](hiertext.ipynb)
```

#
## Evaluation

Uses the following command for word-level detection evaluation:

```
python3 eval.py --gt=gt/validation.jsonl --result=/path/to/your/results.jsonl --output=/tmp/scores.txt --mask_stride=1
```
=======
# HierTextV1
>>>>>>> 30da4edffd674f2f4e8eeb1610fa7ec1e215b133
