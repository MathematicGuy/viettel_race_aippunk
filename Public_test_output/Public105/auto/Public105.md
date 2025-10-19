<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE                V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUAN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TaGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 1. Thuật toán liên quan đến Hidden Markov Model (HMM)

Các thuật toán liên quan đến HMM là trung tâm của việc áp dụng mô hình trong các bài toán thực tiễn. Dưới đây là ba thuật toán quan trọng, mỗi thuật toán giải quyết một trong ba bài toán cơ bản của HMM.

1.1. Thuật toán Forward và Backward

1.1.1. Mục đích:

Tính xác suất của một chuỗi quan sát $\mathrm { O } { = } \{ \mathrm { O } _ { 1 } , \mathrm { O } _ { 2 } , . . . , \mathrm { O } _ { \mathrm { T } } \}$ dựa trên một mô hình HMM $\scriptstyle \lambda = ( \operatorname { A } , \operatorname { B } , \pi )$ .

# 1.1.2. Thuật toán Forward

Forward algorithm tính xác suất $\mathrm { P } ( \mathrm { O } \mid \lambda )$ bằng cách sử dụng đệ quy.

Biến forward $\mathsf { \alpha } \mathfrak { a } _ { \mathrm { t } } ( \mathrm { i } )$ : Xác suất của chuỗi quan sát một phần $\mathbf { O } _ { 1 } , \mathbf { O } _ { 2 } , . . . , \mathbf { O } _ { 1 } \mathbf { v } \dot { 2 }$ (cid:) hệ thống $\dot { \mathbf { O } }$ trạng thái $\mathrm { S _ { i } }$ tại thời điểm t:

$$
\alpha _ { t } ( i ) = \ P ( O _ { 1 } , O _ { 2 } , \dots O _ { t } , q _ { t } = S _ { i } | \lambda )
$$

• Quy trình tính toán:

1. Khởi tạo:

2. Đ

$$
\begin{array} { r l r } & { \alpha _ { t } ( i ) = \pi _ { i } b _ { i } ( O _ { 1 } ) , 1 \le i \le N } & \\ & { \vdots \operatorname* { q u y } _ { i \in \mathcal { N } \backslash \mathcal { N } } \mathcal { N } } & \\ & { \alpha _ { t + 1 } ( j ) = \displaystyle \sum _ { i = 1 } ^ { N } \alpha _ { t } ( i ) \alpha _ { i j } b _ { j } ( O _ { t + 1 } ) , 1 \le j \le N , 1 \le t \le T - 1 } & \end{array}
$$

3. Kết thúc:

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

$$
P ( O \mid \lambda ) = \sum _ { i = 1 } ^ { N } \alpha _ { T } ( i )
$$

• Độ phức tạp: $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ .

# 1.1.3. Thuật toán Backward

Backward algorithm $\mathrm { h } \tilde { \hat { 0 } }$ trợ tính toán tương tự nhưng từ cuối chuỗi quan sát trở về đầu.

• Biến backward $\beta _ { \mathrm { t } } ( \mathrm { i } )$ : Xác suất của chuỗi quan sát từ $\mathbf { O } _ { \mathrm { t } + 1 } , \mathbf { O } _ { \mathrm { t } + 2 } , . . . , \mathbf { O } _ { \mathrm { T } } , \mathbf { v } \tilde { \mathbf { O } } \mathrm { i }$ trạng thái $\mathsf { q } _ { \mathrm { t } } { = } \mathsf { S } _ { \mathrm { i } }$ tại thời điểm t:

$$
\mathsf { \beta } _ { \mathrm { t } } ( \mathrm { i } ) = \mathrm { P } ( \mathrm { O } _ { \mathrm { t + 1 } } , \mathrm { O } _ { \mathrm { t + 2 } } , . . . , \mathrm { O } _ { \mathrm { T } } | \mathsf { q } _ { \mathrm { t } } = \mathrm { S } _ { \mathrm { i } } , \lambda )
$$

• Quy trình tính toán:

1. Khởi tạo:

$$
\beta _ { \mathrm { T } } ( \mathrm { i } ) = 1 , 1 \leq \mathrm { i } \leq \mathrm { N }
$$

2. Đệ quy:

$$
\beta _ { t } ( i ) = \sum _ { j = 1 } ^ { N } a _ { i j } b _ { j } ( O _ { t + 1 } ) \beta _ { t + 1 } ( j ) , 1 \le t \le T - 1
$$

3. Kết thúc: Tính xác suất tổng quát:

$$
P ( O \mid \lambda ) = \sum _ { i = 1 } ^ { N } \pi _ { i } b _ { i } ( O _ { 1 } ) \beta _ { 1 } ( i )
$$

• Độ phức tạp: $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$

1.2. Thuật toán Viterbi

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE              •V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUAN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

1.2.1. Mục đích:

Tìm chuỗi trạng thái ẩn tối ưu $\mathrm { Q } { * } { = } \{ \mathbf { q } _ { 1 } { } ^ { * } , \mathbf { q } _ { 2 } { } ^ { * } , { \ldots } , \mathbf { q } _ { \mathrm { T } } { } ^ { * } \}$ giải thích tốt nhất chuỗi quan sát O.

1.2.2. Quy trình tính toán:

Biến trạng thái $\delta _ { \mathrm { t } } ( \mathrm { i } )$ : Xác suất lớn nhất của chuỗi trạng thái dẫn đến $\mathrm { S _ { i } }$ tại thời điểm t:

$$
\delta _ { t } ( i ) = \operatorname* { m a x } _ { q _ { 1 } , q _ { 2 } , \ldots , q _ { t - 1 } } P ( q _ { 1 } , q _ { 2 } , \ldots , q _ { t } = S _ { i } , O _ { 1 } , O _ { 2 } , \ldots , O _ { t } \mid \lambda )
$$

• Bước thực hiện:

1. Khởi tạo:

$$
\begin{array} { r l r } & { \delta _ { 1 } ( \mathrm { i } ) = \pi \mathrm { i } \mathsf { b } _ { \mathrm { i } } ( \mathrm { O } _ { 1 } ) , } & { 1 \leq \mathrm { i } \leq \mathrm { N } } \\ & { } & \\ & { \Psi _ { 1 } ( j ) = 0 , } & { 1 \leq \mathrm { i } \leq \mathrm { N } } \end{array}
$$

2. Đệ quy:

$$
\delta _ { t + 1 } ( j ) = \mathop { m a x } _ { i } ^ { N } \delta _ { t } ( i ) a _ { i j } b _ { j } ( O _ { t + 1 } ) , \qquad 1 \leq j \leq N , 1 \leq t \leq T - 1
$$

3. Kết thúc:

$$
\begin{array} { c } { { N } } \\ { { \displaystyle \Psi _ { t + 1 } ( j ) = \arg \operatorname* { m a x } _ { i } \delta _ { t } ( i ) a _ { i j } \mathrm { ~ } , 1 \le j \le N } } \\ { { \displaystyle \bigotimes _ { i } ^ { \mathcal { R } \mathcal { O } ^ { \mathcal { O } } } i = 1 } } \\ { { \big ( Q ^ { * } , O \mid \lambda \big ) = \displaystyle \operatorname* { m a x } _ { i } \delta _ { T } ( i ) } } \end{array}
$$

$$
\begin{array} { c } { { N } } \\ { { q _ { T } ^ { * } = a r g \ m a x \ \delta _ { T } ( i ) } } \\ { { i = 1 } } \end{array}
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

4. Truy vết trạng thái tối ưu:

$$
q _ { t } ^ { * } = \Psi _ { t + 1 } ( q _ { t + 1 } ^ { * } ) , t = T - 1 , T - 2 , \dots , 1
$$

• Độ phức tạp: $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ .

# 2. Các giả định của Hidden Markov Model (HMM)

Hidden Markov Model (HMM) dựa trên hai giả định cơ bản, giúp đơn giản hóa việc mô hình hóa và tính toán xác suất trong các bài toán thực tế. Mặc dù những giả định này có thể không hoàn toàn chính xác trong mọi trường hợp, chúng vẫn đủ mạnh để mô tả nhiều hệ thống thực tế một cách hiệu quả.

2.1. Giả định Markov (Markov Assumption)

2.1.1. Định nghĩa:

Giả định Markov phát biểu rằng trạng thái hiện tại qtq_tqt chỉ phụ thuộc vào trạng thái ngay trước đó $\mathbf { q } _ { \mathrm { t } ^ { - 1 } }$ , không phụ thuộc vào các trạng thái trước đó trong chuỗi.

$$
\operatorname { P } ( \operatorname { q } _ { \mathrm { t } } | \mathbf { q } _ { \mathrm { t - 1 } } , \mathbf { q } _ { \mathrm { t - 2 } } , \dots , \mathbf { q } _ { \mathrm { 1 } } ) = \operatorname { P } ( \mathbf { q } _ { \mathrm { t } } \mid \mathbf { q } _ { \mathrm { t - 1 } } )
$$

# 2.1.2. Ý nghĩa:

Giả định này giảm độ phức tạp của mô hình, chỉ yêu cầu xét mối quan hệ giữa hai trạng thái liên tiếp thay vì toàn bộ chuỗi trạng thái.

Trong thực tế, giả định Markov có thể hiểu là một hệ thống "có trí nhớ ngắn hạn", nơi trạng thái hiện tại chứa đủ thông tin để dự đoán trạng thái tiếp theo.

# 2.1.3. Hạn chế:

Hệ thống thực tế có thể bị ảnh hưởng bởi nhiều trạng thái trong quá khứ, không chỉ bởi trạng thái ngay trước đó. Tuy nhiên, việc tăng bậc của mô hình Markov (Markov bậc cao hơn) có thể giúp giảm bớt hạn chế này, nhưng làm tăng độ phức tạp tính toán.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE                V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUAN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TaGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

2.2. Giả định độc lập quan sát (Independence Assumption)

2.2.1. Định nghĩa:

Giả định này cho rằng mỗi quan sát OtO_tOt tại thời điểm ttt chỉ phụ thuộc vào trạng thái hiện tại qtq_tqt, không phụ thuộc vào các quan sát khác hoặc các trạng thái khác trong chuỗi.

$$
\mathrm { P } ( \mathrm { O } _ { \mathrm { t } } \mid \mathrm { q } _ { \mathrm { t } } , \mathrm { q } _ { \mathrm { t } - 1 } , \mathrm { O } _ { \mathrm { t } - 1 } , \dots ) = \mathrm { P } ( \mathrm { O } _ { \mathrm { t } } \mid \mathrm { q } _ { \mathrm { t } } )
$$

# 2.2.2. Ý nghĩa:

Giả định này cho phép ta mô hình hóa mối quan hệ giữa trạng thái ẩn và quan sát một cách độc lập, giảm đáng $\mathrm { k } \mathring { \mathrm { e } }$ độ phức tạp khi tính toán xác suất.   
Đây là một trong những lý do HMM được áp dụng rộng rãi trong các bài toán như nhận dạng giọng nói và gắn thẻ từ loại.

2.2.3. Hạn chế:

• Trong thực tế, các quan sát thường có mối liên hệ phụ thuộc với nhau, đặc biệt trong các chuỗi dữ liệu có tính chất tuần tự cao. Giả định này có thể không hoàn toàn chính xác, nhưng thường được chấp nhận để đơn giản hóa mô hình.

Hai giả định Markov và độc lập quan sát là nền tảng của Hidden Markov Model, giúp mô hình này trở thành một công cụ đơn giản nhưng mạnh mẽ để mô tả các chuỗi dữ liệu tuần tự. Mặc dù có những hạn chế nhất định, chúng cho phép HMM áp dụng hiệu quả trong các bài toán thực tế với độ phức tạp tính toán thấp.

3. Ứng dụng của Hidden Markov Model (HMM) vào Gắn thẻ từ loại (POS Tagging)

Gắn thẻ từ loại (Part-of-Speech Tagging - POS Tagging) là một bài toán quan trọng trong xử lý ngôn ngữ tự nhiên (NLP), nhằm gán nhãn ngữ pháp (danh từ, động từ, tính từ,...) cho từng từ trong câu. Hidden Markov Model (HMM) là một phương pháp phổ biến để giải quyết bài toán này nhờ khả năng mô hình hóa chuỗi trạng thái ẩn (các nhãn từ loại) dựa trên chuỗi quan sát (các từ trong câu).

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 3.1. Mô hình HMM cho POS Tagging

Để áp dụng HMM vào bài toán POS Tagging, chúng ta cần xác định các thành phần của mô hình:

Tập trạng thái ẩn (S): o Là tập các nhãn từ loại (POS tags), ví dụ: $\mathrm { S } { = } \{ \mathrm { N N }$ (danh từ),VB (động từ),JJ (tính từ),… }. Tập quan sát (O):   
o Là tập các từ trong câu, ví dụ: $O = \left\{ \begin{array} { r l } \end{array} \right.$ {The, cat, runs, fast} Phân phối xác suất ban đầu $( \pmb { \pi } )$ :   
o Xác suất một từ trong câu bắt đầu với một từ loại cụ thể: $\pi _ { \mathrm { i } } { = } \mathrm { P } ( \mathrm { S } _ { 1 } { = } \mathrm { i } )$ Ví dụ: Một câu thường bắt đầu bằng các nhãn như DT (mạo từ) hoặc NN (danh từ).   
Ma trận chuyển trạng thái (A):   
o Xác suất chuyển từ nhãn từ loại này sang nhãn từ loại khác: $\mathrm { a _ { i j } { = } P ( S _ { t + 1 } { = } j | S _ { t } { = } i ) }$ Ví dụ: Sau một danh từ (NN), khả năng cao sẽ là một động từ (VB) hoặc mạo từ (DT). Ma trận xác suất phát xạ (B):   
o Xác suất một nhãn từ loại phát sinh một từ cụ thể: $\mathsf { b } _ { \mathrm { j } } ( \mathrm { O } _ { \mathrm { t } } ) { = } \mathsf { P } ( \mathrm { O } _ { \mathrm { t } } | \mathsf { S } _ { \mathrm { t } } { = } \mathrm { j } )$ Ví dụ: Xác suất từ "runs" thuộc nhãn động từ (VB) sẽ cao hơn các nhãn khác.

3.2. Thuật toán Viterbi để giải bài toán POS Tagging

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

POS Tagging sử dụng thuật toán Viterbi để tìm chuỗi nhãn từ loại tối ưu $\mathbf { S } { } ^ { * } { = } \{ \mathbf { S } _ { 1 } { } ^ { * } , \mathbf { S } _ { 2 } { } ^ { * } , { \ldots } , \mathbf { S } _ { \mathrm { T } } { } ^ { * } \}$ tương ứng với chuỗi quan sát $\mathrm { O } { = } \{ \mathrm { O } _ { 1 } , \mathrm { O } _ { 2 } , . . . , \mathrm { O } _ { \mathrm { T } } \}$ .

Quy trình thực hiện:

B1: Khởi tạo: Tại thời đi $\dot { \mathrm { e m } } \mathrm { t } { = } 1$ :

$$
\delta _ { 1 } ( \mathrm { i } ) { = } { \pi } _ { \mathrm { i } } { \cdot } { \mathrm b } _ { \mathrm { i } } ( \mathrm { O } _ { 1 } ) , \ \mathrm { \psi } _ { \mathrm { } } \mathrm { = } 0
$$

o δ1(i): Xác suất lớn nhất khi bắt đầu với trạng thái $\mathrm { S _ { i } }$ . o $\Psi _ { 1 } ( \mathrm { i } )$ : Truy vết trạng thái trước đó, tại thời điểm khởi đầu, giá trị này bằng 0.

B2: Đệ quy: Từ $\scriptstyle { \mathrm { t } = 2 }$ đến T (số lượng từ trong câu): $\delta _ { t } ( j ) = \operatorname* { m a x } _ { i } \bigl [ \delta _ { t - 1 } ( i ) \cdot a _ { i j } \cdot b _ { j } ( O _ { t } ) \bigr ] , \Psi _ { t } ( j ) = a r g \operatorname* { m a x } _ { i } \bigl [ \delta _ { t - 1 } ( i ) \cdot a _ { i j } \bigr ]$ o δt(j): Xác suất lớn nhất dẫn đến trạng thái $\mathrm { S _ { j } }$ tại thời điểm t. o $\Psi _ { \mathrm { t } } ( \dot { \mathrm { J } } )$ : Truy vết trạng thái $\mathrm { S _ { i } }$ tốt nhất trước $\mathrm { S _ { j } }$ .

B3: Kết thúc: Tại thời điểm cuối T:

$$
S _ { T } ^ { * } = \ a r g \operatorname* { m a x } _ { i } \delta _ { T } ( i )
$$

B4: Truy vết: Từ t=T−1 đến t=1:

$$
\begin{array} { r l r } & { } & { \qquad \mathrm { S } _ { t } ^ { s } = \Psi _ { t + 1 } ( S _ { t + 1 } ^ { * } ) } \\ & { } & { \qquad \mathrm { S } _ { t } ^ { s } } \\ & { } & { \qquad \mathrm { S } _ { t + \tau + \eta ( t + 1 \ast ) \mathrm { S } _ { - } \mathrm { t } ^ { s + \tau } } = \mathrm { s p s i } _ { - } \{ \mathrm { t } + 1 \} ( \mathrm { S } _ { - } \{ \mathrm { t } + 1 \} \wedge \ast ) \mathrm { S } _ { \mathrm { t } \ast - \eta ( t + 1 \ast ) } ^ { 0 \ast - \eta ( t + 1 \ast ) } } \\ & { } & \end{array}
$$

o Kết quả là chuỗi nhãn từ loại tối ưu $\mathbf { S } { } { } ^ { * } { = } \{ \mathbf { S } _ { \mathrm { 1 } } { } ^ { * } , \mathbf { S } _ { 2 } { } ^ { * } , { \ldots } , \mathbf { S } _ { \mathrm { T } } { } ^ { * } \}$ .

3.3. Ví dụ minh họa

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

Đề bài: Cho câu quan sát:

Với tập nhãn từ loại:

Các tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { 0 } }$ hình:

$\scriptstyle \pi = \{ \mathrm { P } ( \mathrm { D T } ) = 0 . 6 , \mathrm { P } ( \mathrm { N N } ) = 0 . 3 , \mathrm { P } ( \mathrm { V B } ) = 0 . 1 \} .$ . Ma trận chuyển trạng thái:

$$
\begin{array} { r l } { A = [ P ( D T  D T ) \quad P ( D T  N N ) \quad P ( D T  V B ) ] = } & { { } } \\ { P ( N N  D T ) } & { { } P ( N N  N N ) \quad P ( N N  V B ) \quad = } \\ { P ( V B  D T ) } & { { } P ( V B  N N ) \quad P ( V B  V B ) } \end{array}
$$

• Ma trận phát xạ:

$$
\begin{array} { r l } & { B = [ P ( O \mid D T ) ] = } \\ & { P ( O \mid V N ) ] = } \\ & { [ P ( O \mid V B ) ] } \\ & { [ P ^ { ( " \mathrm { T h e " } ) } = 0 . 5 , P ^ { ( " \mathrm { c a t " } ) } = 0 . 1 , P ^ { ( " r u n s " ) } = 0 . 1 ] } \\ & { [ P ^ { ( " \mathrm { T h e " } ) } = 0 . 1 , P ^ { ( " \mathrm { c a t " } ) } = 0 . 6 , P ^ { ( " r u n s " ) } = 0 . 1 ] } \\ & { [ P ^ { ( " \mathrm { T h e " } ) } = 0 . 1 , P ^ { ( " \mathrm { c a t " } ) } = 0 . 1 , P ^ { ( " r u n s " ) } = 0 . 8 ] } \end{array}
$$

# Giải:

Khởi tạo:

$$
\begin{array} { r l } & { \delta _ { 1 } ( D T ) = \pi _ { D T } \cdot b _ { D T } ( ^ { \ " } \mathrm { T h e " } ) = 0 . 6 \cdot 0 . 5 = 0 . 3 } \\ & { } \\ & { \delta _ { 1 } ( N N ) = \pi _ { N N } \cdot b _ { N N } ( ^ { \ " } \mathrm { T h e " } ) = 0 . 3 \cdot 0 . 1 = 0 . 0 3 } \end{array}
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE               V</td><td rowspan=1 colspan=1>Public 105</td></tr><tr><td rowspan=1 colspan=1>THUAT TOAN LIEN QUaN DÉN HIDDENMARKOV MODEL (HMM), CAC GIA DINH &amp; UNGDUNG VAO POS TAGGING</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

$$
\delta _ { 1 } ( V B ) = \pi _ { V B } \cdot b _ { V B } ( " \mathrm { T h e " } ) = 0 . 1 \cdot 0 . 1 = 0 . 0 1
$$

• $\mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { D } \hat { \mathbf { e } }$ quy (tại $\scriptstyle { \mathfrak { t } } = 2$ ):

$$
\begin{array} { r } { \delta _ { 2 } ( N N ) = m a x [ \delta _ { 1 } ( D T ) \cdot a _ { D T  N N } , \delta _ { 1 } ( N N ) \cdot a _ { N N  N N } , \delta _ { 1 } ( V B ) \cdot a _ { V B  N N } ] } \\ { \cdot b _ { N N } ( ^ { \circ } c a t ^ { \prime \prime } ) \qquad } \end{array}
$$

# • Tiếp tục:

Lặp lại các bước trên cho đến $\mathrm { t } { = } 3$ để tìm chuỗi nhãn tối ưu.