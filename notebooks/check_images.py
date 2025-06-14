
from PIL import Image, ImageStat
import os

def check_image_issues(image_folder, min_size=(100, 100)):
    issues = []

    for root, _, files in os.walk(image_folder):
        for file in files:
            if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
                continue

            img_path = os.path.join(root, file)
            try:
                with Image.open(img_path) as img:
                    # Kiểm tra kích thước
                    if img.size[0] < min_size[0] or img.size[1] < min_size[1]:
                        issues.append((img_path, 'Kích thước quá nhỏ'))

                    # Kiểm tra độ mờ / trắng
                    stat = ImageStat.Stat(img.convert('L'))
                    if stat.stddev[0] < 5:
                        issues.append((img_path, 'Ảnh có độ tương phản thấp (trắng hoặc mờ)'))

            except Exception as e:
                issues.append((img_path, f'Lỗi không mở được ảnh: {e}'))

    return issues

# Kiểm tra ảnh trong tất cả thư mục
folders = ['train', 'test', 'validation']
base_path = "/content/drive/MyDrive/dataanalysis/dataanalysisHiertexNhom1/data/raw/images"

for folder in folders:
    print(f"\nĐang kiểm tra thư mục: {folder}")
    issues = check_image_issues(os.path.join(base_path, folder))
    for path, reason in issues:
        print(f"{reason} → {path}")
        