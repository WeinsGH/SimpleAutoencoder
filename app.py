import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
from funcs import preprocess_image, transforming
from AutoEncoder_model import ImprovedConvAutoencoder


def main():
    st.title('Autoencoder')
    model_cleaning = ImprovedConvAutoencoder()
    model_cleaning.load_state_dict(torch.load('weights/improved_model_weights.pth', map_location=torch.device('cpu')))
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        with torch.no_grad():
            clean_doc = model_cleaning(preprocess_image(image))
        col3, col4 = st.columns(2)
        with col3:
            st.image(transforming(image), caption='Before')

        with col4:
            st.image(transforms.ToPILImage()(clean_doc.squeeze(0)), caption='After')


if __name__ == "__main__":
    main()
