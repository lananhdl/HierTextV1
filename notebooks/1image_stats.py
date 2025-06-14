
import os
from PIL import Image
from collections import defaultdict

# Đường dẫn đến thư mục chứa dữ liệu
base_dir = "/content/drive/MyDrive/dataanalysis/dataanalysisHiertexNhom1/data/raw/images"
folders = ['test', 'validation', 'train']

# Khởi tạo biến lưu trữ kết quả
stats = {
    'total_images': 0,
    'total_sizes': [],
    'folder_stats': {}
}

# Duyệt qua từng thư mục
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    image_count = 0
    sizes = []

    # Đếm số lượng ảnh và thu thập kích thước
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        try:
            with Image.open(img_path) as img:
                sizes.append(img.size)
                image_count += 1
        except Exception as e:
            print(f"Lỗi khi xử lý ảnh {img_path}: {e}")

    # Tính toán thống kê cho từng thư mục
    if sizes:
        avg_width = sum(w for w, h in sizes) / len(sizes)
        avg_height = sum(h for w, h in sizes) / len(sizes)
    else:
        avg_width, avg_height = 0, 0

    # Lưu kết quả
    stats['folder_stats'][folder] = {
        'image_count': image_count,
        'avg_width': avg_width,
        'avg_height': avg_height,
        'all_sizes': sizes
    }
    stats['total_images'] += image_count
    stats['total_sizes'].extend(sizes)

# Tính toán thống kê tổng hợp
if stats['total_sizes']:
    total_avg_width = sum(w for w, h in stats['total_sizes']) / len(stats['total_sizes'])
    total_avg_height = sum(h for w, h in stats['total_sizes']) / len(stats['total_sizes'])
else:
    total_avg_width, total_avg_height = 0, 0

# In kết quả
print("="*50)
print("THỐNG KÊ CHI TIẾT TỪNG THƯ MỤC")
print("="*50)
for folder, data in stats['folder_stats'].items():
    print(f"\nThư mục {folder.upper()}:")
    print(f"- Số lượng ảnh: {data['image_count']}")
    print(f"- Kích thước trung bình: {data['avg_width']:.1f}x{data['avg_height']:.1f}")

print("\n" + "="*50)
print("TỔNG HỢP TOÀN BỘ DỮ LIỆU")
print("="*50)
print(f"- Tổng số ảnh: {stats['total_images']}")
print(f"- Kích thước trung bình tổng hợp: {total_avg_width:.1f}x{total_avg_height:.1f}")
print("="*50)
