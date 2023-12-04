from PIL import Image
import torch
import requests
from io import BytesIO
import pandas as pd
from torchvision import transforms as T

def preprocess_image(image):
    # Преобразование изображения в формат RGB
    transform = T.Compose([
        T.Resize((440, 440)),
        T.Grayscale(num_output_channels=1),
        T.ToTensor(),
    ])
    return transform(image).unsqueeze(0)


def transforming(image):
    transform = T.Compose([T.Resize((440, 440))])
    return transform(image)


def detect_objects(image, model):
    # Преобразование изображения, чтобы соответствовать ожиданиям модели
    transform = T.Compose([
        T.Resize((640, 640)),  # Размер может отличаться в зависимости от вашей модели
        T.ToTensor(),
        # Другие преобразования, которые могут потребоваться
    ])

    input_image = transform(image).unsqueeze(0)  # Добавляем размерность батча

    # Переводим модель в режим оценки и применяем предсказание
    model.eval()
    with torch.no_grad():
        predictions = model(input_image)



    return predictions
