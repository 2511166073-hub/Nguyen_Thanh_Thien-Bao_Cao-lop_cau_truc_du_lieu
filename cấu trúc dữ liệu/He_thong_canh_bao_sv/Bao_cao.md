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

Bài toán được phát biểu như sau:

> Cho dữ liệu lịch sử của sinh viên gồm thông tin cá nhân, kết quả học tập, chuyên cần, học phí, hoạt động ngoại khóa và các sự kiện hỗ trợ. Hãy dự đoán khả năng sinh viên đó có nguy cơ thôi học trong kỳ tiếp theo.

Về mặt kỹ thuật, đây có thể xem là các bài toán sau:

| Cách tiếp cận | Mô tả |
|---|---|
| Phân loại nhị phân | Dự đoán sinh viên có thôi học hay không thôi học |
| Chấm điểm rủi ro | Trả về điểm rủi ro từ 0 đến 100 |
| Xếp hạng ưu tiên | Chọn ra nhóm sinh viên nguy cơ cao nhất để can thiệp trước |
| Dự báo theo thời gian | Nếu mở rộng, có thể dự đoán thời điểm sinh viên có nguy cơ nghỉ học |

Trong phạm vi báo cáo này, hướng tiếp cận phù hợp là:

> **Bài toán dự đoán rủi ro sinh viên thôi học, kết hợp chấm điểm rủi ro và đề xuất hành động can thiệp.**

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

---

## 5. Cấu trúc dữ liệu đề xuất

Hệ thống không nên chỉ dùng một cấu trúc dữ liệu duy nhất. Nên thiết kế theo nhiều lớp, tùy theo loại dữ liệu và mục đích xử lý.

### 5.1. Cơ sở dữ liệu quan hệ

Dùng để lưu dữ liệu gốc của sinh viên, lớp học, môn học, điểm số, học phí và các sự kiện hỗ trợ.

Các thực thể chính có thể bao gồm:

```text
students
semesters
courses
enrollments
grades
attendance
finance
support_events
risk_scores
alerts
interventions
feedback
```

Vai trò:

- Lưu trữ dữ liệu có cấu trúc.
- Dễ truy vấn theo sinh viên, học kỳ, môn học.
- Đảm bảo tính toàn vẹn dữ liệu.
- Tích hợp với hệ thống quản lý đào tạo hiện có của nhà trường.

Ví dụ mối quan hệ:

- Một sinh viên có nhiều kết quả học tập theo từng học kỳ.
- Một sinh viên có nhiều bản ghi chuyên cần.
- Một sinh viên có nhiều khoản học phí.
- Một sinh viên có thể nhận nhiều cảnh báo và được can thiệp nhiều lần.

---

### 5.2. Feature matrix cho mô hình dự đoán

Từ dữ liệu quan hệ, hệ thống cần tạo ra một bảng đặc trưng để phục vụ tính toán rủi ro.

Ma trận đặc trưng có kích thước N × F.
Trong đó:
- N là số sinh viên.
- F là số đặc trưng rủi ro.
Mỗi dòng đại diện cho một sinh viên trong một học kỳ.  
Mỗi cột đại diện cho một đặc trưng rủi ro.

Ví dụ các đặc trưng:

| Đặc trưng | Ý nghĩa |
|---|---|
| GPA | Điểm trung bình học kỳ |
| Số môn rớt | Số học phần không đạt |
| Tỷ lệ vắng học | Mức độ chuyên cần |
| Nợ học phí | Áp lực tài chính |
| Điểm rèn luyện | Mức độ tham gia phong trào, câu lạc bộ |
| Tiến độ tín chỉ | So với yêu cầu chương trình |
| Số ngày không liên hệ cố vấn | Mức độ kết nối với hệ thống hỗ trợ |

ví dụ: 
feature_matrix = [
    # MSSV, GPA, failed, absent, debt, activity, progress
    ["SV001", 3.2, 0, 0.05, 0,         80, 0.90],
    ["SV002", 1.8, 4, 0.38, 9000000,   12, 0.40],
    ["SV003", 2.4, 2, 0.22, 4000000,   30, 0.65],
]


Feature matrix giúp chuyển dữ liệu quản lý thô thành đầu vào phù hợp cho giải thuật tính điểm rủi ro hoặc mô hình học máy.


---

### 5.3. Dữ liệu chuỗi thời gian

Sinh viên không nên chỉ được đánh giá tại một thời điểm, mà cần theo dõi xu hướng qua nhiều học kỳ.

Ví dụ:

```text
Học kỳ 1: GPA = 3.2
Học kỳ 2: GPA = 2.8
Học kỳ 3: GPA = 2.2
```

Xu hướng giảm liên tục là tín hiệu rủi ro quan trọng.

Các đặc trưng chuỗi thời gian hữu ích:

- Mức giảm GPA trong hai học kỳ gần nhất.
- Tốc độ tăng tỷ lệ vắng học.
- Số học kỳ liên tiếp có môn rớt.
- Thời gian kéo dài tình trạng nợ học phí.
- Mức giảm tham gia hoạt động so với kỳ trước.

Cấu trúc dữ liệu phù hợp:

- Bảng lưu dữ liệu theo học kỳ.
- Mảng chuỗi giá trị theo thời gian.
- Cửa sổ trượt để tính xu hướng.

---

### 5.4. Graph cho quan hệ xã hội

Graph có thể dùng để biểu diễn mối quan hệ giữa sinh viên và các thực thể khác trong môi trường học đường.

Các đỉnh có thể là:

```text
Sinh viên
Lớp học
Câu lạc bộ
Giảng viên
Cố vấn học tập
Nhóm học tập
```

Các cạnh có thể là:

```text
Học cùng lớp
Tham gia cùng câu lạc bộ
Được cố vấn bởi
Học nhóm cùng nhau
```

Ứng dụng:

- Phát hiện sinh viên bị cô lập.
- Phát hiện nhóm bạn có cùng nguy cơ bỏ học.
- Phân tích ảnh hưởng xã hội.
- Đánh giá mức độ kết nối của sinh viên với cộng đồng học tập.

Cấu trúc dữ liệu phù hợp:

- Danh sách kề.
- Danh sách cạnh.
- Đồ thị quan hệ nếu triển khai mở rộng.

---

### 5.5. Priority queue cho hàng đợi cảnh báo

Khi hệ thống tạo ra nhiều cảnh báo, cần xử lý theo mức ưu tiên.

Ví dụ:

| Sinh viên | Điểm rủi ro |
|---|---:|
| SV_A | 92 |
| SV_C | 88 |
| SV_B | 61 |
| SV_D | 35 |

Priority queue giúp lấy sinh viên có mức rủi ro cao nhất ra trước để cố vấn học tập can thiệp kịp thời.

Cấu trúc dữ liệu phù hợp:

- Heap.
- Hàng đợi ưu tiên.
- Danh sách cảnh báo được sắp xếp theo điểm rủi ro giảm dần.

---

## 6. Giải thuật đề xuất

### 6.1. Rule-based scoring

Đây là phương pháp tính điểm rủi ro dựa trên các luật nghiệp vụ.

Ưu điểm:

- Dễ hiểu.
- Dễ triển khai.
- Giải thích được lý do cảnh báo.
- Phù hợp khi chưa có nhiều dữ liệu lịch sử để huấn luyện mô hình machine learning.

Ví dụ bộ luật:

| Điều kiện | Điểm rủi ro cộng thêm |
|---|---:|
| GPA dưới 2.0 | +30 |
| GPA từ 2.0 đến dưới 2.5 | +20 |
| GPA từ 2.5 đến dưới 3.0 | +10 |
| Số môn rớt từ 4 trở lên | +25 |
| Số môn rớt từ 2 đến 3 | +15 |
| Có 1 môn rớt | +5 |
| Tỷ lệ vắng học trên 30% | +25 |
| Tỷ lệ vắng học từ 20% đến 30% | +15 |
| Tỷ lệ vắng học từ 10% đến 20% | +5 |
| Nợ học phí trên 8 triệu đồng | +20 |
| Nợ học phí từ 3 triệu đến 8 triệu đồng | +10 |
| Điểm rèn luyện dưới 20 | +10 |
| Điểm rèn luyện từ 20 đến dưới 40 | +5 |
| Tiến độ tín chỉ dưới 50% | +15 |
| Hơn 90 ngày không liên hệ cố vấn | +10 |
| Hơn 60 ngày không liên hệ cố vấn | +5 |

Công thức tổng quát:

```text
risk_score = min(100, tổng điểm rủi ro của các luật được kích hoạt)
```

Ví dụ minh họa:

Sinh viên A có:

- GPA = 1.8.
- Số môn rớt = 4.
- Tỷ lệ vắng học = 38%.
- Nợ học phí = 9 triệu đồng.
- Điểm rèn luyện = 12.
- Tiến độ tín chỉ = 40%.
- Hơn 90 ngày không liên hệ cố vấn.

Điểm rủi ro:

```text
GPA dưới 2.0: +30
Từ 4 môn rớt trở lên: +25
Vắng học trên 30%: +25
Nợ học phí trên 8 triệu: +20
Điểm rèn luyện dưới 20: +10
Tiến độ tín chỉ dưới 50%: +15
Hơn 90 ngày không liên hệ cố vấn: +10

Tổng = 135
Giới hạn tối đa = 100
```

Kết luận:

```text
Risk score = 100
Mức cảnh báo = RẤT CAO
```

---

### 6.2. Machine learning classification

Khi nhà trường có dữ liệu lịch sử với nhãn sinh viên thôi học, có thể dùng các mô hình học máy để dự đoán xác suất thôi học.

Các mô hình phù hợp:

| Mô hình | Đặc điểm |
|---|---|
| Logistic Regression | Đơn giản, dễ giải thích |
| Decision Tree | Trực quan, dễ hiểu |
| Random Forest | Mạnh, phù hợp dữ liệu bảng |
| Gradient Boosting | Hiệu suất cao trên dữ liệu có cấu trúc |
| XGBoost / LightGBM | Phù hợp bài toán phân loại quy mô vừa và lớn |

Đầu vào:

```text
Vector đặc trưng của sinh viên trong một học kỳ
```

Đầu ra:

```text
Xác suất thôi học
Điểm rủi ro
Mức cảnh báo
Lý do chính
Hành động đề xuất
```

Ưu điểm:

- Tự học từ dữ liệu.
- Phát hiện được các mẫu phức tạp.
- Có thể cải thiện theo thời gian khi có thêm dữ liệu phản hồi.

Nhược điểm:

- Cần dữ liệu lịch sử đủ tốt.
- Dễ gặp vấn đề mất cân bằng nhãn vì số sinh viên thôi học thường ít.
- Cần cơ chế giải thích để cố vấn học tập tin tưởng kết quả.

---

### 6.3. Hybrid rule-based và machine learning

Hướng thực tế và đáng đề xuất nhất là kết hợp cả hai phương pháp.

Ý tưởng:

- Machine learning dự đoán xác suất rủi ro tổng quát.
- Rule-based bổ sung các luật nghiệp vụ quan trọng.
- Kết quả cuối cùng vừa có tính dự đoán, vừa giải thích được.

Ví dụ công thức tổng hợp:

```text
final_risk_score =
    0.6 * ml_risk_score
  + 0.4 * rule_based_risk_score
```

Hoặc có thể dùng rule-based như một lớp hiệu chỉnh:

```text
Nếu sinh viên có nợ học phí nghiêm trọng hoặc vắng học quá cao,
nâng mức cảnh báo lên ít nhất là CAO.
```

Ưu điểm:

- Giảm rủi ro mô hình học máy dự đoán sai trong các trường hợp nghiệp vụ rõ ràng.
- Tăng khả năng giải thích.
- Phù hợp với hệ thống quản lý sinh viên thực tế.

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
