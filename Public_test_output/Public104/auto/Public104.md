<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIOI THIEU VE HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

# 1. Khái niệm cơ bản về Hidden Markov Model (HMM)

Hidden Markov Model (HMM) là một mô hình thống kê được sử dụng để phân tích các chuỗi dữ liệu có tính chất tuần tự, trong đó trạng thái thực của hệ thống (trạng thái ẩn) không thể quan sát trực tiếp, nhưng có thể suy ra thông qua các quan sát (observations). HMM kết hợp hai quá trình ngẫu nhiên:

Một quá trình Markov ẩn, mô tả sự chuyển đổi giữa các trạng thái ẩn. Một quá trình phát xạ, liên kết mỗi trạng thái ẩn với một tập các quan sát theo một phân phối xác suất.

HMM thường được biểu diễn thông qua các thành phần sau:

Tập trạng thái ẩn (Hidden States): Đại diện cho các trạng thái không quan sát được của hệ thống. Ma trận xác suất chuyển trạng thái (State Transition Matrix): Xác định xác suất chuyển từ một trạng thái ẩn này sang trạng thái ẩn khác. Ma trận xác suất phát xạ (Emission Probability Matrix): Mô tả xác suất của một quan sát cụ thể dựa trên trạng thái hiện tại. Phân phối xác suất ban đầu (Initial State Distribution): Xác định trạng thái khởi đầu của hệ thống.

# 2. Sự khác biệt giữa Markov Chain và HMM

Markov Chain là một mô hình toán học đơn giản hơn HMM, trong đó:

• Trạng thái của Markov Chain là có thể quan sát trực tiếp. Xác suất chuyển trạng thái chỉ phụ thuộc vào trạng thái hiện tại, không quan tâm đến các trạng thái trước đó.

Ngược lại, HMM phức tạp hơn:

• Trạng thái ẩn của HMM không thể quan sát trực tiếp, mà chỉ có thể suy đoán thông qua các quan sát.   
HMM bổ sung thêm quá trình phát xạ, liên kết các trạng thái ẩn với dữ liệu quan sát.

Ví dụ minh họa: Trong Markov Chain, nếu ta đang xem một chuỗi các điều kiện thời tiết (nắng, mưa), bạn có thể quan sát trực tiếp điều kiện thời tiết tại từng thời điểm. Trong HMM, các điều kiện thời tiết có thể được ẩn (không trực tiếp quan sát được), nhưng ta có thể suy luận từ các quan sát như mức độ ẩm, nhiệt độ, hoặc áp suất không khí.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIÓI THIEU VE HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

# 2.1. Vai trò và ứng dụng của HMM trong các bài toán thực tiễn

HMM đóng vai trò quan trọng trong nhiều lĩnh vực nghiên cứu và ứng dụng, đặc biệt là trong xử lý chuỗi dữ liệu. Một số ứng dụng điển hình của HMM bao gồm:

# 2.1.1. Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP):

o Gắn thẻ từ loại (POS Tagging): Dự đoán nhãn ngữ pháp (danh từ, động từ,...) của các từ trong câu.   
o Nhận dạng thực thể (Named Entity Recognition): Xác định tên riêng, địa danh, hoặc tổ chức trong văn bản.

# 2.1.2. Nhận dạng giọng nói (Speech Recognition):

o Mô hình hóa các chuỗi âm thanh để chuyển đổi thành văn bản.

# 2.1.3. Phân tích sinh học (Bioinformatics):

o Dự đoán cấu trúc protein từ chuỗi axit amin.   
o Phân tích trình tự DNA để xác định gen.

# 2.1.4. Phát hiện bất thường (Anomaly Detection):

o Dự đoán lỗi trong hệ thống máy tính hoặc mạng lưới.   
o Phát hiện gian lận trong các giao dịch tài chính.

# 2.1.5. Ứng dụng trong thời gian thực:

o Phân tích dữ liệu cảm biến trong hệ thống IoT (Internet of Things). o Dự đoán trạng thái hoạt động trong các hệ thống điều khiển tự động.

công cụ mạnh mẽ trong việc mô hình hóa các quá trình phức tạp mà các trạng thái ẩn không thể quan sát trực tiếp.

# 2.2. Cấu trúc cơ bản của Hidden Markov Model

2.2.1. Mô hình Markov và trạng thái ẩn

<table><tr><td rowspan=2 colspan=1>xi</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIOI THIEU VÉ HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

Hidden Markov Model (HMM) là sự mở rộng của mô hình Markov truyền thống, trong đó trạng thái của hệ thống không thể quan sát trực tiếp, mà chỉ có thể được suy luận từ các quan sát (emissions). Một hệ thống được mô tả bởi HMM có các trạng thái ẩn liên kết với một tập hợp các quan sát cụ thể thông qua xác suất phát xạ.

Trong HMM, hai quá trình ngẫu nhiên được kết hợp:

Quá trình Markov ẩn: Mô tả sự chuyển đổi giữa các trạng thái ẩn theo xác suất.   
Quá trình phát xạ: Liên kết mỗi trạng thái ẩn với các quan sát thông qua phân phối xác suất phát xạ.

HMM thường được biểu diễn dưới dạng một đồ thị có hướng, trong đó các nút là trạng thái và các cạnh thể hiện xác suất chuyển đổi giữa các trạng thái.

2.2.2. Các thành phần chính của HMM

Một HMM được định nghĩa bởi bốn thành phần chính:

2.2.3. Tập trạng thái (Hidden States)

Tập trạng thái ẩn của HMM được ký hiệu là $\mathrm { S } { = } \{ \mathrm { S } _ { 1 } , \mathrm { S } _ { 2 } { , \ldots } , \mathrm { S } _ { \mathrm { N } } \}$ , trong đó:

• Si: Trạng thái ẩn thứ iii.   
• N: Số lượng trạng thái ẩn.

Tại mỗi thời điểm, hệ thống sẽ nằm ở một trong các trạng thái $\mathrm { S _ { i } }$ , nhưng trạng thái này không thể quan sát trực tiếp mà chỉ có thể suy ra từ các quan sát.

Ví dụ: Trong bài toán nhận dạng giọng nói, các trạng thái ẩn có thể là các âm vị (phonemes) mà người nói đang phát âm.

2.2.4. Ma trận chuyển trạng thái (State Transition Matrix)

Ma trận chuyển trạng thái, ký hiệu là A=[aij], là một ma trận vuông kích thước $\mathbf { N } { \times } \mathbf { N } _ { ; }$ , trong đó:

• $\mathrm { { a } _ { i j } { = } \mathrm { { P } ( \mathrm { { S } _ { j } | \mathrm { { S } _ { i } ) } } } }$ : Xác suất chuyển từ trạng thái $\mathrm { S _ { i } }$ sang trạng thái $\mathrm { S _ { j } }$ .   
• $\textstyle \sum _ { j = 1 } ^ { N } a _ { i j }$ = 1: Tổng các xác suất từ một trạng thái phải bằng 1.

Ma trận A biểu diễn các mối quan hệ giữa các trạng thái ẩn trong mô hình.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIOI THIEU VE HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

Ví dụ: Trong một chuỗi thời tiết, xác suất chuyển từ trạng thái "nắng" sang "mưa" là một phần của ma trận chuyển trạng thái.

2.2.5. Ma trận xác suất phát xạ (Emission Probability Matrix)

Ma trận xác suất phát xạ, ký hiệu là $\scriptstyle \mathrm { B = } [ \mathrm { b } _ { \mathrm { j } } ( \mathrm { k } ) ]$ , là một ma trận kích thước $\mathbf { N } { \times } \mathbf { M } .$ , trong đó:

• $\mathsf { b } _ { \mathrm { j } } ( \mathbf { k } ) = \mathsf { P } ( \mathbf { O } _ { \mathrm { k } } \mid \mathbf { S } _ { \mathrm { j } } )$ : Xác suất quan sát $\mathrm { O _ { k } }$ xảy ra khi hệ thống ở trạng thái Sj. • $ \mathrm { O } = \{ \mathrm { O } _ { 1 } , \mathrm { O } _ { 2 } , . . . , \mathrm { O } _ { \mathrm { M } } \}$ : Tập các quan sát có thể xảy ra, với M là số lượng quan sát.

Ma trận B mô tả mối quan hệ giữa trạng thái ẩn và quan sát.

Ví dụ: Trong bài toán nhận dạng giọng nói, các quan sát có thể là các đặc trưng âm thanh (spectral features) được trích xuất từ tín hiệu âm thanh.

2.2.6. Phân phối xác suất ban đầu (Initial State Distribution)

Phân phối xác suất ban đầu, ký hiệu là $\pi { = } \{ \pi _ { 1 } , \pi _ { 2 } , . . . , \pi _ { \mathrm { N } } \}$ , trong đó:

• πi = P(Si): Xác suất hệ thống bắt đầu $\dot { \mathbf { O } }$ trạng thái $\mathrm { S _ { i } }$ .   
• $\begin{array} { r } { \sum _ { i = 1 } ^ { N } \pi _ { i } = 1 } \end{array}$ : Tổng xác suất của tất cả các trạng thái ban đầu phải bằng 1.

Phân phối $\pi$ cung cấp thông tin $\mathrm { v } \dot { \hat { \mathrm { e } } }$ trạng thái khởi đầu của hệ thống trước khi các quan sát được thực hiện.

# 2.3. Công thức tổng quát của HMM

Một HMM được định nghĩa bởi các tham ${ \hat { \mathbf { s } } } { \hat { \hat { 0 } } } \ { \hat { \lambda } } { \mathbf { = } } ( { \mathbf { A } } , { \mathbf { B } } , \pi )$ , trong đó:

• $\mathrm { A } = \left[ \mathrm { a } _ { \mathrm { i j } } \right]$ : Ma trận chuyển trạng thái.   
• $\mathbf { B } = [ \mathrm { b } _ { \mathrm { j } } ( \mathrm { k } ) ]$ : Ma trận xác suất phát xạ.   
• $\pi = \{ \pi \} $ : Phân phối xác suất ban đầu.

Cho một chuỗi quan sát $\mathrm { O = \{ O _ { 1 } , O _ { 2 } , . . . , O _ { T } \} }$ với chiều dài T, xác suất của chuỗi quan sát được tính theo công thức:

$$
\begin{array} { r } { P ( O \mid \lambda ) = \sum _ { Q } P ( O , Q \mid \lambda ) = \sum _ { Q } P ( Q \mid \lambda ) \cdot \operatorname { P } \left( 0 \mid Q , \lambda \right) } \end{array}
$$

Trong đó:

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIOI THIEU VÉ HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

• $\mathrm { Q } = \{ \mathrm { S } _ { \mathrm { q 1 } } , \mathrm { S } _ { \mathrm { q 2 } } , . . . , \mathrm { S } _ { \mathrm { q T } } \}$ : Một chuỗi trạng thái ẩn.   
• Tổng $\Sigma _ { \mathrm { Q } }$ được tính trên tất cả các chuỗi trạng thái có thể xảy ra.

Công thức này cho phép ta tính xác suất quan sát của một chuỗi và xác định chuỗi trạng thái ẩn tối ưu.

# 3. Ba bài toán cơ bản của Hidden Markov Model (HMM)

Hidden Markov Model (HMM) được sử dụng để giải quyết ba bài toán cơ bản trong các ứng dụng thực tế. Các bài toán này là trung tâm của việc áp dụng HMM vào việc phân tích dữ liệu tuần tự. Dưới đây là chi tiết từng bài toán.

3.1.Bài toán 1: Đánh giá (Evaluation)

# Mục tiêu:

Tính xác suất của một chuỗi quan sát $\mathrm { O } { = } \{ \mathrm { O } _ { 1 } , \mathrm { O } _ { 2 } , . . . , \mathrm { O } _ { \mathrm { T } } \}$ đã cho, dựa trên mô hình HMM $\scriptstyle \lambda = ( \operatorname { A } , \operatorname { B } , \pi )$ .

# Ý nghĩa:

Bài toán này giúp đánh giá mức độ phù hợp của một chuỗi quan sát với một mô hình HMM cụ thể. Đây là bước cần thiết để so sánh và lựa chọn mô hình tốt nhất từ các mô hình cạnh tranh.

# Công thức:

Xác suất của chuỗi quan sát $\mathrm { P } ( \mathrm { O } \mid \lambda )$ được tính bằng cách tổng hợp xác suất trên tất cả các chuỗi trạng thái ẩn $\mathrm { Q } { = } \{ \mathsf { q } _ { 1 } , \mathsf { q } _ { 2 } , { \ldots } { \ldots } \mathsf { q } _ { \mathrm { T } } \}$ :

$$
P ( O \mid \lambda ) = \sum _ { Q } P ( P , Q \mid \lambda )
$$

# Thách thức:

Việc tính toán trực tiếp rất phức tạp, vì số lượng các chuỗi trạng thái Q tăng theo hàm mũ với chiều dài T của chuỗi quan sát.

# Giải pháp:

Sử dụng thuật toán Forward:

• Thuật toán này tính toán xác suất một cách hiệu quả bằng cách sử dụng phương pháp đệ quy. Độ phức tạp được giảm từ $\mathrm { O } ( \mathrm { N } ^ { \mathrm { T } } )$ xuống $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ , trong đó N là số trạng thái ẩn.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIÓI THIEU VE HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

3.2. Bài toán 2: Giải mã (Decoding)

# Mục tiêu:

Tìm chuỗi trạng thái ẩn tối ưu $\mathrm { Q } { * } { = } \{ \mathbf { q } _ { 1 } { } ^ { * } , \mathbf { q } _ { 2 } { } ^ { * } , { \ldots } , \mathbf { q } _ { \mathrm { T } } { } ^ { * } \}$ tương ứng với chuỗi quan sát O, sao cho:

$$
Q ^ { * } = a r g \operatorname* { m a x } _ { Q } P ( Q \mid O , \lambda )
$$

# Ý nghĩa:

Bài toán này giúp xác định chuỗi trạng thái ẩn khả dĩ nhất, giải thích tốt nhất cho chuỗi quan sát. Đây là một bước quan trọng trong các ứng dụng như nhận dạng giọng nói và phân tích chuỗi sinh học.

# Thách thức:

Việc tìm kiếm chuỗi trạng thái tối ưu yêu cầu tối ưu hóa toàn cục trên toàn bộ chuỗi thời gian.

# Giải pháp:

Sử dụng thuật toán Viterbi:

• Thuật toán này dựa trên lập trình động, tìm chuỗi trạng thái tối ưu bằng cách lưu trữ các giá trị tối đa tại mỗi bước.   
• Độ phức tạp của thuật toán là $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ .

3.3. Bài toán 3: Học (Learning)

# Mục tiêu:

Ước lượng các tham số của mô hình $\scriptstyle \lambda = ( \operatorname { A } , \operatorname { B } , \pi )$ từ một tập dữ liệu quan sát ${ \mathrm { O } } { = } \{ { \mathrm { O } } ^ { ( 1 ) } , { \mathrm { O } } ^ { ( 2 ) } , { \dots } , { \mathrm { O } } ^ { ( \mathrm { K } ) } \}$ .

# Ý nghĩa:

Bài toán này giúp xây dựng một mô hình HMM phù hợp từ dữ liệu quan sát, phục vụ cho việc phân tích và dự đoán.

# Thách thức:

Không thể tối ưu trực tiếp P(O∣λ) vì các trạng thái ẩn không được quan sát trực tiếp.

# Giải pháp:

Sử dụng thuật toán Baum-Welch hoặc Expectation-Maximization (EM):

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 104</td></tr><tr><td rowspan=1 colspan=1>GIÓI THIEU VE HIDDEN MARKOV MODEL</td><td rowspan=1 colspan=1>Làn   banhành: 1</td></tr></table>

• Thuật toán này lặp lại hai bước:

1. E-step (Expectation): Tính xác suất kỳ vọng cho các trạng thái ẩn dựa trên các tham số hiện tại.   
2. M-step (Maximization): Cập nhật các tham số $\mathbf { A } , \mathbf { B } , \pi$ để tối đa hóa xác suất quan sát $\mathrm { P } ( \mathrm { O } | \lambda )$ .

• Thuật toán hội tụ đến một cực đại cục của $\mathrm { P } ( \mathrm { O } | \lambda )$ .