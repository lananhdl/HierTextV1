HiertextNhom1
==============================
download the dataset from https://www.kaggle.com/datasets/uciml/iris
 then unzip the file and put it in the gt folder

==============================
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
then save the images in the `images` folder

===============================
# HierText analysis:
run .py in the notebooks folder to analyze the dataset

```
