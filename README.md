# SimpleAutoencoder
Autoencoder for docs/books, etc. with 4 decode and 4 encode layers and ReLU-activations.
You can use this to remove noise from photos or document scans. Model output is an image of 640x640 image size. 
Model class in **AutoEncoder_model.py**, it weights in **weights/improved_model_weights**.
Model was fitted by [shabby-docs dataframe](https://drive.google.com/file/d/1LsHSn8dM8BTZ7EoWU6-n1I1BvR0p5tIx/view) with 981/290/186 images in train/valid/test on 35 epochs. It was written on PyTorch 2.1.

This service is implemented on [Streamlit](https://simpleautoencoder-bs39kbsh8ebolyic48njyd.streamlit.app/)

----
# Model Architecture

![image](https://github.com/WeinsGH/SimpleAutoencoder/assets/109025285/1e866f02-50a4-4554-8600-5e58d9095d8f)

----
# Train/Valid MSE
![photo_2023-12-01_13-19-42](https://github.com/WeinsGH/SimpleAutoencoder/assets/109025285/d40c886c-6b1d-4e38-8c15-821f6814c0a2)


----
# Result by test images:
![tempsnip](https://github.com/WeinsGH/SimpleAutoencoder/assets/109025285/6bb40648-5dd8-4c39-84ea-658a8f68c3b9)
![Снимок](https://github.com/WeinsGH/SimpleAutoencoder/assets/109025285/45305bcb-9275-4267-ae42-30f8b02b7c90)

