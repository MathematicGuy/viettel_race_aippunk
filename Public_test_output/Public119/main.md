

# Giới thiệu

Trong hai bài viết trước, PCA (unsupervised) giữ lại tổng phương sai lớn nhất nhưng không dùng nhãn. Trong phân lớp (supervised), tận dụng nhãn thường cho kết quả tốt hơn. Ví dụ chiếu lên các hướng d1 (gần PC1) và d2 (gần thành phần phụ): d1 có thể làm hai lớp chồng lấn, trong khi d2 tách tốt hơn cho classification. Điều này cho thấy giữ lại nhiều phương sai nhất không phải lúc nào cũng tốt cho phân lớp. LDA ra đời để tìm phép chiếu tuyến tính (projection matrix) tối đa hóa khả năng phân biệt (discriminant). Với C lớp, số chiều mới không vượt quá C−1.

# LDA cho bài toán với 2 classes

## Ý tưởng cơ bản

Discriminant tốt khi: (i) mỗi lớp tập trung (within-class variance nhỏ), (ii) các lớp cách xa nhau (between-class variance lớn).

## Xây dựng hàm mục tiêu

Ký hiệu: dữ liệu $x \_ n$ , phép chiếu $y \_ n = w { \wedge } T x \_ n .$

Kỳ vọng mỗi lớp: m $\underline { { \mathbf { \Pi } } } _ { - } \mathbf { k } = ( 1 / \mathbf { N } \underline { { \mathbf { \Pi } } } _ { - } \mathbf { k } ) \sum _ { - } \{ \mathfrak { n } { \in } \mathbf { C } \underline { { \mathbf { \Pi } } } _ { - } \mathbf { k } \} \mathbf { x } \underline { { \textbf { \Pi } } } _ { - } \mathbf { n }$ , k=1,2. (1)

Hiệu kỳ vọng sau chiếu: $\mathrm { m } \_ 1 - \mathrm { m } \_ 2 \Rightarrow \mathrm { w } ^ { \wedge } \mathrm { T } ( \mathrm { m } \_ 1 - \mathrm { m } \_ 2 ) .$ (2)

Within-class variances (không lấy trung bình): $\scriptstyle \mathtt { s \_ k } \wedge 2 = \sum _ { - } \{ \mathtt { n } \in \mathbb { C } \_ \mathrm { k } \} ( \mathtt { y \_ n } -$ $\mathrm { ~ m ~ } \mathbf { k } ) \mathord { \uparrow } 2$ . (3)

Ma trận between-class: $\mathrm { S \_ B } = ( \mathrm { m \_ l } - \mathrm { m \_ } 2 ) ( \mathrm { m \_ l } - \mathrm { m \_ } 2 ) ^ { \wedge } \mathrm { T } .$ (5)

Ma trận within-class: $\begin{array} { r l r } { \mathrm { S } _ { - } \mathrm { W } } & { { } = } & { \sum _ { - } \{ \mathrm { k } { = } 1 \} { \wedge } 2 } \end{array}$ ∑_{n∈C_k} $( \mathrm { x \_ n - m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ n - m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } m \mathrm { \underline { { ~ \cdot ~ } } } m \mathrm { \underline { { ~ \cdot ~ } } } } } } } } } } } } } } } $ (6)

Hàm mục tiêu Fisher $( 2 \ : \mathbf { l i } \delta \mathbf { p } )$ :

$$
\mathrm { J ( w ) } = ( \mathrm { w } ^ { \wedge } \mathrm { T } \mathrm { S } \_ { \mathbf { B } } \mathrm { w } ) / ( \mathrm { w } ^ { \wedge } \mathrm { T } \mathrm { S } \_ { \mathbf { W } } \mathrm { w } ) .
$$

## Nghiệm tối ưu (Fisher’s linear discriminant)

Đạo hàm và sắp xếp lại:

$$
\mathrm { S \_ W \wedge \{ - 1 \} \setminus S \_ B \ w = J ( w ) \ w . }
$$

Chọn nghiệm tỷ lệ:

$$
{ \bf w } = { \bf { \alpha } } { \bf S \_ W } { \bf \wedge } \{ - 1 \} ( { \bf m \_ 1 } - { \bf m \_ 2 } ) , { \bf \alpha } { \bf { \alpha } } { \bf { \alpha } } { \bf { 0 } } .
$$

# LDA cho multi-class classification

Phép chiếu tuyến tính: $\mathbf { y } = \mathbf { W } \mathbf { \land } \mathbf { T } \mathbf { \land }$ , $\mathrm { W } \in \mathrm { R } ^ { \wedge } \{ \mathrm { D } { \times } \mathrm { D } ^ { \prime } \}$ . Không dùng bias. Within-class tổng quát:



$\mathbf { s } \_ { \mathbf { W } } =$ trace(W^T S_W W), với S_W = ∑_{k=1}^C ∑_{n∈C_k} (x_n − $\underline { { { \mathrm { ~ m ~ k ~ } } } } ) ( \underline { { { \mathrm { ~ x ~ } } } } \underline { { { \mathrm { ~ n ~ } } } } - \underline { { { \mathrm { ~ m ~ } } } } \underline { { { \mathrm { ~ k ~ } } } } ) { \mathrm { { ~ \hat { T } } } } .$ (17–19)

# Between-class tổng quát:

$\mathbf { s } \_ { \mathbf { B } } =$ trace(W^T S_B W), với S_B = ∑_{k=1}^C N_k (m_k − m)(m_k − $\mathrm { m } ) { } ^ { \wedge } \mathrm { T }$ . (21–22)

Hàm mục tiêu multi-class:

$$
\operatorname { J } ( \mathbb { W } ) = \operatorname { t r a c e } ( \mathbb { W } \wedge \operatorname { T } \operatorname { S } _ { - } \operatorname { B } \mathbb { W } ) / \operatorname { t r a c e } ( \mathbb { W } ^ { \wedge } \operatorname { T } \operatorname { S } _ { - } \mathbb { W } \mathbb { W } ) .
$$

Điều kiện tối ưu bậc nhất:

$$
\mathrm { S \_ W } { \setminus } \{ - 1 \} \mathrm { S \_ B } \mathrm { W } = \mathrm { J } \mathrm { W } .
$$

Các cột của $W$ là các eigenvectors ứng với các trị riêng lớn nhất của $S \_ W \wedge \{ - I \} \ S \_ B$ .

Bổ đề: rank $\langle ( S \_ B ) \leq C - I \Rightarrow s \acute { \partial }$ chiều tối đa sau $L D A \leq C - I$ .

# Ví dụ nhanh (Python, phác thảo)

• Tạo dữ liệu 2 lớp: $X 0 , X I \in R \land \{ N \land D \}$ ; tính m0, m1.

$$
\bullet S _ { \_ B } = ( m O - m I ) ( m O - m I ) ^ { \wedge } T ; S _ { \_ B } = \sum ( x - m _ { \_ } k ) ( x - m _ { \_ } k ) ^ { \wedge } T .
$$

• W từ eigenvectors của $i n \nu ( S \_ W ) \textcircled { a } S \_ B ,$ so sánh sklearn.discriminant_analysis.LDA.

# Thảo luận

LDA là phương pháp supervised giảm chiều và/hoặc phân lớp: tối ưu small within-class & large between-class. Số chiều tối đa sau LDA $\mathrm { l } \dot { \mathrm { a } } \le \mathrm { C } ^ { - 1 }$ . Giả định thường gặp: phân phối gần Gaussian, các ma trận hiệp phương sai giữa các lớp gần nhau. LDA tốt khi các lớp gần linearly separable; kém hiệu quả nếu không tách tuyến tính.