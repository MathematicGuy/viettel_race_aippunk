import os
import re
import shutil
from pathlib import Path

def process_public_directory(public_dir):
    """
    Xử lý thư mục PublicXXX để đổi tên ảnh, cập nhật tham chiếu trong main.md,
    và xóa các ảnh không được tham chiếu.
    """
    main_md = public_dir / 'main.md'
    images_dir = public_dir / 'images'

    if not main_md.exists() or not images_dir.exists():
        print(f"Bỏ qua {public_dir}: không tìm thấy main.md hoặc thư mục images")
        return

    print(f"Đang xử lý {public_dir}")

    with open(main_md, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm tất cả các tham chiếu ảnh trong nội dung markdown
    image_refs = re.findall(r'!\[.*?\]\(([^)]+)\)', content)
    
    # Chỉ lọc các file ảnh trong thư mục images
    image_refs = [
        ref for ref in image_refs if ref.startswith('images/') and 
        ref.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
    ]

    # --- THAY ĐỔI LOGIC BẮT ĐẦU TỪ ĐÂY ---

    # 1. Tạo bản đồ cho TẤT CẢ các ảnh được tham chiếu, dù có đổi tên hay không
    # Đây là danh sách các ảnh sẽ được "giữ lại"
    kept_images_map = {}
    updated_content = content

    for i, old_ref in enumerate(image_refs, 1):
        old_path = public_dir / old_ref
        if not old_path.exists():
            print(f"  Cảnh báo: {old_ref} không tồn tại, bỏ qua")
            continue
            
        ext = os.path.splitext(old_ref)[1]
        new_filename = f"image{i}{ext}"
        new_ref = f"images/{new_filename}"
        
        # Thêm vào bản đồ kept_images_map
        kept_images_map[old_ref] = new_ref
        
        # Cập nhật nội dung markdown ngay lập tức để thay thế các tham chiếu
        # Điều này an toàn hơn việc replace hàng loạt sau này
        if old_ref != new_ref:
            updated_content = updated_content.replace(f"]({old_ref})", f"]({new_ref})")

    # Nếu không có ảnh nào được tham chiếu, ta có thể xóa tất cả ảnh
    if not kept_images_map:
        print("  Không có ảnh nào được tham chiếu trong main.md. Xóa tất cả ảnh...")
        for item in images_dir.glob('*'):
            if item.is_file():
                item.unlink()
        return # Kết thúc sớm

    # 2. Sử dụng thư mục tạm để xử lý an toàn
    temp_dir = public_dir / 'temp_images'
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir()

    try:
        # 3. Sao chép và đổi tên các ảnh cần giữ vào thư mục tạm
        for old_ref, new_ref in kept_images_map.items():
            old_path = public_dir / old_ref
            new_path = temp_dir / os.path.basename(new_ref)
            shutil.copy2(old_path, new_path)
        print(f"  Đã sao chép {len(kept_images_map)} ảnh cần giữ vào thư mục tạm")

        # 4. Xóa sạch thư mục images gốc
        for item in images_dir.glob('*'):
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
        
        # 5. Di chuyển các ảnh đã đổi tên từ temp về lại images
        for item in temp_dir.glob('*'):
            shutil.move(str(item), str(images_dir / item.name))
        
        # 6. Ghi lại nội dung main.md đã được cập nhật
        with open(main_md, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"  Đã cập nhật các tham chiếu và dọn dẹp thư mục images")

    finally:
        # 7. Dọn dẹp thư mục tạm
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

# Các hàm process_all_directories và __main__ giữ nguyên như cũ
# ... (phần code còn lại của bạn) ...
def process_all_directories(root_dir):
    """
    Process all PublicXXX directories in the root directory
    """
    root_path = Path(root_dir)
    
    # Iterate through all PublicXXX directories
    for public_dir in sorted(root_path.glob('Public*')):
        if public_dir.is_dir():
            process_public_directory(public_dir)

if __name__ == "__main__":
    # Get the directory where this script is located
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    except NameError:
        script_dir = os.getcwd() # Dành cho môi trường interactive như Jupyter
        
    out_dir = os.path.join(script_dir, 'out')
    
    if os.path.exists(out_dir):
        print(f"Bắt đầu xử lý ảnh trong {out_dir}")
        process_all_directories(out_dir)
        print("Hoàn tất!")
    else:
        print(f"Lỗi: Không tìm thấy thư mục: {out_dir}")