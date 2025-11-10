import csv
from typing import List, Dict, Tuple

def load_knapsack_data_from_csv(filename: str) -> Dict[str, List]:
    """"
    Tải dữ liệu vật phẩm từ file CSV được chỉ định.
    
    Args:
        filename (str): Tên file CSV cần tải.

    Returns:
        Dict[str, List]: Dictionary chứa 'names', 'values', và 'weights'.
    """
    item_names = []
    item_values = []
    item_weights = []
    
    try:
        with open(filename, mode='r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            header = next(reader) # Bỏ qua header
            
            for row in reader:
                if len(row) >= 3:
                    try:
                        # Giả định cột 0: Tên, 1: Giá trị, 2: Khối lượng
                        name = row[0] 
                        value = int(row[1]) 
                        weight = int(row[2]) 
                        
                        item_names.append(name)
                        item_values.append(value)
                        item_weights.append(weight)
                    except ValueError:
                        continue # Bỏ qua dòng có dữ liệu không phải là số
                        
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file dữ liệu {filename}.")
        return {'names': [], 'values': [], 'weights': []}
    except Exception as e:
        print(f"Lỗi khi đọc file {filename}: {e}")
        return {'names': [], 'values': [], 'weights': []}
        
    return {'names': item_names, 'values': item_values, 'weights': item_weights}