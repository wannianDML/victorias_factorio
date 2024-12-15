import os

def rename_files_in_directory(directory, old_suffix, new_suffix):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否以 old_suffix 结尾
        if filename.endswith(old_suffix):
            # 构建旧文件路径
            old_file_path = os.path.join(directory, filename)
            # 构建新文件名（仅替换后缀部分）
            new_filename = filename[:-len(old_suffix)] + new_suffix
            # 构建新文件路径
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

def replace_first_line_text(directory, old_text, new_text):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 构建文件路径
        file_path = os.path.join(directory, filename)
        
        # 检查是否是文件（而不是目录）
        if os.path.isfile(file_path):
            try:
                # 以读取模式打开文件
                with open(file_path, 'r', encoding='utf-8') as file:
                    # 读取文件的所有内容
                    lines = file.readlines()
                
                # 检查第一行是否包含 old_text
                if lines and old_text in lines[0]:
                    # 替换第一行中的 old_text 为 new_text
                    lines[0] = lines[0].replace(old_text, new_text)
                    
                    # 以写入模式打开文件（会覆盖原文件）
                    with open(file_path, 'w', encoding='utf-8') as file:
                        # 写入修改后的内容
                        file.writelines(lines)
                    print(f'Modified: {file_path}')
            except Exception as e:
                # 打印错误信息（可能由于文件编码、权限等问题）
                print(f'Error processing {file_path}: {e}')
                

# 调用函数，指定当前文件夹（'.' 表示当前文件夹）
rename_files_in_directory('.', 'simp_chinese.yml', 'english.yml')
replace_first_line_text('.', 'l_simp_chinese:', 'l_english:')
