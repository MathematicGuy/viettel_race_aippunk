<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 121</td></tr><tr><td rowspan=1 colspan=1>PHUONG PHAP VA MOT SO DO DODÁNH GIA CAC Mo HiNH PHAN LoPDA NHAN</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 1. Phương pháp đánh giá các mô hình phân lớp đa nhãn

Để đánh giá các mô hình phân lớp đa nhãn MLL, khóa luận đã sử dụng phương pháp $\mathrm { k }$ -fold cross validation tập dữ liệu ban đầu được chia ngẫu nhiên thành k tập con (fold) có kích thước xấp xỉ nhau S1, S2 … Sk. Quá trình học và kiểm tra được thực hiện tại k lần. Tại lần lặp thứ i, Si là tập dữ liệu kiểm tra, các tập còn lại hợp thành dữ liệu huấn luyện. Có nghĩa là, đầu tiên chạy được thực hiện trên tập S2, S3 … Sk, sau đó test trên tập S1; tiếp tục quá trình dạy được thực hiện trên tập S1, S3, S4 … Sk, sau đó test trên tập S2; và cứ tiếp tục như thế.

Ví dụ, ${ \mathrm { k } } = 1 0$ , thì phương pháp $\mathrm { k \Omega }$ -fold cross validation được minh họa như hình dưới:

Bảng minh họa phương pháp k-fold cross validation   

<table><tr><td rowspan=1 colspan=1>K=1</td></tr><tr><td rowspan=1 colspan=1>K=2</td></tr><tr><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>K=10</td></tr></table>

![](images/6f0249e120d9d664f28c88817840f4e09b2b0b25e0635bc2eaa1198232d2770b.jpg)

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 121</td></tr><tr><td rowspan=1 colspan=1>PHUONG PHAP VA MOT SO DO DODÁNH GIA CAC Mo HiNH PHAN LoPDA NHAN</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 2. Một số độ đo để đánh giá mô hình phân lớp đa nhãn

Đánh giá kết quả phương pháp phân lớp đa nhãn có sự khác biệt với đơn nhãn. Khóa luận đánh giá các phương pháp phân lớp đa nhãn dựa trên một số độ đo sau: Hamming Loss [15], One-error [15], Coverage [15], Ranking Loss [15], Average Precision, Mean Average Precision.

Cho một tập $\mathrm { \bf S } = \{ ( \mathrm { x } 1 , \mathrm { Y } 1 ) \dots ( \mathrm { x n } , \mathrm { Y } \mathrm { n } ) \}$ của n ví dụ kiểm tra. Cho $\mathrm { Y } ^ { * } \mathrm { i } = \mathrm { h }$ (xi) là tập hợp nhãn dự đoán cho kiểm tra xi, khi Yi là tập nhãn cho xi.

Hamming Loss: độ mất mát dữ liệu, được tính như sau:

$$
\begin{array} { r } { \mathrm { ~ ; ~ } ( \mathbf { h } ) = \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \frac { 1 } { Q } \sum _ { q = 1 } ^ { Q } ( \delta ( q \epsilon Y * _ { i } \textit { } A q \notin ) Y i ) + \delta \left( \mathbf { q } \notin Y * _ { i } \textit { } A q \epsilon Y i \right) } \end{array}
$$

Trong đó, ?? là một hàm mà đầu ra là 1 nếu một nội dung đúng và 0 trong trường hợp ngược lại. Nhỏ hơn giá trị của hloss (h), thực thi tốt hơn. Trong trường hợp lí tưởng, hloss $( \mathrm { h } ) = 0$ .

One-error: đánh giá lỗi cho nhãn xếp hạng đầu:

$$
o n e _ { - } e r r o r { _ { S } } _ { ( f ) } = \frac 1 n \sum _ { i = 1 } ^ { n } \delta ( [ \arg \operatorname* { m a x } _ { y \in \gamma } f ( x _ { i } , y ) ] \notin Y i )
$$

Giá trị nhỏ hơn one_err (f), thực thi tốt hơn. Chú ý, vấn đề phân loại cho đơn nhãn, một lỗi chính là phân loại lỗi thường.

Coverage: Để đánh giá hiệu suất của một hệ thống cho tất cả các nhãn của một mẫu (đếm số lượng tất cả các nhãn). Coverage được định nghĩa như khoảng cách trung bình cho tất cả các nhãn thích hợp được gán cho một ví dụ thử nghiệm:

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 121</td></tr><tr><td rowspan=1 colspan=1>PHUONG PHAP VA MOT SO DO DODÁNH GIA CAC Mo HiNH PHAN LoPDA NHAN</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

$$
c o v e r a g e s _ { s } ( f ) = \frac { 1 } { n } { \sum _ { i = 1 } ^ { n } \operatorname* { m a x } _ { y \in \Upsilon \mathrm { i } } { r a n k _ { f } ( x _ { i } , y ) } } - 1
$$

Ranking Loss: Tính phân bố trung bình của các cặp nhãn:

$$
\begin{array} { r }  \mathfrak { s } \left( \mathbf { f } \right) = \frac { 1 } { n } { \sum _ { i = 1 } ^ { n } } \frac { 1 } { | Y _ { i } | | \overline { { Y _ { t } } } | } \mid \left\{ ( y _ { 1 } , y _ { 2 } ) \in \begin{array} { l l } { Y _ { i } X \overline { { Y _ { t } } } | \textup { f } ( \mathbf { x } _ { \mathrm { i } } , \mathbf { y } _ { 1 } ) \leq \mathbf { f } \left( \mathbf { x } _ { 1 } , \mathbf { y } _ { 2 } \right) \right\} } \end{array} \end{array}
$$

Với $\bar { Y _ { \iota } }$ là phần bù của tập nhãn $\mathrm { Y _ { i } }$ . Giá trị của rloss (f) càng nhỏ thì càng tốt.

Average Precision: độ chính xác trung bình của $\mathrm { P } @ \mathrm { K }$ tại các mức K có đối tượng đúng. Gọi I (K) là hàm xác định đối tượng $\dot { \mathbf { O } }$ vị trí hạng K nếu đúng $\mathrm { I } ( \mathrm { K } ) = 1$ và ngược lại $\mathrm { I } ( \mathrm { K } ) = 0$ , khi đó:

$$
{ \mathrm { A P } } = { \frac { \sum _ { K = 1 } ^ { n } P @ K X I ( K ) } { \sum _ { j = 1 } ^ { n } I ( j ) } }
$$

Với n là số đối tượng được xét, $\mathrm { P } @ \mathrm { K }$ là độ chính xác của K đối tượng đầu bảng xếp hạng. Xác định số đối tượng đúng ở K vị trí đầu tiên của xếp hạng và gọi là Match@K và ta có

Mean Average Precision: Độ chính xác trung bình trên N xếp hạng. (N truy vấn, mỗi truy vấn có một thứ tự xếp hạng kết quả tương ứng).

$$
\mathrm { M A P } = { \frac { \sum _ { i = 1 } ^ { N } A P i } { N } }
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 121</td></tr><tr><td rowspan=1 colspan=1>PHUONG PHÁP VA MOT SO DO DODÁNH GIA CAC Mo HiNH PHAN LoPDA NHAN</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

Xét ví dụ:

Giả sử có có 5 đối tượng được xếp hạng tương ứng là: c, a, e, b, d Một xếp hạng của đối tượng cần đánh giá là: c, a, e, d, b

Khi đó, $^ { \circ } ( \underline { { \omega } } 1 = 1 / 1 , \mathrm { P } @ 2 = 2 / 2 , \mathrm { P } @ 3 = 3 / 3 , \mathrm { P } @ 4 = 3 / 4 , \mathrm { P } @ 5 = 3 / 5 .$

$$
\begin{array} { l } { { \displaystyle \mathrm { A P } = ( \frac 1 1 + \frac 2 2 + \frac { 3 } { 3 } ) } } \\ { { \mathrm { M A P } = \ \frac { 1 } { 3 } ( \frac 1 { 1 } + \frac { 2 } { 2 } + \ \frac { 3 } { 3 } ) } } \end{array}
$$