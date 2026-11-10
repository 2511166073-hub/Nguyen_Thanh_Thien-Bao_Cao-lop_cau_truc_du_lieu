``` python
def tim_chuoi_con(doan_van, chuoi_can_tim):
    """
    Tìm tất cả vị trí xuất hiện của chuoi_can_tim trong doan_van.
    
    Tham số:
        doan_van (str): Đoạn văn gốc
        chuoi_can_tim (str): Chuỗi cần tìm
    
    Trả về:
        list: Danh sách các vị trí (index) tìm thấy chuỗi
    """
    n = len(doan_van)
    m = len(chuoi_can_tim)
    vi_tri_tim_thay = []
    
    # Nếu chuỗi cần tìm rỗng hoặc dài hơn đoạn văn -> trả về rỗng
    if m == 0 or m > n:
        return vi_tri_tim_thay
    
    # Duyệt qua từng vị trí trong đoạn văn
    # Chỉ cần duyệt đến (n - m) vì sau đó không đủ ký tự để so sánh
    for i in range(n - m + 1):
        da_khop = True
        
        # So sánh từng ký tự của chuỗi cần tìm với đoạn văn
        for j in range(m):
            if doan_van[i + j] != chuoi_can_tim[j]:
                da_khop = False
                break  # Lệch 1 ký tự -> dừng ngay, không cần so tiếp
        
        # Nếu tất cả ký tự đều khớp
        if da_khop:
            vi_tri_tim_thay.append(i)
    
    return vi_tri_tim_thay


def dem_chuoi_con(doan_van, chuoi_can_tim):
    """
    Đếm số lần xuất hiện của chuoi_can_tim trong doan_van.
    
    Tham số:
        doan_van (str): Đoạn văn gốc
        chuoi_can_tim (str): Chuỗi cần tìm
    
    Trả về:
        int: Số lần xuất hiện
    """
    vi_tri = tim_chuoi_con(doan_van, chuoi_can_tim)
    return len(vi_tri)


def kiem_tra_chua_chuoi(doan_van, chuoi_can_tim):
    """
    Kiểm tra chuoi_can_tim có xuất hiện trong doan_van hay không.
    
    Tham số:
        doan_van (str): Đoạn văn gốc
        chuoi_can_tim (str): Chuỗi cần tìm
    
    Trả về:
        bool: True nếu có, False nếu không
    """
    vi_tri = tim_chuoi_con(doan_van, chuoi_can_tim)
    return len(vi_tri) > 0


# ============================================================
# CHẠY THỬ (TEST)
# ============================================================
if __name__ == "__main__":
    
    # Test 1: Tìm chuỗi đơn giản
    print("=" * 50)
    print("TEST 1: Tìm chuỗi đơn giản")
    print("=" * 50)
    
    doan_van = "Hom nay troi dep, xe 5x-1234 va 5x-5678 di qua nga tu."
    chuoi = "5x"
    
    ket_qua = tim_chuoi_con(doan_van, chuoi)
    
    print(f"Đoạn văn: '{doan_van}'")
    print(f"Chuỗi cần tìm: '{chuoi}'")
    print(f"Vị trí tìm thấy: {ket_qua}")
    print(f"Số lần xuất hiện: {len(ket_qua)}")
    
    # Test 2: Tìm chuỗi không tồn tại
    print("\n" + "=" * 50)
    print("TEST 2: Tìm chuỗi không tồn tại")
    print("=" * 50)
    
    chuoi2 = "abc"
    ket_qua2 = tim_chuoi_con(doan_van, chuoi2)
    
    print(f"Chuỗi cần tìm: '{chuoi2}'")
    print(f"Vị trí tìm thấy: {ket_qua2}")
    print(f"Số lần xuất hiện: {len(ket_qua2)}")
    
    # Test 3: Tìm chuỗi xuất hiện nhiều lần
    print("\n" + "=" * 50)
    print("TEST 3: Tìm chuỗi xuất hiện nhiều lần")
    print("=" * 50)
    
    doan_van3 = "aaaa"
    chuoi3 = "aa"
    
    ket_qua3 = tim_chuoi_con(doan_van3, chuoi3)
    
    print(f"Đoạn văn: '{doan_van3}'")
    print(f"Chuỗi cần tìm: '{chuoi3}'")
    print(f"Vị trí tìm thấy: {ket_qua3}")
    print(f"Số lần xuất hiện: {len(ket_qua3)}")
    
    # Test 4: Sử dụng hàm đếm
    print("\n" + "=" * 50)
    print("TEST 4: Sử dụng hàm dem_chuoi_con")
    print("=" * 50)
    
    so_lan = dem_chuoi_con(doan_van, "5x")
    print(f"Số lần '5x' xuất hiện: {so_lan}")
    
    # Test 5: Sử dụng hàm kiểm tra
    print("\n" + "=" * 50)
    print("TEST 5: Sử dụng hàm kiem_tra_chua_chuoi")
    print("=" * 50)
    
    co_chua = kiem_tra_chua_chuoi(doan_van, "5x")
    print(f"Đoạn văn có chứa '5x': {co_chua}")
    
    co_chua2 = kiem_tra_chua_chuoi(doan_van, "xyz")
    print(f"Đoạn văn có chứa 'xyz': {co_chua2}")
  ```
