# Bài tập giữa kỳ: Tìm hiểu 05 thuật toán tìm kiếm

## 1. Mục tiêu bài tập
Bài tập này nhằm tìm hiểu 05 thuật toán tìm kiếm nâng cao ngoài Linear Search và Binary Search, bao gồm:
1. Linear Search 
2. Binary Search 
3. Jump Search
4. Interpolation Search
5. Exponential Search
6. Fibonacci Search
7. Ternary Search
## 2. Tổng quan 05 thuật toán tìm kiếm
| Thuật toán | Điều kiện dữ liệu | Ý tưởng chính | Độ phức tạp trung bình | Khi nào nên dùng |
|---|---|---|---|---|
| Jump Search | Mảng đã sắp xếp | Nhảy theo block rồi tìm tuyến tính trong block | O(√n) | Mảng lớn, đã sắp xếp, muốn giảm số lần so sánh |
| Interpolation Search | Mảng đã sắp xếp, phân bố đều | Ước lượng vị trí phần tử dựa trên giá trị | O(log log n) | Dữ liệu số phân bố gần đều |
| Exponential Search | Mảng đã sắp xếp | Tăng chỉ số theo lũy thừa 2 rồi dùng Binary Search | O(log n) | Mảng rất lớn hoặc không biết trước kích thước |
| Fibonacci Search | Mảng đã sắp xếp | Dùng dãy Fibonacci để chia mảng | O(log n) | Khi muốn tránh phép chia, tối ưu tính toán |
| Ternary Search | Mảng đã sắp xếp hoặc hàm đơn đỉnh | Chia khoảng tìm kiếm thành 3 phần | O(log₃ n) | Tìm phần tử hoặc tìm cực trị của hàm unimodal |
## 3. Jump Search
### 3.1 Jump search là gì? 
Jump Search, hay còn gọi là Block Search, là thuật toán tìm kiếm áp dụng cho mảng đã được xắp xếp. thuật toán này nhảy qua từng khối với bước nhảy cố định, sau đó tìm tuyến tính khối chứa giá trị cần tìm. 
### 3.2 Ý tưởng hoạt động
Giả sử có n phần tử. 
bước nhảy thường được gọi là: 
step = ⌊√n⌋
Thuật toán thực hiện: 
1. Nhảy từ đầu mảng theo từng bước √n. 
2. Dừng lại khi gặp phần tử lớn hoặc bằng giá trị cần tìm. 
3. Tìm tuyến tính trong khối vừa dừng. 
### 3.3 Khi nào nên dùng? 
Nên dùng khi:
- Mảng đã được xắp xếp 
- Kích thước mảng khá lớn 
- Muốn giảm số lần so với linear Search. 
- không cần tối ưu bằng Binary Search. 

## 4. Interpolation Search
### 4.1 Interpolation Search là gì? 
Interpolation Search là thuật toán tìm kiếm mảng đã xắp xếp, cải tiến từ Binary Search. Thay vì luôn chia đôi mảng, thuật toán ước lượng vị trí của phần tử cần tìm dựa trên giá trị của nó so với giá trị ở hai đầu tìm kiếm. 
### 4.2 Ý tưởng  hoạt động 
công  thức ước lượng vị trí: 
pos = low + ((x-arr[low])*(high-low))//(arr[high]-arr[low])
trong đó: 
- low: chỉ số đầu ra khoảng tìm kiếm 
-high: chỉ số cuối khoảng tìm kiếm 
-x: giá trị cần tìm 
-pos: vị trí ước lượng
ví dụ: 
mảng:[39,73,76,86,87,89,95,97]
Tìm x = 89 
Binary Search sẽ chia đôi. 
Interpolation Search ước lượng bằng 60 gần cuối mảng hơn, nên có thể nhảy thẳng đến vị trí gần đúng. 
### 4.3 Khi nào nên dùng 
- Mảng đã xắp xếp. 
- Dữ liệu là số. 
- Dữ liệu phân bố tương đối đều. 
- Giá trị cần tìm có thể nội suy được từ khoảng giá trị.
### 4.4 Nhận xét 
Ưu điểm:
- rất nhanh nếu dữ liệu phân bố đều. 
- Có thể vượt trội hơn Binary Search nếu dữ liệu số lớn. 
Nhược điểm: 
- Phụ thuộc vào phân bố dữ liệu. 
- Nếu dữ liệu lệch, hiệu xuất giảm mạnh. 
- Cần kiểm tra điều kiện arr[low]<=x<=arr[high] để tránh truy cập ngoài mảng. 

## 5. Exponential Search
### 5.1 Exponential Search là gì? 
Exponential Search, còn gọi là Doubling Search hoặc Galloping Search, là thuật toán tìm kiếm trên mảng đã xắp xếp. Thuật toán này tìm khoảng chứa giá trị cần tìm bằng cách tăng theo cấp số nhân, sau đó áp dụng Binary Search trong khoảng đó. 
### 5.2 ý tưởng hoạt động 
Các bước: 
1. Bắt đầu từ index = 1 
2. Nhân đôi index: 1, 2, 4, 8, 16...
3. Dùng khi arr[index] >= x hoặc vượt quá mảng. 
4. Dùng Binary Search trong khoảng [index/2, min(index, n-1)].
### 5.3 Khi nào nên dùng. 
Nên dùng khi: 
- Mảng đã xắp xếp. 
- Mảng rất lớn. 
- Không biết kích thước mảng. 
- Làm việc với dữ liệu stream hoặc unbounded array.    
### 5.6. Nhận xét

Ưu điểm:

- Tốt cho mảng lớn hoặc không biết trước kích thước.
- Kết hợp ưu điểm của Binary Search.
- Thời gian O(log n).

Nhược điểm:

- Vẫn yêu cầu mảng đã sắp xếp.
- Trong trường hợp mảng nhỏ, có thể không nhanh hơn Binary Search đáng kể.
## 6. Fibonacci Search
## 6. Fibonacci Search

### 6.1. Fibonacci Search là gì?

Fibonacci Search là thuật toán tìm kiếm trên mảng đã sắp xếp, sử dụng dãy Fibonacci để xác định vị trí chia mảng thay vì chia đôi như Binary Search.

Dãy Fibonacci:

F(0) = 0  
F(1) = 1  
F(n) = F(n-1) + F(n-2)

Ví dụ:

0, 1, 1, 2, 3, 5, 8, 13, 21...

### 6.2. Ý tưởng hoạt động

Thay vì tính:

mid = (low + high) // 2

Fibonacci Search dùng các số Fibonacci để xác định vị trí chia mảng.

Điều này hữu ích trong các hệ thống mà phép chia hoặc phép tính mid tốn kém.

### 6.3. Khi nào nên dùng?

Nên dùng khi:

- Mảng đã sắp xếp.
- Muốn tránh phép chia.
- Làm việc trong môi trường hạn chế tài nguyên tính toán.
- Cần một biến thể của Binary Search dựa trên dãy Fibonacci.
### 6.4. Nhận xét

Ưu điểm:

- Cũng đạt O(log n).
- Tránh được phép chia trong quá trình xác định mid.
- Hữu ích trong một số môi trường tính toán đặc thù.

Nhược điểm:

- Khó hiểu hơn Binary Search.
- Trong thực tế Python, ít khi cần dùng vì phép chia không phải bottleneck lớn.

## 7. Ternary Search
## 7. Ternary Search

### 7.1. Ternary Search là gì?

Ternary Search là thuật toán chia khoảng tìm kiếm thành ba phần thay vì hai phần như Binary Search.

Ternary Search có thể dùng để:

1. Tìm một giá trị trong mảng đã sắp xếp.
2. Tìm giá trị lớn nhất hoặc nhỏ nhất của một hàm đơn đỉnh.

### 7.2. Ternary Search tìm phần tử

Chia mảng thành 3 phần:

mid1 = low + (high - low) // 3  
mid2 = high - (high - low) // 3

So sánh x với arr[mid1] và arr[mid2] để loại bỏ 2/3 khoảng không cần tìm.

### 7.3. Ternary Search tìm cực trị

Nếu hàm f(x) là đơn đỉnh, tức có một đỉnh cực đại hoặc cực tiểu, ta có thể dùng Ternary Search để tìm vị trí cực trị.

Ví dụ tìm max:

Nếu f(mid1) < f(mid2), cực đại nằm về phía phải.

Ngược lại, cực đại nằm về phía trái.

### 7.4. Khi nào nên dùng?

Nên dùng khi:

- Mảng đã sắp xếp và muốn tìm phần tử.
- Cần tìm cực trị của hàm unimodal.
- Không cần chính xác tuyệt đối với hàm liên tục, có thể dùng epsilon.

### 7.5. Độ phức tạp

- Tìm phần tử: O(log₃ n)
- Tìm cực trị hàm liên tục: O(log₃((high-low)/epsilon))
### 7.6. Nhận xét

Ưu điểm:

- Linh hoạt: vừa tìm phần tử, vừa tìm cực trị.
- Phù hợp với bài toán tối ưu hàm đơn đỉnh.

Nhược điểm:

- Khi tìm phần tử trong mảng rời rạc, Binary Search thường đơn giản và hiệu quả hơn.
- Với hàm liên tục, cần chọn epsilon phù hợp.
## 8. Linear Search 
- ý tưởng: duyệt từng phần tử đến cuối mảng, so sánh với giá trị cần tìm. Nếu gặp thì trả về vị trí, nếu hết mảng mà không thấy thì trả về"không tìm thấy".
- giống như lật một cuốn sách chưa xắp xếp, lật từng trang một.
- Dùng khi mảng nhỏ chưa xắp xếp, dữ liệu dạng linked list không truy cập ngẫu nhiên được.
+ Dữ liệu thay đổi liên tục.
## 9. Binary Search(Tìm kiếm nhị Phân)
- Yêu cầu bắt buộc: mảng phải được xắp xếp trước. 
- Mỗi bước, so sánh giá trị cần tìm với phần tử ở giữa. Nếu nhỏ hơn-> tìm nửa trái; nếu lớn hơn-> tìm nửa phải; nếu bằng -> tìm thấy. mỗi lần loại bỏ một nửa giữ liệu 
- Giống như mở sách, mở giữa rồi lật nửa trước hoặc nửa sau  
## 8. So sánh tổng hợp

| Tiêu chí | Jump Search | Interpolation Search | Exponential Search | Fibonacci Search | Ternary Search |
|---|---|---|---|---|---|
| Điều kiện | Mảng sorted | Sorted + phân bố đều | Mảng sorted | Mảng sorted | Sorted hoặc hàm unimodal |
| Trung bình | O(√n) | O(log log n) | O(log n) | O(log n) | O(log₃ n) |
| Tệ nhất | O(√n) | O(n) | O(log n) | O(log n) | O(log₃ n) |
| Không gian | O(1) | O(1) | O(1) | O(1) | O(1) |
| Điểm mạnh | Đơn giản | Nhanh với dữ liệu đều | Tốt cho mảng lớn/không biết size | Tránh phép chia | Tìm cực trị tốt |
| Điểm yếu | Chậm hơn binary | Nhạy với dữ liệu lệch | Vẫn cần sorted | Khó hiểu hơn | Ít dùng cho mảng rời rạc |
## 9. Kết luận

Qua việc tìm hiểu 05 thuật toán tìm kiếm, có thể rút ra một số nhận xét:

1. Không có thuật toán tìm kiếm nào tốt nhất cho mọi trường hợp.
2. Linear Search đơn giản nhưng chậm, chỉ phù hợp với dữ liệu nhỏ hoặc chưa sắp xếp.
3. Binary Search là nền tảng quan trọng cho nhiều thuật toán khác.
4. Jump Search phù hợp khi muốn một phương pháp đơn giản trên mảng đã sắp xếp.
5. Interpolation Search rất hiệu quả khi dữ liệu phân bố đều.
6. Exponential Search phù hợp với mảng lớn hoặc không biết trước kích thước.
7. Fibonacci Search hữu ích trong môi trường hạn chế phép chia.
8. Ternary Search đặc biệt phù hợp để tìm cực trị của hàm đơn đỉnh.

Do đó, khi lựa chọn thuật toán tìm kiếm, cần xem xét:

- Dữ liệu đã sắp xếp hay chưa.
- Kích thước dữ liệu.
- Phân bố dữ liệu.
- Yêu cầu bộ nhớ và tốc độ.
- Bài toán là tìm phần tử hay tìm cực trị.
