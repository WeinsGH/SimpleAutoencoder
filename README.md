# SimpleAutoencoder
Autoencoder for docs/books, etc. with 4 decode and 4 encode layers and ReLU-activations.
You can use this to remove noise from photos or document scans. Model output is an image of 640x640 image size.
Programm is written on PyTorch. Model class in *AutoEncoder_model.py*, it weights in *weights/improved_model_weights*
Model was fitted by shabby-docs dataframe with 981/290/186 images in train/valid/test on 50 epochs.

data_link: <https://drive.google.com/file/d/1LsHSn8dM8BTZ7EoWU6-n1I1BvR0p5tIx/view>
----
Model Architecture

![image](https://github.com/WeinsGH/SimpleAutoencoder/assets/109025285/1e866f02-50a4-4554-8600-5e58d9095d8f)
----
