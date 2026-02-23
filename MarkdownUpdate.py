import os
import urllib.parse

# ====== CẤU HÌNH ======
folder_path = r"./Source"      # Thư mục chứa ảnh
output_md = "Readme.md"    # File Markdown xuất ra
relative_path = "Source"       # Đường dẫn tương đối trong Markdown
image_width = 300              # Kích thước ảnh hiển thị

# Các định dạng ảnh hợp lệ
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

# ====== TÌM FILE ẢNH ======
image_files = []

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        if ext in image_extensions:
            image_files.append(file)

# Sắp xếp A-Z (không phân biệt hoa thường)
image_files.sort(key=lambda x: x.lower())

# ====== TẠO FILE MARKDOWN ======
with open(output_md, "w", encoding="utf-8") as md:

    # Tiêu đề chính
    md.write("# SAMPI DEVELOPMENT KIT - ELECTRONIC COMPONENT 3D MODEL LIBRARY\n\n")

    # Tạo bảng
    md.write("| No | Component Name | Preview |\n")
    md.write("|----|----------------|---------|\n")

    for index, file in enumerate(image_files, start=1):
        name_no_ext = os.path.splitext(file)[0].upper()

        # Encode đường dẫn để xử lý dấu cách và ký tự đặc biệt
        encoded_file = urllib.parse.quote(file)

        image_path = f"{relative_path}/{encoded_file}"

        md.write(f"| {index} | {name_no_ext} | "
                 f"<img src=\"{image_path}\" width=\"{image_width}\"> |\n")

print(f"Đã tạo file Markdown: {output_md}")