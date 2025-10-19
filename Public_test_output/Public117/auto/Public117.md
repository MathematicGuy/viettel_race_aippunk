<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 117</td></tr><tr><td rowspan=1 colspan=1>ON TAP VE xAC SUAT</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 1. Random variables

Một biến ngẫu nhiên (random variable) x là một đại lượng dùng để đo những đại lượng không xác định. Biến này có thể ký hiệu kết quả/đầu ra (outcome) của một thí nghiệm (ví dụ như tung đồng xu) hoặc một đại lượng biến đổi trong tự nhiên (ví dụ như nhiệt độ trong ngày). Nếu chúng ta quan sát rất nhiều đầu ra $\{ \mathrm { x } \underline { { \mathrm { i } } } \} \_ { - } \{ \mathrm { i } { = } 1 \} \wedge \mathrm { I }$ của các thí nghiệm này, ta có thể nhận được những giá trị khác nhau ở mỗi thí nghiệm. Tuy nhiên, sẽ có những giá trị xảy ra nhiều lần hơn những giá trị khác. Thông tin về đầu ra được đo bởi phân phối xác suất (probability distribution) $\mathfrak { p } ( \mathbf { x } )$ của biến ngẫu nhiên.

Một biến ngẫu nhiên có thể là rời rạc (discrete) hoặc liên tục (continuous). Một biến ngẫu nhiên rời rạc sẽ lấy giá trị trong một tập hợp cho trước. Ví dụ tung đồng xu thì có hai khả năng là head và tail (tên gọi này bắt nguồn từ đồng xu Mỹ, một mặt có hình mặt người, được gọi là head, trái ngược với mặt này được gọi là mặt tail, cách gọi này hay hơn cách gọi xấp ngửa vì ta không có quy định rõ ràng thế nào là xấp ngay ngửa). Tập các giá trị này có thể là có thứ tự (khi tung xúc xắc) hoặc không có thứ tự (unordered), ví dụ khi đầu ra là các giá trị nắng, mưa, bão, etc. Mỗi đầu ra có một giá trị xác suất tương ứng với nó. Các giá trị xác suất này không âm và có tổng bằng một:

if x is discrete:

$$
\begin{array} { r } { \sum _ { - } \mathbf { x p } ( \mathbf { x } ) = 1 } \end{array}
$$

Biến ngẫu nhiên liên tục lấy các giá trị là tập con của các số thực. Những giá trị này có thể là hữu hạn, ví dụ thời gian làm bài của mỗi thí sinh trong một bài thi 180 phút, hoặc vô hạn, ví dụ thời gian để chiếc xe bus tiếp theo tới. Không như biến ngẫu nhiên rời rạc, xác suất để đầu ra bằng chính xác một giá trị nào đó, theo lý thuyết, là bằng 0. Thay vào đó, ta có thể hình dung xác suất để đầu ra nằm trong một khoảng giá trị nào đó; và việc này được mô tả bởi hàm mật độ xác suất (probability density function - pdf). Hàm mật độ xác suất luôn cho giá trị dương, và tích phân của nó trên toàn miền possible outcome phải bằng 1.

if x is continuous:

$$
\int \mathbf { p } ( \mathbf { x } ) \mathrm { d } \mathbf { x } = 1
$$

Để giảm thiểu ký hiệu, hàm mật độ xác suất của một biến ngẫu nhiên liên tục x cũng được ký hiệu là p(x).

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 117</td></tr><tr><td rowspan=1 colspan=1>ON TaP VE xAc SUAT</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

Chú ý: Nếu x là biến ngẫu nhiên rời rạc, p(x) luôn luôn nhỏ hơn hoặc bằng 1. Trong khi đó, nếu x là biến ngẫu nhiên liên tục, p(x) có thể nhận giá trị dương bất kỳ, điều này vẫn đảm bảo là tích phân của hàm mật độ xác suất theo toàn bộ giá trị có thể có của x bằng 1. Với biến ngẫu nhiên rời rạc, p(x) được hiểu là mật độ xác suất tại x.

# 2. Joint probability

Xét hai biến ngẫu nhiên x và y. Nếu ta quan sát rất nhiều cặp đầu ra của x và y, thì có những tổ hợp hai đầu ra xảy ra thường xuyên hơn những tổ hợp khác. Thông tin này được biểu diễn bằng một phân phối được gọi là joint probability của x và y, và được viết là p(x, y). Dấu phẩy trong p(x, y) có thể đọc là và, vậy $\mathfrak { p } ( \mathrm { x } , \mathrm { y } )$ là xác suất của x và y. x và y có thể là hai biến ngẫu nhiên rời rạc, liên tục, hoặc một rời rạc, một liên tục. Luôn nhớ rằng tổng các xác suất trên mọi cặp giá trị có thể xảy ra (x, y) bằng 1.

both are discrete: $\begin{array} { r l } { { } } & { { } \sum _ { - } \{ \mathrm { x } , \mathrm { y } \} ~ \mathrm { p } ( \mathrm { x } , \mathrm { y } ) = 1 } \\ { { } } & { { } \mathrm { s } : ~ \iint _ { \mathbb { P } } ( \mathrm { x } , \mathrm { y } ) \mathrm { d } \mathrm { x } ~ \mathrm { d } \mathrm { y } = 1 } \end{array}$   
both are continuou   
x is discrete, y is continuous: $\begin{array} { r } { \sum _ { - } \mathbf { x } \int \mathbf { p } ( \mathbf { x } , \mathbf { y } ) \mathrm { d } \mathbf { y } = \int \left( \sum _ { - } \mathbf { x } \mathbf { p } ( \mathbf { x } , \mathbf { y } ) \right) \mathrm { d } \mathbf { y } = 1 } \end{array}$ Thông thường, chúng ta sẽ làm việc với các bài toán $\dot { \mathbf { O } }$ đó joint probability xác định trên nhiều hơn 2 biến ngẫu nhiên. Chẳng hạn, $\mathsf { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } )$ thể hiện joint probability của 3 biến ngẫu nhiên x, y và z. Khi có nhiều biến ngẫu nhiên, ta có thể viết chúng dưới dạng vector. Ta có thể viết $\mathfrak { p } ( \mathbf { x } )$ để thể hiện joint probability của biến ngẫu nhiên nhiều chiều $\mathrm { \bf x } = [ \mathrm { x } 1 , \mathrm { x } 2 , . . . , \mathrm { x n } ] ^ { \wedge } \mathrm { T } .$ Khi có nhiều tập các biến ngẫu nhiên, ví dụ x và y, ta có thể viết $\mathfrak { p } ( \mathrm { x } , \mathrm { y } )$ để thể hiện joint probability của tất cả các thành phần trong hai biến ngẫu nhiên nhiều chiều này.

# 3. Marginalization

Nếu biết joint probability của nhiều biến ngẫu nhiên, ta cũng có thể xác định được phân bố xác suất của từng biến bằng cách lấy tổng (rời rạc) hoặc tích phân (liên tục) theo tất cả các biến còn lại:

$\begin{array} { r } { \mathsf { p } ( \mathbf { x } ) = \sum \_ { \mathbf { y } } \mathsf { p } ( \mathbf { x } , \mathbf { y } ) } \end{array}$ (3) $\begin{array} { r } { \mathsf { p } ( \mathsf { y } ) = \sum _ { - } \mathbf { x } \mathsf { p } ( \mathbf { x } , \mathsf { y } ) } \end{array}$ (4) Và với biến liên tục: $\mathsf { p } ( \mathbf { x } ) = \int \mathsf { p } ( \mathbf { x } , \mathbf { y } ) \mathrm { d } \mathbf { y }$ (5)

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 117</td></tr><tr><td rowspan=1 colspan=1>ON TaP VE xAC SUAT</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

$\mathsf { p } ( \mathsf { y } ) = \boldsymbol { \int } \mathsf { p } ( \mathbf { x } , \mathsf { y } ) \mathrm { d } \mathbf { x }$ (6)

Với nhiều biến hơn, chẳng hạn 4 biến rời rạc x, y, z, w:

$$
\begin{array} { r } { \mathrm { p ( x ) } = \sum _ { \mathrm { - } } \{ \mathrm { y , z , w } \} \ \mathrm { p ( x , y , z , w ) } } \end{array}
$$

$$
\begin{array} { r } { \mathrm { p } ( \mathrm { x } , \mathrm { y } ) = \sum _ { - } \{ \mathrm { z } , \mathrm { w } \} \ \mathrm { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } , \mathrm { w } ) } \end{array}
$$

Từ đây trở đi, nếu không nói gì thêm, tôi sẽ dùng ký hiệu ∑ để chỉ chung cho cả hai loại biến. Nếu biến ngẫu nhiên là liên tục, bạn đọc ngầm hiểu rằng dấu $\sum$ cần được thay bằng dấu tích phân ∫, biến lấy vi phân chính là biến được viết dưới dấu ∑.

# 4. Conditional probability

Xác suất có điều kiện (conditional probability) của một biến ngẫu nhiên x biết rằng biến ngẫu nhiên y có giá trị ${ \boldsymbol { \mathrm { y } } } ^ { * }$ được ký hiệu là $\mathsf { p } ( \mathbf { x } \mid \mathbf { y } = \mathbf { y } ^ { * } )$ . Conditional probability $\mathsf { p } ( \mathrm { x } \mid \mathrm { y } = \mathrm { y } ^ { \ast } )$ có th $\acute { \hat { \mathbf { e } } }$ được tính dựa trên joint probability $\mathrm { p } ( \mathrm { x } , \mathrm { y } )$ .

$\begin{array} { r } { \mathsf { p } ( \mathbf { x } \mid \mathbf { y } = \mathbf { y } ^ { * } ) = \mathsf { p } ( \mathbf { x } , \mathbf { y } = \mathbf { y } ^ { * } ) / \sum \mathbf { x } \mathsf { p } ( \mathbf { x } , \mathbf { y } = \mathbf { y } ^ { * } ) = \mathsf { p } ( \mathbf { x } , \mathbf { y } = \mathbf { y } ^ { * } ) / \mathsf { p } ( \mathbf { y } = \mathbf { y } ^ { * } ) } \end{array}$ ) (9)

Thông thường, viết gọn: $\operatorname { p } ( \mathbf { x } \mid \mathbf { y } ) = \operatorname { p } ( \mathbf { x } , \mathbf { y } ) / \operatorname { p } ( \mathbf { y } )$

Tương tự: $\mathfrak { p } ( \mathrm { y } \mid \mathrm { x } ) = \mathfrak { p } ( \mathrm { y } , \mathrm { x } ) / \mathfrak { p } ( \mathrm { x } )$

$$
\mathtt { p ( x , y ) } = \mathtt { p ( x \mid y ) } \mathtt { p ( y ) } = \mathtt { p ( y \mid x ) } \mathtt { p ( x ) }
$$

Khi có nhiều hơn hai biến:

$$
\begin{array} { r l } & { \mathfrak { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } , \mathrm { w } ) = \mathfrak { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } \mid \mathrm { w } ) \mathfrak { p } ( \mathrm { w } ) \quad ( 1 2 ) } \\ & { = \mathfrak { p } ( \mathrm { x } , \mathrm { y } \mid \mathrm { z } , \mathrm { w } ) \mathfrak { p } ( \mathrm { z } , \mathrm { w } ) = \mathfrak { p } ( \mathrm { x } , \mathrm { y } \mid \mathrm { z } , \mathrm { w } ) \mathfrak { p } ( \mathrm { z } \mid \mathrm { w } ) \mathfrak { p } ( \mathrm { w } ) } \\ & { = \mathfrak { p } ( \mathrm { x } \mid \mathrm { y } , \mathrm { z } , \mathrm { w } ) \mathfrak { p } ( \mathrm { y } \mid \mathrm { z } , \mathrm { w } ) \mathfrak { p } ( \mathrm { z } \mid \mathrm { w } ) \mathfrak { p } ( \mathrm { w } ) \quad ( 1 4 ) } \end{array}
$$

# 5. Quy tắc Bayes

$$
\begin{array} { r l } & { \mathrm { T i r } \left( 1 1 \right) : \mathrm { p ( y \mid x ) p ( x ) } = \mathrm { p ( x \mid y ) p ( y ) } \Rightarrow \mathrm { p ( y \mid x ) } = \mathrm { p ( x \mid y ) p ( y ) / p ( x ) } } \\ & { = \mathrm { p ( x \mid y ) p ( y ) } / \sum \mathrm { y p ( x , y ) } \quad \mathrm { ( 1 6 ) } } \\ & { = \mathrm { p ( x \mid y ) p ( y ) } / \sum \mathrm { y p ( x \mid y ) p ( y ) } \quad \mathrm { ( 1 7 ) } } \end{array}
$$

Ba công thức (15)–(17) thường được gọi là Quy tắc Bayes (Bayes’ rule).

# 6. Independence

Nếu x và y độc lập: $\mathsf { p } ( \mathbf { x } \mid \mathbf { y } ) = \mathsf { p } ( \mathbf { x } )$ (18), $\mathsf { p } ( \boldsymbol { \mathrm { y } } \mid \boldsymbol { \mathrm { x } } ) = \mathsf { p } ( \boldsymbol { \mathrm { y } } )$ Khi đó: $\mathtt { p ( x , y ) } = \mathtt { p ( x ) } \mathtt { p ( y ) }$ (20)

7. Kỳ vọng

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 117</td></tr><tr><td rowspan=1 colspan=1>ON TaP VE xAC SUAT</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

Kỳ vọng (expectation) của một biến ngẫu nhiên:

$\begin{array} { r } { \operatorname { E } [ \mathbf { x } ] = \sum _ { - } ^ { } \mathbf { x } \mathbf { x } \mathbf { p } ( \mathbf { x } ) } \end{array}$ nếu x rời rạc (21)   
$\operatorname { E } [ \mathbf { x } ] = \int \mathbf { x } \ \mathbf { p } ( \mathbf { x } ) \ \mathrm { d } \mathbf { x }$ nếu x liên tục (22)   
Với hàm $\begin{array} { r } { \mathrm { f ( . ) } { \mathrm { : ~ E [ f ( x ) ] } } = \sum _ { - } { \mathrm { ~ x ~ f ( x ) ~ p ( x ) ~ } } } \end{array}$ (23)   
Với joint probability: $\begin{array} { r } { \mathrm { E } [ \mathrm { f } ( \mathrm { x } , \mathrm { y } ) ] = \sum _ { - } \{ \mathrm { x } , \mathrm { y } \} \ \mathrm { f } ( \mathrm { x } , \mathrm { y } ) \ \mathrm { p } ( \mathrm { x } , \mathrm { y } ) } \end{array}$ Ba quy tắc:   
$\operatorname { E } [ { \mathfrak { a } } ] = { \mathfrak { a } }$ (25)   
$\operatorname { E } [ { \mathfrak { a } } \mathbf { x } ] = \mathbf { a } \operatorname { E } [ \mathbf { x }$ (26); $\operatorname { E } [ \mathbf { f } ( \mathbf { x } ) + \mathbf { g } ( \mathbf { x } ) ] = \operatorname { E } [ \mathbf { f } ( \mathbf { x } ) ] + \operatorname { E } [ \mathbf { g } ( \mathbf { x } ) ]$ Nếu x, y độc lập: $\operatorname { E } [ \operatorname { f } ( \mathbf { x } ) \ \mathbf { g } ( \mathbf { y } ) ] = \operatorname { E } [ \operatorname { f } ( \mathbf { x } ) ] \operatorname { E } [ \mathbf { g } ( \mathbf { y } ) ]$ (28)

8. Một vài phân phối thường gặp

# 8.1 Bernoulli distribution

Bernoulli distribution: $\mathbf { x } \in \{ 0 , 1 \}$ , tham $\mathrm { s } \acute { 0 } \lambda \in [ 0 , 1 ]$ là xác suất để $\mathbf { x } { = } 1$

${ \mathrm { p } } ( { \mathrm { x } } { = } 1 ) { = } \lambda , \quad { \mathrm { p } } ( { \mathrm { x } } { = } 0 ) { = } 1 - \lambda$ Viết gọn: $\mathrm { p ( x ) } = \lambda \mathrm { \hat { x } } \left( 1 - \lambda \right) \mathrm { \hat { \Omega } } \{ 1 - \mathrm { x } \}$ Ký hiệu: $\mathsf { p } ( \mathrm { x } ) = \mathrm { B e r n } \_ \mathrm { x } [ \lambda ]$ (30)

# 8.2 Categorical distribution

Categorical distribution với K lớp, tham $\mathrm { s } \mathring { \hat { 0 } } \lambda = [ \lambda 1 , . . . , \lambda \mathrm { K } ] , \sum _ { - } \mathrm { k } \lambda \mathrm { k } = 1 .$

$\mathsf { p } ( \mathbf { x } = \mathbf { k } ) = \lambda \big \mathrm { ~ k ~ }$ ; viết gọn: $\mathsf { p } ( \mathrm { x } ) = \mathrm { C a t \_ x } [ \lambda ]$ Biểu diễn one-hot: $\mathrm { x } \in \{ \mathrm { e l } , . . . , \mathrm { e K } \}$ ${ \mathrm { p } } ( \mathbf { x } = { \mathbf { e } } \bot ) = \prod  \mathrm { ~ \{ j = 1 \} ~ \cdot K ~ \land ~ j ~ \land ~ j \} } = \lambda { \mathrm { ~ \bf ~ k ~ } }$

# 8.3 Univariate normal distribution

$\mathrm { p } ( \mathrm { x } ) = 1 / \sqrt { ( 2 \pi \sigma ^ { \wedge } 2 ) \cdot \exp ( - { \left( \mathrm { x } - \mu \right) ^ { \wedge } } 2 / ( 2 \sigma ^ { \wedge } 2 ) ) }$ (3 Ký hiệu: $\mathtt { p } ( \mathrm { x } ) = \mathrm { N o r m \_ x } [ \mu , \sigma ^ { \wedge } 2 ]$

8.4 Multivariate normal distribution   
$\mathrm { p ( x ) } = 1 / \left( ( 2 \pi ) ^ { \wedge } \{ \mathrm { D } / 2 \} \right.$ |Σ|^{1/2}) · exp(−1/2 (x−μ)^T Σ^{−1} (x−μ))   
Ký hiệu: $\mathtt { p ( x ) } = \mathtt { N o r m \_ x [ \mu , \Sigma ] }$

# 8.5 Beta distribution

$\mathrm { p ( \boldsymbol { \lambda } ) } = \Gamma ( \alpha + \beta ) / \left( \Gamma ( \alpha ) \Gamma ( \beta ) \right) \cdot \lambda \wedge \{ \alpha - 1 \} \ ( 1 - \lambda ) ^ { \wedge } \{ \beta - 1 \}$ (34) Trong đó $\Gamma ( \mathrm { z } ) = \int \_ 0 \land _ { \infty } { \mathrm { t } } \land \{ \mathrm { z }  - 1 \} \ \exp ( - \mathrm { t } )$ dt, và $\Gamma [ z ] = ( z - 1 ) !$ nếu $\mathbf { Z }$ là số tự nhiên.

Ký hiệu: $\mathsf { p } ( \lambda ) = \mathbf { B e t a } \_ \lambda [ \mathsf { a } , \mathsf { \beta } ]$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 117</td></tr><tr><td rowspan=1 colspan=1>ON TaP VE xAC SUAT</td><td rowspan=1 colspan=1>Làn ban hành: 1</td></tr></table>

# 8.6 Dirichlet distribution

p(λ1, …, λK) = Γ(∑_{k=1}^K α_k) / ∏_{k=1}^K Γ(α_k) · ∏_{k=1}^K   
$\lambda \stackrel { \mathrm { \scriptsize ~ k } ^ { \wedge } } { - } \stackrel { \textstyle \left\{ { \mathfrak { a } \stackrel { \mathrm { \scriptsize ~ k } ^ { - 1 } } { \mathfrak { a } } } \right\} }$ (35)   
Ký hiệu: $\mathrm { p } ( \mathbb { A } 1 , . . . , \mathbb { A } \mathrm { K } ) = \mathrm { D i r } _ { - } \{ \lambda 1 , . . . , \lambda \mathrm { K } \} [ \alpha 1 , . . . , \alpha \mathrm { K } ]$

# 9. Thảo luận

Về Xác suất thống kê, còn rất nhiều điều cần lưu ý. Tạm thời, phần này ôn tập lại các kiến thức xác suất cơ bản để phục vụ cho các bài viết tiếp theo. Khi nào có phần nào cần nhắc lại, sẽ tiếp tục ôn tập bổ sung.