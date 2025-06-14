
import os
import random
import matplotlib.pyplot as plt
from PIL import Image

base_dir = "/content/drive/MyDrive/dataanalysis/dataanalysisHiertexNhom1/data/raw/images"
folders = ['test', 'validation', 'train']

def show_random_images(folder_path, num_images=5):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('jpg', 'jpeg', 'png'))]
    if not files:
        print(f"Không có ảnh trong thư mục: {folder_path}")
        return
    
    sample_files = random.sample(files, min(num_images, len(files)))

    plt.figure(figsize=(15, 5))
    for i, file in enumerate(sample_files):
        img_path = os.path.join(folder_path, file)
        try:
            img = Image.open(img_path)
            plt.subplot(1, num_images, i + 1)
            plt.imshow(img)
            plt.title(file)
            plt.axis('off')
        except Exception as e:
            print(f"Lỗi khi mở ảnh {file}: {e}")
    plt.tight_layout()
    plt.show()

# Gọi hàm cho từng folder
for folder in folders:
    print(f"\nHiển thị ảnh mẫu từ thư mục: {folder}")
    folder_path = os.path.join(base_dir, folder)
    show_random_images(folder_path, num_images=5)
# In thông báo
print(f"\n Copy toàn bộ nội dung file này để chạy trên Google Colab sẽ hiển thị ảnh nhé.")
    