

# Binary relevance (BR)

Phương pháp chuyển đổi đơn giản nhất là phương pháp chuyển đổi nhị phân (BR), tức là với mỗi nhãn khác nhau sẽ xây dựng một bộ phân lớp khác nhau. Phương pháp này xây dựng |L| bộ phân lớp nhị phân: Hl: $\mathrm { X \to \{ l ; - l \} }$ cho mỗi nhãn l khác nhau trong L. Thuật toán chuyển đổi dữ liệu ban đầu trong tập L nhãn. Nhãn là l nếu các nhãn của ví dụ ban đầu $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m } 1$ , nhãn là $^ { - 1 }$ trong trường hợp ngược lại. Theo [12], phương pháp này đã được sử dụng bởi Boutell (2004), Goncalves và Quaresma (2003), Lauser và Hotho (2003), Li và Ogihara (2003). Sau đây là ví dụ biểu diễn dữ liệu theo phương pháp này:

Biểu diễn dữ liệu theo phương pháp nhị phân   



Công thức tính Euclidean để tính khoảng cách giữa các điểm dữ liệu: Giả sử có hai phần tử dữ liệu ${ \mathrm { X 1 } } { = } ( \mathrm { x 1 } 1 , \mathrm { x 1 } 2 \ \ldots \ \mathrm { x } 1 { \mathrm { n } } )$ và ${ \bf X } 2 { = } ( { \bf x } 2 1$ , $\mathbf { x } 2 2 \ldots \mathbf { x } 2 \mathbf { n } )$ , độ đo khoảng cách Euclide được tính bằng công thức:

$$
D i s t ( X _ { 1 } , X _ { 2 } ) = \sqrt { \sum _ { i = 1 } ^ { n } ( x _ { 1 i } - x _ { 2 i } ) } ^ { 2 }
$$

Mô tả thuật toán:

- Đầu vào: tập dữ liệu học D đã có nhãn và đối tượng kiểm tra z.

- Tiến trình:

- Tính d (x, x’) khoảng cách giữa đối tượng kiểm tra và mọi đối tượng $( \mathbf { x } , \mathbf { y } ) \in \mathbf { D }$ .

- Lựa chọn tập Dz gồm k đối tượng ϵ - Đầu ra: nhãn của đối tượng kiểm tra được xác định là

$$
y ^ { ' } = \arg \operatorname* { m a x } \sum I ( v = y i )
$$

Trong đó:

- v là một nhãn trong tập nhãn

- I () là một hàm số trả lại giá trị 1 khi v có nhãn yi, 0 nếu trong trường hợp ngược lại.

- X là đối tượng xét, y là nhãn của nó.

Nhược điểm của thuật toán k-NN: Đòi hỏi không gian lưu trữ lớn.



Thuật toán MLkNN [13] là thuật toán k-NN áp dụng cho bài toán gán đa nhãn.

Phat bièu bài toán: cho 1 thè hièn x và tàp nhan két hop $\mathrm { Y } \subseteq \mathrm { Y }$ , k láng gièng duroc → nhac tói trong phurong pháp ML-KNN. Cho là $y _ { \textrm { x } }$ vector phàn loai cho x, vói l-th la thành phàn $\stackrel {  } { y } _ { \bf x } ( \mathrm { l } ) ( \mathrm { l } _ { \in \mathrm { ~ Y } } )$ mang giá tri 1 néu ε Y va 0 trong trròng hop nguoc lai. Them vào dó, cho N (x) tàp cua k láng gièng cua x trong tàp di lièu huán luyèn. Theo dó, nèn tang trèn tàp nhan cia nhing nguòi hàng xóm láng gièng, mòt vector thành vièn duroc dinh nghia nhur sau:

$$
\overrightarrow { C _ { x } } ( l ) = \sum _ { a \in N ( x ) } \overrightarrow { y _ { a } } ( l ) , l \in y
$$

Vói $\vec { C } _ { \mathrm { x } } \mathrm { t } \dot { \hat { \mathrm { o } } } \mathrm { n g } \ s \dot { \hat { \mathrm { o } } }$ trong láng gièng x tói lóp thur 1.

Trong mỗi trường hợp kiểm tra t, ML-KNN có k hàng xóm N (t) trong mỗi tập huấn luyện. Kí hiệu $\mathrm { H } ^ { 1 } \boldsymbol { 1 }$ là trường hợp t có nhãn l, $\mathrm { H } 0$ là trường hợp t không có nhãn l, Elj (jÎ{0, 1 … K}) biểu thị cho các trường hợp đó, giữa K láng giềng của t, chính xác j thể hiện có l nhãn. Do đó, nền tảng trên vector $C _ { \mathrm { t } } ,$ phân loại vector $y _ { \mathrm { t } }$ sử dụng theo nguyên tắc:

$$
\overrightarrow { y _ { t } } ( l ) = a r g m a x _ { b \in \{ 0 , 1 \} } P ( H ) _ { b } ^ { l } \ \Big | \ E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } \Big ) , l \in y
$$

Sử dụng luận Bayesian, có thể viết lại:



Mã giả thuật toán MLkNN được trình bày như sau:

// Tinh toán xác suát trróc P $\mathrm { ( H ^ { l } \mathfrak { b } ) }$

$$
\begin{array} { r } { \mid \mathrm { P } \left( \mathrm { H } _ { 1 } ^ { 1 } \right) = \left( \mathsf { s } + \sum _ { i = 1 } ^ { m } y _ { x i } ( l ) \right) / \left( \mathsf { s } \thinspace \mathbf { x } \thinspace 2 + \mathrm { m } \right) ; \mathrm { P } ( \mathrm { H } _ { 0 } ^ { 1 } ) = 1 - \mathrm { P } ( \mathrm { H } _ { 1 } ^ { 1 } ) } \end{array}
$$

$$
\begin{array} { r } { \operatorname { N h a n } \ \mathrm { d a n g ~ N ~ ( x i ) , i \in ~ \{ 1 , 2 \dots m \} ; } } \end{array}
$$

$$
\mathbf { f o r j } \in \{ 0 , 1 \dots \mathrm { K } \} \ \mathbf { d o }
$$

$$
\mathsf { c } [ \mathrm { j } ] = 0 ; \mathsf { c } ^ { \ast } [ \mathrm { j } ] = 0
$$

for i∈ { 1, .. m} do

$$
\begin{array} { r } { \mathcal { S } = \mathbf { C x i } ( \mathbf { l } ) = \sum _ { a \in \mathbf { N } ( \mathrm { x i } ) } y a ( l ) ; } \end{array}
$$

$$
{ \mathrm { i f ~ } } \ { \stackrel {  } { ( \gamma _ { \mathrm { x i } } ( \mathrm { l } ) } } = = 1 ) { \mathrm { ~ t h e n ~ c } } [ \delta ] = \mathbf { c } [ \delta ] + 1 ;
$$

for j ∈ {0, 1 . K} do

$$
\begin{array} { r l r } & { } & { { \mathrm { P } } ( \mathrm { E } _ { \mathrm { j } } ^ { 1 } \vert \mathrm {  ~ H ~ } ^ { 1 } _ { 1 } ) = ( \mathbf { s } + \mathbf { c } [ \mathbf { j } ] ) / \left( \mathbf { s } \mathbf { x } \left( \mathrm { K } + 1 \right) + \sum _ { p = 0 } ^ { k } c [ p ] \right) } \\ & { } & { { \mathrm { P } } ( \mathrm { E } _ { \mathrm { j } } ^ { 1 } \vert \mathrm {  ~ H ~ } ^ { 1 } _ { 0 } ) = ( \mathbf { s } + \mathbf { c } ^ { \prime } [ \mathbf { j } ] ) / \left( \mathbf { s } \mathbf { x } \left( \mathrm { K } + 1 \right) + \sum _ { p = 0 } ^ { k } c [ p ] \right) } \end{array}
$$

/tinh toáan $\vec { \bf \Phi } _ { y _ { \mathrm { t } } } ^ { \prime }$ và $\vec { N }$

(14)

(15)

$$
\begin{array} { r l } & { \mathrm { N h } \acute { \underset { \mathbf { \xi } } { \mathrm { A n } } } \mathrm { ~ d a n g ~ N ~ ( t ) } } \\ & { \mathrm { ~ } } \\ & { \widehat { C _ { t } } ( l ) = \sum _ { a \in N ( t ) } \overrightarrow { y _ { a } } ( l ) ; } \\ & { \qquad } \\ & { \qquad \quad \widehat { y _ { \mathrm { t } } } ( { \sf l } ) = \arg \operatorname* { m a x } _ { \mathbf { \lambda } \in \{ 0 , 1 \} } \mathrm { ~ P ~ } ( { \sf H } _ { \mathrm { b } } ^ { l } ) \mathrm { ~ P ~ } ( { \cal E } _ { \mathbf { \Lambda } \_ { C ( I ) } } ^ { l } \mid H _ { b } ^ { l } ) ; } \end{array}
$$

$$
\overrightarrow { r _ { t } } ( l ) = P \left( H _ { b } ^ { l } \Big | E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } \right) = ( P ( H _ { 1 } ^ { l } ) P \left( E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } \Big | H _ { 1 } ^ { l } ) / P E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } \right)
$$

$$
= ( P ( H _ { 1 } ^ { l } ) P ( E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } | H _ { 1 } ^ { l } ) ) / ( \sum _ { b \in \{ 0 , 1 \} } P ( H _ { b } ^ { l } ) P ( E _ { \overrightarrow { C _ { t } } ( l ) } ^ { l } | H _ { b } ^ { l } ) )
$$



# Random k-labelsets (RAKEL)

Phương pháp Label Powerset (LP) là một phương pháp chuyển đổi của phân lớp dữ liệu đa nhãn mà có xem xét đến sự phụ thuộc của các nhãn lớp. Ý tưởng của phương pháp này là coi một tập con các nhãn như là một nhãn và tiến hành phân lớp như việc phân lớp dữ liệu đơn nhãn. Theo phương pháp này thì số lượng các tập con nhãn được tạo ra là rất lớn, Grigorios và đồng nghiệp [11] đã đề xuất phương pháp RAKEL với mục đích tính đến độ tương quan giữa các nhãn, đồng thời tránh những vấn đề nói trên của LP.

Định nghĩa tập $\mathrm { K }$ nhãn, cho tập nhãn L của phân lớp đa nhãn, L= $\{ \lambda \mathrm { i } \}$ , với $\mathrm { i } = 1 \ldots$ |L|. Một tập $\mathrm { \Delta Y \subseteq L }$ với $\mathrm { K } = | \mathrm { L } |$ gọi là tập K nhãn. Ta sử dụng giới hạn $\mathrm { L } ^ { \mathrm { K } }$ là tập của tất cả tập nhãn $\mathrm { K }$ khác nhau trên L. Kích thước $\mathrm { L } ^ { \mathrm { K } }$ cho bởi công thức: $\vert \mathrm { L } ^ { \mathrm { K } } \vert = ( ^ { \vert \mathrm { L } \vert } \kappa )$ .

Thuật toán RAKEL là cấu trúc toàn bộ của m phân loại LP, với $\dot { 1 } =$ 1 …m, chọn ngẫu nhiên một tập $\mathrm { K }$ nhãn, Yi, từ $\mathrm { L } ^ { \mathrm { k . } }$ Sau đó, học phân loại LP $h _ { i }$ : $X  P ( Y _ { i } )$ . Thủ tục của RAKEL:

Dàu vào: só cùa các mò hinh m, kích thróc cua tàp K nhān, tàp cua các nhan L, tàp huán luyen D. Dàu ra: toàn bo cuia phàn lóp LP $\mathrm { h } _ { \mathrm { i } }$ và trong 'ng tàp K nhan $\mathrm { Y _ { i } }$ : $_ { \mathrm { R }  \mathrm { L } ^ { \mathrm { K } } }$ for i ←— 1 dén min (m, LK) do $\mathrm { Y _ { i }  }$ mòt tàp nhan k ngǎu nhièn chon tir R; Huán luyèn mot phàn lóp LP hi: $\mathrm { X } \longrightarrow \mathrm { P }$ (Yi) tren D R ←R \ {Yi} ;

# Hình 2.2 Mã giả thuật toán RAKEL

Số của sự lặp lại (m) là một tham số cụ thể cùng dãy giá trị có thể chấp nhận được từ 1 tới $| \mathrm { L } ^ { \mathrm { K } } |$ . Kích cỡ của tập $\mathrm { K }$ nhãn là một tham số cụ thể cùng dãy giá trị từ 2 tới |L| - 1. Cho $\mathrm { K } = 1$ và $\mathbf { m } = | \mathrm { L } |$ ta phân loại



toàn bộ nhị phân của phương pháp Binary Relevance, khi $\mathrm { K } = | \mathrm { L } |$ (cid:) $\mathbf { \langle m = }$ 1). Giả thiết việc sử dụng tập nhãn có kích thước nhỏ, số lặp vừa đủ, khi đó RAKEL sẽ quản lý để mô hình nhãn tương quan hiệu quả.

# ClassifierChain (CC)

Thuật toán này bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ chuyển đổi nhị phân L như BR. Thuật toán này khác với thuật toán BR trong không gian thuộc tính cho mỗi mô hình nhị phân, nó được mở rộng cùng nhãn 0/1 cho tất cả phân lớp trước đó [8]. Ví dụ, chuyển đổi giữa BR và CC cho (x, y) với $\mathrm { { y } = [ 1 , 0 , }$ 0, 1, 0] và $\mathbf { x } = [ 0 , 1 , 0 , 1 , 0 , 0 , 1 , 1 , 0 ]$ (giả sử, cho đơn giản, không gian nhị phân). Mỗi phân loại hj được huấn luyện dự đoán yj $= \{ 0 , 1 \}$ .

<table><tr><td>Chuyén</td><td></td><td></td><td>dói nhi phàn gia BR và CC [8]</td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td rowspan=1 colspan=1>Chuyěn dói cüa BR</td><td rowspan=1 colspan=1>Chuyěn dói cüa CC</td></tr><tr><td rowspan=1 colspan=1>h:     x→                     y</td><td rowspan=1 colspan=1>h： x^→                                y</td></tr><tr><td rowspan=1 colspan=1>h1: [0, 1, 0, 1, 0, 0, 1, 1, 0]    1Raceh2: [0, 1, 0, 1, 0, 0, 1, 1, 0] 0h3: [0, 1, 0, 1, 0, 0, 1, 1, 0] 0h4: [0, 1, 0, 1, 0, 0, 1, 1, 0]h5: [0, 1, 0, 1, 0, 0, 1, 1, 0]   0</td><td rowspan=1 colspan=1>h1: [0, 1, 0, 1, 0, 0, 1, 1, 0]             1h2: [0, 1, 0, 1, 0, 0, 1, 1, 0, 1]         0h3: [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]  0h4: [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0]h5: [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1] 0</td></tr></table>