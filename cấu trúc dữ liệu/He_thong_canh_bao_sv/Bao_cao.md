# Báo cáo: Hệ thống cảnh báo sớm sinh viên thôi học


## Mục lục

1. Đặt vấn đề  
2. Mục tiêu hệ thống  
3. Bài toán cốt lõi  
4. Dữ liệu sử dụng  
5. Cấu trúc dữ liệu đề xuất  
6. Giải thuật đề xuất  
7. Kiến trúc hệ thống  
8. Quy trình cảnh báo và can thiệp  
9. Đánh giá và đạo đức dữ liệu  
10. Kết luận  

---

## 1. Đặt vấn đề

Theo các bài báo và thực tế quản lý giáo dục, tỉ lệ sinh viên thôi học giữa chừng gây ảnh hưởng đến cá nhân sinh viên, gia đình, nhà trường và nguồn nhân lực xã hội. Nếu chỉ phát hiện sinh viên bỏ học khi sự việc đã xảy ra, nhà trường sẽ mất cơ hội can thiệp sớm.

Trong thực tế, sinh viên hiếm khi nghỉ học đột ngột mà thường có quá trình giảm dần qua nhiều tín hiệu, chẳng hạn:

- Điểm trung bình học kỳ giảm.
- Số môn rớt tăng.
- Tỷ lệ vắng học cao.
- Nợ học phí kéo dài.
- Ít tham gia hoạt động học tập và ngoại khóa.
- Mất kết nối với lớp, nhóm học tập hoặc cố vấn học tập.

Do đó, cần xây dựng một hệ thống cảnh báo sớm giúp:

- Phát hiện sinh viên có nguy cơ thôi học.
- Xếp hạng mức độ rủi ro.
- Đề xuất hành động can thiệp phù hợp.
- Hỗ trợ cố vấn học tập, phòng công tác sinh viên và giảng viên.

---

## 2. Mục tiêu hệ thống

Hệ thống cần đạt các mục tiêu sau:

1. **Dự đoán rủi ro thôi học** của từng sinh viên theo từng học kỳ.
2. **Cảnh báo sớm** trước khi sinh viên có quyết định nghỉ học.
3. **Phân loại mức cảnh báo**: thấp, trung bình, cao, rất cao.
4. **Đề xuất hành động can thiệp** như nhắc nhở, gặp cố vấn, hỗ trợ tài chính, tư vấn học tập.
5. **Theo dõi hiệu quả can thiệp** để cải thiện mô hình và quy trình hỗ trợ sinh viên.

Hệ thống không nhằm mục đích loại bỏ hay trừng phạt sinh viên, mà nhằm hỗ trợ nhà trường can thiệp kịp thời và nhân văn hơn.

---

## 3. Bài toán cốt lõi

### 3.1. Phát biểu bài toán

Bài toán được phát biểu như sau:

> Cho dữ liệu lịch sử và dữ liệu hiện tại của N sinh viên trong một học kỳ, bao gồm thông tin cá nhân, kết quả học tập, chuyên cần, tài chính, hoạt động ngoại khóa và các sự kiện hỗ trợ. Hãy **tính điểm rủi ro thôi học** của từng sinh viên, **xác định mức cảnh báo**, **giải thích nguyên nhân** và **xếp hạng sinh viên theo mức độ ưu tiên can thiệp**.

Nói cách khác, hệ thống cần trả lời các câu hỏi:

```text
1. Sinh viên nào có nguy cơ thôi học?
2. Mức độ nguy cơ là bao nhiêu?
3. Nguyên nhân chính của nguy cơ là gì?
4. Sinh viên nào cần được ưu tiên hỗ trợ trước?
5. Nhà trường nên thực hiện hành động can thiệp nào?
```

---

### 3.2. Dữ liệu đầu vào

Đầu vào của bài toán là dữ liệu của `N` sinh viên trong một học kỳ. Với mỗi sinh viên, dữ liệu bao gồm:

| Nhóm dữ liệu | Ví dụ |
|--------------|-------|
| Thông tin cá nhân | Mã sinh viên, lớp, năm đào tạo, diện chính sách |
| Kết quả học tập | GPA, số môn rớt, số tín chỉ tích lũy, tiến độ học tập |
| Chuyên cần | Số buổi vắng, tỷ lệ vắng học, số lần đi muộn |
| Tài chính | Nợ học phí, số lần chậm đóng học phí, học bổng |
| Hoạt động | Điểm rèn luyện, hoạt động ngoại khóa, câu lạc bộ |
| Hỗ trợ | Lịch sử liên hệ cố vấn học tập, tư vấn tâm lý |
| Quan hệ xã hội | Bạn cùng lớp, nhóm học tập, câu lạc bộ |

Ký hiệu tập sinh viên là `S = {s₁, s₂, ..., s_N}`. Mỗi sinh viên `sᵢ` được biểu diễn dưới dạng một vector đặc trưng:

```text
xᵢ = {GPA, số môn rớt, tỷ lệ vắng, nợ học phí, điểm rèn luyện, ...}
```

Ngoài ra, mỗi sinh viên còn có dữ liệu chuỗi thời gian:

```text
GPAᵢ = [GPA_kỳ_1, GPA_kỳ_2, ..., GPA_kỳ_T]
```

và dữ liệu quan hệ xã hội được biểu diễn bằng đồ thị:

```text
G = (V, E)
```

trong đó `V` là tập đỉnh (sinh viên, lớp, câu lạc bộ, cố vấn học tập) và `E` là tập cạnh biểu diễn quan hệ giữa các đỉnh.

---

### 3.3. Dữ liệu đầu ra

Với mỗi sinh viên, hệ thống trả về:

```text
1. Điểm rủi ro: risk_score ∈ [0, 100]
2. Mức cảnh báo: THẤP, TRUNG BÌNH, CAO, RẤT CAO
3. Danh sách lý do chính gây ra rủi ro
4. Hành động can thiệp được đề xuất
```

Ngoài ra, hệ thống tạo ra danh sách ưu tiên:

```text
Top-k sinh viên có risk_score cao nhất
```

để cố vấn học tập và phòng công tác sinh viên xử lý trước.

**Ví dụ đầu ra:**

```text
Sinh viên: SV001
Risk score: 100
Mức cảnh báo: RẤT CAO

Lý do chính:
- GPA dưới 2.0
- Có từ 4 môn rớt trở lên
- Tỷ lệ vắng học trên 30%
- Nợ học phí trên 8 triệu đồng
- Hơn 90 ngày không liên hệ cố vấn học tập

Hành động đề xuất:
- Cố vấn học tập liên hệ khẩn cấp
- Kiểm tra tình trạng tài chính và đề xuất hỗ trợ học phí
- Xếp nhóm học tập hoặc tư vấn học đường nếu cần
```

---

### 3.4. Các hướng tiếp cận

Về mặt kỹ thuật, bài toán có thể được tiếp cận theo nhiều hướng:

| Hướng tiếp cận | Mô tả |
|----------------|-------|
| Phân loại nhị phân | Dự đoán sinh viên có thôi học hay không thôi học |
| Chấm điểm rủi ro | Trả về điểm rủi ro từ 0 đến 100 |
| Xếp hạng ưu tiên | Chọn ra nhóm sinh viên có nguy cơ cao nhất để can thiệp trước |
| Phát hiện xu hướng | Phân tích dữ liệu theo thời gian để phát hiện sinh viên đang suy giảm |
| Phân tích quan hệ xã hội | Phát hiện sinh viên bị cô lập hoặc thiếu kết nối |
| Dự báo theo thời gian | Nếu mở rộng, có thể dự đoán thời điểm sinh viên có nguy cơ nghỉ học |

Trong phạm vi báo cáo này, hướng tiếp cận được lựa chọn là:

> **Bài toán tính điểm rủi ro, xếp hạng ưu tiên can thiệp và phát hiện sớm các dấu hiệu suy giảm của sinh viên.**

Hướng tiếp cận này phù hợp với môn **Cấu trúc dữ liệu và Giải thuật** vì có thể phân rã thành các bài toán con như: tra cứu dữ liệu, tính điểm, sắp xếp/xếp hạng, xử lý chuỗi thời gian, duyệt đồ thị và hàng đợi ưu tiên.

---

### 3.5. Phân rã bài toán

Bài toán tổng thể được phân rã thành các bài toán con sau:

| STT | Bài toán con | Mục tiêu | Cấu trúc dữ liệu | Giải thuật | Độ phức tạp |
|-----|--------------|----------|------------------|------------|-------------|
| 1 | Tra cứu hồ sơ sinh viên | Tìm thông tin sinh viên theo MSSV | Bảng băm | Tra cứu trực tiếp | `O(1)` |
| 2 | Xây dựng ma trận đặc trưng | Chuyển dữ liệu thô thành bảng đặc trưng | Mảng hai chiều | Duyệt và tổng hợp | `O(N·F)` |
| 3 | Tính điểm rủi ro | Chấm điểm nguy cơ thôi học | Mảng luật | Duyệt luật | `O(N·R)` |
| 4 | Phát hiện xu hướng học tập | Phát hiện GPA giảm, vắng tăng | Mảng chuỗi thời gian | Duyệt mảng, cửa sổ trượt, prefix sum | `O(N·T)` |
| 5 | Phân tích quan hệ xã hội | Phát hiện sinh viên bị cô lập | Đồ thị danh sách kề | BFS/DFS | `O(V + E)` |
| 6 | Chọn sinh viên ưu tiên can thiệp | Lấy top-k sinh viên rủi ro cao nhất | Heap | Top-k | `O(N log k)` |
| 7 | Quản lý cảnh báo động | Cập nhật cảnh báo khi điểm rủi ro thay đổi | Indexed heap | Push/update/pop | `O(log N)` |
| 8 | Chống trùng cảnh báo | Tránh tạo nhiều cảnh báo cho cùng một sinh viên trong một kỳ | Tập hợp | Kiểm tra thành viên | `O(1)` |

**Trong đó:**

- `N` = số sinh viên
- `F` = số đặc trưng
- `R` = số luật
- `T` = số học kỳ
- `V` = số đỉnh trong đồ thị
- `E` = số cạnh trong đồ thị
- `k` = số sinh viên cần lấy ra trong top-k

---

### 3.6. Phạm vi của báo cáo

Trong phạm vi môn học, báo cáo tập trung vào các phần sau:

1. **Xây dựng bộ luật tính điểm rủi ro.**
2. **Sử dụng mảng hai chiều để biểu diễn ma trận đặc trưng.**
3. **Sử dụng mảng chuỗi thời gian để phát hiện xu hướng giảm GPA.**
4. **Sử dụng đồ thị danh sách kề để phát hiện sinh viên bị cô lập.**
5. **Sử dụng heap để xếp hạng và chọn top-k sinh viên cần can thiệp trước.**

Các phương pháp học máy như Logistic Regression, Random Forest, XGBoost được xem là **hướng phát triển mở rộng**, không phải trọng tâm của báo cáo này.

---

## 4. Dữ liệu sử dụng

Hệ thống có thể thu thập các nhóm dữ liệu sau.

### 4.1. Thông tin cá nhân

- Mã sinh viên.
- Họ tên.
- Giới tính.
- Năm sinh.
- Quê quán.
- Diện chính sách.
- Dân tộc.
- Hộ khẩu thường trú.
- Hoàn cảnh kinh tế.

### 4.2. Dữ liệu học tập

- Điểm trung bình học kỳ.
- Điểm từng môn.
- Số môn rớt.
- Số tín chỉ tích lũy.
- Tiến độ so với chương trình.
- Kết quả rèn luyện.
- Số lần học lại.
- Số môn đang nợ.

### 4.3. Dữ liệu chuyên cần

- Số buổi vắng.
- Tỷ lệ đi học.
- Vắng không phép.
- Đi muộn.
- Tham gia lớp học trực tuyến nếu có.

### 4.4. Dữ liệu tài chính

- Học phí còn nợ.
- Số lần chậm đóng học phí.
- Được miễn giảm học phí.
- Nhận học bổng.
- Vay vốn sinh viên.

### 4.5. Dữ liệu hành vi và hoạt động

- Đăng ký môn học.
- Hủy môn.
- Sử dụng thư viện.
- Truy cập portal sinh viên.
- Tham gia câu lạc bộ.
- Hoạt động ngoại khóa.
- Tư vấn tâm lý.
- Liên hệ phòng công tác sinh viên.

### 4.6. Dữ liệu quan hệ xã hội

- Bạn cùng lớp.
- Nhóm học tập.
- Câu lạc bộ.
- Giảng viên phụ trách.
- Cố vấn học tập.

Nhóm dữ liệu quan hệ xã hội có thể biểu diễn bằng đồ thị để phân tích mức độ kết nối, sự cô lập hoặc ảnh hưởng nhóm đối với nguy cơ thôi học.

### 4.7. Dữ liệu sự kiện hỗ trợ và can thiệp

Nhóm dữ liệu này ghi nhận các lần nhà trường đã tiếp cận, hỗ trợ hoặc can thiệp sinh viên.

Trường có thể bao gồm:

- Mã sinh viên
- Ngày tạo cảnh báo
- Ngày can thiệp
- Người phụ trách can thiệp
- Loại can thiệp
- Nội dung hỗ trợ
- Kết quả ban đầu
- Trạng thái sau can thiệp
- Ghi chú của cố vấn học tập

**Ví dụ các loại can thiệp:**

- Nhắc nhở học tập
- Mời gặp cố vấn học tập
- Hỗ trợ học phí
- Giới thiệu học bổng
- Xếp nhóm học tập
- Tư vấn tâm lý
- Liên hệ gia đình

**Vai trò:**

- Giúp theo dõi sinh viên đã được hỗ trợ hay chưa
- Tránh tạo cảnh báo trùng lặp
- Đánh giá loại can thiệp nào có hiệu quả
- Cung cấp dữ liệu phản hồi để cải thiện hệ thống

  ### 4.8. Dữ liệu trạng thái và kết quả của sinh viên

Nhóm dữ liệu này cho biết kết quả thực tế của sinh viên sau mỗi học kỳ hoặc sau khi được can thiệp.

**Các trạng thái có thể bao gồm:**

- Tiếp tục học
- Nghỉ học tạm thời
- Bảo lưu
- Bị cảnh báo học vụ
- Buộc thôi học
- Tự thôi học
- Tốt nghiệp

**Vai trò:**

- Dùng để đánh giá hiệu quả dự đoán của hệ thống
- Xác định sinh viên nào thực sự có rủi ro cao
- Nếu mở rộng bằng học máy, đây là dữ liệu nhãn để huấn luyện mô hình
- Giúp đo các chỉ số như recall, precision, F1-score hoặc top-k recall

**Ví dụ:**

| MSSV | Học kỳ | Trạng thái |
|------|--------|------------|
| SV001 | 20252 | Tiếp tục học |
| SV002 | 20252 | Tự thôi học |
| SV003 | 20252 | Bảo lưu |
| SV004 | 20252 | Tiếp tục học |

### 4.9. Ánh xạ dữ liệu sang cấu trúc xử lý

Không phải toàn bộ dữ liệu thô đều được đưa trực tiếp vào thuật toán. Hệ thống cần chuyển dữ liệu thành các cấu trúc phù hợp cho từng bài toán.

| Nhóm dữ liệu | Dữ liệu ví dụ | Cấu trúc xử lý đề xuất | Bài toán sử dụng |
|--------------|---------------|------------------------|------------------|
| Thông tin cá nhân | MSSV, họ tên, lớp | Bảng băm `dict` | Tra cứu hồ sơ sinh viên |
| Kết quả học tập | GPA, số môn rớt, tín chỉ | Ma trận đặc trưng | Tính điểm rủi ro |
| Dữ liệu học tập theo học kỳ | GPA các kỳ, số môn rớt các kỳ | Mảng chuỗi thời gian | Phát hiện xu hướng giảm |
| Chuyên cần | Tỷ lệ vắng, số buổi nghỉ | Mảng chuỗi thời gian | Phát hiện vắng tăng dần |
| Tài chính | Nợ học phí, thời gian nợ | Mảng đặc trưng / chuỗi thời gian | Đánh giá áp lực tài chính |
| Hoạt động | Điểm rèn luyện, câu lạc bộ | Ma trận đặc trưng | Đánh giá mức độ tham gia |
| Quan hệ xã hội | Bạn cùng lớp, nhóm học tập, câu lạc bộ | Đồ thị danh sách kề | Phát hiện sinh viên cô lập |
| Cảnh báo | MSSV, điểm rủi ro, học kỳ | Heap / indexed heap | Xếp hạng ưu tiên can thiệp |
| Lịch sử can thiệp | Ngày hỗ trợ, loại hỗ trợ | Danh sách liên kết / bảng ghi | Theo dõi hiệu quả can thiệp |
| Chống trùng cảnh báo | MSSV đã có cảnh báo trong kỳ | Tập hợp `set` | Tránh tạo cảnh báo trùng |

### 4.10. Ví dụ biểu diễn dữ liệu trong Python

 **Hồ sơ sinh viên — bảng băm:**

```python
students = {
    "SV001": {
        "name": "Nguyễn Văn A",
        "class": "CA3",
        "policy": "Không",
        "economic_status": "Khó khăn",
    },
    "SV002": {
        "name": "Trần Thị B",
        "class": "CA3",
        "policy": "Có",
        "economic_status": "Ổn định",
    }
}
```

**Đặc trưng dùng để tính điểm rủi ro:**

```python
features = {
    "SV001": {
        "gpa": 1.8,
        "failed": 4,
        "absent_rate": 0.38,
        "tuition_debt": 9000000,
        "activity_score": 12,
        "credit_progress": 0.40,
        "days_no_advisor": 95
    },
    "SV002": {
        "gpa": 3.2,
        "failed": 0,
        "absent_rate": 0.05,
        "tuition_debt": 0,
        "activity_score": 85,
        "credit_progress": 0.95,
        "days_no_advisor": 10
    }
}
```

 **Dữ liệu chuỗi thời gian:**

```python
time_series = {
    "SV001": {
        "semester": ["20241", "20242", "20251", "20252"],
        "gpa": [3.2, 2.8, 2.2, 2.0],
        "failed": [0, 1, 3, 4],
        "absent_rate": [0.05, 0.12, 0.25, 0.38]
    }
}
```

 **Đồ thị quan hệ xã hội:**

```python
social_graph = {
    "SV001": ["SV002", "SV003"],
    "SV002": ["SV001", "SV003"],
    "SV003": ["SV001", "SV002"],
    "SV004": ["SV005"],
    "SV005": ["SV004"],
    "SV006": []
}
```

**Hàng đợi ưu tiên cảnh báo:**

```python
alerts = [
    ("SV001", 100),
    ("SV002", 25),
    ("SV003", 68),
    ("SV004", 88)
]
```
---


## 5. Cấu trúc dữ liệu đề xuất

Hệ thống cảnh báo sớm sinh viên thôi học không nên chỉ sử dụng một cấu trúc dữ liệu duy nhất, vì bài toán bao gồm nhiều loại dữ liệu và nhiều thao tác khác nhau: tra cứu hồ sơ, tính điểm rủi ro, phân tích xu hướng học tập, phân tích quan hệ xã hội và xếp hạng cảnh báo để can thiệp.

Do đó, hệ thống được thiết kế theo hướng phân tầng:

```text
Tầng lưu trữ:
   - Cơ sở dữ liệu quan hệ

Tầng xử lý:
   - Bảng băm
   - Ma trận đặc trưng
   - Mảng chuỗi thời gian
   - Đồ thị danh sách kề

Tầng điều phối cảnh báo:
   - Heap / hàng đợi ưu tiên
   - Tập hợp chống trùng cảnh báo
```

---

### 5.1. Cơ sở dữ liệu quan hệ

Cơ sở dữ liệu quan hệ lưu trữ dữ liệu gốc của nhà trường: thông tin sinh viên, lớp học, môn học, điểm số, chuyên cần, học phí, hoạt động ngoại khóa và các sự kiện hỗ trợ.

Các thực thể chính:

```text
students, semesters, courses, enrollments, grades, attendance,
finance, support_events, risk_scores, alerts, interventions, feedback
```

**Vai trò:**

- Lưu trữ dữ liệu có cấu trúc.
- Dễ truy vấn theo sinh viên, học kỳ, môn học.
- Đảm bảo tính toàn vẹn dữ liệu.
- Tích hợp với hệ thống quản lý đào tạo hiện có.

**Ví dụ mối quan hệ:**

- Một sinh viên có nhiều kết quả học tập theo từng học kỳ.
- Một sinh viên có nhiều bản ghi chuyên cần.
- Một sinh viên có nhiều khoản học phí.
- Một sinh viên có thể nhận nhiều cảnh báo và được can thiệp nhiều lần.

Tuy nhiên, cơ sở dữ liệu quan hệ chủ yếu thuộc **tầng lưu trữ**. Phần xử lý và tính toán sẽ dùng các cấu trúc dữ liệu phù hợp với giải thuật hơn: bảng băm, ma trận đặc trưng, mảng chuỗi thời gian, đồ thị và heap.

---

### 5.2. Bảng băm — tra cứu hồ sơ sinh viên

#### Bài toán

Hệ thống cần tra cứu nhanh hồ sơ sinh viên theo mã sinh viên:

```text
Nhập MSSV = "SV001"
Trả về hồ sơ của sinh viên SV001
```

Với hàng nghìn hoặc hàng chục nghìn sinh viên, duyệt tuần tự qua danh sách sẽ chậm. Bảng băm là cấu trúc phù hợp.

#### Cấu trúc dữ liệu

Bảng băm — trong Python cài đặt bằng `dict`.

- **Khóa:** mã sinh viên
- **Giá trị:** hồ sơ sinh viên

#### Ví dụ

```python
students = {
    "SV001": {
        "name": "Nguyễn Văn A",
        "class": "CA3",
        "gpa": 1.8,
        "failed": 4,
        "absent_rate": 0.38,
        "tuition_debt": 9000000,
        "activity_score": 12
    },
    "SV002": {
        "name": "Trần Thị B",
        "class": "CA3",
        "gpa": 3.2,
        "failed": 0,
        "absent_rate": 0.05,
        "tuition_debt": 0,
        "activity_score": 85
    }
}

def get_student(mssv):
    return students.get(mssv)
```

#### Độ phức tạp

| Thao tác | Độ phức tạp trung bình |
|----------|------------------------|
| Tra cứu theo MSSV | `O(1)` |
| Thêm sinh viên | `O(1)` |
| Cập nhật hồ sơ | `O(1)` |
| Xóa sinh viên | `O(1)` |

#### Vì sao chọn bảng băm?

Hệ thống thường xuyên tra cứu hồ sơ theo mã sinh viên — thao tác đọc nhiều hơn ghi. Bảng băm cho phép tra cứu nhanh hơn mảng hoặc danh sách liên kết.

---

### 5.3. Ma trận đặc trưng — tính điểm rủi ro

#### Bài toán

Từ dữ liệu gốc, hệ thống cần tạo bảng đặc trưng để tính điểm rủi ro.

| Đặc trưng | Ý nghĩa |
|-----------|---------|
| GPA | Điểm trung bình học kỳ |
| Số môn rớt | Số học phần không đạt |
| Tỷ lệ vắng học | Mức độ chuyên cần |
| Nợ học phí | Áp lực tài chính |
| Điểm rèn luyện | Mức độ tham gia hoạt động |
| Tiến độ tín chỉ | So với yêu cầu chương trình |
| Số ngày không liên hệ cố vấn | Mức độ kết nối với hệ thống hỗ trợ |

#### Cấu trúc dữ liệu

Ma trận hai chiều — trong Python dùng `list[list]`, kích thước `N × F`:

- `N` = số sinh viên
- `F` = số đặc trưng

Mỗi dòng là một sinh viên trong một học kỳ; mỗi cột là một đặc trưng rủi ro.

#### Ví dụ

```python
mssv_list = ["SV001", "SV002", "SV003"]

feature_matrix = [
    [1.8, 4, 0.38, 9000000, 12, 0.40, 95],
    [3.2, 0, 0.05, 0,       85, 0.95, 10],
    [2.4, 2, 0.22, 4000000, 35, 0.65, 70]
]

feature_names = [
    "gpa", "failed", "absent_rate", "tuition_debt",
    "activity_score", "credit_progress", "days_no_advisor"
]
```

Ý nghĩa: `feature_matrix[0]` là đặc trưng của SV001, `feature_matrix[1]` là của SV002, v.v.

#### Độ phức tạp

| Thao tác | Độ phức tạp |
|----------|-------------|
| Xây dựng ma trận đặc trưng | `O(N·F)` |
| Truy cập đặc trưng của một sinh viên | `O(1)` |
| Tính điểm rủi ro cho một sinh viên | `O(R)` |
| Tính điểm rủi ro cho N sinh viên | `O(N·R)` |

Trong đó `R` = số luật trong rule-based scoring.

#### Vì sao chọn ma trận đặc trưng?

Dữ liệu tính điểm rủi ro có dạng bảng `sinh viên × đặc trưng`. Ma trận giúp dễ duyệt từng sinh viên, dễ tính toán hàng loạt, dễ đưa vào hàm tính điểm và dễ mở rộng nếu sau này dùng học máy.

---

### 5.4. Mảng chuỗi thời gian — phát hiện xu hướng

#### Bài toán

Sinh viên không nên chỉ được đánh giá tại một thời điểm. Hệ thống cần theo dõi dữ liệu qua nhiều học kỳ để phát hiện xu hướng xấu:

```text
Học kỳ 1: GPA = 3.2
Học kỳ 2: GPA = 2.8
Học kỳ 3: GPA = 2.2
Học kỳ 4: GPA = 2.0
```

GPA giảm liên tục là tín hiệu rủi ro quan trọng.

#### Cấu trúc dữ liệu

Mảng một chiều lưu dữ liệu theo thứ tự thời gian — trong Python dùng `list`. Ngoài ra dùng thêm **mảng tổng tiền tố** và **cửa sổ trượt**.

#### Ví dụ

```python
time_series = {
    "SV001": {
        "semester": ["20241", "20242", "20251", "20252"],
        "gpa": [3.2, 2.8, 2.2, 2.0],
        "failed": [0, 1, 3, 4],
        "absent_rate": [0.05, 0.12, 0.25, 0.38]
    }
}
```

#### Phát hiện GPA giảm liên tiếp

```python
def longest_decreasing_streak(values):
    best = 0
    current = 0
    for i in range(1, len(values)):
        if values[i] < values[i - 1]:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
```

```python
gpa_history = [3.2, 2.8, 2.2, 2.0]
print(longest_decreasing_streak(gpa_history))  # 3
```

→ GPA giảm liên tiếp qua 3 lần.

#### Tính trung bình bằng mảng tổng tiền tố

```python
def build_prefix_sum(values):
    prefix = [0]
    total = 0
    for value in values:
        total += value
        prefix.append(total)
    return prefix


def range_average(prefix, left, right):
    if left < 0 or right >= len(prefix) - 1 or left > right:
        return None
    total = prefix[right + 1] - prefix[left]
    count = right - left + 1
    return total / count
```

```python
gpa_history = [3.2, 2.8, 2.2, 2.0]
prefix = build_prefix_sum(gpa_history)
print(range_average(prefix, 1, 3))  # 2.3333...
```

#### Độ phức tạp

Gọi `T` = số học kỳ.

| Thao tác | Độ phức tạp |
|----------|-------------|
| Lưu chuỗi thời gian | `O(T)` |
| Dựng mảng tổng tiền tố | `O(T)` |
| Tính trung bình một đoạn | `O(1)` sau tiền xử lý |
| Đếm số kỳ GPA giảm liên tiếp | `O(T)` |
| Tính mức giảm trong w kỳ gần nhất | `O(1)` nếu truy cập trực tiếp |

#### Vì sao chọn mảng chuỗi thời gian?

Dữ liệu học tập có tính thời gian: `GPA kỳ 1 → kỳ 2 → kỳ 3 → ...`. Mảng chuỗi thời gian giúp phát hiện GPA giảm dần, số môn rớt tăng dần, tỷ lệ vắng tăng dần, nợ học phí kéo dài, điểm rèn luyện giảm dần.

---

### 5.5. Đồ thị danh sách kề — phân tích quan hệ xã hội

#### Bài toán

Hệ thống cần phân tích mối quan hệ giữa sinh viên với các thực thể khác trong môi trường học đường.

- **Đỉnh:** sinh viên, lớp học, câu lạc bộ, giảng viên, cố vấn học tập, nhóm học tập.
- **Cạnh:** học cùng lớp, tham gia cùng câu lạc bộ, được cố vấn bởi, học nhóm cùng nhau.

**Ứng dụng:**

- Phát hiện sinh viên bị cô lập.
- Phát hiện nhóm bạn có cùng nguy cơ bỏ học.
- Phân tích ảnh hưởng xã hội.
- Đánh giá mức độ kết nối với cộng đồng học tập.

#### Cấu trúc dữ liệu

Đồ thị danh sách kề — trong Python dùng `dict[list]` hoặc `defaultdict(list)`.

#### Ví dụ

```python
social_graph = {
    "SV001": ["SV002", "SV003"],
    "SV002": ["SV001", "SV003"],
    "SV003": ["SV001", "SV002"],
    "SV004": ["SV005"],
    "SV005": ["SV004"],
    "SV006": []
}
```

Ý nghĩa: SV001 quan hệ với SV002 và SV003; SV004 quan hệ với SV005; SV006 không có quan hệ nào.

#### BFS phát hiện thành phần liên thông

```python
from collections import deque


def component_size(start, graph):
    visited = {start}
    queue = deque([start])
    size = 0

    while queue:
        u = queue.popleft()
        size += 1
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)

    return size
```

```python
print(component_size("SV001", social_graph))  # 3
print(component_size("SV006", social_graph))  # 1
```

SV001, SV002, SV003 nằm trong cùng một nhóm liên thông (kích thước 3); SV006 cô lập (kích thước 1).

#### Độ phức tạp

Gọi `V` = số đỉnh, `E` = số cạnh.

| Thao tác | Độ phức tạp |
|----------|-------------|
| Duyệt đồ thị bằng BFS | `O(V + E)` |
| Duyệt đồ thị bằng DFS | `O(V + E)` |
| Tìm thành phần liên thông | `O(V + E)` |
| Đếm số bạn của một sinh viên | `O(1)` nếu đã lưu danh sách kề |

#### Vì sao chọn danh sách kề?

Đồ thị quan hệ sinh viên thường là **đồ thị thưa** — mỗi sinh viên chỉ có một số quan hệ nhất định, không kết nối với tất cả sinh viên khác.

Nếu dùng ma trận kề `V × V` với 20.000 sinh viên: `20.000 × 20.000 = 400.000.000 ô nhớ` — rất tốn bộ nhớ. Danh sách kề chỉ lưu các quan hệ thật sự tồn tại, tiết kiệm hơn và phù hợp hơn.

---

### 5.6. Heap / hàng đợi ưu tiên — cảnh báo

#### Bài toán

Khi hệ thống tạo ra nhiều cảnh báo, cần ưu tiên xử lý sinh viên có điểm rủi ro cao nhất.

| Sinh viên | Điểm rủi ro |
|-----------|-------------|
| SV_A | 92 |
| SV_C | 88 |
| SV_B | 61 |
| SV_D | 35 |

Cần lấy `SV_A` ra trước.

#### Cấu trúc dữ liệu

Heap nhị phân — trong Python dùng `heapq`. Lưu ý `heapq` mặc định là **min-heap**; muốn lấy phần tử lớn nhất, lưu số âm (`-score`).

#### Ví dụ

```python
import heapq

alerts = [("SV_A", 92), ("SV_C", 88), ("SV_B", 61), ("SV_D", 35)]

heap = [(-score, mssv) for mssv, score in alerts]
heapq.heapify(heap)

while heap:
    neg_score, mssv = heapq.heappop(heap)
    print(mssv, -neg_score)
```

Kết quả:

```text
SV_A 92
SV_C 88
SV_B 61
SV_D 35
```

#### Bài toán top-k

Nếu cần chọn `k` sinh viên rủi ro cao nhất từ danh sách lớn:

- Sắp xếp toàn bộ: `O(N log N)`
- Heap top-k: `O(N log k)`

Vì `k` nhỏ hơn `N` rất nhiều, heap top-k hiệu quả hơn.

```python
import heapq


def top_k_alerts(alerts, k):
    heap = []
    for mssv, score in alerts:
        if len(heap) < k:
            heapq.heappush(heap, (score, mssv))
        elif score > heap[0][0]:
            heapq.heapreplace(heap, (score, mssv))
    return [(mssv, score) for score, mssv in sorted(heap, reverse=True)]
```

```python
alerts = [("SV_A", 92), ("SV_C", 88), ("SV_B", 61), ("SV_D", 35)]
for mssv, score in top_k_alerts(alerts, 2):
    print(mssv, score)
```

Kết quả:

```text
SV_A 92
SV_C 88
```

#### Độ phức tạp

| Thao tác | Độ phức tạp |
|----------|-------------|
| Thêm cảnh báo vào heap | `O(log N)` |
| Lấy cảnh báo ưu tiên cao nhất | `O(log N)` |
| Chọn top-k bằng heap | `O(N log k)` |
| Sắp xếp toàn bộ danh sách | `O(N log N)` |
| Cập nhật điểm rủi ro trong indexed heap | `O(log N)` |

#### Vì sao chọn heap?

Heap phù hợp vì hệ thống cần: lấy sinh viên rủi ro cao nhất ra xử lý trước, thêm cảnh báo mới, cập nhật điểm rủi ro, chọn top-k sinh viên nguy cấp. Heap hiệu quả hơn danh sách thường hoặc danh sách liên kết trong các thao tác ưu tiên.

---

### 5.7. Tập hợp — chống trùng cảnh báo

#### Bài toán

Một sinh viên trong một học kỳ chỉ nên có một cảnh báo đang mở. Nếu hệ thống tạo cảnh báo nhiều lần, cố vấn học tập sẽ bị trùng thông tin.

```text
SV001 đã có cảnh báo trong học kỳ 20252
→ Không nên tạo thêm cảnh báo mới cho SV001 trong cùng kỳ đó
```

#### Cấu trúc dữ liệu

Tập hợp — trong Python dùng `set`.

#### Ví dụ

```python
opened_alerts = {"SV001", "SV004"}

def should_create_alert(mssv):
    return mssv not in opened_alerts

print(should_create_alert("SV001"))  # False
print(should_create_alert("SV007"))  # True
```

#### Độ phức tạp

| Thao tác | Độ phức tạp trung bình |
|----------|------------------------|
| Kiểm tra đã có cảnh báo chưa | `O(1)` |
| Thêm cảnh báo | `O(1)` |
| Xóa cảnh báo | `O(1)` |

---

### 5.8. Bảng tổng hợp cấu trúc dữ liệu

| Bài toán | Cấu trúc dữ liệu | Python tương ứng | Độ phức tạp |
|----------|------------------|------------------|-------------|
| Tra cứu hồ sơ sinh viên | Bảng băm | `dict` | `O(1)` trung bình |
| Lưu đặc trưng tính điểm | Ma trận hai chiều | `list[list]` | `O(N·F)` để xây dựng |
| Tính điểm rủi ro | Mảng luật | `list` | `O(R)` mỗi sinh viên |
| Lưu GPA theo học kỳ | Mảng chuỗi thời gian | `list` | `O(T)` |
| Tính trung bình theo khoảng kỳ | Mảng tổng tiền tố | `list` | `O(1)` truy vấn |
| Phát hiện GPA giảm liên tiếp | Duyệt mảng | `list` | `O(T)` |
| Phân tích quan hệ xã hội | Đồ thị danh sách kề | `dict[list]` | `O(V + E)` |
| Phát hiện sinh viên cô lập | BFS / DFS | `deque` | `O(V + E)` |
| Chọn top-k sinh viên rủi ro cao nhất | Heap | `heapq` | `O(N log k)` |
| Lấy cảnh báo ưu tiên cao nhất | Heap | `heapq` | `O(log N)` |
| Cập nhật điểm rủi ro động | Indexed heap | Tự viết | `O(log N)` |
| Chống trùng cảnh báo | Tập hợp | `set` | `O(1)` trung bình |

---

### 5.9. Kết luận về cấu trúc dữ liệu

Hệ thống không sử dụng một cấu trúc dữ liệu duy nhất. Mỗi cấu trúc được chọn để giải quyết một bài toán cụ thể:

```text
Bảng băm        → tra cứu sinh viên theo MSSV
Ma trận 2 chiều → lưu đặc trưng tính điểm rủi ro
Mảng thời gian  → phát hiện xu hướng giảm GPA, tăng vắng học
Đồ thị kề       → phát hiện sinh viên cô lập
Heap            → xếp hạng cảnh báo và chọn top-k
Set             → chống trùng cảnh báo
```

Giá trị của việc lựa chọn đúng cấu trúc dữ liệu là giúp hệ thống: tra cứu nhanh hồ sơ sinh viên, tính điểm rủi ro hiệu quả, phát hiện sớm xu hướng suy giảm, phân tích quan hệ xã hội, ưu tiên can thiệp đúng sinh viên, tránh cảnh báo trùng lặp và có thể mở rộng khi số lượng sinh viên tăng lên.

---

## 6. Giải thuật đề xuất

Hệ thống cảnh báo sớm sinh viên thôi học không nên chỉ sử dụng một giải thuật duy nhất. Bài toán gồm nhiều công việc khác nhau: tính điểm rủi ro, phát hiện xu hướng học tập, phân tích quan hệ xã hội, xếp hạng cảnh báo và cập nhật cảnh báo theo thời gian.

Vì vậy, giải thuật đề xuất được chia thành các nhóm sau:

```text
1. Giải thuật tính điểm rủi ro bằng luật
2. Giải thuật xếp hạng và chọn top-k sinh viên rủi ro cao nhất
3. Giải thuật phát hiện xu hướng giảm theo chuỗi thời gian
4. Giải thuật phát hiện sinh viên bị cô lập bằng đồ thị
5. Giải thuật cập nhật hàng đợi cảnh báo động
6. Hướng mở rộng: học máy hoặc mô hình kết hợp
```

---

### 6.1. Giải thuật tính điểm rủi ro bằng luật

#### Mục tiêu

Tính điểm rủi ro thôi học cho từng sinh viên dựa trên các đặc trưng học tập, chuyên cần, tài chính, hoạt động và kết nối với cố vấn học tập.

#### Đầu vào

- Vector đặc trưng của sinh viên.
- Danh sách các luật rủi ro.

Ví dụ đặc trưng: `GPA`, số môn rớt, tỷ lệ vắng học, nợ học phí, điểm rèn luyện, tiến độ tín chỉ, số ngày không liên hệ cố vấn học tập.

#### Đầu ra

```text
1. Điểm rủi ro từ 0 đến 100
2. Danh sách lý do khiến sinh viên có nguy cơ
```

#### Ý tưởng giải thuật

Sử dụng **rule-based scoring**. Mỗi luật gồm:

```text
- Điều kiện
- Trọng số điểm
- Lý do cảnh báo
```

Giải thuật duyệt qua toàn bộ danh sách luật. Nếu sinh viên thỏa mãn một luật, hệ thống cộng điểm rủi ro tương ứng. Cuối cùng, điểm rủi ro được chặn tối đa ở 100.

#### Công thức

```text
risk_score = min(100, tổng điểm của các luật được kích hoạt)
```

#### Ví dụ bộ luật

| Điều kiện | Điểm cộng |
|-----------|-----------|
| GPA dưới 2.0 | +30 |
| GPA từ 2.0 đến dưới 2.5 | +20 |
| GPA từ 2.5 đến dưới 3.0 | +10 |
| Số môn rớt từ 4 trở lên | +25 |
| Số môn rớt từ 2 đến 3 | +15 |
| Có 1 môn rớt | +5 |
| Tỷ lệ vắng học trên 30% | +25 |
| Tỷ lệ vắng học từ 20% đến 30% | +15 |
| Tỷ lệ vắng học từ 10% đến dưới 20% | +5 |
| Nợ học phí trên 8 triệu đồng | +20 |
| Nợ học phí từ 3 triệu đến 8 triệu đồng | +10 |
| Điểm rèn luyện dưới 20 | +10 |
| Điểm rèn luyện từ 20 đến dưới 40 | +5 |
| Tiến độ tín chỉ dưới 50% | +15 |
| Hơn 90 ngày không liên hệ cố vấn | +10 |
| Từ 60 đến 90 ngày không liên hệ cố vấn | +5 |

#### Mã giả

```text
function compute_risk(feature):
    score = 0
    reasons = []

    for rule in rules:
        if rule.condition(feature):
            score = score + rule.weight
            reasons.append(rule.name)

    score = min(score, 100)
    return score, reasons
```

#### Cài đặt Python minh họa

```python
from dataclasses import dataclass


@dataclass
class Feature:
    gpa: float
    failed: int
    absent_rate: float
    tuition_debt: float
    activity_score: int
    credit_progress: float
    days_no_advisor: int


RULES = [
    ("GPA dưới 2.0", 30, lambda f: f.gpa < 2.0),
    ("GPA từ 2.0 đến dưới 2.5", 20, lambda f: 2.0 <= f.gpa < 2.5),
    ("GPA từ 2.5 đến dưới 3.0", 10, lambda f: 2.5 <= f.gpa < 3.0),

    ("Số môn rớt từ 4 trở lên", 25, lambda f: f.failed >= 4),
    ("Số môn rớt từ 2 đến 3", 15, lambda f: 2 <= f.failed <= 3),
    ("Có 1 môn rớt", 5, lambda f: f.failed == 1),

    ("Tỷ lệ vắng học trên 30%", 25, lambda f: f.absent_rate > 0.30),
    ("Tỷ lệ vắng học từ 20% đến 30%", 15, lambda f: 0.20 <= f.absent_rate <= 0.30),
    ("Tỷ lệ vắng học từ 10% đến dưới 20%", 5, lambda f: 0.10 <= f.absent_rate < 0.20),

    ("Nợ học phí trên 8 triệu", 20, lambda f: f.tuition_debt > 8_000_000),
    ("Nợ học phí từ 3 đến 8 triệu", 10, lambda f: 3_000_000 <= f.tuition_debt <= 8_000_000),

    ("Điểm rèn luyện dưới 20", 10, lambda f: f.activity_score < 20),
    ("Điểm rèn luyện từ 20 đến dưới 40", 5, lambda f: 20 <= f.activity_score < 40),

    ("Tiến độ tín chỉ dưới 50%", 15, lambda f: f.credit_progress < 0.50),

    ("Hơn 90 ngày không liên hệ cố vấn", 10, lambda f: f.days_no_advisor > 90),
    ("Từ 60 đến 90 ngày không liên hệ cố vấn", 5, lambda f: 60 < f.days_no_advisor <= 90),
]


def compute_risk(feature: Feature):
    score = 0
    reasons = []
    for rule_name, weight, condition in RULES:
        if condition(feature):
            score += weight
            reasons.append(rule_name)
    return min(score, 100), reasons
```

#### Ví dụ

```python
sv_a = Feature(
    gpa=1.8, failed=4, absent_rate=0.38,
    tuition_debt=9_000_000, activity_score=12,
    credit_progress=0.40, days_no_advisor=95
)

score, reasons = compute_risk(sv_a)
print(score)
print(reasons)
```

Kết quả:

```text
100
['GPA dưới 2.0', 'Số môn rớt từ 4 trở lên', 'Tỷ lệ vắng học trên 30%',
 'Nợ học phí trên 8 triệu', 'Điểm rèn luyện dưới 20',
 'Tiến độ tín chỉ dưới 50%', 'Hơn 90 ngày không liên hệ cố vấn']
```

#### Độ phức tạp

Gọi `R` = số luật.

| Thao tác | Độ phức tạp |
|----------|-------------|
| Tính điểm cho một sinh viên | `O(R)` |
| Tính điểm cho N sinh viên | `O(N·R)` |

#### Vì sao chọn giải thuật này?

Ưu điểm: dễ hiểu, dễ triển khai, dễ giải thích lý do cảnh báo, không cần dữ liệu lịch sử đã gán nhãn, phù hợp với giai đoạn đầu của hệ thống.

---

### 6.2. Giải thuật xếp hạng và chọn top-k sinh viên rủi ro cao nhất

#### Mục tiêu

Chọn ra `k` sinh viên có điểm rủi ro cao nhất để ưu tiên can thiệp. Ví dụ: `N = 20.000` sinh viên, `k = 50` sinh viên nguy cấp nhất.

#### Đầu vào

- Danh sách cảnh báo của N sinh viên dạng `(mssv, risk_score)`.
- Số lượng `k` sinh viên cần chọn.

#### Đầu ra

Danh sách k sinh viên có điểm rủi ro cao nhất, sắp xếp giảm dần theo điểm rủi ro.

#### Ý tưởng giải thuật

| Cách | Độ phức tạp | Nhận xét |
|------|-------------|----------|
| Sắp xếp toàn bộ danh sách | `O(N log N)` | Dễ, nhưng không tối ưu nếu k nhỏ |
| Dùng heap top-k | `O(N log k)` | Phù hợp khi k nhỏ hơn N nhiều |
| Quickselect | `O(N)` trung bình | Nhanh nhưng khó giải thích hơn |

Trong báo cáo này, giải thuật được đề xuất là: **dùng min-heap kích thước k** để chọn top-k sinh viên có điểm rủi ro cao nhất.

#### Ý tưởng của min-heap kích thước k

Duy trì một heap chứa `k` sinh viên có điểm cao nhất đã gặp. Khi duyệt một sinh viên mới:

- Nếu heap chưa đủ `k` phần tử, thêm vào heap.
- Nếu heap đã đủ `k` phần tử và điểm của sinh viên mới lớn hơn phần tử nhỏ nhất trong heap, thay phần tử nhỏ nhất đó bằng sinh viên mới.

Cuối cùng, heap chứa `k` sinh viên có điểm rủi ro cao nhất.

#### Mã giả

```text
function top_k_alerts(alerts, k):
    heap = empty min-heap

    for alert in alerts:
        if heap.size < k:
            heap.push(alert)
        else if alert.score > heap.min().score:
            heap.replace_min(alert)

    return heap sorted by score descending
```

#### Cài đặt Python

```python
import heapq


def top_k_alerts(alerts, k):
    if k <= 0:
        return []

    heap = []
    for mssv, score in alerts:
        item = (score, mssv)
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif score > heap[0][0]:
            heapq.heapreplace(heap, item)

    return [(mssv, score) for score, mssv in sorted(heap, reverse=True)]
```

#### Ví dụ

```python
alerts = [
    ("SV001", 92), ("SV002", 61), ("SV003", 100),
    ("SV004", 35), ("SV005", 88), ("SV006", 79),
]

for mssv, score in top_k_alerts(alerts, 3):
    print(mssv, score)
```

Kết quả:

```text
SV003 100
SV001 92
SV005 88
```

#### Độ phức tạp

Gọi `N` = số cảnh báo, `k` = số sinh viên cần chọn.

| Cách | Độ phức tạp |
|------|-------------|
| Sắp xếp toàn bộ | `O(N log N)` |
| Heap top-k | `O(N log k)` |

Vì trong thực tế `N` lớn, `k` nhỏ, nên heap top-k phù hợp hơn.

---

### 6.3. Giải thuật phát hiện xu hướng giảm theo chuỗi thời gian

#### Mục tiêu

Phát hiện sinh viên đang có xu hướng suy giảm học tập qua nhiều học kỳ:

```text
Học kỳ 1: GPA = 3.2
Học kỳ 2: GPA = 2.8
Học kỳ 3: GPA = 2.2
Học kỳ 4: GPA = 2.0
```

GPA giảm liên tục là tín hiệu rủi ro.

#### Đầu vào

Chuỗi giá trị theo thời gian của một sinh viên, ví dụ `gpa_history = [3.2, 2.8, 2.2, 2.0]`.

#### Đầu ra

```text
1. Số lần giảm liên tiếp dài nhất
2. Mức giảm trong w học kỳ gần nhất
3. Cờ cảnh báo xu hướng xấu
```

#### 6.3.1. Đếm chuỗi giảm liên tiếp

Duyệt mảng từ trái sang phải. Nếu giá trị hiện tại nhỏ hơn giá trị trước đó thì tăng độ dài chuỗi giảm; nếu không thì đặt lại về 0.

```python
def longest_decreasing_streak(values):
    best = 0
    current = 0
    for i in range(1, len(values)):
        if values[i] < values[i - 1]:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best
```

```python
gpa_history = [3.2, 2.8, 2.2, 2.0]
print(longest_decreasing_streak(gpa_history))  # 3
```

#### 6.3.2. Tính mức giảm trong w kỳ gần nhất

Với `w = 3` và `gpa_history = [3.2, 2.8, 2.2, 2.0]`:

```text
drop = gpa_history[-3] - gpa_history[-1] = 2.8 - 2.0 = 0.8
```

```python
def drop_over_last_window(values, window_size=3):
    if len(values) < window_size:
        return 0
    return values[-window_size] - values[-1]
```

#### 6.3.3. Cảnh báo xu hướng GPA giảm

Điều kiện: GPA giảm liên tiếp ít nhất 2 lần **và** mức giảm trong 3 kỳ gần nhất từ 0.5 trở lên.

```python
def has_gpa_decline_alert(values, window_size=3, min_drop=0.5, min_streak=2):
    streak = longest_decreasing_streak(values)
    drop = drop_over_last_window(values, window_size)
    return streak >= min_streak and drop >= min_drop
```

```python
gpa_history = [3.2, 2.8, 2.2, 2.0]
print(has_gpa_decline_alert(gpa_history))  # True
```

#### Độ phức tạp

Gọi `T` = số học kỳ.

| Bài toán | Độ phức tạp |
|----------|-------------|
| Đếm chuỗi giảm liên tiếp | `O(T)` |
| Tính mức giảm trong w kỳ gần nhất | `O(1)` nếu truy cập trực tiếp |
| Kiểm tra cảnh báo xu hướng | `O(T)` |

Nếu cần tính trung bình nhiều đoạn học kỳ, có thể dùng thêm mảng tổng tiền tố để truy vấn `O(1)` sau khi tiền xử lý `O(T)`.

---

### 6.4. Giải thuật phát hiện sinh viên bị cô lập bằng đồ thị

#### Mục tiêu

Phát hiện sinh viên có ít kết nối xã hội, có thể dẫn đến nguy cơ thôi học cao hơn.

#### Đầu vào

- Đồ thị quan hệ xã hội.
- Điểm rủi ro của sinh viên.

Đồ thị có thể gồm:

```text
Đỉnh: sinh viên, lớp học, câu lạc bộ, nhóm học tập, cố vấn học tập
Cạnh: học cùng lớp, tham gia câu lạc bộ, học nhóm, được cố vấn
```

#### Đầu ra

Danh sách sinh viên có nguy cơ cao và bị cô lập.

#### Ý tưởng giải thuật

Sử dụng đồ thị danh sách kề và duyệt BFS hoặc DFS. Một sinh viên được xem là đáng chú ý nếu:

```text
1. Có điểm rủi ro cao
2. Có bậc đỉnh thấp
3. Thuộc thành phần liên thông nhỏ
```

Ví dụ điều kiện: `risk_score >= 60`, `degree <= 1`, `component_size <= 3`.

#### Cài đặt Python

```python
from collections import deque


def component_size(start, graph):
    visited = {start}
    queue = deque([start])
    size = 0
    while queue:
        u = queue.popleft()
        size += 1
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return size


def is_isolated_high_risk(mssv, graph, risk_scores,
                          risk_threshold=60,
                          max_degree=1,
                          max_component_size=3):
    score = risk_scores.get(mssv, 0)
    degree = len(graph.get(mssv, []))
    size = component_size(mssv, graph)
    return (
        score >= risk_threshold
        and degree <= max_degree
        and size <= max_component_size
    )
```

#### Ví dụ

```python
social_graph = {
    "SV001": ["SV002", "SV003"], "SV002": ["SV001", "SV003"],
    "SV003": ["SV001", "SV002"], "SV004": ["SV005"],
    "SV005": ["SV004"], "SV006": []
}

risk_scores = {
    "SV001": 85, "SV002": 40, "SV003": 55,
    "SV004": 70, "SV005": 65, "SV006": 90,
}

print(is_isolated_high_risk("SV006", social_graph, risk_scores))  # True
```

`SV006` có điểm rủi ro 90, không có quan hệ nào, thành phần liên thông chỉ có 1 đỉnh.

#### Độ phức tạp

Gọi `V` = số đỉnh, `E` = số cạnh.

| Thao tác | Độ phức tạp |
|----------|-------------|
| BFS / DFS một thành phần | `O(V + E)` |
| Tính bậc đỉnh | `O(1)` nếu đã lưu danh sách kề |
| Kiểm tra cô lập cho một sinh viên | `O(V + E)` nếu tính lại thành phần liên thông |

Nếu cần kiểm tra cho nhiều sinh viên, nên duyệt đồ thị **một lần** để tính kích thước thành phần liên thông cho tất cả đỉnh. Khi đó độ phức tạp tổng là `O(V + E)`.

---

### 6.5. Giải thuật cập nhật hàng đợi cảnh báo động

#### Mục tiêu

Trong hệ thống thực tế, điểm rủi ro của sinh viên có thể thay đổi theo thời gian. Ví dụ SV001 đang có risk score = 60, sau đó phát hiện vắng thêm nhiều buổi, risk score tăng lên 85. Hệ thống cần cập nhật ưu tiên của SV001 trong hàng đợi cảnh báo.

#### Đầu vào

- Hàng đợi cảnh báo hiện tại.
- Điểm rủi ro mới của một sinh viên.

#### Đầu ra

Hàng đợi cảnh báo đã được cập nhật theo điểm rủi ro mới.

#### Cách 1: Heap với xóa lười (lazy deletion)

Ý tưởng:

- Mỗi lần điểm rủi ro thay đổi, thêm một bản ghi mới vào heap.
- Khi lấy cảnh báo ra, kiểm tra bản ghi đó còn hợp lệ không.
- Nếu điểm trong heap không khớp với điểm hiện tại của sinh viên, bỏ qua bản ghi đó.

Ưu điểm: dễ cài đặt, không cần sửa phần tử nằm giữa heap.
Nhược điểm: heap có thể chứa nhiều bản ghi cũ, cần kiểm tra hợp lệ khi lấy cảnh báo.

```python
import heapq


class AlertQueueLazy:
    def __init__(self):
        self.heap = []
        self.current_scores = {}

    def push(self, mssv, score):
        self.current_scores[mssv] = score
        heapq.heappush(self.heap, (-score, mssv))

    def update(self, mssv, new_score):
        self.push(mssv, new_score)

    def pop_valid(self):
        while self.heap:
            neg_score, mssv = heapq.heappop(self.heap)
            score = -neg_score
            if self.current_scores.get(mssv) == score:
                return mssv, score
        return None
```

#### Cách 2: Indexed heap

Ý tưởng:

- Heap lưu các sinh viên theo điểm rủi ro.
- Bảng băm lưu vị trí của từng sinh viên trong heap.
- Khi điểm rủi ro thay đổi, cập nhật trực tiếp phần tử trong heap rồi sắp xếp lại heap.

Ưu điểm: không tạo bản ghi cũ, cập nhật hiệu quả, phù hợp hơn nếu muốn trình bày sâu về cấu trúc dữ liệu.

Mã giả:

```text
IndexedMaxHeap:
    heap: array of (score, mssv)
    position: dictionary mssv -> index

function push_or_update(mssv, new_score):
    if mssv not in position:
        add (new_score, mssv) to heap
        position[mssv] = last_index
        sift_up(last_index)
    else:
        i = position[mssv]
        old_score = heap[i].score
        heap[i].score = new_score
        if new_score > old_score:
            sift_up(i)
        else if new_score < old_score:
            sift_down(i)

function extract_max():
    swap root with last element
    remove last element
    delete position of removed mssv
    sift_down(root)
    return removed element
```

#### Độ phức tạp

| Thao tác | Độ phức tạp |
|----------|-------------|
| Thêm cảnh báo | `O(log N)` |
| Cập nhật điểm rủi ro | `O(log N)` |
| Lấy cảnh báo ưu tiên cao nhất | `O(log N)` |
| Tra cứu vị trí theo MSSV | `O(1)` nhờ bảng băm |

---

### 6.6. Hướng mở rộng: giải thuật học máy

Nếu nhà trường có dữ liệu lịch sử đủ lớn và có nhãn sinh viên thôi học, hệ thống có thể mở rộng bằng mô hình học máy.

- **Đầu vào:** vector đặc trưng của sinh viên.
- **Đầu ra:** xác suất thôi học.

Các mô hình có thể dùng:

| Mô hình | Đặc điểm |
|---------|----------|
| Logistic Regression | Đơn giản, dễ giải thích |
| Decision Tree | Trực quan, dễ hiểu |
| Random Forest | Mạnh, phù hợp dữ liệu bảng |
| Gradient Boosting | Hiệu suất cao |
| XGBoost / LightGBM | Phù hợp bài toán phân loại dữ liệu có cấu trúc |

**Ưu điểm:** tự học từ dữ liệu lịch sử, có thể phát hiện các mẫu phức tạp hơn luật thủ công, có thể cải thiện theo thời gian nếu có phản hồi can thiệp.

**Nhược điểm:** cần dữ liệu lịch sử đủ lớn, dữ liệu thôi học thường mất cân bằng, kết quả khó giải thích hơn rule-based, cần đánh giá bằng precision, recall, F1-score, PR-AUC, top-k recall.

**Mô hình kết hợp:** hướng thực tế là kết hợp rule-based và học máy.

```text
final_risk_score = 0.6 * ml_risk_score + 0.4 * rule_based_risk_score
```

Hoặc dùng luật để hiệu chỉnh:

```text
Nếu sinh viên nợ học phí nghiêm trọng hoặc vắng học quá cao,
nâng mức cảnh báo lên ít nhất mức CAO.
```

Tuy nhiên, trong phạm vi môn Cấu trúc dữ liệu và Giải thuật, phần học máy chỉ nên xem là hướng mở rộng. Phần trọng tâm vẫn nên là: rule-based scoring, heap / top-k, chuỗi thời gian, đồ thị, hàng đợi ưu tiên.

---

### 6.7. Bảng tổng hợp giải thuật đề xuất

| Giải thuật | Mục tiêu | Cấu trúc dữ liệu | Độ phức tạp |
|------------|----------|------------------|-------------|
| Rule-based scoring | Tính điểm rủi ro | Mảng luật | `O(R)` mỗi sinh viên |
| Tính điểm hàng loạt | Tính điểm cho N sinh viên | Ma trận đặc trưng | `O(N·R)` |
| Top-k bằng heap | Chọn k sinh viên rủi ro cao nhất | Min-heap kích thước k | `O(N log k)` |
| Sắp xếp danh sách cảnh báo | Xếp hạng toàn bộ | Mảng | `O(N log N)` |
| Đếm chuỗi giảm GPA | Phát hiện xu hướng giảm | Mảng chuỗi thời gian | `O(T)` |
| Prefix sum | Tính trung bình theo đoạn học kỳ | Mảng tổng tiền tố | `O(T)` tiền xử lý, `O(1)` truy vấn |
| BFS / DFS | Phát hiện sinh viên cô lập | Đồ thị danh sách kề | `O(V + E)` |
| Indexed heap | Cập nhật điểm rủi ro động | Heap + bảng băm | `O(log N)` |
| Lazy heap | Cập nhật cảnh báo đơn giản hơn | Heap + dict | `O(log N)` mỗi lần đẩy |
| Machine learning | Dự đoán xác suất thôi học | Feature matrix | Phụ thuộc mô hình |

---

### 6.8. Quy trình giải thuật tổng thể

Hệ thống có thể được mô tả bằng quy trình sau:

```text
Bước 1: Thu thập dữ liệu sinh viên
Bước 2: Trích xuất đặc trưng
Bước 3: Tính điểm rủi ro bằng luật
Bước 4: Phân tích chuỗi thời gian
Bước 5: Phân tích đồ thị quan hệ xã hội
Bước 6: Tổng hợp điểm rủi ro
Bước 7: Lọc cảnh báo trùng
Bước 8: Đưa cảnh báo vào heap
Bước 9: Chọn top-k sinh viên ưu tiên can thiệp
Bước 10: Ghi nhận can thiệp và cập nhật mô hình
```

Mã giả tổng thể:

```text
function run_alert_system(students, k):
    alerts = []
    opened_alerts = empty set

    for student in students:
        features = extract_features(student)
        risk_score, reasons = compute_risk(features)

        trend_alert = analyze_time_series(features.gpa_history)
        social_alert = analyze_social_graph(student.mssv)

        if trend_alert:
            risk_score = min(100, risk_score + 10)
            reasons.append("GPA có xu hướng giảm liên tục")

        if social_alert:
            risk_score = min(100, risk_score + 10)
            reasons.append("Sinh viên có dấu hiệu bị cô lập")

        if risk_score >= ALERT_THRESHOLD:
            if student.mssv not in opened_alerts:
                alerts.append((student.mssv, risk_score))
                opened_alerts.add(student.mssv)

    top_alerts = top_k_alerts(alerts, k)
    return top_alerts
```

---

### 6.9. Đề xuất phạm vi cho báo cáo cá nhân

Nếu đây là báo cáo cá nhân môn Cấu trúc dữ liệu và Giải thuật, nên chọn các giải thuật sau để cài đặt minh họa:

```text
1. Rule-based scoring
2. Top-k bằng heap
3. Phát hiện GPA giảm bằng mảng chuỗi thời gian
4. Phát hiện sinh viên cô lập bằng BFS trên đồ thị
5. Hàng đợi ưu tiên hoặc indexed heap
```

Các phần như machine learning, XGBoost, Random Forest, deep learning chỉ nên để ở mục hướng phát triển, không nên làm trọng tâm.

---

### 6.10. Kết luận phần giải thuật

Giải thuật đề xuất của hệ thống không chỉ là một mô hình dự đoán duy nhất, mà là một quy trình kết hợp nhiều giải thuật:

```text
Tính điểm rủi ro bằng luật
Phân tích xu hướng bằng mảng chuỗi thời gian
Phân tích cô lập bằng đồ thị danh sách kề
Xếp hạng cảnh báo bằng heap
Cập nhật cảnh báo bằng hàng đợi ưu tiên
```

Cách tiếp cận này giúp hệ thống: dễ giải thích, dễ triển khai, phù hợp với dữ liệu giáo dục, tận dụng được các cấu trúc dữ liệu và giải thuật cơ bản, và có thể mở rộng sang học máy trong tương lai.

> **Tóm tắt:** Hệ thống đề xuất sử dụng giải thuật rule-based scoring để tính điểm rủi ro cho từng sinh viên. Sau đó, heap được sử dụng để xếp hạng cảnh báo và chọn top-k sinh viên cần ưu tiên can thiệp. Mảng chuỗi thời gian được dùng để phát hiện xu hướng giảm GPA hoặc tăng tỷ lệ vắng học. Đồ thị danh sách kề được dùng để phát hiện sinh viên bị cô lập. Hướng mở rộng của hệ thống là kết hợp với mô hình học máy nếu có đủ dữ liệu lịch sử.

---

## 7. Kiến trúc hệ thống

Kiến trúc đề xuất gồm các tầng sau:

```text
Nguồn dữ liệu
   ↓
Thu thập và làm sạch dữ liệu
   ↓
Cơ sở dữ liệu quan hệ / Data warehouse
   ↓
Feature engineering
   ↓
Mô hình tính điểm rủi ro
   ↓
Hệ thống cảnh báo
   ↓
Dashboard cho cố vấn học tập
   ↓
Can thiệp và phản hồi
   ↓
Cập nhật mô hình
```

### Giải thích từng tầng

#### Tầng 1: Nguồn dữ liệu

Bao gồm dữ liệu từ:

- Phòng đào tạo.
- Phòng công tác sinh viên.
- Hệ thống điểm danh.
- Hệ thống tài chính.
- Portal sinh viên.
- Câu lạc bộ và hoạt động ngoại khóa.

#### Tầng 2: Thu thập và làm sạch dữ liệu

Xử lý:

- Giá trị thiếu.
- Dữ liệu trùng.
- Sai định dạng.
- Ngoại lai không hợp lệ.
- Dữ liệu bất thường.

#### Tầng 3: Lưu trữ dữ liệu

Dùng cơ sở dữ liệu quan hệ để lưu dữ liệu gốc và các bảng nghiệp vụ.

#### Tầng 4: Tạo đặc trưng

Chuyển dữ liệu quan hệ thành feature matrix, bao gồm:

- Đặc trưng hiện tại.
- Đặc trưng xu hướng.
- Đặc trưng quan hệ xã hội nếu có.

#### Tầng 5: Tính điểm rủi ro

Sử dụng rule-based scoring, machine learning hoặc hybrid.

#### Tầng 6: Cảnh báo

Phân loại mức rủi ro và đưa vào hàng đợi ưu tiên.

#### Tầng 7: Can thiệp

Cố vấn học tập, phòng công tác sinh viên và giảng viên bộ môn thực hiện hành động hỗ trợ.

#### Tầng 8: Phản hồi

Ghi nhận kết quả can thiệp để cải thiện mô hình và quy trình.

---

## 8. Quy trình cảnh báo và can thiệp

### 8.1. Đầu ra của hệ thống

Hệ thống không nên chỉ trả về một con số rủi ro. Đầu ra cần bao gồm:

- Mã sinh viên.
- Học kỳ đánh giá.
- Điểm rủi ro.
- Mức cảnh báo.
- Các lý do chính.
- Hành động đề xuất.

Ví dụ một cảnh báo:

```text
Sinh viên: SV003
Học kỳ: 20261
Điểm rủi ro: 100/100
Mức cảnh báo: RẤT CAO

Lý do chính:
- GPA dưới 2.0
- Có từ 4 môn rớt trở lên
- Tỷ lệ vắng học trên 30%
- Nợ học phí trên 8 triệu đồng
- Điểm rèn luyện dưới 20
- Tiến độ tín chỉ dưới 50%
- Hơn 90 ngày không liên hệ cố vấn học tập

Hành động đề xuất:
- Can thiệp khẩn cấp trong tuần.
- Phòng công tác sinh viên phối hợp với cố vấn học tập.
- Kiểm tra tình trạng học phí và đề xuất hỗ trợ tài chính nếu cần.
- Cân nhắc tư vấn tâm lý hoặc hỗ trợ cá nhân nếu có dấu hiệu khủng hoảng.
```

---

### 8.2. Thang mức cảnh báo

| Risk score | Mức cảnh báo | Ý nghĩa | Hành động đề xuất |
|---:|---|---|---|
| 0–39 | THẤP | Bình thường | Theo dõi định kỳ |
| 40–59 | TRUNG BÌNH | Có dấu hiệu giảm sút | Nhắc nhở, gửi tài liệu hỗ trợ |
| 60–79 | CAO | Nguy cơ rõ ràng | Cố vấn học tập liên hệ trực tiếp |
| 80–100 | RẤT CAO | Cần can thiệp khẩn cấp | Họp khoa/phòng, hỗ trợ tài chính, tư vấn tâm lý nếu cần |

---

### 8.3. Quy trình can thiệp

Quy trình đề xuất:

```text
Hệ thống tính điểm rủi ro
   ↓
Sinh viên vượt ngưỡng cảnh báo
   ↓
Tạo alert
   ↓
Đưa vào hàng đợi ưu tiên
   ↓
Cố vấn học tập nhận cảnh báo
   ↓
Liên hệ và xác minh nguyên nhân
   ↓
Đề xuất hỗ trợ phù hợp
   ↓
Ghi nhận kết quả can thiệp
   ↓
Cập nhật mô hình và quy trình
```

Các hành động can thiệp có thể bao gồm:

- Nhắn tin nhắc nộp học phí.
- Mời gặp cố vấn học tập.
- Giới thiệu hỗ trợ tài chính.
- Xếp nhóm học tập cho sinh viên yếu.
- Cảnh báo môn học có nguy cơ rớt cao.
- Tư vấn tâm lý nếu có dấu hiệu bất thường.
- Liên hệ gia đình theo quy định nếu cần thiết.

---

## 9. Đánh giá và đạo đức dữ liệu

### 9.1. Metric đánh giá

Không nên chỉ dùng accuracy vì dữ liệu sinh viên thôi học thường mất cân bằng.

Ví dụ:

```text
95% sinh viên không thôi học
5% sinh viên thôi học

Nếu mô hình dự đoán tất cả sinh viên đều không thôi học:
Accuracy = 95%
Nhưng không phát hiện được sinh viên rủi ro nào.
```

Do đó cần dùng nhiều metric khác nhau.

| Metric | Ý nghĩa |
|---|---|
| Precision | Trong số sinh viên bị cảnh báo, có bao nhiêu em thực sự rủi ro |
| Recall | Trong số sinh viên thực sự rủi ro, hệ thống phát hiện được bao nhiêu |
| F1-score | Cân bằng giữa precision và recall |
| ROC-AUC | Khả năng phân biệt chung giữa hai nhóm |
| PR-AUC | Phù hợp với dữ liệu mất cân bằng |
| Top-k recall | Trong k sinh viên có điểm rủi ro cao nhất, có bao nhiêu em thực sự rủi ro |

Trong bài toán cảnh báo sớm:

> **Recall thường quan trọng hơn accuracy**, vì bỏ sót sinh viên cần giúp đỡ có thể dẫn đến hậu quả lớn.

Tuy nhiên, cũng cần kiểm soát precision để tránh cảnh báo sai gây phiền hà và lãng phí nguồn lực cố vấn.

---

### 9.2. Đạo đức dữ liệu

Hệ thống này liên quan trực tiếp đến sinh viên, nên cần có các nguyên tắc đạo đức rõ ràng.

#### Nguyên tắc 1: Mô hình chỉ cảnh báo, không quyết định thay con người

Kết quả dự đoán chỉ là gợi ý. Người quyết định can thiệp vẫn là cố vấn học tập, giảng viên và phòng công tác sinh viên.

#### Nguyên tắc 2: Phải giải thích được

Không nên chỉ hiển thị:

```text
Sinh viên A: rủi ro cao
```

Mà cần hiển thị:

```text
Sinh viên A: rủi ro cao vì GPA giảm mạnh, vắng 35%, nợ học phí và ít tham gia hoạt động.
```

#### Nguyên tắc 3: Tránh thiên kiến

Cần cẩn trọng với các biến có thể gây phân biệt đối xử:

- Giới tính.
- Quê quán.
- Dân tộc.
- Hoàn cảnh kinh tế.
- Diện chính sách.

Các yếu tố này có thể liên quan đến rủi ro, nhưng không được dùng để dán nhãn tiêu cực cho sinh viên.

#### Nguyên tắc 4: Bảo mật dữ liệu

Thông tin sinh viên cần được phân quyền truy cập:

- Cố vấn chỉ xem sinh viên phụ trách.
- Phòng công tác sinh viên xem theo phạm vi quản lý.
- Giảng viên bộ môn chỉ xem dữ liệu liên quan đến môn học.

#### Nguyên tắc 5: Có cơ chế phản hồi

Sinh viên cần có quyền biết mình bị cảnh báo và phản hồi nếu dữ liệu sai.

Ví dụ:

```text
Sinh viên cho rằng mình vắng học vì ốm có giấy xác nhận.
Hệ thống cần cập nhật lại dữ liệu chuyên cần.
```

#### Nguyên tắc 6: Không dán nhãn vĩnh viễn

Risk score là giá trị theo thời điểm, không phải đánh giá cố định về con người.

---

## 10. Kết luận

Hệ thống cảnh báo sớm sinh viên thôi học là một bài toán dự đoán rủi ro dựa trên dữ liệu giáo dục.

Bài toán có thể phát biểu là:

> Dự đoán khả năng sinh viên có nguy cơ thôi học trong kỳ tiếp theo dựa trên dữ liệu học tập, chuyên cần, tài chính, hành vi và quan hệ xã hội.

Cấu trúc dữ liệu phù hợp không phải là một cấu trúc duy nhất, mà là sự kết hợp:

- **Cơ sở dữ liệu quan hệ** để lưu dữ liệu gốc.
- **Feature matrix** để phục vụ tính toán rủi ro.
- **Dữ liệu chuỗi thời gian** để phát hiện xu hướng giảm sút.
- **Graph** để phân tích quan hệ xã hội nếu mở rộng.
- **Priority queue** để xử lý cảnh báo theo mức ưu tiên.

Giải thuật phù hợp có thể bắt đầu từ **rule-based scoring**, sau đó nâng cấp lên **machine learning classification**. Hướng thực tế nhất là kết hợp cả hai để vừa dự đoán tốt, vừa giải thích được.

Tuy nhiên, giá trị cốt lõi của hệ thống không nằm ở việc dự đoán chính xác tuyệt đối, mà nằm ở khả năng:

1. Phát hiện sớm.
2. Cảnh báo có lý do.
3. Hỗ trợ hành động can thiệp kịp thời.
4. Tôn trọng quyền riêng tư và đạo đức dữ liệu.
5. Liên tục cải thiện dựa trên phản hồi thực tế.

Nói ngắn gọn:

> Hệ thống không chỉ trả lời câu hỏi “ai có nguy cơ thôi học?”, mà còn phải trả lời “vì sao?”, “mức độ nào?” và “nhà trường nên làm gì tiếp theo?”.
