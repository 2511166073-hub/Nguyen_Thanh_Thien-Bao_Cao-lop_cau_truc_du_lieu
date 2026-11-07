# mục lục
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



## 1. Đặt vấn đề

Theo các bài báo và thực tế quản lý giáo dục, tỉ lệ sinh viên thôi học giữa chừng gây ảnh hưởng đến cá nhân sinh viên, gia đình, nhà trường và nguồn nhân lực xã hội. Nếu chỉ phát hiện sinh viên bỏ học khi đã xảy ra, nhà trường sẽ mất cơ hội can thiệp sớm.

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
5. **Theo dõi hiệu quả can thiệp** để cải thiện mô hình.

---

## 3. Bài toán cốt lõi

Bài toán được phát biểu như sau:

> Cho dữ liệu lịch sử của sinh viên gồm thông tin cá nhân, kết quả học tập, chuyên cần, học phí, hoạt động ngoại khóa và các sự kiện hỗ trợ. Hãy dự đoán khả năng sinh viên đó có nguy cơ thôi học trong kỳ tiếp theo.

Về mặt kỹ thuật, đây là bài toán:

- **Phân loại nhị phân**: sinh viên thôi học hay không thôi học.
- **Chấm điểm rủi ro**: trả về xác suất hoặc điểm từ 0 đến 100.
- **Xếp hạng ưu tiên**: chọn ra nhóm sinh viên nguy cơ cao nhất để can thiệp.
- **Dự báo theo thời gian**: nếu mở rộng, có thể dùng survival analysis để dự đoán thời điểm có nguy cơ nghỉ học.

---

## 4. Dữ liệu sử dụng

Hệ thống có thể thu thập các nhóm dữ liệu sau:

### 4.1. Thông tin cá nhân

- Mã sinh viên
- Họ tên
- Giới tính
- Năm sinh
- Quê quán
- Diện chính sách
- Dân tộc
- Hộ khẩu thường trú
- Hoàn cảnh kinh tế

### 4.2. Dữ liệu học tập

- Điểm trung bình học kỳ
- Điểm từng môn
- Số môn rớt
- Số tín chỉ tích lũy
- Tiến độ so với chương trình
- Kết quả rèn luyện
- Số lần học lại
- Số môn đang nợ

### 4.3. Dữ liệu chuyên cần

- Số buổi vắng
- Tỷ lệ đi học
- Vắng không phép
- Đi muộn
- Tham gia lớp học trực tuyến nếu có

### 4.4. Dữ liệu tài chính

- Học phí còn nợ
- Số lần chậm đóng học phí
- Được miễn giảm học phí
- Nhận học bổng
- vay vốn sinh viên

### 4.5. Dữ liệu hành vi và hoạt động

- Đăng ký môn học
- Hủy môn
- Sử dụng thư viện
- Truy cập portal sinh viên
- Tham gia câu lạc bộ
- Hoạt động ngoại khóa
- Tư vấn tâm lý
- Liên hệ phòng công tác sinh viên

### 4.6. Dữ liệu quan hệ xã hội

- Bạn cùng lớp
- Nhóm học tập
- Câu lạc bộ
- Giảng viên phụ trách
- Cố vấn học tập

Nhóm dữ liệu này có thể biểu diễn bằng đồ thị.

---

## 5. Cấu trúc dữ liệu đề xuất

Hệ thống không nên chỉ dùng một cấu trúc dữ liệu duy nhất. Nên thiết kế theo nhiều lớp.

### 5.1. Cơ sở dữ liệu quan hệ

Dùng để lưu dữ liệu gốc của sinh viên, lớp học, môn học, điểm số, học phí.

Các bảng chính:

```text
students
enrollments
courses
grades
attendance
finance
support_events
alerts
interventions
