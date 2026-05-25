#!/usr/bin/env python3
import os
import re

# Mapping từ ký tự có dấu sang không dấu
ACCENT_MAP = {
    'À': 'A', 'Á': 'A', 'Ả': 'A', 'Ã': 'A', 'Ạ': 'A',
    'Ă': 'A', 'Ằ': 'A', 'Ắ': 'A', 'Ẳ': 'A', 'Ẵ': 'A', 'Ặ': 'A',
    'Â': 'A', 'Ầ': 'A', 'Ấ': 'A', 'Ẩ': 'A', 'Ẫ': 'A', 'Ậ': 'A',
    'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
    'ă': 'a', 'ằ': 'a', 'ắ': 'a', 'ẳ': 'a', 'ẵ': 'a', 'ặ': 'a',
    'â': 'a', 'ầ': 'a', 'ấ': 'a', 'ẩ': 'a', 'ẫ': 'a', 'ậ': 'a',
    'Đ': 'D', 'đ': 'd',
    'È': 'E', 'É': 'E', 'Ẻ': 'E', 'Ẽ': 'E', 'Ẹ': 'E',
    'Ề': 'E', 'Ế': 'E', 'Ể': 'E', 'Ễ': 'E', 'Ệ': 'E',
    'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
    'ề': 'e', 'ế': 'e', 'ể': 'e', 'ễ': 'e', 'ệ': 'e',
    'Ì': 'I', 'Í': 'I', 'Ỉ': 'I', 'Ĩ': 'I', 'Ị': 'I',
    'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
    'Ò': 'O', 'Ó': 'O', 'Ỏ': 'O', 'Õ': 'O', 'Ọ': 'O',
    'Ô': 'O', 'Ồ': 'O', 'Ố': 'O', 'Ổ': 'O', 'Ỗ': 'O', 'Ộ': 'O',
    'Ơ': 'O', 'Ờ': 'O', 'Ớ': 'O', 'Ở': 'O', 'Ỡ': 'O', 'Ợ': 'O',
    'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
    'ô': 'o', 'ồ': 'o', 'ố': 'o', 'ổ': 'o', 'ỗ': 'o', 'ộ': 'o',
    'ơ': 'o', 'ờ': 'o', 'ớ': 'o', 'ở': 'o', 'ỡ': 'o', 'ợ': 'o',
    'Ù': 'U', 'Ú': 'U', 'Ủ': 'U', 'Ũ': 'U', 'Ụ': 'U',
    'Ư': 'U', 'Ừ': 'U', 'Ứ': 'U', 'Ử': 'U', 'Ữ': 'U', 'Ự': 'U',
    'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
    'ư': 'u', 'ừ': 'u', 'ứ': 'u', 'ử': 'u', 'ữ': 'u', 'ự': 'u',
    'Ỳ': 'Y', 'Ý': 'Y', 'Ỷ': 'Y', 'Ỹ': 'Y', 'Ỵ': 'Y',
    'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
}

def remove_accents(text):
    """Loại bỏ dấu tiếng Việt từ text, thay space bằng underscore, và xóa commas"""
    result = []
    for char in text:
        if char == ' ':
            result.append('_')
        elif char == ',':
            continue  # Bỏ qua commas
        else:
            result.append(ACCENT_MAP.get(char, char))
    return ''.join(result)


def rename_files_in_dir(directory):
    """Rename all PDF files in a directory to remove accents"""
    if not os.path.isdir(directory):
        return
    
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    for f in sorted(pdf_files):
        new_name = remove_accents(f)
        old_path = os.path.join(directory, f)
        new_path = os.path.join(directory, new_name)
        if f != new_name:
            os.rename(old_path, new_path)
            print(f'✓ {f}')
            print(f'  → {new_name}')
        else:
            print(f'- {f} (no change)')

# Rename files in src/assets/scans
src_scans = '/Users/tuanpham/Works/Website/KhanhLyLandingPage/src/assets/scans'
print(f'📁 {src_scans}:')
rename_files_in_dir(src_scans)

# Rename files in src/assets/scans/Documents
src_docs = os.path.join(src_scans, 'Documents')
print(f'\n📁 {src_docs}:')
rename_files_in_dir(src_docs)

# Rename files in public/scans
pub_scans = '/Users/tuanpham/Works/Website/KhanhLyLandingPage/public/scans'
if os.path.isdir(pub_scans):
    print(f'\n📁 {pub_scans}:')
    rename_files_in_dir(pub_scans)

    # Rename files in public/scans/Documents
    pub_docs = os.path.join(pub_scans, 'Documents')
    print(f'\n📁 {pub_docs}:')
    rename_files_in_dir(pub_docs)

print('\n✅ Done!')
