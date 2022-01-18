import torch
from PIL import Image
from torchvision import transforms
from model import Model

model = Model("model_files/gender_v1.pth")

image_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

decode_answer = {
    0: "Male",
    1: "Female",
}

def get_predict(image):
    int_predict = torch.max(model(image), 1)[1].numpy()[0]
    str_predict = decode_answer[int_predict]
    return str_predict

def prepare_image(image):
    image = Image.open(image)
    image = image_transforms(image).unsqueeze(0)
    return image
