

# 1. Kiểm thử bằng bảng quyết định

Kỹ thuật kiểm thử lớp tương đương và kiểm thử giá trị biên thích hợp cho các hàm có các biến đầu vào không có quan hệ ràng buộc với nhau. Kỹ thuật kiểm thử dựa trên bảng quyết định sẽ phù hợp cho các hàm có các hành vi khác nhau dựa trên tính chất của bộ giá trị của đầu vào. Nói cách khác, kỹ thuật này phù hợp với các hàm/chương trình có các biến đầu vào phụ thuộc lẫn nhau.

Kiểm thử dựa trên bảng quyết định là phương pháp chính xác nhất trong các kỹ thuật kiểm thử chức năng. Bảng quyết định là phương pháp hiệu quả để mô tả các sự kiện, hành vi sẽ xảy ra khi một số điều kiện thỏa mãn.

# 1.1 Bảng quyết định

Cấu trúc của một bảng quyết định chia thành bốn phần chính như trong Bảng 5.9, bao gồm:

Các biểu thức điều kiện C1, C2, C3; Giá trị điều kiện T, F, –;   
• Các hành động A1, A2, A3, A4; và Giá trị hành động, có (xảy ra) hay không. Chúng ta ký hiệu X để chỉ hành động là có xảy ra ứng với các điều kiện tương ứng của cột.

Khi lập bảng quyết định, chúng ta thường tìm các điều kiện có thể xảy ra để xét các tổ hợp của chúng mà từ đó chúng ta sẽ xác định được các ca kiểm thử tương ứng cho các điều kiện được thỏa mãn. Các hành động xảy ra chính là kết quả mong đợi của ca kiểm thử đó.

Bảng quyết định với các giá trị điều kiện chỉ là T, F, và – được gọi là bảng quyết định lôgic. Chúng ta có thể mở rộng các giá trị này bằng các tập giá trị khác, ví dụ 1, 2, 3, 4, khi đó chúng ta có bảng quyết định tổng quát.

Bảng 5.10 là một ví dụ đơn giản về một bảng quyết định để khắc phục sự cố máy in. Khi máy in có sự cố, chúng ta sẽ xem xét tình trạng dựa trên các điều kiện trong bảng là đúng (T) hay sai (F), từ đó xác định được cột duy nhất có các điều kiện thỏa mãn, và thực hiện các hành động khắc phục sự cố tương ứng.

Bảng 5.9: Ví dụ về một bảng quyết định







Kiểm thử bằng bảng quyết định cho hàm NextDate: Có nhiều cách xác định các điều kiện. Ví dụ chúng ta sẽ đặc tả ngày và tháng trong năm và quy đổi về dạng của một năm nhuận hay một năm thông thường giống như trong lần thử đầu tiên, do đó năm 1900 sẽ không có gì đặc biệt. Các miền tương đương bây giờ như sau:

• $\begin{array} { r } { \mathbf { M } 1 = \left. \begin{array} { r l r } \end{array} \right\} } \end{array}$ tháng | tháng có 30 ngày } • $\begin{array} { r } { { \bf M } 2 = \left\{ \begin{array} { r l r } \end{array} \right. } \end{array}$ tháng | tháng có 31 ngày, trừ tháng 12 } • $\mathbf { M } 3 = \left\{ \begin{array} { r l r } \end{array} \right.$ tháng | tháng 12 } • $\mathbf { M } 4 = \left\{ { \mathrm { ~ t h a n g ~ } } | { \mathrm { ~ t h a n g ~ } } 2 \right\}$ Ngày • • $\begin{array} { l }  { \mathrm { D 1 } = \{ \mathrm { n g \dot { a } y \mid 1 \leq \mathrm { n g \dot { a } y \leq 2 7 \ } \} } } \\ { { } } \\ { { \mathrm { D 2 } = \{ \mathrm { n g \dot { a } y \mid n g \dot { a } y = 2 8 \ \} } } } \end{array}$ $\mathrm { { D 3 } = \{ n g \dot { a } y | n g \dot { a } y = 2 9 \Big \} }$ • $\mathrm { D 4 } = \{ { \mathrm { n g } } { \mathrm { \dot { a } y ~ | \ n g { \dot { a } y } = 3 0 ~ } } \}$ • $\mathrm { D 5 } = \{ \mathrm { n g } \mathrm { \dot { a } y | \ n g \dot { a } y = 3 1 \ } \}$ Năm • $\mathrm { Y 1 } = \{ \mathrm { n } \breve { \mathrm { a m } } \ | \ \mathrm { n } \breve { \mathrm { a m } } \ \mathrm { n h u } \hat { \mathrm { a n } } \ \}$ • $\mathrm { Y } 2 = \{ \mathrm { n } \mathrm { \breve { a } m } \ |$ năm thông thường }

Trong khi tích $\mathrm { \bf { \vec { \ p } } \vec { \hat { e } } } ^ { }$ -các sẽ tạo ra 40 bộ giá trị nếu áp dụng kiểm thử lớp tương đương mạnh, bảng quyết định được lập như Bảng 5.13 chỉ cần 22 bộ giá trị ứng với 22 ca kiểm thử. $\mathrm { C o } 2 2$ quy tắc, so với 36 trong thử lần hai. Chúng ta có một bảng quyết định với 22 quy tắc. Năm quy tắc đầu tiên cho tháng có 30 ngày. Hai bộ tiếp theo (6-10 và 11-15) cho tháng có 31 ngày, với các tháng khác Tháng Mười Hai và với Tháng Mười Hai.