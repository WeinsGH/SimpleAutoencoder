from PIL import Image
import torch
from io import BytesIO
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
