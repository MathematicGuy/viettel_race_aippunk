<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUÁN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

# 1. Giải thích:

Tương tự CRFs, Linear-Chain CRFs phân loại chuỗi dựa trên xác suất $P ( Y \vert X )$ . Với chuỗi x cho trước, CRFs sẽ tìm ra chuỗi y sao cho xác suất $P ( Y = y | X = x )$ là lớn nhất.

$$
\hat { y } = a r g m a x _ { y } P ( y | x )
$$

Xác suất $P ( Y \vert X )$ được xây dựng thông qua việc định nghĩa các hàm đặc trưng $f _ { k } { \mathrm { v } } { \dot { { \mathrm { a } } } } g _ { k }$ và xác định giá trị $\lambda _ { k } , \mu _ { k }$ . Các trọng số được tối ưu trong quá trình huấn huyện với tập dữ liệu huấn luyện. Nói cách khác, quá trình huấn luyện CRFs là quá trình học phân phối xác suất $P ( Y \vert X )$ của tập dữ liệu huấn luyện.

Việc tối ưu hóa các trọng $\begin{array} { r } { \mathrm { s } \hat { \hat { \mathbf { o } } } \theta = ( \lambda _ { 1 } , \dots , \lambda _ { k } ; \mu _ { 1 } , \dots , \mu _ { k } ) } \end{array}$ tương đương với việc tìm kiếm hàm năng lượng tối ưu cho mô hình. Mô hình CRFs sẽ điều chỉnh các trọng số để hàm đặc trưng phản ánh chính xác mối quan hệ giữa chuỗi quan sát và chuỗi nhãn, từ đó đưa ra dự đoán chính xác nhất. Do đó, hàm đặc trưng đóng vai trò then chốt trong việc xác định $\mathrm { m } \acute { \mathrm { o 1 } }$ quan hệ giữa chuỗi quan sát x và chuỗi nhãn y. Việc lựa chọn và thiết kế hàm đặc trưng phù hợp với bài toán cụ thể là rất quan trọng để đảm bảo mô hình có thể học được các mẫu quan trọng từ dữ liệu và đưa ra dự đoán chính xác.

# 2. Huấn luyện

Việc huấn luyện thường sử dụng phương pháp MLE (Maximum Likelihood Estimation) để tối ưu hóa các trọng số $\theta = ( \lambda _ { 1 } , \ldots , \lambda _ { k } ; \mu _ { 1 } , \ldots , \mu _ { k } )$ từ tập huấn luyện $D = \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { N } . \}$ Mục tiêu của quá trình huấn luyện là tìm ra bộ trọng số $\theta$ để hàm mục tiêu log-likelihood $L ( \theta )$ là lớn nhất.

$$
L ( \theta ) = \sum _ { i = 1 } ^ { N } l o g \left( P _ { \theta } { \bigl ( } y ^ { ( i ) } { \bigl | } x ^ { ( i ) } { \bigr ) } \right)
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

$$
\begin{array} { c l } { { } } & { { = \displaystyle \sum _ { i = 1 } ^ { N } \left( \displaystyle \sum _ { t = 1 } ^ { n } \left( \displaystyle \sum _ { k } \lambda _ { k } f _ { k } \left( y _ { t - 1 } ^ { ( i ) } , y _ { t } ^ { ( i ) } , x ^ { ( i ) } , t \right) + \displaystyle \sum _ { k } \mu _ { k } g _ { k } \left( y _ { t } ^ { ( i ) } , x ^ { ( i ) } , t \right) \right) \right. } } \\ { { } } & { { } } \\ { { \left. - \ l o g \left( { \cal Z } _ { \theta } \left( x ^ { ( i ) } \right) \right) \right) } } \end{array}
$$

Việc tối ưu hóa hàm mục tiêu có thể sử dụng các phương pháp tối ưu dựa trên việc tính gradient như Gradient Descent, Stochastic Gradient Descent (SGD), LBFGS (Limited-memory BFGS). Do đó chúng ta cần tính gradient của $L ( \theta )$ .

$$
\frac { \partial L } { \partial \lambda _ { k } } = \sum _ { i = 1 } ^ { N } \left( \sum _ { t = 1 } ^ { n } f _ { k } \left( y _ { t - 1 } ^ { ( i ) } , y _ { t } ^ { ( i ) } , x ^ { ( i ) } , t \right) - \frac { 1 } { Z _ { \theta } ( x ^ { ( i ) } ) } \frac { \partial Z _ { \theta } } { \partial \lambda _ { k } } \right)
$$

$$
{ \frac { 1 } { Z _ { \theta } ( x ^ { ( i ) } ) } } { \frac { \partial Z _ { \theta } } { \partial \lambda _ { k } } } = { \frac { 1 } { Z _ { \theta } ( x ^ { ( i ) } ) } } \sum _ { y ^ { \prime } \in \varOmega _ { y } } \left( \sum _ { t = 1 } ^ { n } f _ { k } \big ( y ^ { \prime } _ { t - 1 } , y ^ { \prime } _ { t } , x ^ { ( i ) } , t \big ) e ^ { - E \left( x ^ { ( i ) } , y ^ { \prime } \right) } \right)
$$

$$
\begin{array} { r l r } & { } & \\ & { } & { = \displaystyle \sum _ { y ^ { \prime } \in \mathcal { X } _ { \sigma } } \left( \sum _ { i = 1 } ^ { \infty } \hat { \rho } _ { x ^ { \prime } \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \right) } \\ & { } & { = \displaystyle \sum _ { y ^ { \prime } \in \mathcal { Y } _ { \sigma } } \left( \sum _ { i = 1 } ^ { \infty } \hat { \rho } _ { x ^ { \prime } \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \right) } \\ & { } & { = \displaystyle \sum _ { y ^ { \prime } \in \mathcal { Y } _ { \sigma } } \sum _ { \phi \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } \hat { \rho } _ { x ^ { \prime } } } \\ & { } &  = \displaystyle \sum _ { \phi \in \mathcal { X } _ { \sigma } } \sum _ { \phi \in \mathcal { X } _ { \sigma } } \hat { \rho } _ { x ^ { \prime } } ( y ^ { \prime } _ { \sigma } - y ^ { \prime } _ { \phi \in \mathcal { X } _ { \sigma } } \hat { \rho } _  x  \end{array}
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUYEN VA SUY LUAN LINEaR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

Gọi $E _ { x } ( f _ { k } )$ là kì vòng hàm đặc trưng $f _ { k }$ theo phân phối xác suất $P ( y | x )$ :

$$
E _ { x } ( f _ { k } ) = \sum _ { t = 1 } ^ { n } \sum _ { y ^ { \prime } \in \varOmega _ { y } } f _ { k } \big ( y ^ { \prime } { } _ { t - 1 } , y ^ { \prime } { } _ { t } , x ^ { ( i ) } , t \big ) P \big ( y ^ { \prime } \big | x ^ { ( i ) } \big )
$$

$$
\Rightarrow \frac { \partial L } { \partial \lambda _ { k } } = \sum _ { i = 1 } ^ { N } \left( \sum _ { t = 1 } ^ { n } f _ { k } \left( y _ { t - 1 } ^ { ( i ) } , y _ { t } ^ { ( i ) } , x ^ { ( i ) } , t \right) + ⨏ _ { x ^ { ( i ) } } ( f _ { k } ) \right)
$$

Tương tự ta cũng có gradient cho $\mu _ { k }$ :

$$
E _ { x } ( g _ { k } ) = \sum _ { t = 1 } ^ { n } \sum _ { y ^ { \prime } \in \varOmega _ { y } } g _ { k } \big ( y ^ { \prime } { } _ { t } , x ^ { ( i ) } , t \big ) P \big ( y ^ { \prime } \big | x ^ { ( i ) } \big )
$$

$$
\frac { \partial L } { \partial \mu _ { k } } = \sum _ { i = 1 } ^ { N } \left( \sum _ { t = 1 } ^ { n } g _ { k } \left( y _ { t } ^ { ( i ) } , x ^ { ( i ) } , t \right) + E _ { x ^ { ( i ) } } ( g _ { k } ) \right)
$$

Nếu tính trực tiếp kì vọng của các hàm đặc trưng từ công thức trên thì độ phức tạp tính toán sẽ là hàm mũ $\left( O ( n \times | \mathcal { Y } | ^ { n } ) \right)$ . Do đó không khả thi khi số lượng nhãn và bộ dữ liệu lớn. Để giảm độ phức tạp tính toán ta biến đổi công thức trên thành dạng sau:

$$
\begin{array} { r } { E _ { x } ( f _ { k } ) = \displaystyle \sum _ { t = 1 } ^ { n } \sum _ { y ^ { \prime } \in \mathcal { Q } _ { y } } f _ { k } \big ( y ^ { \prime } _ { t - 1 } , y ^ { \prime } _ { t } , x ^ { ( i ) } , t \big ) P \big ( y ^ { \prime } \big | x ^ { ( i ) } \big ) } \\ { \displaystyle \sum _ { = 1 } ^ { n } \sum _ { y ^ { \prime } , y ^ { \prime \prime } \in \mathcal { Y } } f _ { k } \big ( y ^ { \prime } , y ^ { \prime \prime } , x ^ { ( i ) } , t \big ) P \big ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } \big | x ^ { ( i ) } \big ) _ { ? \ \mathrm { 0 } 2 5 \cdot \mathrm { 0 } 9 \cdot \mathrm { 0 } ^ { - 2 8 } } . } \end{array}
$$

Trong đó $P \big ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } \big | x ^ { ( i ) } \big )$ là xác xuất biên của $Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime }$ khi biết chuỗi quan sát $x ^ { ( i ) }$ , tức xác suất để cặp nhãn $( y ^ { \prime } , y ^ { \prime \prime } )$ được gán tại vị trí

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUÁN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

t-1 và t khi biết $\boldsymbol { x } ^ { ( i ) }$ mà không quan tâm đến các nhãn còn lại. Xác suất biên này có th $\dot { \hat { \mathbf { e } } }$ được tính trong thời gian đa thức bằng thuật toán Forward-Backward.

Tương tự cho $\mu _ { k }$ :

$$
E _ { x } ( g _ { k } ) = \sum _ { t = 1 } ^ { n } \sum _ { y ^ { \prime } \in \mathcal { Y } } g _ { k } \big ( y ^ { \prime } , x ^ { ( i ) } , t \big ) P \big ( Y _ { t } = y ^ { \prime } \big | x ^ { ( i ) } \big )
$$

# 3. Thuật toán Forward-Backward áp dụng trong tính gradient

![](images/a3a5c63a8d581421db81951c6b8b86d4c52a34280d87046508c85554a68aa50a.jpg)  
Hình 3.1. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 nút

Ý tưởng của thuật toán Forward-Backward là tính xác suất biên dựa vào việc tính xác suất tiến $\alpha _ { i } ( x )$ và xác suất lùi $\beta _ { i } ( x )$ . Hình $8 \mathrm { m } \hat { \mathrm { o } }$ tả ý tưởng tính xác suất biên $P ( Y _ { 2 } = v | x )$ và $\operatorname { h i n h } \ 9 \cdot \mathrm { m } \widehat { \mathrm { ~ } }$ tả ý tưởng cách tính xác suất biên $P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x )$ cho bài toán POS. Mỗi một đường đi từ ${ \bf \mathrm { < } } { \bf { S } } >$ đến <T> là 1 trường hợp của chuỗi Y. Trọng số của của mỗi cạnh được tính theo công thức $M _ { i } ( C _ { j } , C _ { k } | x ) \backslash$ đã trình bày $\acute { \mathbf { O } }$ phần trước thể hiện khả năng nhãn của từ liền kề khi biết trước nhãn, trọng số của 1 đường đi là tích các trọng số cạnh mà đường đi qua.

$$
p _ { \theta } ( Y = y | X = x ) = \left. p _ { \theta } \big ( p a t h _ { y } \big | X = x \big ) = \frac { T r _ { 0 } n g s \tilde { \mathcal { O } } ~ c \tilde { \mathsf { u } } a ~ p a t h _ { y } } { Z _ { \theta } ( x ) } \right.
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUÁN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

Xác suất biên $P ( Y _ { 2 } = v | x )$ sẽ là tổng xác suất của tất cả các đường đi đi qua v tại $Y _ { 2 }$ hay tổng trọng số các đường đi đó. Ta có thể phân tích tổng này thành tích của 2 tổng $\alpha _ { 2 } ( v | x )$ và $\beta _ { 2 } ( v | x )$ .

$$
P ( Y _ { 2 } = v | x ) = \alpha _ { 2 } ( v | x ) \times \beta _ { 2 } ( v | x )
$$

Trong đó $\alpha _ { 2 } ( v | x )$ là tổng trọng số tất cả các đường đi từ ${ \bf \mathrm { < } } { \bf { S } } >$ đến $\mathbf { V }$ tại $Y _ { 2 }$ , $\beta _ { 2 } ( v | x )$ là tổng trọng số tất cả các đường đi từ $\mathbf { V }$ tại $Y _ { 2 }$ đến ${ < } \mathrm { T } >$ .

Để tính $\alpha _ { 2 } ( v | x )$ ta sẽ tính $\alpha _ { 1 }$ của tất cả các giá trị của Y1 rồi nhân với trọng số chuyển đổi thành nhãn v tương ứng với từng giá trị $\mathbf { \check { V } } = > \mathbf { V } _ { : }$ , $\mathbf { n } = > \mathbf { V }$ , $\mathfrak { p } \Rightarrow \mathfrak { v }$ , d $\mathbf { \Psi } = > \mathbf { v } )$ ). Như vậy thì $\alpha _ { i }$ sẽ được tính dựa theo $\alpha _ { i - 1 }$ và quá trình này là quá trình tiến của thuật toán Forward-Backward. Tương tự $\beta _ { i }$ cũng được tính toán dựa trên quy hoạch động và quá trình này là quá trình lùi.

Tổng quát, ta có chuỗi $Y = \left( Y _ { 0 } , \ldots , Y _ { n } \right)$ , gọi $Y _ { i : j } = \left( Y _ { i } , \ldots , Y _ { j } \right)$ ??ớ?? $0 \leq i <$ $j \leq n .$

Ta có:

$$
\begin{array}{c} \alpha _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \left\{ \sum _ { y _ { 0 : t - 1 } ^ { \prime } } \prod _ { i = 1 } ^ { t } M _ { i } \big ( y _ { \ i - 1 } ^ { \prime } , y _ { \ i } ^ { \prime } | x \big ) , \qquad v \dot { o } i 1 < t \leq n \right.  \\ { M _ { 1 } \big ( < S t a r t > , y _ { \ i } ^ { \prime } | x \big ) , \qquad v \dot { o } i t = 1 } \end{array}
$$

$$
\beta _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \left\{ \begin{array} { l l } { \displaystyle \sum _ { y _ { t + 1 : n } ^ { \prime } } \prod _ { i = t + 1 } ^ { n } M _ { i } \big ( { y ^ { \prime } } _ { i - 1 } , { y ^ { \prime } } _ { i } \big | x \big ) , } & { v \delta { i } 1 \leq t < n - 1 } \\ { \displaystyle \sum _ { y _ { t } ^ { \prime \prime } \in \mathcal { Y } } M _ { t } ( y ^ { \prime } , y ^ { \prime \prime } | x ) , } & { v \delta { i } t = n - 1 } \\ { \displaystyle 1 , } & { v \delta { i } \hat { t } = n } \end{array} \right.
$$

Ta chứng minh $\begin{array} { r } { \alpha _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \sum _ { { y ^ { \prime } } _ { t - 1 } \in \mathcal { Y } } \alpha _ { t - 1 } \big ( Y _ { t - 1 } = { y ^ { \prime } } _ { t - 1 } \big | x \big ) \times } \end{array}$ $M _ { t } \big ( y ^ { \prime } { } _ { t - 1 } , y ^ { \prime } \big | x \big )$ với $1 < t \leq n$ , thật vậy:

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUYEN VA SUY LUAN LINEaR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

$$
\alpha _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \sum _ { y _ { 0 : t - 2 } ^ { \prime } } \sum _ { y ^ { \prime } } \prod _ { t = 1 } ^ { t - 1 } M _ { i } \big ( { y ^ { \prime } } _ { i - 1 } , { y ^ { \prime } } _ { i } | x \big ) \times M _ { t } \big ( { y ^ { \prime } } _ { t - 1 } , { y ^ { \prime } } _ { t } \big | x \big )
$$

$$
\begin{array} { r l } & { = \displaystyle \sum _ { y ^ { \prime } _ { t - 1 } \in \mathcal { Y } } \left( \displaystyle \sum _ { y _ { 0 : t - 2 } ^ { \prime } } \prod _ { i = 1 } ^ { t - 1 } M _ { i } \big ( { y ^ { \prime } } _ { i - 1 } , { y ^ { \prime } } _ { i } \big | x \big ) \right) \times M _ { t } \big ( { y ^ { \prime } } _ { t - 1 } , { y ^ { \prime } } _ { t } \big | x \big ) } \\ & { = \displaystyle \sum _ { y ^ { \prime } _ { t - 1 } \in \mathcal { Y } } \alpha _ { t - 1 } \big ( Y _ { t - 1 } = { y ^ { \prime } } _ { t - 1 } \big | x \big ) \times M _ { t } \big ( { y ^ { \prime } } _ { t - 1 } , { y ^ { \prime } } \big | x \big ) } \end{array}
$$

Tương tự, với $1 \leq t < n - 1$ ta cũng có:

$$
\beta _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \sum _ { y ^ { \prime } _ { t + 1 } \in y } M _ { t + 1 } \big ( y ^ { \prime } , y ^ { \prime } _ { t + 1 } \big | x \big ) \beta _ { t + 1 } \big ( Y _ { t + 1 } = y ^ { \prime } _ { t + 1 } \big | x \big )
$$

Với cách biểu diễn dưới dạng ma trận công thức $\alpha _ { t } ( Y _ { t } = y ^ { \prime } | x )$ và $\beta _ { t } ( Y _ { t } = y ^ { \prime } | x )$ có thể biểu diễn dưới dạng tích ma trận và vector với $M _ { i } ( x ) _ { < s t a r t > }$ là vetor hàng ứng vói nhãn $< S t a r t > , 1 _ { | y \prime | \times 1 }$ là ma trận các giá trị 1 kích thước $\vert \mathcal { Y } ^ { \prime } \vert \times 1$ :

$$
\alpha _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \left\{ \begin{array} { c c } { \left( M _ { i } ( x ) _ { < s t a r t > } \times \displaystyle \prod _ { i = 2 } ^ { t } M _ { i } ( x ) \right) _ { 0 , y \dot { \sigma } i } } & { , v \dot { \sigma } i 1 < t \leq n } \\ { M _ { i } ( x ) _ { < s t a r t > , y ^ { \prime } } , } & { v \dot { \sigma } i t = 1 } \end{array} \right.
$$

$$
\beta _ { t } ( Y _ { t } = y ^ { \prime } | x ) = \{ ( ( \prod _ { i = 1 } ^ { t + 1 } M _ { i } ( x ) ) \times 1 _ { | y r | \times 1 } ) _ { y ^ { \prime } , 0 } , v \dot { \sigma } i 1 \leq t < n
$$

Công thức xác xuất biên biểu diễn bằng xác suất tiến và lùi có dạng:

$$
P ( Y _ { t } = y ^ { \prime } | x ) = \frac { \alpha _ { t } ( Y _ { t } = y ^ { \prime } | x ) \times \beta _ { t } ( Y _ { t } = y ^ { \prime } | x ) } { Z _ { \theta } ( x ) }
$$

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

![](images/0824a9f505db790114122dab1f9c502b3255321639eb18580a7227c47d634ce2.jpg)  
Hình 3.2. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 cạnh

Tương tự với xác suất biên $P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x )$ , ta có:

$$
\begin{array} { r l } & { P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x ) } \\ & { \qquad = \frac { \alpha _ { t - 1 } ( Y _ { t - 1 } = y ^ { \prime } | x ) \times M _ { t } ( y ^ { \prime } , y ^ { \prime \prime } | x ) \times \beta _ { t } ( Y _ { t } = y ^ { \prime \prime } | x ) } { Z _ { \theta } ( x ) } } \end{array}
$$

Bằng phương pháp quy hoạch động, ta có th $\acute { \hat { \mathbf { e } } }$ tính các xác suất biên với độ phức tạp $O ( n \times | \mathcal { Y } | ^ { 2 } )$ và chính là độ phức tạp khi tính kì vọng của các hàm đặc trưng.

# 4. Thuật toán Viterbi áp dụng trong suy luận Linear-Chain CRFs

Xác định chuỗi $\hat { y }$ có xác suất xảy ra cao nhất khi biết x:

$$
\hat { y } = a r g m a x _ { y } \ : P ( y | x ) = a r g m a x _ { y } \frac { \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) } { Z _ { \theta } ( x ) } 
$$

Vì $Z _ { \theta } ( x )$ là hằng số khi biết nên việc xác định chuỗi $\hat { y }$ có xác suất xảy ra cao nhất khi biết x t:

$$
\begin{array} { r l r } {  { \operatorname { t r o n g } \mathrm { d u o n g ~ v o i x a c ~ d i n h ~ c h u \tilde { \hat { o } } i } \hat { y } \mathrm { d } \hat { \hat { e } } \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) \mathrm { l o n } \mathrm { n h } \hat { \hat { a } } } } \\ & { } & { \hat { y } = a r g m a x _ { y } \displaystyle \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) } \end{array}
$$

Việc tìm $\hat { y }$ có thể tính trong thời gian $O ( n \times | \mathcal { Y } | ^ { 2 } )$ với thuật toán quy hoạch động Viterbi. Thuật toán Viterbi được mô tả bằng $\mathrm { m } \tilde { \mathbf { a } }$ giả trong hình 10.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUYEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

![](images/c36cfcc97627c80b71e70848c88ae1c3f717e8a426099c5da8fea8826d7069a5.jpg)  
Hình 4.1: Thuật toán Viterbi cho suy luận Linear-chain CRFs

$M _ { i } ( x )$ là ma trận đã được trình bày trong phần 3 với hàng 0 và cột 0 tương ứng với nhãn <Start>.

<table><tr><td rowspan=2 colspan=1>Ai</td><td rowspan=1 colspan=1>VIETTEL AI RACE</td><td rowspan=1 colspan=1>Public 103</td></tr><tr><td rowspan=1 colspan=1>HUAN LUyEN VA SUY LUAN LINEAR-CHAIN CRFS</td><td rowspan=1 colspan=1>Làn banhành: 1</td></tr></table>

![](images/1848f0045753a0134514e43c0acc09b8fa8ef66552c02e0fa506ea9c2897fab9.jpg)  
Hình 4.2: Hình minh họa thuật toán Viterbi cho POS

Hình 4.2 là minh họa quá trình suy luận Viterbi cho POS. Giả sử sau khi huấn luyện ta đã có được trọng số của các đường đi $M _ { i }$ . Với đầu câu đầu vào có 4 từ, và cần gán nhãn cho 4 từ này một nhãn từ loại là 1 trong 4 giá trị: v, n, p, d. Ở đây, mỗi một miền tương đương với 1 từ cần được gán nhãn và số đỉnh trong miền là nhãn có thể có của từ, ví dụ, miền Y1 có 4 đỉnh là v, n, p, d tương đương với 4 giá trị có thể gán cho từ đầu tiên của câu. Một đường đi hợp lệ là đường đi đi qua duy nhất một đỉnh trong mỗi miền. Thuật toán Viterbi sẽ tìm đường sao cho trọng số là lớn nhất (tương đương với xác suất chuỗi nhãn là lớn nhất.

Ý tưởng của Viterbi là đường đi lớn nhất đến một đỉnh sẽ bao gồm đường đi lớn nhất đến đỉnh trước nó. Xuất phát từ ý tưởng này, để tìm đường đi lớn nhất đến miền Y4, ta sẽ tính đường đi lớn nhất đến các đỉnh của miền Y3, sau đó từ các đỉnh của Y3 ta tính trọng số đến các đỉnh của Y4 và chọn ra đường đi có trọng số lớn nhât. Tương tự đường đi có trọng số lớn nhất đến các đỉnh trong Y3 có thểtính qua đường đi có trọng số lớn nhất đến các đỉnh trong Y2, ….