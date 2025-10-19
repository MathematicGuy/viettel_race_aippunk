

# Định nghĩa:

Attention là một kĩ thuật được sử dụng trong các mạng neural, kỹ thuật này được sử dụng trong các mô hình thực hiện các task như dịch máy hay ngôn ngữ tự nhiên. BERT và GPT là $2 \mathrm { m } \hat { \mathrm { o } }$ hình điển hình có sử dụng Attention. Attention là thành phần chính tạo nên sự đình đám của mô hình Transformer, mô hình này chính là sự đột phá trong các bài toán xử lý của NLP so với các mạng neural hồi quy. Vậy Attention là gì mà tại sao nó lại là sự khác biệt đến vậy, hãy cũng tôi đi tìm hiểu trong bài viêt ngày hôm nay với tiêu đề “Attention và sự hình thành của mô hình Transformer”

# Động lực cho sự phát triển của Attention

## Recurrent Neural Network (RNN) và sự hạn chế đáng kể

### Ý tưởng cốt lõi của RNN

Con người chúng ta không thể bắt đầu suy nghĩ của mình tại tất cả các thời điểm, cũng giống như việc bạn đang đọc bài viết này, bạn hiểu mỗi chữ ở đây dựa vào các chữ mà bạn đã đọc và hiểu trước đó, chứ không phải đọc xong là quên chữ đó đi rồi đến lúc gặp thì lại phải đọc và tiếp thu lại. Giống như trong bài toán của chúng ta. Các mô hình mạng nơ-ron truyền thống lại không thể làm được việc trên. Vì vậy mạng nơ-ron hồi quy (RNN) được sinh ra để giải quyết việc đó. Mạng này chứa các vòng lặp bên trong cho phép nó lưu lại các thông tin đã nhận được. RNN là một thuật toán quan trọng trong xử lý thông tin dạng chuỗi hay nói cách khác là dạng xử lý tuần tự.

![](images/image1.jpg)  
Cäu trúc co bán cúa RNN



Vậy như nào là xử lý tuần tự - Xử lý tuần tự là mỗi block sẽ lấy thông tin của block trước và input hiện tại làm đầu vào

Tai mǒi buóc t, giá tri kích hoat $a ^ { t }$ và đäu ra $y ^ { t }$ duoc biéu diěn nhu sau:

$$
a ^ { t } = g _ { 1 } . ( W _ { a a } . a ^ { t - 1 } + W _ { a x } . x ^ { t } + b _ { a } )
$$

ta có thé viét gon lai nhu sau:

$$
\begin{array} { c } { { a ^ { t } = g _ { 1 } . ( \left( W _ { a a } W _ { a x } \right) \left( \begin{array} { c } { { a ^ { t - 1 } } } \\ { { x ^ { t } } } \end{array} \right) + b _ { a } ) } } \\ { { { } } } \\ { { a ^ { t } = g _ { 1 } . ( W \left( \begin{array} { c } { { a ^ { t - 1 } } } \\ { { x ^ { t } } } \end{array} \right) + b _ { a } ) } } \end{array}
$$

Tùr vói $a ^ { t }$ ta có còng thúrc tính dau ra tuong úng $y ^ { t }$

$$
y ^ { t } = g _ { 2 } . ( W _ { y a } . a ^ { t } + b _ { y } )
$$

![](images/image2.jpg)  
Cau trúc mot block trong RNN

2.1.2. Ưu điểm và nhược điểm của RNN





Cấu trúc của LSTM không khác gì RNN, nhưng sự cải tiến ở đây năm ở phần tính toán trong từng hidden state như sau: Thay vì chỉ có một tầng mạng nơ-ron, LSTM thiết kế với 4 tầng mạng nơ-ron tương tác với nhau một các rất đặc biệt.

Dưới đây là 2 hình ảnh biểu diễn sự khác nhau giữa RNN và LSTM

![](images/image3.jpg)  
RNN with tanh function

![](images/image4.jpg)  
LSTM with tanh and sigmoid functions

Chìa khóa để giúp LSTM có thể truyền tải thông tin giữa các hidden state một các xuyên suốt chính là cell state (hình dưới):



![](images/image5.jpg)  
LSTM cell state

Đầu ra là hàm sigmoid chứa các giá trị từ 0 đến 1.

Nếu forget gate có giá trị bằng 0, LSTM sẽ "quên" trạng thái được lưu trữ trong đơn vị tương ứng của trạng thái cell trước đó.

Nếu cổng quên có giá trị bằng 1, LSTM sẽ chủ yếu ghi nhớ giá trị tương ứng ở trạng thái được lưu trữ.

$$
\Gamma _ { f } ^ { \left. t \right. } = \sigma ( \mathbf { W } _ { f } [ \mathbf { a } ^ { \left. t - 1 \right. } , \mathbf { x } ^ { \left. t \right. } ] + \mathbf { b } _ { f } )
$$

Candidate value $\tilde { \mathbf { c } } ^ { ( t ) }$



Chứa thông tin có thể được lưu trữ từ time step hiện tại.

$$
\tilde { \mathbf { c } } ^ { ( t ) } = \operatorname { t a n h } \left( \mathbf { W } _ { c } [ \mathbf { a } ^ { ( t - 1 ) } , \mathbf { x } ^ { ( t ) } ] + \mathbf { b } _ { c } \right)
$$

Update gate $\mathbf { { r } } _ { i }$

Quyět dinh xem phan thòng tin nào cúa $\tilde { \mathbf { c } } ^ { ( t ) }$ có the thèm vào $\mathbf { c } ^ { ( t ) }$

$$
\mathbf { \Gamma } _ { i } ^ { \left. t \right. } = \sigma ( \mathbf { W } _ { i } [ a ^ { \left. t - 1 \right. } , \mathbf { x } ^ { \left. t \right. } ] + \mathbf { b } _ { i } )
$$

# Cell state c(tci)

Là bộ nhớ trong của LSTM. Cell state như 1 băng tải truyền các thông tin cần thiết xuyết suất cả quá trình, qua các nút mạng và chỉ tương tác tuyển tính 1 chút. Vì vậy thông tin có thể tuyền đi thông suốt mà không bị thay đổi.

$$
\mathbf { c } ^ { \left. t \right. } = \mathbf { \Gamma } _ { f } ^ { \left. t \right. } * \mathbf { c } ^ { \left. t - 1 \right. } + \mathbf { \Gamma } _ { i } ^ { \left. t \right. } * \tilde { \mathbf { c } } ^ { \left. t \right. }
$$



# Output gate $\mathbf { \delta T } _ { o }$

Cong diěeu chinh luong thòng tin däu ra cúa cell hièn tai và luong thòng tin truyěn tói trang thái tiép theo.

$$
\mathbf { \Gamma } _ { o } ^ { \left\{ t \right\} } = \sigma ( \mathbf { W } _ { o } [ \mathbf { a } ^ { \left\{ t - 1 \right\} } , \mathbf { x } ^ { \left\{ t \right\} } ] + \mathbf { b } _ { o } )
$$

Hidden state $\mathbf { a } ^ { ( t ) }$

Dugc sú dung dě xác dinh ba cǒng $( \mathbf { T } f , \mathbf { T } u , \mathbf { T } _ { o } )$ cua time step tiép theo.

$$
\mathbf { a } ^ { ( t ) } = \Gamma _ { o } ^ { ( t ) } * \operatorname { t a n h } ( \mathbf { c } ^ { ( t ) } )
$$

Prediction $\mathbf { y } _ { p r e d } ^ { ( t ) }$

Du doán trong truòng hop sú' dung này là phân loai, vì vày ban sě sú' dung softmax.

$$
\mathbf { y } _ { p r e d } ^ { \left. t \right. } = \mathrm { s o f t m a x } ( \mathbf { W } _ { y } \mathbf { a } ^ { \left. t \right. } + \mathbf { b } _ { y } )
$$