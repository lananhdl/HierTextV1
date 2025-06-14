
from torchvision import transforms
from PIL import Image
import torch

# Pipeline resize + normalize
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),  # chuyển về tensor [0,1]
    transforms.Normalize(mean=[0.5], std=[0.5])  # hoặc mean/std 3 kênh nếu RGB
])

# Data augmentation
augment = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.RandomResizedCrop(224)
])

# Ví dụ áp dụng lên ảnh
def preprocess_image(image_path):
    img = Image.open(image_path).convert('RGB')
    img_tensor = preprocess(img)
    return img_tensor

        