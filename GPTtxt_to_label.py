import os
import ast

def extract_info(txt_file, encoding='utf-8'):
    with open(txt_file, 'r', encoding=encoding) as f:
        data = f.read().split('\n')

    results = []
    for idx, item in enumerate(data, 1):
        if item:
            try:
                info_dict = ast.literal_eval(item)
                image_path = info_dict.get('image_path', '')  # 获取image_path字段，若不存在则为空字符串
                if image_path:
                    content = info_dict.get('content', '')  # 获取content字段，若不存在则为空字符串
                    if content:
                        categories = [category.split(': ')[1] for category in content.split('\n') if ': ' in category and '-----' not in category]
                        results.append((image_path, ', '.join(categories)))
            except Exception as e:
                print(f"Error processing line {idx}: {e}")
                print("Problematic line:", item)

    return results

def save_results(image_path, categories, output_dir):
    file_name = os.path.basename(image_path)[:-4] + '.txt'
    output_path = os.path.join(output_dir, file_name)
    with open(output_path, 'w') as f:
        f.write(categories)

if __name__ == "__main__":
    txt_file = r'GPTtxt.txt'
    output_dir = r'label_output_path'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    extracted_info = extract_info(txt_file)

    for image_path, categories in extracted_info:
        try:
            save_results(image_path, categories, output_dir)
        except Exception as e:
            print(f"{image_path}: {e}")
