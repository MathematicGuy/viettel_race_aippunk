### TASK EXTRACT

# Public_101 

# Phát biểu bài toán

Trong học sâu, một bài toán cơ bản là huấn luyện mô hình mạng nơ-ron sâu để tối ưu hóa tham $\mathrm { s } \acute { 0 } \mathrm { m } \acute { 0 }$ hình nhằm giảm thiểu hàm mất mát (loss function). Bài toán này được biểu diễn như sau:

$$
\theta ^ { * } = a r g \operatorname* { m i n } _ { \theta } L ( \theta )
$$

Trong đó:

o ??: Là các tham số của mô hình   
o ??(??): Là hàm mất mát đo lường độ chênh lệch giữa dự đoán của mô hình và nhãn thực tế.

Thuật toán Stochastic Gradient Descent (SGD) thường được sử dụng để giải quyết bài toán trên bằng cách cập nhật các tham số dựa trên gradient của hàm mất mát theo công thức:

$$
\theta  \theta - \eta \cdot \nabla L ( \theta )
$$

Trong đó:

o η: Tốc độ học (learning rate).   
o ∇L(θ): Gradient của hàm mất mát.

Thuật toán SGD (tuần tự) hoạt động theo các bước sau:

Bước 1: Khởi tạo tham số ban đầu với giá trị ngẫu nhiên.

Bước 2: Lặp lại qua các epoch: Chia tập dữ liệu thành các batch nhỏ. Lặp qua từng batch: $^ +$ Tính gradient trên batch. + Cập nhật

Bước 3: Kết thúc khi số epoch đạt ngưỡng hoặc hàm mất mát không còn cải thiện.

Mã giả:





# Thuật Toán Song Song

Để tối ưu hóa thuật toán Stochastic Gradient Descent (SGD) trong môi trường phân tán, hai thiết kế song song chính được triển khai: Thiết kế tập trung (Centralized Design) và Thiết kế phân tán (Decentralized Design). Cả hai phương pháp nhằm mục tiêu giảm thời gian huấn luyện và đảm bảo độ chính xác mô hình.

## Thiết kế tập trung (Centralized Design)

Thiết $\mathrm { k } \acute { \mathrm { e } }$ tập trung dựa trên việc sử dụng một tiến trình trung tâm (master node) để quản lý toàn bộ quá trình huấn luyện. Master chịu trách nhiệm khởi tạo và điều phối các tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình, đồng thời nhận kết quả từ các tiến trình còn lại (worker nodes). Các worker thực hiện tính toán gradient cục bộ dựa trên phần dữ liệu được phân công, sau đó gửi kết quả này về master. Master sẽ tổng hợp thông tin từ các worker, cập nhật tham số mô hình, và phát truyền lại tham số đã cập nhật để tiếp tục vòng huấn luyện. Cách tiếp cận này giúp duy trì tính nhất quán của mô hình và đảm bảo quy trình huấn luyện được đồng bộ hóa.

# Luồng hoạt động:

Master khởi tạo các tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình và phát truyền chúng đến các worker.

- Mỗi worker huấn luyện trên dữ liệu của mình, tính toán gradient cục bộ và gửi kết quả về master.

- Master tổng hợp gradient từ các worker, cập nhật tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình và truyền lại cho các worker.

- Quá trình lặp lại cho đến khi hoàn tất số lượng epoch hoặc đạt điều kiện dừng.

Mã giả:



Master Node:

1. Initialize model parameters θ.   
2. Broadcast θ to all worker nodes.

3. Repeat for each epoch:

a. Gather gradients $\{ \nabla \mathtt { L } ( \Theta ) \underline { { \mathrm { ~ i ~ } } } \}$ from all worker nodes. b. Compute weighted average of gradients: $\nabla \mathbb { L } ( \Theta ) \quad = \quad \mathbb { \Omega } \ ( \mathbb { w } \mathrm { ~ \underline { ~ { ~ i ~ } ~ } ~ } \star \quad \nabla \mathbb { L } ( \Theta ) \mathrm { ~ \underline { ~ { ~ i ~ } ~ } ) ~ } \mathrm { ~ / ~ } \ \Sigma \ ( \mathbb { w } \mathrm { ~ \underline { ~ { ~ i ~ } ~ } ~ } )$ c. Update parameters: $\theta ~ = ~ \theta ~ - ~ \eta ~ \star ~ \nabla \mathrm { L } ~ ( $ (θ). d. Broadcast updated $\ominus$ to all worker nodes.

4. Output final model θ.

Worker Node:

1. Receive initial model parameters θ from master.

2. Repeat for each epoch: a. Compute gradient ∇L(θ)_i on local dataset. b. Send ∇L(θ)_i to master. c. Receive updated θ from master.

3. Terminate.

Thiết kế tập trung có ưu điểm lớn ở tính quản lý tập trung, giúp dễ triển khai và theo dõi trạng thái của toàn bộ hệ thống. Đây là phương pháp phù hợp khi số lượng worker nhỏ, do việc xử lý và tổng hợp thông tin ở master không gây quá tải. Tuy nhiên, nhược điểm chính là master dễ trở thành điểm cổ chai (bottleneck) khi số lượng worker lớn, dẫn đến hiệu suất giảm. Đồng thời, chi phí truyền thông giữa master và các worker tăng đáng kể khi số lượng tiến trình tăng, gây ảnh hưởng đến khả năng mở rộng của hệ thống.

## Thiết kế phân tán (Decentralized Design)

Thiết kế phân tán (Decentralized Design) loại bỏ hoàn toàn vai trò của master node, đảm bảo tất cả các tiến trình (nodes) tham gia bình đẳng vào quá trình tính toán và tổng hợp thông tin. Các nodes khởi tạo tham số mô hình giống nhau và thực hiện huấn luyện trên dữ liệu cục bộ. Thông qua cơ chế Allgather, các nodes chia sẻ gradient hoặc trọng số với nhau, sau đó mỗi node tính toán giá trị trung bình từ thông tin thu thập được để cập nhật tham số mô hình. Cách tiếp cận này tạo ra một quy trình đồng đẳng, trong đó các tiến trình hoạt động độc lập nhưng vẫn duy trì tính nhất quán của mô hình.

# Luồng hoạt động:



1. Tất cả các nodes khởi tạo tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình giống nhau.

2. Mỗi node huấn luyện trên tập dữ liệu cục bộ, tính toán gradient.

3. Các nodes sử dụng Allgather để chia sẻ gradient hoặc trọng số.

4. Mỗi node cập nhật tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình dựa trên giá trị trung bình thu thập được.

5. Quá trình lặp lại cho đến khi hoàn tất.

# Mã giả:

All Nodes:

1. Initialize model parameters θ.

2. Repeat for each epoch:

a. Compute gradient ∇L(θ)_i on local dataset.   
b. Share gradients using Allgather.   
c. Compute average gradient: ∇L(θ) = Σ(∇L(θ)_i) / N (where N is the number of nodes).   
d. Update parameters: $\theta ~ = ~ \theta ~ - ~ \eta ~ \star ~ \nabla \mathbb { L } \left( \theta \right)$ .

3. Output final model θ.

Thiết kế phân tán có ưu điểm vượt trội trong việc loại bỏ điểm cổ chai (bottleneck) thường gặp ở master node, giúp cải thiện khả năng mở rộng khi số lượng nodes tăng. Các nodes hoạt động đồng đẳng, không phụ thuộc vào một trung tâm, từ đó tăng tính linh hoạt và khả năng chịu lỗi của hệ thống. Tuy nhiên, nhược điểm lớn nhất của thiết $\mathrm { k } \acute { \mathrm { e } }$ này là chi phí truyền thông cao hơn, do tất cả các nodes đều phải chia sẻ thông tin với nhau. Đồng thời, việc triển khai và đồng bộ hóa các nodes cũng phức tạp hơn, đặc biệt trong các hệ thống lớn và đa dạng về tài nguyên.

# Public_102 

# Định nghĩa

![](images/image1.jpg)  
Hình 1. Linear-Chain CRFs dạng factor với các ô vuông là các hàm phụ thuộc giữa các nút

Gọi X là biến ngẫu nhiên đại diện cho chuỗi dữ liệu đầu vào cần được gán nhãn, Y là biến ngẫu nhiên đại diện cho chuỗi nhãn tương ứng với chuỗi dữ liệu X. Tất cả các thành phần $Y _ { i }$ của Y thuộc một tập nhãn hữu hạn $\mathcal { Y }$ (tập các nhãn có thể có). $\varOmega _ { x }$ là các trường hợp có thể có của chuỗi X, $\varOmega _ { y }$ là các trường hợp có thể có của chuỗi nhãn Y.

Giả định cả X và Y đều được coi là biến ngẫu nhiên phân phối chung (jointly distributed), nghĩa là chúng có mối liên hệ xác suất với nhau, và xác suất $P ( X , Y )$ là dương nghiêm ngặt $( P ( X = \ x , Y = y ) > 0 , \forall x , y )$ .

CRFs [8] là một mô hình phân biệt, tập trung vào việc xây dựng mô hình xác suất có điều kiện P(Y|X). CRFs dự đoán chuỗi nhãn Y dựa trên chuỗi dữ liệu X đã cho. CRFs không cố gắng mô hình hóa xác suất của $\mathrm { X }$ (tức là P(X)), mà chỉ quan tâm đến xác suất của Y khi biết X.

Định nghĩa: Cho đồ thị $G = ( V , E )$ sao cho $Y = ( Y _ { v } ) _ { v \in V } ,$ nghĩa là ?? được chỉ mục hóa theo các đỉnh của đồ thị $G$ . Khi đó, cặp $( X , Y )$ là một trường ngẫu nhiên điều kiện (conditional random fields - CRFs) trong trường hợp, khi biết $X$ , các biến ngẫu nhiên $Y _ { v }$ thỏa mãn tính chất Markov đối với đồ thị:

$$
P ( Y _ { v } | X , Y _ { w } , w \neq v ) = \ P ( Y _ { v } | X , Y _ { w } , w { \sim } v )
$$



trong đó $w { \sim } v$ có nghĩa là ?? và $v$ là các đỉnh kề nhau trong đồ thị ??. Hay nói cách khác trạng thái của các đỉnh trong đồ thị chỉ phụ thuộc vào các điểm lân cận.

$= >$ CRFs là một trường hợp đặc biệt của MRF, trong có các nút có thể chia thành 2 tập riêng biệt X, Y. Và xác suất của chuỗi nhãn Y được xác định dựa trên toàn bộ chuỗi quan sát X. Do X là các biến quan sát lên cấu trúc đồ thị của X là tùy ý và Y và các biến y ∈ Y có th $\acute { \hat { \mathbf { e } } }$ phụ thuộc vào bất kì biến nào trong X.

Trong trường hợp CRFs có X, Y là các chuỗi $\mathrm { X } = ( \mathrm { X } 1 , . . . , \mathrm { X } { \mathrm { n } } )$ , $\mathrm { Y } = ( \mathrm { Y } 1 , . . . ,$ Yn) và đồ thị G là cây mà các đỉnh có bậc không quá 2 (chuỗi tuyến tính) thì được gọi là trường ngẫu nhiên có điều kiện tuyến tính (Linear-Chain CRFs).

![](images/image2.jpg)  
Hình 2. Ví dụ minh họa Linear-Chain CRFs trong bài toán gán nhãn thực thể có

tên

Hình 2 là một ví dụ về Linear-Chain CRFs được sử dụng trong bài toán gán nhãn thực thể có tên (tìm xem từ nào là tên riêng – PER, từ nào là tên địa danh – LOC). Ở đây, các từ trong câu đầu vào cần được gán nhãn sẽ có vai trò là chuỗi X, các nhãn cần được gán cho từng từ trong câu đầu vào sẽ là chuỗi Y. Các nhãn này sẽ nhận một trong các giá trị: PER-Tên riêng, LOC-Địa điểm, O-Không xác định. Theo tích chất Markov thì nhãn của từ hiện tại chỉ phụ thuộc vào nhãn trước, nhãn sau và câu đầu vào.

# Xây dựng mô hình xác suất $\mathbf { P } ( \mathbf { Y } | \mathbf { X } )$

Với giả định $P ( X = x , Y = y )$ là dương nghiêm ngặt, theo định lý Hammersley–Clifford [9], ta có:



$$
E ( x , y ) = \mathrm { ~ - ~ } \sum _ { c _ { i } \in C } f _ { i } \left( c _ { i } \right)
$$

$$
P ( X = x , Y = y ) = \frac { 1 } { Z } e ^ { - E ( x , y ) }
$$

$$
Z = \sum _ { x \in \varOmega _ { x } , y \in \varOmega _ { y } } e ^ { - E ( x , y ) }
$$

Trong đó C là tập tất cả các nhóm đầy đủ của $\mathtt { d } \overset { \triangledown } { \hat { \boldsymbol { \alpha } } }$ thị G (một nhóm đầy đủ trong đồ thị vô hướng là một tập hợp các đỉnh mà giữa tất cả các cặp đỉnh trong tập hợp đó đều tồn tại một cạnh), $f _ { i }$ là hàm năng lượng của cụm $c _ { i }$ chỉ ra khả năng xảy ra các mối quan $\mathrm { h } \hat { \mathrm { e } }$ trong cụm. Z là hằng số chuẩn hóa để tạo phân phối xác suất hợp lệ $( < 1 )$ . $E ( x , y )$ là hàm năng lượng được sử dụng để đánh giá mức độ "tốt" của một cặp giá trị $( x , y )$ cụ th $\acute { \hat { \mathbf { e } } }$ của các biến ngẫu nhiên X, Y. Cặp giá trị $( x , y )$ có $E ( x , y )$ thấp hơn được coi là tốt hơn.

Dựa vào công thức trên kết hợp định lý Bayes, ta suy ra phân phối của chuỗi nhãn Y khi biết X có dạng sau:

$$
\begin{array} { c c l } { P ( Y = y | X = x ) = \displaystyle \frac { P ( Y = y , X = x ) } { \bigotimes ^ { \otimes \langle P \rangle } } = \displaystyle \frac { \frac { e ^ { - E ( X , y ) } } { Z } } { \sum _ { y ^ { \prime } \in \mathcal { Q } _ { y } } e ^ { - E ( x , y ^ { \prime } ) } } } \\ { \displaystyle } & { \displaystyle \qquad = \frac { e ^ { - E ( x , y ) } } { Z ( x ) } } \\ { \displaystyle } & { = \frac { e x p \left( \sum _ { c \in \mathcal { C } } f _ { i } ( c _ { i } ) \right) } { Z ( x ) } } \end{array}
$$



Với Linear-Chain CRFs, tập các cụm là 2 đỉnh của các cạnh và các đỉnh lẻ, khi đó, ta có:

$$
E ( x , y ) = { } - \left( \sum _ { ( i - 1 , i ) \in E } f \left( y _ { i - 1 } , y _ { i } , x , i \right) + \sum _ { y _ { i } \in y } g \left( y _ { i } , x , i \right) \right)
$$

Để đơn giản, ta thêm 2 nhãn vào đầu và cuối chuỗi nhãn: $\mathrm { Y } 0 = <$ <Start>. Trong Linear-Chain CRFs, hàm năng lượng cho các cạnh là tổng hợp các hàm đặc trưng cạnh $f _ { k }$ và hàm năng lượng cho đỉnh là tổng hợp các hàm đặc trưng của đỉnh $g _ { k }$ .

$$
E ( x , y ) = \ - \left( \sum _ { i = 1 } ^ { n } \sum _ { k } \lambda _ { k } \ f _ { k } ( y _ { i - 1 } , y _ { i } , x , i ) + \ \sum _ { i = 1 } ^ { n } \sum _ { k } \mu _ { k } \ g _ { k } ( y _ { i } , x , i ) \right)
$$

$$
\begin{array} { r l } {  { _ { \theta } ( Y = y | X = \ x ) } } \\ & { = \ \frac { e x p ( \sum _ { i = 1 } ^ { n } \sum _ { k } \lambda _ { k } f _ { k } ( y _ { i - 1 } , y _ { i } , x , i ) + \ \sum _ { i = 1 } ^ { n } \sum _ { k } \mu _ { k } \ g _ { k } ( y _ { i } , x , i ) ) } { Z _ { \theta } ( x ) } } \end{array}
$$

$$
_ { \geqslant } ( x ) = \sum _ { y ^ { \prime } \in \varOmega _ { y } } e x p \left( \sum _ { i = 1 } ^ { n } \sum _ { k } \lambda _ { k } f _ { k } ( y ^ { \prime } _ { i - 1 } , y ^ { \prime } _ { i } , x , i ) + \sum _ { i = 1 } ^ { n } \sum _ { k } \mu _ { k } g _ { k } ( y ^ { \prime } _ { i } , x , i ) \right)
$$

Các hàm đặc trưng $f _ { k } { \mathrm { v a } } \ g _ { k }$ được cho trước và cố định, thường là chỉ báo cho 1 đặc trưng ví dụ $1$ hàm đặc trưng sẽ trả $\mathbf { v } \dot { \hat { \mathbf { e } } }$ giá trị 1 khi $X _ { i }$ viết hoa chữ cái đầu và $Y _ { i }$ có nhãn là “N” ngược lại sẽ trả về 0.

Trọng số $\lambda _ { k }$ , $\mu _ { k }$ của hàm đặc trưng là một hệ số điều chỉnh mức độ ảnh hưởng của hàm đặc trưng đến năng lượng của cấu hình. Trọng số càng cao, hàm đặc trưng càng có ảnh hưởng lớn đến xác suất của chuỗi nhãn.



# Linear-Chain CRFs dạng ma trận

Giả sử, $\mathcal { Y } = \{ C _ { 1 } , \dots , C _ { l } \} , \mathcal { Y } ^ { \prime } = \mathcal { Y } \cup \{ < S t a r t > \}$ . Xác xuất có điều kiện của chuỗi Y có thể được biểu diễn dưới dạng ma trận. Tại mỗi vị trí i trong chuỗi quan sát $\mathbf { X }$ , ta định nghĩa một ma trận biến ngẫu nhiên kích thước $| \mathcal { Y } ^ { \prime } | \times | \mathcal { Y } ^ { \prime } | , M _ { i } ( x ) =$ $\bigl [ M _ { i } \bigl ( C _ { j } , C _ { k } \bigl | x \bigr ) \bigr ] , \ C _ { j } , C _ { k } \in \mathcal { Y } .$

Mỗi phần tử $M _ { i } { \left( C _ { j } , C _ { k } \middle | x \right) }$ đại diện cho một giá trị xác suất chưa chuẩn hóa. $M _ { i } ( x )$ là biến ngẫu nhiên mà giá trị phụ thuộc vào chuỗi quan sát X.

$$
\begin{array} { r l } {  { M _ { i } \big ( C _ { j } , C _ { k } \big | x \big ) } } \\ & { = \textstyle { e x p } ( \sum _ { k } \lambda _ { k } f _ { k } \big ( Y _ { i - 1 } = C _ { j } , y _ { i } = C _ { k } , x , i \big )  } \\ & { +  \sum _ { k } \mu _ { k } g _ { k } \big ( Y _ { i } = C _ { j } , x , i \big ) ) } \end{array}
$$

Với cách biểu diễn trên, $Z _ { \theta } ( x )$ có thể viết lại dưới dạng sau với $1 _ { | \mathcal { Y } \prime | \times 1 }$ là ma trận kích thước $| \mathcal { Y } ^ { \prime } |$ hàng và 1 cột có các giá trị bằng 1:

$$
{ \cal Z } _ { \theta } ( x ) = \left( M _ { 1 } ( x ) \times M _ { 2 } ( x ) \times . . . \times M _ { n + 1 } \times 1 _ { | \mathcal { Y } | \times 1 } \right) _ { 0 , 0 }
$$

Công thức xác suất có điều kiện có thể biểu diễn dưới dạng ma trận:

$$
p _ { \theta } ( Y = y | X = x ) = \ { \frac { \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) } { \left( \left( \prod _ { i = 1 } ^ { n } M _ { i } ( x ) \right) \times 1 _ { | \mathcal { Y } | \times 1 } \right) _ { 0 , 0 } } }
$$

Biểu diễn này hữu ích trong việc huấn luyện và suy luận mô hình CRFs.



![](images/image3.jpg)  
Hình 3. Linear-Chain CRFs biều diễn dưới dạng factor với các factor được coi là ma trận chuyển đổi

Hình 3 là một ví dụ mình họa của linear-Chain CRFs biểu diễn dưới dạng factor cho bài toán POS tiếng Việt (gán nhãn động từ - v, danh từ - n, đại từ - p, trạng từ - d). Ở đây, câu đầu vào có 5 từ và mỗi 1 từ sẽ được gán nhãn từ loại tương ứng. Chuỗi từ loại chính là chuỗi Y. Giữa mỗi cặp nhãn cần gán kề nhau sẽ có một ma trận thể hiện khả năng mà giá trị nhán được gán khi biết nhãn của từ liền kề.

# Public_103 

# Giải thích:

Tương tự CRFs, Linear-Chain CRFs phân loại chuỗi dựa trên xác suất $P ( Y \vert X )$ . Với chuỗi x cho trước, CRFs sẽ tìm ra chuỗi y sao cho xác suất $P ( Y = y | X = x )$ là lớn nhất.

$$
\hat { y } = a r g m a x _ { y } P ( y | x )
$$

Xác suất $P ( Y \vert X )$ được xây dựng thông qua việc định nghĩa các hàm đặc trưng $f _ { k } { \mathrm { v } } { \dot { { \mathrm { a } } } } g _ { k }$ và xác định giá trị $\lambda _ { k } , \mu _ { k }$ . Các trọng số được tối ưu trong quá trình huấn huyện với tập dữ liệu huấn luyện. Nói cách khác, quá trình huấn luyện CRFs là quá trình học phân phối xác suất $P ( Y \vert X )$ của tập dữ liệu huấn luyện.

Việc tối ưu hóa các trọng $\begin{array} { r } { \mathrm { s } \hat { \hat { \mathbf { o } } } \theta = ( \lambda _ { 1 } , \dots , \lambda _ { k } ; \mu _ { 1 } , \dots , \mu _ { k } ) } \end{array}$ tương đương với việc tìm kiếm hàm năng lượng tối ưu cho mô hình. Mô hình CRFs sẽ điều chỉnh các trọng số để hàm đặc trưng phản ánh chính xác mối quan hệ giữa chuỗi quan sát và chuỗi nhãn, từ đó đưa ra dự đoán chính xác nhất. Do đó, hàm đặc trưng đóng vai trò then chốt trong việc xác định $\mathrm { m } \acute { \mathrm { o 1 } }$ quan hệ giữa chuỗi quan sát x và chuỗi nhãn y. Việc lựa chọn và thiết kế hàm đặc trưng phù hợp với bài toán cụ thể là rất quan trọng để đảm bảo mô hình có thể học được các mẫu quan trọng từ dữ liệu và đưa ra dự đoán chính xác.

# Huấn luyện

Việc huấn luyện thường sử dụng phương pháp MLE (Maximum Likelihood Estimation) để tối ưu hóa các trọng số $\theta = ( \lambda _ { 1 } , \ldots , \lambda _ { k } ; \mu _ { 1 } , \ldots , \mu _ { k } )$ từ tập huấn luyện $D = \{ ( x ^ { ( i ) } , y ^ { ( i ) } ) \} _ { i = 1 } ^ { N } . \}$ Mục tiêu của quá trình huấn luyện là tìm ra bộ trọng số $\theta$ để hàm mục tiêu log-likelihood $L ( \theta )$ là lớn nhất.

$$
L ( \theta ) = \sum _ { i = 1 } ^ { N } l o g \left( P _ { \theta } { \bigl ( } y ^ { ( i ) } { \bigl | } x ^ { ( i ) } { \bigr ) } \right)
$$



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



t-1 và t khi biết $\boldsymbol { x } ^ { ( i ) }$ mà không quan tâm đến các nhãn còn lại. Xác suất biên này có th $\dot { \hat { \mathbf { e } } }$ được tính trong thời gian đa thức bằng thuật toán Forward-Backward.

Tương tự cho $\mu _ { k }$ :

$$
E _ { x } ( g _ { k } ) = \sum _ { t = 1 } ^ { n } \sum _ { y ^ { \prime } \in \mathcal { Y } } g _ { k } \big ( y ^ { \prime } , x ^ { ( i ) } , t \big ) P \big ( Y _ { t } = y ^ { \prime } \big | x ^ { ( i ) } \big )
$$

# Thuật toán Forward-Backward áp dụng trong tính gradient

![](images/image1.jpg)  
Hình 3.1. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 nút

Ý tưởng của thuật toán Forward-Backward là tính xác suất biên dựa vào việc tính xác suất tiến $\alpha _ { i } ( x )$ và xác suất lùi $\beta _ { i } ( x )$ . Hình $8 \mathrm { m } \hat { \mathrm { o } }$ tả ý tưởng tính xác suất biên $P ( Y _ { 2 } = v | x )$ và $\operatorname { h i n h } \ 9 \cdot \mathrm { m } \widehat { \mathrm { ~ } }$ tả ý tưởng cách tính xác suất biên $P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x )$ cho bài toán POS. Mỗi một đường đi từ ${ \bf \mathrm { < } } { \bf { S } } >$ đến <T> là 1 trường hợp của chuỗi Y. Trọng số của của mỗi cạnh được tính theo công thức $M _ { i } ( C _ { j } , C _ { k } | x ) \backslash$ đã trình bày $\acute { \mathbf { O } }$ phần trước thể hiện khả năng nhãn của từ liền kề khi biết trước nhãn, trọng số của 1 đường đi là tích các trọng số cạnh mà đường đi qua.

$$
p _ { \theta } ( Y = y | X = x ) = \left. p _ { \theta } \big ( p a t h _ { y } \big | X = x \big ) = \frac { T r _ { 0 } n g s \tilde { \mathcal { O } } ~ c \tilde { \mathsf { u } } a ~ p a t h _ { y } } { Z _ { \theta } ( x ) } \right.
$$



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



![](images/image2.jpg)  
Hình 3.2. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 cạnh

Tương tự với xác suất biên $P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x )$ , ta có:

$$
\begin{array} { r l } & { P ( Y _ { t - 1 } = y ^ { \prime } , Y _ { t } = y ^ { \prime \prime } | x ) } \\ & { \qquad = \frac { \alpha _ { t - 1 } ( Y _ { t - 1 } = y ^ { \prime } | x ) \times M _ { t } ( y ^ { \prime } , y ^ { \prime \prime } | x ) \times \beta _ { t } ( Y _ { t } = y ^ { \prime \prime } | x ) } { Z _ { \theta } ( x ) } } \end{array}
$$

Bằng phương pháp quy hoạch động, ta có th $\acute { \hat { \mathbf { e } } }$ tính các xác suất biên với độ phức tạp $O ( n \times | \mathcal { Y } | ^ { 2 } )$ và chính là độ phức tạp khi tính kì vọng của các hàm đặc trưng.

# Thuật toán Viterbi áp dụng trong suy luận Linear-Chain CRFs

Xác định chuỗi $\hat { y }$ có xác suất xảy ra cao nhất khi biết x:

$$
\hat { y } = a r g m a x _ { y } \ : P ( y | x ) = a r g m a x _ { y } \frac { \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) } { Z _ { \theta } ( x ) } 
$$

Vì $Z _ { \theta } ( x )$ là hằng số khi biết nên việc xác định chuỗi $\hat { y }$ có xác suất xảy ra cao nhất khi biết x t:

$$
\begin{array} { r l r } {  { \operatorname { t r o n g } \mathrm { d u o n g ~ v o i x a c ~ d i n h ~ c h u \tilde { \hat { o } } i } \hat { y } \mathrm { d } \hat { \hat { e } } \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) \mathrm { l o n } \mathrm { n h } \hat { \hat { a } } } } \\ & { } & { \hat { y } = a r g m a x _ { y } \displaystyle \prod _ { i = 1 } ^ { n } M _ { i } ( y _ { i - 1 } , y _ { i } | x ) } \end{array}
$$

Việc tìm $\hat { y }$ có thể tính trong thời gian $O ( n \times | \mathcal { Y } | ^ { 2 } )$ với thuật toán quy hoạch động Viterbi. Thuật toán Viterbi được mô tả bằng $\mathrm { m } \tilde { \mathbf { a } }$ giả trong hình 10.



![](images/image3.jpg)  
Hình 4.1: Thuật toán Viterbi cho suy luận Linear-chain CRFs

$M _ { i } ( x )$ là ma trận đã được trình bày trong phần 3 với hàng 0 và cột 0 tương ứng với nhãn <Start>.



![](images/image4.jpg)  
Hình 4.2: Hình minh họa thuật toán Viterbi cho POS

Hình 4.2 là minh họa quá trình suy luận Viterbi cho POS. Giả sử sau khi huấn luyện ta đã có được trọng số của các đường đi $M _ { i }$ . Với đầu câu đầu vào có 4 từ, và cần gán nhãn cho 4 từ này một nhãn từ loại là 1 trong 4 giá trị: v, n, p, d. Ở đây, mỗi một miền tương đương với 1 từ cần được gán nhãn và số đỉnh trong miền là nhãn có thể có của từ, ví dụ, miền Y1 có 4 đỉnh là v, n, p, d tương đương với 4 giá trị có thể gán cho từ đầu tiên của câu. Một đường đi hợp lệ là đường đi đi qua duy nhất một đỉnh trong mỗi miền. Thuật toán Viterbi sẽ tìm đường sao cho trọng số là lớn nhất (tương đương với xác suất chuỗi nhãn là lớn nhất.

Ý tưởng của Viterbi là đường đi lớn nhất đến một đỉnh sẽ bao gồm đường đi lớn nhất đến đỉnh trước nó. Xuất phát từ ý tưởng này, để tìm đường đi lớn nhất đến miền Y4, ta sẽ tính đường đi lớn nhất đến các đỉnh của miền Y3, sau đó từ các đỉnh của Y3 ta tính trọng số đến các đỉnh của Y4 và chọn ra đường đi có trọng số lớn nhât. Tương tự đường đi có trọng số lớn nhất đến các đỉnh trong Y3 có thểtính qua đường đi có trọng số lớn nhất đến các đỉnh trong Y2, ….

# Public_104 

# Khái niệm cơ bản về Hidden Markov Model (HMM)

Hidden Markov Model (HMM) là một mô hình thống kê được sử dụng để phân tích các chuỗi dữ liệu có tính chất tuần tự, trong đó trạng thái thực của hệ thống (trạng thái ẩn) không thể quan sát trực tiếp, nhưng có thể suy ra thông qua các quan sát (observations). HMM kết hợp hai quá trình ngẫu nhiên:

Một quá trình Markov ẩn, mô tả sự chuyển đổi giữa các trạng thái ẩn. Một quá trình phát xạ, liên kết mỗi trạng thái ẩn với một tập các quan sát theo một phân phối xác suất.

HMM thường được biểu diễn thông qua các thành phần sau:

Tập trạng thái ẩn (Hidden States): Đại diện cho các trạng thái không quan sát được của hệ thống. Ma trận xác suất chuyển trạng thái (State Transition Matrix): Xác định xác suất chuyển từ một trạng thái ẩn này sang trạng thái ẩn khác. Ma trận xác suất phát xạ (Emission Probability Matrix): Mô tả xác suất của một quan sát cụ thể dựa trên trạng thái hiện tại. Phân phối xác suất ban đầu (Initial State Distribution): Xác định trạng thái khởi đầu của hệ thống.

# Sự khác biệt giữa Markov Chain và HMM

Markov Chain là một mô hình toán học đơn giản hơn HMM, trong đó:

• Trạng thái của Markov Chain là có thể quan sát trực tiếp. Xác suất chuyển trạng thái chỉ phụ thuộc vào trạng thái hiện tại, không quan tâm đến các trạng thái trước đó.

Ngược lại, HMM phức tạp hơn:

• Trạng thái ẩn của HMM không thể quan sát trực tiếp, mà chỉ có thể suy đoán thông qua các quan sát.   
HMM bổ sung thêm quá trình phát xạ, liên kết các trạng thái ẩn với dữ liệu quan sát.

Ví dụ minh họa: Trong Markov Chain, nếu ta đang xem một chuỗi các điều kiện thời tiết (nắng, mưa), bạn có thể quan sát trực tiếp điều kiện thời tiết tại từng thời điểm. Trong HMM, các điều kiện thời tiết có thể được ẩn (không trực tiếp quan sát được), nhưng ta có thể suy luận từ các quan sát như mức độ ẩm, nhiệt độ, hoặc áp suất không khí.



## Vai trò và ứng dụng của HMM trong các bài toán thực tiễn

HMM đóng vai trò quan trọng trong nhiều lĩnh vực nghiên cứu và ứng dụng, đặc biệt là trong xử lý chuỗi dữ liệu. Một số ứng dụng điển hình của HMM bao gồm:

### Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP):

o Gắn thẻ từ loại (POS Tagging): Dự đoán nhãn ngữ pháp (danh từ, động từ,...) của các từ trong câu.   
o Nhận dạng thực thể (Named Entity Recognition): Xác định tên riêng, địa danh, hoặc tổ chức trong văn bản.

### Nhận dạng giọng nói (Speech Recognition):

o Mô hình hóa các chuỗi âm thanh để chuyển đổi thành văn bản.

### Phân tích sinh học (Bioinformatics):

o Dự đoán cấu trúc protein từ chuỗi axit amin.   
o Phân tích trình tự DNA để xác định gen.

### Phát hiện bất thường (Anomaly Detection):

o Dự đoán lỗi trong hệ thống máy tính hoặc mạng lưới.   
o Phát hiện gian lận trong các giao dịch tài chính.

### Ứng dụng trong thời gian thực:

o Phân tích dữ liệu cảm biến trong hệ thống IoT (Internet of Things). o Dự đoán trạng thái hoạt động trong các hệ thống điều khiển tự động.

công cụ mạnh mẽ trong việc mô hình hóa các quá trình phức tạp mà các trạng thái ẩn không thể quan sát trực tiếp.

## Cấu trúc cơ bản của Hidden Markov Model

2.2.1. Mô hình Markov và trạng thái ẩn



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

## Công thức tổng quát của HMM

Một HMM được định nghĩa bởi các tham ${ \hat { \mathbf { s } } } { \hat { \hat { 0 } } } \ { \hat { \lambda } } { \mathbf { = } } ( { \mathbf { A } } , { \mathbf { B } } , \pi )$ , trong đó:

• $\mathrm { A } = \left[ \mathrm { a } _ { \mathrm { i j } } \right]$ : Ma trận chuyển trạng thái.   
• $\mathbf { B } = [ \mathrm { b } _ { \mathrm { j } } ( \mathrm { k } ) ]$ : Ma trận xác suất phát xạ.   
• $\pi = \{ \pi \} $ : Phân phối xác suất ban đầu.

Cho một chuỗi quan sát $\mathrm { O = \{ O _ { 1 } , O _ { 2 } , . . . , O _ { T } \} }$ với chiều dài T, xác suất của chuỗi quan sát được tính theo công thức:

$$
\begin{array} { r } { P ( O \mid \lambda ) = \sum _ { Q } P ( O , Q \mid \lambda ) = \sum _ { Q } P ( Q \mid \lambda ) \cdot \operatorname { P } \left( 0 \mid Q , \lambda \right) } \end{array}
$$

Trong đó:



• $\mathrm { Q } = \{ \mathrm { S } _ { \mathrm { q 1 } } , \mathrm { S } _ { \mathrm { q 2 } } , . . . , \mathrm { S } _ { \mathrm { q T } } \}$ : Một chuỗi trạng thái ẩn.   
• Tổng $\Sigma _ { \mathrm { Q } }$ được tính trên tất cả các chuỗi trạng thái có thể xảy ra.

Công thức này cho phép ta tính xác suất quan sát của một chuỗi và xác định chuỗi trạng thái ẩn tối ưu.

# Ba bài toán cơ bản của Hidden Markov Model (HMM)

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



• Thuật toán này lặp lại hai bước:

1. E-step (Expectation): Tính xác suất kỳ vọng cho các trạng thái ẩn dựa trên các tham số hiện tại.   
2. M-step (Maximization): Cập nhật các tham số $\mathbf { A } , \mathbf { B } , \pi$ để tối đa hóa xác suất quan sát $\mathrm { P } ( \mathrm { O } | \lambda )$ .

• Thuật toán hội tụ đến một cực đại cục của $\mathrm { P } ( \mathrm { O } | \lambda )$ .

# Public_105 

# Thuật toán liên quan đến Hidden Markov Model (HMM)

Các thuật toán liên quan đến HMM là trung tâm của việc áp dụng mô hình trong các bài toán thực tiễn. Dưới đây là ba thuật toán quan trọng, mỗi thuật toán giải quyết một trong ba bài toán cơ bản của HMM.

1.1. Thuật toán Forward và Backward

1.1.1. Mục đích:

Tính xác suất của một chuỗi quan sát $\mathrm { O } { = } \{ \mathrm { O } _ { 1 } , \mathrm { O } _ { 2 } , . . . , \mathrm { O } _ { \mathrm { T } } \}$ dựa trên một mô hình HMM $\scriptstyle \lambda = ( \operatorname { A } , \operatorname { B } , \pi )$ .

### Thuật toán Forward

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



$$
P ( O \mid \lambda ) = \sum _ { i = 1 } ^ { N } \alpha _ { T } ( i )
$$

• Độ phức tạp: $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ .

### Thuật toán Backward

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



4. Truy vết trạng thái tối ưu:

$$
q _ { t } ^ { * } = \Psi _ { t + 1 } ( q _ { t + 1 } ^ { * } ) , t = T - 1 , T - 2 , \dots , 1
$$

• Độ phức tạp: $\mathrm { O } ( \mathrm { N } ^ { 2 } \mathrm { T } )$ .

# Các giả định của Hidden Markov Model (HMM)

Hidden Markov Model (HMM) dựa trên hai giả định cơ bản, giúp đơn giản hóa việc mô hình hóa và tính toán xác suất trong các bài toán thực tế. Mặc dù những giả định này có thể không hoàn toàn chính xác trong mọi trường hợp, chúng vẫn đủ mạnh để mô tả nhiều hệ thống thực tế một cách hiệu quả.

2.1. Giả định Markov (Markov Assumption)

2.1.1. Định nghĩa:

Giả định Markov phát biểu rằng trạng thái hiện tại qtq_tqt chỉ phụ thuộc vào trạng thái ngay trước đó $\mathbf { q } _ { \mathrm { t } ^ { - 1 } }$ , không phụ thuộc vào các trạng thái trước đó trong chuỗi.

$$
\operatorname { P } ( \operatorname { q } _ { \mathrm { t } } | \mathbf { q } _ { \mathrm { t - 1 } } , \mathbf { q } _ { \mathrm { t - 2 } } , \dots , \mathbf { q } _ { \mathrm { 1 } } ) = \operatorname { P } ( \mathbf { q } _ { \mathrm { t } } \mid \mathbf { q } _ { \mathrm { t - 1 } } )
$$

### Ý nghĩa:

Giả định này giảm độ phức tạp của mô hình, chỉ yêu cầu xét mối quan hệ giữa hai trạng thái liên tiếp thay vì toàn bộ chuỗi trạng thái.

Trong thực tế, giả định Markov có thể hiểu là một hệ thống "có trí nhớ ngắn hạn", nơi trạng thái hiện tại chứa đủ thông tin để dự đoán trạng thái tiếp theo.

### Hạn chế:

Hệ thống thực tế có thể bị ảnh hưởng bởi nhiều trạng thái trong quá khứ, không chỉ bởi trạng thái ngay trước đó. Tuy nhiên, việc tăng bậc của mô hình Markov (Markov bậc cao hơn) có thể giúp giảm bớt hạn chế này, nhưng làm tăng độ phức tạp tính toán.



2.2. Giả định độc lập quan sát (Independence Assumption)

2.2.1. Định nghĩa:

Giả định này cho rằng mỗi quan sát OtO_tOt tại thời điểm ttt chỉ phụ thuộc vào trạng thái hiện tại qtq_tqt, không phụ thuộc vào các quan sát khác hoặc các trạng thái khác trong chuỗi.

$$
\mathrm { P } ( \mathrm { O } _ { \mathrm { t } } \mid \mathrm { q } _ { \mathrm { t } } , \mathrm { q } _ { \mathrm { t } - 1 } , \mathrm { O } _ { \mathrm { t } - 1 } , \dots ) = \mathrm { P } ( \mathrm { O } _ { \mathrm { t } } \mid \mathrm { q } _ { \mathrm { t } } )
$$

### Ý nghĩa:

Giả định này cho phép ta mô hình hóa mối quan hệ giữa trạng thái ẩn và quan sát một cách độc lập, giảm đáng $\mathrm { k } \mathring { \mathrm { e } }$ độ phức tạp khi tính toán xác suất.   
Đây là một trong những lý do HMM được áp dụng rộng rãi trong các bài toán như nhận dạng giọng nói và gắn thẻ từ loại.

2.2.3. Hạn chế:

• Trong thực tế, các quan sát thường có mối liên hệ phụ thuộc với nhau, đặc biệt trong các chuỗi dữ liệu có tính chất tuần tự cao. Giả định này có thể không hoàn toàn chính xác, nhưng thường được chấp nhận để đơn giản hóa mô hình.

Hai giả định Markov và độc lập quan sát là nền tảng của Hidden Markov Model, giúp mô hình này trở thành một công cụ đơn giản nhưng mạnh mẽ để mô tả các chuỗi dữ liệu tuần tự. Mặc dù có những hạn chế nhất định, chúng cho phép HMM áp dụng hiệu quả trong các bài toán thực tế với độ phức tạp tính toán thấp.

3. Ứng dụng của Hidden Markov Model (HMM) vào Gắn thẻ từ loại (POS Tagging)

Gắn thẻ từ loại (Part-of-Speech Tagging - POS Tagging) là một bài toán quan trọng trong xử lý ngôn ngữ tự nhiên (NLP), nhằm gán nhãn ngữ pháp (danh từ, động từ, tính từ,...) cho từng từ trong câu. Hidden Markov Model (HMM) là một phương pháp phổ biến để giải quyết bài toán này nhờ khả năng mô hình hóa chuỗi trạng thái ẩn (các nhãn từ loại) dựa trên chuỗi quan sát (các từ trong câu).



## Mô hình HMM cho POS Tagging

Để áp dụng HMM vào bài toán POS Tagging, chúng ta cần xác định các thành phần của mô hình:

Tập trạng thái ẩn (S): o Là tập các nhãn từ loại (POS tags), ví dụ: $\mathrm { S } { = } \{ \mathrm { N N }$ (danh từ),VB (động từ),JJ (tính từ),… }. Tập quan sát (O):   
o Là tập các từ trong câu, ví dụ: $O = \left\{ \begin{array} { r l } \end{array} \right.$ {The, cat, runs, fast} Phân phối xác suất ban đầu $( \pmb { \pi } )$ :   
o Xác suất một từ trong câu bắt đầu với một từ loại cụ thể: $\pi _ { \mathrm { i } } { = } \mathrm { P } ( \mathrm { S } _ { 1 } { = } \mathrm { i } )$ Ví dụ: Một câu thường bắt đầu bằng các nhãn như DT (mạo từ) hoặc NN (danh từ).   
Ma trận chuyển trạng thái (A):   
o Xác suất chuyển từ nhãn từ loại này sang nhãn từ loại khác: $\mathrm { a _ { i j } { = } P ( S _ { t + 1 } { = } j | S _ { t } { = } i ) }$ Ví dụ: Sau một danh từ (NN), khả năng cao sẽ là một động từ (VB) hoặc mạo từ (DT). Ma trận xác suất phát xạ (B):   
o Xác suất một nhãn từ loại phát sinh một từ cụ thể: $\mathsf { b } _ { \mathrm { j } } ( \mathrm { O } _ { \mathrm { t } } ) { = } \mathsf { P } ( \mathrm { O } _ { \mathrm { t } } | \mathsf { S } _ { \mathrm { t } } { = } \mathrm { j } )$ Ví dụ: Xác suất từ "runs" thuộc nhãn động từ (VB) sẽ cao hơn các nhãn khác.

3.2. Thuật toán Viterbi để giải bài toán POS Tagging



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



$$
\delta _ { 1 } ( V B ) = \pi _ { V B } \cdot b _ { V B } ( " \mathrm { T h e " } ) = 0 . 1 \cdot 0 . 1 = 0 . 0 1
$$

• $\mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { D } \hat { \mathbf { e } }$ quy (tại $\scriptstyle { \mathfrak { t } } = 2$ ):

$$
\begin{array} { r } { \delta _ { 2 } ( N N ) = m a x [ \delta _ { 1 } ( D T ) \cdot a _ { D T  N N } , \delta _ { 1 } ( N N ) \cdot a _ { N N  N N } , \delta _ { 1 } ( V B ) \cdot a _ { V B  N N } ] } \\ { \cdot b _ { N N } ( ^ { \circ } c a t ^ { \prime \prime } ) \qquad } \end{array}
$$

# • Tiếp tục:

Lặp lại các bước trên cho đến $\mathrm { t } { = } 3$ để tìm chuỗi nhãn tối ưu.

# Public_106 

Thuật toán tìm kiếm không có thông tin được xem xét trước tiên là tìm kiếm theo chiều rộng (Breadth-first search, viết tắt là BFS), một dạng tìm kiếm vét cạn.

# Nguyên tắc:

Tìm kiếm theo chiều rộng là trong số những nút biên lựa chọn nút nông nhất (gần nút gốc nhất) để mở rộng. Như vậy, trước hết tất cả các nút có độ sâu bằng 0 (nút gốc) được mở rộng, sau đó tới các nút có độ sâu bằng 1 được mở rộng, rồi tới các nút có độ sâu bằng 2, và tiếp tục như vậy. Ở đây, độ sâu được tính bằng số nút nằm trên đường đi từ nút gốc tới nút đang xét.

Có thể nhận thấy, để thực hiện nguyên tắc tìm kiếm theo chiều rộng, ta cần lựa chọn nút được thêm vào sớm hơn trong danh sách nút biên O để mở rộng. Điều này có thể thực hiện dễ dàng bằng cách dùng một hàng đợi FIFO để lưu các nút biên.

Thuật toán tìm theo chiều rộng được thể hiện trên hình 1. Khác với thuật toán tìm kiếm tổng quát ở trên, tập nút biên O được tổ chức dưới dạng hàng đợi FIFO: các nút mới sinh ra được thêm vào cuối của O tại bước 3 của mỗi vòng lặp; nút đầu tiên của O sẽ được lấy ra để mở rộng như tại bước 1 của vòng lặp của thuật toán trên hình vẽ. Bước 2 của vòng lặp kiểm tra điều kiện đích và trả về kết quả trong trường hợp nút lấy ra từ O là nút đích. Thuật toán kết thúc trong hai trường hợp: 1) khi lấy được nút đích từ O; và 2) khi tập O rỗng. Hai trường hợp này tương ứng với hai lệnh return ở trong và ngoài vòng lặp.

Con trỏ ngược: khi mở rộng một nút ta cần sử dụng con trỏ ngược để ghi lại nút cha của nút vừa được mở ra. Con trỏ này được sử dụng để tìm ngược lại đường đi về trạng thái xuất phát khi tìm được trạng thái đích. Khi cài đặt thuật toán, mỗi nút được biểu diễn bằng một cấu trúc dữ liệu có chứa một con trỏ ngược trỏ tới nút cha.

Sau khi tìm được nút đích, có thể khôi phục đường đi tới nút đó bằng cách lần theo các con trỏ ngược, bắt đầu từ nút đích. 2025-09-2



While (O không rỗng) do

Return: Không có lời giải

Hình 1. Thuật toán tìm kiếm theo chiều rộng

# Các cải tiến:

Một số cải tiến sau đây có thể sử dụng kết hợp với thuật toán tìm theo chiều rộng vừa trình bày.

Tránh xem xét lại các nút đã mở rộng. Việc xem xét lại các nút đã mở rộng có thể dẫn tới vòng lặp. Mặc dù vòng lặp không ảnh hưởng tới khả năng tìm ra lời giải của tìm theo chiều rộng, xong việc có vòng lặp và xem xét lại các nút làm tăng độ phức tạp tính toán do phải khảo sát nhiều nút hơn. Vấn đề này có thể giải quyết bằng cách sử dụng tập đóng tương tự trong thuật toán Graph Search. Một trạng thái đã có mặt trong tập đóng hoặc tập biên sẽ không được thêm vào tập biên nữa. Người đọc có thể tự kiểm tra kết quả của thuật toán trong trường hợp có sử dụng kiểm tra tập đóng và tập biên với trường hợp không kiểm tra bằng cách thực hiện thuật toán với ví dụ trên hình 2.1

Kiểm tra đích trước khi thêm vào tập biên. Trong thuật toán tổng quát, việc kiểm tra điều kiện đích được thực hiện khi nút được lấy ra khỏi O để mở rộng. Thay vào đó, ta có thể kiểm tra trước khi thêm nút vào O. Ưu điểm của cách làm này là giảm bớt số lượng nút cần lưu trong nút biên cũng như số nút được mở rộng. Cụ thể về số lượng nút cần mở rộng khi thực hiện kiểm tra đích trước sẽ được trình bày trong phần tính chất của thuật toán ở bên dưới.



Ví dụ: Xét ví dụ tìm đường đi từ nút S tới nút G trên đồ thị ở hình 2.1 (để đơn giản, ví dụ này sử dụng đồ thị có hướng; quá trình tìm đường đi trên đồ thị vô hướng được thực hiện tương tự, trừ việc từ một nút có thể di chuyển sang nút cha của nút đó)

![](images/image1.jpg)  
Hình 2.1: Ví dụ đồ thị cho bài toán tìm đường đi

Một số bước đầu tiên của thuật toán, có sử dụng việc lưu và kiểm tra tập nút đóng, được thể hiện dưới dạng các cây tìm kiếm như trên hình 2.2. Lưu ý: để thống nhất trong việc trình bày, trong số các nút có vai trò giống nhau, tức là có cùng độ sâu, nút đứng trước trong bảng chữ cái sẽ được mở rộng trước. Quy tắc này không được quy định trong thuật toán và chỉ để tiện cho trình bày.



![](images/image2.jpg)

Hình 2.9. Một số cây tìm kiếm sinh ra khi tìm kiếm theo chiều rộng. Các cây được thể hiện theo thứ tự từ trái sang phải, từ trên xuống dưới. Nút mở rộng tiếp theo được đánh dấu bằng mũi tên

Kết quả thực hiện các bước của thuật toán cũng có thể theo dõi qua thứ tự mở rộng các nút và nội dung danh sách tập nút biên. Dưới đây là minh họa cho thứ tự mở rộng nút và tập biên cho ví dụ trên hình 2.1 (có sử dụng tập nút đóng). Để tiện cho trình bầy, ta sẽ quy định phía bên trái là đầu của hàng đợi O và phía bên phải là cuối của hàng đợi O. Như vậy các nút được thêm vào từ phía bên phải và lấy ra từ bên trái. Con trỏ tới nút cha sẽ được viết dưới dạng chỉ số bên cạnh mỗi nút





khi b và d tăng.

Giả sử rằng, mỗi trạng thái khi được phát triển sẽ sinh ra b trạng thái $\mathrm { k } \dot { \hat { \mathbf { e } } } .$ . Như vậy từ nút gốc sẽ sinh ra b nút với độ sâu 1, các nút này lại sinh ra b2 nút với độ sâu 2, và tiếp tục như vậy. Giả sử nút đích của bài toán nằm ở độ sâu d. Trong trường hợp xấu nhất, nút đích nằm cuối cùng trong số các nút $\dot { \mathbf { O } }$ độ sâu này và do vậy ta cần mở rộng tất cả nút $\dot { \mathbf { O } }$ độ sâu d trước khi tìm ra đích, tức là sinh ra $\mathrm { b d } + 1$ nút $\dot { \mathbf { O } }$ độ sâu $\mathrm { d } + 1$ . Như vậy, tổng số nút cần mở rộng để tìm ra nút đích là (tính cả nút $\mathrm { g } \acute { \mathrm { o c } }$ ):

$$
1 + b + b 2 + . . . + b d + 1 = O ( b d + 1 )
$$

Nếu tiến hành kiểm tra điều kiện đích trước khi thêm vào tập biên như đề cập ở trên, ta sẽ không phải sinh ra các nút $\dot { \mathbf { O } }$ độ sâu $\mathrm { d } + 1$ và do vậy số nút cần sinh ra chỉ c n là O(bd).

• Yêu cầu bộ nhớ: thuật toán cần lưu O $( \mathsf { b d } + \mathsf { l } )$ nút trong tập biên sau khi đã mở rộng tất cả các nút ở độ sâu d. Nếu sử dụng tập các nút đóng thì tập này cần lưu O(bd) nút. Như vậy độ phức tạp bộ nhớ của tìm kiếm rộng là O (bd $+ 1$ ).

Như vậy, ưu điểm của tìm theo chiều rộng là tính đầy đủ và tối ưu nếu giá thành đường đi như nhau. Nhược điểm của thuật toán này là độ phức tạp tính toán lớn và yêu cầu về bộ nhớ lớn. Trong hai nhược điểm sau, độ phức tạp về bộ nhớ lớn là nghiêm trọng hơn do không thể kiếm được máy tính có bộ nhớ đủ lớn để chạy thuật toán, trong khi ta có thể đợi thêm thời gian để chờ thuật toán chạy xong nếu thời gian chạy không quá lâu. Trên thực thế, thuật toán tìm theo chiều rộng chỉ có thể sử dụng cho các bài toán có kích thước rất nhỏ (b và d không quá 10).

# Public_107 

# Giới thiệu:

Trong Machine Learning nói riêng và Toán Tối Ưu nói chung, chúng ta thường xuyên phải tìm giá trị nhỏ nhất (hoặc đôi khi là lớn nhất) của một hàm số nào đó. Ví dụ như các hàm mất mát trong hai bài Linear Regression và K-means Clustering. Nhìn chung, việc tìm global minimum của các hàm mất mát trong Machine Learning là rất phức tạp, thậm chí là bất khả thi. Thay vào đó, người ta thường cố gắng tìm các điểm local minimum, và ở một mức độ nào đó, coi đó là nghiệm cần tìm của bài toán.

Các điểm local minimum là nghiệm của phương trình đạo hàm bằng 0. Nếu bằng một cách nào đó có thể tìm được toàn bộ (hữu hạn) các điểm cực tiểu, ta chỉ cần thay từng điểm local minimum đó vào hàm số rồi tìm điểm làm cho hàm có giá trị nhỏ nhất (đoạn này nghe rất quen thuộc, đúng không?). Tuy nhiên, trong hầu hết các trường hợp, việc giải phương trình đạo hàm bằng 0 là bất khả thi. Nguyên nhân có thể đến từ sự phức tạp của dạng của đạo hàm, từ việc các điểm dữ liệu có số chiều lớn, hoặc từ việc có quá nhiều điểm dữ liệu.

Hướng tiếp cận phổ biến nhất là xuất phát từ một điểm mà chúng ta coi là gần với nghiệm của bài toán, sau đó dùng một phép toán lặp để tiến dần đến điểm cần tìm, tức đến khi đạo hàm gần với 0. Gradient Descent (viết gọn là GD) và các biến thể của nó là một trong những phương pháp được dùng nhiều nhất.

Vì kiến thức về GD khá rộng nên tôi xin phép được chia thành hai phần. Phần 1 này giới thiệu ý tưởng phía sau thuật toán GD và một vài ví dụ đơn giản giúp các bạn làm quen với thuật toán này và vài khái niệm mới. Phần 2 sẽ nói về các phương pháp cải tiến GD và các biến thể của GD trong các bài toán mà số chiều và số điểm dữ liệu lớn. Những bài toán như vậy được gọi là large-scale.

# Gradient Descent cho hàm 1 biến

Quay trở lại hình vẽ ban đầu và một vài quan sát tôi đã nêu. Giả sử xt là điểm ta tìm được sau vòng lặp thứ t. Ta cần tìm một thuật toán để đưa xt về càng gần $^ { \mathbf { X * } }$ càng tốt.

Trong hình đầu tiên, chúng ta lại có thêm hai quan sát nữa:



Nếu đạo hàm của hàm số tại xt: $\mathrm { f } ^ { \prime } ( \mathrm { x t } ) { > } 0$ thì xt nằm về bên phải so với $^ { \mathbf { X * } }$ (và ngược lại). Để điểm tiếp theo xt+1 gần với x∗ hơn, chúng ta cần di chuyển xt về phía bên trái, tức về phía âm. Nói các khác, chúng ta cần di chuyển ngược dấu với đạo hàm:xt+1 $=$ xt+ΔTrong đó $\Delta$ là một đại lượng ngược dấu với đạo hàm $\mathbf { f } ^ { \prime } ( \mathbf { x } \mathbf { t } )$ . xt càng xa $^ { \mathbf { X * } }$ về phía bên phải thì f′(xt) càng lớn hơn 0 (và ngược lại). Vậy, lượng di chuyển $\Delta$ , một cách trực quan nhất, là tỉ lệ thuận với $- \mathrm { f } ^ { \prime } ( \mathrm { x t } )$ .

Hai nhận xét phía trên cho chúng ta một cách cập nhật đơn giản là: $\mathbf { x t } + 1 =$ xt−ηf′(xt)

Trong đó η (đọc là eta) là một số dương được gọi là learning rate (tốc độ học). Dấu trừ thể hiện việc chúng ta phải đi ngược với đạo hàm (Đây cũng chính là lý do phương pháp này được gọi là Gradient Descent - descent nghĩa là đi ngược). Các quan sát đơn giản phía trên, mặc dù không phải đúng cho tất cả các bài toán, là nền tảng cho rất nhiều phương pháp tối ưu nói chung và thuật toán Machine Learning nói riêng.

Ví dụ đơn giản với Python

Xét hàm số f(x)=x2+5sin(x) với đạo hàm $\scriptstyle \mathrm { f ( x ) = } 2 \mathrm { x + } 5 \cos ( \mathrm { x } )$ (một lý do tôi chọn hàm này vì nó không dễ tìm nghiệm của đạo hàm bằng 0 như hàm phía trên). Giả sử bắt đầu từ một điểm x0 nào đó, tại vòng lặp thứ t, chúng ta sẽ cập nhật như sau:xt+1 $=$ xt−η(2xt+5cos(xt))

Như thường lệ, tôi khai báo vài thư viện quen thuộc # To support both python 2 and python 3 from __future__ import division, print_function, unicode_literals

import math import numpy as np import matplotlib.pyplot as plt

Tiếp theo, tôi viết các hàm số :

- grad để tính đạo hàm



cost để tính giá trị của hàm số. Hàm này không sử dụng trong thuật toán nhưng thường được dùng để kiểm tra việc tính đạo hàm của đúng không hoặc để xem giá trị của hàm số có giảm theo mỗi vòng lặp hay không. myGD1 là phần chính thực hiện thuật toán Gradient Desent nêu phía trên. Đầu vào của hàm số này là learning rate và điểm bắt đầu. Thuật toán dừng lại khi đạo hàm có độ lớn đủ nhỏ.

def grad(x):

return 2\*x+ 5\*np.cos(x)

def cost(x):

return $\mathrm { x } ^ { \ast \ast } 2 + 5 ^ { \ast } \mathrm { n p . s i n ( x ) }$ def myGD1(eta, x0):

for it in range(100):

$$
\mathbf { x } \lrcorner \mathrm { n e w } = \mathbf { x } [ - 1 ] - \mathrm { e t a } ^ { * } \mathrm { g r a d } ( \mathbf { x } [ - 1 ] )
$$

if abs(grad(x_new)) < 1e-3:

# break

x.append(x_new)

return (x, it)

Điểm khởi tạo khác nhau

Sau khi có các hàm cần thiết, tôi thử tìm nghiệm với các điểm khởi tạo khác nhau là $\mathrm { x 0 = - 5 }$ và $\mathbf { x 0 = 5 }$ .

(x2, it2) $=$ myGD1(.1, 5)



print('Solution $\mathbf { x l } = \% \mathbf { f } .$ , cost $= \% \mathrm { f } .$ , obtained after $\% \mathrm { d }$ iterations'%(x1[-1], cost(x1[-1]), it1))

print('Solution $\mathbf { x } 2 = \% \mathbf { f } .$ , cost $= \% \mathrm { f } .$ , obtained after $\mathrm { ‰ }$ iterations'%(x2[-1], cost(x2[-1]), it2))

Solution $\mathbf { x } 1 = - 1 . 1 1 0 6 6 7 , \mathbf { c o s t } = - 3 . 2 4 6 3 9 4$ , obtained after 11 iterations

Solution $\mathbf { x } 2 = - 1 . 1 1 0 3 4 1$ , cost $= - 3 . 2 4 6 3 9 4$ , obtained after 29 iterations

Vậy là với các điểm ban đầu khác nhau, thuật toán của chúng ta tìm được nghiệm gần giống nhau, mặc dù với tốc độ hội tụ khác nhau. Dưới đây là hình ảnh minh họa thuật toán GD cho bài toán này (xem tốt trên Desktop ở chế độ full màn hình).



![](images/image1.jpg)

Từ hình minh họa trên ta thấy rằng ở hình bên trái, tương ứng với $\mathrm { x 0 = - 5 }$ , nghiệm hội tụ nhanh hơn, vì điểm ban đầu x0 gần với nghiệm $\mathbf { x } { * } { \approx } - 1$ hơn. Hơn nữa, với $\mathbf { x 0 = 5 }$ ở hình bên phải, đường đi của nghiệm có chứa một khu vực có đạo hàm khá nhỏ gần điểm có hoành độ bằng 2. Điều này khiến cho thuật toán la cà ở đây khá lâu. Khi vượt qua được điểm này thì mọi việc diễn ra rất tốt đẹp.

Learning rate khác nhau



Tốc độ hội tụ của GD không những phụ thuộc vào điểm khởi tạo ban đầu mà còn phụ thuộc vào learning rate. Dưới đây là một ví dụ với cùng điểm khởi tạo $\mathrm { x 0 = - 5 }$ nhưng learning rate khác nhau:

![](images/image2.jpg)

Ta quan sát thấy hai điều:

1. Với learning rate nhỏ $\eta { = } 0 . 0 1$ , tốc độ hội tụ rất chậm. Trong ví dụ này tôi chọn tối đa 100 vòng lặp nên thuật toán dừng lại trước khi tới đích, mặc dù đã rất gần. Trong thực tế, khi việc tính toán trở nên phức tạp, learning rate quá thấp sẽ ảnh hưởng tới tốc độ của thuật toán rất nhiều, thậm chí không bao giờ tới được đích.



2. Với learning rate lớn $\mathfrak { n } { = } 0 . 5$ , thuật toán tiến rất nhanh tới gần đích sau vài vòng lặp. Tuy nhiên, thuật toán không hội tụ được vì bước nhảy quá lớn, khiến nó cứ quẩn quanh ở đích.

Việc lựa chọn learning rate rất quan trọng trong các bài toán thực tế. Việc lựa chọn giá trị này phụ thuộc nhiều vào từng bài toán và phải làm một vài thí nghiệm để chọn ra giá trị tốt nhất. Ngoài ra, tùy vào một số bài toán, GD có thể làm việc hiệu quả hơn bằng cách chọn ra learning rate phù hợp hoặc chọn learning rate khác nhau ở mỗi vòng lặp. Tôi sẽ quay lại vấn đề này ở phần 2.

# Gradient Descent cho hàm nhiều biến

Giả sử ta cần tìm global minimum cho hàm f(θ) trong đó θ (theta) là một vector, thường được dùng để ký hiệu tập hợp các tham số của một mô hình cần tối ưu (trong Linear Regression thì các tham số chính là hệ số w). Đạo hàm của hàm số đó tại một điểm θ bất kỳ được ký hiệu là ∇θf(θ) (hình tam giác ngược đọc là nabla). Tương tự như hàm 1 biến, thuật toán GD cho hàm nhiều biến cũng bắt đầu bằng một điểm dự đoán θ0, sau đó, ở vòng lặp thứ t, quy tắc cập nhật là:

Hoặc viết dưới dạng đơn giản hơn: $\scriptstyle \theta = \theta - \eta \nabla \theta \mathrm { f } ( \theta ) .$ .

Quy tắc cần nhớ: luôn luôn đi ngược hướng với đạo hàm.

Việc tính toán đạo hàm của các hàm nhiều biến là một kỹ năng cần thiết. Một vài đạo hàm đơn giản có thể được tìm thấy ở đây.

Quay lại với bài toán Linear Regression

Trong mục này, chúng ta quay lại với bài toán Linear Regression và thử tối ưu hàm mất mát của nó bằng thuật toán GD.

Hàm mất mát của Linear Regression là:L(w) $\mid =$ 12N||y−¯Xw||22



Chú ý: hàm này có khác một chút so với hàm tôi nêu trong bài Linear Regression. Mẫu số có thêm N là số lượng dữ liệu trong training set. Việc lấy trung bình cộng của lỗi này nhằm giúp tránh trường hợp hàm mất mát và đạo hàm có giá trị là một số rất lớn, ảnh hưởng tới độ chính xác của các phép toán khi thực hiện trên máy tính. Về mặt toán học, nghiệm của hai bài toán là như nhau.

Đạo hàm của hàm mất mát là:∇wL(w) $=$ 1N¯XT(¯Xw−y) (1)

Sau đây là ví dụ trên Python và một vài lưu ý khi lập trình

Load thư viện

# To support both python 2 and python 3 from __future__ import division, print_function, unicode_literals

import numpy as np import matplotlib import matplotlib.pyplot as plt np.random.seed(2)

Tiếp theo, chúng ta tạo 1000 điểm dữ liệu được chọn gần với đường thẳng $\scriptstyle \mathbf { y } = 4 + 3 \mathbf { x }$ , hiển thị chúng và tìm nghiệm theo công thức:

$\mathrm { X = }$ np.random.rand(1000, 1)

$\mathrm { y } = 4 + 3 \ast \mathrm { X } + . 2 ^ { \ast }$ np.random.randn(1000, 1) # noise added # Building Xbar one $=$ np.ones((X.shape[0],1)) Xbar $=$ np.concatenate((one, X), axis $= 1$ )

A $=$ np.dot(Xbar.T, Xbar) b $=$ np.dot(Xbar.T, y)



w_lr $=$ np.dot(np.linalg.pinv(A), b) print('Solution found by formula: $\mathbf { W } = \mathbf { \Psi } ^ { \prime }$ ,w_lr.T)

# Display result

$\mathbf { w } = \mathbf { w } \_ { \mathrm { I r } }$   
w_0 = w[0][0]   
w_1 = w[1][0]   
$\mathbf { \boldsymbol { x } } 0 =$ np.linspace(0, 1, 2, endpoint=True)   
$\mathrm { y 0 = w \_ 0 + w \_ l ^ { * } x 0 }$   
# Draw the fitting line   
plt.plot(X.T, y.T, 'b.') # data   
plt.plot(x0, y0, 'y', linewidth $= 2$ ) # the fitting line   
plt.axis([0, 1, 0, 10])   
plt.show()   
Solution found by formula: $\mathbf { w } = \left[ [ \ 4 . 0 0 3 0 5 2 4 2 \ 2 . 9 9 8 6 2 6 6 5 ] \right]$



![](images/image3.jpg)

Đường thẳng tìm được là đường có màu vàng có phương trình $\mathrm { y } { \approx } 4 { + } 2 . 9 9 8 \mathrm { x }$ . Tiếp theo ta viết đạo hàm và hàm mất mát:

def grad(w):

$$
\mathrm { N = X b a r . s h a p e [ 0 ] }
$$

return 1/N \* Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):

$$
\mathrm { N = X b a r . s h a p e [ 0 ] }
$$

return .5/N\*np.linalg.norm(y - Xbar.dot(w), 2)\*\*2;

Kiểm tra đạo hàm

Việc tính đạo hàm của hàm nhiều biến thông thường khá phức tạp và rất dễ mắc lỗi, nếu chúng ta tính sai đạo hàm thì thuật toán GD không thể chạy đúng được. Trong thực nghiệm, có một cách để kiểm tra liệu đạo hàm tính được có chính xác không. Cách này dựa trên định nghĩa của đạo hàm (cho hàm 1 biến) $\scriptstyle 1 \cdot \mathbf { f } ( \mathbf { x } ) = \operatorname* { l i m } \varepsilon \longrightarrow 0 \mathbf { f } ( \mathbf { x } + \varepsilon ) - \mathbf { f } ( \mathbf { x } ) \varepsilon$

Một cách thường được sử dụng là lấy một giá trị ε rất nhỏ, ví dụ 10−6, và sử dụng công thức:f $' ( \mathrm { x } ) { \approx } \mathrm { f } ( \mathrm { x } + \varepsilon ) { \ - } \mathrm { f } ( \mathrm { x } - \varepsilon ) { \ - } 2 \varepsilon$ (2)



Cách tính này được gọi là numerical gradient.

Câu hỏi: Tại sao công thức xấp xỉ hai phía trên đây lại được sử dụng rộng rãi, sao không sử dụng công thức xấp xỉ đạo hàm bên phải hoặc bên trái?

Có hai các giải thích cho vấn đề này, một bằng hình học, một bằng giải tích.

Giải thích bằng hình học

Quan sát hình dưới đây:

![](images/image4.jpg)

Trong hình, vector màu đỏ là đạo hàm chính xác của hàm số tại điểm có hoành độ bằng x0. Vector màu xanh lam (có vẻ là hơi tím sau khi convert từ .pdf sang .png) thể hiện cách xấp xỉ đạo hàm phía phải. Vector màu xanh lục thể hiện cách xấp xỉ đạo hàm phía trái. Vector màu nâu thể hiện cách xấp xỉ đạo hàm hai phía. Trong ba vector xấp xỉ đó, vector xấp xỉ hai phía màu nâu là gần với vector đỏ nhất nếu xét theo hướng.

Sự khác biệt giữa các cách xấp xỉ còn lớn hơn nữa nếu tại điểm x, hàm số bị bẻ cong mạnh hơn. Khi đó, xấp xỉ trái và phải sẽ khác nhau rất nhiều. Xấp xỉ hai bên sẽ ổn định hơn.

Giải thích bằng giải tích



Chúng ta cùng quay lại một chút với Giải tích I năm thứ nhất đại học: Khai triển Taylor.

Với ε rất nhỏ, ta có hai xấp xỉ sau:

$$
\mathrm { f ( x + \varepsilon ) - f ( x - \varepsilon ) } 2 \varepsilon \mathrm { \sim } \mathrm { f ^ { \prime } ( x ) } \mathrm { + } \mathrm { f ( 3 ) } \mathrm { ( x ) } 6 \varepsilon 2 \mathrm { + } \cdots \mathrm { = } \mathrm { f ^ { \prime } ( x ) } \mathrm { + } \mathrm { O } \mathrm { ( } \varepsilon 2 \mathrm { ) } ( \mathrm { \Omega } 
$$

Từ đó, nếu xấp xỉ đạo hàm bằng công thức (3) (xấp xỉ đạo hàm phải), sai số sẽ là O(ε). Trong khi đó, nếu xấp xỉ đạo hàm bằng công thức (4) (xấp xỉ đạo hàm hai phía), sai số sẽ là O(ε2)≪O(ε) nếu ε nhỏ.

Cả hai cách giải thích trên đây đều cho chúng ta thấy rằng, xấp xỉ đạo hàm hai phía là xấp xỉ tốt hơn.

Với hàm nhiều biến

Với hàm nhiều biến, công thức (2) được áp dụng cho từng biến khi các biến khác cố định. Cách tính này thường cho giá trị khá chính xác. Tuy nhiên, cách này không được sử dụng để tính đạo hàm vì độ phức tạp quá cao so với cách tính trực tiếp. Khi so sánh đạo hàm này với đạo hàm chính xác tính theo công thức, người ta thường giảm số chiều dữ liệu và giảm số điểm dữ liệu để thuận tiện cho tính toán. Một khi đạo hàm tính được rất gần với numerical gradient, chúng ta có thể tự tin rằng đạo hàm tính được là chính xác.

Dưới đây là một đoạn code đơn giản để kiểm tra đạo hàm và có thể áp dụng với một hàm số (của một vector) bất kỳ với cost và grad đã tính ở phía trên.

_# def numerical_grad(w, cost):_

$\mathrm { e p s } = 1 \mathrm { e } { - } 4$ ${ \bf g } =$ np.zeros_like(w) for i in range(len(w)):



w_p = w.copy()   
w_n = w.copy()   
w_p[i] $+ =$ eps   
w_n[i] -= eps   
g[i] = (cost(w_p) - cost(w_n))/(2\*eps)

return g

def check_grad(w, cost, grad):

$\mathbf { W } =$ np.random.rand(w.shape[0], w.shape[1])

grad1 $=$ grad(w)

grad2 $=$ numerical_grad(w, cost)

print( 'Checking gradient...', check_grad(np.random.rand(2, 1), cost, grad))

Checking gradient... True

(Với các hàm số khác, bạn đọc chỉ cần viết lại hàm grad và cost ở phần trên rồi áp dụng đoạn code này để kiểm tra đạo hàm. Nếu hàm số là hàm của một ma trận thì chúng ta thay đổi một chút trong hàm numerical_grad, tôi hy vọng không quá phức tạp).

Với bài toán Linear Regression, cách tính đạo hàm như trong (1) phía trên được coi là đúng vì sai số giữa hai cách tính là rất nhỏ (nhỏ hơn 10−6). Sau khi có được đạo hàm chính xác, chúng ta viết hàm cho GD:

def myGD(w_init, grad, eta):

$$
\mathrm { \mathbf { w } } = \mathrm { [ w \_ i n i t ] }
$$

for it in range(100):



w_new $=$ w[-1] - eta\*grad(w[-1])

if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3:

# break

w.append(w_new)

return (w, it)

w_init $=$ np.array([[2], [1]])

(w1, it1) $=$ myGD(w_init, grad, 1)

print('Solution found by GD: $\mathbf { W } = \mathbf { \Psi } ^ { \prime }$ , w1[-1].T, ',\nafter $\mathrm { ‰ }$ iterations.' $\% ( \mathrm { i t } 1 + 1 )$ )

Solution found by GD: $\mathbf { w } = \left[ [ ~ 4 . 0 1 7 8 0 7 9 3 ~ 2 . 9 7 1 3 3 6 9 3 ] \right] .$ ,

after 49 iterations.

Sau 49 vòng lặp, thuật toán đã hội tụ với một nghiệm khá gần với nghiệm tìm được theo công thức.

Dưới đây là hình động minh họa thuật toán GD.



![](images/image5.jpg)

Trong hình bên trái, các đường thẳng màu đỏ là nghiệm tìm được sau mỗi vòng lặp.

Trong hình bên phải, tôi xin giới thiệu một thuật ngữ mới: đường đồng mức.

Đường đồng mức (level sets)

Với đồ thị của một hàm số với hai biến đầu vào cần được vẽ trong không gian ba chiều, nhều khi chúng ta khó nhìn được nghiệm có khoảng tọa độ bao nhiêu. Trong toán tối ưu, người ta thường dùng một cách vẽ sử dụng khái niệm đường đồng mức (level sets).



Nếu các bạn để ý trong các bản độ tự nhiên, để miêu tả độ cao của các dãy núi, người ta dùng nhiều đường cong kín bao quanh nhau như sau:

Ví dụ về đường đồng mức trong các bản đồ tự nhiên. (Nguồn: Địa lý 6: Đường đồng mức là những đường như thế nào?)

Các vòng nhỏ màu đỏ hơn thể hiện các điểm ở trên cao hơn.



Trong toán tối ưu, người ta cũng dùng phương pháp này để thể hiện các bề mặt trong không gian hai chiều.

Quay trở lại với hình minh họa thuật toán GD cho bài toán Liner Regression bên trên, hình bên phải là hình biểu diễn các level sets. Tức là tại các điểm trên cùng một vòng, hàm mất mát có giá trị như nhau. Trong ví dụ này, tôi hiển thị giá trị của hàm số tại một số vòng. Các vòng màu xanh có giá trị thấp, các vòng tròn màu đỏ phía ngoài có giá trị cao hơn. Điểm này khác một chút so với đường đồng mức trong tự nhiên là các vòng bên trong thường thể hiện một thung lũng hơn là một đỉnh núi (vì chúng ta đang đi tìm giá trị nhỏ nhất).

Tôi thử với learning rate nhỏ hơn, kết quả như sau:

![](images/image6.jpg)

![](images/image7.jpg)

Tốc độ hội tụ đã chậm đi nhiều, thậm chí sau 99 vòng lặp, GD vẫn chưa tới gần được nghiệm tốt nhất. Trong các bài toán thực tế, chúng ta cần nhiều vòng lặp hơn 99 rất nhiều, vì số chiều và số điểm dữ liệu thường là rất lớn.

# Một ví dụ khác



Để kết thúc phần 1 của Gradient Descent, tôi xin nêu thêm một ví dụ khác.

![](images/image8.jpg)

$\scriptstyle { \mathrm { H a m ~ s } } \hat { \hat { 0 } } \ { \mathrm { f ( x , y ) } } = ( { \mathrm { x } } 2 + { \mathrm { y } } - 7 ) 2 + ( { \mathrm { x } } - { \mathrm { y } } + 1 ) 2$ có hai điểm local minimum màu xanh lục tại (2,3) và (−3,−2), và chúng cũng là hai điểm global minimum. Trong ví dụ này, tùy vào điểm khởi tạo mà chúng ta thu được các nghiệm cuối cùng khác nhau.

# Thảo luận

Dựa trên GD, có rất nhiều thuật toán phức tạp và hiệu quả hơn được thiết kế cho những loại bài toán khác nhau. Vì bài này đã đủ dài, tôi xin phép dừng lại ở đây. Mời các bạn đón đọc bài Gradient Descent phần 2 với nhiều kỹ thuật nâng cao hơn.

# Tài liệu tham khảo

1. An overview of gradient descent optimization algorithms   
2. An Interactive Tutorial on Numerical Optimization   
3. Gradient Descent by Andrew NG

# Public_108 

# Giới thiệu

Bài báo này đề xuất phương pháp định vị và tránh vật cản cho robot di động hoạt động trong môi trường đa vật thể dựa trên thuật toán học tăng cường. Mô hình robot di động gồm đầy đủ các thông số hình học và thông số vật lý được xây dựng trên nền tảng phần mềm Gazebo. Các hoạt động huấn luyện cho mô hình để robot tự tìm đường di chuyển được thực hiện cho cả thuật toán QLearning và thuật toán SARSA. Kết quả thử nghiệm được so sánh giữa hai thuật toán để đánh giá hiệu quả và chất lượng của các hoạt động huấn luyện.

# Cơ sở lý thuyết

Phương pháp học tăng cường tập trung vào việc học hướng tới mục tiêu từ sự tương tác khác nhau. Thực thể thực hiện quá trình học tập sẽ không biết trước hành động cần phải thực hiện, thay vào đó phải tự khám phá ra hành động nào mang lại phần thưởng lớn nhất bằng cách kiểm tra các hành động này thông qua phương pháp thử sai. Các thành phần cơ bản trong học tăng cường bao gồm:

- Tác nhân (Agent): đóng vai trò trong việc giải quyết các vấn đề ra quyết định, tác động dưới sự không chắc chắn. Môi trường (Environment): là những gì tồn tại bên ngoài tác nhân, tiếp nhận các tác độc từ tác nhân và tạo ra phần thưởng và những quan sát. Hành động (Actions): tập hợp các phương thức hành động mà tác nhân tác động đến môi trường. Trạng thái (State): trạng thái của tác nhân sau khi tác động qua lại với môi trường. Phần thưởng (Reward): là giá trị thu được tương ứng với mỗi cặp Trạng thái - Hành động của tác nhân nhận được khi thực hiện tương tác với môi trường. Tập (Episode): một chu kỳ bao gồm các tương tác giữa tác nhân và môi trường từ thời điểm bắt đầu đến kết thúc. Chính sách (Policy): là hàm biểu diễn sự tương quan giữa những quan sát thu được từ môi trường và hành động cần thực hiện.

Trong đó, tác nhân và môi trường là hai thành phần cốt lõi của một mô hình học tăng cường. Hai thành phần này tương tác liên tục với nhau theo trình tự: Tác nhân thực hiện các tương tác tới môi trường thông qua các hành động, từ đó môi trường tác động lại các hành động của tác nhân. Môi trường lưu trữ các luồng thông tin khác nhau và phản hồi cho tác nhân một “giá trị khen thưởng” sau mỗi hành động của tác nhân. Giá trị này biểu hiện mức độ hiệu quả từng hành động của tác nhân trong quá trình hoàn thành nhiệm vụ. Mục đích của phương pháp học tăng cường là tác nhân tìm ra được chính sách tối đa hoá giá trị phần thưởng tích luỹ trong thời gian dài. Trong hướng tiếp cận của bài báo, tác giả chỉ ra tính hiệu quả của phương thức triển khai mô hình đề xuất dựa trên hai thuật toán học tăng cường Q-Learning và SARSA.



2.1. Thuật toán Q-Learning

Q-Learning là một thuật toán học tăng cường thực hiện phương thức cập nhật giá trị (values-based) dựa trên cập nhật hàm giá trị từ phương trình Bellman [14]. Phương trình Bellman tính toán giá trị kỳ vọng của trạng thái như sau:

$$
\vee ^ { * } ( \mathsf { s } _ { \mathrm { t } } , \mathsf { a } _ { \mathrm { t } } ) = \mathsf { m a x Q } ^ { \pi } ( \mathsf { s } _ { \mathrm { t } } , \mathsf { a } _ { \mathrm { t } } )
$$

- Trong đó: $\check { \mathsf { V } } ( \mathsf { s } _ { \mathrm { t } } )$ là giá trị tối ưu trả về từ giá trị kỳ vọng theo trạng thái st theo chính sách thực hiện $\pi$ ; maxQπ là giá trị Q lớn nhất thể hiện hành động at tại trạng thái st theo chính sách $\pi$ .

Phương trình tính toán giá trị Q kỳ vọng thực hiện một hành động at tại trạng thái st dựa trên phương trình Bellman:

$$
{ \sf Q } ^ { * } ( \mathsf { s } _ { { \sf t } } , \mathsf { a } _ { { \sf t } } ) = { \sf r } _ { { \sf t } } + \mathsf { v } \mathsf { m } \mathsf { a } \times { \sf Q } ^ { * } ( \mathsf { s } _ { { \sf t } + 1 } , \mathsf { a } )
$$

- Trong đó: $\mathsf { Q } ^ { * } ( \mathsf { s } _ { \mathrm { t } } , \mathsf { a } _ { \mathrm { t } } )$ là giá trị kỳ vọng của phần thưởng mà phương trình hướng đến nhằm tối ưu cho mỗi cặp trạng thái st và hành động at tại thời điểm t; rt là phần thưởng tức thời nhận lại được tại thời điểm t; γlà hằng số chiết khấu xác định mức độ quan trọng được trao cho phần thưởng hiện tại và phần thưởng trong tương lai; là giá trị kỳ vọng lớn nhất có thể xảy ra của Q tại trạng thái $s _ { t + 1 } ,$ với mọi hành động a.

Q-Learning là một thuật toán Off-policy, quá trình học của mô hình chủ yếu dựa trên giá trị của chính sách tối ưu và độc lập với các hành động của chủ thể. Off-policy được định nghĩa là tác nhân tuân theo một chính sách quyết định cho việc lựa chọn hành động để đạt trạng thái $s _ { \mathrm { t } + 1 }$ từ trạng thái st . $\mathrm { K } \mathring { \mathrm { e } }$ từ trạng thái $S _ { t + 1 } ,$ , tác nhân sử dụng một chính sách khác cho khâu quyết định này.



Phương trình của thuật toán Q-Learning được trình bày như sau:

$$
\mathrm { Q } _ { \mathrm { s t , a t } } = \mathrm { Q } _ { \mathrm { s t , a t } } + \mathbf { a } ^ { * } \left[ \mathsf { r } _ { \mathrm { t } } + \mathsf { Y } ^ { * } \operatorname* { m a x } \mathbf { Q } ( \mathsf { s } _ { \mathrm { t } + 1 } , \mathsf { a } ) - \mathsf { Q } _ { \mathrm { s t , a t } } \right]
$$

${ \bf Q } ^ { * } ( { \bf s } , { \bf a } )$ trong (3) là giá trị kỳ vọng (phần thưởng của chiết khấu tích lũy trong việc thực hiện hành động a ở trạng thái s và sau đó tuân theo chính sách tối ưu. Hành động từ mỗi trạng thái thu được của thuật toán Q-Learning được xác định bởi quy trình ra quyết định Markov (MDP) [15, 16]. Các bước triển khai thuật toán được trình bày như trong bảng 1.



Bang 1. Thuat toán cap nhat Q-Learning.   



$$
\mathrm { Q } _ { \mathrm { s t , a t } } = \mathrm { Q } _ { \mathrm { s t , a t } } + \mathsf { a } [ \mathsf { r } _ { \mathrm { t } } + \mathsf { y Q } ( \mathsf { s } _ { \mathrm { t + 1 } } , \mathsf { a } _ { \mathrm { t + 1 } } ) - \mathsf { Q } _ { \mathrm { s t , a t } } ]
$$



Bang 2. Thuat toán càp nhat SARSA   

<table><tr><td>Dàu vào: Tap trang thai S =  {1, 2,. . ., n };</td></tr><tr><td>Khǎi tao các sieu tham sō cúa thuàt toán: a, Y ∈ [0; 1] Phuong thúc:</td></tr><tr><td>Kh∂i tao Q: S × A →→ [ ]ngāu nhien; for giá tri Q chua hoi tu, do:</td></tr><tr><td>Dǎt trang thái st ∈ S ; Thyc hièn hành dòng at ∈ A (dua vào chính sách tǒi uu);</td></tr><tr><td>for s khòng phai là trang thái cuǒi, do: Lua chon hành dòng at+1 ∈ A (dua vào chính sách toi uu);</td></tr><tr><td>Thuc hièn hành dòng at+1i Quan sát trang thái s mói và thu nhàn phǎn thuòng R;</td></tr><tr><td>Cap nhat; Qst,at = Qst,at + a[r + yQ(St+1, at+1) − Qst,at ]</td></tr></table>

# Public_109 

# Tầm quan trọng của việc khai thác thông tin tuần tự trong dữ liệu người dùng

Hệ gợi ý tuần tự là một trong những hướng nghiên cứu quan trọng trong lĩnh vực hệ gợi ý, tập trung vào việc khai thác thông tin từ chuỗi hành vi của người dùng để dự đoán hành động tiếp theo. Khác với các hệ gợi ý truyền thống chỉ dựa trên thông tin tĩnh, như lịch sử tương tác tổng quát hoặc các thuộc tính người dùng, hệ gợi ý tuần tự tận dụng các thay đổi động trong sở thích và hành vi người dùng theo thời gian.

Nhờ sự phát triển của học sâu, các phương pháp hiện đại như GRU4Rec, SASRec và BERT4Rec đã cải thiện đáng kể khả năng khai thác thông tin tuần tự:

GRU4Rec: Giúp mã hóa chuỗi sự kiện tuần tự, nhưng còn hạn chế trong việc xử lý chuỗi dài.

- SASRec: Loại bỏ hạn chế của RNN bằng cách sử dụng self-attention để nắm bắt các mối quan hệ giữa các sự kiện mà không bị giới hạn bởi khoảng cách.

BERT4Rec: Mở rộng SASRec với khả năng khai thác ngữ cảnh hai chiều, tối ưu hóa thông tin từ cả phía trước và phía sau trong chuỗi.

Việc áp dụng các phương pháp này đã mở ra khả năng gợi ý chính xác và hiệu quả hơn, đặc biệt trong các môi trường thực tế như thương mại điện tử, nơi hành vi người dùng thay đổi nhanh chóng và có tính cá nhân hóa cao.



# Cấu trúc GRU

Để xử lý vấn đề gradient biến mất hoặc bùng nổ khi chuỗi trở nên quá dài, các biến thể như GRU (Gated Recurrent Unit) và LSTM (Long Short-Term Memory) đã được giới thiệu. Chúng sử dụng các cổng kiểm soát (gates) để điều chỉnh dòng thông tin trong quá trình lan truyền ngược.

GRU sử dụng hai cổng chính, gồm cổng cập nhật $\left( \mathrm { z _ { t } } \right)$ và cổng xoá bỏ (rt), để kiểm soát dòng thông tin trong quá trình cập nhật trạng thái ẩn. Công thức cập nhật trạng thái trong GRU được định nghĩa như sau:

- Cổng cập nhật:

$$
z _ { t } = \sigma ( W _ { z } \cdot [ h _ { t - 1 } , x _ { t } ] + b _ { z } )
$$

Cổng này xác định tỷ lệ thông tin từ trạng thái cũ $\mathrm { h } _ { \mathrm { t } - 1 }$ cần giữ lại để sử dụng trong trạng thái hiện tại.

- Cổng xóa bỏ:

$$
r _ { t } = \sigma ( W _ { r } \cdot [ h _ { t - 1 } , x _ { t } ] + b _ { r } )
$$

Cổng xoá bỏ kiểm soát mức độ ảnh hưởng của trạng thái trước đó $\mathrm { h } _ { \mathrm { t } - 1 }$ khi tạo trạng thái mới.

- Trạng thái ứng viên:

$$
\tilde { h } _ { t } = t a n h ( W _ { h } \cdot [ r _ { t } \odot h _ { t - 1 } , x _ { t } ] + b _ { h } )
$$

Trạng thái ứng viên $\widetilde { h } _ { t }$ là biểu diễn trung gian, chịu tác động bởi cổng xoá bỏ $r _ { t }$ và thông tin đầu vào $x _ { t }$ .

Trạng thái ẩn cuối cùng:

$$
h _ { t } = z _ { t } \odot h _ { t - 1 } + ( 1 - z _ { t } ) \odot \tilde { h } _ { t }
$$

Trạng thái cuối cùng $h _ { t }$ là sự kết hợp giữa trạng thái trước đó ℎ??−1 (được điều chỉnh bởi $z _ { t }$ ) và trạng thái ứng viên $\widetilde { h } _ { t }$ .



![](images/image1.jpg)

Ở đây:

$\bigcirc$ $x _ { t }$ là đầu vào tại thời điểm $t$ (ví dụ: embedding của sản phẩm).   
$\bigcirc$ $h _ { t - 1 }$ là trạng thái ẩn tại thời điểm trước đó.   
$\bigcirc$ $\sigma$ là hàm sigmoid, còn tanh làm hàm kích hoạt phi tuyến.   
$\bigcirc$ $W _ { z } , W _ { r } , W _ { h }$ là các trọng số cần học.   
$\bigcirc$ $b _ { z } , b _ { r } , b _ { h }$ là bias.

- Dự đoán đầu ra: Dựa trên trạng thái ẩn $h _ { t }$ , GRU dự đoán phần tử tiếp theo trong chuỗi thông qua một lớp softmax:

$$
y _ { t } = s o f t m a x ( W _ { y } \cdot h _ { t } + b _ { y } )
$$

Hàm mất mát thường được sử dụng là cross-entropy giữa phân phối dự đoán yt và nhãn thực $\mathrm { y _ { t } ^ { * } }$ .



# GRU4Rec

Cấu trúc mạng sử dụng trong GRU4Rec được tổ chức theo các tầng sau:

Tầng đầu vào (Input Layer): Nhận chuỗi nhấp chuột của người dùng.

- Tầng nhúng (Embedding Layer): Biểu diễn sản phẩm dưới dạng vector nhúng và có thể áp dụng dropout để giảm overfitting.

Tầng hồi tiếp (Recurrent Layer - GRU): Mô hình hóa thông tin tuần tự dựa trên GRU.

- Tầng fully connected: Hợp nhất thông tin từ trạng thái ẩn của GRU.

- Tầng đầu ra (Output Layer): Có thể sử dụng hàm softmax hoặc linear để dự đoán sản phẩm tiếp theo.

![](images/image2.jpg)

Kiến trúc tổng quát của mạng sử dụng trong GRU4Rec, bao gồm các tầng xử lý từ đầu vào đến đầu ra

# Public_110 

# SASRec

SASRec (Self-Attentive Sequential Recommendation) là một mô hình gợi ý tuần tự dựa trên self-attention, được thiết kế để thay thế các phương pháp truyền thống như Markov Chains (MCs) và Recurrent Neural Networks (RNNs) trong việc dự đoán hành vi người dùng. Không giống như các mô hình RNN có tính tuần tự cao và khó xử lý song song, SASRec sử dụng self-attention để chọn lọc các tương tác quan trọng trong lịch sử người dùng, đồng thời tận dụng sức mạnh tính toán song song của GPU.

Kiến trúc của SASRec

![](images/image1.jpg)

Kiến trúc của SASRec dựa trên mô hình Transformer Decoder, cụ thể là multihead self-attention để học các mối quan hệ giữa các mục trong chuỗi tương tác của người dùng. Mô hình bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ các thành phần chính sau:

1.1. Embedding Layer: o Mỗi mục sản phẩm $v _ { t }$ được ánh xạ thành một vector nhúng $e _ { t }$ . o Một positional embedding được thêm vào để mô hình hóa thứ tự của các mục trong chuỗi.   
1.2. Self-Attention Layer: o Sử dụng scaled dot-product attention để xác định trọng số giữa các mục trong chuỗi: $A t t e n t i o n ( Q , K , V ) \stackrel { \displaystyle C } { = } s o f t m a x \left( \frac { Q K ^ { T } } { \sqrt { d } } \right) V$

Trong đó:

Q, K, V là ma trận truy vấn (query), khóa (key) và giá trị (value) được ánh xạ từ các mục trước đó. ▪ d là kích thước của vector nhúng để chuẩn hóa giá trị attention.

o Mô hình sử dụng masked attention để ngăn chặn việc nhìn thấy tương lai, đảm bảo tính tuần tự trong dự đoán.



1.3. Position-wise Feed-Forward Network (FFN): o Mỗi mục sau khi được xử lý bởi self-attention sẽ đi qua một mạng FeedForward để học biểu diễn tốt hơn.   
1.4. Output layer: o Sử dụng softmax để tính xác suất mục tiếp theo mà người dùng có thể tương tác.

Mô hình SASRec có thể được biểu diễn dưới dạng công thức như sau:

$$
H = M u l t i H e a d S e l f A t t e n t i o n ( E + P )
$$

$$
\widehat { H } = F e e d F o r w a r d ( H )
$$

$$
y _ { t } = s o f t m a x ( W _ { y } \cdot \widehat { H } + b _ { y } )
$$

trong đó:

$\bigcirc$ E là ma trận nhúng của các mục.   
o P là Positional Embedding.   
o H là đầu ra từ self-attention.   
o $\widehat { H }$ là đầu ra từ feed-forward network.

Hình dưới đây minh họa cách SASRec sử dụng self-attention để xử lý chuỗi dữ liệu tuần tự. Các khối màu xanh biểu diễn các lớp Transformer (Trm) thực hiện selfattention, trong khi các khối màu hồng đại diện cho embedding input ban đầu của các mục:

![](images/image2.jpg)

Kiến trúc SASRec, thể hiện cách self-attention kết nối các mục trong chuỗi tuần tự để học biểu diễn gợi ý.

# BERT4Rec

BERT4Rec là một mô hình gợi ý tuần tự dựa trên kiến trúc Transformer, được thiết kế để học biểu diễn ngữ cảnh hai chiều (bidirectional context) nhằm cải thiện độ chính xác trong dự đoán sản phẩm tiếp theo mà người dùng có thể quan tâm. Khác với các mô hình gợi ý tuần tự truyền thống như RNN-based methods và SASRec, BERT4Rec không giới hạn trong việc học thông tin từ quá khứ mà có thể tận dụng toàn bộ chuỗi lịch sử để tạo ra biểu diễn mạnh mẽ hơn.



Các phương pháp trước đó, như SASRec, sử dụng self-attention nhưng vẫn là một mô hình unidirectional, tức là chỉ dựa vào thông tin từ các mục trước đó để dự đoán mục tiếp theo. Trong khi đó, BERT4Rec áp dụng kiến trúc bidirectional Transformer, giúp mô hình hóa hành vi người dùng bằng cách tận dụng cả ngữ cảnh phía trước và phía sau của một mục được quan tâm.

## Kiến trúc của BERT4Rec

BERT4Rec được xây dựng dựa trên stacked bidirectional Transformer layers. Tại mỗi lớp, mô hình liên tục cập nhật biểu diễn của từng vị trí bằng cách trao đổi thông tin giữa tất cả các vị trí trong chuỗi thông qua self-attention mechanism. So với các mô hình RNN truyền thống, phương pháp này giúp BERT4Rec loại bỏ giới hạn của gradient vanishing/exploding trong RNN, cùng với đó tận dụng được toàn bộ lịch sử người dùng, không chỉ dựa vào quá khứ. Phương phá này cũng có thể xử lý song song trên GPU, giúp huấn luyện nhanh hơn.

Mỗi tầng Transformer trong BERT4Rec bao gồm:

1. Multi-Head Self-Attention (MHSA): Cho phép mô hình tập trung vào nhiều khía cạnh khác nhau của dữ liệu tuần tự.   
2. Position-wise Feed-Forward Network (PFFN): Áp dụng các biến đổi phi tuyến lên từng phần tử trong chuỗi.   
3. Layer Normalization & Residual Connections: Giúp cải thiện quá trình tối ưu hóa.

Biểu diễn đầu vào của BERT4Rec bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ :

Item Embedding: Biểu diễn nhúng của sản phẩm. - Positional Embedding: Mô hình hóa vị trí của sản phẩm trong chuỗi.



![](images/image3.jpg)  
input

Segment Embedding (loại bỏ trong BERT4Rec): Khác với BERT trong NLP, BERT4Rec không sử dụng nhúng phân đoạn do chỉ làm việc với một chuỗi tương tác duy nhấtBERT4Rec.

![](images/image4.jpg)

## Mục tiêu Cloze trong BERT4Rec

Một điểm khác biệt quan trọng của BERT4Rec so với các mô hình trước đó là sử dụng Cloze objective, thay vì dự đoán trực tiếp mục tiếp theo như RNN hoặc SASRec. Cụ thể, BERT4Rec ẩn ngẫu nhiên một số mục trong chuỗi đầu vào và huấn luyện mô hình để dự đoán lại chúng. Công thức tối ưu hóa được biểu diễn như sau:



Trong đó:

$\bigcirc$ M là tập hợp các vị trí bị ẩn $\bigcirc$ S là chuỗi tương tác của người dùng $\bigcirc$ θ là tham $\mathrm { s } \acute { \mathrm { o } } \mathrm { m } \hat { \mathrm { o } }$ hình $\bigcirc$ $v _ { t }$ là sản phẩm cần dự đoán.

# Public_111 

Trong các phần trước ta đã làm quen với vấn đề suy diễn xác suất, trong đó cho trước một số bằng chứng $E _ { 1 } , . . . , E _ { n }$ , cần tính xác suất điều kiện $P \left( Q \mid E 1 , . . . , E _ { n } \right)$ để kết luận về câu truy vấn $\boldsymbol { \mathcal { Q } }$ .

Xác suất điều kiện trên có thể tính được nếu biết toàn bộ xác suất đồng thời của các biến ngẫu nhiên. Tuy nhiên, trên thực tế, các bài toán thường có số lượng biến ngẫu nhiên lớn, dẫn tới số lượng xác suất đồng thời tăng theo hàm mũ. Do vậy, liệt kê và sử dụng bảng xác suất đồng thời đầy đủ để suy diễn là không thực tế.

Để khắc phục khó khăn trên, trong phần này ta sẽ xem xét cách sử dụng mạng Bayes như một mô hình biểu diễn xác suất rút gọn và cách thực hiện suy diễn xác suất trên mạng Bayes.

# 1.Khái niệm mạng Bayes

Để tiện cho việc trình bày khái niệm mạng Bayes, xét một ví dụ sau3.

Một người đi làm về và muốn dự đoán xem ở nhà có người không thông qua một số dấu hiệu có thể quan sát được. Cho biết một số dữ kiện sau:

Nếu cả nhà đi vắng thì thường bật đèn ngoài sân. Tuy nhiên, đèn ngoài sân có thể được cả trong một số trường hợp có người ở nhà, ví dụ khi có khách đến chơi. - Nếu cả nhà đi vắng thì thường buộc chó ở sân sau.

Tuy nhiên chó có thể được buộc ở sân sau cả khi có người ở nhà nếu như chó bị đau bụng.

Nếu chó buộc ở ngoài thì có thể nghe tiếng sủa, tuy nhiên có thể nghe tiếng sủa (của chó hàng xóm) cả khi chó không buộc ở ngoài.

Để thực hiện suy diễn xác suất cho bài toán trên, trước tiên cần xây dựng mô hình xác suất. Ta sẽ sử dụng năm biến ngẫu nhiên sau để thể hiện các dữ kiện liên quan tới bài toán.

O: không ai ở nhà   
L: đèn sáng   
D: chó ở ngo   
B: chó bị ốm.   
H: nghe thấy tiếng sủa.   
Việc phân tích bài toán cho thấy: Nếu biết D thì H không phụ thuộc vào O, L, B. Nếu biết B thì D độc lập với O. O và B độc lập với nhau



Tiếp theo, ta xây dựng một đồ thị, trong đó mỗi biến ngẫu nhiên ở trên được biểu diễn bởi một nút như trên hình vẽ dưới đây (hình 4.1). Các nút được nối với nhau bằng những cung có hướng sao cho hai hai nút có quan hệ phụ thuộc được nối bởi một cung và hướng của cung thể hiện chiều tác động của nút gốc tới nút đích. Với đồ thị có hướng, ta có thể xác định quan hệ giữa các nút như sau: nếu tồn tại cung có hướng từ nút A tới nút B thì nút A được gọi là nút cha (mẹ) và nút B là nút con.

![](images/image1.jpg)  
Hình 4.1: Một ví dụ mạng Bayes

Sau khi có đồ thị, ta thêm vào bảng xác suất điều kiện. Bảng xác suất điều kiện thể hiện xác suất của biến khi biết giá trị cụ thể của các biến ở các nút cha mẹ. Trong trường hợp nút không có cha mẹ, xác suất trở thành xác suất tiền nghiệm. Để thuận tiện, bảng xác suất điều kiện được thể hiện ngay trên hình vẽ cùng với đồ thị.

Đồ thị vừa xây dựng cùng với các bảng xác suất điều kiện tạo thành mạng Bayes cho bài toán trong ví dụ trên.

Định nghĩa: Mạng Bayes là một mô hình xác suất bao gồm 2 phần

Phần thứ nhất là một đồ thị có hướng không chứa chu trình, trong đó mỗi nút tương ứng với một biến ngẫu nhiên, các cung thể hiện mối quan hệ phụ thuộc giữa các biến.

Phần thứ hai là các bảng xác suất điều kiện: mỗi nút có một bảng xác suất điều kiện cho biết xác suất các giá trị của biến khi biết giá trị các nút cha mẹ.

Cấu trúc của đồ thị trong mạng Bayes thể hiện mối quan hệ phụ thuộc hoặc độc lập giữa các biến ngẫu nhiên của bài toán. Hai nút được nối với nhau bởi một cung khi giữa hai nút có quan hệ trực tiếp với nhau, trong đó giá trị nút gốc ảnh hưởng tới giá trị nút đích.

Lưu ý rằng trong cấu trúc của mạng Bayes không cho phép có chu trình. Hạn chế này ảnh hưởng tới khả năng mô hình hóa của mạng Bayes trong một số trường hợp tuy nhiên cho phép đơn giản hóa việc xây dựng và suy diễn trên mạng Bayes.



Bảng xác suất điều kiện xác định cụ thể ảnh hưởng của các nút cha mẹ tới giá trị nút con. $\mathring { \mathrm { O } }$ đây ta chỉ xét trường hợp biến ngẫu nhiên có thể nhận giá trị rời rạc và bảng xác suất điều kiện được cho theo tổ hợp giá trị của các nút cha mẹ. Mỗi d ng trong bảng tương ứng với một điều kiện cụ thể, thực chất là một tổ hợp giá trị các nút cha. Ví dụ, trong mạng Bayes của ví dụ trên, d ng thứ nhất trong bảng xác suất của nút D ứng với điều kiện trong đó $\mathrm { O } =$ True và $\boldsymbol { \mathrm { B } } =$ True. Nếu nút không có cha mẹ thì bảng xác suất chỉ gồm một d ng duy nhất như trường hợp với nút O và nút B.

# Tính độc lập xác suất trong mạng Bayes

Mạng Bayes thể hiện hai thông tin chính.

Thứ nhất, đây là biểu diễn rút gọn của toàn bộ xác suất đồng thời. Trong ví dụ trên ta chỉ cần 10 xác suất thay vì $2 ^ { 5 } – 1$ xác suất đồng thời. Tùy theo kích thước và đặc điểm cụ thể của bài toán, hiệu quả của việc rút gọn số lượng xác suất có thể lớn hơn rất nhiều. Chẳng hạn, với mạng $\mathrm { g } \dot { 0 } \mathrm { m } 3 0$ nút nhị phân, mỗi nút có 5 nút cha, ta cần tất cả 960 xác suất điều kiện cho mạng Bayes, trong khi bảng xác suất đồng thời cho 30 biến như vậy phải có $2 ^ { 3 0 } – 1$ , tức là hơn một tỷ dòng.

Thứ hai, mạng Bayes cho thấy sự phụ thuộc hoặc độc lập xác suất có điều kiện giữa các biến. Về thực chất, chính việc độc lập về xác suất dẫn tới khả năng biểu diễn rút gọn các xác suất đồng thời.

Tính độc lập xác suất trong mạng Bayes thể hiện qua tính chất sau.

# Tính chất:

Mỗi nút trên mạng Bayes độc lập có điều kiện với tất cả các nút không phải là hậu duệ của nút đó nếu biết giá trị các nút cha.

Mỗi nút độc lập có điều kiện với tất cả các nút khác trên mạng nếu biết giá trị tất cả nút cha, nút con và nút cha của các nút con.

Ví dụ: Theo mạng Bayes trong ví dụ trên H độc lập với O, L, B nếu biết giá trị của D.

Tính các xác suất đồng thời

Sử dụng tính độc lập xác suất vừa phát biểu ở trên, có thể tính xác suất đồng thời của tất cả các biến. Xét ví dụ sau

Ví dụ: cần tính $P ( H , D , L , \neg O , B )$

Theo công thức chuỗi:

$$
^ { \circ } ( H , D , L , \^ { \neg } O , B ) = P ( H | D , L , \ \neg O , B ) ^ { \ast } P ( D | L , \neg O , B ) ^ { \ast } P ( L | \neg O , B ) ^ { \ast } P ( \neg O | B )
$$

$^ * P ( B )$ Do tính độc lập xác suất (có điều kiện):

$$
P \left( H \mid B , D , \neg O , L \right) = P ( H | D )
$$



do vậy,

$$
\begin{array} { r l } & { \quad P ( H , D , L , \neg O , B ) = P ( H | D , L , \neg O , B ) \ast P ( D | L , \neg O , B ) \ast P ( L | \neg O , B ) \ast P ( \neg O | B , \neg O , B ) } \\ & { \ast P ( B ) = P ( H | \neg O ) \ast P ( D | \neg O , B ) \ast P ( L | \neg O ) \ast P ( \neg O ) \ast P ( B ) } \end{array}
$$

Một cách tổng quát, giả sử mạng có n nút tương ứng với n biến ngẫu nhiên $X _ { 1 }$ , …, $X _ { n }$ của bài toán đang xét. Từ thông tin của mạng, có thể tính mọi xác suất đồng thời của n biến, trong đó mỗi xác suất đồng thời có dạng $P \left( X _ { 1 } = x _ { 1 } \ \wedge \ X _ { 2 } = x _ { 2 } \ \wedge \cdots \wedge \ X _ { n } = x _ { n } \right)$ (id:) hay viết gọn là $P ( x _ { 1 } , . . . , x _ { n } )$ . Xác suất đồng thời được tính theo công thức tổng quát sau:

$$
P ( X _ { 1 } = x _ { 1 } , . . . , X _ { n } = x _ { n } ) = \prod _ { i = 1 } ^ { n } P ( X _ { i } = x _ { i } | c h a _ { - } m e ( X _ { i } ) )
$$

hay viết gọn là

$$
P ( x _ { 1 } , . . . , x _ { n } ) = \prod _ { i = 1 } ^ { n } P ( x _ { i } | c h a _ { - } m e ( X _ { i } ) )
$$

trong đó cha_me $( X _ { i } )$ là giá trị cụ th $\acute { \hat { \mathbf { e } } }$ các nút cha mẹ của nút $X _ { i }$ .

$\mathrm { \Delta \vec { \mathrm { p \acute { e } } } }$ minh họa cho công thức trên, ta sẽ tính xác suất xẩy ra tình huống $\dot { \mathbf { O } }$ nhà có người, chó bị $\mathrm { { \acute { o } m } }$ và được buộc ngoài sân, đồng thời đèn không sáng và nghe tiếng chó sủa. Xác suất tình huống này chính là $P ( B , \neg O , D , \neg L , H )$ và được tính như sau:

$$
P ( B , \neg O , D , \neg L , H ) = P ( B ) \ ^ { * } P ( \neg O ) \ ^ { * } P ( D | \neg O , B ) \ ^ { * } P ( H | D ) \ ^ { * } P ( \neg L | \neg O )
$$

$$
\begin{array} { l } { { = 0 , 3 * 0 , 4 * 0 , 0 5 * 0 , 7 * 0 , 3 } } \\ { { \ } } \\ { { = 0 , 0 0 1 2 6 \ \qquad , \ \circ \mathrm { { 8 } } ^ { \circ } } } \end{array}
$$

Trong một phần trên ta đã thấy rằng nếu có mọi xác suất đồng thời thì có thể thực hiện suy diễn xác suất cho mọi dạng câu truy vấn. Như vậy, với mạng Bayes ta có thể suy diễn bằng cách trước tiên tính ra mọi xác suất đồng thời cần thiết. Tuy nhiên, cách này đòi hỏi tính toán nhiều và vì vậy trên thực tế thường sử dụng một số phương pháp suy diễn khác hiệu quả hơn. Vấn đề này sẽ được nhắc tới trong một phần sau.

# Cách xây dựng mạng Bayes



Để có thể sử dụng, trước tiên cần xây dựng ra mạng Bayes. Quá trình xây dựng mạng Bayes bao gồm việc xác định tất cả các biến ngẫu nhiên liên quan, xác định cấu trúc đồ thị của mạng, và cuối cùng là xác định giá trị cho các bảng xác suất điều kiện. Trong phần này, ta sẽ coi như đã có biến ngẫu nhiên, việc xây dựng mạng chỉ bao gồm xác định cấu trúc và bảng xác suất điều kiện.

Có hai cách tiếp cận chính để xây dựng mạng Bayes.

• Cách thứ nhất do con người (chuyên gia) thực hiện dựa trên hiểu biết của mình về bài toán đang xét. Việc xây dựng mạng được chia thành hai bước: xác định cấu trúc đồ thị và điền giá trị cho bảng xác suất điều kiện.

• Cách thứ hai là tự động xác định cấu trúc và xác suất điều kiện từ dữ liệu. Ở đây, dữ liệu có dạng giá trị các biến ghi nhận được trong quá khứ, ví dụ ta có thể ghi lại tổ hợp cá giá trị của năm biến trong ví dụ trên trong thời gian vài năm. Quá trình xây dựng mạng khi đó bao gồm xác định cấu trúc của đồ thị và bảng xác suất điều kiện sao cho phân bố xác suất do mạng thể hiện phù hợp nhất với tần suất xuất hiện các giá trị trong tập dữ liệu.

Phần này chỉ xem xét cách xây dựng mạng do con người thực hiện và mô tả một quy trình cụ thể cho việc xây dựng mạng.

Các bước xây dựng mạng được thực hiện như trên hình 4.2. Sau khi đã có cấu trúc mạng, chuyên gia sẽ xác định giá trị cho các bảng xác suất điều kiện. Thông thường, việc xác định giá trị xác suất điều kiện khó hơn nhiều so với việc xác định cấu trúc mạng, tức là xác định quan hệ giữa các nút.

B1: Xác định các biến ngẫu nhiên cho phép mô tả miền của bài toán. B2: Sắp xếp các biến theo một thứ tự nào đó. Ví dụ theo thứ tự sau: X1, X2 …   
Xn. B3: For $i = I$ to n do a. Thêm một nút mới $X _ { i }$ vào mạng b. Xác định tập Cha_Mẹ(Xi) là tập nhỏ nhất các nút đã có trước đó sao cho Xi độc lập có điều kiện với tất cả nút còn lại khi biết bố mẹ của Xi. c. Với mỗi nút thuộc tập Cha_Mẹ(Xi). Ta thêm một cạnh có hướng từ nút đó tới   
Xi. d. Xác định bảng xác suất điều kiện cho Xi the các giá trị của bố mẹ hoặc bằng xác suất tiền nghiệm nếu Xi không có bố mẹ.



Để minh họa, xét ví dụ sau. Một người vừa lắp hệ thống báo động chống trộm ở nhà. Hệ thống sẽ phát tiếng động khi có trộm. Tuy nhiên, hệ thống có thể báo động (sai) nếu có chấn động do động đất. Trong trường hợp nghe thấy hệ thống báo động, hai người hàng xóm tên làm Nam và Việt sẽ gọi điện cho chủ nhà. Do nhiều nguyên nhân khác nhau, Nam và Việt có thể thông báo sai, chẳng hạn do ồn nên không nghe thấy chuông báo động hoặc ngược lại, nhầm âm thanh khác là tiếng chuông.

Theo phương pháp trên, các bước xây dựng mạng được thực hiện như sau.

B1: lựa chọn biến: sử dụng 5 biến sau T (có trộm), Đ (động đất), B (chuông báo động), N (Nam gọi điện), V (Việt gọi điện)   
B2: các biến được sắp xếp theo thứ tự T, Đ, B, N, V B3: thực hiện như các bước ở hình vẽ, ta xây dựng được mạng thể hiện trên hình sau (để đơn giản, trên hình vẽ chỉ thể hiện cấu trúc và không có bảng xác suất điều kiện).

![](images/image2.jpg)  
Hình 3.2.: Kết quả xây dựng mạng Bayes cho ví dụ chuông báo trộm

# Ảnh hướng của việc sắp xếp các nút tới kết quả xây dựng mạng.

Trên thực tế, việc xây dựng mạng Bayes không đơn giản, đặc biệt trong việc chọn thứ tự các nút đúng để từ đây chọn được tập nút cha có kích thước nhỏ. Để làm rõ điểm này, ta giả sử trong ví dụ trên, các biến được xếp theo thứ tự khác: N, V, C, T, Đ.

Các bước thêm nút sẽ thực hiện như sau:

- Thêm nút N: không có nút cha - Thêm nút V: nếu Nam gọi điện, xác suất Việt gọi điện sẽ tăng lên do sự kiện Nam gọi điện nhiều khả năng do có báo động và do vậy xác suất Việt nghe thấy chuông và gọi điện tăng theo. Do vậy N có ảnh hướng tới V và được thêm vào tập cha của V.



- Thêm C: Nếu Nam và Việt cùng gọi thì khả năng có chuông cao hơn, do vậy cần thêm cả N và V vào tập cha của C.

- Thêm T: Nếu đã biết trạng thái của chuông thì không cần quan tâm tới Nam và Việt nữa, do vậy chỉ có C là cha của T.

- Thêm Đ: nếu có chuông, khả năng động đất tăng lên. Tuy nhiên, nếu đồng thời ta biết có trộm thì việc có trộm giải thích phần nào nguyên nhân chuông kêu. Như vậy, cả chuông và có trộm ảnh hướng tới xác suất động đất, tức là C và T đều là cha của Đ.

Kết quả của mạng Bayes xây dựng theo thứ tự mới được thể hiện trên hình dưới. So sánh với kết quả ở trên, mạng Bayes mới phức tạp hơn, theo nghĩa có nhiều cung hơn hay trung bình các nút có nhiều nút cha hơn. Ngoài ra, ý nghĩa một số quan hệ trên mạng rất không trực quan và khó giải thích, chẳng hạn việc xác suất động đất phục thuộc vào chuông báo động và có trộm. Như vậy, mặc dù cả hai mạng Bayes xây dựng ở trên đều đúng theo nghĩa đảm bảo các ràng buộc về xác suất và đều cho phép tính ra các xác suất đồng thời, việc lựa chọn không đúng thứ tự nút sẽ làm mạng khó hiểu và phức tạp hơn.

![](images/image3.jpg)  
Hình 3.3: Kết quả xây dựng mạng Bayes khi sử dụng thứ tự các nút khác

Từ ví dụ trên ta có thể đưa ra một số nhận xét về kết quả xây dựng mạng Bayes.

# Nhận xét:

Cùng một tập hợp biến có thể xây dựng nhiều mạng Bayes khác nhau. - Thứ tự sắp xếp có ảnh hưởng tới mạng Bayes. Nêđóng vai tr nguyên nhân đứng trước nút hệ quả.- Tất cả các mạng được xây dựng như trên đều hợ phạm các ràng buộc về xác suất và đều cho phép thực hiện suy diễn.

4. Tính độc lập xác suất tổng quát: khái niệm d-phân cách



Trong phần trước, ta đã xem xét khả năng biểu diễn tính độc lập xác suất của mạng Bayes, ví dụ, $\mathrm { m } \tilde { \hat { \mathrm { { o } i } } } x$ nút độc lập với các nút không phải hậu duệ nếu biết giá trị tất cả nút cha của $x$ . Tuy nhiên, đây mới là các trường hợp riêng, trong trường hợp tổng quát cần có khả năng xác định liệu một tập hợp các nút X có độc lập với tập hợp các nút Y khi biết các nút $E$ không. Các tính chất độc lập xác suất đã trình bầy trong phần trước không cho phép trả lời tất cả các câu hỏi tổng quát dạng này. Chẳng hạn, trong ví dụ mạng Bayes trên hình 4.1 dưới đây, nếu không biết giá trị của nút C thì theo tính chất của mạng Bayes, N và V độc lập (không điều kiện) với nhau do V không phải hậu duệ của N và N không có cha. Tuy nhiên, nếu đã biết giá trị của C thì N và V còn độc lập với nhau không? Hai tính chất trình bày trong phần trước không cho phép trả lời câu hỏi này.

![](images/image4.jpg)  
Hình 4.1. Ví dụ mạng Bayes

Trong phần này, ta sẽ xem xét cách trả lời câu hỏi về tính độc lập của tập các nút X với tập nút Y khi biết tập nút E trên một mạng Bayes bằng cách sử dụng khái niệm d-phân cách $d \cdot$ -separation).

Nguyên lý chung của $d \mathbf { \cdot }$ -phân cách là gắn khái niệm phụ thuộc xác suất với tính kết nối (tức là có đường đi giữa các nút), và khái niệm độc lập xác suất với tính không kết nối, hay chia cắt, trên đồ thị có hướng khi ta biết giá trị một số nút $E$ . Chữ $^ { 6 6 } d ^ { 3 9 } \mathrm { ~ \overset { ? } { \mathbf { \alpha } } ~ }$ đây là viết tắt của từ “directional” tức là “có hướng”. Theo đó, các nút $X$ và các nút Y là $d$ -kết nối với nhau nếu chúng không bị $d$ -phân cách. Nếu các nút X và các nút Y bị dphân cách bởi các nút $E$ thì $X$ và Y là độc lập xác suất với nhau khi biết $E$ .

Để xác định tính $d \mathbf { \cdot }$ -phân cách của tập X và Y, trước tiên ta cần xác định tính $d \mathbf { \cdot }$ - phân cách giữa hai nút đơn $x$ thuộc $X$ và $y$ thuộc Y. Từ đây, hai tập nút sẽ độc lập với nhau nếu mỗi nút trong tập này độc lập với tất cả các nút trong tập kia. Sau đây là các quy tắc cho phép xác định tính $d \mathbf { \cdot }$ -phân cách hay tính độc lập xác suất của hai biến $x$ và y.

Quy tắc 1: nút $x$ và $y$ được gọi là $d \mathbf { \cdot }$ -kết nối nếu tồn tại đường đi không bị phong tỏa giữa hai nút. Ngược lại, nếu không tồn tại đường đi như vậy thì $x$ và $y$ là $d$ -phân cách.



Trong quy tắc này, đường đi là một chuỗi các cung nằm liền nhau, không tính tới hướng của các cung đó. Đường đi không bị phong tỏa là đường đi mà trên đó không có hai cung liền $\mathrm { k } \dot { \hat { \mathbf { e } } }$ hướng vào nhau. Trong trường hợp tồn tại hai cung như vậy thì thông tin sẽ không thể đi qua được và do vậy các nút không thể kết nối với nhau. Nút có hai cung hướng vào như vậy gọi là nút xung đột.

Ví dụ, trong trường hợp sau:

$$
x { \longrightarrow } r { \longrightarrow } s { \longrightarrow } t { \longmapsto } u { \longrightarrow } v { \longrightarrow } y
$$

giữa $x$ và $y$ tồn tại đường đi $x \mathrm { ~ - ~ } r \mathrm { ~ - ~ } s \mathrm { ~ - ~ } t \mathrm { ~ - ~ } u \mathrm { ~ - ~ } \nu \mathrm { ~ - ~ } y ;$ , tuy nhiên $t$ là nút xung đột do hai cung $^ { s t }$ và ut hướng vào nhau. Đường đi $x - r - s - t$ và $t - u - \nu - y$ là các đường đi không bị phong tỏa, do vậy $x$ và $t$ là d-kết nối, $t$ và $y$ cũng vậy. Tuy vậy, $x$ và $y$ không phải là $d$ -kết nối do không tồn tại đường đi nào không qua nút xung đột $t .$ Như vậy, x và $y$ là $d \mathbf { \cdot }$ -phân cách trên mạng này và do vậy độc lập xác suất (không điều kiện) với nhau.

Tính kết nối và phân cách xác định theo quy tắc 1 là không điều kiện và do vậy tính độc lập xác suất được xác định theo quy tắc 1 là độc lập không điều kiện.

Quy tắc 2: nút $x$ và y là $d \mathbf { \cdot }$ -kết nối có điều kiện khi biết tập nút $E$ nếu tồn tại đường đi không bị phong tỏa (không chứa nút xung đột) và không đi qua bất cứ nút nào thuộc E. Ngược lại, nếu không tồn tại đường đi như vậy thì ta nói rằng $x$ và $y$ là $d$ -phân cách bởi E. Nói cách khác, mọi đường đi giữa $x$ và $y$ (nếu có) đều bị $E$ phong tỏa.

Quy tắc 2 là cần thiết do khi ta biết giá trị một số nút (tập nút $E$ ), tính chất độc lập hay phụ thuộc giữa các nút c n lại có thể thay đổi: một số nút độc lập trở nên phụ thuộc, và ngược lại, một ss nút phụ thuộc trở thành độc lập. Tính độc lập hay phụ thuộc trong trường hợp này được gọi là $d \mathbf { \cdot }$ -phân cách có điều kiện theo tập biến $E$ .

Ví dụ: trên hình sau, giả sử tập $E { \mathrm { g } } { \dot { \hat { \mathbf { o } } } } { \mathrm { m } } $ hai nút $r$ và $\nu$ được khoanh tr n. Theo quy tắc 2, không tồn tại đường đi không bị phong tỏa nào giữa $x$ và $y$ mà không đi qua $E$ , do đó $x$ và $y$ là $d \mathbf { \cdot }$ -phân cách khi biết $E$ . Tương tự như vậy: $x$ và $s$ , $u$ và $y$ , $s$ và $u$ là $d \mathbf { \cdot }$ -phân cách khi biết $E$ do đường đi $s  r - t$ đi qua nút $r$ thuộc $E$ , đường đi $y - \nu - s$ đi qua nút $\nu$ thuộc $E$ , c n đường đi $s ^ { \scriptscriptstyle - } t ^ { \scriptscriptstyle - } u$ là đường đi bị phong tỏa tại nút xung đột $t$ theo quy tắc 1. Chỉ có các cặp nút $s \operatorname { v a } t$ , $t$ và $u$ là không bị phong tỏa bởi $E$ .

$$
x - \textcircled { r } \cdots - s - 1 \longleftarrow u - \textcircled { 2 } - y
$$

Quy tắc 3: nếu một nút xung đột là thành viên của tập $E$ , hoặc có hậu duệ thuộc tập $E _ { \mathrm { { ; } } }$ , thì nút đó không c n phong tỏa các đường đi qua nó nữa.

Quy tắc này được sử dụng cho trường hợp ta biết một sự kiện được gây ra bởi hai hay nhiều nguyên nhân. Khi ta đã biết một nguyên nhân là đúng thì xác suất những nguyên nhân c n lại giảm đi, và ngược lại nếu ta biết một nguyên nhân là sai thì xác suất những nguyên nhân c n lại tăng lên. Chẳng hạn, xẩy ra tai nạn máy bay với hai nguyên nhân là trục trặc kỹ thuật hoặc lỗi của con người. Nếu ta đã xác định được xẩy ra trục trặc kỹ thuật thì xác suất lỗi con người sẽ bị giảm đi (mặc dù không loại trừ hoàn toàn).



Ví dụ: trên ví dụ ở hình sau, giả sử tập E gồm các nút r và p được đánh dấu bằng cách khoanh tr n. Theo quy tắc 3, nút s và y là d-kết nối do nút xung đột t có hậu duệ là nút p thuộc E, do vậy đã giải tỏa đường đi $\mathbf { s } - \mathbf { t } - \mathbf { u } - \mathbf { v } - \mathbf { y }$ . Trong khi đó x và u vẫn là d-phân cách do mặc dù t đã được giải tỏa nhưng nút r vẫn bị phong tỏa theo quy tắc 2.

![](images/image5.jpg)

# Public_112 

# PHÂN LOẠI BAYES ĐƠN GIẢN

Phần này sẽ đề cập tới phân loại Bayes đơn giản (Naïve Bayes), một phương pháp phân loại đơn giản nhưng có nhiều ứng dụng trong thực tế như phân loại văn bản, dự đoán sắc thái văn bản, lọc thư rác, chẩn đoán y tế. Phân loại Bayes đơn giản là trường hợp riêng của kỹ thuật học máy Bayes, trong đó các giả thiết về độc lập xác suất được sử dụng để đơn giản hóa việc tính xác suất.

# Phương pháp phân loại Bayes đơn giản

Tương tự như học cây quyết định ở trên, phân loại Bayes đơn giản sử dụng trong trường hợp mỗi ví dụ được cho bằng tập các thuộc tính $< x _ { 1 } , x _ { 2 } , . . . , x _ { n } >$ và cần xác định nhãn phân loại y, y có thể nhận giá trị từ một tập nhãn hữu hạn $C$ .

Trong giai đoạn huấn luyện, dữ liệu huấn luyện được cung cấp dưới dạng các mẫu $< _ { \mathbf { X } i } , y _ { i } >$ . Sau khi huấn luyện xong, bộ phân loại cần dự đoán nhãn cho mẫu mới $\mathbf { X }$ .

Theo lý thuyết học Bayes, nhãn phân loại được xác định bằng cách tính xác suất điều kiện của nhãn khi quan sát thấy tổ hợp giá trị thuộc tính $< x _ { 1 } , x _ { 2 } , . . . , x _ { n } >$ . Thuộc tính được chọn, ký hiệu cMAP là thuộc tính có xác suất điều kiện cao nhất (MAP là viết tắt của maximum a posterior), tức là:

$$
y = c _ { _ { M A P } } = \underset { _ { c _ { j } \in C } } { \arg \operatorname* { m a x } } P ( c _ { _ j } \mid x _ { _ 1 } , x _ { _ 2 } , . . . , x _ { _ n } )
$$

Sử dụng quy tắc Bayes, biểu thức trên được viết lại như sau

$$
c _ { \scriptscriptstyle M A P } = \underset { c _ { j } \in C } { \arg \operatorname* { m a x } } \frac { P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \mid c _ { j } ) P ( c _ { j } ) } { P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } ) }
$$

Trong $\mathbf { v } \acute { \mathbf { e } }$ phải của biểu thức này, mẫu số không phụ thuộc vào $c _ { j }$ và vì vậy không ảnh hưởng tới giá trị của $C _ { M A P }$ . Do đó, ta có thể bỏ mẫu số và viết lại như sau:

$$
C _ { M P } = \underset { c _ { j } \in C } { \operatorname { a r g m a x } } P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } | c _ { j } ) P ( c _ { j } )
$$

Hai thành phần trong biểu thức trên được tính từ dữ liệu huấn luyện. Giá trị $P ( c _ { j } )$ được tính bằng tần suất quan sát thấy nhãn $c _ { j } \operatorname { t r e n }$ tập huấn luyện, tức là bằng số mẫu có nhãn là $c _ { j }$ chia cho tổng số mẫu. Việc tính $P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \mid c _ { j } )$ khó khăn hơn nhiều. Vấn đề là số tổ hợp giá trị của $n$ thuộc tính cùng với nhãn phân loại là rất lớn khi n lớn. Để tính xác suất này được chính xác, mỗi tổ hợp giá trị thuộc tính phải xuất hiện cùng nhãn phân loại đủ nhiều, trong khi số mẫu huấn luyện thường không đủ lớn.

Để giải quyết vấn đề trên, ta giả sử các thuộc tính là độc lập về xác suất với nhau khi biết nhãn phân loại $c _ { j }$ . Trên thực tế, các thuộc tính thường không độc lập với nhau như vậy, chẳng hạn đối với ví dụ chơi tennis, khi trời nắng thì xác suất nhiệt độ cao cũng lớn hơn. Chính vì dựa trên giả thiết độc lập xác suất đơn giản như vậy nên phương pháp có tên gọi “Bayes đơn giản”. Tuy nhiên, như ta thấy sau đây, giả thiết như vậy cho phép tính xác suất điều kiện đơn giản hơn nhiều và trên thực tế phân loại Bayes có độ chính xác tốt trong rất nhiều ứng dụng.



Với giả thiết về tính độc lập xác suất có điều kiện, có thể viết:

$$
P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \mid c _ { j } ) = P ( x _ { 1 } \mid c _ { j } ) P ( x _ { 2 } \mid c _ { j } ) \dots P ( x _ { n } \mid c _ { j } )
$$

tức là xác suất đồng thời quan sát thấy các thuộc tính bằng tích xác suất điều kiện của tứng thuộc tính riêng lẻ. Thay vào biểu thức $\dot { \mathbf { O } }$ trên, ta được bộ phân loại Bayes đơn giản (có đầu ra ký hiệu là $c _ { N B } \mathrm { i }$ ) như sau.

$$
\begin{array} { c } { c _ { N B } = \operatorname * { a r g m a x } P ( c _ { j } ) \prod P ( x _ { i } \mid c _ { j } ) } \\ { c _ { j } \in C \qquad i } \end{array}
$$

trong đó, $P ( x _ { i } \mid c _ { j } )$ được tính từ dữ liệu huấn luyện bằng số lần $x _ { i }$ xuất hiện cùng với $c _ { j }$ chia cho số lần $c _ { j }$ xuất hiện. Việc tính xác suất này đòi hỏi ít dữ liệu hơn nhiều so với tính $P ( x _ { 1 } , x _ { 2 } , . . . , x _ { n } \mid c _ { j } )$ .

Trên hình 1 là biểu diễn $\mathrm { m } \hat { \mathrm { o } }$ hình phân loại Bayes đơn giản dưới dạng mạng Bayes. Các thuộc tính không được nối với nhau bởi các cạnh và do vậy các thuộc tính độc lập xác suất với nhau nếu biết giá trị của nhãn phân loại.

![](images/image1.jpg)  
Hình 1: Mô hình Bayes đơn giản: các thuộc tính Xi độc lập xác suất với nhau nếu biết giá trị nhãn phân loại Y.

# Huấn luyện.

Quá trình huấn luyện hay học Bayes đơn giản là quá trình tính các xác suất $P ( c _ { j } )$ và các xác suất điều kiện $P ( x _ { i } \mid c _ { j } )$ bằng cách đếm trên tập dữ liệu huấn luyện. Như vậy, khác với học cây quyết định, Học Bayes đơn giản không đòi hỏi tìm kiếm trong không gian các bộ phân loại. Các xác suất $P ( c _ { j } )$ và các xác suất điều kiện $P ( x _ { i } \mid c _ { j } )$ được tính trên tập dữ liệu huấn luyện theo công thức sau:



Ví dụ.

Để minh họa cho kỹ thuật học Bayes đơn giản, ta sử dụng lại bài toán phân chia ngày thành phù hợp hay không phù hợp cho việc chơi tennis theo điều kiện thời tiết đã được sử dụng trong phần học cây quyết định với dữ liệu huấn luyện cho trong bảng 4.1. Giả sử phải xác định nhãn phân loại cho ví dụ sau:

$< \mathrm { T r } \dot { \bf \mathrm { o r i } } =$ nắng, Nhiệt $\hat { \mathrm { d } } \hat { \mathrm { o } } =$ trung bình, $\mathrm { D } \hat { 0 } \hat { \hat { \mathrm { a } } } \mathrm { m } = \mathrm { c } \mathrm { a } 0$ , $\mathrm { G i } \dot { 0 } = \mathrm { m a n h } >$ Thay số liệu của bài toán vào công thức Bayes đơn giản, ta có: $\begin{array} { r l } & { \qquad c _ { N B } = \underset { c j \in C } { \operatorname { a r g m a x } } P ( c _ { j } ) ~ \Pi ~ P ( x _ { i } | ~ c _ { j } ) } \\ & { \qquad \quad i } \\ & { = \underset {  \vphantom { \operatorname { a r g m a x } }  } { \operatorname { a r g m a x } } } \\ & {  ( \vphantom { \operatorname { a r g m a x } }   } \\ & {   P ( \mathrm { T r o i } \mathord { \operatorname { i \alpha } } \mathrm { \ n a n g } | ~ c _ { j } ) P ( \mathrm { N h . ~ d \hat { o } } \mathrm { - t . ~ b i n h } | ~ c _ { j } ) P ( \mathrm { b \hat { o } } ~ \hat { a } \mathrm { m } \mathrm { = c a o } | ~ c _ { j } ) \ P ( \mathrm { G i } \mathrm { \acute { o } } \mathrm { - m a n h } | ~ c _ { j } ) P ( c _ { j } )  } \end{array}$

Do $c _ { j }$ có thể nhận hai giá trị, ta cần tính 10 xác suất. Các xác suất $P ( \mathrm { c o } )$ và $P ( \mathrm { k h } \hat { \mathrm { o n g } } )$ được tính bằng tất suất “có” và “không” trên dữ liệu huấn luyện.

$$
\begin{array} { l } { { P ( \mathrm { c } \acute { 0 } ) } } \\ { { P ( \mathrm { k h } \acute { 0 } \mathrm { n g } ) = 5 / 1 4 = 0 , 3 6 } } \end{array}
$$

Các xác suất điều kiện cũng được tính từ dữ liệu huấn luyện, ví dụ ta có:

$$
\begin{array} { l } { { P ( \mathrm { b } \hat { \rho } \hat { \mathrm { \ a m } } = \mathrm { c a o } | \mathrm { c } \hat { \rho } ) } } \\ { { P \left( \mathrm { b } \hat { \rho } \hat { \mathrm { a } } \mathrm { m } = \mathrm { c a o } | \mathrm { k h } \hat { \mathrm { o } } \mathrm { n g } \right) = 4 / 5 = 0 , 8 } } \end{array}
$$

$$
\begin{array} { r l r } { \mathrm { ~  ~ \psi ~ } = } & { { } ~ 3 / 9 } & { \mathrm { ~  ~ \psi ~ } = } & { 0 , 3 3 } \end{array}
$$

Thay các xác suất thành phần vào công thức Bayes đơn giản, ta được:

$$
\begin{array} { r l } & { \mathrm { n } \dot { \mathrm { \tilde { a } n g } } | \mathrm { c \tilde { o } } ) P ( \mathrm { t r u n g ~ b i n h } | \mathrm { c \tilde { o } } ) P ( \mathrm { c a o } | \mathrm { c \tilde { o } o } ) P ( \mathrm { m a n h } | \mathrm { c \tilde { o } } ) = 0 . 0 0 5 3 } \\ & { \mathrm { ) } P ( \mathrm { n } \dot { \mathrm { \tilde { a } n g } } | \mathrm { k h \hat { o } n g } ) P ( \mathrm { t r u n g ~ b i n h } | \mathrm { k h \hat { o } n g } ) P ( \mathrm { c a o } | \mathrm { k h \hat { o } n g } ) P ( \mathrm { m a n h } | \mathrm { k h \hat { o } n g } ) = 0 . 0 2 0 6 } \end{array}
$$

Như vậy, theo phân loại Bayes đơn giản, ví dụ đang xét sẽ được phân loại là “không”. Cần chú ý rằng, 0.0053 và 0.0206 không phải là xác suất thực của nhãn “có”



và “không”. Để tính xác suất thực, ta cần chuẩn hóa để tổng hai xác suất bằng 1. Việc chuẩn hoá được thực hiện bằng cách chia mỗi số cho tổng của hai số. Chẳng hạn xác suất có chơi sẽ bằng 0.0053/ $( 0 . 0 0 5 3 + 0 . 0 2 0 6 ) = 0 . 2 0 5 $

# Vấn đề tính xác suất trên thực tế

Phân loại Bayes đơn giản đòi hỏi tính các xác suất điều kiện thành phần $P ( x _ { i } \mid c _ { j } )$ . Xác suất này được tính bằng $n _ { c } / n$ , trong đó $n _ { c }$ số lần $x _ { i }$ và $c _ { j }$ xuất hiện đồng thời trong tập huấn luyện và n là số lần $c _ { j }$ xuất hiện.

Trong nhiều trường hợp, giá trị $n _ { c }$ có thể rất nhỏ, thậm chí bằng không, và do vậy ảnh hưởng tới độ chính xác khi tính xác suất điều kiện. Nếu $n _ { c } = 0$ , xác suất điều kiện cuối cùng sẽ bằng không, bất $\mathrm { k } \mathring { \mathrm { e } }$ các xác suất thành phần khác có giá trị thế nào.

Để khắc phục vấn đề này, một kỹ thuật được gọi là làm trơn thường được sử dụng. Kỹ thuật làm trơn đơn giản nhất sử dụng công thức tính $P ( x _ { i } \mid c _ { j } )$ như sau:

$$
\begin{array} { r } { P ( x _ { i } \mid c _ { j } ) = ( n _ { c } + 1 ) ~ / \left( n + 1 \right) } \end{array}
$$

Như vậy, $\mathrm { k } \mathring { \mathrm { e } }$ cả khi $n _ { c } = 0$ , xác suất vẫn nhận giá trị khác 0.

Trong trường hợp chung, có thể sử dụng công thức được làm trơn sau:

$$
\begin{array} { r l } { P ( x _ { i } \mid c _ { j } ) = { } } & { { } { \cfrac { n c + m p } { n + m p } } } \end{array}
$$

trong đó $p$ là xác suất tiền nghiệm của $x _ { i }$ và $m$ là tham $\mathrm { s } \acute { \mathrm { o } }$ cho phép xác định ảnh hưởng của $p$ tới công thức. Nếu không có thêm thông tin gì khác thì xác suất tiền nghiệm thường được tính $p = 1 ~ / ~ k$ , trong đó $k$ là số thuộc tính của thuộc tính $X _ { i }$ . Ví dụ, nếu không có thêm thông tin gì thêm thì xác suất quan sát thấy $\mathrm { G i } \acute { \mathrm { o } } =$ mạnh sẽ là 1/2 do thuộc tính Gió có hai giá trị. Nếu $m = 0$ , ta được công thức không làm trơn ban đầu. Ngược lại, khi $\mathbf { m } \longrightarrow \infty$ , xác suất hậu nghiệm sẽ bằng $p$ , bất $\ker \hat { \mathsf { e } } n _ { c }$ thế nào. Trong những trường hợp c n lại, cả $n _ { c } / n$ và p cùng đóng góp vào công thức.

# Ứng dụng trong phân loại văn bản tự động

Phân loại văn bản tự động là bài toán có nhiều ứng dụng thực tế. Trước tiên, cho một tập huấn luyện bao gồm các văn bản. Mỗi văn bản có thể thuộc vào một trong C loại khác nhau (ở đây ta không xét trường hợp mỗi văn bản có thể thuộc vào nhiều loại khác nhau). Sau khi huấn luyện xong, thuật toán phân loại nhận được văn bản mới và cần xác định phân loại cho văn bản này. Ví dụ, với các văn bản là nội dung thư điện tử, thuật toán có thể phân loại thư thành “thư rác” và “thư bình thường”. Khi huấn luyện, thuật toán học được cung cấp một tập thư rác và một tập thư thường. Sau đó, dựa trên nội dung thư mới nhận, bộ phân loại sẽ tự xác định đó có phải thư rác không. Một ứng dụng khác là tự động phân chia bản tin thành các thể loại khác nhau, ví dụ “chính trị”, “xã hội”, “thể thao”.v.v. như trên báo điện tử.



Phân loại văn bản tự động là dạng ứng dụng trong đó phân loại Bayes đơn giản và các phương pháp xác suất khác được sử dụng rất thành công. Chương trình lọc thư rác mã nguồn mở SpamAssassin (http://spamassassin.apache.org) là một chương trình lọc thư rác được sử dụng rộng rãi với nhiều cơ chế lọc khác nhau, trong đó lọc Bayes đơn giản là cơ chế lọc chính được gán trọng số cao nhất.

Sau đây ta sẽ xem xét cách sử dụng phân loại Bayes đơn giản cho bài toán phân loại văn bản. Để đơn giản, ta sẽ xét trường hợp văn bản có thể nhận một trong hai nhãn: “rác” và “không”.

Để sử dụng phân loại Bayes đơn giản, cần giải quyết hai vấn đề chủ yếu: thứ nhất, biểu diễn văn bản thế nào cho phù hợp; thứ hai: lựa chọn công thức cụ thể cho bộ phân loại Bayes.

Cách thông dụng và đơn giản nhất để biểu diễn văn bản là cách biểu diễn bằng “túi từ” (bag-of-word). Theo cách này, mỗi văn bản được biểu diễn bằng một tập hợp, trong đó mỗi phần tử của tập hợp tương ứng với một từ khác nhau của văn bản. Để đơn giản, ở đây ta coi mỗi từ là một đơn vị ngôn ngữ được ngăn với nhau bởi dấu cách. Lưu ý rằng đây là cách đơn giản nhất, ta cũng có thể thêm số lần xuất hiện thực tế của từ trong văn bản. Cách biểu diễn này không quan tâm tới vị trí xuất hiện của từ trong văn bản cũng như quan hệ với các từ xung quanh, do vậy có tên gọi là túi từ. Ví dụ, một văn bản có nội dung “Chia thư thành thư rác và thư thường” sẽ được biểu diễn bởi tập từ {“chia”, “thư”, “thành”, “rác”, “và”, “thường”} với sáu phần tử.

Giả thiết các từ biểu diễn cho thư xuất hiện độc lập với nhau khi biết nhãn phân loại, công thức Bayes đơn giản cho phép ta viết:

$\begin{array} { r } { c _ { N B } = \underset { c j \in \{ r a c , k h o n g \} } { \operatorname { a r g m a x } } P ( c _ { j } ) \prod _ { i } P ( x _ { i } | c _ { j } ) } \\ { c _ { j } \in \{ r a c , k h o n g \} \quad \quad } \end{array}$ = argmax cj∈{rac,khong}

P(cj) P(“chia”| cj) P(“thư ”| cj) P(“thành”| cj) P(“rác”| cj) P(“và”| cj) P(“thường ”| cj)

Các xác suất $P ( \operatorname { \mathbb { f } } \operatorname { \mathrm { r a c } } ^ { , 9 } | c _ { j } )$ được tính từ tập huấn luyện như mô tả ở trên. Những từ chưa xuất hiện trong tập huấn luyện sẽ bị bỏ qua, không tham gia vào công thức.



Cần lưu ý rằng cách biểu diễn và áp dụng phân loại Bayes đơn giản cho phân loại văn bản vừa trình bày là những phương án đơn giản. Trên thực tế có rất nhiều biến thể khác nhau cả trong việc chọn từ, biểu diễn văn bản bằng các từ, cũng như công thức tính xác suất điều kiện của văn bản.

Mặc dù đơn giản, nhiều thử nghiệm cho thấy, phân loại văn bản tự động bằng Bayes đơn giản có độ chính xác khá cao. Trên nhiều tập dữ liệu thư điện tử, tỷ lệ phân loại chính xác thư rác có thể đạt trên $9 8 \%$ . Kết quả này cho thấy, mặc dù giả thiết các từ độc lập với nhau là không thực tế, độ chính xác phân loại của Bayes đơn giản không bị ảnh hưởng đáng $\mathrm { k } \mathring { \mathrm { e } }$ .

# Public_113 

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

# Public_114 

# I. Giới thiệu

Mặc dù công nghệ xử lý hình ảnh đã có nhiều tiến bộ, các hình ảnh thu được vẫn thường không thể hiện đầy đủ chi tiết cảnh hoặc có độ tương phản thấp do giới hạn dải động. Các phương pháp tăng cường tương phản (Contrast Enhancement - CE) đã được phát triển nhằm khắc phục vấn đề này. Tuy nhiên, các phương pháp truyền thống như Histogram Equalization - HE thường tập trung vào phân phối mức xám tuyệt đối, dẫn đến hạn chế trong việc xử lý tương phản cục bộ và dễ gây hiện tượng quá làm nổi bật ở một số vùng ảnh.

Phương pháp được đề xuất là một thuật toán tăng cường tương phản toàn cục mới, dựa trên khung lý thuyết Layered Difference Representation - LDR. Điểm khác biệt chính của phương pháp này so với các thuật toán truyền thống là việc sử dụng lược đồ 2D để biểu diễn mối quan hệ mức xám giữa các điểm ảnh liền $\mathbf { k } \dot { \hat { \mathbf { e } } } .$ , thay vì chỉ xét đến phân phối mức xám đơn lẻ. Điều này cho phép phương pháp tận dụng sự nhạy cảm tự nhiên của hệ thống thị giác con người (Human Visual System - HVS) đối với sự khác biệt mức xám, mang lại kết quả cải thiện tương phản phù hợp hơn với nhận thức thị giác.

Phương pháp LDR $\mathrm { k } \acute { \mathrm { e } }$ thừa từ các nghiên cứu sử dụng lược đồ 2D trước đó, chẳng hạn như thuật toán Contextual Visual Contrast (CVC). Tuy nhiên, thay vì chỉ khai thác thông tin biên và cạnh vật thể, phương pháp LDR thiết lập mối quan hệ chặt chẽ giữa lược đồ 2D của ảnh đầu vào và sự khác biệt mức xám trong ảnh đầu ra. Phương pháp này nhấn mạnh các sự khác biệt xuất hiện thường xuyên, qua đó cải thiện tương phản cục bộ và tận dụng tối đa dải động. Điều này giúp LDR vượt qua các hạn chế của HE và CVC, mang lại hình ảnh đầu ra có độ tương phản cao hơn và chất lượng thị giác tốt hơn.

# II. Mô tả thuật toán

Thuật toán tăng cường tương phản toàn cục được đề xuất dựa trên Layered Difference Representation – LDR. Thuật toán gồm hai thành phần chính: intralayer optimization và inter-layer aggregation. Các bước chính được mô tả lần lượt dưới đây.



![](images/image1.jpg)

Hình minh họa quy trình, thể hiện các bước từ việc trích xuất lược đồ $2 D _ { i }$ , tối ưu hóa trong lớp, tổng hợp giữa các lớp, đến tái cấu trúc ảnh đầu ra.

# Trích Xuất Lược Đồ 2D

- Bước đầu tiên là xây dựng lược đồ 2D $\mathrm { { h } } ( \mathrm { { k } } , \mathrm { { k } } + 1 )$ từ ảnh đầu vào. Lược đồ này đếm số lượng các cặp điểm ảnh liền $\mathrm { k } \dot { \hat { \mathbf { e } } }$ với mức xám k và $_ { \mathrm { k + l } }$ , biểu diễn sự khác biệt mức xám giữa các điểm ảnh trong không gian ảnh.

ℎ(??, ?? + ??) = ??ầ?? ??ố ??á?? ??ặ?? đ??ể?? ả??ℎ ??ó ??ứ?? ??á?? $( k , k + l )$

Lược đồ 2D cung cấp thông tin phong phú về sự thay đổi mức xám, giúp phát hiện các đặc điểm cục bộ quan trọng để cải thiện tương phản.

# Intra-Layer Optimization

Lược đồ $\mathrm { { h } } ( \mathrm { { k } } , \mathrm { { k } } + 1 )$ được phân tách thành các lớp (layers), mỗi lớp đại diện cho một khoảng chênh lệch mức xám cụ thể l.

- Với mỗi lớp l, một vector lược $\dot { \mathrm { d } } \dot { \hat { \mathrm { o } } } \mathrm { h } _ { \mathrm { l } }$ được tính toán. Vector này được sử dụng để thiết lập một hệ phương trình tuyến tính, từ đó giải ra vector sự khác biệt ${ \bf d } _ { \mathrm { l } }$ cho lớp l.

$$
D \cdot d _ { l } = s _ { l } ,
$$

với D là ma trận chênh lệch, sl là tổng của $\mathrm { h } _ { \mathrm { l } }$ .

- Quá trình tối ưu này đảm bảo rằng các sự khác biệt mức xám xuất hiện thường xuyên sẽ được làm nổi bật trong ảnh đầu ra.

# Inter-Layer Aggregation

- Các vector khác biệt dl từ tất cả các lớp được tổng hợp lại thành một vector sự khác biệt hợp nhất d, sử dụng một vector trọng số w để xác định mức độ đóng góp của mỗi lớp.



$$
d = \sum _ { l = 1 } ^ { 2 5 5 } w _ { l } \cdot d _ { l }
$$

Quá trình tổng hợp này giúp kết hợp thông tin từ tất cả các lớp, tạo ra một biểu diễn toàn diện cho toàn bộ ảnh.

# Tái Cấu Trúc Hàm Biến Đổi

Vector d được sử dụng để tái cấu trúc hàm biến đổi $\mathbf { X }$ , ánh xạ mức xám đầu vào thành mức xám đầu ra.

$$
x _ { k } = x _ { k - 1 } + d _ { k - 1 } , \forall k \in [ 1 , 2 5 5 ]
$$

Hàm biến đổi này được áp dụng để biến đổi ảnh đầu vào, tạo ra ảnh đầu ra với độ tương phản được cải thiện.

# Kết Quả

Hàm biến đổi x được áp dụng lên ảnh đầu vào:

$$
o u t = x [ i m g ]
$$

- Phương pháp tập trung vào việc tăng cường các sự khác biệt mức xám thường xuất hiện trong ảnh đầu vào. Điều này giúp cải thiện đáng $\mathrm { k } \mathring { \mathrm { e } }$ độ tương phản so với các phương pháp truyền thống, đồng thời tận dụng toàn bộ dải động của ảnh.

# Public_115 

# I. Giới thiệu

Trong các điều kiện ánh sáng yếu, ảnh chụp thường bị suy giảm đáng $\mathrm { k } \mathring { \mathrm { e } }$ về chất lượng, xuất hiện noise và màu sắc không chính xác, gây khó khăn cho các ứng dụng như giám sát an ninh, xử lý y tế, và thị giác máy tính. Nhiệm vụ cải thiện ảnh ánh sáng yếu (Low-Light Image Enhancement - LLIE) nhằm phục hồi chi tiết, cân bằng độ sáng và giảm thiểu nhiễu từ các ảnh bị suy giảm chất lượng. Các phương pháp hiện tại chủ yếu dựa vào mạng nơ-ron học sâu để học hàm ánh xạ từ ảnh ánh sáng yếu sang ảnh sáng chuẩn trên không gian màu sRGB hoặc HSV. Tuy nhiên, các không gian màu này thường không ổn định do mối liên hệ phức tạp giữa độ sáng và màu sắc, dẫn đến sự phụ thuộc mạnh giữa các kênh RGB hoặc sự bất liên tục trên trục màu Hue trong không gian HSV.

Để giải quyết những hạn chế này, phương pháp tiếp cận mới được đề xuất nhằm định nghĩa một không gian màu có khả năng học được, có tên là Horizontal/Vertical-Intensity (HVI). Không gian HVI được thiết kế đặc biệt để tách biệt rõ ràng độ sáng và màu sắc, đồng thời thích ứng với các điều kiện chiếu sáng khác nhau thông qua các tham số học được. Điều này cho phép cải thiện sự ổn định trong việc xử lý ảnh, giảm thiểu hiệu ứng giả màu và lỗi về độ sáng thường gặp trong các không gian màu truyền thống. Bên cạnh đó, không gian HVI cung cấp nền tảng hiệu quả để xây dựng các kiến trúc mạng nơ-ron tối ưu hóa, phù hợp với các thiết bị tài nguyên hạn chế.

Để tận dụng tối đa không gian màu HVI, một mạng học sâu có tên Color and Intensity Decoupling Network (CIDNet) được đề xuất, kết hợp hai nhánh xử lý song song cho độ sáng và màu sắc. CIDNet được trang bị cơ chế Lighten CrossAttention (LCA), giúp tối ưu hóa tương tác giữa các đặc trưng của nhánh độ sáng và nhánh màu sắc, đảm bảo tính bổ sung thông tin giữa hai thành phần. Kết quả thực nghiệm trên nhiều bộ dữ liệu đã chứng minh rằng CIDNet, dựa trên không gian HVI, không chỉ đạt hiệu suất vượt trội so với các phương pháp hiện đại mà còn giảm thiểu đáng $\mathrm { k } \mathring { \mathrm { e } }$ độ phức tạp tính toán, đáp ứng yêu cầu triển khai trên các thiết bị biên.



# II. Mô tả phương pháp

# Không gian màu HVI

Không gian màu Horizontal/Vertical-Intensity (HVI) được thiết kế để tách biệt hoàn toàn độ sáng và màu sắc, đồng thời bổ sung các tham số học được, cho phép hệ thống thích nghi tốt hơn với các điều kiện chiếu sáng khác nhau.

# Cấu trúc của HVI

Không gian màu HVI bao gồm ba thành phần chính, được thiết kế để cải thiện khả năng biểu diễn và xử lý ảnh:

2.1. Intensity Map (Bản đồ độ sáng):

Bản đồ độ sáng được tính toán dựa trên giá trị lớn nhất trong ba kênh RGB tại mỗi điểm ảnh, giúp biểu diễn trực tiếp cường độ ánh sáng của cảnh. Công thức được định nghĩa như sau:

$$
I _ { m a x } = \operatorname* { m a x } _ { c \epsilon \{ R , G , B \} } ( I _ { C } )
$$

Bản đồ này đóng vai trò làm tham chiếu để phân tách độ sáng và màu sắc.

2.2. HV Transformation (Chuyển đổi màu sắc theo trục ngang/dọc):

Chuyển đổi HV được thiết kế để khắc phục tính không liên tục của trục Hue trong không gian HSV. Nó sử dụng các tham số học được và ánh xạ từng điểm ảnh sang mặt phẳng màu ngang/dọc, tạo thành một hệ tọa độ trực giao cho màu sắc.

Công thức tổng quát:

$$
\begin{array} { c } { { \widehat { H } = C _ { k } \cdot S \cdot D _ { T } \cdot \cos { ( 2 \pi P _ { \gamma } ) } } } \\ { { { } } } \\ { { \widehat { V } = C _ { k } \cdot S \cdot D _ { T } \cdot s i n ( 2 \pi P _ { \gamma } ) } } \end{array}
$$



Trong đó, $\mathrm { C _ { k } }$ đại diện cho mật độ màu, $\mathrm { D } _ { \mathrm { T } }$ là hàm điều chỉnh độ bão hòa, và $\mathrm { P } _ { \gamma }$ là ánh xạ tuyến tính điều chỉnh màu sắc

2.3. Perceptual-Invert HVI Transformation (Chuyển đổi ngược):

Không gian HVI tích hợp các tham số học được để cải thiện khả năng xử lý linh hoạt:

# a. Color-Density-k (Mật độ màu):

Tham số k điều chỉnh mật độ màu trên mặt phẳng màu ở các vùng có độ sáng thấp, giảm thiểu mất mát thông tin trong vùng tối. Công thức được định nghĩa như sau:

$$
C _ { k } = k \sqrt { \sin \left( \frac { \pi I _ { m a x } } { 2 } \right) + \epsilon }
$$

b. Hue Bias Parameters $( \gamma _ { G } , \gamma _ { B } )$ :

Các tham số này điều chỉnh độ nhạy màu sắc theo các kênh RGB để phù hợp với các đặc tính của cảm biến máy ảnh, giảm thiểu hiện tượng lệch màu, đặc biệt ở các vùng ánh sáng yếu.

c. Chức năng điều chỉnh độ bão hòa $( \mathrm { D } _ { \mathrm { T } } )$

Một hàm học được để tối ưu hóa độ bão hòa màu sắc dựa trên ánh xạ tuyến tính của tham số $\mathrm { P } _ { \gamma }$ , đảm bảo tính linh hoạt trong việc điều chỉnh cường độ màu.

# Chuyển đổi hai chiều giữa HVI và sRGB

Quá trình chuyển đổi giữa HVI và sRGB được thiết kế để đảm bảo tính thuận nghịch, với hai bước chính:

## Từ sRGB sang HVI:

Sử dụng bản đồ độ sáng $( I _ { \mathrm { m a x } }$ ) để tính toán các thành phần HVI, bao gồm các mặt phẳng ngang và dọc (Ĥ, V̂ ). Phương pháp này đảm bảo rằng màu sắc và độ sáng được tách biệt hoàn toàn.



## Từ HVI về sRGB:

Chuyển đổi ngược được thực hiện bằng cách tái hợp nhất các thành phần HVI và ánh xạ về không gian sRGB. Các công thức sau đây được sử dụng:

$$
R = f ( \widehat { H } , \widehat { V } , I _ { m a x } )
$$

$$
G , B = T u o n g t \downarrow \downarrow d a t r \hat { \mathsf { e } } n \dot { a } n h x \mathsf { a } c \dot { \mathsf { u } } a \widehat { H } , \widehat { V }
$$

Quá trình này không chỉ phục hồi màu sắc chính xác mà còn duy trì độ sáng tự nhiên của ảnh.

4. CIDNet

## Kiến trúc tổng thể

![](images/image1.jpg)

Tổng quan về mô hình CIDNet được đề xuất. (a) Chuyển đổi màu HVI (HVIT) nhận một ảnh sRGB làm đầu vào và tạo ra bản đồ màu HV cùng bản đồ cường độ sáng làm đầu ra. (b) Mạng tăng cường thực hiện quá trình xử lý chính, sử dụng kiến trúc UNet hai nhánh, bao gồm sáu khối Lighten Cross-Attention (LCA). Cuối cùng, áp dụng Perceptual-inverse HVI Transform (PHVIT) để nhận bản đồ HVI đã được làm sáng làm đầu vào và chuyển đổi nó thành ảnh sRGB đã được cải thiện.

Mô hình CIDNet (Color and Intensity Decoupling Network) được thiết kế dựa trên không gian màu HVI để tách biệt và xử lý độ sáng (Intensity) và màu sắc (HV-plain) trong ảnh ánh sáng yếu. Kiến trúc CIDNet bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ ba thành phần chính:



### HVI Transformation (HVIT):

Thành phần này chuyển đổi ảnh từ không gian sRGB sang không gian HVI, tách biệt hai đặc trưng:

- Intensity Map (Bản đồ độ sáng): Đại diện cho độ sáng tổng thể của cảnh, được tính toán từ giá trị lớn nhất trong các kênh RGB tại mỗi điểm ảnh.

- HV Color Map (Bản đồ màu HV): Chứa thông tin màu sắc và cấu trúc của ảnh, được điều chỉnh bởi các tham số học được như Color-Density-k và Hue Bias Parameters $( \gamma _ { \mathrm { G } } , \gamma _ { \mathrm { B } } )$ .

Quá trình này đảm bảo tách biệt hoàn toàn giữa độ sáng và màu sắc, giúp giảm độ phức tạp của mô hình trong các bước xử lý sau.

4.1.2. Mạng Tăng cường (Enhancement Network):

Đây là thành phần chính trong CIDNet, được thiết kế dựa trên kiến trúc UNet hai nhánh:

- HV-branch: Xử lý các đặc trưng màu sắc từ HV Color Map để loại bỏ nhiễu và đảm bảo màu sắc chính xác.

- Intensity-branch: Xử lý thông tin độ sáng từ Intensity Map, cải thiện độ sáng tổng thể của ảnh.

Mạng sử dụng cơ chế Lighten Cross-Attention (LCA) để trao đổi thông tin giữa hai nhánh, đảm bảo sự phối hợp và bổ sung thông tin giữa màu sắc và độ sáng.

4.1.3. Perceptual-Inverse HVI Transformation (PHVIT):

Thành phần này chuyển đổi ảnh đã được cải thiện trong không gian HVI trở lại không gian sRGB, tái hợp nhất thông tin màu sắc và độ sáng để tạo ra ảnh đầu ra tự nhiên và chính xác.

## Lighten Cross-Attention (LCA) Module



CIDNet là một mạng học sâu không gian màu HVI và cơ chế LCA để tối ưu hóa khả năng xử lý ảnh ánh sáng yếu. Với kiến trúc UNet hai nhánh và các thành phần được thiết $\mathrm { k } \acute { \mathrm { e } }$ chuyên biệt, CIDNet không chỉ cải thiện chất lượng độ sáng và màu sắc của ảnh mà còn giảm thiểu độ phức tạp tính toán, phù hợp với các thiết bị tài nguyên hạn chế.

![](images/image2.jpg)

Khối Lighten CrossAttention (LCA) hai nhánh (tức là nhánh và nhánh HV). LCA bao gồm một khối Chú ý Chéo (CAB), một Lớp Tăng cường Cường độ (IEL), và một Lớp Giảm nhiễu Màu sắc (CDL). Các lớp tích chập nhúng đặc trưng bao gồm một lớp tích chập theo chiều sâu $I \times I$ và một lớp tích chập theo nhóm $3 \times 3 .$ .

LCA là thành phần quan trọng trong CIDNet, được thiết kế để tăng cường sự phối hợp giữa hai nhánh HV-branch và Intensity-branch bằng cách học các thông tin bổ sung giữa chúng. LCA bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ ba thành phần chính:



### Cross Attention Block (CAB)

- CAB thực hiện cơ chế chú ý chéo (cross-attention), trong $\tt d \ ' 0 \ m o t$ nhánh hoạt động như "query" và nhánh còn lại là "key" và "value".

- Cơ chế này giúp mỗi nhánh học được thông tin bổ sung từ nhánh đối diện, cải thiện hiệu quả xử lý. Công thức được định nghĩa như sau:

$$
Y _ { I } = W ( V \odot S o f t m a x ( K / \alpha _ { H } ) ) + Y _ { I }
$$

o Q, K, V: Các ma trận chú ý được tính từ các nhành   
o W: Lớp tích chập nhúng đặc trưng (Feature Embedding Convolution)   
o $\alpha _ { H }$ : Tham số điều chỉnh.

4.2.2. Intensity Enhance Layer (IEL)

- Lớp IEL được thiết kế để cải thiện độ sáng tổng thể, sử dụng phép nhân theo phần tử (element-wise multiplication) giữa các tensor đầu vào, giúp tăng cường các vùng sáng mà không gây bão hòa. Công thức IEL:

$$
Y _ { I } = \ T a n h ( W _ { I } \cdot Y _ { I } ) \odot \ T a n h ( W _ { R } \cdot Y _ { R } )
$$

o $\mathrm { W _ { I } }$ , $\mathrm { W _ { R } }$ : Lớp tích chập chiều sâu (depth-wise convolution)

4.2.3. Color Denoise Layer (CDL) - CDL giảm nhiễu trong các vùng tối của ảnh, đảm bảo màu sắc chính xác. Cơ chế này giúp duy trì tính tự nhiên của ảnh và giảm thiểu lỗi giả màu.

## Hàm mất mát (Loss Function)

Hàm mất mát của CIDNet được thiết kế để khai thác ưu điểm của cả không gian màu HVI và không gian sRGB, giúp tối ưu hóa chất lượng ảnh đầu ra. Cụ thể, hàm mất mát bao gồm:

4.3.1. Hàm Mất Mát trong Không gian HVI

Trong không gian HVI, hàm mất mát được cấu thành bởi ba thành phần chính:

a. L1 Loss (L1):

- Đo lường sự khác biệt trung bình tuyệt đối giữa ảnh dự đoán $( \widehat { X } _ { H V I } )$ và ảnh gốc $( X _ { H V I } )$ .



- Đảm bảo rằng ảnh dự đoán gần với ảnh gốc về mặt giá trị điểm ảnh.

b. Edge Loss $\mathrm { ( L _ { e } ) }$ :

- Bảo tồn các cạnh và cấu trúc trong ảnh bằng cách tối thiểu hóa sự khác biệt giữa các gradient của ảnh dự đoán và ảnh gốc.

c. Perceptual Loss (Lp):

- Đảm bảo chất lượng nhận thức của ảnh dự đoán, bằng cách sử dụng các đặc trưng được trích xuất từ mạng đã huấn luyện trước (chẳng hạn VGG19).

Hàm mất mát tổng hợp trong không gian HVI được biểu diễn như sau:

$$
\begin{array} { r l } & { l \bigl ( \hat { X } _ { H V I } , X _ { H V I } \bigr ) } \\ & { \qquad = \lambda _ { 1 } \cdot L _ { 1 } \bigl ( \hat { X } _ { H V I } , X _ { H V I } \bigr ) + \lambda _ { e } \cdot L _ { e } \bigl ( \hat { X } _ { H V I } , X _ { H V I } \bigr ) + \lambda _ { p } } \\ & { \qquad \cdot L _ { p } \bigl ( \hat { X } _ { H V I } , X _ { H V I } \bigr ) } \end{array}
$$

4.3.2. Hàm Mất Mát trong Không gian sRGB

Trong không gian sRGB, hàm mất mát cũng sử dụng các thành phần $\mathrm { L _ { l } , L _ { e } }$ và Lp, tương tự như trong không gian HVI, để đảm bảo chất lượng ảnh đầu ra ở không gian màu chuẩn.

### Hàm Mất Mát Tổng quát

Hàm mất mát tổng quát kết hợp cả hai không gian HVI và sRGB:

$$
L = \lambda _ { c } \mathbf { \langle } l \bigl ( \widehat { X } _ { H V I } , X _ { H V I } \bigr ) + l ( \widehat { I } , I )
$$

Trong đó:

o ??(??̂??????, ????????): Hàm mất mát trong không gian HVI.   
o ??(??̂, ??): Hàm mất mát trong không gian sRGB.   
o ????: Trọng số để cân bằng giữa hai không gian.

# Public_116 

# Mở đầu

Để huấn luyện một mô hình mạng nơ-ron, chúng ta cần dựa trên giá trị hàm mất mát để biết được sự khác biệt giữa các dự đoán của mô hình đưa ra và nhãn mà chúng ta muốn dự đoán. Giá trị hàm mất mát càng bé có nghĩa là mô hình học đưa ra càng chính xác. Với mục tiêu hạ thấp giá trị của hàm mất mát, việc sử dụng các thuật toán tối ưu tập hợp các tham số và siêu tham số (parameter và hyper parameter) là một thành phần cốt lõi giúp cải thiện kết quả nhận dạng.

Trong bài báo này, chúng tôi thực hiện khảo sát các thuật toán tối ưu hiện đang nhận được nhiều sự quan tâm như SGD, RMS Prop, AdaGrad, AdaDelta và Adam. Mỗi thuật toán sẽ có những đặc điểm kĩ thuật riêng, và sẽ được đánh giá khảo sát dựa trên nhiệm vụ nhận dạng/phân loại hình ảnh. Tập dữ liệu được sử dụng trong nghiên cứu này là MNIST và CIFAR-10, hai tập cơ sở dữ liệu được sử dụng phổ biến cho nhiều nghiên cứu khác trên thế giới.

# Mạng nơ-ron tích chập và thuật toán tối ưu

Để đọc giả có thể tiếp cận được vấn đề một cách tổng quan và dễ dàng, trong nội dung phần này chúng tôi chọn trình bày những nội dung cơ bản nhất về mạng nơ-ron tích chập cũng như sơ lược về thuật toán tối ưu. Đây là những nội dung cốt lõi của nghiên cứu này.

## Mạng nơ-ron tích chập

Đối với mạng đa lớp Perceptron (Multi-layer Perceptron – MLP) truyền thống, mỗi nơ-ron trong lớp phía trước sẽ kết nối đến tất cả các nơ- ron ở lớp phía sau, khi tăng độ sâu của mô hình sẽ khiến khối lượng tính toán trong mạng tăng mạnh.

Sự ra đời của mạng CNN đã giúp giải quyết vấn đề trên dựa trên 3 ý tưởng cơ bản: vùng tiếp nhận cục bộ, tập trọng số chia sẻ và phương pháp lấy mẫu xuống. Nhìn chung, cấu trúc của CNN gồm một số lớp cơ bản sau:

![](images/image1.jpg)



# Hình 2.1. Mô hình một mạng CNN đơn giản.

## Lớp tích chập (Convolutional layer)

Lớp tích chập là một thành phần cốt lõi của mạng nơ-ron tích chập (CNN), sử dụng để trích xuất các thông tin đặc tính của hình ảnh (feature map). Kết quả đầu ra nhận được là các đặc tính của ảnh, tương ứng với bộ lọc đã sử dụng, với càng nhiều bộ lọc được sử dụng, sẽ thu được càng nhiều thông tin của ảnh tương ứng. Bên cạnh đó, việc sử dụng lớp tích chập sẽ có nhiều ưu điểm so với mạng nơ-ron truyền thống MLP, đặc biệt khi dữ liệu là hình ảnh. Một số ưu điểm có thể nổi trội so với mô hình trước đây có thể kể đến: Trích xuất thông tin theo phân vùng không gian hay hạn chế số lượng tham số và khối lượng tính toán khi tăng chiều sâu cho mô hình.

## Lớp lấy mẫu xuống (Pooling/Subsampling layer)

Lớp lấy mẫu xuống có tác dụng giảm kích thước của dữ liệu hình ảnh từ đó giúp cho mạng có thể học được các thông tin có tính chất khái quát hơn, đây cũng chính là phương pháp mà trung khu thần kinh thị giác của con người hoạt động. Đồng thời quá trình này giảm số lượng các thông số trong mạng. Các phương pháp lấy mẫu xuống thường được sử dụng là Max Pooling và Average Pooling.

## Lớp kết nối đầy đủ (Fully-connected layer - FC)

Đầu vào của lớp kết nối đầy đủ là đầu ra từ lớp lấy mẫu xuống hoặc lớp tích chập cuối cùng, nó được làm phẳng và sau đó được đưa vào lớp kết nối đầy đủ để chuyển tiếp. Lớp FC có nhiệm vụ tổng hợp thông tin đưa ra lớp quyết định (output) cho ra kết quả đánh giá.

# Thuật toán tối ưu

Về cơ bản, trong việc tối ưu hóa thiết kế, mục tiêu thiết kế hướng tới có thể chỉ là giảm thiểu chi phí sử dụng hoặc tối đa hóa hiệu quả nhận được. Để thực hiện điều này, thuật toán tối ưu hóa là một khâu không thể thiếu, đây một quy trình được thực hiện lặp đi lặp lại bằng cách so sánh các giải pháp khác nhau cho đến khi tìm thấy một giải pháp tối ưu hoặc thỏa đáng.

Đối với kỹ thuật học sâu nói riêng, thuật toán tối ưu là các kỹ thuật giúp xây dựng các mô hình mạng nơ-ron để tối ưu hóa độ chính xác của mô hình mạng [1]. Với mục tiêu là “học” được các đặc tính từ dữ liệu đầu vào, từ đó có thể tìm một tập các trọng số (weights - w) và ngưỡng (bias - $b$ ) phù hợp hơn.

## Vai trò của thuật toán tối ưu



Trong thuật toán học máy nói chung và kĩ thuật học sâu nói riêng, thuật toán tối ưu hóa là một khâu quan trọng không thể thiếu. Quá trình tối ưu hóa thực hiện xác định hàm mất mát (loss function) và sau đó tối thiểu hóa hàm trên bằng cách sử dụng hàm tối ưu. Cụ thể, thông qua việc cập nhật các tham số của mô hình $( w , b )$ và đánh giá lại hàm mất mát với một tỉ lệ học (learning rate) xác định, quá trình tối ưu giúp mô hình tương thích tốt hơn với tập dữ liệu được đào tạo.

## Hàm mất mát (Loss function)

Hàm mất mát là một phương pháp đánh giá độ hiệu quả của thuật toán “học” cho mô hình trên tập dữ liệu được sử dụng. Hàm mất mát trả về một số thực không âm thể hiện sự chênh lệch giữa hai đại lượng: a, nhãn được dự đoán và y, nhãn đúng. Hàm mất mát, bản thân chính là một cơ chế thưởng-phạt, mô hình sẽ phải đóng phạt mỗi lần dự đoán sai và mức phạt tỉ lệ thuận với độ lớn sai sót. Trong mọi bài toán học có giám sát, mục tiêu luôn bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ giảm tổng mức phạt phải đóng. Trong trường hợp lý tưởng a = y, loss function sẽ trả về giá trị cực tiểu bằng 0 [2]. Hai hàm mất mát thường xuyên được sử dụng trong mạng nơ-ron: MSE (Mean Squared Error) và Cross Entropy.

## Tỉ lệ học (Learning rate)

Learning rate hay tỉ lệ học là một thông số quan trọng trong việc quyết định tốc độ học của mạng nơ-ron. Tốc độ học được thể hiện bằng sự thay đổi giá trị cập nhật trọng số (w) trong các chu kỳ học. Tùy theo mục đích của mô hình mà tăng/giảm tỉ lệ học. Tỉ lệ học càng cao thì giúp mô hình học khá nhanh và tiết kiệm được thời gian huấn luyện, tuy nhiên việc tỉ lệ học lớn đồng nghĩa với việc sự thay đổi trọng số $( w )$ và tham số ngưỡng - bias $( b )$ càng lớn, mô hình không ổn định, một số chu kỳ học có sự dao động mạnh ở tỉ lệ nhận dạng đúng hay nói cách khác là thuật toán không được tối ưu và ngược lại đối với tỉ lệ học nhỏ.

# Một số thuật toán tối ưu

Trong phạm vi bài báo một số thuật toán tối ưu hóa sẽ được đánh giá khảo sát gồm: Gradient Descent [3], SGD với động lượng [4], RMSProp [5], Adagrad [6], Adadelta [7], Adam [6]. Việc đánh giá được thực hiện dựa trên tiêu chí giá trị hàm mất mát và tỉ lệ nhận dạng đúng hình ảnh dựa trên hai tập Train và Test data. Dựa trên các kết quả đó có thể đánh giá tác động của thuật toán tối ưu đến mô hình mạng ứng dụng vào bài toán nhận dạng hình ảnh.

## Gradient Descent



Gradient Descent (GD) là thuật toán tìm tối ưu chung cho các hàm số. $\acute { \mathrm { Y } }$ tưởng chung của GD là điều chỉnh các tham số để lặp đi lặp lại thông qua $\mathrm { m } \tilde { \hat { \mathrm { m } } } \mathrm { i }$ dữ liệu huấn luyện để giảm thiểu hàm chi phí.

$$
w ^ { ( k + 1 ) } = w ^ { ( k ) } - \eta \nabla _ { w } J ( w ^ { ( k ) } )
$$

Với $w ^ { ( k ) }$ là tham $\mathrm { s } \acute { \mathrm { o } }$ tại bước cập nhật tại lớp k, $\boldsymbol { \eta }$ là tỉ lệ học, $J ( w )$ là hàm lỗi, $\nabla _ { w } J ( w ^ { ( k ) } )$ : đạo hàm của hàm lỗi tại điểm $w ^ { ( k ) }$ .

## SGD với động lượng (SGD with momentum)

SGD với momentum là phương pháp giúp tăng tốc các vectơ độ dốc theo đúng hướng, và giúp hệ thống hội tụ nhanh hơn. Đây là một trong những thuật toán tối ưu hóa phổ biến nhất và nhiều mô hình hiện đại sử dụng nó để đào tạo. Mô tả như sau:

$$
v _ { j }  \alpha * v _ { j } - \eta * \nabla _ { W } \sum _ { 1 } ^ { m } L _ { m } ( w )
$$

$$
w _ { j }  v _ { j } + w _ { j }
$$

Phương trình (3.2) có hai phần. Thuật ngữ đầu tiên là độ dốc $\mathbf { v } _ { \mathrm { j } }$ được giữ lại từ các lần lặp trước. Hệ số động lượng $\alpha$ là tỉ lệ phần trăm của độ dốc được giữ lại mỗi lần lặp. L là hàm mất mát, $\boldsymbol { \mathsf { \Pi } } \boldsymbol { \mathsf { \Pi } }$ là tỉ lệ học.

## RMSProp (Root Mean Square Propogation)

RMSProp sử dụng trung bình bình phương của gradient để chuẩn hóa gradient. Có tác dụng cân bằng kích thước bước - giảm bước cho độ dốc lớn để tránh hiện tượng phát nổ độ dốc (Exploding Gradient), và tăng bước cho độ dốc nhỏ để tránh biến mất độ dốc (Vanishing Gradient). RMSProp tự động điều chỉnh tốc độ học tập, và chọn một tỉ lệ học tập khác nhau cho mỗi tham số. Phương pháp cập nhật các trọng số được thực hiện như mô tả:

$$
\begin{array} { l } { \displaystyle { s _ { t } = \rho s _ { t - 1 } + ( 1 - \rho ) * g _ { t } ^ { 2 } } } \\ { \displaystyle { \quad \varDelta x _ { t } = - \frac { \eta } { \sqrt { s _ { t } + \epsilon } } * g _ { t } } } \end{array}
$$

$$
x _ { t + 1 } = x _ { t } + \varDelta x _ { t }
$$

$\ldots ( \mathrm { N } \dot { \mathrm { o i } }$ $s _ { t }$ : tích luỹ phương sai của các gradient trong quá khứ, $\rho$ : tham số suy giảm, $\varDelta x _ { t }$ : sự thay đổi các tham số trong mô hình, $g _ { t }$ : gradient của các tham số tại vòng lặp t, ϵ: tham số đảm bảo kết quả xấp xỉ có ý nghĩa.

## Adagrad



Adagrad là một kỹ thuật học máy tiên tiến, thực hiện giảm dần độ dốc bằng cách thay đổi tốc độ học tập. Adagrad được cải thiện hơn bằng cách cho trọng số học tập chính xác dựa vào đầu vào trước nó để tự điều chỉnh tỉ lệ học theo hướng tối ưu nhất thay vì với một tỉ lệ học duy nhất cho tất cả các nút.

$$
w _ { t + 1 } = w _ { t } - \frac { \eta } { \sqrt { G _ { t } + \epsilon } } . g _ { t }
$$

Trong công thức (3.4), $\mathrm { G } _ { \mathrm { t } }$ là ma trận đường chéo chứa bình phương của đạo hàm vecto tham $\mathrm { s } \acute { \mathrm { o } }$ tại vòng lặp t; $\mathbf { g } _ { \mathrm { t } }$ là vectơ của độ dốc cho vị trí hiện tại và $\boldsymbol { \eta }$ là tỉ ${ \bf l } \hat { \bf e }$ học.

## Adadelta

Adadelta là một biến thể khác của AdaGrad. Adadelta không có tham số tỉ lệ học. Thay vào đó, nó sử dụng tốc độ thay đổi của chính các tham số để điều chỉnh tỉ lệ học nghĩa là bằng cách giới hạn cửa sổ của gradient tích lũy trong quá khứ ở một số kích thước cố định của trọng số w.

$$
g _ { t } ^ { \prime } = \sqrt { \frac { \varDelta x _ { t - 1 } + \epsilon } { s _ { t } + \epsilon } } . g _ { t }
$$

$$
x _ { t } = x _ { t - 1 } - g _ { t } ^ { \prime }
$$

$$
\varDelta x _ { t } = \rho \varDelta x _ { t - 1 } + ( 1 - \rho ) \mathscr { x } _ { t } ^ { 2 }
$$

Từ công thức (3.5), Adadelta sử dụng 2 biến trạng thái: $s _ { t }$ để lưu trữ trung bình của khoảng thời gian thứ hai của gradient và $\Delta x _ { t }$ để lưu trữ trung bình của khoảng thời gian thứ 2 của sự thay đổi các tham số trong mô hình. $g _ { t } ^ { \prime }$ : căn bậc hai thương của trung bình tốc độ thay đổi bình phương và trung bình mô-men bậc hai của gradient.

## Adam

Adam được xem như là sự kết hợp của RMSprop và Stochastic Gradient Descent với động lượng. Adam là một phương pháp tỉ lệ học thích ứng, nó tính toán tỉ lệ học tập cá nhân cho các tham số khác nhau. Adam sử dụng ước tính của khoảng thời gian thứ nhất và thứ hai của độ dốc để điều chỉnh tỉ lệ học cho từng trọng số của mạng nơ-ron. Tuy nhiên, qua nghiên cứu thực nghiệm, trong một số trường hợp, Adam vẫn còn gặp phải nhiều thiếu sót so với thuật toán SGD. Thuật toán Adam được mô tả:

$$
\begin{array} { r } { m _ { t } = \beta _ { 1 } m _ { t - 1 } + ( 1 - \beta _ { 1 } ) g _ { t } } \\ { v _ { t } = \beta _ { 2 } v _ { t - 1 } + ( 1 - \beta _ { 2 } ) g _ { t } ^ { 2 } } \end{array}
$$



Trong công thức (3.6), $\mathbf { v _ { t } }$ là trung bình động của bình phương và $\mathrm { m } _ { \mathrm { t } }$ là trung bình động của gradient; $\beta _ { 1 } \mathrm { v } \dot { \mathrm { a } } \beta _ { 2 }$ là tốc độ của di chuyển.

# Đánh giá kết quả với các thuật toán tối ưu

## Cơ sở dữ liệu

Để thực hiện khảo sát và đánh giá các thuật toán tối ưu với bài toán phân loại hình ảnh, nhóm nghiên cứu đề xuất hai tập cơ sở dữ liệu phổ biến cho mục đích nghiên cứu là MNIST và CIFAR-10 để thực hiện quá trình đào tạo và thực nghiệm.

### MNIST

Bộ dữ liệu MNIST là bộ dữ liệu gồm các hình ảnh xám (grayscale picture) các chữ số viết tay được chia sẻ bởi Yann Lecun bao $\mathrm { g \dot { o } m 7 0 0 0 0 }$ ảnh chữ số viết tay được chia thành 2 tập: tập huấn luyện $\mathrm { g \dot { o } m \widetilde { \ o } 0 0 0 0 }$ ảnh và tập kiểm tra 10000 ảnh. Các chữ số viết tay ở tập MNIST được chia thành 10 nhóm tương ứng với các chữ số từ 0 đến 9. Tất cả hình ảnh trong tập MNIST đều được chuẩn hóa với kích thước $2 8 \times 2 8$ điểm ảnh. Dưới đây là một số hình ảnh được trích xuất từ bộ dữ liệu.

![](images/image2.jpg)  
Hình 4.1. Hình ảnh chữ số viết tay từ tập MNIST [8].

### CIFAR-10

Bộ cơ sở dữ liệu CIFAR10 là bộ dữ liệu chứa các ảnh màu có kích thước $3 2 \times 3 2 \times 3$ (3 lớp màu RGB) trong 10 nhóm khác nhau, gồm: máy bay, ô tô, chim, mèo, hươu, chó, ếch, ngựa, tàu và xe tải. Mỗi nhóm gồm 6000 hình ảnh, cùng với sự đa dạng về các thành phần như độ sáng, vị trí, hướng của các đối tượng. Nó là một trong những bộ dữ liệu được sử dụng rộng rãi nhất cho nghiên cứu máy học bao $\mathrm { g \dot { o } m \bar { 6 } 0 0 0 0 }$ ảnh được chia thành 2 tập: tập huấn luyện gồm 50000 ảnh và tập kiểm tra 10000 ảnh.

## Mô hình và phương pháp đánh giá

Ở đây, nhóm nghiên cứu đề xuất sử dụng mô hình CNN với cấu trúc:



Input → Convolution2D → Maxpooling → Dropout → Convolution2D Maxpooling Dropout Flatten Dense Output.

Quá trình huấn luyện và đánh giá với chu kì học là 50 và tỉ lệ học của từng thuật toán được sử dụng theo khuyến nghị của Google Colab, cụ thể tỉ lệ học ứng với các thuật toán SGD với động lượng, RMSProp, Adagrad, Adadelta, Adam lần lượt là 0.01, 0.001, 0.01, 1.0, 0.001. Phương pháp thực hiện đánh giá kết quả sử dụng trong bài là loss function và tỉ lệ nhận dạng đúng trên các tập dữ liệu được xét.

![](images/image3.jpg)  
Hình 5.2. Một số hình ảnh từ bộ cơ sở dữ liệu CIFAR-10 [9].

## Kết quả với bộ cơ sở dữ liệu MNIST

Dánh giá các thuat toán tói ru vói bo dir lieu MNIsT

![](images/image4.jpg)

Hình 5.3 Tỉ lệ mất mát của các thuật toán tối ưu trên tập dữ liệu MNIST.   



Hình $5 . 3 ~ \mathrm { m } \hat { \mathrm { { o } } }$ tả kết quả của loss function của các thuật toán, xét trên tập dữ liệu MNIST. Ở đây, sau 50 chu kì học kết quả gần như không thay đổi nên chúng tôi chỉ xét ở 30 chu kì học đầu để có cách nhìn cụ thể hơn về sự biến thiên của hàm mất mát.

Từ đồ thị, có thể nhận thấy rằng, Adam và RMSProp là 2 thuật toán có biên độ dao động thấp nhất, gần như không thay đổi quá nhiều quanh giá trị 0.5. Trong khi đó, AdaDelta và AdaGrad là hai thuật toán có sự biến động lớn nhất trong suốt các chu kì học. Bên cạnh đó, nhận thấy rằng thuật toán SGD với động lượng là thuật toán có kết quả hội tụ nhanh nhất và tốt nhất là với tỉ lệ mất mát rơi vào khoảng 0.023. Các thuật toán Adam, RMSProp và Adagrad cũng có kết quả rất tốt lần lượt là 0.06, 0.067, 0.059, thuật toán Adelta có kết quả cao nhất trong các thuật toán đang xét với tỉ lệ mất mát 0.229.

Để có cách nhìn tổng thể hơn, tỉ lệ nhận dạng đúng của mô hình với các thuật toán khác nhau cũng được mô tả ở mô hình 5.4.

![](images/image5.jpg)  
Hình 4.4 Tỉ lệ nhận dạng đúng của các thuật toán trên tập huấn luyện và tập đánh giá.

Từ hình 5.4, có thể thấy rằng tỉ lệ nhận dạng đúng của mô hình chịu sự ảnh hưởng từ các thuật toán tối ưu. Cụ thể, đối với thuật toán cho tỉ lệ mất mát cao như Adadelta hay Adagrad, tỉ lệ nhận dạng đúng khá thấp, rơi vào khoảng $9 3 . 4 \%$ trên tập đánh giá (Adadelta). Trong khi đó, các thuật toán cho tỉ lệ mất mát thấp như SGD with momentum, RMSProp và Adam cho tỉ lệ nhận dạng đúng khả quan hơn, đạt khoảng $9 9 . 2 \%$ , khi sử dụng trên cùng một mô hình kiến trúc mạng đề ra.

## Kết quả với bộ cơ sở dữ liệu CIFAR10



Để có thể đánh giá chính xác hơn về vai trò của các thuật toán, nhóm thực hiện khảo sát trên tập dữ liệu CIFAR-10, $\mathrm { c o } \ \mathrm { d } \hat { \mathbf { \mathrm { 0 } } }$ phức tạp cao hơn so với MNIST. Tương tự với bộ cơ sở dữ liệu MNIST, hình 4.6 đưa ra kết quả khảo sát từng thuật toán riêng biệt trên cùng một mô hình mạng và tập dữ liệu xét sau 50 chu kì học.

Từ đồ thị hình 5.4, nhận thấy rằng, xu hướng hội tụ của thuật toán Adadelta và Adagrad khá tốt, tuy nhiên, tỉ lệ mất mát lại khá cao, xấp xỉ 1.2 với Adagrad và 1.6 với Adadelta sau khoảng chu kì học được xét. SGD with momentum là thuật toán có kết quả khả quan hơn cả, độ hội tụ khá ổn định, giá trị thấp, đạt đỉnh 0.8 tại chu kì học 20. Tiếp đến là thuật toán Adam, tuy nhiên, nhận thấy rằng thuật toán Adam có xu hướng tăng tỉ lệ mất mát khi qua khỏi 10 chu kì học. RMSProp là thuật toán có sự dao động lớn nhất về tỉ lệ mất mát qua các chu kì học trong các thuật toán được khảo sát.

![](images/image6.jpg)  
Hình 5.4 Tỉ lệ mất mát của các thuật toán tối ưu trên tập dữ liệu CIFAR10.

Hình 5.5 cho thấy, tỉ lệ nhận dạng đúng của 2 thuật toán Adagrad và Adadelta không cao so với các thuật toán còn lại. Tuy nhiên ưu điểm là giảm được hiện tượng overfitting - hiện tượng kết quả trên tập dữ liệu huấn luyện rất cao trong khi thử nghiệm mô hình trên tập dữ liệu kiểm tra cho kết quả thấp.



![](images/image7.jpg)  
Hình 5.5 Tỉ lệ nhận dạng đúng của các thuật toán trên tập huấn luyện và tập đánh giá.

Tổng quát ta cũng có thể thấy rằng với thuật toán cho tỉ lệ mất mát cao và các thuật toán cho tỉ lệ mất mát thấp sẽ ảnh hưởng đến tỉ lệ nhận dạng đúng của mô hình, SGD with momentum và Adam là hai thuật toán có kết quả khá hứa hẹn. Cụ thể tỉ lệ nhận dạng đúng khi sử dụng các thuật toán tối ưu SGD với động lượng, RMSProp, Adagrad, Adadelta, Adam lần lượt là $7 3 . 9 \%$ , $5 7 . 3 \%$ , $5 8 . 9 \%$ , $4 4 . 5 \%$ , $7 2 . 9 \%$ .

# Kết luận

Tổng quát, kết quả từ nghiên cứu trên đã đánh giá được sự tác động của thuật toán tối ưu đến việc phân loại đúng kết quả trong bài toán nhận dạng hình ảnh. Nghiên cứu cũng cung cấp thêm hiểu biết về thuật toán tối ưu, thông qua các kết quả từ thực nghiệm đánh giá, từ đó giúp chúng ta có sự lựa chọn các thuật toán thật hợp lí trong việc xây dựng và huấn luyện, đánh giá mô hình mạng. Trong phạm vi bài báo, chúng tôi chỉ so sánh các thuật toán phổ biến và trong thực tế còn rất nhiều các thuật toán tối ưu khác. Kết quả trên chỉ so sánh và xác định ra thuật toán tối ưu nhất trong phạm vi các thuật toán được xét, đối với bộ cơ sở dữ liệu CIFAR-10 và MNIST. Một số thành phần khác như kiến trúc, các tham số, siêu tham số và các tập dữ liệu khác chúng tôi sẽ thực hiện phân tích và đánh giá ở các nghiên cứu sau.

# TÀI LIỆU THAM KHẢO

[1]. Léon Bottou, Frank E. Curtis, Jorge Nocedal (2016). Optimization Methods for Large-Scale Machine Learning, arXiv:1606.04838



[2]. Jonathan T. Barron (2017). A General and Adaptive Robust Loss Function, arXiv:1701.03077, Cornell University

[3]. Qian, N. (1999). On the momentum term in gradient descent learning algorithms. Neural Networks: The Official Journal of the International Neural Network Society, 12(1), 145–151. http://doi.org/10.1016/S0893- 6080(98)00116-6

[4]. Sutskever, I., Martens, J., Dahl, G.E. and Hinton, G.E. (2013). On the importance of initialization and momentum in deep learning. ICML (3), Vol 28, pp. 1139—1147

[5]. Christian Igel and Michael H ̈usken (2000). Improving the RMSprop Learning Algorithm. http://citeseerx.ist.psu.edu/viewdoc/summary?doi $\equiv$ 10.1.1.17.1332

[6]. Alexandre Défossez, Léon Bottou, Francis Bach, Nicolas Usunier (2020). On the Convergence of Adam and Adagrad, arXiv:2003.02395 [7]. Matthew D. Zeiler (2012), Adadelta: An Adaptive Learning Rate Method, arXiv:1212.5701v1 [cs.LG] 22 Dec 2012

[8]. Yann LeCun, Courant Institute (1989). The MNIST Database of Handwritten Digits.

[9]. Alex Krizhevsky, Vinod Nair and Geoffrey Hinton (2009). The CIFAR-10 dataset

# Public_117 

# Random variables

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



Chú ý: Nếu x là biến ngẫu nhiên rời rạc, p(x) luôn luôn nhỏ hơn hoặc bằng 1. Trong khi đó, nếu x là biến ngẫu nhiên liên tục, p(x) có thể nhận giá trị dương bất kỳ, điều này vẫn đảm bảo là tích phân của hàm mật độ xác suất theo toàn bộ giá trị có thể có của x bằng 1. Với biến ngẫu nhiên rời rạc, p(x) được hiểu là mật độ xác suất tại x.

# Joint probability

Xét hai biến ngẫu nhiên x và y. Nếu ta quan sát rất nhiều cặp đầu ra của x và y, thì có những tổ hợp hai đầu ra xảy ra thường xuyên hơn những tổ hợp khác. Thông tin này được biểu diễn bằng một phân phối được gọi là joint probability của x và y, và được viết là p(x, y). Dấu phẩy trong p(x, y) có thể đọc là và, vậy $\mathfrak { p } ( \mathrm { x } , \mathrm { y } )$ là xác suất của x và y. x và y có thể là hai biến ngẫu nhiên rời rạc, liên tục, hoặc một rời rạc, một liên tục. Luôn nhớ rằng tổng các xác suất trên mọi cặp giá trị có thể xảy ra (x, y) bằng 1.

both are discrete: $\begin{array} { r l } { { } } & { { } \sum _ { - } \{ \mathrm { x } , \mathrm { y } \} ~ \mathrm { p } ( \mathrm { x } , \mathrm { y } ) = 1 } \\ { { } } & { { } \mathrm { s } : ~ \iint _ { \mathbb { P } } ( \mathrm { x } , \mathrm { y } ) \mathrm { d } \mathrm { x } ~ \mathrm { d } \mathrm { y } = 1 } \end{array}$   
both are continuou   
x is discrete, y is continuous: $\begin{array} { r } { \sum _ { - } \mathbf { x } \int \mathbf { p } ( \mathbf { x } , \mathbf { y } ) \mathrm { d } \mathbf { y } = \int \left( \sum _ { - } \mathbf { x } \mathbf { p } ( \mathbf { x } , \mathbf { y } ) \right) \mathrm { d } \mathbf { y } = 1 } \end{array}$ Thông thường, chúng ta sẽ làm việc với các bài toán $\dot { \mathbf { O } }$ đó joint probability xác định trên nhiều hơn 2 biến ngẫu nhiên. Chẳng hạn, $\mathsf { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } )$ thể hiện joint probability của 3 biến ngẫu nhiên x, y và z. Khi có nhiều biến ngẫu nhiên, ta có thể viết chúng dưới dạng vector. Ta có thể viết $\mathfrak { p } ( \mathbf { x } )$ để thể hiện joint probability của biến ngẫu nhiên nhiều chiều $\mathrm { \bf x } = [ \mathrm { x } 1 , \mathrm { x } 2 , . . . , \mathrm { x n } ] ^ { \wedge } \mathrm { T } .$ Khi có nhiều tập các biến ngẫu nhiên, ví dụ x và y, ta có thể viết $\mathfrak { p } ( \mathrm { x } , \mathrm { y } )$ để thể hiện joint probability của tất cả các thành phần trong hai biến ngẫu nhiên nhiều chiều này.

# Marginalization

Nếu biết joint probability của nhiều biến ngẫu nhiên, ta cũng có thể xác định được phân bố xác suất của từng biến bằng cách lấy tổng (rời rạc) hoặc tích phân (liên tục) theo tất cả các biến còn lại:

$\begin{array} { r } { \mathsf { p } ( \mathbf { x } ) = \sum \_ { \mathbf { y } } \mathsf { p } ( \mathbf { x } , \mathbf { y } ) } \end{array}$ (3) $\begin{array} { r } { \mathsf { p } ( \mathsf { y } ) = \sum _ { - } \mathbf { x } \mathsf { p } ( \mathbf { x } , \mathsf { y } ) } \end{array}$ (4) Và với biến liên tục: $\mathsf { p } ( \mathbf { x } ) = \int \mathsf { p } ( \mathbf { x } , \mathbf { y } ) \mathrm { d } \mathbf { y }$ (5)



$\mathsf { p } ( \mathsf { y } ) = \boldsymbol { \int } \mathsf { p } ( \mathbf { x } , \mathsf { y } ) \mathrm { d } \mathbf { x }$ (6)

Với nhiều biến hơn, chẳng hạn 4 biến rời rạc x, y, z, w:

$$
\begin{array} { r } { \mathrm { p ( x ) } = \sum _ { \mathrm { - } } \{ \mathrm { y , z , w } \} \ \mathrm { p ( x , y , z , w ) } } \end{array}
$$

$$
\begin{array} { r } { \mathrm { p } ( \mathrm { x } , \mathrm { y } ) = \sum _ { - } \{ \mathrm { z } , \mathrm { w } \} \ \mathrm { p } ( \mathrm { x } , \mathrm { y } , \mathrm { z } , \mathrm { w } ) } \end{array}
$$

Từ đây trở đi, nếu không nói gì thêm, tôi sẽ dùng ký hiệu ∑ để chỉ chung cho cả hai loại biến. Nếu biến ngẫu nhiên là liên tục, bạn đọc ngầm hiểu rằng dấu $\sum$ cần được thay bằng dấu tích phân ∫, biến lấy vi phân chính là biến được viết dưới dấu ∑.

# Conditional probability

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

# Quy tắc Bayes

$$
\begin{array} { r l } & { \mathrm { T i r } \left( 1 1 \right) : \mathrm { p ( y \mid x ) p ( x ) } = \mathrm { p ( x \mid y ) p ( y ) } \Rightarrow \mathrm { p ( y \mid x ) } = \mathrm { p ( x \mid y ) p ( y ) / p ( x ) } } \\ & { = \mathrm { p ( x \mid y ) p ( y ) } / \sum \mathrm { y p ( x , y ) } \quad \mathrm { ( 1 6 ) } } \\ & { = \mathrm { p ( x \mid y ) p ( y ) } / \sum \mathrm { y p ( x \mid y ) p ( y ) } \quad \mathrm { ( 1 7 ) } } \end{array}
$$

Ba công thức (15)–(17) thường được gọi là Quy tắc Bayes (Bayes’ rule).

# Independence

Nếu x và y độc lập: $\mathsf { p } ( \mathbf { x } \mid \mathbf { y } ) = \mathsf { p } ( \mathbf { x } )$ (18), $\mathsf { p } ( \boldsymbol { \mathrm { y } } \mid \boldsymbol { \mathrm { x } } ) = \mathsf { p } ( \boldsymbol { \mathrm { y } } )$ Khi đó: $\mathtt { p ( x , y ) } = \mathtt { p ( x ) } \mathtt { p ( y ) }$ (20)

7. Kỳ vọng



Kỳ vọng (expectation) của một biến ngẫu nhiên:

$\begin{array} { r } { \operatorname { E } [ \mathbf { x } ] = \sum _ { - } ^ { } \mathbf { x } \mathbf { x } \mathbf { p } ( \mathbf { x } ) } \end{array}$ nếu x rời rạc (21)   
$\operatorname { E } [ \mathbf { x } ] = \int \mathbf { x } \ \mathbf { p } ( \mathbf { x } ) \ \mathrm { d } \mathbf { x }$ nếu x liên tục (22)   
Với hàm $\begin{array} { r } { \mathrm { f ( . ) } { \mathrm { : ~ E [ f ( x ) ] } } = \sum _ { - } { \mathrm { ~ x ~ f ( x ) ~ p ( x ) ~ } } } \end{array}$ (23)   
Với joint probability: $\begin{array} { r } { \mathrm { E } [ \mathrm { f } ( \mathrm { x } , \mathrm { y } ) ] = \sum _ { - } \{ \mathrm { x } , \mathrm { y } \} \ \mathrm { f } ( \mathrm { x } , \mathrm { y } ) \ \mathrm { p } ( \mathrm { x } , \mathrm { y } ) } \end{array}$ Ba quy tắc:   
$\operatorname { E } [ { \mathfrak { a } } ] = { \mathfrak { a } }$ (25)   
$\operatorname { E } [ { \mathfrak { a } } \mathbf { x } ] = \mathbf { a } \operatorname { E } [ \mathbf { x }$ (26); $\operatorname { E } [ \mathbf { f } ( \mathbf { x } ) + \mathbf { g } ( \mathbf { x } ) ] = \operatorname { E } [ \mathbf { f } ( \mathbf { x } ) ] + \operatorname { E } [ \mathbf { g } ( \mathbf { x } ) ]$ Nếu x, y độc lập: $\operatorname { E } [ \operatorname { f } ( \mathbf { x } ) \ \mathbf { g } ( \mathbf { y } ) ] = \operatorname { E } [ \operatorname { f } ( \mathbf { x } ) ] \operatorname { E } [ \mathbf { g } ( \mathbf { y } ) ]$ (28)

8. Một vài phân phối thường gặp

## Bernoulli distribution

Bernoulli distribution: $\mathbf { x } \in \{ 0 , 1 \}$ , tham $\mathrm { s } \acute { 0 } \lambda \in [ 0 , 1 ]$ là xác suất để $\mathbf { x } { = } 1$

${ \mathrm { p } } ( { \mathrm { x } } { = } 1 ) { = } \lambda , \quad { \mathrm { p } } ( { \mathrm { x } } { = } 0 ) { = } 1 - \lambda$ Viết gọn: $\mathrm { p ( x ) } = \lambda \mathrm { \hat { x } } \left( 1 - \lambda \right) \mathrm { \hat { \Omega } } \{ 1 - \mathrm { x } \}$ Ký hiệu: $\mathsf { p } ( \mathrm { x } ) = \mathrm { B e r n } \_ \mathrm { x } [ \lambda ]$ (30)

## Categorical distribution

Categorical distribution với K lớp, tham $\mathrm { s } \mathring { \hat { 0 } } \lambda = [ \lambda 1 , . . . , \lambda \mathrm { K } ] , \sum _ { - } \mathrm { k } \lambda \mathrm { k } = 1 .$

$\mathsf { p } ( \mathbf { x } = \mathbf { k } ) = \lambda \big \mathrm { ~ k ~ }$ ; viết gọn: $\mathsf { p } ( \mathrm { x } ) = \mathrm { C a t \_ x } [ \lambda ]$ Biểu diễn one-hot: $\mathrm { x } \in \{ \mathrm { e l } , . . . , \mathrm { e K } \}$ ${ \mathrm { p } } ( \mathbf { x } = { \mathbf { e } } \bot ) = \prod  \mathrm { ~ \{ j = 1 \} ~ \cdot K ~ \land ~ j ~ \land ~ j \} } = \lambda { \mathrm { ~ \bf ~ k ~ } }$

## Univariate normal distribution

$\mathrm { p } ( \mathrm { x } ) = 1 / \sqrt { ( 2 \pi \sigma ^ { \wedge } 2 ) \cdot \exp ( - { \left( \mathrm { x } - \mu \right) ^ { \wedge } } 2 / ( 2 \sigma ^ { \wedge } 2 ) ) }$ (3 Ký hiệu: $\mathtt { p } ( \mathrm { x } ) = \mathrm { N o r m \_ x } [ \mu , \sigma ^ { \wedge } 2 ]$

8.4 Multivariate normal distribution   
$\mathrm { p ( x ) } = 1 / \left( ( 2 \pi ) ^ { \wedge } \{ \mathrm { D } / 2 \} \right.$ |Σ|^{1/2}) · exp(−1/2 (x−μ)^T Σ^{−1} (x−μ))   
Ký hiệu: $\mathtt { p ( x ) } = \mathtt { N o r m \_ x [ \mu , \Sigma ] }$

## Beta distribution

$\mathrm { p ( \boldsymbol { \lambda } ) } = \Gamma ( \alpha + \beta ) / \left( \Gamma ( \alpha ) \Gamma ( \beta ) \right) \cdot \lambda \wedge \{ \alpha - 1 \} \ ( 1 - \lambda ) ^ { \wedge } \{ \beta - 1 \}$ (34) Trong đó $\Gamma ( \mathrm { z } ) = \int \_ 0 \land _ { \infty } { \mathrm { t } } \land \{ \mathrm { z }  - 1 \} \ \exp ( - \mathrm { t } )$ dt, và $\Gamma [ z ] = ( z - 1 ) !$ nếu $\mathbf { Z }$ là số tự nhiên.

Ký hiệu: $\mathsf { p } ( \lambda ) = \mathbf { B e t a } \_ \lambda [ \mathsf { a } , \mathsf { \beta } ]$



## Dirichlet distribution

p(λ1, …, λK) = Γ(∑_{k=1}^K α_k) / ∏_{k=1}^K Γ(α_k) · ∏_{k=1}^K   
$\lambda \stackrel { \mathrm { \scriptsize ~ k } ^ { \wedge } } { - } \stackrel { \textstyle \left\{ { \mathfrak { a } \stackrel { \mathrm { \scriptsize ~ k } ^ { - 1 } } { \mathfrak { a } } } \right\} }$ (35)   
Ký hiệu: $\mathrm { p } ( \mathbb { A } 1 , . . . , \mathbb { A } \mathrm { K } ) = \mathrm { D i r } _ { - } \{ \lambda 1 , . . . , \lambda \mathrm { K } \} [ \alpha 1 , . . . , \alpha \mathrm { K } ]$

# Thảo luận

Về Xác suất thống kê, còn rất nhiều điều cần lưu ý. Tạm thời, phần này ôn tập lại các kiến thức xác suất cơ bản để phục vụ cho các bài viết tiếp theo. Khi nào có phần nào cần nhắc lại, sẽ tiếp tục ôn tập bổ sung.

# Public_118 

# Giới thiệu

Dimensionality Reduction (giảm chiều dữ liệu) là một kỹ thuật quan trọng trong Machine Learning. Dữ liệu thực tế có thể có số chiều rất lớn (hàng nghìn). Việc giảm chiều giúp tiết kiệm lưu trữ, tăng tốc tính toán và có thể coi như nén dữ liệu. Một phương pháp tuyến tính cơ bản là Principal Component Analysis (PCA).

# Một chút toán

## Norm 2 của ma trận

$$
\left\| \mathbf { A } \right\| _ { - } 2 = \operatorname* { m a x } _ { - } \mathbf { x } \left\| \mathbf { A x } \right\| _ { - } 2 / \left\| \mathbf { x } \right\| _ { - } 2
$$

$$
\| \mathbf { A } \| _ { - } 2 = \operatorname* { m a x } _ { - } \{ | \mathbf { x } | | _ { - } 2 { = } 1 \} \| \mathbf { A x } \| _ { - } 2
$$

Giải bằng nhân tử Lagrange cho thấy norm 2 của ma trận chính là singular value lớn nhất của A. Vector tương ứng là right-singular vector của A.

## Biểu diễn vector trong các hệ cơ sở khác nhau

$$
\mathbf { x } = \mathbf { U } \mathbf { y } , \mathbf { y } = \mathbf { U } ^ { \wedge } \{ - 1 \} \mathbf { x }
$$

Nếu U trực giao: $\mathrm { U } ^ { \wedge } \{ - 1 \} { = } \mathrm { U } ^ { \wedge } \mathrm { T }$ , do đó $\mathbf { y } = \mathbf { U } \mathbf { \land } \mathbf { T } \mathbf { x }$

## Trace

Một số tính chất: - trace(A) $=$ trace(A^T) - trace $( \mathrm { k A } ) = \mathrm { k }$ trace(A) - trace $( \mathrm { A B } ) =$ trace(BA) - $\cdot \| \mathbf { A } \| \_ { \Gamma ^ { \wedge } 2 } =$ trace(A^T A) - trace $( \mathbf { A } ) =$ tổng các trị riêng của A

## Kỳ vọng và ma trận hiệp phương sai

Một chiều: $\bar { \mathbf { x } } = \left( 1 / \mathrm { N } \right) \boldsymbol { \Sigma } \mathbf { x } \mathrm { ~ \underline { { ~ n ~ } } ~ }$ , $\sigma ^ { \wedge } 2 = ( 1 / \mathrm { N } ) \Sigma ( \mathrm { x } \underset { - } { \mathrm { ~ n } } - \bar { \mathrm { x } } ) { \overset { \wedge } { \wedge } } 2$ Đa chiều: $\bar { \mathbf { x } } = ( 1 / \mathrm { N } ) \Sigma \mathbf { x } \underline { { \mathrm { ~ n ~ } } }$ , $\mathbf { S } = ( 1 / \mathrm { N } )$ (X − x̄ 1^T)(X − x̄ 1^T)^T

# Principal Component Analysis (PCA)

Mục tiêu: Tìm hệ cơ sở trực chuẩn sao cho phương sai dữ liệu tập trung ở K thành phần đầu.

Dữ liệu chuẩn hoá: ${ \dot { \mathbf { X } } } = { \mathbf { X } } - { \bar { \mathbf { x } } } { \mathbf { l } } \cdot { \mathbf { \Omega } } { \mathbf { T } }$ Ma trận hiệp phương sai: $\mathbf { S } = ( 1 / \mathrm { N } ) \dot { \mathrm { X } } \dot { \mathrm { X } } \mathrm { \hat { T } }$



Hàm mất mát: $\mathbf { J } = \Sigma \ \{ \mathrm { i } \mathrm { = K } { + } 1 \} \wedge \mathrm { D } \ \mathrm { u } \ \underline { { \mathrm { i } } } { \wedge } \mathrm { T } \ \mathrm { S } \ \mathrm { u } \ \underline { { \mathrm { i } } }$ Tối ưu tương đương chọn $\mathrm { K }$ vector riêng ứng với K trị riêng lớn nhất của S.

# Các bước PCA

Tính kỳ vọng x̄ - Chuẩn hoá dữ liệu: ${ \dot { \mathbf { X } } } = { \mathbf { X } } - { \bar { \mathbf { x } } } { \mathbf { l } } \cdot { \mathbf { \Omega } } { \mathbf { T } }$ Tính ma trận hiệp phương sai S Tính trị riêng & vector riêng, sắp xếp $\lambda$ giảm dần Chọn K vector riêng lớn nhất $ \mathrm { ~ U ~ } \underline { { \mathrm { ~ K ~ } } }$ Tính toạ độ mới: $Z = \mathrm { U } \_ { \mathrm { R } } \mathrm { \tiny { \wedge } } \mathrm { T } \dot { X }$ Xấp xỉ khôi phục: $\mathbf { x } \approx \mathbf { U } \subset \mathbf { K } \subset + { \bar { \mathbf { x } } }$

# Public_119 

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

# Public_120 

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

# Public_121 

# Phương pháp đánh giá các mô hình phân lớp đa nhãn

Để đánh giá các mô hình phân lớp đa nhãn MLL, khóa luận đã sử dụng phương pháp $\mathrm { k }$ -fold cross validation tập dữ liệu ban đầu được chia ngẫu nhiên thành k tập con (fold) có kích thước xấp xỉ nhau S1, S2 … Sk. Quá trình học và kiểm tra được thực hiện tại k lần. Tại lần lặp thứ i, Si là tập dữ liệu kiểm tra, các tập còn lại hợp thành dữ liệu huấn luyện. Có nghĩa là, đầu tiên chạy được thực hiện trên tập S2, S3 … Sk, sau đó test trên tập S1; tiếp tục quá trình dạy được thực hiện trên tập S1, S3, S4 … Sk, sau đó test trên tập S2; và cứ tiếp tục như thế.

Ví dụ, ${ \mathrm { k } } = 1 0$ , thì phương pháp $\mathrm { k \Omega }$ -fold cross validation được minh họa như hình dưới:

Bảng minh họa phương pháp k-fold cross validation   



# Một số độ đo để đánh giá mô hình phân lớp đa nhãn

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



Xét ví dụ:

Giả sử có có 5 đối tượng được xếp hạng tương ứng là: c, a, e, b, d Một xếp hạng của đối tượng cần đánh giá là: c, a, e, d, b

Khi đó, $^ { \circ } ( \underline { { \omega } } 1 = 1 / 1 , \mathrm { P } @ 2 = 2 / 2 , \mathrm { P } @ 3 = 3 / 3 , \mathrm { P } @ 4 = 3 / 4 , \mathrm { P } @ 5 = 3 / 5 .$

$$
\begin{array} { l } { { \displaystyle \mathrm { A P } = ( \frac 1 1 + \frac 2 2 + \frac { 3 } { 3 } ) } } \\ { { \mathrm { M A P } = \ \frac { 1 } { 3 } ( \frac 1 { 1 } + \frac { 2 } { 2 } + \ \frac { 3 } { 3 } ) } } \end{array}
$$

# Public_122 

# Giới thiệu

Động lực của nghiên cứu xuất phát từ những hạn chế của các phương pháp hiện tại trong việc xử lý các điều kiện ánh sáng phức tạp trong thực tế. Hình ảnh được chụp trong các bối cảnh đa dạng thường gặp phải tình trạng phơi sáng không đồng đều do sự thay đổi của ánh sáng, sự hiện diện của nhiều nguồn sáng, hoặc độ tương phản mạnh giữa các vùng sáng và tối. Các phương pháp truyền thống, như histogram equalization và tone mapping thường dựa trên các mô hình chiếu sáng toàn cục hoặc đơn giản, dẫn đến việc không khôi phục được các chi tiết quan trọng ở cả vùng thừa sáng và thiếu sáng, đặc biệt là trong các cảnh có điều kiện ánh sáng phức tạp.

Các phương pháp deep learning gần đây đã cải thiện đáng $\mathrm { k } \mathring { \mathrm { e } }$ hiệu năng hiệu chỉnh độ phơi sáng so với các phương pháp truyền thống. Tuy nhiên, hầu hết các mô hình này giả định ánh sáng đồng nhất và không xử lý được sự tương tác giữa nhiều nguồn sáng, điều rất phổ biến trong các cảnh tự nhiên. Tương tự, các mô hình chiếu sáng dựa trên vật lý chủ yếu tập trung vào một nguồn sáng duy nhất, khiến chúng khó áp dụng hiệu quả trong thực tế khi có nhiều nguồn chiếu sáng.

Nghiên cứu này nhằm giải quyết các hạn chế trên bằng cách đề xuất Dual Illumination Estimation. Ý tưởng cốt lõi là mô hình hóa và ước lượng đồng thời hai nguồn sáng chính và phụ, cho phép hiệu chỉnh độ phơi sáng một cách thích ứng và chi tiết trong các điều kiện ánh sáng đa dạng. Phương pháp này không chỉ nâng cao chất lượng hình ảnh được hiệu chỉnh mà còn cung cấp một giải pháp tiền xử lý mạnh mẽ cho các ứng dụng trong nhiếp ảnh, thị giác máy tính, và xử lý ảnh tự động. Bằng cách giải quyết khoảng trống trong các phương pháp hiện có, nghiên cứu kỳ vọng sẽ thiết lập một tiêu chuẩn mới trong hiệu chỉnh độ phơi sáng cho các môi trường phức tạp trong thực tế.

# Mô tả thuật toán

Với một hình ảnh đầu vào, trước tiên quá trình ước lượng chiếu sáng kép (dual illumination estimation) được thực hiện để thu được các ánh sáng tiến (forward illumination) và ngược (reverse illumination). Từ đó, hình ảnh được hiệu chỉnh độ phơi sáng trung gian cho các trường hợp thiếu sáng (underexposure) và thừa sáng (overexposure) sẽ được khôi phục. Tiếp theo, một phương pháp hòa trộn hình ảnh hiệu chỉnh đa phơi sáng (multi-exposure image fusion) hiệu quả sẽ được áp dụng để kết hợp liền mạch các phần được phơi sáng tốt nhất từ hai hình ảnh hiệu chỉnh phơi sáng trung gian, cũng như hình ảnh đầu vào, thành một hình ảnh cuối cùng được phơi sáng đồng đều trên toàn cầu.



![](images/image1.jpg)  
Tổng quan về thuật toán hiệu chỉnh độ phơi sáng được đề xuất.

## Ước lượng chiếu sáng kép (Dual Illumination Estimation)

Phần này mô tả chi tiết kỹ thuật ước lượng chiếu sáng kép. Mục tiêu là ước lượng hai bản đồ chiếu sáng bổ sung: ánh sáng tiến Lf và ánh sáng ngược Lr. Các bản đồ này cho phép hiệu chỉnh các vùng thiếu sáng và thừa sáng của ảnh đầu vào một cách hiệu quả.

Cho ảnh đầu vào I được biểu diễn trong không gian màu RGB với các giá trị cường độ pixel được chuẩn hóa trong khoảng [0,1]. Phương pháp ước lượng chiếu sáng kép dựa trên quan sát rằng có thể tạo ra các ánh sáng bổ sung để cải thiện các vùng phơi sáng khác nhau của ảnh:

1. Chiếu sáng tiến Lf: Làm nổi bật và cải thiện các vùng tối hoặc thiếu sáng.   
2. Chiếu sáng ngược $\mathrm { L } _ { \mathrm { r } }$ : Tập trung làm giảm các vùng bị thừa sáng.

Quá trình ước lượng Lf và $\mathrm { L } _ { \mathrm { r } }$ được thực hiện qua các bước sau:

# Bước 1: Ảnh đảo ngược

Để tạo ra ánh sáng ngược, ảnh đầu vào III được đảo ngược:

$$
\tilde { I _ { i n v } } ^ { \mathrm { C } ^ { \mathrm { B } } } = 1 - I
$$

Phép đảo ngược này thực chất lật các mức cường độ sáng, làm cho các vùng bị thừa sáng trở nên giống như thiếu sáng.

# Bước 2: Mô hình chiếu sáng

Các bản đồ chiếu sáng được ước lượng bằng cách giải các bài toán tối ưu hóa cho cả Lf và Lr. Các bản đồ này dựa trên mô hình Retinex, tách ảnh thành thành phần phản xạ và chiếu sáng:

$$
I = R \odot L
$$



Trong đó R là phần phản xạ và L là phần chiếu sáng. Framework dual illumination tính toán $\mathrm { L } _ { \mathrm { f } }$ và $\mathrm { L } _ { \mathrm { r } }$ bằng cách áp dụng các ràng buộc về độ mượt (smoothness) và tính trung thực (fidelity).

Chiếu sáng tiến Lf:

$$
L _ { r } = a r g \operatorname* { m i n } _ { L } \lVert I - L \odot R \rVert ^ { 2 } + \lambda \Phi ( \mathrm { L } )
$$

trong đó:

1.1. $\Phi ( \mathrm { L } )$ là độ mượt (v.d. Total Variation)   
1.2. ?? là tham số điều chỉnh mức độ của ràng buộc độ mượt.

# Chiếu sáng ngược $\mathbf { L _ { r } }$

Ánh sáng ngược được tính toán tương tự từ ảnh đảo ngược $\operatorname { I } _ { \mathrm { i n v } }$

$$
L _ { r } = a r g \operatorname* { m i n } _ { L } \lVert I _ { i n v } - L \odot R \rVert ^ { 2 } + \lambda \Phi \left( \mathrm { L } \right)
$$

# Bước 3: Ước lượng số học

Các bài toán tối ưu hóa trên được giải theo phương pháp gradient-based, đảm bảo rằng các bản đồ ánh sáng thu được mượt mà đồng thời nắm bắt chính xác điều kiện ánh sáng của ảnh đầu vào.

# Bước 4: Lọc mịn

Để đảm bảo tính nhất quán giữa Lf và Lr, kỹ thuật lọc song phương (bilateral filtering) được áp dụng. Phương pháp này làm mịn các bản đồ chiếu sáng trong khi vẫn bảo toàn các chi tiết tại biên. Cuối cùng, các bản đồ ánh sáng được chuẩn hóa để đảm bảo tương thích với các bước tiếp theo trong pipeline.

# Mã giả:

Input: Image I   
Output: Forward Illumination L_f, Reverse Illumination L_r   
1. Compute inverted image: I_inv $= 1 - 1$   
2. Initialize $\mathsf { L } \_ { \mathsf { f } } , \mathsf { L } \_ { \mathsf { r } }$ (e.g., with uniform values)   
3. While not converged: a. Update L_f: $\mathsf { L } _ { - } \mathsf { f } = \mathsf { a r g m i n } \mid \mid \mathsf { I } - \mathsf { L } _ { - } \mathsf { f } ^ { \ast } \mathsf { R } \mid \mid \mathsf { \Lambda } ^ { 2 } + \lambda ^ { \ast } \mathsf { S m o o t h n e s s } ( \mathsf { L } _ { - } \mathsf { f } )$ b. Update L_r: $=$ $\mathsf { a r g m i n } | | \mathsf { l } | \mathsf { i n v - L } _ { - } \mathsf { r } ^ { * } \mathsf { R } \mid | \mathsf { \Lambda } 2 + \lambda ^ { * } \mathsf { S m o o t h n e s s } ( \mathsf { L } _ { - } \mathsf { r } )$ c. Apply bilateral filter to L_f, L_r   
4. Normalize L_f, L_r

## Trộn đa hình ảnh phơi sáng (Multi-Exposure Image Fusion)

Phần này mô tả chi tiết kỹ thuật hòa trộn hình ảnh đa phơi sáng. Mục tiêu của bước này là kết hợp liền mạch các phần được phơi sáng tốt nhất từ các hình ảnh



đã hiệu chỉnh (underexposure-corrected và overexposure-corrected) và ảnh đầu vào để tạo ra một hình ảnh cuối cùng có độ phơi sáng đồng đều trên toàn cầu. Cho các hình ảnh đầu vào:

Iu: Hình ảnh đã được hiệu chỉnh vùng thiếu sáng (underexposure-corrected).   
Io: Hình ảnh đã được hiệu chỉnh vùng thừa sáng (overexposure-corrected).   
I: Ảnh gốc.

Nhiệm vụ là hợp nhất Iu, Io, và I sao cho các vùng được chọn từ mỗi ảnh có độ phơi sáng tối ưu nhất. Quá trình này được thực hiện dựa trên các bản đồ trọng số cục bộ (weight maps) để chỉ định vùng nào sẽ được lấy từ mỗi hình ảnh.

# Bước 1: Tạo bản đồ trọng số cục bộ

Bản đồ trọng số W được tính toán cho từng hình ảnh Iu, Io, và I. Các trọng số này được thiết $\mathrm { k } \acute { \mathrm { e } }$ để phản ánh chất lượng phơi sáng cục bộ của từng vùng. Công thức tính trọng số thường dựa trên các đặc trưng như độ tương phản, độ sắc nét và độ sáng cục bộ:

$$
W _ { x } ( p ) = C o n t r a s t ( p ) \cdot S h a r p n e s s ( p ) \cdot S a t u r a t i o n ( p )
$$

Trong đó:

1.3. Contrast(p): Đo lường độ tương phản tại điểm ảnh p. 1.4. Sharpness(p): Đánh giá độ sắc nét bằng cách sử dụng các bộ lọc gradient. 1.5. Saturation(p): Đo mức độ bão hòa màu tại p.

Các bản đồ trọng số được chuẩn hóa để đảm bảo tổng trọng số tại mỗi điểm ảnh bằng 1:

$$
I _ { f } ( p ) = \sum _ { x } \widehat { W } _ { x } ( p ) \cdot I _ { x } ( p ) , x \in \{ I _ { u } , I _ { o } , I \}
$$

Quá trình này đảm bảo rằng mỗi điểm ảnh trong hình ảnh cuối cùng được lấy từ nguồn có chất lượng phơi sáng tốt nhất.

# Bước 3: Tăng độ mượt

Để đảm bảo tính liên tục và không gây ra hiện tượng đường biên giữa các vùng được chọn từ các hình ảnh khác nhau, các bản đồ trọng số được làm mượt bằng bộ lọc Gaussian hoặc bộ lọc song phương trước khi sử dụng trong bước hòa trộn.

# Mã giả:

Input: I_u (underexposure-corrected image), I_o (overexposure-corrected image), I (original image)   
Output: Final globally well-exposed image I_f



1. Compute local weight maps:

W_ $\lambda =$ Contrast(I_u) \* Sharpness(I_u) \* Saturation(I_u) W_o $=$ Contrast(I_o) \* Sharpness(I_o) \* Saturation(I_o) W_orig $=$ Contrast(I) \* Sharpness(I) \* Saturation(I)

2. Normalize weights:

W $\underline { { \mathbf { \Pi } } } \mathsf { u } = \mathsf { W \_ u } / \left( \mathsf { W \_ u } + \mathsf { W \_ o } + \mathsf { W \_ o r i g } \right)$ $\mathcal { N } _ { - } { \sf 0 } = \sf W _ { - } { \sf 0 } / ( \mathsf { W } _ { - } { \sf u } + \mathsf { W } _ { - } { \sf 0 } + \mathsf { W } _ { - }$ orig) $\mathsf { W \_ o r i g } = \mathsf { W \_ o r i g } / \left( \mathsf { W \_ u } + \mathsf { W \_ o } + \mathsf { W \_ o r i g } \right)$

3. Smooth weight maps using Gaussian filter:

W_u $1 =$ GaussianFilter(W_u) W_o $=$ GaussianFilter(W_o) W_orig $=$ GaussianFilter(W_orig)

4. Fuse images:

$$
\mathsf { \Pi } _ { \_ } \mathsf { f } = \mathsf { W } \_ { \mathsf { U } } * \mathsf { \Pi } _ { \_ } \mathsf { u } + \mathsf { W } \_ { 0 } * \mathsf { \Pi } _ { \mathsf { - } } \mathsf { 0 } + \mathsf { W } \_ { 0 } \mathsf { r i g } * \mathsf { I }
$$

# Public_123 

# Giới thiệu tích chập

Tích chập là một khái niệm trong xử lý tín hiệu số nhằm biến đổi thông tin đầu vào thông qua một phép tích chập với bộ lọc để trả về đầu ra là một tín hiệu mới. Tín hiệu này sẽ làm giảm những đặc trưng mà bộ lọc không quan tâm và chỉ giữ những đặc trưng chính.

Tích chập thông dụng nhất là tích chập 2 chiều được áp dụng trên ma trận đầu vào và ma trận bộ lọc 2 chiều. Phép tích chập của một ma trận $\dot { \mathbf { X } } \in \mathbb { R } ^ { W _ { 1 } \times \check { H } _ { 1 } }$ với một bộ lọc (receptive field) $\mathbf { F } \in \mathbb { R } ^ { F \times F }$ là một ma trận $\mathbf { Y } \in \mathbb { R } ^ { W _ { 2 } \times H _ { 2 } }$

Trong một mạng nơ ron tích chập, các tầng (layer) liền sau lấy đầu vào từ tầng liền trước nó. Do đó để hạn chế lỗi trong thiết $\mathrm { k } \acute { \mathrm { e } }$ mạng nơ ron chúng ta cần xác định kích thước đầu ra ở mỗi tầng. Điều đó có nghĩa là dựa vào kích thước ma trận đầu vào (W1, H1), kích thước bộ lọc (F,F) và bước nhảy S để xác định kích thước ma trận đầu ra (W2, H2)   
Xét quá trình trượt trên chiều W1 của ma trận đầu vào.

![](images/image1.jpg)

Hình 1: Quá trình trượt theo chiều rộng w1. Mỗi dòng tương ứng với một bước. Mỗi bước chúng ta dịch sang phải một khoảng s đơn vị cho tới khi đi hết w1 ô. Nếu bước cuối cùng bị dư thì chúng ta sẽ lát (padding) thêm để mở rộng ma trận sao cho quá trình tích chập không bị dư ô.

Giả sử quá trình này sẽ dừng sau w2 bước. Tại bước đầu tiên ta đi được đến vị trí thứ F . Sau mỗi bước liền sau sẽ tăng so với vị trí liền trước là S. Như vậy đến bước thứ i quá trình trượt sẽ đi đến vị trí $\mathrm { F } + ( \mathrm { i } { - } 1 ) \mathrm { S }$ . Suy ra tại bước cuối cùng w2 ma trận sẽ đi đến vị trí $\mathrm { F } + ( \mathrm { W } 2 \mathrm { - } 1 ) \mathrm { S }$ . Đây là vị trí lớn nhất gần với vị trí cuối cùng là w1 . Trong trường hợp lý tưởng thì $\mathrm { F } + ( \mathrm { W } 2 $ - 1)S. Từ đó ta suy ra:



$$
W _ { 2 } = \frac { W _ { 1 } - F } { S } + 1
$$

Khi vị trí cuối cùng không trùng với w1 thì số bước w2 sẽ được lấy phần nguyên:

$$
W _ { 2 } = \qquad \frac { W _ { 1 } - F } { S } + 1
$$

Chúng ta luôn có thể tạo ra đẳng thức (1) nhờ thêm phần đường viền (padding) tại các cạnh của ảnh với độ rộng viền là P sao cho phép chia cho S là chia hết. Khi đó:

$$
W _ { 2 } = \frac { W _ { 1 } + 2 P - F } { S } + 1
$$

![](images/image2.jpg)

Hình 2: Thêm padding kích thước P vào $2 1 { \dot { \hat { \mathbf { e } } } }$ chiều rộng (W1) Hoàn toàn tương tự ta cũng có công thức ứng với chiều cao:

$$
H _ { 2 } = \frac { H _ { 1 } + 2 P - F } { S } + 1
$$

# Mạng nơ ron tích chập (mạng CNN)

## Các Thuật ngữ

Do bài này khá nhiều thuật ngữ chuyên biệt trong mạng CNN nên để dễ hiểu hơn cho bạn đọc tôi sẽ diễn giải trước khái niệm.

- Đơn vị (Unit): Là giá trị của một điểm nằm trên ma trận khối ở mỗi tầng của mạng CNN.

- Vùng nhận thức (Receptive Field): Là một vùng ảnh trên khối ma trận đầu vào mà bộ lọc sẽ nhân tích chập để ánh xạ tới một đơn vị trên layer tiếp theo.



- Vùng địa phương (Local region): Theo một nghĩa nào đó sẽ bao hàm cả vùng nhận thức. Là một vùng ảnh cụ thể nằm trên khối ma trận ở các tầng (layer) của mạng CNN.

- Bản đồ đặc trưng (Feature Map): Là ma trận đầu ra khi áp dụng phép tích chập giữa bộ lọc với các vùng nhận thức theo phương di chuyển từ trái qua phải và từ trên xuống dưới.

Bản đồ kích hoạt (Activation Map): Là output của bản đồ đặc trưng CNN khi áp dụng thêm hàm activation để tạo tính phi tuyến.

## Kiến trúc chung của mạng neural tích chập

Tích chập được ứng dụng phổ biến trong lĩnh vực thị giác máy tính. Thông qua các phép tích chập, các đặc trưng chính từ ảnh được trích xuất và truyền vào các tầng tích chập (layer convolution). Mỗi một tầng tích chập sẽ bao gồm nhiều đơn vị mà kết quả ở mỗi đơn vị là một phép biến đổi tích chập từ layer trước đó thông qua phép nhân tích chập với bộ lọc.

Về cơ bản thiết $\mathrm { k } \acute { \mathrm { e } }$ của một mạng nơ ron tích chập 2 chiều có dạng như sau:

INPUT $_ - >$ [[CONV $_ - >$ RELU]\*N $_ - >$ POOL?]\*M $_ - >$ [FC $_ - >$ RELU]\*K ->FC

Trong đó:

• INPUT: Tầng đầu vào   
• CONV: Tầng tích chập   
• RELU: Tầng kích hoạt. Thông qua hàm kích hoạt (activation function), thường là ReLU hoặc LeakyReLU để kích hoạt phi tuyến POOL: Tầng tổng hợp, thông thường là Max pooling hoặc có thể là Average pooling dùng để giảm chiều của ma trận đầu vào. FC: Tầng kết nối hoàn toàn. Thông thường tầng này nằm ở sau cùng và kết nối với các đơn vị đại diện cho nhóm phân loại.

Các kí hiệu []N, []M hoặc []\*K ám chỉ các khối bên trong [] có thể lặp lại nhiều lần liên tiếp nhau. M, K là số lần lặp lại. Kí hiệu $\mathrm { . > }$ đại diện cho các tầng liền kề nhau mà tầng đứng trước sẽ làm đầu vào cho tầng đứng sau. Dấu ? sau POOL để thể hiện tầng POOL có thể có hoặc không sau các khối tích chập.

Như vậy ta có thể thấy một mạng nơ ron tích chập về cơ bản có 3 quá trình khác nhau:

Quá trình tích chập (convolution): Thông qua các tích chập giữa ma trận đầu vào với bộ lọc để tạo thành các đơn vị trong một tầng mới. Quá trình này có thể diễn ra liên tục ở phần đầu của mạng và thường sử dụng kèm với hàm kích hoạt ReLU. Mục tiêu của tầng này là trích suất đặc trưng hai chiều.



Quá trình tổng hợp (max pooling): Các tầng càng về sau khi trích xuất đặc trưng sẽ cần số lượng tham số lớn do chiều sâu được qui định bởi số lượng các kênh ở các tầng sau thường tăng tiến theo cấp số nhân. Điều đó làm tăng số lượng tham số và khối lượng tính toán trong mạng nơ ron. Do đó để giảm tải tính toán chúng ta sẽ cần giảm kích thước các chiều của khối ma trận đầu vào hoặc giảm số đơn vị của tầng. Vì mỗi một đơn vị sẽ là kết quả đại diện của việc áp dụng 1 bộ lọc để tìm ra một đặc trưng cụ thể nên việc giảm số đơn vị sẽ không khả thi. Giảm kích thước khối ma trận đầu vào thông qua việc tìm ra 1 giá trị đại diện cho mỗi một vùng không gian mà bộ lọc đi qua sẽ không làm thay đổi các đường nét chính của bức ảnh nhưng lại giảm được kích thước của ảnh. Do đó quá trình giảm chiều ma trận được áp dụng. Quá trình này gọi là tổng hợp nhằm mục đích giảm kích thước dài, rộng.

Quá trình kết nối hoàn toàn (fully connected): Sau khi đã giảm kích thước đến một mức độ hợp lý, ma trận cần được trải phẳng (flatten) thành một vector và sử dụng các kết nối hoàn toàn giữa các tầng. Quá trình này sẽ diễn ra cuối mạng CNN và sử dụng hàm kích hoạt là ReLU. Tầng kết nối hoàn toàn cuối cùng (fully connected layer) sẽ có số lượng đơn vị bằng với số classes và áp dụng hàm kích hoạt là softmax nhằm mục đích tính phân phối xác xuất.

# Tính chất của mạng nơ ron tích chập

Tính kết nối trượt: Khác với các mạng nơ ron thông thường, mạng nơ ron tích chập không kết nối tới toàn bộ hình ảnh mà chỉ kết nối tới từng vùng địa phương (local region) hoặc vùng nhận thức (receptive field) có kích thước bằng kích thước bộ lọc của hình ảnh đó. Các bộ lọc sẽ trượt theo chiều của ảnh từ trái qua phải và từ trên xuống dưới đồng thời tính toán các giá trị tích chập và điền vào bản đồ kích hoạt (activation map) hoặc bản đồ đặc trưng (feature map).



![](images/image3.jpg)  
Hinh5:Quátrintrtvatin tichchpcamt blokichtuocxtrnnkétitibnichhoat，Sourceub

Các khối nơ ron 3D: Không giống như những mạng nơ ron thông thường khi cấu trúc ở mỗi tầng là một ma trận 2D (batch size x số đơn vị ở mỗi tầng). Các kết quả ở mỗi tầng của một mạng nơ ron là một khối 3D được sắp xếp một cách hợp lý theo 3 chiều rộng (width), cao (height), sâu (depth). Trong đó các chiều rộng và cao được tính toán theo công thức tích chập mục 1.1. Giá trị chiều rộng và cao của một tầng phụ thuộc vào kích thước của bộ lọc, kích thước của tầng trước, kích thước mở rộng (padding) và bước trượt bộ lọc (stride). Tuy nhiên chiều sâu lại hoàn toàn không phụ thuộc vào những tham số này mà nó bằng với số bộ lọc trong tầng đó. Quá trình tính bản đồ kích hoạt dựa trên một bộ lọc sẽ tạo ra một ma trận 2D. Như vậy khi áp dụng cho d bộ lọc khác nhau, mỗi bộ lọc có tác dụng trích suất một dạng đặc trưng trên mạng nơ ron, ta sẽ thu được d ma trận 2D có cùng kích thước mà mỗi ma trận là một bản đồ đặc trưng. Khi sắp xếp chồng chất các ma trận này theo chiều sâu kết quả đầu ra là một khối nơ ron 3D. Thông thường đối với xử lý ảnh thì tầng đầu vào có depth $= 3$ (số kênh) nếu các bức ảnh đang để ở dạng màu gồm 3 kênh RBG. Bên dưới là một cấu trúc mạng nơ ron điển hình có dạng khối.

![](images/image4.jpg)  
Hinh 6: Cáu trúc các khói no ron 3D mang Alexnet, Source: mdpi.com

Tính chia sẻ kết nối và kết nối cục bộ: Chúng ta đã biết quá trình biến đổi trong mạng tích chập sẽ kết nối các khối nơ ron 3D. Tuy nhiên các đơn vị sẽ không kết nối tới toàn bộ khối 3D trước đó theo chiều rộng và cao mà chúng sẽ chọn ra các vùng địa phương (hoặc vùng nhận thức) có kích thước bằng với bộ lọc. Các vùng địa phương sẽ được chia sẻ chung một bộ siêu tham số có tác dụng nhận thức đặc trưng của bộ lọc. Các kết nối cục bộ không chỉ diễn ra theo chiều rộng và cao mà kết nối sẽ mở rộng hoàn toàn theo chiều sâu. Như vậy số tham số trong một tầng sẽ là FxFxD ( F, D lần lượt là kích thước bộ lọc và chiều depth).

Mỗi bộ lọc sẽ có khả năng trích xuất một đặc trưng nào đó như đã giải thích ở mục 1. Do đó khi đi qua toàn bộ các vùng địa phương của khối nơ ron 3D, các đặc trưng được trích xuất sẽ hiển thị trên tầng mới.

![](images/image5.jpg)  
Hinh 7: Két nói cuc bo, Source: cs231n-stanford

Tính tổng hợp: Ở các tầng tích chập gần cuối số tham số sẽ cực kì lớn do sự gia tăng của chiều sâu và thông thường sẽ theo cấp số nhân. Như vậy nếu không có một cơ chế kiểm soát sự gia tăng tham số, chi phí tính toán sẽ cực kì lớn và vượt quá khả năng của một số máy tính cấu hình yếu. Một cách tự nhiên là chúng ta sẽ giảm kích thước các chiều rộng và cao bằng kỹ 6 thuật giảm mẫu (down sampling) mà vẫn giữ nguyên được các đặc trưng của khối. Theo đó những bộ lọc được di chuyển trên bản đồ đặc trưng và tính trung bình (average pooling) hoặc giá trị lớn nhất (max pooling) của các phần tử trong vùng nhận thức. Trước đây các tính trung bình được áp dụng nhiều nhưng các mô hình hiện đại đã thay thế bằng giá trị lơn nhất do tốc độ tính max nhanh hơn so với trung bình.



![](images/image6.jpg)  
Hinh 8: Quá trinh tong hop, Source: cs231n -stanford

Độ phức tạp phát hiện hình ảnh tăng dần: Ở tầng đầu tiên, hình ảnh mà chúng ta có chỉ là những giá trị pixels. Sau khi đi qua tầng thứ 2 máy tính sẽ nhận diện được các hình dạng cạnh, rìa và các đường nét đơn giản được gọi là đặc trưng bậc thấp (low level). Càng ở những tầng tích chập về sau càng có khả năng phát hiện các đường nét phức tạp, đã rõ ràng hình thù và thậm chí là cấu thành vật thể, đây được gọi là những đặc trưng bậc cao (high level). Máy tính sẽ học từ tầng cuối cùng để nhận diện nhãn của hình ảnh.

# Public_124 

# GIỚI THIỆU

Xử lý ngôn ngữ tự nhiên là một lĩnh vực nghiên cứu của trí tuệ nhân tạo nhằm xây dựng một hệ thống xử lý cho máy tính, làm cho máy tính có thể hiểu được ngôn ngữ của con người gồm cả ngôn ngữ nói và viết. Không chỉ với một ngôn ngữ của một dân tộc, của một quốc gia mà máy tính có thể hiểu được ngôn ngữ của tất cả các dân tộc, các quốc gia trên thế giới. Nhờ đó, mọi người trên thế giới dựa vào máy tính cũng có thể hiểu và giao tiếp được với nhau mà không cần học, hiểu ngôn ngữ của nhau,... Và hơn thế nữa, máy tính có thể phân tích, tổng hợp ngôn ngữ để đưa ra tri thức cho con người một cách nhanh chóng và chính xác. Nhất là khi các dữ liệu liên quan đến ngôn ngữ đang dần trở nên là kiểu dữ liệu chính của con người.

Xử lý ngôn ngữ tự nhiên nhằm mục đích: Phân tích, nhận biết, tổng hợp ngôn ngữ tự nhiên. Là cơ sở chính để hiểu ngôn ngữ, dịch ngôn ngữ, xử lý tiếng nói, xử lý văn bản,... Để xử lý ngôn ngữ tự nhiên bằng máy tính, trên thế giới người ta đã cho ra đời một ngành học mới được kết hợp giữa hai ngành máy tính và ngôn ngữ học, được gọi là ngôn ngữ học máy tính. Trong tương lai máy tính sử dụng ngôn ngữ tự nhiên để giao tiếp giữa người và máy, máy có khả năng hiểu được ngôn ngữ tự nhiên của con người và trả lời các câu hỏi của con người. Thậm chí máy sẽ dịch được các ngôn ngữ tự nhiên từ một ngôn ngữ này sang một một ngôn ngữ khác một cách nhanh chóng và chính xác.

Với một hệ thống xử lý ngôn ngữ tự nhiên, đầu vào của một hệ thống có thể là một hoặc nhiều câu dưới dạng tiếng nói hay văn bản. Các dữ liệu liên quan đến ngôn ngữ viết (văn bản) và nói (tiếng nói) đang dần trở nên kiểu dữ liệu chính con người có và lưu trữ dưới dạng điện tử. Đặc điểm chính của các kiểu dữ liệu này là không có cấu trúc hoặc nửa cấu trúc và chúng không thể lưu trữ trong các khuôn dạng cố định như các bảng biểu. Theo đánh giá của công ty Oracle, hiện có đến $80 \%$ dữ liệu không cấu trúc trong lượng dữ liệu của loài người đang có [Oracle Text]. Với sự ra đời và phổ biến của Internet, của sách báo điện tử, của máy tính cá nhân, của viễn thông, của thiết bị âm thanh, … người người ai cũng có thể tạo ra dữ liệu văn bản hay tiếng nói. Vấn đề là làm sao ta có thể xử lý chúng, tức chuyển chúng từ các dạng ta chưa hiểu được thành các dạng ta có thể hiểu và giải thích được, tức là ta có thể tìm ra thông tin, tri thức hữu ích cho mình [1].

# CÁC BƯỚC XỬ LÝ VĂN BẢN



Quá trình xử lý văn bản hay quá trình phân tích và kiểm tra tính chính xác của một văn bản là một vấn đề khá phức tạp, trải qua nhiều bước khác nhau. Ở mỗi bước xử lý đòi hỏi người nghiên cứu phải có một nền tảng kiến thức vững vàng về ngôn ngữ cũng như nhiều kiến thức bổ trợ khác mới có thể xử lý tốt được. Quá trình này có thể được chia thành các bước sau.

• Tiền xử lý văn bản: Sẽ xử lý sơ bộ văn bản đầu vào (làm sạch văn bản) bằng cách xóa bỏ những ký tự, những mã điều khiển, những vùng không cần thiết cho việc xử lý và phân rã nó ra thành các câu là đơn vị cơ sở của một văn bản. Phân tích hình thái: phân tích câu thành một bảng các từ (hay cụm từ) riêng biệt, đồng thời kèm theo tất cả các thông tin về từ đó, như là: Từ loại, phạm trù ngữ pháp, các biến cách của từ, tiền tố, hậu tố của từ (nếu có). Trong trường hợp gặp từ mới, hệ thống sẽ để nguyên và đánh dấu một từ loại đặc biệt để chuyển sang phần xử lý tên riêng hay từ mới. Phân tích cứu pháp: Phân tích một câu thành những thành phần văn phạm có liên quan với nhau và được thể hiện thành cây cú pháp. Khi nhập câu, ta phải phân thành các thành phần như chủ ngữ, vị ngữ; gán vai trò chủ từ, đối từ của động từ chính, bổ nghĩa,.. Phân tích ngữ nghĩa: là kiểm tra ý nghĩa của câu có mâu thuẫn với ý nghĩa của đoạn hay không. Dựa trên mối liên hệ logic về nghĩa giữa các cụm từ trong câu và mối liên hệ giữa các câu trong đoạn, hệ thống sẽ xác định được một phần ý nghĩa của câu trong ngữ cảnh của đoạn. Tích hợp văn bản: Ngữ nghĩa của một câu riêng biệt có thể phụ thuộc vào những câu đứng trước, đồng thời nó cũng có thể ảnh hưởng đến các câu phía sau. Phân tích thực nghĩa: phân tích nhằm xác định ý nghĩa câu dựa trên mối liên hệ của câu với hiện thực. Ý nghĩa thực tế của câu phụ thuộc   
rất nhiều vào ý tứ của người nói và ngữ cảnh diễn ra lời nói.

3. HƯỚNG TIẾP CẬN VỚI BÀI TOÁN TÁCH TỪ



Các nhà nghiên cứu đã đề xuất một số hướng tiếp cận để giải quyết bài toán tách từ. Nhìn chung, các hướng tiếp cận đó được chia thành 2 hướng: tiếp cận dựa trên từ và tiếp cận dựa trên ký tự từ[2].

Hướng tiếp cận dựa trên từ với mục tiêu tách được các từ hoàn chỉnh trong câu. Hướng tiếp cận này được chia thành 3 nhóm: dựa trên thống kê (statistics-based), dựa trên từ điển (dictionary-based) và kết hợp nhiều phương pháp (hydrid-based).

Hướng tiếp cận dựa vào thống kê cần phải dựa vào thông tin thống kê như từ hay tần số ký tự, hay xác suất cùng xuất hiện trong một tệp dữ liệu cơ sở. Do đó, tính hiệu quả của các giải pháp này chủ yếu dựa vào dữ liệu huấn luyện cụ thể được sử dụng. Tác giả Đinh Điền [7] đã xây dựng ngữ liệu huấn luyện riêng (khoảng 10Mb) dựa vào các tài nguyên, tin tức và sách điện tử trên Internet, bộ dữ liệu này khá nhỏ và không toàn diện tức là không bao quát nhiều lĩnh vực, nhiều chủ đề.

Hướng tiếp cận dựa trên từ điển: Ý tưởng của hướng tiếp cận này là những cụm từ được tách ra từ văn bản phải được so khớp với các từ trong từ điển. Từ điển sử dụng để so khớp thì lại có 2 loại: từ điển hoàn chỉnh (full word/pharse) và từ điển thành phần (component). Trong từ điển hoàn chỉnh thì chia thành 3 loại: so khớp dài nhất (longest match), so khớp ngắn nhất (shortest match) và so khớp kết hợp (overlap). Hướng tiếp cận này có đặc điểm là đơn giản, dễ hiểu tuy nhiên hiệu quả mang lại chưa được cao. Lý do là bởi nó chưa xử lý được nhiều trường hợp nhập nhằng cũng như khả năng phát hiện từ mới trong văn bản chưa cao. Hiện nay, hướng tiếp cận so khớp cực đại được xem là phương pháp quan trọng và có hiệu quả nhất trong hướng tiếp cận từ điển.

Hướng tiếp cận nhiều phương pháp với mục đích kết hợp các phương pháp tiếp cận khác nhau để thừa hưởng các ưu điểm của nhiều kỹ thuật và hướng tiếp cận khác nhau nhằm nâng cao hiệu quả. Hướng tiếp cận này thường kết hợp giữa hướng tiếp cận thống kê và dựa trên từ điển nhằm tận dụng những mặt mạnh của các phương pháp này. Tuy nhiên, hướng tiếp cận này lại mất nhiều thời gian xử lý, không gian đĩa và chi phí cao.

Hướng tiếp cận dựa trên ký tự từ: Hướng tiếp cận này đơn thuần là rút trích ra một số lượng nhất định các tiếng trong văn bản như rút trích 1 ký tự (unigram) hay nhiều ký tự (n-gram). Phương pháp này tuy đơn giản nhưng mang lại kết quả quan trọng được chứng minh qua một số công trình nghiên cứu đã được công bố, như của tác giả Lê An Hà [3].



Trong bài báo gần đây của H.Nguyễn et al, đề xuất năm 2005. Đây là phương pháp tách từ dựa trên thống kê từ Internet và giải thuật di truyền thay vì sử dụng dữ liệu thô, để tìm ra những cách phân cách đoạn văn bản tối ưu nhất cùng một văn bản. Khi so sánh kết quả của tác giả Lê An Hà và H.Nguyễn thì thấy công trình nghiên cứu của H.Nguyễn cho được kết quả tốt hơn khi tiến hành tách từ, tuy nhiên thời gian xử lý lâu hơn. Ưu điểm của hướng tiếp cận dựa trên nhiều ký tự là tính đơn giản, dễ ứng dụng, chi phí thấp. Qua nhiều công trình nghiên cứu của các tác giả đã được công bố, hướng tiếp cận dựa trên ký tự từ được cho là sự lựa chọn thích hợp.

# MỘT SỐ PHƯƠNG PHÁP TÁCH TỪ

## Phương pháp so khớp cực đại (Maximum Matching)

Phương pháp này đã được ChihHao Tsai [4] giới thiệu năm 1996. Ý tưởng chính của phương pháp này là duyệt một câu từ trái qua phải và chọn từ có nhiều tiếng nhất có mặt trong từ điển tiếng Việt, rồi cứ thế tiếp tục cho từ kế tiếp cho đến hết câu.

Phương pháp so khớp cực đại dạng đơn giản: Giả sử chúng ta có một câu $\mathrm { S } =$ {c1, c2, c3,...,cn} với c1, c2, c3,... cn là các tiếng được tách bởi khoảng trắng trong câu. Chúng ta bắt đầu duyệt từ đầu chuỗi, xác định đâu là từ. Trước tiên, chúng ta sẽ kiểm tra xem c1 có phải là từ có trong từ điển hay không, sau đó kiểm tra c1c2 có trong từ điển hay không. Tiếp tục như vậy c1c2c3, c1c2c3c4,..., c1c2c3... cn, với n là số tiếng lớn nhất của một từ có thể có nghĩa (nghĩa là có trong từ điển tiếng Việt). Sau đó, chúng ta chọn từ có nhiều tiếng nhất có mặt trong từ điển và đánh dấu từ đó. Tiếp tục quá trình trên với tất cả các từ còn lại trong câu và trong toàn bộ văn bản.

Phương pháp so khớp cực đại dạng phức tạp: Phương pháp này về cơ bản cũng giống như so khơp cực đại dạng đơn giản. Tuy nhiên, dạng này có thể tránh được một số nhập nhằng gặp phải trong dạng đơn giản. Độ chính xác cao lên đến $9 9 . 6 9 \%$ và 93.21 nhập nhằng được giải quyết. Đầu tiên, chúng ta sẽ kiểm tra xem c1 có phải từ có trong từ điển hay không, sau đó kiểm tra tiếp c1c2 có nằm trong từ điển hay không. Giả sử có 1 trường hợp xảy ra như sau: ta có c1 và c1c2 đều có trong từ điển thì thuật toán thực hiện chiến thực 3 từ tốt nhất được Chen & Liu (1992) đưa ra như sau:

Độ dài trung bình của từ lớn nhất: ở cuối mỗi chuỗi thường gặp những bộ chỉ có một hoặc hai từ. Luật này chỉ có lợi khi thiếu một hoặc một vài vị trí trong bộ. Khi bộ là bộ ba thì luật này không được hiệu quả lắm. Vì bộ ba từ có cùng tổng độ dài, đương nhiên nó sẽ có cùng độ dài chung bình. Nên giải pháp này không đạt hiệu quả cao vì thế chúng ta cần một giải pháp khác.



Sự chênh lệch độ dài của 3 từ là ít nhất: là độ biến đổi nhỏ nhất chiều dài từ. Luật này cho phép lấy bộ đầu tiên với độ biến đổi chiều dài từ nhỏ nhất. Trong ví dụ trên, ta lấy từ C1C2 từ bộ đầu tiên. Giả thiết của luật này là những từ có chiều dài đều bằng nhau.

Đánh giá phương pháp: Phương pháp so khớp cực đại là cách tách từ đơn giản, dễ hiểu và chạy nhanh. Hơn chúng ta chỉ cần một tập từ điển đầy đủ là có thể tiến hành tách các văn bản. Tuy nhiên, phương pháp này không giải quyết 2 vấn đề quan trọng của bài toán tách từ tiếng Việt là thuật toán gặp phải nhiều nhập nhằng; độ chính xác của phương pháp này phụ thuộc vào tính đầy đủ và tính chính xác của từ điển.

## Phương pháp chuyển dịch trạng thái hữu hạng có trọng số

Chuyển dịch trạng thái hữu hạn có trọng số (Weighted Finite-State Transducer – WFST) [5]. Mô hình chuyển dịch trạng thái hữu hạn có trọng số WFST đã được đề xuất năm 1996. Ý tưởng chính của phương pháp này áp dụng cho tách từ tiếng Việt là các từ sẽ được gán trọng số bằng xác suất xuất hiện của từ đó trong dữ liệu. Sau đó duyệt qua các câu, cách duyệt có trọng số lớn nhất sẽ là cách dùng để tách từ. Trong phương pháp này, tầng tiền xử lý có nhiệm vụ xử lý định dạng văn bản: Tiêu đề, đoạn, câu; chuẩn hoá về chính tả tiếng Việt (cách bỏ dấu, cách viết các ký tự y, i,... trong tiếng Việt). Ví dụ: Vật lý $=$ vật lí, thời kỳ $=$ thời kì).

Sau đó câu được chuyển sang tầng WFST. Trong tầng này tác giả xử lý thêm các vấn đề liên quan đến đặc thù của tiếng Việt, như: Từ láy, tên riêng, ...và tầng mạng Neural dùng để khử nhập nhằng về ngữ nghĩa sau khi đã tách từ (nếu có).

Sơ đồ các bước xử lý của WFST

Xét tầng WFST:

Hoạt động của WFST có thể chia thành ba bước sau:

- Bước 1: Xây dựng từ điển trọng số, trong mô hình WFST, thì việc phân đoạn từ có thể được xem như là một sự chuyển dịch trạng thái có xác xuất. Chúng ta miêu tả từ điển D là một đồ thị biến đổi trạng thái hữu hạn có trọng số.



- Bước 2: Xây dựng khả năng tách từ, bước này thống kê tất cả các khả năng tách từ của một câu. Vấn đề ở đây là để giảm sự bùng nổ các cách tách từ, thuật toán sẽ loại bỏ ngay những nhánh tách từ nào đó không phù hợp mà chứa từ không xuất hiện trong từ điển, không phải là từ láy, không phải là danh từ riêng thì loại bỏ các nhánh xuất phát từ cách tách từ đó. Thật vậy, giả sử một câu gồm n âm tiết, mà trong tiếng Việt thì một từ có tối đa 4 âm tiết tức là ta sẽ có tối đa 2n-1 cách tách từ khác nhau. Một câu tiếng Việt trung bình có 24 âm tiết thì lúc đó ta phải giải quyết 8.000.000 trường hợp tách từ có thể trong một câu.

- Bước 3: Lựa chọn khả năng tối ưu: Sau khi liệt kê tất cả các khả năng tách từ, thuật toán sẽ chọn cách tách tốt nhất, đó là tách đoạn có trọng số bé nhất.

Xét ví dụ sau: Đầu vào là câu: “Tốc độ truyền thông tin sẽ tăng cao”:

Trọng số theo mỗi cách tách từ được tính là:

Id(I).D\* $=$ “Tốc độ # truyền thông # tin # sẽ # tăng # cao” (1) $= 8 . 6 8 + 1 2 . 3 1 + 7 . 3 3 + 6 . 0 9 + 7 . 4 3 + 6 . 9 5 = 4 8 . 7 9$

ID(I).D\* = “TỐC ĐỘ # TRUYỀN # THÔNG TIN # SẼ # TĂNG # CAO” (2)

$= 8 . 6 8 + 1 2 . 3 1 + 7 . 2 4 + 6 . 0 9 + 7 . 4 3 + 6 . 9 5 = 4 8 . 7 0$

Khi đó ta có được cách tối ưu là tách đoạn (2) “Tốc độ # truyền # thông tin # sẽ # tăng # cao”.

Xét tầng Neural:

Sau khi cho câu được tách từ qua mô hình WFST. Để xác định kết quả tách từ trên có thực sự hợp lệ hay không, tác giả định nghĩa một ngưỡng giá trị t0 với ý nghĩa như sau: nếu sự chênh lệch về trọng số (giữa các cách tách từ khác nhau với cách tách từ có trọng số nhỏ nhất) lớn hơn t0 thì đó là kết quả tách từ có trọng số nhỏ nhất đó đúng của câu và được chấp nhận. Còn nếu sự chênh lệch đó không lớn hơn t0, thì cách tách từ có trọng số nhỏ nhất đó chưa được xem là kết quả tách từ đúng của câu. Lúc này, ta sẽ đưa những cách tách từ của câu này qua mô hình mạng Neural để xử lý tiếp.

Tầng nhập của mạng được kết nối hoàn toàn với một tầng ẩn $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m } \ 1 0$ nút với một hàm truyền. Những nút ẩn này lại được kết nối hoàn toàn với một tầng xuất chỉ $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m } 1$ nút. Nút xuất là một giá trị thực nằm giữa 0..1. Biểu thị cho khả năng hợp lệ của một dãy các từ loại đứng liền nhau trong một cửa sổ trượt. Khi cửa sổ trượt từ đầu câu đến cuối câu, cộng dồn các kết quả lại với nhau và gán giá trị này vào thành trọng số của câu. Câu có trọng số lớn nhất sẽ được chọn.



Hàm truyền được chọn là hàm sigmoid:

Đánh giá phương pháp: phương pháp này là sẽ cho độ chính xác cao nếu ta xây dựng được một dữ liệu học đầy đủ và chính xác. Nó còn có thể kết hợp với các phương pháp khử nhập nhằng để cho kết quả tách rất cao (có thể chính xác đến $9 7 \%$ , tỉ lệ này tuỳ thuộc vào loại văn bản). Tuy nhiên, việc đánh trọng số dựa trên tần số xuất hiện của từ, nên khi tiến hành tách thì không tránh khỏi các nhập nhằng trong tiếng Việt. Hơn nữa với những văn bản dài thì phương pháp này còn gặp phải sự bùng nổ các khả năng phân đoạn của từng câu.

## Phương pháp mô hình Markov ẩn

Mô hình Markov (Hidden Markov Model - HMM) được giới thiệu vào cuối những năm 1960 [6]. Cho đến hiện nay phương pháp này có một ứng dụng khá rộng như trong nhận dạng giọng nói, tính toán sinh học và xử lý ngôn ngữ tự nhiên. Mô hình Markov là mô hình trạng thái hữu hạn với các tham số biểu diễn xác suất chuyển trạng thái và xác suất sinh dữ liệu quan sát tại mỗi trạng thái.

Mô hình Markov ẩn là mô hình thống kê trong đó hệ thống được mô hình hóa được cho là một quá trình Markov với các tham số không biết trước và nhiệm vụ là xác định các tham số ẩn từ các tham số quan sát được, dựa trên sự thừa nhận này. Các tham số của mô hình được rút ra sau đó có thể sử dụng để thực hiện các phân tích kế tiếp.

Trong một mô hình Markov điển hình, trạng thái được quan sát trực tiếp bởi người quan sát, vì vậy các xác suất chuyển tiếp trạng thái là các tham số duy nhất. Mô hình Markov ẩn thêm vào các đầu ra, mỗi trạng thái có xác suất phân bổ trên các biểu hiện đầu ra có thể. Vì vậy, nhìn vào dãy của các biểu hiện được sinh ra bởi HMM không trực tiếp chỉ ra dãy các trạng thái.

Các thông số trong mô hình: xi: các trạng thái trong mô hình Markov, aij: Các xác suất chuyển tiếp, bij: các xác suất đầu ra, yi: Các dữ liệu quan sát. Mô hình Markov ẩn thêm vào các đầu ra, mỗi trạng thái có xác suất phân bố trên các biểu hiện đầu ra có thể. Vì vậy, nhìn vào dãy của các biểu hiện được sinh ra bởi HMM không trực tiếp chỉ ra dãy các trạng thái. Ta có thể tìm ra được chuỗi các trạng thái mô tả tốt nhất cho mỗi dữ liệu quan sát đước bằng cách tính: $\operatorname { P } ( \mathrm { Y } \mid \mathrm { X } ) = \operatorname { P } ( \mathrm { Y } \mid \mathrm { X } ) / \operatorname { P } ( \mathrm { X } ) .$ .



Trong khi đó Yn là trạng thái thời điểm thứ $\mathbf { t } = \mathbf { n }$ trong chuỗi trạng thái Y, Xn là dữ liệu quan sát được tại thời đ $\dot { \mathrm { { e m } } }$ thứ $\mathbf { t } = \mathbf { n }$ trong chuỗi X. Do trạng thái hiện tại chỉ phụ thuộc vào trạng thái ngay trước đó với giả thiết rằng dữ liệu quan sát được tại thời điểm t chỉ phụ thuộc vào trạng thái t. Ta có thể tính P(Y, X) theo công thức:

Đánh giá phương pháp: mô hình Markov để tính được xác suất P(Y,X) thông thường ta phải liệt kê hết các trường hợp có thể của chuỗi Y và chuỗi X. Thực tế thì chuỗi Y là hữu hạn có thể liệt kê được, còn X (các dữ liệu quan sát) là rất phong phú. Để giải quyết các vấn đề này HMM đưa ra giả thiết về sự độc lập giữa các dữ liệu quan sát. Dữ liệu quan sát được tại thời điểm t chỉ phụ thuộc vào trạng thái tại thời điểm đó. Hạn chế thứ hai gặp phải là việc sử dụng xác suất đồng thời P (Y, X) đôi khi không chính xác vì với một số bài toán thì việc sử dụng xác suất điều kiện P(Y|X) cho kết quả tốt hơn rất nhiều.

## Phương pháp so khớp từ dài nhất (Longest Matching):

Phương pháp so khớp từ dài nhất [7] dựa trên tư tưởng tham lam. Với mỗi câu, duyệt từ trái qua phải các âm tiết trong câu, kiểm tra xem có nhóm các âm tiết có tồn tại trong từ điển hay không. Chuỗi dài nhất các âm tiết được xác định là từ sẽ được chọn ra. Tiếp tục thực hiện việc so khớp cho đến hết câu. Thuật toán chỉ đúng khi không có sự nhập nhằng những tiếng đầu của từ sau có thể ghép với từ trước tạo thành một từ có trong từ điển.

Giải thuật

Input: Chuỗi ký tự;

Output: Chuỗi từ, cụm từ (từ có chiều dài dài nhất);

V là danh sách các tiếng chưa xét;

T là bộ từ điển.

While $\mathrm { V } \neq \emptyset$ do

Begin

Wmax $\underline { { \underline { { \mathbf { \Pi } } } } }$ từ đầu danh sách V;   
Foreach (v thuộc từ $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ các tiếng bắt đầu trong V)   
If(length(v) $>$ length(Wmax) and (v thuộc T)) Then $\operatorname { W m a x } { = } \mathbf { V }$ ;



Loại bỏ đi các từ Wmax ở đầu danh sách V;

End.

Xét ví dụ: “Tôi là sinh viên trường Đại học Kiên Giang”:

Đánh giá phương pháp: phương pháp so khớp từ dài nhất là phương pháp tách từ đơn giản chỉ cần dựa vào từ điển với đội chính xác tương đối cao. Phương pháp này sẽ không tốt nếu có hiện tượng nhập nhằng xảy ra. Độ chính xác phụ thuộc hoàn toàn vào tính đầy đủ và chính xác của từ điển.

# THỰC NGHIỆM – KẾT QUẢ

## Thực nghiệm

Mục tiêu nghiên cứu là đánh giá tính khả thi của thuật toán tách từ dựa vào phương pháp so khớp cực đại (Maximum Matching) để tách toàn bộ văn bản, với dữ liệu sử dụng là bảng âm tiết tiếng Việt và từ điển từ vựng tiếng Việt. Phần mềm Vntokenizer là phần mềm tách từ biểu diễn cho phương pháp so khớp cực đại.

Quy trình thực hiện tách từ theo phương pháp so khớp cực đại (Vntokenizer).

Input: của phần mềm Vntokenizer là một câu, một văn bản được lưu dưới dạng tệp (.txt).

Output: là một chuỗi các từ đã được tách ở dạng file (.txt).

Thuật toán sẽ duyệt từ đầu chuỗi xác định đâu là từ. Đầu tiên, ta kiểm tra xem nó có trong từ điển hay không, sau đó kiểm tra tiếp chữ kế có trong từ điển hay không, nếu chữ đầu tiên và chữ kế tiếp có trong kho dữ liệu thì chương trình sẽ đọc chữ tiếp theo, quá trình đó sẽ lập lại cho đến khi đọc chữ tiếp theo mà dãy chữ đó không có trong từ điển thì sẽ dừng lại và lấy từ. Tức là chương trình sẽ duyệt một câu từ trái sang phải và chọn từ có nhiều âm tiết nhất có mặt trong từ điển và đánh dấu từ đó. Sau đó, tiếp tục quá trình trên với tất cả các từ kế tiếp cho đến hết câu.

Các đơn vị từ bao gồm các từ trong từ điển cũng như các chuỗi số, chuỗi ký tự từ nước ngoài, các dấu câu và các chuỗi kí tự hỗn tạp khác trong văn bản. Các đơn vị từ không chỉ bao gồm các từ có trong từ điển mà còn có thể là các từ mới hoặc các từ được sinh tự do theo một quy tắc nào đó (như phương thức thêm hậu tố hay phương thức láy) hoặc các chuỗi kí hiệu không được liệt kê trong từ điển.



## Kết quả

Kết quả phân tích sau khi áp dựng phương pháp so khớp cực đại, bằng cách chạy phần mềm Vntokenizer như sau: với file dữ liệu tên là 1.txt.

Giao diện màn hình khi chạy chương trình

Kết quả sau khi tách từ

Tính số lần xuất hiện của các từ

# KẾT LUẬN

Trong bài báo này chúng tôi giới thiệu các thuật toán tách từ trong xử lý ngôn ngữ tự nhiên dựa vào phương pháp so khớp cực đại, phương pháp mô hình MarKov ẩn, phương pháp chuyển dịch trạng thái hữu hạn có trọng số, phương pháp so khớp từ dài nhất. Kết quả mà chúng tôi thu được từ nghiên cứu này là hết sức khả quan và thiết nghĩ là hoàn toàn khả thi khi ứng dụng vào thực tế.

Trên cơ sở các phương pháp tách từ đó, bài báo này sử dụng phương pháp so khớp cực đại để minh họa cho các phương pháp tách từ trên. Phần mềm vntokenizer là phần mềm tách từ để biểu diễn cho thuật toán trên. Sau khi tách từ xong, tính tầng số xuất hiện các từ được tách trong tệp dữ liệu ban đầu. Đề xuất mô hình phân loại văn bản ứng dụng vào phân loại văn bản ở phòng ban, và thư viện trường Đại học Kiên Giang. Mặc dù kết quả nghiên cứu bước đầu đã khẳng định thuật toán tách từ dựa vào phương pháp so khớp cực đại là hoàn toàn khả thi và hoàn toàn có thể áp dụng vào thực tế, tuy nhiên Bài báo chỉ mới tách được các từ trong văn bản và tính được số lần xuất hiện của từ trong đoạn văn nhằm xây dựng vector đặc trưng từ đó hình thành ma trận để so sánh với từ khóa cho trước như: công nghệ thông tin, nông nghiệp,... từ đó làm cơ sở cho bài toán phân loại văn bản.

# TÀI LIỆU THAM KHẢO

[1] Hồ Tú Bảo, Lương Chi Mai (2008), Về xử lý tiếng Việt trong công nghệ thông tin, Viện Công nghệ Thông tin, Viện Khoa học và Công nghệ tiên tiến Nhật Bản.



[2] Trần Thị Oanh, Mô hình tách từ, gán nhãn từ loại và hướng tiếp cận tích hợp cho tiếng Việt, Luận văn thạc sĩ trường Đại học Công nghệ, Đại học Quốc gia Hà Nội.

[3] Le An Ha (2003), A method for word segmentation in Vietnamese.   
In Proceedings of Curpus Linguistics. Lancaster, UK.

[4] Chih-Hao Tsai (2000). MMSEG: A word identification system for Mandarin Chinese text Based on two variants of the Maximum Matching Algorithm.

[5] Dinh Dien, Hoang Kiem, Nguyen Van Toan (2001), Vietnamese Word Segmentation, the sexth 6th Natural Language Processing Pacific Rim Symposium Tokyo, Japan, pp.749 – 756.

[6] Phil Blunsom (2004), Hidden Markov Medels, pp. 1-7

[7] Chen,K.J.,&Liu, S. H. (1992), Word identification for Mandarin Chinese sentences. Proceedings of the fifteenth inrernational Conference on computational Linguistics, Nantes.

# Public_125 

Loài kiến là loài sâu bọ có tính chất xã hội, chúng sống thành từng đàn, bởi vậy có sự tác động lẫn nhau, chúng thạo tìm kiếm thức ăn và hoàn thành những nhiệm vụ từ kiến chỉ huy. Một điều thú vị trong tìm kiếm thức ăn của vài con kiến đặc biệt là khả năng của chúng để tìm kiếm đường đi ngắn nhất giữa tổ kiến và nguồn thức ăn. Trên thực tế, điều dễ nhận thấy có trong suy nghĩ nhưng nhiều con kiến hầu hết không nhận ra vì chúng không dùng thị giác để tìm kiếm những đầu mối thức ăn.

Tất cả mọi con kiến hầu như là mù, chúng chỉ có thể tương tác với nhau và với môi trường bằng cách sử dụng pheromone: đi đến đâu chúng xịt pheromone ra đến đấy. Mỗi một con kiến tại mỗi vị trí quyết định hướng đi tiếp theo dựa vào nồng độ pheromone của các hướng. Tại vị trí mà nồng độ pheromone xung quanh đều bằng nhau hoặc không có pheromone thì chúng sẽ quyết định hướng đi một cách ngẫu nhiên. Cứ như vậy thì các con kiến cứ đi theo bước chân của nhau và tạo thành một đường đi (path). Ta xét trường hợp tổ kiến ở vị trí 1 và nguồn thức ăn ở vị trí 2 như hình vẽ

![](images/image1.jpg)

Giả sử tại thời điểm ban đầu có 2 con kiến ra đi tìm thức ăn. Vì ban đầu chưa có pheromone nên chúng chọn 2 hướng đi khác nhau một cách ngẫu nhiên. Một hướng có đường đi đến nguồn thức ăn dài hơn hướng kia. Trong giai đoạn đầu các con kiến đi sau sẽ cảm nhận thấy nồng độ pheromone của cả 2 hướng là như nhau nên cũng chọn đi theo một trong 2 hướng một cách ngẫu nhiên. Tuy nhiên đường đi ngắn hơn làm cho khoảng 1 thời gian di chuyển từ tổ đến nguồn thức ăn rồi quay trở lại của mỗi con kiến theo con đường đó cũng ngắn hơn và do đó mật độ di chuyển qua lại của đàn kiến tại mỗi vị trí của con đường ngắn sẽ cao hơn con đường dài. Do mật độ qua lại lớn hơn dẫn đến kết quả là nồng độ pheromone trên con đường ngắn càng ngày càng cao hơn con đường dài. Kết quả cuối cùng là đàn kiến ngày càng từ bỏ con đường dài và đi theo con dường ngắn. Đến một lúc nào đó sẽ không còn con kiến nào đi theo con đường dài nữa mà tất cả đều đi theo con đường ngắn.



![](images/image2.jpg)

Thuật toán dựa trên hoạt động của đàn kiến có một số biến thể. Dạng đơn giản nhất gọi là AS (Ant System). Thuật toán này chỉ dùng để giải quyết bài toán tìm đường. Ở mức cao hơn là thuật toán ACO (Ant Colony Optimization).

# Từ những con kiến trong tự nhiên tới thuật toán ACO.

Thuật toán ACO lấy ý tưởng từ việc kiếm thức ăn của đàn kiến ngoài thực tế để giải quyết các bài toán tối ưu tổ hợp. Chúng dựa trên cơ sở một đàn kiến nhân tạo, chúng được tính toán tìm kiếm thức ăn nhờ mùi lạ nhân tạo.



Cấu trúc cơ bản của thuật toán ACO: trong mỗi thuật toán, tất cả kiến đi xây dựng cách giải quyết bài toán bằng cách xây dựng một đồ thị. Mỗi cạnh của đồ thị miêu tả các bước kiến có thể đi được kết hợp từ hai loại thông tin hướng dẫn kiến di chuyển:

Thông tin kinh nghiệm (heuristic information): giới hạn kinh nghiệm ưu tiên di chuyển từ nút r tới s…của cạnh $\mathrm { a _ { r s } }$ . Nó được đánh dấu bởi rs. Thông tin này không được thay đổi bởi kiến trong suốt quá trình chạy thuật toán.

Thông tin mùi lạ nhân tạo (artificial pheromone trail information), nó giới hạn “nghiên cứu sự thèm muốn” của chuyển động là kiến nhân tạo và bắt chước mùi lạ thực tế của đàn kiến tự nhiên. Thông tin này bị thay đổi trong suốt quá trình thuật toán chạy phụ thuộc vào cách giải quyết được tìm thấy bởi những con kiến. Nó được đánh dấu bởi rs.

Giới thiệu các bước ảnh hưởng từ những con kiến thật vào ACO. Có hai vấn đề cần chú ý:

• Chúng trừu tượng hoá vài mô hình thức ăn của kiến ngoài thực tế để tìm ra đường đi tìm kiếm thức ăn ngắn nhất. Chúng bao gồm vài đặc điểm không giống với tự nhiên nhưng lại cho phép thuật toán phát triển chứa đựng cách giải quyết tốt tới bài toán bị cản (ví dụ: sử dụng thông tin kinh nghiệm để hướng dẫn chuyển động của kiến).

Cách thức hoạt động cơ bản của một thuật toán ACO như sau: m kiến nhân tạo di chuyến, đồng thời và không đồng bộ, qua các trạng thái liền kề của bài toán. Sự di chuyển này theo một tập quy tắc làm cơ sở từ những vùng thông tin có sẵn ở các thành phần (các nút). Vùng thông tin này bao gồm thông tin kinh nghiệm và thông tin mùi lạ để hướng dẫn tìm kiếm. Qua sự di chuyển trên đồ thị kiến xây dựng được cách giải quyết. Những con kiến sẽ giải phóng mùi lạ ở mỗi lần chúng đi qua một cạnh (kết nối) trong khi xây dựng cách giải quyết (cập nhật từng bước mùi lạ trực tuyến). Mỗi lần những con kiến sinh ra cách giải quyết, nó được đánh giá và nó có thể tạo luồng mùi lạ là hoạt động của chất lượng của cách giải quyết của kiến (cập nhật lại mùi lạ trực tuyến). Thông tin này sẽ hướng dẫn tìm kiếm cho những con kiến đi sau.



Hơn thế nữa, cách thức sinh hoạt động của thuật toán ACO bao gồm thêm hai thủ tục, sự bay hơi mùi lạ (pheromone trail evaporation) và hoạt động lạ (daemon actions). Sự bay hơi của mùi lạ được khởi sự từ môi trường và nó được sử dụng như là một kĩ thuật để tránh tìm kiếm bị dừng lại và cho phép kiến khảo sát vùng không gian mới. Daemon actions là những hoạt động tối ưu như một bản sao tự nhiên để thực hiện những nhiệm vụ từ một mục tiêu xa tới vùng của kiến.

# Giới thiệu về thuật toán

Các thuật toán kiến là các thuật toán dựa vào sự quan sát các bầy kiến thực. Kiến là loại cá thể sống bầy đàn. Chúng giao tiếp với nhau thông qua mùi mà chúng để lại trên hành trình mà chúng đi qua. Mỗi kiến khi đi qua một đoạn đường sẽ để lại trên đoạn đó một chất mà chúng ta gọi là mùi. Số lượng mùi sẽ tăng lên khi có nhiều kiến cùng đi qua. Các con kiến khác sẽ tìm đường dựa vào mật độ mùi trên đường, mật độ mùi càng lớn thì chúng càng có xu hướng chọn. Dựa vào hành vi tìm kiếm này mà đàn kíên tìm được đường đi ngắn nhất từ tổ đến nguồn thức ăn và sau đó quay trở tổ của mình.

Sau đây là ví dụ về luồng đi của đàn kiến thực tế.



![](images/image3.jpg)  
Hình 1

a. Kiến đi theo đường thẳng giữa A và E b. Khi có chướng ngại vật kiến sẽ chọn hướng đi, có hai hướng với khả năng kiến sẽ chọn là như nhau.

c. Trên đường ngắn hơn thì nhiều mùi (pheromone) hơn

![](images/image4.jpg)  
Hình 2

Xem hình 2a là giải thích rõ tình huống trong hình 1b.



Giả sử khoảng cách $\scriptstyle \mathrm { D H = B H = D B }$ qua C và =1, C là điểm nằm giữa B và D (hình 2a). Bây giờ chúng ta xem xét điều gì xảy ra tại những khoảng thời gian rời rạc: $\scriptstyle { \mathrm { t } } = 0$ , 1, 2… Giả định rằng 30 con kiến mới đi từ A đến B, 30 con từ E đến D, mỗi kiến di chuyển với tốc độ một đơn vị thời gian và khi di chuyển kiến để tại thời điểm t một vệt pheromone với nồng độ là 1. Để đơn giản chúng ta xét lượng pheromone bay hơi hoàn toàn và liên tục trong khoảng thời gian $( \mathrm { t } { + } 1 , \mathrm { t } { + } 2 )$ .

Tại thời điểm $\scriptstyle { \mathrm { { t } = 0 } }$ , thì không có vệt mùi nào trên cạnh và có 30 kiến ở B, 30 ở D. Việc lựa chọn đường đi của chúng ta ngẫu nhiên do đó, trung bình từ mỗi nút có 15 con kiến sẽ đi đến H và 15 con sẽ đi đến C (hình 2b)

Tại thời điểm $\mathrm { \ t } { = } 1$ , 30 con kiến mới đi từ A đến B, lúc này nó sẽ chọn hướng đến C hoặc hướng đến H. Tại hướng đến H có vệt mùi 15 do 15 con kiến đi từ B đến H, tại hướng đến C có vệt mùi 30 do 15 kiến đi từ B đến D và 15 con đi từ D đến B thông qua C (hình 2c). Do đó khả năng kiến hướng đến chọn đường đến C, do đó số kiến mong muốn đi đến C sẽ gấp đôi số kiến đi đến H (20 con đến C và 10 con đến H). Tương tự như vậy cho 30 con kiến mới đi từ D đến B.

Quá trình sẽ liên tục cho đến khi tất cả kiến sẽ chọn đường đi ngắn nhất.

Trên đây chúng ta mô tả hành vi tìm kiếm của bầy kiến thực.Sau đây , chúng ta sẽ tìm hiểu sâu hơn về các thuật toán kiến.

Thuật toán tối ưu bầy kiến (ACO) nghiên cứu các hệ thống nhân tạo dựa vào hành vi tìm kiếm của bầy kiến thực và được sử dụng để giải quyết các vấn đề về tối ưu rời rạc.Thuật toán bầy kiến siêu tìm kiếm(ACO meta_heuristic) lần đầu tiên được Dorigo, Di Caro và Gambardella đề xuất vào năm 1999.

Metaheuristic là một tập các khái niệm về thuật toán được sử dụng để xác định các phương thức tìm kiếm thích hợp cho một tập các vấn đề khác nhau. Hay nói cách khác, một siêu tìm kiếm ( meta-heuristic) có thể coi là một phương thức tìm kiếm đa năng.



ACO là một meta-heuristic, trong đó một tập các con kiến nhân tạo phối hợp tìm kiếm các giải pháp tốt cho các vấn đề về tối ưu rời rạc. Sự phối hợp là yếu tố cối lõi của các thuật toán ACO. Các con kiến nhân tạo liên lạc với nhau thông qua trung gian mà ta thường gọi là mùi.

Các thuật toán ACO được sử dụng để giải quyết các vấn đề về tối ưu tổ hợp tĩnh và động. Các vấn đề tĩnh là các vấn đề mà ở đó các đặc tính của vấn đề là không thay đổi trong suốt quá trình giải quyết vấn đề. Còn các vấn đề động thì ngược lại là một hàm các tham số mà giá trị của nó là động hay thay đổi trong quá trình giải quyết vấn đề, ví dụ bài toán người đưa thư là một vấn đề dynamic problem

Hệ thống ACO lần đầu tiên được Marco Dorigo giới thiệu trong luận văn của mình vào năm 1992, và được gọi là Hệ thống kiến (Ant System, hay AS). AS là kết quả của việc nghiên cứu trên hướng tiếp cận trí tuệ máy tính nhằm tối ưu tổ hợp mà Dorigo được hướng dẫn ở Politecnico di milano với sự hợp tác của Alberto Colorni và Vittorio Maniezzo. AS ban đầu được áp dụng cho bài toán người du lịch (TSP) và QAP

Cũng vào năm 1992, tại hội nghị sự sống nhân tạo lần đầu tiên ở châu Âu, Dorigo và các cộng sự đã công bố bài: sự tối ưu được phân bố bởi đàn kiến.

Tiếp theo tại hội nghị quốc tế thứ hai về giải quyết các vấn đề song song trong tự nhiên ở Hà Lan (1992), ông và các cộng sự đã công bố bài: nghiên cứu về các đặc tính của một giải thuật kiến.

Kể từ năm 1995 Dorigo, Gambardella và Stützle đã phát triển các sơ đồ AS khác nhau. Dorigo và Gambardella đã đề xuất Hệ thống bầy kiến (Ant Colony System, hay ACS) trong khi Stützle and Hoos đề xuất MAXMIN Ant System (MMAS). Tất cả đều áp dụng cho bài toán người du lịch đối xứng hay không đối xứng và cho kết quả mỹ mãn. Dorigo, Gambardella and Stützle cũng đề xuất những phiên bản lai của ACO với tìm kiếm địa phưong.



Vào năm 1995, L.M. Gambardella và M. Dorigo đã đề xuất hệ thống Ant-Q, là một cách tiếp cận học tăng cường cho cho bài toán TSP.Và nó được áp dụng trong Học Máy.

Tiếp đó, vào năm 1996, trong bài báo công nghệ của mình tại Bruxelles M. Dorigo và L.M. Gambardella đã công bố hệ thống Ant Conoly System. Đây là hệ thống đề cập đến cách học phối hợp áp dụng cho bài toán TSP.

Cũng trong năm 1996 này, T. Stützle và H. H. Hoos đã đề xuất hệt thống Max-Min Ant System. Đây là một hệ thống cải tiến hệ thống AntSystem ban đầu và được đánh giá là hệ thống tính toán trong tương lai.

Sau đó, vào năm 1997, G. Di Caro và M. Dorigo đã đề xuất hệ thống AntNet. Đây là cách tiếp cận về định hướng sự thích nghi. Và phiên bản cuối cùng của hệ thống AntNet về điều khiển mạng truyền thông đã được công bố vào năm 1998.

Cũng trong năm 1997, hệ thống Rank-based Ant System, một hệ thống cải tiến hệ thống kiến ban đầu về nghiên cứu hệ thống tính toán đã được đề xuất bởi B. Bullnheimer, R. F. Hartl và C. Strauss. Phiên bản cuối cùng của hệ thống này được công bố vào năm 1999.

Vào năm 2001, C. Blum, A. Roli, và M. Dorigo đã cho công bố về hệ thống kiến mới là Hyper Cube – ACO. Phiên bản mở rộng tiếp đó đã được công bố vào năm 2004.

Hầu hết các nghiên cứu gần đây về ACO tập trung vào việc phát triển các thuật toán biến thể để làm tăng hiệu năng tính toán của thuật toán Ant System ban đầu.

Trên đây là sơ lược chung về các thuật toán kiến, mục tiếp theo sẽ mô tả về sơ đồ chung của thuật toán kiến.

# Sơ đồ chung thuật toán đàn kiến

Procedure ACO



Initial(); While (!ĐK dừng) do ConstructSolutions(); LocalSearch(); /\*Tuỳ ý, có thể có hoặc không UpdateTrails(); End; End;

trong đó:

ĐK dừng (tức là điều kiện dừng) là điều kiện đạt được khi thuật toán ở trạng thái kết thúc. Với bài toán người đưa thư thì ĐK dừng là điều kiện đạt được khi số vòng lặp của thuật toán $= \mathrm { s } \acute { \mathrm { 0 } }$ vòng lặp lớn nhất do người dùng tự định nghĩa hoặc là tất cả đàn kiến đều đi theo một đường (tức là đường đi ngắn nhất).

ConstrucSolutions() là hàm xây dựng một giải pháp có thể theo phương pháp siêu tìm kiếm(meta-heuristic), với bài toán người đưa thư thì đó là hàm xây dựng chu trình cho mỗi kiến .

UpdateTrails() là hàm cập nhật mùi cho hành trình mà kiến đã đi qua.

LocalSearch() là hàm tìm kiếm địa phương, giúp tìm ra tối ưu cục bộ.

![](images/image5.jpg)  
Hình 3. Sơ đồ chung của thuật toán bầy kiến

# Các bước giải quyết bài toán đàn kiến

Từ thuật toán trên ta có thể rút ra các bước giải quyết một bài toán ứng dụng với thuật toán đàn kiến:

Bước 1: Thể hiện bài toán trong khung của tập các thành phần và sự chuyển đổi hoặc bởi một đồ thị được đánh dấu bởi kiến đề xây dựng cách giải quyết.



Bước 2: Định nghĩa thích hợp cho mùi lạ rs là một xu hướng quyết định. Đó là một bước chủ yếu trong việc hình thanhg thuật toán ACO và xác định rõ mùi lạ không là một nhiệm vụ tầm thường và nó tính toán yêu cầu bên trong của bài toán sau đáp án.

Bước 3: Định nghĩa thích hợp kinh nghiệm cho mỗi quyết định để một con kiến có thể xây dựng cách giải quyết, ví dụ: định nghĩa thông tin kinh nghiệm rs kết hợp mỗi thành phần hoặc trạng thái chuyển đổi. Thông tin kinh nghiệm chủ yếu cho việc tìm kiếm tốt nếu thuật toán tìm kiếm vùng không có sẵn hoặc không thể ứng dụng.

Bước 4: Nếu thực hiện được, tạo ra một vùng thuật toán tìm kiếm hiệu quả cho bài toán sau đáp án bởi vì kết quả của nhiều ứng dụng ACO cho bài toán tổ hợp tối ưu NP-hard thể hiện qua sự tìm kiếm tốt nhất đạt được khi ACO có vùng lạc quan.

Bước 5: Lựa chọn một thuật toán ACO và ứng dụng nó vào những bài toán cần giải quyết.

Bước 6: Các tham số phù hợp của thuật toán ACO. Một điểm bắt đầu tốt cho tham số phù hợp là sử dụng cài đặt tham số để tìm kiếm tốt khi ứng dụng thuật toán ACO vào bài toán đơn giản hoặc các bài toán khác nhau. Một vấn đề khác chi phối thời gian trong nhiệm phù hợp là để sử dụng thủ tục động cho tham số phù hợp.

Nó nên xoá các bước tiếp có thể chỉ đưa ra một hướng dẫn sử dụng thuật toán ACO. Thêm nữa, việc sử dụng là sự kết hợp các quá trình ở đó với vài bài toán sâu hơn và hoạt động của thuật toán, vài lựa chọn ban đầu cần phải sửa lại. Cuối cùng, chúng ta muốn trên thực tế, điều quan trọng nhất của các bước là đầu tiên phải khớp bởi vì lựa chọn tồi ở trạng thái này tính không thể tính với một tham số gốc phù hợp tốt.



# Các sơ đồ thuật toán khác phát triển trên mô hình ACO

Nhiều thuật toán đã được đưa ra dựa trên mô hình thuật toán metaheuristic ACO. Trong các mô hình đưa ra để giải quyết các bài toán tổ hợp tối ưu NP-khó sau đây xin trình bày chi tiết về $5 ~ \mathrm { m } \hat { \mathrm { o } }$ hình. Các mô hình này là phát triển dựa trên mô hình thuật toán ACO cụ thể trình bày ở phần trên. Theo các nghiên cứu cho thấy khi sử dụng thuật toán bầy kiến nói chung các thông tin pheromone và heuristic có th $\acute { \hat { \mathbf { e } } }$ áp dụng cho các nút hoặc cạnh nối. Trong các thuật toán đưa ra sau đây thì thông tin pheromone và heuristic chỉ gắn với các cạnh mà thôi.

## Thuật toán Ant System (AS)

Được phát triển bởi Dorigo, Maniezzo và Colorni năm 1991, là thuật toán ACO đầu tiên. Ban đầu có 3 biến thể khác nhau là: AS-Density, ASQuantity và AS-Cycle khác nhau bởi cách thức cập nhật thông tin Pheromone.

Trong đó:

⮚ AS-Density: Thì đàn kiến sẽ đặt thêm pheromone trong quá trình xây dựng lời giải (online step-by-step pheromone update), lượng pheromone để cập nhật là một hằng số.

⮚ AS-Quantity: Thì đàn kiến sẽ đặt thêm pheromone trong quá trình xây dựng lời giải (online step-by-step pheromone update), lượng pheromone để cập nhật là phụ thuộc vào độ mong muốn (thông tin heuristic) với đoạn đường đi qua ηij.

⮚ AS-Cycle: Thông tin pheromone sẽ được cập nhật khi lời giải đã hoàn thành (online delayed pheromone update). Đây là mô hình cho kết quả tốt nhất và được coi như là thuật toán AS.



#  Quy tắc di chuyển của kiến

Trong thuật toán AS, kiến xây dựng một đường đi bắt đầu tại một đỉnh được chọn ngẫu nhiên.

Tại đỉnh i, một con kiến k sẽ chọn đỉnh j chưa được đi qua trong tập láng giềng của i theo công thức sau:

$$
p _ { i j } ^ { k } = \frac { ( \tau _ { i j } ) ^ { \alpha } ( \eta _ { i j } ) ^ { \beta } } { \sum _ { l \in N _ { i } ^ { k } } ( \tau _ { i l } ) ^ { \alpha } ( \eta _ { i l } ) ^ { \beta } } , j \in N _ { i } ^ { k }
$$

Trong đó:

$p _ { \mathrm { i j } } ^ { \mathrm { ~ k ~ } }$ : xác suát con kién k lra chon canh (i,j) $\tau _ { i j }$ : nòng do vét mùi trèn canh (i,j) : he só dièu chinh ành hróng cúa $\tau _ { i j }$ $\eta _ { i j }$ : thòng tin heuristic giúp dánh giá chính xác

Sự lựa chọn của con khi quyết định đi từ đỉnh i qua đỉnh j và được tính theo công thức:

$$
\eta _ { i j } = \frac { 1 } { d _ { i j } }
$$

${ \bf d } _ { \mathrm { i j } }$ : khoang cách giüra dinhi và dinh j $\beta$ : he só dièu chinh ành hróng cúa $\eta _ { i j }$ ${ \bf N } _ { \mathrm { i } } ^ { \bf k }$ : tàp các dinh láng gièng cuai mà con kién k

chura di qua

#  Quy tắc cập nhật thông tin mùi

Trong quá trình di chuyển tìm đường đi của đàn kiến, chúng thực hiện cập nhật thông tin mùi trên những đoạn đường mà chúng đã đi qua.



Gắn với mỗi cạnh (i,j) nồng độ vết mùi ij và thông số heuristic ij trên cạnh đó.

Ban đầu nồng độ mùi trên mỗi cạnh (i,j) được khởi tạo một hằng số c, hoặc được xác định theo công thức:

$$
\tau _ { _ { i j } } = \tau _ { 0 } = \frac { m } { C ^ { n n } } , \forall ( i , j )
$$

Việc cập nhập pherpmone được tiến hành như sau:

⮚ Đầu tiên tất cả pheromone trên các cung sẽ được giảm đi bởi một lượng:

$$
\tau _ { i j } \gets ( 1 - \rho ) . \tau _ { i j }
$$

Với $p$ trong khoảng (0,1) là tốc độ bay hơi của pheromone.

⮚ Tiếp theo mỗi con kiến trong đàn sẽ đặt thêm một lượng thông tin pheromone trên những cung mà chúng đã đi qua trong hành trình của chúng.

$$
\tau _ { i j } \gets \tau _ { i j } + \sum _ { k = 1 } ^ { m } \Delta \tau _ { i j } ^ { k }
$$

Trong đó: deta ${ \big \vert } _ { \mathrm { i j } }$ là lượng pheromone mà con kiến k đặt lên cạnh mà nó đã đi qua và được tính như sau:

$$
\Delta \tau _ { i j } ^ { k } = \left\{ \begin{array} { l l } { { 1 / C ^ { k } , \mathrm { ~ n \hat { e } u \ k i \hat { \hat { e } } n \ k q u a c u n g \left( i , j \right) ~ } } } \\ { { 0 , \mathrm { ~ n g u r o c \ l a i } } } \end{array} \right.
$$

Với: $C ^ { \mathrm { k } }$ là độ dài đường đi của con kiến thứ k sau khi hoàn thành đường đi, tức là bằng tổng các cung thuộc đường đi mà kiến đã đi qua.

## Thuật toán Ant Colony System (ACS)

Phát triển từ thuật toán AS



# # Quy tàc di chuyén cǔa kién

Trong thuật toán ACS, con kiến k đang ở đỉnh i, việc kiến chọn đỉnh j để di chuyển đến được xác định bằng quy luật như sau:

Cho ${ \bf q } _ { 0 }$ là một hằng số cho trước $( 0 { < } { \mathsf { q } } _ { 0 } { < } 1 )$ )   
Chọn ngẫu nhiên một giá trị q trong khoảng [0,1]   
Nếu q<q0 kiến k chọn điểm j di chuyển tiếp theo dựa trên giá trị lớn nhất   
của thông tin mùi và thông tin heuristic có trên cạnh tương ứng với công   
thức:

$$
j = \arg _ { l \in N _ { i } ^ { k } } \operatorname* { m a x } \bigl ( \tau _ { i l } ( \eta _ { i l } ) ^ { \beta } \bigr )
$$

Nếu ${ \tt q } > { \tt q } _ { 0 }$ kiến k sẽ chọn đỉnh j chưa được đi qua trong tập láng giềng của I theo một quy luật phân bổ xác xuất được xác định theo công thức sau:

$$
p _ { i j } ^ { k } = \frac { ( \tau _ { i j } ) ^ { \alpha } ( \eta _ { i j } ) ^ { \beta } } { \sum _ { k \in N _ { i } ^ { k } } ( \tau _ { i l } ) ^ { \alpha } ( \eta _ { i l } ) ^ { \beta } } , j \in N _ { i } ^ { k }
$$

# # Quy tàc càp nhàt thōng tin mùi

Cập nhật thông tin mùi toàn cục:

Một con kiến có đường đi tốt nhất sau mỗi lần lặp thì được phép cập nhật thông tin pheromone. Việc cập nhật được thực hiện theo công thức sau:

$$
\tau _ { i j } \gets ( 1 - \rho ) \tau _ { i j } + \rho \Delta \tau _ { i j } ^ { b s }
$$

Cập nhật thông tin mùi cục bộ:

Công thức sau:



$$
\tau _ { i j } \gets ( 1 - \rho ) \tau _ { i j } + \rho \tau _ { 0 }
$$

Với $p$ : là tham số bay hơi năm trong khoảng (0,1)

$$
\ K _ { 0 } = 1 / ( \mathrm { n C _ { n m } } )
$$

n: là số dỉnh hay là số thành phố

$C _ { \mathrm { n m } }$ : chiều dài hành trình cho bởi phương pháp tìm kiếm gần nhát

## Thuật toán Max–Min Ant System (MMAS)

Được phát triển bởi Stutzle và Hooss vào năm 1996, được mở rộng lên từ hệ thống AS. Luật di chuyển của kiến được thực hiện tương tự như trong thuật toán ACS

# + Quy tác càp nhàt thōng tin mùi

Thuật toán MMAS thực hiện việc cập nhật thông tin mùi khi toàn bộ kiến trong đàn hoàn thành lời giải và lượng thông tin mùi chỉ cập nhật trên các cạnh thuộc lời giải tối ưu nhất. Ban đầu cũng thực hiện bay hơi thông tin mùi trên các cạnh thuộc lơi giải tối ưu với một lượng được xác định tại công thức (2.4).

Lượng pheromone trên một cạnh được xác định như sau:

$$
\begin{array} { r l } & { \tau _ { i j } \gets \tau _ { i j } + \Delta \tau _ { i j } ^ { b e s t } } \\ & { \Delta \tau _ { i j } ^ { b e s t } = \left\{ 1 / C _ { b e s t } \right. \quad } & { \mathrm { n \ ' e u k i \ ' e n ~ q u a ~ c a n h ~ ( i , j ) } } \\ & { \Delta \tau _ { i j } ^ { b e s t } = \left\{ 0 \right. } \end{array}
$$

vói

Cbest là độ dài đường đi ngắn nhất của con kiến thứ k sau khi cả đàn hoàn thành đường đi.

# Khoi tao và khōi tao lai thōng tin mùi

Thuật toán MMAS đã thêm vào giá trị cận trên và giá trị cận dưới cho thông tin pheromone gọi là $\tau _ { \mathrm { m i n } }$ và $\tau _ { \mathrm { m a x } }$



Sau mỗi lần cập nhật giá trị thông tin mùi τij nếu τij < $\tau _ { \mathrm { m i n } }$ thì sẽ gán τij = τmin và nếu $\tau _ { \mathrm { i j } } > \tau _ { \mathrm { m a x } }$ thì gán $\tau _ { \mathrm { i j } } = \tau _ { \mathrm { m a x } }$

Giá trị cận trên $\tau _ { \mathrm { m a x } }$ thường được thiết lập với công thức sau:

$$
\tau _ { m a x } = \frac { 1 } { \rho C _ { b e s t } }
$$

Giá trị cận dưới $\tau _ { \mathrm { m i n } }$ được xác định bằng công thức:

$$
\tau _ { \operatorname* { m i n } } = \tau _ { \operatorname* { m a x } } / 2 \mathrm { n } .
$$

## Thuật toán Rank-Based Ant System (RBAS)

Đây cũng là một thuật toán được mở rộng phát triển từ hệ thống AS đưa ra bởi Bullnheimer, Hartl và Strauss vào năm 1997. Thuật toán này đưa vào ý tưởng xếp hạng cho các lời giải khi thực hiện cập nhật pheromone. Cụ thể như sau:

Đầu tiên, m con kiến được xếp hạng theo thứ tự giảm dần dựa theo chất lượng lời giải mà nó thu được. Ví dụ: $( \mathrm { S } _ { 1 } , \mathrm { S } _ { 2 } , \ldots \mathrm { S } _ { \mathrm { m } - 1 } , \mathrm { S } _ { \mathrm { m } } )$ trong đó $\mathrm { S } _ { 1 }$ là phương án tốt nhất.

Pheromone chỉ được đặt thêm trên các cung của б -1 con kiến có lời giải tốt nhất. Lượng pheromone cũng phụ thuộc trực tiếp vào thứ hạng sắp xếp của con kiến.

Các đoạn đường đi của lời giải tốt nhất được nhận thêm một lượng pheromone phụ thuộc vào chất lượng lời giải.

Các công thứ

$$
\begin{array} { r l } & { \mathrm { ~ s ~ n h u ~ s a u : ~ } } \\ & { \tau _ { r s }  \tau _ { r s } + \sigma . \Delta \tau _ { r s } ^ { g b } + \Delta \tau _ { r s } ^ { r a n k } . } \\ & { ~ \Delta \tau _ { r s } ^ { g b } = ~ \{ \begin{array} { l l } { f ( C ( S _ { g l o b a l - b e s t } ) ) , } & { a _ { r s } \in S _ { g l o b a l - b e s t } } \\ { 0 , } & { \mathrm { t r \ ' a i ~ } \mathrm { l a i } . } \end{array}  } \end{array}
$$

Trong đó



Tóm tắt thủ tục cập nhật pheromone của thuật toán này:

1 Procedure daemon_actions   
2 for each $S _ { k }$ do local_search $( ^ { S _ { k } }$ ) {optional}   
3 rank $( S _ { 1 } , . . . , S _ { m } )$ in decreasing order of solution   
quality into ' '1( ,..., ) S Sm   
4 if (best $( S _ { 1 } ^ { ' } , S _ { g l o b a l - b e s t } ) )$   
5 $S _ { g l o b a l - b e s t } = S _ { 1 } ^ { ' }$   
6 end if   
7 for $\mu { = } 1$ to σ-1 do   
8 for each edge $a _ { r s } \in \ S _ { \mu } ^ { ' }$ do   
9 $\tau _ { r s } = \tau _ { r s } + ( \sigma - \mu ) . f \bigl ( C \bigl ( S _ { \mu } ^ { ' } \bigr ) \bigr )$   
10 end for   
11 end for   
12 for each edge $a _ { r s } ~ \in ~ S _ { g l o b a l - b e s t }$ do   
13 $\tau _ { r s } = \tau _ { r s } + \sigma . f \Bigl ( C \bigl ( S _ { g l o b a l - b e s t } \bigr ) \Bigr )$   
14 end for   
15 end Procedure

## Thuật toán Best-Worst Ant System(BWAS)

Thuật toán được đưa ra bởi Cordon vào năm 1999. Thuật toán này bao gồm một thuật toán mở rộng khác của AS là MMAS (về luật di chuyển và việc bay hơi của pheromone). Bên cạnh đó trong thuật toán này còn quan tâm tới của việc tối ưu cục bộ một cách hệ thống để nâng cao chất lượng lời giải của con kiến. Trong thuật toán BWAS có 3 daemon action thêm vào gồm có:



Đầu tiên, áp dụng luật có tên best-worst pheromone update để tăng cường pheromone trên các đoạn đường đi qua bởi lời giải tốt nhất toàn cục (global best solution). Thêm vào đó luật này sẽ phạt những cạnh của lời giải tồi nhất trong lần lặp Scurrent-worst.

Áp dụng Pheromone trail mutation để đi theo các hướng khác nhau trong quá trình tìm kiếm.

BWAS có cơ chế khởi tạo lại thông tin pheromone khi thuật toán bị đình trệ, bằng cách thiết lập pheromone trail cho tất cả các thành phần bằng $\tau _ { 0 }$ .

Mô hình thủ tục Daemon action của thuật toán BWAS như sau:

1 Procedure daemon_actions 2 for each $S _ { k }$ do local_search $( ^ { S _ { k } } )$ 3 $S _ { c u r r e n t - b e s t } =$ best_solution $( ^ { S _ { k } } )$ 4 if (best ( current best S − , global best S − )) 5 $S _ { g l o b a l - b e s t } = S _ { c u r r e n t - b e s t }$ 6 end if 7 for each edge $a _ { r s } \in \ S _ { g l o b a l - b e s t }$ do 8 $\begin{array} { l } { { \tau _ { r s } = \tau _ { r s } + p . f \bigl ( C ( S _ { g l o b a l - b e s t } ) \bigr ) } } \\ { { \ s u m = s u m + \tau _ { r s } } } \end{array}$ 9 10 end for sum 11 threshold | |globad bestS − 12 _S worst solutioncurrent worst− = $( S _ { k }$ ) for each edge rs a current worst S  − and rs a Sglobal best − do 14  (1 ).rs rs15 end for 16 17 for each nút / component $r { \in } \{ 1 , . . . , l \}$ do 18 $z =$ generate_random_value_in_[0,1]



19 if $\scriptstyle ( z < = P _ { m } )$   
20 ${ \bf s } =$ generate_random_value_in_[1,…, 1]   
21 ${ \bf a } =$ generate_random_value_in_[0,1]   
22 if $( a = 0 )$ $\tau _ { r s } = \tau _ { r s } + m u t$   
23 else = − mut   
24 end if   
25 end for   
26 if (stagnation_condition)   
27 for each $a _ { _ { r s } }$ do $\tau _ { r s } = \tau _ { 0 }$   
28 end if   
29 end Procedure

Mục này chỉ đưa ra $5 \mathrm { m } \hat { \mathrm { o } }$ hình thuật toán ACO phát triển từ hệ thống Ant System. Nhưng đó chỉ là một số các dạng tiêu biểu của thuật toán ACO, còn tồn tại rất nhiều các biến thể khác. Và trong đồ án sẽ áp dụng thuật toán theo mô hình hệ thống MMAS để giải bài toán CPMP. Mô hình thuật toán MMAS là một trong các thuật toán hiệu quả nhất của các thuật toán bầy kiến.

# Thuật toán đàn kiến song song

Từ sơ đồ giải thuật ta nhận thấy các cá thể kiến trong giải thuật là rất độc lập với nhau và vì vậy ý tưởng song song đơn giản và hiệu quả nhất là phân chia kiến ra các bộ xử lý khác nhau , các bộ xử lý mạnh có thể nhận nhiều kiến, các bộ xử lý yếu hơn sẽ nhận ít kiến hơn. Việc phân chia như vậy sẽ làm tăng hiệu suất của giải thuật,tuy nhiên khi tới bước cập nhập ma trận mùi các bộ xử lý cần phải trao đổi dữ liệu với nhau, tùy vào thông tin được trao đổi và mô hình các bộ xử lý mà ta có các kiểu thuật toán song song khác nhau và các tham số khác nhau cho giải thuật.

All-to-all topology:Các cụm kiến gửi thông tin tới tất cả các cụm kiến khác



(Directed or undirected) ring topology: trong mô hình directed ring colony cụm kiến $( \mathrm { z } + \mathrm { l } \ \mathrm { m o d } p ) + 1$ là hàng xóm của cụm i cho tất cả các cụm kiến và trong mô hình undirected ring colony cụm kiến $( i \mathrm { ~ - ~ } 1 \mathrm { ~ m o d } p )$ $+ \nobreakspace 1 \nobreakspace$ là hàng xóm của cụm kiến   
i cho tất cả các cụm kiến.

Hypercube topology: Mô hình này yêu cầu có $p = 2 ^ { \wedge } k$ cụm kiến và mỗi cụm kiến I là hàng xóm với cụm kiến j nếu và chỉ nếu kiểu biểu diễn nhị phân của i và j chỉ khác nhau 1 bit. Vì vậy mỗi cụm kiến chỉ có k hàng xóm.

Random topology:Trong mô hình này các hàng xóm của mỗi cụm kiến được đinh nghĩa một cách ngẫu nhiên trong mỗi bước trao đổi thông tin .Có nhiều phương thức xác định hàng xóm ngẫu nhiên trong trường hợp này Cũng có thể phân biệt các giải thuật với nhau bằng loại thông tin gửi nhận qua mỗi bước lặp.

Lời giải: Trong chiến thuật này các lời giải tố đã tìm ra sẽ được gửi đi tới các cụm kiến khác .có nhiều kiểu lời giải có thể được gửi đi

Kiến: Lời giải của một con kiến từ lần lặp này được gửi tới cụm kiến khác, thông thường đây là lời giải của con kiến tốt nhất

Lời giải toàn cục tốt nhất. Lời giải tốt nhất của các cụm kiến được gửi đi cho tất cả các cụm kiến

Lời giải của hàng xóm tốt nhất . Lời giải tốt nhất của các cụm kiến được gửi tới các hàng xóm

Lời giải cục bộ tốt nhất. Lời giải cục bộ tốt nhất được gửi đi tới các hàng xóm

Vector mùi . Thay vì gửi lời giải thì vector mùi sẽ được gửi sau mỗi buớc lặp.

# Public_126 

Cũng như các khoa học khác, vật lý là khoa học dựa trên các quan sát thực nghiệm và các phép đo định lượng. Mục tiêu chính của vật lý là xác định số lượng có hạn các định luật cơ bản chi phối các hiện tượng trong tự nhiên và sử dụng chúng để phát triển các lý thuyết có thể dự đoán được kết quả của các thí nghiệm trong tương lai.

Các định luật cơ bản này được diễn đạt bằng ngôn ngữ toán học, một công cụ để để gắn kết lý thuyết với thực nghiệm.

Mỗi khi có sự không nhất quán giữa tiên đoán của lý thuyết và kết quả thực nghiệm thì cần phải đưa ra một lý thuyết mới hoặc chỉnh sửa lý thuyết đã có để loại bỏ sự không nhất quán đó. Nếu một lý thuyết chỉ được thỏa mãn trong những điều kiện nhất định thì một lý thuyết tổng quát hơn sẽ có thể thỏa mãn được mà không cần các điều kiện này. Ví dụ như các định luật chuyển động được Newton (1642-1727) khám phá mô tả chính xác chuyển động của các vật có tốc độ bình thường nhưng lại không áp dụng được cho các vật chuyển động với tốc độ tương đương với tốc độ ánh sáng. Ngược lại, thuyết tương đối hẹp của Einstein (1879-1955) cho các kết quả giống với các định luật Newton đối với tốc độ nhỏ nhưng cũng mô tả chính xác chuyển động của các vật có tốc độ gần bằng tốc độ ánh sáng. Do đó, thuyết tương đối hẹp của Einstein là một thuyết về chuyển động tổng quát hơn so với thuyết được xây dựng từ các định luật Newton.

Vật lý học cổ điển bao gồm các nguyên lý của cơ học cổ điển, nhiệt động lực học, quang học và điện từ học đã được phát triển trước năm 1900. Newton là người đã có những đóng góp quan trọng cho vật lý học cổ điển, ông cũng là một trong những người khai sinh ra phép tính vi tích phân như là một công cụ toán học. Các phát triển chủ yếu của cơ học được tiếp diễn trong thế kỷ 18, nhưng ngành nhiệt động lực học và điện từ thì phải đến nửa sau của thế kỷ 19 mới được phát triển. Nguyên nhân chủ yếu là do các thiết bị thí nghiệm thời đó quá thô sơ hoặc thiếu thốn.

Cuộc cách mạng lớn của vật lý, có liên quan với vật lý hiện đại, bắt đầu vào gần cuối thế kỷ 19. Vật lý hiện đại được phát triển là do vật lý cổ điển không thể giải thích được nhiều hiện tượng vật lý. Hai sự phát triển quan trọng nhất trong kỷ nguyên hiện đại là thuyết tương đối và cơ học lượng tử. Thuyết tương đối hẹp của Einstein không những chỉ mô tả chính xác chuyển động của các vật có tốc độ tươndg đương với tốc độ ánh sáng mà còn hiệu chỉnh một cách trọn vẹn các khái niệm truyền thống về không gian, thời gian và năng lượng. Lý thuyết này còn chỉ ra rằng tốc độ ánh sáng là giới hạn trên của tốc độ của một vật và khối lượng và năng lượng có liên hệ với nhau. Cơ học lượng tử được hình thành bởi nhiều nhà khoa học khác nhau, mô tả các hiện tượng vật lý ở cấp độ nguyên tử. Nhiều thiết bị thực tiễn đã được chế tạo dựa vào các nguyên lý của cơ học lượng tử.

Các nhà khoa học làm việc không ngừng để cải thiện hiểu biết của chúng ta về các định luật cơ bản. Nhiều tiến bộ về công nghệ trong hiện tại như tàu vũ trụ không người lái, hàng loạt ứng dụng tiềm năng trong công nghệ na nô, vi mạch và máy tính siêu tốc, kỹ thuật chụp ảnh tinh xảo dùng trong nghiên cứu khoa học và y khoa cũng như nhiều kết quả đáng kể trong kỹ thuật gien là kết quả của những nỗ lực của nhiều nhà khoa học, kỹ sư, nhà kỹ thuật. Ảnh hưởng của những phát triển và khám phá này đến xã hội của chúng ta quả thực là to lớn và chắc chắn là các khám phá và phát triển trong tương lai cũng sẽ đầy hứng thú, thách thức và mang lại nhiều lợi ích cho nhân loại.



# Các chuẩn độ dài, khối lượng và thời gian

Để mô tả các hiện tượng vật lý, ta cần phải đo lường nhiều khía cạnh khác nhau của tự nhiên. Mỗi phép đo tương ứng với một đại lượng vật lý, ví dụ như chiều dài của một vật. Các định luật vật lý được diễn đạt như là các mối quan hệ toán học giữa các đại lượng vật lý.

Trong cơ học, ba đại lượng cơ bản nhất là chiều dài, khối lượng và thời gian. Mọi đại lượng khác trong cơ học có thể được biểu diễn thông qua ba đại lượng này.

Do các quốc gia khác nhau sử dụng các chuẩn khác nhau nên cần phải có chuẩn chung cho các đại lượng. Cái được chọn làm chuẩn phải:

• có sẵn;   
• có một vài thuộc tính có thể đo lường được một cách tin cậy;   
• phải cho cùng một kết quả khi đo bởi bất kỳ ai và bất kỳ nơi nào; không thay đổi theo thời gian.

Vào năm 1960, một ủy ban quốc tế đã đưa ra một bộ các chuẩn cho các đại lượng cơ bản của khoa học. Nó được gọi là SI (Système International d’unités – Hệ đơn vị quốc tế). Bảng dưới đây là các đại lượng cơ bản nhất và đơn vị tương ứng.





$\mathrm { N a m } 1 9 6 0$ , mét được định nghĩa là khoảng cách giữa hai vạch trên một thanh platinum– iridium đặc biệt được lưu trữ tại Pháp trong điều kiện kiểm soát được.

Trong những năm 1960 và 1970, mét được định nghĩa bằng 1.650.763,73 lần bước sóng $\lambda$ của ánh sáng đỏ - cam phát ra từ đèn khí kripton-86.

Năm 1983, mét được định nghĩa là quãng đường mà ánh sáng đi được trong chân không trong khoảng thời gian 1/299.792.458 s. Trong thực tế, định nghĩa này thiết lập tốc độ ánh sáng trong chân không chính xác bằng 299.792.458 m/s. Định nghĩa này là hợp lệ trong toàn vũ trụ và dựa trên giả thiết rằng ánh sáng là như nhau $\dot { \mathbf { O } }$ khắp mọi nơi. Bảng 1.1Bảng liệt kê các giá trị ước lượng của một số chiều dài đã đo đạc được.

Bảng 1.1: Ước lượng giá trị số đo của một vài độ dài (m)   





Bảng 1.2: Ước lượng khối lượng của các vật thể khác nhau   



Bảng 1.3: Ước lượng giá trị của một số khoảng thời gian   



Tính hợp lý của các kết quả: Khi giải bài tập, bạn cần phải kiểm tra câu trả lời của mình xem chúng có hợp lý không. Việc xem lại các bảng giá trị gần đúng của độ dài, khối lượng và thời gian có thể giúp bạn kiểm tra tính hợp lý này.

Bảng 1.4: Các tiếp đầu ngữ cho bội/ước số của 10   



# Vật chất và xây dựng mô hình

Nếu nhà vật lý không thể tương tác trực tiếp với một số hiện tượng, họ thường hình dung ra một mô hình cho hệ vật lý có liên quan đến các hiện tượng này. Ví dụ, ta không thể tương tác trực tiếp với các nguyên tử vì chúng quá nhỏ. Do đó, ta xây dựng một mô hình tưởng tượng về nguyên tử như một hệ gồm một hạt nhân và một hoặc nhiều electron nằm bên ngoài hạt nhân. Khi đã xác định được các thành phần vật lý của mô hình thì ta đưa ra các tiên đoán về hành vi của chúng trên cơ sở các tương tác giữa các thành phần của hệ hoặc tương tác giữa hệ với môi trường bên ngoài hệ.

Hãy xem xét hành vi của vật chất để làm ví dụ. Hình đầu tiên của hình 1.1 cho thấy một miếng vàng đặc. Có phải miếng vàng này toàn là vàng, không có chỗ trống nào? Nếu cắt đôi miếng vàng này, hai miếng vàng thu được vẫn giữ nguyên đặc tính hóa học như miếng vàng nguyên. Chuyện gì sẽ xảy ra nếu ta cứ chia đôi các miếng này liên tục, vô hạn lần? Các miếng ngày càng nhỏ dần này có luôn là vàng hay không? Những câu hỏi như vậy đã được đặt ra từ rất lâu bởi các nhà triết học Hi Lạp. Hai trong số họ, Leucippus và học trò của ông là Democritus, không chấp nhận ý tưởng rằng sự chia cắt như vậy có thể diễn ra mãi mãi. Họ xây dựng một mô

Mòt máu vàng bao gòm nhièu nguyèn tùr vàng ò tàm nguyèn tr là hat nhàn   
Bèn trong hat nhan là   
các proton (màu cam)   
và neutron (màu xám)

Các proton và neutron duroc tao thành tùr các hat quark. Hinh này là to hop các quark tao thành proton.

Hình 1.1   
Hình 0.1

![](images/image1.jpg)

hình một mô hình vật chất với suy đoán rằng quá trình nói trên cuối cùng cũng phải kết thúc khi nó tạo ra một hạt không thể bị chia cắt được nữa. Trong tiếng Hi lạp, “atomos” có nghĩa là “không chia cắt được”. Từ tiếng Anh “atom” (nguyên tử) bắt nguồn từ cách gọi này trong tiếng Hi lạp.

Mô hình Hi lạp về cấu trúc vật chất cho rằng mọi vật chất bình thường đều có các nguyên tử (xem hình giữa của hình 1.1). Ngoài ra, không có thêm cấu trúc nào khác được xác định trong mô hình này; các nguyên tử hoạt động như các hạt nhỏ có tương tác với nhau, nhưng mô hình này không đề cập đến cấu trúc bên trong nguyên tử.

Vào năm 1897, J. J. Thomson đã xác định electron là một hạt tích điện và là một thành phần của nguyên tử. Điều này dẫn đến mô hình nguyên tử đầu tiên có cấu trúc bên trong. Mô hình này sẽ được thảo luận trong chương 42.

Sau sự phát hiện các hạt nhân vào năm 1911, người ta đã đưa ra một mô hình nguyên tử trong đó nguyên tử được tạo thành từ các electron bao quanh một hạt nhân $\dot { \mathbf { O } }$ giữa. Tuy vậy, mô hình này dẫn đến một câu hỏi mới: Hạt nhân có cấu trúc hay không? Nghĩa là, phải chăng hạt nhân là một hạt đơn lẻ hay là một tập hợp các hạt? Vào đầu những năm 1930, người ta đưa ra một mô hình mô tả hai thành phần cơ bản trong hạt nhân: proton và neutron. Proton mang điện tích dương và một nguyên tố hóa học được xác định bằng số lượng proton trong hạt nhân của nó. Con số này được gọi là nguyên tử số (atomic number) của nguyên tố. Bên cạnh nguyên tử số, một số khác, khối số (mass number), được định nghĩa bằng tổng của số proton và số neutron tạo nên hạt nhân. Nguyên tử số của một nguyên tố không bao giờ thay đổi, còn khối số có thể thay đổi.





Tuy nhiên, có phải sự phân chia vật chất đã kết thúc? Hiện nay, người ta đã biết rằng các proton, neutron và một số đông đảo các hạt ngoại lai được tạo nên từ 6 hạt khác gọi là quark, các hạt này được đặt tên là up, down, strange, charmed, bottom và top. Các hạt quark up, charmed và top có điện tích $+ 2 / 3$ điện tích của proton trong khi 3 hạt còn lại có điện tích $- 1 / 3$ điện tích của proton. Proton được tạo thành từ 2 hạt up và 1 hạt down (ký hiệu lần lượt là u và d trong hình 1.2). Tương tự, neutron được tạo thành từ 2 hạt down và 1 hạt up.

Khi học vật lý, bạn phải phát triển một tiến trình xây dựng các mô hình. Bạn sẽ được thử thách với việc giải quyết nhiều vấn đề toán học. Một kỹ thuật giải quyết bài toán quan trọng nhất là xây dựng mô hình cho vấn đề cần giải quyết:

• Xác định một hệ các thành phần vật lý cho bài toán và   
• Đưa ra dự đoán về hành vi của hệ thống trên cơ sở các tương tác giữa các thành phần của hệ hoặc tương tác của hệ này với môi trường xung quanh.

# Phân tích thứ nguyên

Trong vật lý, từ “thứ nguyên” được dùng để bản chất vật lý của một đại lượng. Ví dụ, khoảng cách giữa hai điểm có thể được đo bằng feet1, mét hay fulong2, tất cả đều là các cách khác nhau để biểu thị thứ nguyên độ dài.

Trong sách này, chúng tôi dùng các ký hiệu cho thứ nguyên độ dài, khối lượng và thời gian tương ứng là L, M và T 3. Chúng tôi cũng thường dùng cặp dấu ngoặc [ ] để biểu thị các thứ nguyên của các đại lượng. Ví dụ, $\nu$ được dùng để chỉ tốc độ, thứ nguyên của tốc độ sẽ được biểu thị là $[ \nu ] { = } \mathrm { L } / \mathrm { T }$ . Với diện tích (ký hiệu là $A$ ) thì ta có $[ A ] { = } \mathrm { L } ^ { 2 }$ . Bảng 1.5Error! Reference source not found. giới thiệu thứ nguyên của một số đại lượng.

Bảng 1.5: Các thứ nguyên và đơn vị của 4 đại lượng đã biết   



2 Fulong: đơn vị đo chiều dài, bằng $1 / 8 ~ \mathrm { d } \mathrm { \breve { a } m }$ Anh, tức khoảng $2 0 1 \mathrm { m }$ 3 Thứ nguyên của một đại lượng được viết bằng chữ viết hoa, thẳng; còn ký hiệu đại số cho đại lượng được ký hiệu bằng chữ in nghiêng: $L$ cho $\mathtt { d } \hat { \mathbf { \rho } }$ dài và $t$ cho thời gian.



hữu ích, phân tích thứ nguyên, vì các thứ nguyên có thể được xem như là các đại lượng đại số. Cần lưu ý:

• Chỉ có thể cộng hoặc trừ các đại lượng với nhau nếu chúng có cùng thứ nguyên.   
• Vế trái và vế phải của một đẳng thức (bất đẳng thức) cần phải có cùng thứ nguyên.

Tuân theo quy tắc cơ bản này, ta có thể sử dụng phép phân tích thứ nguyên để kiểm tra tính đúng đắn của một biểu thức. Một quan hệ bất kỳ chỉ có thể đúng nếu thứ nguyên của hai vế phương trình là giống nhau.

Để minh họa cho thủ thuật này, giả thiết rằng bạn quan tâm đến một phương trình về vị trí $x$ của một chiếc xe và thời gian t nếu xe khởi hành từ trạng thái đứng yên tại vị trí $\scriptstyle x = 0$ và chuyển động với gia tốc không đổi a. Biểu thức đúng cho trường hợp này là $x = \sqrt [ 1 ] { 2 } a t ^ { 2 }$ (xem chương 2). Đại lượng x ở vế trái có thứ nguyên là L. Để cho phương trình này đúng về thứ nguyên thì vế bên phải của phương trình cũng phải có thứ nguyên là L. Ta có thể tiến hành kiểm tra thứ nguyên bằng cách thay thế thứ nguyên cho gia tốc là $\mathrm { L } / \mathrm { T } ^ { 2 }$ , và thời gian là T vào phương trình. Ta được:

$$
\mathrm { L } { = } \frac { \mathrm { L } } { \chi ^ { 2 } } \mathcal { X } ^ { 2 } = \mathrm { L }
$$

Các thứ nguyên thời gian được khử đi như trên nên chỉ còn lại thứ nguyên độ dài. Hai vế trái và phải khớp với nhau.

Một thủ thuật tổng quát hơn khi sử dụng phép phân tích thứ nguyên là lập một biểu thức có dạng: $x \propto a ^ { n } t ^ { m }$

Với m, n là các số cần tìm và $\infty$ là dấu tỉ lệ. Quan hệ này chỉ đúng nếu thứ nguyên của hai vế là như nhau. Vì thứ nguyên của vế bên trái là chiều dài nên thứ nguyên của phần bên phải cũng là chiều dài. Nghĩa là:

Do gia tốc a có thứ nguyên là $\mathrm { L } / \mathrm { T } ^ { 2 }$ (xem chương 2) nên ta có:

$$
( \mathrm { L } / \mathrm { T } ^ { 2 } ) ^ { n } \mathrm { T } ^ { m } = \mathrm { L } ^ { 1 } \mathrm { T } ^ { 0 }  \mathrm { L } / \mathrm { T } ^ { m - 2 n } = \mathrm { L } ^ { 1 } \mathrm { T } ^ { 0 }
$$

Từ phương trình trên, ta dễ thấy là $n { = } 1$ và $m { = } 2$ . Tức là: $x \propto a t ^ { 2 }$

Phép phân tích thứ nguyên chỉ có một hạn chế là không kiểm tra được các hệ số bằng số trong công thức.

Các ký hiệu dùng trong công thức không nhất thiết phải là ký hiệu dùng cho thứ nguyên của đại lượng vật lý. Một số ký hiệu được dùng thường xuyên (ví dụ như t). Một đại lượng có thể được biểu diễn bởi nhiều ký hiệu (ví dụ như tọa độ, có thể dùng x, y hoặc z), tùy theo trường hợp sử dụng.



Câu hỏi 1.2: Nói rằng “Phép phân tích đơn vị có thể cho ra giá trị bằng số của các hằng số của các tỉ lệ có thể xuất hiện trong các biểu thức đại số” là đúng hay sai?

# Bài tập mẫu 1.1:

Hãy chứng tỏ rằng biểu thức $\nu = a t$ (với v là tốc độ, a là gia tốc và t là khoảng thời gian) là đúng về thứ nguyên.

# Bài tập mẫu 1.2:

Giả sử người ta bảo rằng gia tốc của một hạt chuyển động với tốc độ không đổi $\nu$ theo một đường tròn bán kính $r$ tỉ $\mathsf { l e }$ với $r ^ { n }$ và với $\nu ^ { m }$ . Hãy tìm giá trị của m và n và viết biểu thức tối giản của gia tốc.

# Giải:

Ta có thể viết biểu thức ban đầu của gia tốc với $k$ là hệ số tỉ lệ, không có thứ nguyên:

$$
a = k r ^ { n } \nu ^ { \mathrm { m } }
$$

Thay các thứ nguyên của gia tốc, tốc độ và bán kính vào, ta được:

$$
{ \frac { \mathrm { L } } { \mathrm { T } ^ { 2 } } } = \mathrm { L } ^ { n } \left( { \frac { \mathrm { L } } { \mathrm { T } } } \right) _ { } ^ { m }
$$

Cân bằng các $\mathrm { { s } \it { \tilde { 0 } } \mathrm { { m } \tilde { { u } } } }$ của L và T ta được

$$
n + m = 1 ; ~ m = 2
$$

Từ đó:

$$
n = - 1
$$

Biểu thức của gia tốc sẽ là

$$
a = k r ^ { - 1 } \nu ^ { 2 } = k \frac { \nu ^ { 2 } } { r }
$$

Trong phần $4 . 4 ~ \mathrm { v } \dot { \hat { \mathrm { e } } }$ sau, ta sẽ thấy rằng $k { = } 1$ với hệ đơn vị được chọn phù hợp. Nếu dùng hệ đơn vị khác thì $k$ sẽ khác 1. Ví dụ nếu đơn vị vận tốc là km/h và ta muốn có gia tốc tính bằng $\mathrm { m } / \mathrm { s } ^ { 2 }$ .

# Phép đổi đơn vị

Trong các bài toán, đôi khi ta phải đổi đơn vị từ một hệ đơn vị này sang một hệ đơn vị khác (ví dụ từ inch sang cm) hoặc đổi đơn vị trong cùng một hệ (ví dụ từ km sang m). Xem phụ lục A về danh sách các hệ số qui đổi.

Cũng như với thứ nguyên, có thể xem đơn vị là các đại lượng đại số và có thể ước lược



lẫn nhau trong một công thức.

Cần lưu ý là phải luôn ghi kèm đơn vị cho mỗi đại lượng, nếu cần thì ghi đơn vị trong suốt quá trình tính toán. Làm như vậy thì có thể phát hiện được các sai sót trong tính toán.



# Ước lượng và phép tính bậc độ lớn

Trong nhiều trường hợp, ta không cần phải có một con số chính xác cho đại lượng vật lý mà chỉ cần một giá trị gần đúng, biểu diễn dưới dạng số dùng trong khoa học. Giá trị ước lượng này có thể thiếu chính xác hơn nữa (more approximate) nếu được biểu diễn theo bậc độ lớn (order of magnitute). Cách tính theo bậc độ lớn như sau:

• Biểu diễn số dưới dạng khoa học: là tích của một số $x$ (có giá trị từ 1 đến 10) với một lũy thừa của $1 0 \mathrm { k e m }$ theo một đơn vị đo. (ví dụ $1 , 2 3 { \times } 1 0 ^ { - 2 } \mathrm { m } )$ (d   
• Nếu $x$ nhỏ hơn 3,162 $\left( { \sqrt { 1 0 } } \right)$ thì bậc của độ lớn là số mũ của 10 khi biểu diễn số đã cho dưới dạng khoa học.   
• Nếu $x$ lớn hơn 3,162 thì bậc của độ lớn bằng số mũ của 10 cộng thêm 1.

Ta dùng dấu $\sim$ để chỉ “cùng bậc với”. Sử dụng qui ước này để xem xét một số giá trị về độ dài, ta được kết quả như sau:

$0 , 0 0 2 \ 1 \ \mathrm { m } = 2 , 1 { \times } 1 0 ^ { - 3 } \mathrm { m } \sim 1 0 ^ { - 3 } \ \mathrm { m }$ ; (bậc độ lớn bằng số mũ của 10, trong trường hợp này là –3)

$0 , 0 0 8 \ : 6 \mathrm { m } = 8 . 6 { \times } 1 0 ^ { - 3 } \mathrm { m } \sim 1 0 ^ { - 2 } \mathrm { m } ;$ ; (bậc độ lớn bằng số mũ của 10 cộng thêm 1)

$7 2 0 ~ \mathrm { m } = 7 , 2 { \times } 1 0 ^ { 2 } \mathrm { m } \sim 1 0 ^ { 3 } ~ \mathrm { m }$ ; (bậc độ lớn bằng số mũ của 10 cộng thêm 1)

Khi sử dụng ước lượng theo bậc độ lớn thì các kết quả chỉ tin cậy được trong phạm vi một bội số của 10. Nếu một đại lượng tăng 3 bậc độ lớn thì giá trị của nó được nhân với một hệ số là $1 0 ^ { 3 } = 1$ , 000.

# Các chữ số có nghĩa

Khi đo một đại lượng nào đó, các giá trị đo được chỉ được biết đến trong giới hạn của sai số thực nghiệm. Giá trị của sai số này phụ thuộc vào nhiều yếu tố khác nhau.

• Các sai số này có thể là do dụng cụ đo, kỹ năng của người làm thí nghiệm và/hoặc số lượng phép đo được thực hiện.   
• Ta cần có một kỹ thuật để tính đến các sai số này.

Ta sẽ dụng các qui tắc về chữ số có nghĩa để ước lượng sai số trong kết quả của các phép tính.

Số chữ số có nghĩa trong một phép đo có thể mô tả được ít nhiều về sai số. Nó có liên quan với số chữ số được ghi trong kết quả của phép đo.

Ví dụ ta cần đo bán kính của một cái đĩa CD bằng thước mét. Giả sử rằng độ chính xác mà ta có thể đạt được $^ { \mathrm { l } \dot { \mathbf { a } } \pm 0 , 1 }$ cm. Nếu ta đo được $6 { , } 0 \mathrm { c m }$ thì ta chỉ có thể nói được rằng bán kính của đĩa nằm đâu đó trong khoảng 5,9 cm đến 6,1 cm. Trong trường hợp này, giá trị đo 6,0 cm có 2 chữ số có nghĩa. Lưu ý rằng chữ số được ước lượng đầu tiên cũng được tính là chữ số có nghĩa. Vì vậy ta có thể viết giá trị bán kính của đĩa là $( 6 , 0 \pm 0 , 1 )$ cm.



Chữ số có nghĩa là chữ số đáng tin. Số không (0) có thể có nghĩa hoặc không có nghĩa.

• Số 0 dùng để xác định vị trí của dấu thập phân thì không có nghĩa. Ví dụ như các số 0 trong các số 0,03 và 0,007 5 là không có nghĩa. Số chữ số có nghĩa của hai giá trị này lần lượt là 1 và 2. Tuy nhiên, số 10,0 lại có 3 chữ số có nghĩa. Nếu số 0 nằm sau các chữ số khác thì có thể bị nhầm lẫn. Ví dụ như khối lượng của một vật được ghi là 1 $5 0 0 \ \mathrm { g }$ thì các chữ số 0 có phải là số có nghĩa hay không. Để đỡ nhầm lẫn thì phải dùng dạng số khoa học. Trong trường hợp này, nếu ghi là $1 { , } 5 \times 1 0 ^ { 3 }$ thì có 2 chữ số có nghĩa. Nếu ghi là $1 { , } 5 0 \times 1 0 ^ { 3 }$ thì có 3 chữ số có nghĩa và nếu ghi $1 { , } 5 0 0 \times 1 0 ^ { 3 }$ thì có 4 chữ số có nghĩa. Các giá trị nhỏ hơn 1 cũng được xem xét với qui tắc tương tự: $2 , 3 \times 1 0 ^ { - 4 }$ (hoặc 0,000 23) thì có 2 chữ số có nghĩa, trong khi $2 { , } 3 0 \times 1 0 ^ { - }$ 4 (hoặc 0,000 230) thì có 3 chữ số có nghĩa.

Khi giải bài tập, ta thường kết hợp các đại lượng với nhau bằng các phép toán nhân, chia, cộng, trừ… Khi làm như vậy thì cần phải bảo đảm rằng kết quả có một số chữ số có nghĩa thích hợp.

• Khi nhân hoặc chia các đại lượng, số chữ số có nghĩa ở kết quả là số chữ số có nghĩa nhỏ nhất trong các giá trị tham gia vào phép tính.

Tính diện tích của một hình chữ nhật có 2 cạnh là 25,57 m và $^ { 2 , 4 5 \mathrm { m } }$ , ta có:

$$
2 5 , 5 7 \mathrm { m } \times 2 , 4 5 \mathrm { m } = 6 2 , 6 \mathrm { m } ^ { 2 }
$$

do số chữ số có nghĩa của hai thừa số lần lượt là 4 và 3 nên lấy 3 là số chữ số có nghĩa cho kết quả phép nhân.

Tính diện tích của một hình tròn bán kính 6,0 cm:

$$
A = \pi r ^ { 2 } = \pi \left( 6 { , } 0 \mathrm { c m } \right) ^ { 2 } = 1 { , } 1 { \times } 1 0 ^ { 2 } \mathrm { c m } ^ { 2 }
$$

Nếu dùng máy tính thì bạn có thể thu được kết quả là 113,097 335 5. Tất nhiên là không thể ghi hết các chữ số như vậy nên có thể là bạn sẽ ghi kết quả là $1 1 3 \mathrm { c m } ^ { 2 }$ . Kết quả này không đúng vì nó có đến 3 chữ số có nghĩa trong khi bán kính của hình tròn chỉ có 2 chữ số có nghĩa. Vì vậy, kết quả phải được ghi là $1 , 1 { \times } 1 0 ^ { 2 } \mathrm { c m } ^ { 2 }$ (chứ không phải là $1 1 0 \mathrm { c m } ^ { 2 } .$ )

• Nếu cộng và trừ các số thì kết quả sẽ lấy số chữ số thập phân nhỏ nhất trong các số hạng của phép tính.

Ví dụ: Tổng của 135 cm và 3,25 cm sẽ là:

$1 3 5 \mathrm { c m } + 3 , 2 5 \mathrm { c m } = 1 3 8 \mathrm { c m }$ (do số 135 cm không có số thập phân nào).

Tương tự như vậy, ta có: $2 3 , 2 + 5 , 1 7 4 = 2 8 , 4$ (Lưu ý là không thể ghi kết quả là 28,374 vì số 23,2 chỉ có 1 chữ số thập phân).



Qui tắc về cộng hoặc trừ có thể dẫn đến trường hợp mà số chữ số có nghĩa của kết quả không giống với số chữ số có nghĩa của các số hạng trong phép tính. Xét các phép tính dưới đây:

$$
1 , 0 0 0 \ 1 + 0 , 0 0 0 \ 3 = 1 , 0 0 0 \ 4
$$

$$
1 , 0 0 2 - 0 , 9 9 8 = 0 , 0 0 4
$$

Ở phép tính thứ nhất, số chữ số có nghĩa của kết quả là 5, trong khi số chữ số có nghĩa của các số hạng lần lượt là 5 và 1. Ở phép tính thứ 2, số chữ số có nghĩa của kết quả là 1, trong khi số chữ số có nghĩa của các số hạng lần lượt là 4 và 3.

Lưu ý: Trong sách này, các ví dụ về số cũng như các bài toán ở cuối chương sẽ dùng các số với 3 chữ số có nghĩa.

Qui tắc về làm tròn số:

• Chữ số cuối cùng được giữ lại sẽ tăng lên 1 đơn vị nếu chữ số cuối cùng bị bỏ đi lớn hơn 5. (Ví dụ, 1,346 được làm tròn thành 1,35)   
• Giữ nguyên chữ số cuối cùng được giữ lại nếu chữ số cuối cùng bị bỏ đi nhỏ hơn 5. (Ví dụ, 1,342 được làm tròn thành 1,34)   
Nếu chữ số cuối cùng được bỏ đi là 5 thì chữ số được giữ lại được làm tròn thành số chẵn gần nhất.4 (Qui tắc này được đưa ra để tránh sai số tích lũy trong một loạt phép tính số học liên tiếp).   
• Khi làm toán, nếu có nhiều phép tính trung gian thì để tránh cộng dồn sai số, ta chỉ làm tròn ở phép tính cuối cùng.

# Bài tập mẫu 1.5:

Người ta trải một tấm thảm trong phòng hình chữ nhật có các số đo chiều dài là 12,71 m và chiều rộng là 3,56 m. Hãy tìm diện tích của căn phòng.

# Giải:

Nếu nhân 12,71 m với $^ { 3 , 4 6 \mathrm { m } }$ bằng máy tính bỏ túi thì ta sẽ được kết quả là $4 3 , 9 7 6 6 \mathrm { m } ^ { 2 }$ . Ta sẽ chấp nhận bao nhiêu chữ số trong kết quả này. Áp dụng qui tắc về số chữ số có nghĩa thì con số có ít chữ số có nghĩa nhất là 3,46 m. Vì vậy ta phải biểu diễn kết quả là $4 4 , 0 \mathrm m ^ { 2 }$ .



4 Qui tắc này dựa trên lập luận là trong quá trình tính toán thì $50 \%$ các $\mathrm { s } \acute { \mathrm { o } }$ đã được làm tròn lên và $50 \%$ còn lại được làm tròn xuống. Theo qui tắc này, khi bỏ đi chữ $\mathrm { s } \acute { \circ } 5$ cuối cùng thì 2,315 và 2,325 đều được làm tròn thành 2,32.

# Tóm tắt chương 1

# Định nghĩa:

Ba đại lượng vật lý cơ bản của cơ học là độ dài, khối lượng và thời gian. Trong hệ đơn vị quốc tế, chúng lần lượt có đơn vị là mét (m), kilogram $( \mathrm { k g } )$ và giây (s). Không thể định nghĩa các đại lượng này bằng các đại lượng khác cơ bản hơn chúng.

Khối lượng riêng của một chất được định nghĩa là khối lượng của một đơn vị thể tích

$$
\rho \equiv \frac { m } { V }
$$

# Khái niệm và nguyên lý:

Phương pháp phân tích thứ nguyên là rất hữu ích đối với việc giải bài tập vật lý. Có thể xử lý các thứ nguyên như là các đại lượng đại số. Bằng cách ước lượng và tính toán theo bậc của độ lớn, ta có thể áng chừng được câu trả lời cho bài tập nếu không có đủ thông tin cần thiết để tìm ra một lời giải hoàn toàn chính xác.

Khi tính một kết quả từ một số giá trị đo mà mỗi giá trị đều có độ chính xác nhất định thì cần phải ghi kết quả với một số chính xác các chữ số có nghĩa. Khi nhân một vài đại lượng, số chữ số có nghĩa trong kết quả cuối cùng bằng số chữ số có nghĩa của đại lượng có ít chữ số có nghĩa nhất. Qui tắc này cũng áp dụng cho phép chia.

Khi cộng hoặc trừ các số, số chữ số sau dấu thập phân phải bằng số chữ số thập phân của số hạng có ít chữ số sau dấu thập phân nhất.

1. Một lốp ô tô được dùng cho 50 000 miles (dặm). Nó quay được bao nhiêu vòng trong cuộc đời của nó? Giả sử lốp xe có đường kính là 2,5 ft, chu vi khoảng 8 ft. 1 mile $= 5 2 8 0$ ft

ĐS: $1 0 ^ { 7 }$ vòng

2. Năm dương lịch, khoảng thời gian từ một Xuân phân này đến một Xuân phân tiếp theo, là cơ sở cho lịch chúng ta. Nó có 365,242 199 ngày. Tìm số giây trong một năm dương lịch.

ĐS: 31556926,0 s

3. Trong bãi đỗ xe của trường đại học cộng đồng, số xe bình thường lớn hơn số xe thể thao tiện ích (SUV) là $9 4 , 7 \%$ . Hiệu của chúng là 18. Tìm số lượng SUV trong bãi đỗ xe .

ĐS: 19

4. Bán kính của một quả cầu rắn đồng chất được đo là $( 6 , 5 0 \pm 0 , 2 0 ) \mathrm { ~ c ~ }$ m, và khối lượng của nó được đo là $( 1 , 8 5 \pm 0 , 0 2 ) \mathrm { k g }$ . Xác định khối lượng riêng của quả cầu tính bằng kilôgam trên mét khối và sai số của nó.

$$
1 , 6 \pm ~ 0 , 2 \times 1 0 ^ { 3 } ~ \mathrm { k g }
$$

5. Khoảng cách từ Mặt trời đến ngôi sao gần nhất là khoảng $4 \times 1 0 ^ { 1 6 } \mathrm { m }$ . Có thể xem dải Ngân hà là một đĩa hình trụ đường kính $\mathord { \sim } 1 0 ^ { 2 1 }$ m và độ dày ${ \sim } 1 0 ^ { 1 9 } \mathrm { m }$ . Hãy tìm số ngôi sao trong dải Ngân hà theo bậc của độ lớn. Xem khoảng cách giữa Mặt trời và ngôi sao gần nhất là khoảng cách điển hình.

ĐS: $1 0 ^ { 1 1 }$ ngôi sao.

# Public_127 

Trong vật lý, ta thường làm việc với các đại lượng có cả thuộc tính về số và về hướng đó là các đại lượng vec-tơ. Đại lượng vec-tơ được dùng nhiều trong sách này nên bạn cần phải nắm vững những kỹ thuật được trình bày trong chương này.

# Các hệ tọa độ

Các hệ tọa độ được sử dụng $\tt d \hat { e } \ m \hat { o }$ tả vị trí của một điểm trong không gian. Phần này sẽ trình bày về hệ tọa độ Descartes và hệ tọa độ cực.

### Hệ tọa độ Descartes:

Hệ tọa độ Descartes còn được gọi là hệ tọa độ vuông góc. Trong đó có hai trục tọa $\hat { \mathrm { d } } \hat { \mathrm { o } } x$ và $y$ vuông góc với nhau và giao nhau tại $\mathrm { g } \acute { \mathrm { o c } }$ tọa độ (hình 3.1).

# $3 . 1 . 2 \mathrm { H } \hat { \mathbf { e } }$ tọa độ cực

Hệ tọa độ cực bao gồm một gốc tọa độ và một đường thẳng qui chiếu. Một điểm cách gốc tọa $\mathtt { d } \hat { \mathrm { ~ o ~ } } \mathtt { m } \hat { \mathrm { ~ \rVert ~ } }$ khoảng $r$ theo hướng  tính từ đường thẳng qui chiếu (hình 3.2 a). Thường thì ta chọn trục Ox làm đường thẳng qui chiếu.

![](images/image1.jpg)  
Hình 3.1 Trong hệ tọa độ Descartes, một điểm trong mặt phẳng được gán nhãn $( x , y )$

![](images/image2.jpg)  
Hình 3.2 (a) Hệ tọa độ cực, các điểm được gán nhãn (r, θ); (b) liên hệ giữa $( x , y ) \nu \dot { a } \mathcal { ( r , \theta ) }$

Trong nhiều trường hợp, sử dụng hệ tọa độ cực sẽ dẫn đến các phép tính đơn giản hơn so với hệ tọa độ Descartes.

### Chuyển đổi từ tọa độ cực sang tọa độ Descartes:

Dựa trên tam giác vuông dựng từ $r$ và $\theta$ ta có: $x = r$ cos () y = r sin



Nếu biết trước các tọa độ x và y thì tan = y (3.4) và x x 2 + y2

# Bài tập mẫu 3.1:

Các tọa độ Descartes của một điểm trong mặt phẳng xy là $( \mathrm { x } , \mathrm { y } ) = ( - 3 . 5 0 ; - 2 . 5 0 ) \mathrm { m }$ như hình 3.3. Hãy tìm các tọa $\mathtt { d } \hat { \mathbf { \rho } }$ cực của điểm này.

# Giải:

Từ phương trình (3.4) ta có:

$$
r = \sqrt { x ^ { 2 } + y ^ { 2 } } = \sqrt { ( - 3 , 5 0 ~ \mathrm { m } ) ^ { 2 } + ( - 2 , 5 0 ~ \mathrm { m } ) ^ { 2 } } = 4 , 3 0 ~ \mathrm { m }
$$

![](images/image3.jpg)

Từ phương trình (3.3) suy ra:

$$
1 \mathsf { n } \mathsf { \theta } = \frac { y } { x } = \frac { - 2 , 5 0 \mathsf { m } } { - 3 , 5 0 \mathsf { m } } = 0 , 7 1 4 \Leftrightarrow \mathsf { \theta } = 2 1 6 ^ { \circ }
$$

Hình 3.3 Tìm các tọa độ cực.

# Đại lượng vec-tơ và đại lượng vô hướng

### Đại lượng vô hướng

Đại lượng vô hướng được xác định một cách trọn vẹn bằng một giá trị với một đơn vị đo tương ứng và không có hướng.

• Nhiều đại lượng là số luôn dương.   
• Một vài đại lượng có thể âm hoặc dương.   
• Có thể dùng các qui tắc số học để làm việc với các đại lượng vô hướng.

### Đại lượng vec-tơ

Đại lượng vec-tơ chỉ được xác định một cách trọn vẹn bởi một con số kèm theo đơn vị đo và một hướng nhất định.

Ví dụ về vec-tơ: Một hạt chuyển động từ A đến B dọc theo một đường cong (nét đứt) như hình vẽ.

Quãng đường mà hạt đi được là một đại lượng vô hướng (chính là độ dài của đường cong).   
Độ dời của chất điểm là đường thẳng liền nét từ A đến B, nó không phụ thuộc vào dạng của đường cong giữa 2 điểm A và B. Vì vậy độ dời là một vec-tơ.

![](images/image4.jpg)

Hình 3.4 Một chất điểm chuyển động từ A đến B theo đường nét đứt.



Cách trình bày vec-tơ: Trong tài liệu này, vec-tơ được thể hiện bằng một chữ cái in đậm và một dấu mũi tên trên đầu hoặc có thể không có mũi tên: A, A . Khi nói về độ lớn của vectơ, ta dùng chữ in nghiêng $A$ hoặc ghi rõ | A | .

Độ lớn của vec-tơ sẽ có một đơn vị vật lý và luôn là một số dương.   
Nếu viết tay thì phải dùng thêm dấu mũi tên.



Câu hỏi 3.1: Điều nào sau đây là đại lượng vec-tơ và điều nào là đại lượng vô hướng? (a) Tuổi của bạn, (b) gia tốc, (c) vận tốc, (d) tốc độ, (e) khối lượng.

# Một vài thuộc tính của vec-tơ

### Sự bằng nhau của các vec-tơ:

Hai vec-tơ là bằng nhau nếu chúng có cùng độ lớn và cùng hướng. Khi dịch chuyển một vec-tơ sang một vị trí mới mà vẫn song song với chính nó thì vec-tơ không thay đổi ví dụ như 4 vec-tơ trên hình 3.5.

### Phép cộng vec-tơ:

Phép cộng vec-tơ rất khác với cộng các đại lượng vô hướng.

![](images/image5.jpg)  
Hình 3.5 Bốn vec-tơ bằng nhau.

Khi cộng các vec-tơ, phải lưu ý đến hướng của chúng. Đơn vị của các vec-tơ phải giống nhau (nghĩa là chúng phải là các vec-tơ cùng loại). Không thể lấy vec-tơ độ dời cộng với vec-tơ vận tốc.

Có hai cách cộng vec-tơ: bằng hình học và bằng đại số. Cách cộng đại số là thuận tiện hơn so với cách cộng hình học (phải vẽ các vec-tơ theo tỉ lệ).

# Cộng vec-tơ theo kiểu hình học:

Khi thực hiện phép cộng vec-tơ theo kiểu hình học thì phải chọn một tỉ lệ xích. Vẽ vectơ thứ nhất với độ dài phù hợp theo hướng xác định (theo một hệ tọa độ). Vẽ vec-tơ tiếp theo sao cho $\mathrm { g } \acute { \mathrm { o c } }$ tọa độ của vec-tơ này trùng với ngọn của vec-tơ trước và các trục của hệ tọa độ của vec-tơ sau song song với các trục tọa độ của vec-tơ trước (kiểu vẽ gốc nối ngọn). Vec-tơ

tổng được vẽ từ gốc của vec-tơ đầu tiên đến ngọn của vec-tơ cuối cùng. Sau khi vẽ xong, đo độ dài của vec-tơ tổng và hướng (theo góc hợp với các trục tọa độ) của nó (xem hình 3.6).

Do phép cộng vec-tơ có tính giao hoán nên thứ tự vẽ các vec-tơ là không quan trọng. Đồng thời, do phép cộng vectơ có tính kết hợp nên khi tìm tổng của nhiều vec-tơ thì có thể gộp các vec-tơ thành nhóm một cách tùy ý. Kết quả của phép cộng không thay đổi. Ví dụ với tổng sau:

![](images/image6.jpg)  
Hình 3.6 Một số ví dụ về cộng vec-tơ



![](images/image7.jpg)  
Hình 3. 7 Cộng vec-tơ kiểu hình học



$$
\vec { \pmb { \ A } } + \left( \vec { \pmb { \ B } } + \vec { \pmb { C } } \right) = \left( \vec { \pmb { A } } + \vec { \pmb { \ B } } \right) + \vec { \pmb { C } }
$$

Có thể tìm tổng $\mathbf { B }$ và C trước rồi tìm tổng của A với $\mathbf { s } + \mathbf { c }$ . Nhưng cũng có thể tìm tổng của A và B trước rồi sau đó tìm tổng của $\mathbb { A } { + } \mathbb { B }$ với C

### Phép trừ vec-tơ:

Vec-tơ trái dấu: Vec-tơ trái dấu của một vec-tơ là một vec-tơ mà tổng của nó với vec-tơ ban đầu là một vec-tơ không. Vec-tơ trái dấu có độ lớn bằng với độ lớn vec-tơ gốc nhưng ngược chiều. Vec-tơ trái dấu của A là –A nên $\pmb { \Delta } + ( - \pmb { \Delta } ) = \pmb { 0 }$

Phép trừ vec-tơ: là trường hợp đặc biệt của phép cộng vec-tơ:  A − B = A + (−B)

Hai cách thực hiện phép trừ vectơ (hình 3.8):

• Cách 1: tìm vec-tơ trừ của vectơ B rồi tiếp tục thực hiện phép cộng với vec-tơ trừ này. Cách 2: Tìm một vec-tơ mà khi cộng vec-tơ này với vec-tơ thứ hai (nằm sau dấu trừ) thì được vec-tơ thứ nhất (nằm trước dấu trừ).

![](images/image8.jpg)  
Hình 3.8 Phép trừ vec-tơ (a) cách 1; (b) cách 2

$$
\vec { \bf A } - \vec { \bf B } = \vec { \bf C } \Rightarrow \vec { \bf C } + \vec { \bf B } = \vec { \bf A }
$$

### Phép nhân (chia) vec-tơ với một số vô hướng:

Khi nhân/chia một vec-tơ với một số vô hướng thì ta được một vec-tơ có độ lớn bằng độ lớn của vec-tơ được nhân (hoặc chia) với số vô hướng đó.

Nếu số vô hướng là số dương thì vec-tơ kết quả cùng hướng với vec-tơ ban đầu. Nếu số vô hướng là số âm thì vec-tơ kết quả ngược hướng với vec-tơ ban đầu.

Câu hỏi 3.2: Độ lớn của 2 vec-tơ A và B là $\mathrm { A } = 1 2$ đơn vị và $\mathrm { B } = 8$ đơn vị. Cặp giá trị nào có giá trị lớn nhất và nhỏ nhất có thể là độ lớn của vec-tơ $R = A + B ?$ (a) 14.4 đơn vị và 4 đơn vị, (b) 12 đơn vị và 8 đơn vị, (c) 20 đơn vị và 4 đơn vị, (d) không phải 3 cặp trên.

Câu hỏi 3.3: B cộng A bằng 0, hãy chọn 2 ý nào là đúng trong các ý sau: (a) A và B song song và cùng chiều, (b) A và B song song và ngược chiều, (c) A và B có cùng độ lớn, (d) A và B trực giao.



# Bài tập mẫu 3.2:

Một ô tô đi theo hướng bắc được $2 0 \mathrm { k m }$ , sau đó quẹo sang hướng tây theo phương hợp với phương bắc 1 góc $6 0 ^ { \mathrm { o } }$ , xe đi được $3 5 \mathrm { k m }$ trên đoạn đường này (hình 3.9). Xác định độ lớn, phương và chiều của vec-tơ độ dời của xe sau 2 đoạn đường trên.

# Giải:

![](images/image9.jpg)  
Hình 3.9 Ví dụ 3.2

Gọi A và $\vec { \textbf { B } }$ là 2 vec-tơ độ dời của xe lần lượt trong 2 đoạn đường $2 0 \mathrm { k m }$ và

Vec-tơ độ dời của 2 xe sau 2 đoạn đường trên là $\overrightarrow { R }$ . Ta có $R = \overrightarrow { A } + \overrightarrow { B }$ với độ lớn của R là:

$$
\begin{array} { r } { \mathsf { R } = \sqrt { A ^ { 2 } + B ^ { 2 } - 2 A B \cos \theta } \ = \sqrt { 2 0 ^ { 2 } + 3 5 ^ { 2 } - 2 \times 2 0 \times 3 5 \times \cos ( 1 2 0 ^ { \circ } ) } = 4 8 . 2 k n \times 3 5 \ \mathsf { R } . } \end{array}
$$

Phương của $\overrightarrow { R }$ tạo với phương bắc 1 góc β. Ta có: sin  = sin

$$
\mid \Rightarrow \sin \beta = B { \frac { \sin \theta } { R } } = 3 5 \times { \frac { \sin 1 2 0 ^ { \circ } } { 4 8 . 2 } } = 3 8 . 9 ^ { \circ }
$$

Vậy: vec-tơ độ dời của xe sau 2 đoạn đường trên có độ lớn 48.2 km, chiều hướng về phía tây, phương hợp với phương bắc $1 \mathrm { g o c } 3 8 . 9 ^ { \mathrm { o } }$ .

# Các thành phần của vec-tơ và vec-tơ đơn vị

Khi cộng các vec-tơ thì phương pháp hình học không được khuyến khích dùng trong trường hợp cần phải có độ chính xác cao hoặc trong các bài toán có không gian 3 chiều. Lúc này, ta sử dụng phương pháp thành phần. Phương pháp thành phần sử dụng các hình chiếu của vec-tơ lên các trục tọa độ.

### Các thành phần của vec-tơ:

Thành phần của vec-tơ là hình chiếu của vec-tơ này lên một trục tọa độ. Có thể biểu diễn một cách đầy đủ mọi vec-tơ theo các thành phần của nó.

![](images/image10.jpg)

![](images/image11.jpg)



Để tiện lợi thì ta sử dụng các thành phần vuông góc của vec-tơ: đó là hình chiếu của vec-tơ lên các trục tọa $\hat { \mathrm { d } } \hat { \boldsymbol { 0 } } \textbf { X }$ và y.

Hình 3.10 Phân tích vec-tơ A thành 2 thành phần $A _ { x }$ và Ay



Trên hình 3.10, các vec-tơ $\vec { \pmb { \mathsf { A } } } _ { x } , \vec { \pmb { \mathsf { A } } } _ { y }$ là các vec-tơ thành phần của $\vec { \pmb { \mathsf { A } } }$ . Các vec-tơ thành phần cũng là các vec-tơ nên chúng tuân theo các qui tắc về vec-tơ.

$A _ { x }$ và $A _ { x }$ là các số vô hướng, được gọi là các thành phần của vec-tơ $\vec { \pmb { A } }$ . Trên hình vẽ bên cạnh, dễ thấy:

$$
\vec { \mathsf { A } } = \vec { \mathsf { A } } _ { x } + \vec { \mathsf { A } } _ { y }
$$

3 vec-tơ này lập thành một tam giác vuông. Các thành phần của vec-tơ A lần lượt là:

$$
\begin{array} { r } { A _ { x } = A \mathrm { c o s } \Theta } \\ { A _ { y } = A \mathrm { s i n } \Theta } \end{array}
$$

Góc  được xác định từ trục Ox.

Các thành phần của vec-tơ là hai cạnh góc vuông của tam giác vuông có cạnh huyền là độ dài của vec-tơ. Dễ thấy:

$$
A = \sqrt { A _ { ~ x } ^ { 2 } + A _ { ~ y } ^ { 2 } }
$$

$$
\theta = \tan ^ { - 1 } \frac { A _ { y } } { A _ { x } }
$$

Trong một bài toán, một vec-tơ có th $\hat { \dot { \mathbf { e } } }$ được xác định bởi các thành phần hoặc độ dài và hướng của nó.

Các thành phần của vec-tơ có thể dương hoặc âm nhưng có cùng đơn vị với vec-tơ. Dấu của thành phần phụ thuộc vào góc (hợp bởi vec-tơ và các trục tọa độ). Hình 3.11 minh họa các trường hợp mà các thành phần vec-tơ có dấu dương, âm.

Câu hỏi 3.4: Hãy chọn từ nào phù hợp với dấu … trong câu sau: “Một thành phần của một vec-tơ … lớn hơn độ lớn của vec-tơ đó”? (a) luôn luôn, (b) không bao giờ, (c) thỉnh thoảng.

![](images/image12.jpg)  
Hình 3.11 Dấu của các thành phần của vec-tơ A

### Vec-tơ đơn vị

Các đại lượng vec-tơ thường được biểu diễn thông qua vec-tơ đơn vị.

Vec-tơ đơn vị là vec-tơ không có thứ nguyên và có độ lớn đúng bằng 1. Các vec-tơ đơn vị được dùng để mô tả hướng trong không gian và không có ý nghĩa vật lý nào khác.

![](images/image13.jpg)

Hình 3.12 Các vec-tơ đơn vị trong hệ tọa độ Descartes.   



Trong không gian 3 chiều, các vec-tơ đơn vị được ký hiệu là ˆi, ˆj, kˆ .Các vec-tơ này vuông góc với nhau từng đôi trong một tam diện thuận. Độ lớn của mỗi vec-tơ này là 1:



Xét một vec-tơ A trong mặt phẳng Xy, $\pmb { \vec { \mathbf { A } } } _ { x } = \pmb { \cal A } _ { x } \pmb { \vec { \mathbf { \tau } } }$ ˆi và Ay = Ay ˆj nên A = Ax ˆi + Ay ˆj

### Vec-tơ vị trí

Một điểm có tọa độ (x, y) trong mặt phẳng Xy của hệ tọa độ Descartes có thể được biểu diễn bởi một vec-tơ vị trí:

$$
\hat { \mathbf { r } } = x \hat { \mathbf { i } } + y \hat { \mathbf { j } }
$$

Trong cách viết này, x và y là các thành phần của vec-tơ r

### Phép cộng vec-tơ khi dùng vec-tơ đơn vị:

Khi dùng vec-tơ đơn vị, các phép tính vec-tơ sẽ đơn giản hơn. Trong mặt phẳng Xy, tổng của hai vec-tơ: $\vec { \mathsf { R } } = \vec { \mathsf { A } } + \vec { \mathsf { B } }$ với các thành phần của vec-tơ $\vec { \bf R }$ là $\begin{array} { r } { R _ { x } = A _ { x } + B _ { x } } \end{array}$ và $\begin{array} { r } { R _ { y } = A _ { y } + B _ { y } } \end{array}$

$$
\begin{array} { r } { \hat { \bf R } = \left( \hat { A } _ { x } \hat { \bf \Phi } \hat { \bf i } + \hat { A } _ { y } \hat { \bf \Phi } \hat { \bf j } \right) + \left( \hat { B } _ { x } \hat { \bf \Phi } \hat { \bf i } + \hat { B } _ { y } \hat { \bf \Phi } \hat { \bf j } \right) } \\ { \hat { \bf R } = \left( \hat { A } _ { x } + \hat { B } _ { x } \right) \hat { \bf \Phi } \hat { \bf i } + \left( \hat { A } _ { y } + \hat { B } _ { y } \right) \hat { \bf j } } \end{array}
$$

![](images/image14.jpg)  
Hình 3.13 Cộng 2 vec-tơ dùng vec-tơ đơn vị theo hình học

Suy ra độ lớn của vec-tơ $\begin{array} { r } { \vec { \textbf { R } } : R = \sqrt { R _ { x } ^ { 2 } + R _ { y } ^ { 2 } } = \sqrt { \left( A _ { x } + B _ { x } \right) ^ { 2 } + \left( A _ { y } + B _ { y } \right) ^ { 2 } } } \end{array}$

Góc hợp bởi vec-tơ tổng với trục Ox cho bởi:

$$
\mathsf { t a n } \theta = \frac { R _ { y } } { R _ { x } } = \frac { A _ { y } + B _ { y } } { A _ { x } + B _ { x } }
$$

Nếu xét trong không gian 3 chiều thì chỉ cần thêm thành phần thứ 3 của các vec-tơ.

$$
\begin{array} { l } { \vec { \bf A } = A _ { x } \hat { \bf i } + A _ { y } \hat { \bf j } + A _ { z } \hat { \bf k } } \\ { \vec { \bf B } = B _ { x } \hat { \bf i } + B _ { y } \hat { \bf j } + B _ { z } \hat { \bf k } } \end{array}
$$

Tổng của 2 vec-tơ này là:

$$
\hat { \mathbf { R } } = \left( A _ { x } + B _ { x } \right) \mathbf { \hat { i } } + \left( A _ { y } + B _ { y } \right) \mathbf { \hat { j } } + \left( A _ { z } + B _ { z } \right) \mathbf { \hat { k } } ^ { * } = R _ { x } \mathbf { \hat { i } } + R _ { y } \mathbf { \hat { j } } + R _ { z } \mathbf { k } ^ { * }
$$

Độ lớn của vec-tơ tổng: $R = \sqrt { R _ { x } ^ { 2 } + R _ { y } ^ { 2 } + R _ { z } ^ { 2 } }$ .

Nếu tính tổng của 3 vec-tơ trở lên thì ta vẫn dùng phương pháp như trên cho từng vec-tơ trong tổng. Ví dụ, với $\vec { \pmb { { \mathrm { R } } } } = \vec { \pmb { { \mathrm { A } } } } + \vec { \pmb { { \mathrm { B } } } } + \vec { \pmb { { \mathrm { C } } } }$ thì:

$$
{ \vec { \mathsf { R } } } = \left( A _ { x } + B _ { x } + C _ { x } \right) \mathbf { \hat { i } } + \left( A _ { y } + B _ { y } + C _ { y } \right) \mathbf { \hat { j } } + \left( A _ { z } + B _ { z } + C _ { z } \right) \mathbf { k } ^ { \prime }
$$



(a) A = 2iˆ + 5ˆj , (b) B = −3ˆj , (c) C = 5k



# Public_128 

Hiểu biết về các cơ sở của chuyển động trong không gian 2 chiều (từ đây gọi tắt là chuyển động hai chiều) sẽ cho chúng ta (trong các chương sau) khảo sát các tình huống khác nhau, từ chuyển động của các vệ tinh trên quỹ đạo đến chuyển động của các electron trong điện trường đều. Chúng ta sẽ bắt đầu nghiên cứu chi tiết hơn về

bản chất vec-tơ của vị trí, vận tốc và gia tốc. Sau đó sẽ xử lý chuyển động ném nghiêng và chuyển động tròn đều như là các trường hợp đặc biệt của chuyển động hai chiều. Chúng ta cũng sẽ thảo luận về khái niệm chuyển đông tương đối.

# Các vec-tơ vị trí, vận tốc và gia tốc

### Vec-tơ độ dời

Trong chương 2, ta đã thấy rằng chuyển động của một chất điểm theo một đường thẳng sẽ được xác định hoàn toàn nếu vị trí của nó được biết đến như là một hàm của thời gian. Bây giờ ta sẽ mở rộng ý tưởng này sang chuyển động 2 chiều của một chất điểm trong mặt phẳng xy. Ta bắt đầu bằng việc mô tả vị trí của một chất điểm bằng vec-tơ vị trí r , vẽ từ gốc của một hệ tọa độ đến vị trí của hạt trong mặt phẳng xy (hình 4.1).

![](images/image1.jpg)  
Hình 4.1

Tại thời điểm ti, vị trí của chất điểm là ở A, được mô tả bởi vec-tơ $\vec { \bf r } _ { \mathrm { i } }$ , tại thời điểm tf, vị trí của chất điểm là B, được mô tả bởi vec-tơ $\vec { \bf r } _ { \mathrm { f } }$ . Quỹ đạo của chất điểm là đoạn cong AB.

Vec-tơ độ dời của chất điểm được định nghĩa là hiệu của vec-tơ vị trí $\tilde { \mathbf { 0 } }$ thời điểm cuối và vec-tơ vị trí ở thời điểm đầu của chất điểm.

$$
\Delta \vec { \mathbf { r } } \equiv \vec { \mathbf { r } } _ { t } - \vec { \mathbf { r } } _ { i }
$$

Như vậy động học chuyển động hai chiều (2 chiều hoặc 3

chiều), mọi thứ đều tương tự như trong chuyển động một chiều ngoại trừ việc ta phải sử dụng trọn vẹn cách biểu diễn vec-tơ.



### Vận tốc trung bình:

Vận tốc trung bình bằng vec-tơ độ dời chia cho khoảng thời gian thực hiện độ dời đó. Hướng của vận tốc trung bình là hướng của vec-tơ độ dời.

$$
\vec { \bf v } _ { a v g } \equiv \frac { \Delta \vec { \bf r } } { \Delta t }
$$

### Vận tốc tức thời:

Vận tốc tức thời là giới hạn của vận tốc trung bình khi $\Delta t$ tiến tới không (tức là bằng đạo hàm của vec-tơ độ dời theo thời gian).

$$
\vec { \pmb { v } } \equiv | \mathbf { \operatorname* { i m } } _ { \Delta t  0 } \frac { \Delta \vec { \mathbf { r } } } { \Delta t } = \frac { d \vec { \mathbf { r } } } { d t }
$$

Vận tốc tức thời tại mỗi điểm trên quỹ đạo của chất

![](images/image2.jpg)  
Hình 4.2 Vận tốc tức thời tại điểm A có phương là đường tiếp tuyến với quỹ đạo tại điểm A.

điểm có phương là phương tiếp tuyến với quỹ đạo và có chiều là chiều chuyển động.

Độ lớn của vận tốc tức thời được gọi là tốc độ. Tốc độ là một đại lượng vô hướng.

### Gia tốc trung bình

Gia tốc trung bình của một chất điểm chuyển động được định nghĩa bằng độ biến thiên của vận tốc tức thời chia cho khoảng thời gian diễn ra sự biến thiên đó.

$$
\vec { \textbf { a } } _ { a v g } \equiv \frac { \Delta \vec { \textbf { v } } } { \Delta t } = \frac { \vec { \textbf { v _ { \mathrm { f } } } } - \vec { \textbf { v _ { i } } } } { t _ { \mathrm { f } } - t _ { \mathrm { ~ , ~ } } }
$$

Gia tốc trung bình là một đại lượng vec-tơ cùng hướng với $\Delta \vec { \mathbf { v } }$

### Gia tốc tức thời:

Gia tốc tức thời là giới hạn khi $\Delta t$ tiến đến không của ∆??ሬԦ ∆??

Gia tốc tức thời bằng đạo hàm theo thời gian của vec-tơ vận tốc.

Câu hỏi 4.1: Xét các vật điều khiển trong 1 ô tô gồm: bàn đạp ga, phanh, tay lái. Trong 3 vật này, vật nào gây ra gia tốc cho xe? (a) Cả 3 vật, (b) bàn đạp ga và phanh, (c) phanh, (d) bàn đạp ga, và (e) tay lái.



# Chuyển động hai chiều với gia tốc không đổi

### Các phương trình động học trong chuyển động hai chiều:

Nếu một chuyển động hai chiều có gia tốc không đổi, ta có thể tìm được một hệ phương trình để mô tả chuyển động đó. Các phương trình này tương tự như các phương trình động học trong chuyển động thẳng.

Có thể mô hình hóa chuyển động trong không gian 2 chiều như là hai chuyển động độc lập trong từng hướng gắn với các trục x và y. Lưu $\acute { y }$ : tác động lên chuyển động theo trục y không ảnh hưởng đến chuyển động theo trục x.

# Các phương trình động học:

Vec-tơ vị trí của một chất điểm chuyển động trong mặt phẳng xy là

$$
\hat { \mathbf { r } } { = } x \mathbf { \hat { i } } { + } y \mathbf { \hat { j } }
$$

Vec-tơ vận tốc của chất điểm được xác định bởi:

$$
\overset { \triangledown } { \boldsymbol { \nu } } = \frac { d \mathfrak { r } } { d t } = \frac { d x \cdot \mathrm {  ~ \hat { \mu } ~ } } { d t } \overset { \triangledown } { \mathbf { i } } + \frac { d y \cdot \mathrm {  ~ \hat { \mu } ~ } } { d t } \bf \hat { j } = \nabla \hat { \mu } _ { x } ^ { \mathrm {  ~ \hat { \mu } ~ } } + V _ { y } \cdot \mathrm {  ~ \hat { j } ~ }
$$

Vì gia tốc của chất điểm là hằng số nên ta tìm được biểu thức của vận tốc như là hàm của thời gian:

$$
\vec { \bf v } _ { t } = \vec { \bf v } _ { i } + \vec { \bf a } t
$$

Vị trí của chất điểm cũng được biểu diễn như là hàm của thời gian:

$$
\mathbf { \Delta } \mathbf { r } _ { } = \mathbf { r } _ { } + \mathbf { v } _ { } t + \mathbf { \Delta } \mathbf { \frac { 1 } { 2 } } \mathbf { a } t ^ { 2 }
$$

![](images/image3.jpg)

Hình 4.3 Biểu diễn các thành phần của vec-tơ (a) vị trí, (b) vận tốc trong chuyển động hai chiều có gia tốc không đổi

# Chuyển động ném nghiêng



Một vật có thể đồng thời chuyển động theo hai trục x và y. Trong phần này, ta xem xét chuyển động ném nghiêng. Phân tích chuyển động ném nghiêng của một vật sẽ đơn giản nếu chấp nhận 2 giả định:

• Gia tốc rơi tự do là hằng số trong phạm vi chuyển động và hướng xuống dưới (giống như là quả đất là phẳng trong phạm vi khảo sát, điều này là hợp lý nếu phạm vi này là bé so với bán kính của Quả đất).   
• Bỏ qua sức cản của không khí.

Phân tích chuyển động ném nghiêng: Xét một chất điểm được ném nghiêng từ gốc tọa độ với vận tốc ban đầu ??ሬ $\mathrm { h } _ { \iota } \mathrm { c } \acute { 0 }$ phương hợp với phương ngang một góc $\theta _ { \mathrm { i } }$ . Với 2 giả định nêu trên, quỹ đạo của chất điểm luôn là một parabol như trong hình 4.4. Ở điểm cao nhất của quỹ đạo, vận tốc theo phương thẳng đứng bằng 0. Gia tốc luôn bằng g tại mọi điểm trên quỹ đạo.

Cụ thể, chúng ta sẽ đi thiết lập phương trình chuyển động của chất điểm trên theo 2 phương x và y. Chuyển

![](images/image4.jpg)  
Hình 4.4 Quỹ đạo parabol của chất điểm được ném nghiêng $I$ góc $\theta _ { i }$ từ gốc tọa độ với vận tốc ban đầu $\nu _ { i }$

động của chất điểm là tổng hợp của các chuyển động theo phương $x$ và y. Vị trí của chất điểm tại thời điểm bất kỳ cho bởi:

$$
{ \vec { \mathbf { r } } } _ { t } = { \vec { \mathbf { r } } } _ { i } + { \vec { \mathbf { v } } } _ { i } t + \big / _ { 2 } { \vec { \mathbf { g } } } t ^ { 2 }
$$

Từ những phân tích trên ta viết được:

• Theo phương x: $\mathtt { a _ { X } } = 0$ và $\mathbf { V } _ { \mathbf { X i } } =$ const nên chất điểm chuyển động thẳng đều với vận tốc $v _ { x i } = v _ { i } c o s \theta _ { i }$ . Từ biểu thức (4.10), ta viết được phương trình chuyển động của chất điểm theo phương $\mathbf { X }$ ứng với hệ tọa độ đã chọn như hình 4.4 như sau:

$$
\begin{array} { r } { x _ { f } = x _ { i } + \stackrel {  } { v _ { x i } } . t + \stackrel {  } { { } _ 2 } a _ { x } t ^ { 2 } = 0 + v _ { i } c o s \theta _ { i } . t + 0 = v _ { i } c o s \theta _ { i } . t } \end{array}
$$

• Theo phương $y \colon a _ { y } = - g = c o n s t$ nên theo phương y chất điểm chuyển động thẳng biến đổi đều với vận tốc ban đầu $v _ { y i } = + v _ { i } s i n \theta _ { i }$ . Từ biểu thức (4.10), ta viết được phương trình chuyển động của chất điểm theo phương y ứng với hệ tọa độ đã chọn như hình 4.4 như sau:

$$
\begin{array} { r } { y _ { f } = y _ { i } + v _ { y i } , t + \frac { 1 } { 2 } a _ { y } t ^ { 2 } = 0 + v _ { i } s i n \theta _ { i } , t + \frac { 1 } { 2 } ( - g ) t ^ { 2 } = v _ { i } s i n \theta _ { i } , t - \frac { 1 } { 2 } g t ^ { 2 } } \end{array}
$$



của những chất điểm chuyển động ném nghiêng vẫn là phương trình bậc 2 của y phụ thuộc x theo quỹ đạo parabol.

Câu hỏi 4.2: (i) Giả sử một vật chuyển động ném nghiêng với quỹ đạo parabol như hình 4.4, tại điểm nào trên quỹ đạo của vật vec-tơ vận tốc và vec-tơ gia tốc vuông góc với nhau? (a) không có điểm nào, (b) điểm cao nhất, (c) điểm xuất phát. (ii) Với cùng lựa chọn như trên, hỏi điểm nào trên quỹ đạo của vật vec-tơ vận tốc và vec-tơ gia tốc song song với nhau?

# Tầm xa và độ cao cực đại của vật ném nghiêng:

Khi phân tích chuyển động ném nghiêng ta thường quan tâm đến hai đặc trưng: tầm xa R (là khoảng cách xa nhất theo phương ngang so với vị trí ban đầu) và độ cao cực đại $\pmb { h }$ (là khoảng cách xa nhất theo phương đứng so với vị trí ban đầu) mà vật đạt được (hình 4.5).

![](images/image5.jpg)  
Hình 4.5 Tại điểm A, chất điểm đạt độ cao cực đại. Tại

• Độ cao cực đại h: Khi chất điểm đi đến điểm A – vị trí đạt độ cao cực đại, vận tốc theo phương y của nó bằng 0. Từ phương trình (4.11), cho $\mathbf { v } _ { \mathrm { y } } = 0$ , ta suy ra thời gian mà chất điểm đi từ O đến A là: $t _ { A } = \begin{array} { c } { { v _ { i } s i n \theta _ { \underline { { i } } } } } \\ { { g } } \end{array}$ . Thay tA vào phương trình chuyển động (4.13), ta thu được biểu thức độ cao cực đại của chất điểm:

điểm $B _ { : }$ , chất điểm đạt vị trí xa nhất theo phương ngang.

$$
h = \frac { \stackrel { v ^ { 2 } s i n ^ { 2 } \theta _ { i } } { } } { 2 g }
$$

• Tầm xa $\pmb { R }$ : Khi chất điểm đến điểm B – vị trí đạt khoảng cách xa nhất theo phương ngang, tọa độ y của chất điểm bằng 0. Từ phương trình (4.14), cho $\mathbf { y } = 0$ ta suy ra biểu thức tính thời gian chất điểm đi từ O đến B. Cách khác, đối với bài toán ta đang xét, ta thấy t $_ 3 = 2 \mathrm { { t _ { A } } }$ . Thay tB vào phương trình (4.12) ta thu được biểu thức tính tầm xa:

Lưu ý: Các kết quả này (4.15) và (4.16) chỉ đúng trong trường hợp chuyển động là đối xứng. Trong trường hợp độ cao ban đầu và độ cao cuối cùng của vật khác nhau thì phải tính từ $\mathrm { g } \acute { \mathrm { o c } }$ tọa độ với cùng tốc độ ban đầu

![](images/image6.jpg)





# Public_129 

# Khái niệm về lực

Có thể phân các loại lực thành hai nhóm: (1) Lực do có tiếp xúc (lực đàn hồi của lò xo, lực căng dây, lực đàn hồi ở các điểm tiếp xúc giữa các vật…) (2) Lực của một trường lực (lực hấp dẫn, lực tĩnh điện, lực từ)

![](images/image1.jpg)  
Hình 5.1: a, b, c lực do có tiếp xúc; d, e, f lực của một trường

Bản chất vectơ của lực: Lực là đại lượng vectơ nên khi tìm lực cần chú ý đến điểm đặt, phương, chiều và độ lớn của lực. Khi tổng hợp các lực, cần chú ý qui tắc cộng vectơ.

Hình 5.2 minh họa 2 lực tác dụng vào móc của lực $\mathrm { k } \acute { \mathrm { e } }$ theo 2 cách khác nhau: 2 lực cùng phương và 2 lực vuông góc với nhau. Khi tác dụng dọc theo trục lò xo, lực $\mathrm { F } _ { 1 }$ và $\mathrm { F } _ { 2 }$ lần lượt làm lò xo giãn ra 1cm và 2cm (hình 5.2 a,b). Nhưng hai lực này tác dụng vuông góc với nhau thì lò xo giãn ra 2,24cm (hình 5.2d).

![](images/image2.jpg)  
Hình 5.2: Các lực tác dụng lên lực $k \acute { e } .$ : $a .$ . lực $F _ { I }$ ; $b .$ . lực $F _ { 2 }$ ; c. 2 lực $F _ { I }$ và $F _ { 2 }$ cùng phương chiều; d. 2 lực $F _ { I }$ và $F _ { 2 }$ vuông góc với nhau.



# Định luật Newton thứ nhất và các hệ qui chiếu quán tính

### Định luật Newton thứ nhất:

Nếu một vật không tương tác với các vật khác thì ta có thể xác định một hệ qui chiếu trong đó vật có gia tốc bằng 0.

![](images/image3.jpg)  
Hình 5.3: Miếng nhựa đặt trên đệm khí.

# ${ \bf 5 . 2 . 2 H \hat { e } }$ qui chiếu quán tính

Một hệ qui chiếu mà định luật Newton thứ nhất được thỏa mãn gọi là hệ qui chiếu quán tính.

Một dạng phát biểu khác của định luật Newton thứ nhất:

Khi không có ngoại lực tác dụng và được quan sát từ một hệ qui chiếu quán tính, một vật đứng yên sẽ vẫn đứng yên và một vật chuyển động sẽ tiếp tục chuyển động với vận tốc không đổi (tức là chuyển động với tốc độ không đổi theo một đường thẳng).

Ví dụ như khi xét một miếng nhựa tròn đặt trên bàn đệm khí, và bàn này đặt trên mặt đất thì miếng nhựa này không tương tác với vật nào khác theo phương ngang nên gia tốc của nó theo phương ngang bằng không. Nếu bàn đệm khí này được đặt trên một con tàu chuyển động thẳng đều thì ta cũng quan sát được hiện tượng tương tự. Tuy nhiên, nếu tàu chuyển động có gia tốc thì hệ qui chiếu gắn với tàu không còn là hệ qui chiếu quán tính nữa. Một người đứng trên tàu sẽ thấy miếng nhựa chuyển động có gia tốc. Hệ qui chiếu gắn với tàu là hệ qui chiếu phi quán tính. Mặc dầu vậy, một người quan sát đứng yên trên mặt đất vẫn thấy miếng nhựa chuyển động thẳng đều.

Một hệ qui chiếu chuyển động với vận tốc không đổi đối với các ngôi sao ở rất xa là một xấp xỉ tốt nhất cho một hệ qui chiếu quán tính. Trong nhiều trường hợp, Trái Đất cũng có thể xem là một hệ qui chiếu quán tính.

Khoảng trước năm 1600 thì người ta cho rằng trạng thái tự nhiên của vật chất là trạng thái nghỉ (đứng yên). Galileo là người đầu tiên đưa ra cách nhìn nhận mới về chuyển động và trạng thái tự nhiên của vật chất. Theo ông thì “Vận tốc mà ta truyền cho một vật chuyển động sẽ được bảo toàn nếu các nguyên nhân bên ngoài làm chậm chuyển động bị loại bỏ”. Lúc đó vật không tìm về “trạng thái nghỉ bản chất” nữa.



dụng lên vật đó. c) Cả (a) và (b) đều đúng. d) Cả (a) và (b) đều sai.



### Cách phát biểu khác của định luật Newton thứ nhất

Nếu không có ngoại lực tác dụng và được quan sát từ một hệ qui chiếu quán tính thì một vật đứng yên sẽ đứng yên và một vật chuyển động sẽ tiếp tục chuyển động với vận tốc không đổi (tức là chuyển động thẳng đều).

Nói cách khác, nếu không có lực tác dụng lên vật thì gia tốc của vật bằng không. Bất kỳ vật cô lập nào cũng đứng yên hoặc chuyển động thẳng đều. Khuynh hướng chống lại sự thay đổi vận tốc của một vật được gọi là quán tính.

### Định nghĩa lực

Lực là nguyên nhân làm thay đổi chuyển động của một vật

# Khối lượng

### Định nghĩa khối lượng

Khối lượng là một thuộc tính của vật xác định mức độ chống lại sự thay đổi vận tốc của nó. Đơn vị của khối lượng trong hệ đo lường quốc tế là kilôgram (kg). Các thí nghiệm đã cho thấy, dưới tác dụng của một lực cho trước thì vật có khối lượng càng lớn sẽ thu được gia tốc càng nhỏ. Giả sử cho cùng một lực tác dụng lên hai vật có khối lượng lần lượt là m1 và m2 và hai vật lần lượt thu được các gia $\vec { a _ { \mathrm { ~ 1 ~ } } }$ ??à $\vec { a _ { \mathrm { ~ } } _ { 2 } }$ . Tỷ số hai khối lượng của hai vật này được định nghĩa bằng nghịch đảo của tỷ số hai độ lớn của hai gia tốc tương ứng:

$$
\frac { m _ { 1 } } { m _ { 2 } } \equiv \frac { \pmb { a } _ { 2 } } { \pmb { a } _ { 1 } }
$$

Các kết quả thí nghiệm cho thấy: Với một lực cho trước tác dụng lên vật, độ lớn gia tốc mà vật thu được tỷ lệ nghịch với khối lượng của vật.

Khối lượng là thuộc tính cố hữu của một vật, không phụ thuộc vào môi trường xung quanh vật và phương pháp được dùng để đo lường nó. Khối lượng là đại lượng vô hướng. Khối lượng tuân theo các phép tính số học thông thường.

# Khối lượng và trọng lượng:

Khối lượng và trọng lượng (weight) là hai đại lượng khác nhau. Trọng lượng là độ lớn của lực hấp dẫn tác dụng lên vật. Trọng lượng có thể thay đổi tùy theo vị trí của vật.

Ví dụ:

• wearth = 180 lb; $\mathbf { W } _ { \mathrm { m o o n } } \sim 3 0 \mathrm { ~ l t }$ b • mearth = 2 kg; mmoon = 2 kg

# Định luật Newton thứ hai

Khi xem xét từ một hệ quy chiếu quán tính, gia tốc của một vật tỉ lệ thuận trực tiếp với



lực tổng hợp tác dụng lên vật và tỉ lệ nghịch với khối lượng của nó.

Lực là nguyên nhân của các thay đổi trong chuyển động, được đo thông qua gia tốc.

Cần lưu ý là một vật có thể chuyển động mà không cần có lực tác dụng. Không được diễn giải rằng lực là nguyên nhân của chuyển động.

Về mặt đại số thì:

$$
\vec { \mathsf { a } } \propto \frac { \sum \vec { \mathsf { F } } } { m } {  } \sum \vec { \mathsf { F } } = m \vec { \mathsf { a } }
$$

ở đây, hệ số tỉ lệ được chọn bằng 1 và các tốc độ chuyển động của các vật phải nhỏ hơn nhiều so với tốc độ ánh sáng. Trong đó, $\sum \limits _ { i = 1 } ^ { \sum \vec { F } }$ là lực tổng hợp, là tổng vectơ của tất cả các lực tác dụng lên vật (còn gọi là lực toàn phần).

Định luật Newton thứ 2 cũng có thể được biểu diễn theo các thành phần:

$$
\begin{array} { l } { \Sigma F _ { x } = m \bar { \alpha } _ { x } } \\ { \Sigma F _ { y } = m \bar { \alpha } _ { y } } \\ { \Sigma F _ { z } = m \bar { \alpha } _ { z } } \end{array}
$$

Lưu ý: ma không phải là một lực.

Tổng tất cả các lực bằng tích của khối lượng của vật với gia tốc của nó.

Đơn vị của lực: Trong SI, đơn vị của lực là newton (N)

$$
1 { \mathrm { N } } = 1 \ { \mathrm { k g } } { \cdot } { \mathrm { m } } \ / s ^ { 2 }
$$

Theo hệ đơn vị của Mỹ thì đơn vị của lực là pound (lb).

• 1 lb = 1 slug·ft / s2

Quy đổi đơn vị: $1 \mathrm { N } \sim \%$ lb

Câu hỏi 5.2: Một vật chuyển động không gia tốc. Hãy chọn phát biểu không đúng trong các phát biểu sau:a) Chỉ có một lực tác dụng lên vật đó. b) Không có lực nào tác dụng lên vật. c) Nhiều lực tác dụng lên vật nhưng các lực này triệt tiêu lẫn nhau.

![](images/image4.jpg)

Câu hỏi 5.3: Khi đẩy một vật từ trạng thái nghỉ trượt qua một mặt sàn không ma sát với lực không đổi trong khoảng thời gian Δt, kết quả vật thu được tốc độ v. Sau đó, lặp lại thí nghiệm trên với lực đẩy lớn hơn 2 lần. Hỏi để đạt được vận tốc cuối cùng như thí nghiệm trên thì thời gian đẩy vật là?a) 4Δt; b) 2 Δt; c) Δt; d) Δt.



# Lực hấp dẫn và khối lượng

Lực hấp dẫn $\vec { \mathsf { F } } _ { g }$ là lực mà Trái đất tác dụng lên một vật. Lực này hướng về tâm của Trái đất, và độ lớn của nó được gọi là trọng lượng của vật.

Theo định luật Newton thứ 2 thì:

$$
{ \vec { \mathsf { F } } } _ { g } = m { \vec { \mathsf { g } } }
$$

Do đó, trọng lượng của vật:



$$
F _ { g } = m g
$$

# Nói thêm về trọng lượng:

Do trọng lượng phụ thuộc vào gia tốc trọng trường (g) nên nó sẽ thay đổi theo vị trí.

• Càng lên cao thì g và trọng lượng càng giảm. • Điều này cũng áp dụng được cho các hành tinh khác, nhưng g thay đổi theo hành tinh nên trọng lượng cũng thay đổi từ hành tinh này sang hành tinh khác.

Trọng lượng không phải là thuộc tính cố hữu của vật. Trọng lượng là thuộc tính của một hệ các vật: vật và Trái đất. Về đơn vị thì kg không phải là đơn vị của trọng lượng. Công thức 1kg=2,2lb là công thức tương đương và chỉ đúng trên mặt đất.

# Khối lượng hấp dẫn và khối lượng quán tính:

Trong các định luật của Newton, khối lượng là khối lượng quán tính và đo bằng sự cản trở đối với sự thay đổi chuyển động của vật. Còn trong công thức (5.6) khối lượng m cho biết lực hấp dẫn giữa vật và Trái Đất. Các thí nghiệm cho thấy khối lượng quán tính và khối lượng hấp dẫn có cùng giá trị.

Câu hỏi 5.4: Giả sử rằng bạn đang gọi một cuộc điện thoại liên hành tinh với bạn của bạn ở trên Mặt Trăng. Người bạn đó kể rằng anh ta mới thắng được 1 Newton vàng trong một cuộc thi. Anh ta khuyên bạn nên tham dự cuộc thi đó phiên bản Trái Đất và nếu chiến thắng cũng được 1 Newton vàng. Hỏi nếu điều đó xảy ra, ai sẽ giàu hơn?, a) Bạn sẽ giàu hơn; b) Bạn của bạn giàu hơn; c) Cả 2 giàu bằng nhau.

# Định luật Newton thứ 3

Nếu hai vật tương tác với nhau, lực $\vec { \mathsf { F } } _ { 1 2 }$ do vật 1 tác dụng lên vật 2 bằng về độ lớn nhưng ngược chiều với lực $\vec { \mathsf { F } } _ { 2 1 }$ do vật 2 tác dụng lên vật 1.

$$
\vec { \pmb { { \mathsf { F } } } } _ { 1 2 } = - \vec { \pmb { { \mathsf { F } } } } _ { 2 1 }
$$

Lưu ý về ký hiệu: $\vec { \mathsf { F } } _ { \mathsf { A B } }$ là lực do A tác dụng lên B.

Một cách phát biểu khác của định luật:

Lực tác dụng và lực phản tác dụng (phản lực) bằng nhau về độ lớn nhưng ngược chiều.

![](images/image5.jpg)

• Một trong hai lực là lực tác dụng, lực kia là phản lực. Lực và phản lực phải tác dụng lên hai vật khác nhau và cùng loại với nhau.



Ví dụ 1 về lực – phản lực: Ở hình 5.5, hai vật tác dụng vào nhau bởi các lực có độ lớn bằng nhau nhưng ngược chiều nhau.



Ví dụ 2 về lực – phảnlực: Trong hình 5.6a ở trên, lực pháp tuy $\mathrm { \hat { e } n ^ { 1 } }$ (normal force) do mặt bàn tác dụng lên màn hình $\vec { \boldsymbol { \mathsf { m } } } = \vec { \boldsymbol { \mathsf { F } } } _ { \mathrm { t m } } ,$ ) là phản lực của lực tác dụng của màn hình lên mặt bàn ( $\vec { \mathsf { F } } _ { \mathsf { m t } } ^ { \mathrm { ~ ~ } } ,$

![](images/image6.jpg)  
Hình 5.6: Các lực tác dụng lên một màn hình máy tính được đặt nằm yên trên một mặt bàn

Lực tác dụng của Trái đất lên màn hình ( $\vec { \mathsf { F } } _ { \mathfrak { g } } = \vec { \mathsf { F } } _ { \mathsf { E m } } .$ ) có độ lớn bằng với lực mà màn hình tác dụng lên Trái đất $( \vec { \pmb { { \mathsf { F } } } } _ { \mathsf { m E } } )$ ) nhưng ngược chiều.

Khi giải toán bằng cách vận dụng các định luật của Newton, ta có thể vẽ các lực tác dụng lên vật như trong hình b (còn gọi là sơ đồ lực). Một cách khác là ta có thể vẽ sơ đồ lực trong đó sử dụng mô hình chất điểm cho vật, ta được một sơ $\mathtt { d } \overset { \mathtt { \backslash } } { \mathtt { d } }$ như trong hình c (gọi là free-body diagram).

Khi vẽ các sơ đồ, cần lưu ý là chỉ vẽ những lực tác dụng lên vật đang xét (kể cả các lực do trường lực gây ra). Các lực tác dụng lên vật xem như là tác dụng lên chất điểm thay thế cho vật. Sơ đồ này giúp ta tách các lực tác dụng lên vật đang xét mà bỏ qua các lực khác khi phân tích.

Câu hỏi 5.5: i) Nếu một con ruồi va chạm vào kính chắn gió của một chiếc xe buýt đang chạy rất nhanh, thì lực nào sau đây lớn hơn? a) của con ruồi tác dụng vào xe, b)của xe buýt tác dụng vào ruồi, c)2 vật tác dụng các lực bằng nhau.

ii) Vật nào có gia tốc lớn hơn? a) Con ruồi, b) Xe buýt, c) 2 vật có gia tốc bằng nhau.



# Các mô hình phân tích sử dụng định luật 2 Newton

Trong phần này, ta thảo luận về hai mô hình phân tích để giải toán trong đó vật cân bằng hoặc chịu tác dụng của các lực không đổi. Để giải các bài toán ta đơn giản hóa mô hình bằng các giả định sau:

• Các vật có thể được mô hình hóa thành các chất điểm (particle).   
• Chỉ quan tâm đến các ngoại lực tác dụng lên vật (có thể bỏ qua phản lực – vì phản lực tác dụng lên vật khác).   
• Tạm thời bỏ qua ma sát ở các bề mặt.   
Khối lượng của các sợi dây là không đáng $\mathrm { k } \mathring { \mathrm { e } }$ : Lực của dây tác dụng lên vật hướng ra xa vật và song song với dây. Khi dây được buộc vào vật và kéo vật đi thì độ lớn của lực này là lực căng dây

# Mô hình phân tích: Hạt ở trạng thái cân bằng

Nếu gia tốc của một vật (xem là một chất điểm) bằng không, vật được gọi là ở trạng thái cân bằng. Mô hình này gọi là mô hình chất điểm $\dot { \mathbf { O } }$ trạng thái cân bằng. Về mặt toán học, lực tổng hợp tác dụng lên vật bằng không:

$$
\sum \vec { \mathbf { F } } = 0
$$

hay $\sum F _ { x } = 0$ và $\sum F _ { y } = 0$

Ví dụ về cân bằng: một cái đèn được treo bằng một dây xích nhẹ (hình 5.7). Các lực tác dụng lên đèn $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ :

![](images/image7.jpg)  
Hình 5.7: Một chiếc đèn được treo trên trần nhà nhờ sợi xích.

• Lực hấp dẫn hướng xuống dưới • Lực căng của dây xích hướng lên trên.

Áp dụng điều kiện cân bằng, ta được

$$
\sum F _ { y } = 0  T - F _ { g } = 0  T = F _ { g }
$$

# Mô hình phân tích: Hạt dưới tác dụng của một lực tổng hợp

Nếu một vật được mô hình hóa như một chất điểm chịu một gia tốc, phải có lực tổng hợp khác không tác dụng lên nó. Mô hình dùng trong trường hợp này là mô hình chất điểm dưới tác dụng của một lực tổng hợp. Ta giải bài toán theo các bước sau:

• Vẽ sơ đồ lực. • Viết định luật 2 Newton: $\sum { \vec { F } } = m { \overset {  } { . } }$ • Xét theo các phương x, y.



Một người kéo một cái thùng như hình 5.8 a. Các lực tác dụng lên thùng: lực căng dây T , trọng lực $\mathsf { \Pi } _ { \mathsf { S } _ { g } }$ , và phản lực pháp tuyến n tác dụng bởi sàn nhà.



Áp dụng định luật 2 Newton theo các phương x, y:

$\sum F _ { x } = T = m \pmb { a } _ { x }$ ${ \sum F _ { y } = n - F _ { g } = 0 \to n = F _ { g } }$

Giải hệ phương trình theo các ẩn.

Nếu lực căng dây là không đổi thì gia tốc $a$ là hằng số, ta có thể áp dụng các phương trình động học $\tt d \hat { e } \ m \hat { o }$ tả đầy đủ hơn về chuyển động của thùng.

# Lưu ý $\nu \dot { \hat { e } }$ phản lực pháp tuyến n :

Lực pháp tuyến không phải là luôn bằng trọng lực tác dụng lên vật. Ví dụ như trong hình bên cạnh thì

$$
\sum F _ { y } = n - F _ { g } - F = 0 \ { \mathrm { n } } { \hat { \mathrm { e } } } { \mathrm { n } } \colon \ n = m g + F
$$

Nó cũng có thể nhỏ hơn trọng lực.

Gợi ý để giải toán: Áp dụng các định luật Newton

# Khái niệm hóa:

• Vẽ một sơ đồ • Chọn hệ tọa độ thích hợp cho mỗi vật

# Phân loại:

• Mô hình chất điểm cân bằng: $\sum \vec { \mathbf { F } } = 0$ • Mô hình chất điểm chịu tác dụng của lực tổng hợp: $\sum \vec { \mathbf { F } } = m \vec { \mathbf { a } }$

# Phân tích:

• Vẽ sơ đồ lực cho mỗi vật • Chỉ vẽ các lực tác dụng lên vật • Tìm các thành phần theo các trục tọa độ Bảo đảm rằng các đơn vị là nhất quán • Áp dụng các phương trình thích hợp dưới dạng thành phần • Giải phương trình để tìm các ẩn số 2025-09-

# Hoàn thành bài giải

• Kiểm tra các kết quả xem có phù hợp với sơ đồ lực không • Kiểm tra các giá trị đặc biệt

![](images/image8.jpg)

![](images/image9.jpg)  
Hình 5.8: Một cái hộp được kéo trên mặt sàn không ma sát.



# Bài tập mẫu 5.2: đèn giao thông

Một hộp đèn giao thông có trọng lượng $1 2 2 \mathrm { { N } }$ được treo trên một sợi dây buộc vào hai sợi dây khác như hình 5.10a. Các sợi dây phía trên không chắc bằng dây thẳng đứng nên sẽ bị dứt nếu lực căng lớn hơn 100 N. Hỏi hộp đèn có đứng yên được không hay là một trong các sợi dây sẽ bị đứt.



![](images/image10.jpg)  
Hình 5.10: Đèn giao thông được treo nhờ các sợi dây cáp

Giải

Khái niệm hóa. Hộp đèn giao thông   
Giả thiết là các sợi dây không bị đứt   
Không có cái gì chuyển động   
Phân loại. Bài toán như là một bài toán về cân bằng   
Không có chuyển động, vậy gia tốc bằng không   
Mô hình chất điểm cân bằng

# Phân tích.

Vẽ sơ đồ các lực tác dụng lên hộp đèn

Vẽ sơ đồ lực tác dụng lên nút buộc ở vị trí các dây nối với nhau: Nút buộc là điểm phù hợp để chọn vì mọi lực ta quan tâm tác dụng dọc theo các đường dây sẽ đi đến nút buộc.

Áp dụng các phương trình cân bằng cho nút buộc

Với hộp đèn, ta có:

$$
\sum F _ { y } = 0 \to T _ { 3 } - F _ { g } = 0 \mathrm { ~ h a y ~ } T _ { 3 } = F _ { g }
$$

Với nút buộc:



$$
\sum F _ { x } = - T _ { 1 } { \cos } \theta _ { 1 } + T _ { 2 } { \cos } \theta _ { 2 } = 0
$$

$$
\sum F _ { y } = T _ { 1 } \mathsf { s i n } \theta _ { 1 } + T _ { 2 } \mathsf { s i n } \theta _ { 2 } - F _ { g } = 0
$$



Giải các phương trình, ta được:

$$
\begin{array} { l } { { T _ { 1 } = \displaystyle \frac { 1 2 2 \mathsf { N } } { \mathsf { s i n } 3 7 , 0 ^ { \circ } + \mathsf { c o s } 3 7 , 0 ^ { \circ } \mathsf { t a n } 5 3 , 0 ^ { \circ } } = 7 3 , 4 \mathsf { N } } } \\ { { \ } } \\ { { T _ { \phantom { \circ } 2 } = ( 7 3 , 4 \mathsf { N } ) \displaystyle \left( \displaystyle \frac { \mathsf { c o s } 3 7 , 0 ^ { \circ } } { \mathsf { c o s } 5 3 , 0 ^ { \circ } } \right) = 9 7 , 4 \mathsf { N } } } \end{array}
$$

# Bài tập mẫu 5.3: Mặt phẳng nghiêng

Một chiếc xe khối lượng m đỗ trên một đường dốc nghiêng có đóng băng như trong hình 5.11a.

(A) Tìm gia tốc của xe, giả thiết mặt đường không có ma sát

Giải:

Khái niệm hóa: dùng hình 5.11a để khái niệm hóa tình huống của bài toán. Từ kinh nghiệm hằng ngày, ta biết rằng một chiếc xe trên dốc nghiêng sẽ chuyển động nhanh dần xuống dưới.

Phân loại: đây là chất điểm dưới tác dụng của lực tổng hợp do xe chuyển động có gia tốc.

Phân tích: Các lực tác dụng vào vật:

![](images/image11.jpg)  
Hình 5.11: Một chiếc xe hơi trên mặt phẳng nghiêng không ma sát

Phản lực vuông góc với mặt nghiêng.

Trọng lực hướng thẳng đứng xuống dưới.

Chọn hệ trục tọa độ với x dọc theo mặt nghiêng và y vuông góc với mặt nghiêng.

Thay trọng lực bởi các thành phần của nó (theo x và y).

Áp dụng mô hình chất điểm chuyển động dưới tác dụng của lực tổng hợp theo phương x và chất điểm cân bằng theo phương y.

$$
\begin{array} { l } { { \sum F _ { x } = m g \sin \theta = m a _ { x } } } \\ { { \sum F _ { y } = n - m g \cos \theta = 0 } } \end{array}
$$



Giải phương trình thứ nhất, ta được $\mathfrak { a } _ { x } = \mathfrak { g }$ sin



(B) Giả sử xe được thả từ trạng thái nghỉ từ đỉnh dốc và khoảng cách từ cản trước của xe đến chân dốc là d. Xe phải mất bao lâu để cản trước của nó chạm chân dốc và tốc độ của xe lúc đến chân dốc.

# Giải:

Đây là nội dung liên quan đến phần động học. Dùng gia tốc tìm được ở câu a để thay vào các phương trình động học. Từ đó tìm được:

$$
t = { \sqrt { \frac { 2 d } { g \sin \theta } } } \ { \mathrm { \ v { \dot { a } } } } \ V _ { x f } = { \sqrt { 2 g d \sin \theta } }
$$



# Trường hợp có nhiều vật:

Khi có hai hay nhiều vật kết nối với nhau hoặc tiếp xúc nhau, có thể áp dụng các định luật Newton cho hệ như một vật tổng thể hay từng vật riêng rẽ. Ta có thể chọn một cách để giải bài toán và dùng cách khác để kiểm tra lại kết quả.

# Các lực ma sát

Khi một vật chuyển động trên bề mặt hoặc xuyên qua một môi trường nhớt thì sẽ xuất hiện sức cản chuyển động. Đó là do các tương tác giữa vật và môi trường quanh nó. Sức cản này được gọi là lực ma sát.

### Lực ma sát nghỉ (tĩnh)

Lực ma sát nghỉ giữ cho vật không chuyển động. Chừng nào vật chưa chuyển động thì lực ma sát nghỉ đúng bằng lực tác động từ bên ngoài $f _ { \mathrm { s } } = \mathrm { F }$

Nếu F tăng thì fs tăng và ngược lại.

Gọi $\mu _ { s }$ là hệ số ma sát nghỉ thì $f _ { s } \leq \mu _ { s } n$

• Lưu ý: dấu bằng xảy ra khi các mặt bắt đầu trượt lên nhau.

### Lực ma sát trượt (động)

![](images/image12.jpg)  
Hình 5.14: Kéo một vật bắt đầu chuyển động khi thắng được lực ma sát nghỉ.

Lực ma sát trượt tác dụng khi vật chuyển động.

Hệ số ma sát trượt $\mu _ { k }$ có thể thay đổi theo tốc độ của vật, tuy nhiên, ta bỏ qua sự thay đổi này.

$$
f _ { k } = \mu _ { k } n
$$

Khảo sát lực ma sát: Để khảo sát, ta tăng dần độ lớn của ngoại lực F và ghi lại giá trị của lực ma sát. Chú ý thời điểm vật bắt đầu trượt. Đồ thị biểu diễn quan hệ giữa lực ma sát và ngoại lực cho trên hình 5.16c.

# Lưu ý:

• Các phương trình này chỉ quan tâm đến độ lớn của các lực, chúng không phải là phương trình vec-tơ.   
Với ma sát nghỉ $( f _ { s } )$ , dấu bằng chỉ đúng khi vật sắp chuyển động, các bề mặt sắp trượt lên nhau. Nếu các bề mặt chưa trượt lên nhau thì dùng dấu nhỏ hơn   
• Hệ số ma sát phụ thuộc vào các mặt tiếp xúc.   
• Lực ma sát nghỉ (tĩnh) thường lớn hơn lực ma sát trượt (động).



• Hướng của lực ma sát ngược với hướng của chuyển động và song song với các mặt tiếp xúc. • $\mathrm { H } \hat { \mathrm { e } }$ số ma sát hầu như không phụ thuộc vào diện tích mặt tiếp xúc.



### Ma sát trong các bài toán dùng các định luật Newton

Ma sát là một lực, do đó chỉ cần thêm nó vào trong các định luật Newton.

Các qui tắc về ma sát cho phép ta xác định hướng và độ lớn của lực ma sát.

# Bài tập mẫu 5.6: thí nghiệm xác định s và k

Một khối hộp đang nằm trên một mặt nghiêng như hình 5.15. Nâng dần góc nghiêng cho đến khi hộp bắt đầu trượt. Chứng tỏ rằng có thể tìm được hệ số ma sát nghỉ $\mu _ { \mathrm { s } }$ theo góc tới hạn .

# Giải:

Khái niệm hóa: Tưởng tượng rằng khối hộp có xu hướng trược xuống dưới do tác dụng của trọng lực. Hộp trượt xuống nên ma sát sẽ hướng lên phía trên.

Phân loại: Khối hộp chịu tác dụng của nhiều lực khác nhau, tuy nhiên, nó chưa trượt xuống dốc nên đây là bài toán chất điểm cân bằng.

![](images/image13.jpg)  
Hình 5.15: Một khối hộp trượt trên một mặt phẳng nghiêng có ma sát

Phân tích: Sơ đồ lực trên hình 5.15 cho thấy các lực tác dụng vào hộp gồm: trọng lực mg , phản lực n và lực ma sát nghỉ $\vec { \pmb { \mathsf { f } } } _ { s }$ . Chọn trục $x$ dọc theo mặt nghiêng và y vuông góc với mặt nghiêng.

$$
\begin{array} { c } { { \sum F _ { x } = m g \mathbf { s } \mathsf { i } \mathsf { n } \theta - \pmb { f } _ { s } = 0 } } \\ { { \sum F _ { y } = n - m g \cos \theta = 0 } } \end{array}
$$

Giải hệ phương trình ta có $\pmb { f _ { s } } = m g \mathsf { s i n } \theta = n$ tan

Với góc nghiêng tới hạn $\theta _ { \mathrm { c } }$ thì lực ma sát nghỉ bằng $f _ { s } = \mu _ { s } n$ nên $\mu _ { s } = \mathsf { t a n } \theta _ { c }$ .

Hoàn tất: Khi hộp bắt đầu trượt thì $\theta \geq \theta _ { \mathrm { c } }$ . Hộp trượt có gia tốc xuống dưới thì lực ma sát trượt $\pmb { f } _ { k } = \mu _ { k } \pmb { n }$ . Tuy nhiên, nếu giảm góc q thì vật cũng có thể trượt xuống, nếu vật trượt thẳng đều thì $\mu _ { k } = \mathsf { t a n } \theta _ { c } ^ { \prime }$ với ${ \theta _ { c } } ^ { \prime } < \theta _ { c }$

Lưu ý: Với bố trí thí nghiệm như trên thì ta có thể xác định hệ số ma sát bằng thực nghiệm: $\mu = \tan \theta$

• Với $\mu _ { s }$ , sử dụng góc nghiêng khi khối hộp bắt đầu trượt.   
• Với $\mu _ { k }$ , sử dụng góc nghiêng khi mà khối hộp trượt xuống với tốc độ không đổi.



# Bài tập mẫu 5.7: Một quả bóng khúc côn cầu đang trượt



Một quả bóng khúc côn cầu trượt trên mặt băng với tốc độ ban đầu là ${ 2 0 , 0 } \mathrm { m } / \mathrm { s }$ . Quả bóng trượt được $1 1 5 ~ \mathrm { m }$ trước khi dừng lại. Hãy xác định hệ số ma sát trượt giữa quả bóng và băng.

# Giải:

Khái niệm hóa: Giả sử quả bóng chuyển động sang phải như hình 5.16. Lực ma sát trượt tác dụng về bên phải và làm quả bóng chuyển động chậm lại cho đến khi dừng hẳn.

Phân loại: Các lực tác dụng lên quả bóng như trong hình 5.16, nhưng bài toán lại cho các biến số về động học. Do đó, có thể phân loại bài toán bằng nhiều cách khác nhau. Theo phương thẳng đứng, đây là bài toán chất điểm cân bằng (tổng lực tác dụng lên vật bằng 0). Theo phương ngang, là bài toán chất điểm có gia tốc không đổi.

![](images/image14.jpg)  
Hình 5.16: quả khúc con cầu trượt có ma sát trên mặt băng

Phân tích: Vẽ sơ đồ lực tác dụng lên vật, lưu ý đến lực ma sát (ngược chiều chuyển động, song song với mặt tiếp xúc).

Áp dụng mô hình chất điểm chịu tác dụng của lực tổng hợp theo phương x:

$$
\sum F _ { x } = - f _ { k } = m \pmb { a } _ { x }
$$

Áp dụng mô hình chất điểm cân bằng theo phương y:

$$
\sum F _ { y } = n - m g = 0
$$

Giải hệ phương trình, với định nghĩa lực ma sát trượt, ta được:

$$
\mathsf { a } _ { x } = - \mu _ { k } \mathsf { g }
$$

Sau khi tìm được gia tốc, áp dụng mô hình động học, ta tìm được

Hoàn tất: Lưu ý rằng $\mu _ { k }$ không có thứ nguyên và có giá trị bé, không đổi với một vật trượt trên mặt băng.

Bài tập mẫu 5.8: Gia tốc của hai vật nối với nhau khi có ma sát



Một khối hộp có khối lượng m2 nằm trên một mặt ngang, nhám được nối với một quả cầu khối lượng m1 bằng một sợi dây nhẹ vắt qua một ròng rọc nhẹ, không ma sát như trong hình 5.20a. Tác dụng vào khối hộp một lực có độ lớn $F$ hợp với phương ngang một góc  và khối hộp chuyển động sang phải. $\mathrm { H } \hat { \mathbf { e } }$ số ma sát trượt giữa khối hộp và mặt ngang là $\mu _ { k }$ Tìm độ lớn của gia tốc của hai vật.



![](images/image15.jpg)  
Hình 5.17: hệ 2 vật nối nhau khi có ma sát.

Giải:

Khái niệm hóa: Hình dung xem chuyện gì xảy ra khi tác dụng lực F vào khối hộp. Giả sử lực đủ lớn hơn lực ma sát nghỉ nhưng không đủ lớn để nhất hộp lên, hộp sẽ trượt sang phải và quả cầu được kéo lên.

Phân loại: Bài toán này là bài toán hai chất điểm dưới tác dụng của lực tổng hợp. Vì khối hộp không bị nhấc lên nên theo phương thẳng đứng, khối hộp được xem là chất điểm cân bằng.

Phân tích: Vẽ sơ đồ lực cho từng vật (hình 5.17b và 5.17c).

Áp dụng mô hình chất điểm chịu tác dụng của lực tổng hợp cho khối hộp theo phương ngang:

$$
\sum F _ { x } = F { \cos \theta } - f _ { k } - T = m _ { 2 } \bar { \alpha } _ { x } = m _ { 2 } \bar { \alpha }
$$

Áp dụng mô hình chất điểm cân bằng cho khối hộp theo phương thẳng đứng

$$
{ \sum } F _ { y } = \eta + F { \sin } \Theta - m _ { 2 } g = 0 \ ( 2
$$

Áp dụng mô hình chất điểm chịu tác dụng của lực tổng hợp cho quả cầu theo phương thẳng đứng:

$$
{ \sum } F _ { y } = T - { m _ { 1 } } g = { m _ { 1 } } { \partial _ { y } } = { m _ { 1 } } a \left( 3 \right)
$$

Giải hệ phương trình, ta tìm được:

$$
a = \frac { F \left( \cos \theta + \mu _ { k } \ : \sin \theta \right) - \left( m _ { 1 } + \mu _ { k } m _ { 2 } \right) g } { \displaystyle m _ { 1 } + m _ { 2 } }
$$

Hoàn tất: Gia tốc của khối hộp có thể hướng sang phải hoặc trái tùy theo dấu của tử số trong phương trình (4). Nếu vận tốc của khối hộp hướng sang trái thì phải đổi dấu của $f _ { k }$ trong (1). Trong trường hợp đó, chỉ cần đổi hai dấu cộng $( + )$ trong tử số của (4)



thành dấu trừ (–).ss



# Public_130 

# Chuyển động tròn không đều

Ở chương 4, chúng ta đã khảo sát chuyển động trên một đoạn đường tròn với tốc độ thay đổi thì ngoài gia tốc hướng tâm sẽ có thêm thành phần gia tốc tiếp tuyến. Điều đó, có nghĩa là lực tác dụng lên chất điểm cũng có thể phân tích ra thành phần hướng tâm và thành phần tiếp tuyến.

Bởi vì, gia tốc tổng cộng có dạng: $\stackrel {  } { \sf a } = \overline { a } _ { r } + \overline { a } _ { t }$ nên tổng hợp lực tác dụng lên chất điểm được biểu diễn là: $\sum \overrightarrow { F } = \sum \overrightarrow { F _ { r } } + \sum \overrightarrow { F _ { t } }$

![](images/image1.jpg)  
Hình 6.5: chuyển động tròn không đều

Vectơ $\sum \overrightarrow { F _ { r } }$ là lực hướng tâm, có chiều vào tâm của quỹ đạo tròn là lực gây ra gia tốc hướng tâm, còn vectơ $\sum _ { \vec { F _ { r } } }$ tiếp tuyến với đường tròn, là lực gây ra gia tốc tiếp tuyến làm thay đổi tốc độ của chất điểm theo thời gian.

Câu hỏi 6.1: Một hạt gỗ đục lỗ trượt dọc theo sợi dây có dạng như hình 6.6: a) Hãy vẽ các vectơ lực tác dụng lên hạt $\mathbf { g } \tilde { \hat { 0 } }$ tại các vị trí A, B và C . b) Giả sử rằng hạt $\mathbf { g } \tilde { \hat { 0 } }$ được tăng tốc với gia tốc tiếp tuyến không đổi khi chuyển động hướng sang phải. Hãy vẽ các vectơ lực tác dụng lên hạt $\mathbf { g } \tilde { \tilde { 0 } }$ tại các điểm A, B và C.

![](images/image2.jpg)  
Hình 6.6: một hạt gỗ chuyển động dọc theo sợi dây



# Bài tập mẫu 6.5: Chuyển động tròn không đều theo phương thẳng đứng

Một quả cầu nhỏ khối lượng m được gắn vào đầu một sợi dây có chiều dài R và đang quay theo phương thẳng đứng quanh điểm O cố định như hình vẽ. Hãy xác định gia tốc tiếp tuyến của quả cầu và lực căng dây khi vận tốc của quả cầu là v và sợi dây tạo một với phương thẳng đứng một góc θ.

# Giải:

Khái niệm: So sánh chuyển động của quả cầu ở hình 6.7 và những đứa trẻ ở hình 6.4 thì thấy rằng cả hai đều chuyển động theo quỹ đạo tròn, nhưng điều khác ở đây là quả cầu chuyển động không đều, do đó, ở tại hầu hết các điểm trên quỹ đạo chuyển động của quả cầu, thành phần gia tốc tiếp tuyến được đóng góp bởi lực hấp dẫn.

Phân loại: Bài toán này sẽ sử dụng mô hình chất điểm chuyển động dưới tổng hợp lực, và chịu tác dụng của lực hấp dẫn trong toàn bộ quá trình chuyển động.

Phân tích: Từ hình 6.7, các lực tác dụng lên quả cầu chỉ có 2 lực: lực hấp dẫn của Trái Đất tác dụng lên quả cầu $\overrightarrow { F _ { g } } = m . \overrightarrow { g }$ và $\overrightarrow { T }$ lực căng dây. F Trọng lực sẽ được phân tích thành 2 thành

![](images/image3.jpg)

Hình 6.7: Một quả cầu được gắn vào một sợi dây và quay theo phương

thẳng đứng.

phần, theo phương tiếp tuyến là mgsinθ và theo phương hướng tấm là mgcosθ.

Áp dụng định luật 2 Newton theo phương tiếp tuyến:

$$
\sum F _ { _ t } = m g \sin \theta _ { } = m a _ { { \scriptscriptstyle t } } \to a _ { { \scriptscriptstyle t } } ^ { } = g \sin \theta
$$

Áp dụng định luật 2 Newton theo phương hướng tâm:

$$
\sum F _ { r } = T - m g \mathrm { c o s } \Theta = m \bar { \pmb { a } } _ { r } = \frac { \phantom { 0 } } { R }
$$

Do đó, đối với chuyển động tròn không đều. Lực căng dây được tính theo công thức:

$$
\left( { \pmb v } ^ { 2 } \right) = m g \bigg ( \frac { \imath } { R g } + \mathrm { c o s } \theta \bigg )
$$



Xét điểm trên cùng và dưới cùng của đường tròn. Ta thấy:

Lực căng tại điểm dưới cùng là lớn nhất:

$$
T = m g \big ( \frac { V _ { b o t } ^ { 2 } } { R g } + 1 \big )
$$

Còn lực căng tại điểm trên cùng là nhỏ nhất

$$
T = m g _ { \left\lfloor \right\} \frac { V _ { t o p } ^ { 2 } } { R g } - 1 rfloor
$$

Nếu lực căng tại điểm trên cùng $T _ { \mathrm { t o p } } = 0$ , thì

$$
V _ { \mathsf { t o p } } = \sqrt { g R }
$$

# Chuyển động trong hệ quy chiếu phi quán tính

Lực quán tính là kết quả khi chúng ta xét chuyển động trong một hệ quy chiếu không (phi) quán tính.

Lực quán tính xuất hiện và tác dụng lên vật giống như một lực thực, tuy nhiên chúng ta không thể phát hiện vật thứ hai nào gây ra lực quán tính đó. Nên nhớ rằng lực thực luôn gây ra bởi tương tác giữa hai vật nào đó.

Lực quán tính dễ thấy nhất khi các vật chuyển động thẳng có gia tốc.

### Lực ly tâm

Đối với hệ quy chiếu gắn với hành khách (trên hình 6.8b), một lực xuất hiện đẩy cô ta nghiêng khỏi ghế về phía bên phải.

Đối với hệ quy chiếu gắn với Trái Đất, chiếc xe hơi tác dụng một lực về bên trái vào hành khách (hình 6.8c).

Lực đẩy hành khách ra ngoài được gọi là lực ly tâm. Nó là lực quán tính do xuất hiện gia tốc hướng tâm khi xe chuyển hướng.

Còn trên thực tế, lực ma sát chính là lực giữ cho hành khách chuyển động cùng với chiếc xe. Do đó, nếu lực ma sát không đủ lớn, hành khách sẽ tiếp tục chuyển động thẳng theo phương ban đầu theo định luật 1 Newton.

### Lực Coriolis

Đây là lực xuất hiện bởi sự thay đổi bán kính quỹ đạo của một vật trong một hệ quy chiếu đang quay.

Trong hình vẽ 6.9, kết quả của chuyển động quay của vòng xoay là đường cong của quả bóng ném.

Đối với người bắt bóng, một lực theo phương ngang tác dụng vào làm quả bóng chuyển động cong.

![](images/image4.jpg)

![](images/image5.jpg)

![](images/image6.jpg)

Hình 6.8: a. Khi chiếc xe đi vào đoạn đường rẽ sang trái thì hành khách bị nghiêng sang phải, lực tác dụng: b. đối với hành khách. c. đối với Trái Đất



![](images/image7.jpg)

Hình 6.9: Khi 2 người bạn đứng trên một vòng xoay lớn, bạn cố gắng ném bóng thẳng về phía bạn mình. a. đối với người quan sát đứng dưới mặt đất. b. đối với người quan sát đứng cùng trên vòng quay.

# Ví dụ về lực quán tính:

Mặc dù lực quán tính không phải lực thực, nhưng nó lại gây ra những tác động thực. Ví dụ:

• Những vật trên xe hơi thường bị trượt đi.   
• Bạn cảm giác như bị đẩy ra ngoài khi ngồi trên một bề mặt đang quay.   
• Lực Coriolis chịu trách nhiệm cho chuyển động quay trong hệ thống thời tiết, bao gồm cả bão, và các dòng hải lưu.

Câu hỏi 6.2: Một hành khách ngồi trên xe đang rẽ trái như hình 6.8. Chọn phát biểu đúng về lực theo phương nằm ngang nếu hành khách ấy đặt tay lên cửa sổ: a) Hành khách ấy ở trạng thái cân bằng bởi lực thực tác dụng sang bên phải và lực thực tác dụng sang bên trái. b) Hành khách chịu tác dụng của lực chỉ tác dụng sang bên phải. c) Hành khách chỉ bị lực thực tác dụng sang bên trái. d) Không có phát biểu nào ở trên đúng.

### Lực quán tính trong chuyển động thẳng

Đối với quan sát viên $\acute { \mathbf { O } }$ ngoài xe (hình a), gia tốc của quả cầu do thành phần nằm ngang của lực căng dây gây ra. Còn vật $\acute { \mathbf { O } }$ trạng thái cân bằng theo phương thẳng đứng

$$
\begin{array} { l } { { \sum F _ { x } = T \sin \theta = m a } } \\ { { \sum F _ { y } = T \cos \theta - m g = 0 } } \end{array}
$$



Đối với quan sát viên trên xe (hình b), tổng hợp lực tác dụng lên quả cầu bằng 0 và vật ở trạng thái cân bằng theo cả hai phương



![](images/image8.jpg)

Hình 6.10: Một quả cầu nhỏ được treo trên một sợi dây cột trên trần một toa tàu. Các lực tác dụng lên quả cầu đối với: ass. hệ quy chiếu quán tính. b. hệ quy chiếu phi quán tính

$$
\begin{array} { r l } & { \sum F _ { \mathrm { ~ } x } ^ { \prime } = T \sin \theta - F _ { { \mathrm { ~ } \mathrm { f i c t i t i o u s } } } = m a } \\ & { \sum F _ { \mathrm { ~ } y } ^ { \prime } = T \cos \theta - m g = 0 } \end{array}
$$

Và hai phương trình $\dot { \mathbf { O } }$ hai hệ quy chiếu sẽ thỏa mãn khi:

$$
F _ { f i c t i i t o u s } = m a
$$

# Chuyển động với lực cản

Chuyển động của một vật có thể trong một môi trường nào đó như chất lỏng, hoặc chất khí. Và môi trường sẽ tác dụng lên vật một lực cản $\vec { R }$ khi vật chuyển động trong nó.

Độ lớn của lực cản $\overrightarrow { R }$ phụ thuộc vào nhiều yếu tố như: bản chất môi trường, tốc độ của vật, hình dạng và kích thước của vật.

Hướng của lực cản luôn ngược với hướng chuyển động của vật so với môi trường.

$\vec { R }$ gần như luôn tăng cùng với sự tăng của tốc độ. Độ lớn của lực cản $\vec { R }$ phụ thuộc rất phức tạp vào tốc độ. Chúng ta chỉ khảo sát hai trường hợp:

• $\vec { R }$ tỉ lệ với tốc độ (v): đối với các trường hợp vật chuyển động với tốc độ nhỏ và các vật có kích thước nhỏ (ví dụ như các hạt bụi chuyển động trong không khí). $\vec { R }$ tỉ lệ với bình phương tốc độ $( \nu ^ { 2 } )$ : trong trường hợp vật có kích thước lớn (ví dụ như người nhảy dù).



### Lực cản tỉ lệ với tốc độ

Lực cản có thể cho bởi công thức:

$$
\stackrel { \longrightarrow } { R } = - b \stackrel {  } { \nu }
$$

Với $b$ phụ thuộc vào tính chất của môi trường và hình dáng, kích thước của vật. $v ^ {  }$ là vận tốc của vật đối với môi trường. Dấu trừ trong công thức th $\acute { \hat { \mathbf { e } } }$ hiện lực cản ngược hướng với chiều chuyển động.

![](images/image9.jpg)

# Bài tập mẫu 6.6:

Xét một quả cầu nhỏ có khối lượng m đang rơi trong chất lỏng từ trạng thái nghỉ.

Những lực tác dụng lên vật:

• Lực cản • Lực hấp dẫn

Kết quả của chuyển động là:

$$
\begin{array} { l } { m g - b v = m a = m \displaystyle \frac { d v } { d t } } \\ { a = \displaystyle \frac { d v } { d t } = g - b \sum v } \end{array}
$$

![](images/image10.jpg)

Lực cản tỉ lệ với tốc độ:

• Tại thời điểm ban đầu, $\nu = 0$ và $d \nu / d t = g$ Theo thời gian, lực cản $R$ tăng, còn gia tốc giảm dần.

Gia tốc của vật bằng $0 { \mathrm { k h i } } R = m g$

Lúc này, tốc độ v đạt đến tốc độ tốc giới hạn và không thay đổi nữa.

Vận tốc giới hạn

Để tìm vận tốc giới hạn, ta có $a = 0$

Giải phương trình vi phân, ta được:

![](images/image11.jpg)  
Hình 6.11: Chuyển động của một vật rơi trong chất lỏng $\overline { { a . , b } }$ . và đồ thị tốc độ phụ thuộc thời gian của vật đó c.

$$
V = \frac { m g } { b } \left( 1 - \Theta ^ { - b t / } \right) = V _ { T } \left( 1 - \Theta ^ { - t / \tau } \right)
$$



Với τ là hằng số thời gian, có độ lớn: $\tau = ^ { \underline { { m } } }$ b



### Lực cản tỉ lệ thuận với bình phương tốc độ

Những vật chuyển động với tốc độ lớn trong không khí, lực cản của không khí sẽ tỉ lệ với bình phương vận tốc:

$$
R = \% D \rho A \nu ^ { 2 }
$$

Với $D$ là một đại lượng không thứ nguyên được gọi là hệ số cản, $\rho$ là mật độ của không khí, $A$ là diện tích tiết diện vuông góc với vận tốc của vật, $\nu$ là tốc độ của vật.

Khảo sát một vật rơi trong không khí khi tính đến lực cản của không khí:

$$
{ \begin{array} { l } { { \mathrm { u } } { \mathrm { ~ a } } { \mathrm { ~ n } } { \mathrm { ~ u } } { \mathrm { ~ u } } { \mathrm { ~ n } } { \mathrm { ~ ; ~ } } } \\ { { \sum } F = m g - { \frac { 1 } { 2 } } D { \mathrm { } } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } V ^ { \mathrm { } } = m a { \mathrm { } } \ { \mathrm { } } a = g - { \Bigl ( } { \frac { D \mathrm { } \rho A } { 2 m } } { \Bigr ) } v ^ { \mathrm { } } } \\ { \qquad \quad \ } \end{array} }
$$

Vận tốc giới hạn sẽ đạt được khi gia tốc tiến tới 0. Giải các phương trình trên ta sẽ được: $v _ { T } = { \sqrt { \frac { 2 m g } { D \rho A } } }$

![](images/image12.jpg)  
Hình 6.12: Chuyển động của một vật rơi trong chất lỏng.

Bảng 6.1: Một vài tốc độ giới hạn   



# Public_131 

Nhiều bài toán có thể giải được nhờ các định luật Newton và các nguyên lý liên quan. Tuy nhiên, về mặt lý thuyết có nhiều bài toán có thể giải được bằng các định luật Newton nhưng thực tế thì rất phức tạp. Các bài toán đó lại có thể giải một cách dễ dàng bằng một cách khác.

Khái niệm về năng lượng là một trong những chủ đề quan trọng nhất trong khoa học và kỹ thuật. Mỗi quá trình vật lý xảy ra trong vũ trụ đều liên quan đến việc chuyển hóa từ dạng năng lượng này sang dạng năng lượng khác. Trên cơ sở khái niệm năng lượng, người ta đã phát triển những phương pháp mới cho phép giải các bài toán vật lý một cách dễ dàng mà khi giải bằng các định luật Newton thì lại rất khó khăn. Chương này sẽ giới thiệu khái niệm hệ và các cách lưu trữ năng lượng trong một hệ.

# Hệ và môi trường

Một hệ là một phần nhỏ của cả vũ trụ. Một hệ có thể là một vật hoặc một chất điểm, một tập hợp nhiều vật hoặc nhiều chất điểm, hay một vùng không gian nào đó. Một hệ sẽ có ranh giới với bên ngoài. Bên ngoài biên giới của hệ là môi trường. Biên giới của một hệ có thể là một bề mặt thực hoặc một bề mặt tưởng tượng, không nhất thiết trùng với một bề mặt thực. Biên giới chia vũ trụ thành hệ và môi trường. Kích thước và hình dạng của một hệ có thể thay đổi theo thời gian.

Ví dụ một hệ: Khi có một lực tác dụng vào một vật trong không gian trống rỗng thì hệ là vật đó, bề mặt của vật là ranh giới của hệ.

Những điều cần chú ý khi giải toán:

• Xác định hệ   
• Cũng xác định một ranh giới hệ   
• Lực ảnh hưởng lên hệ từ môi trường tác động xuyên qua ranh giới của hệ.

# Công thực hiện bởi một lực không đổi

Công (ký hiệu là W) thực hiện bởi một tác nhân tác dụng một ngoại lực không đổi lên hệ là một đại lượng được xác định bằng tích của độ lớn lực F với độ dịch chuyển $\Delta r$ của điểm đặt lực nhân với cosθ, với $\theta$ là góc tạo bởi vectơ lực và vectơ độ dich chuyển.

$$
W { = } F \Delta r \cos \theta
$$



Chú ý rằng độ dịch chuyển ở đây là độ dịch chuyển của điểm mà lực tác dụng vào.

Lực sẽ không thực hiện công trên một vật chuyển động nếu điểm đặt lực không chuyển động cùng với phương dịch chuyển. Công thực hiện bởi một lực làm cho vật dịch chuyển có độ lớn bằng 0 khi lực vuông góc với phương dịch chuyển.

# Độ dịch chuyển trong công thức tính công

Nếu lực tác dụng vào một vật rắn được xem như một chất điểm thì độ dịch chuyển giống như độ dịch chuyển của chất điểm. Đối với vật biến dạng thì độ dịch chuyển

của vật không giống với độ dịch chuyển mà lực tác dụng vào. Do đó, để xác định độ dịch chuyển chúng ta chỉ xét đến điểm mà lực tác dụng vào.

Phản lực pháp tuyến và lực hấp dẫn không sinh ra công trên vật vì cos $\theta = \cos 9 0 ^ { \circ } = 0 .$ . Chỉ có lực F thực hiện công trên vật.

Dấu của công phụ thuộc vào hướng của lực và hướng của độ dịch chuyển. Công dương khi lực và độ dịch chuyển có cùng hướng, công âm khi chúng ngược hướng.

Công là một đại lượng vô hướng. Đơn vị của công là joule (J).

• 1 joule $= 1$ newton. 1 meter $=$ kg.m²/s² • $\mathrm { J } { = } \mathrm { N } . \mathrm { m }$

# Công là một dạng năng lượng trao đổi

Nếu công thực hiện trên một hệ nhận giá trị dương thì năng lượng được truyền vào hệ; còn nếu công thực hiện trên một hệ nhận giá trị âm thì năng lượng thoát ra khỏi hệ. Nếu một hệ tương tác với môi trường ngoài thì sự tương tác đó có thể xem như sự trao đổi năng lượng truyền qua biên giới của hệ. Điều này dẫn đến một sự thay đổi của năng lượng dự trữ trong hệ.

![](images/image1.jpg)

Hình 7.1 Một vật dịch chuyển dưới tác dụng của một lực không đổi.

F is the only force that does work on the block in this situation.

![](images/image2.jpg)

Hình 7.2 Phản lực pháp tuyến và trọng lực không sinh công, chỉ có lực $F ^ {  }$ âm? (d) không thể xác định được?



Hình 7.3 Hình cho câu hỏi 7.2.

![](images/image3.jpg)  
sinh công.



Câu hỏi 7.2: Trên hình 7.3, các lực có độ lớn bằng nhau, quãng đường dịch chuyển của vật sang phải bằng nhau. Hãy sắp xếp theo thứ tự giá trị của công do lực thực hiện trên vật từ dương nhất đến âm nhất.

# Tích vô hướng 2 vectơ

Tích vô hướng của hai vectơ $\vec { \pmb { \mathsf { A } } }$ và B , được kí hiệu là A B và có giá trị bằng:

$$
\vec { \bf A } \cdot \vec { \bf B } \equiv A B c o s \theta
$$

Với $\theta$ là góc giữa hai vectơ $\vec { \pmb { \mathsf { A } } }$ và B

Tích vô hướng có tính chất giao hoán:

$$
\vec { \pmb { \Delta } } \cdot \vec { \pmb { \mathrm { B } } } = \vec { \pmb { \mathrm { B } } } \cdot \vec { \pmb { \Delta } }
$$

và tính chất kết hợp:

$$
\vec { \mathbf { A } } \cdot \left( \vec { \mathbf { B } } + \vec { \mathbf { C } } \right) = \vec { \mathbf { A } } \cdot \vec { \mathbf { B } } + \vec { \mathbf { A } } \cdot \vec { \mathbf { C } }
$$

Áp dụng vào công thức tính công, ta được:

$$
W = F \Delta r \cos \theta = \vec { \mathsf { F } } \cdot \Delta \vec { \mathsf { r } }
$$

![](images/image4.jpg)  
Hình 7.4 Tích vô hướng 2 vectơ.

# Công được thực hiện bởi lực có độ lớn thay đổi

Để sử dụng công thức $\mathrm { W } = \mathrm { F } \Delta \mathrm { r c o s } \ \theta$ lực phải không đổi, do đó công thức này không thể sử dụng cho việc tính công của một lực biến thiên. Giả sử rằng trong khoảng dịch chuyển rất nhỏ $\Delta \mathbf { x }$ , $\mathrm { F _ { x } }$ là hằng số thì trong khoảng đó $\mathrm { W } = \mathrm { F } _ { \mathrm { x } } \Delta \mathbf { x }$ . Vì vậy, trên cả quãng đường dịch chuyển từ vị trí đầu $\mathbf { X } \mathbf { i }$ đến vị trí cuối $\mathbf { X } \mathbf { f }$ thì:

$$
W \approx \sum _ { x _ { i } } ^ { x _ { t } } F _ { x } \Delta x
$$

![](images/image5.jpg)

![](images/image6.jpg)



# Thế năng của một hệ

Bây giờ chúng ta hãy xem xét một hệ gồm nhiều hơn một vật mà các vật bên trong hệ tương tác lực với nhau. Ví dụ, một hệ gồm cuốn sách và Trái đất, hai vật này tương tác với nhau bằng lực hấp dẫn. Ta sẽ thực hiện một công trên cuốn sách bằng cách nâng quyển sách thật chậm theo phương thẳng đứng, cuốn sách đã có một dời chuyển

$$
\Delta \vec { \bf r } = \left( y _ { \it f } - y _ { i } \right) \hat { \bf l }
$$

Công thực hiện trên hệ phải xuất hiện như là sự tăng năng lượng của hệ. Vì trước và sau khi thực hiện công, quyển sách đều $\acute { \mathbf { O } }$ trạng thái nghỉ nên động năng của hệ không có sự thay đổi. Như vậy, năng lượng cung cấp cho hệ từ bên ngoài phải tồn trữ ở một dạng khác động năng của hệ. Khi cuốn sách được thả rơi hệ có động năng; như vậy, trước khi cuốn sách được thả rơi hệ phải có một khả năng (potential) để thu được động năng. Ta gọi cơ chế tích trữ năng lượng trước khi cuốn sách được thả rơi là thế năng (potential energy).

![](images/image7.jpg)  
Hình 7.10 Tác nhân bên ngoài nâng từ từ cuốn sách $\acute { o }$ độ cao $h _ { i }$ lên độ cao hf.

Thế năng là dạng năng lượng được xác định bởi cấu hình của một hệ mà trong đó các thành phần của hệ tương tác với nhau bằng các lực. Các lực này là nội lực của hệ, chỉ liên quan đến tương tác giữa các thành phần của hệ với nhau. Thế năng luôn gắn liền với một hệ của 2 hay nhiều vật tương tác lẫn nhau.



### Thế năng hấp dẫn

Xét hệ gồm Trái Đất và cuốn sách như hình vẽ. Cuốn sách có khối lượng m đang nằm tại độ cao yi so với bề mặt Trái đất. Một tác nhân bên ngoài hệ nâng cuốn sách lến độ cao yf một cách chậm chạp để dịch chuyển không có gia tốc và do đó lực nâng có độ lớn bằng lực hấp dẫn mà Trái đất tác dụng lên cuốn sách. Công mà lực ngoài thực hiện trên hệ Cuốn sách - Trái đất là:

$$
\begin{array} { r l } & { W _ { e x t } = \left( \vec { \mathsf { F } } _ { \mathrm { a p p } } \right) \cdot \Delta \vec { \mathsf { r } } } \\ & { W _ { e x t } = ( m g \mathsf { \hat { J } } ) \cdot \left[ \left( y _ { t } - y _ { i } \right) \mathsf { \hat { J } } \right] } \\ & { W _ { e x t } = m g y _ { t } - m g y _ { i } } \end{array}
$$

Phương trình trên cho thấy công của ngoại lực thực hiện trên hệ bằng hiệu số giữa hai giá trị cuối và đầu của một đại lượng. Công này đã truyền cho hệ một năng lượng và năng lượng đó tích trữ ở một dạng được gọi là thế năng. Đại lượng mgy được gọi là thế năng hấp dẫn $U _ { g }$ của hệ vật khối lượng m và Trái đất.

$$
U _ { g } = m g y
$$

Thế năng là một đại lượng vô hướng. Đơn vị của thế năng là joules (J).

Công có thể làm thay đổi thế năng hấp dẫn của hệ

$$
{ \cal W } _ { \mathrm { e x t } } = \varDelta U _ { g }
$$

Thế năng hấp dẫn là năng lượng liên kết với một vật, phụ thuộc vào độ cao của vật đó trên bề mặt của Trái Đất. Thế năng hấp dẫn chỉ phụ thuộc vào độ cao của vật so với bề mặt Trái Đất. Khi giải các bài toán, chúng ta cần phải chọn một mốc quy chiếu sao cho thế năng hấp dẫn tại đó bằng một giá trị tham chiếu nào đó, thường là bằng 0. Việc chọn lựa mốc thế năng là tùy ý. Thông thường một vật nằm trên bề mặt của Trái Đất được xem như có thế năng hấp dẫn bằng 0. Hoặc các bài toán sẽ đề xuất một mốc thế năng để sử dụng.

Câu hỏi 7.4: Hãy chọn câu trả lời đúng: Thế năng hấp dẫn của một hệ (a) luôn luôn dương.   
(b) luôn luôn âm. (c) có thể âm hoặc dương.

### Thế năng đàn hồi

Thế năng đàn hồi là một loại năng lượng mà một hệ có lò xo sẽ tích trữ. Khi đó lực tương tác giữa các thành phần bên trong hệ là lực đàn hồi của lò xo.

Xét hệ gồm có một vật và một lò xo như trên hình vẽ. Lực đàn hồi lò xo tác dụng lên cái hộp là

$$
F _ { s } = - \mathit { k x }
$$

Công thực hiện bởi ngoại lực Fapp tác dụng lên hệ lò xo - hộp là:

$$
\mathrm { W } _ { \mathrm { e x t } } = \% k x _ { f } ^ { 2 } - \% k x _ { i } ^ { 2 }
$$



Trong $\mathtt { d } \mathtt { d } \mathtt { d } \mathtt { X } \mathtt { i }$ và xf là vị trí đầu và cuối của vật tính từ vị trí cân bằng $\mathbf { \boldsymbol { x } } = 0$ . Công này bằng với độ chênh lệch giữa giá trị đầu và giá trị cuối của một đại lượng gắn với cấu hình của hệ. Do đó thế năng đàn hồi của hệ vật - lò xo có thể được xác định bởi hệ thức:



$$
U _ { s } = \% k x ^ { 2 }
$$

Lúc đó ta cũng có phương trình:

$$
{ \cal W } _ { \mathrm { e x t } } = \varDelta U _ { s }
$$

Thế năng đàn hồi có thể hiểu là năng lượng dự trữ trong một lò xo bị biến dạng. Năng lượng dự trữ này có thể chuyển hóa thành động năng. Quan sát sự biến dạng của lò xo, có thể nhận thấy: Thế năng đàn hồi dự trữ trong lò xo bằng 0 khi lò xo không biến dạng $\mathrm { { { U } _ { s } } = 0 }$ khi x $= 0$ ); năng lượng được dự trữ trong lò xo chỉ khi lò xo bị giãn hay nén; thế năng đàn hồi lớn nhất khi lò xo đạt đến độ nén hoặc độ giãn lớn nhất; thế năng đàn hồi luôn luôn dương bởi vì $\mathbf { X } ^ { 2 }$ luôn dương.

![](images/image8.jpg)  
Hình 7.11 Sự biến đổi năng lượng giữa thế năng đàn hồi và động năng của hệ.

Trên hình 7.11 là một biểu diễn đồ thị quan trọng về năng lượng của một hệ, được gọi là biểu đồ thanh năng lượng. Biểu đồ thanh năng lượng là một đồ thị quan trọng để biểu diễn thông tin về năng lượng của hệ. Trên biểu đồ thanh năng lượng, trục tung biểu diễn giá trị năng lượng, trục hoành cho thấy các loại năng lượng có trong hệ.



Trong hình 7.11a, không có năng lượng nào cả, bởi vì lò xo đang thả lỏng còn hộp thì không chuyển động.

Trong hình 7.11b và c, tác nhân bên ngoài thực hiện công trên hệ. Do lò xo bị nén lại nên có thế năng đàn hồi trong hệ. Không có động năng trong hệ vì hộp vẫn đang được giữ

Trong hình 7.11d, hộp được thả ra cho chuyển động về phía bên phải trong khi vẫn tương tác với lò xo. Do đó, thế năng đàn hồi của hệ giảm trong khi động năng của hệ tăng.

Trong hình 7.11e, lò xo trở về chiều dài ban đầu và hệ chỉ còn động năng do sự chuyển động của cái hộp.

![](images/image9.jpg)

Câu hỏi 7.5: Một trái banh gắn với một lò xo nhẹ được treo thẳng đứng như hình 7.12. Khi kéo trái banh xuống dưới khỏi vị trí cân bằng rồi thả ra thì trái banh sẽ dao động lên xuống.

![](images/image10.jpg)

![](images/image11.jpg)  
Hình 7.12 Câu hỏi 7.5.

(i) Nếu hệ gồm trái banh, lò xo và Trái đất thì có những dạng năng lượng nào trong quá trình chuyển động đó: (a)

động năng và thế năng đàn hồi (b) động năng và thế năng hấp dẫn (c) động năng, thế năng đàn hồi và thế năng hấp dẫn (d) thế năng đàn hồi và thế năng hấp dẫn.

![](images/image12.jpg)

(ii) Nếu hệ gồm trái banh và lò xo thì có những dạng năng lượng nào trong quá trình chuyển động đó: (a) động năng và thế năng đàn hồi (b) động năng và thế năng hấp dẫn (c) động năng, thế năng đàn hồi và thế năng hấp dẫn (d) thế năng đàn hồi và thế năng hấp dẫn.

# Lực bảo toàn và lực không bảo toàn

![](images/image13.jpg)

Trong phần này ta sẽ tìm hiểu một loại năng lượng có thể tồn trữ trong một hệ. Loại năng lượng đó liên hệ với nhiệt độ của hệ, được gọi là nội năng, $E _ { \mathrm { i n t . } }$ Trong ví dụ trên hình 7.13, giả sử ta dùng tay tác dụng lực gia tốc cuốn sách trượt sang phải trên một bề mặt của một chiếc bàn nặng. Ở đây, bề mặt có ma sát nên sau khi thôi tác dụng lực thì cuốn sách sẽ chuyển động chậm lại rồi dừng hẳn. Xét hệ chỉ là bề mặt mà cuốn sách trượt trên đó. Lực ma sát mà cuốn sách tác dụng lên bề mặt thực hiện công. Khi cuốn sách chuyển động sang bên phải, lực ma sát tác dụng lên bề mặt hướng sang phải và điểm đặt lực cũng dịch chuyển sang phải. Do đó công thực hiện trên bề mặt là dương nhưng bề mặt không dịch chuyển sau khi cuốn sách ngừng trượt. Công thực hiện trên hệ là công dương song cả động năng và thế năng của hệ không thay đổi. Vậy năng lượng đó nằm ở đâu?





Từ kinh nghiệm hằng ngày, có thể nhận biết rằng khi cuốn sách trượt trên bề mặt thì sẽ làm bề mặt nóng lên. Như vậy, công thực hiện trên hệ đã làm nóng hệ lên mà không tăng tốc độ hay thay đổi cấu hình của hệ. Người ta gọi năng lượng liên hệ với nhiệt độ của hệ là nội năng, ký hiệu là $E _ { \mathrm { i n t . } }$ Trong trường hợp này, ma sát đã thực hiện công trên bề mặt, truyền cho hệ một năng lượng dưới dạng nội năng còn động năng và thế năng của hệ vẫn giữ nguyên không thay đổi.

Bây giờ, ta xét hệ gồm có cuốn sách và bề mặt. Ban đầu hệ có động năng vì cuốn sách đang di chuyển. Trong khi cuốn sách trượt trên bề mặt thì nội năng của hệ tăng lên vì cả cuốn sách và bề mặt đều ấm hơn trước đó. Khi cuốn sách dừng lại, động năng của hệ đã chuyển hóa hoàn toàn thành nội năng của hệ. Ở đây, lực ma sát – một lực không bảo toàn, tác dụng giữa các thành phần của hệ đã chuyển hóa động năng của hệ thành nội năng.

### Lực bảo toàn (lực thế)

Công thực hiện bởi một lực tác dụng lên một chất điểm làm chất điểm này chuyển động giữa hai điểm mà không phụ thuộc vào quỹ đạo chuyển động của chất điểm đó thì lực này được gọi là lực bảo toàn (lực thế). Do đó, công thực hiện bởi lực bảo toàn tác dụng lên một chất điểm chuyển động trên một quỹ đạo kín bằng 0. Quỹ đạo kín là quỹ đạo mà điểm đầu trùng với điểm cuối.

Lực hấp dẫn và lực đàn hồi là những ví dụ điển hình của lực bảo toàn.

Thế năng của một hệ gắn liền với một lực bảo toàn nào đó tác dụng giữa các thành phần của hệ đó. Một cách tổng quát, công $\mathrm { W _ { i n t } }$ được thực hiện bởi một lực bảo toàn do một thành phần của hệ tác dụng lên một thành phần khác của hệ khi cấu hình của hệ thay đổi sẽ bằng hiệu thế năng của hệ tại vị trí đầu và vị trí cuối.

$$
{ { W } _ { i n t } } = { { U } _ { i } } - { { U } _ { f } } \mathrm { = - } \Delta U
$$

The work done in moving the book is greater along the brown path than along the blue path.

Khi động năng và nội năng của hệ không thay đổi trong một quá trình thì công dương thực hiện bởi một tác nhân bên ngoài $\mathrm { W _ { e x t } }$ trong trình đó sẽ làm tăng thế năng của hệ. Trong khi đó, công do một thành phần của hệ thực hiện $\mathrm { W _ { i n t } }$ bởi lực bảo toàn bên trong một hệ cô lập là nguyên nhân làm giảm th $\acute { \mathrm { e } }$ năng của hệ.

### Lực không bảo toàn (lực phi thế)

Các lực không thỏa mãn các điều kiện của lực bảo toàn được gọi là lực không bảo toàn. Công thực hiện bởi một lực không bảo toàn phụ thuộc vào quãng đường dịch chuyển.

![](images/image14.jpg)

Lực không bảo toàn tác dụng bên trong hệ sẽ làm biến đổi cơ năng Emech của hệ.



# Public_132 

# Hệ không cô lập

Hệ không cô lập về năng lượng là một hệ có trao đổi năng lượng với môi trường qua biên giới của nó. Một hệ không cô lập sẽ tương tác với môi trường. Một vật bị tác dụng lực là một ví dụ của hệ không cô lập.

Hệ cô lập là một hệ không trao đổi năng lượng với môi trường qua biên giới của hệ.

Đối với một hệ không cô lập, năng lượng được truyền qua biên giới của hệ trong thời gian hệ tương tác với môi trường bên ngoài. Sau đây là những phương thức truyền năng lượng vào hoặc ra khỏi một hệ.

Công (Work) là một hình thức truyền năng lượng bằng cách tác dụng lực lên hệ và điểm đặt của lực bị dịch chuyển (hình 8.1a).

![](images/image1.jpg)  
Hình 8.1 Các cơ chế truyền năng lượng.

Sóng cơ (Mechanical waves) là hình thức truyền năng lượng thông qua sự lan truyền nhiễu loạn trong môi trường. Âm thanh rời khỏi chiếc loa radio ở hình 8.1b hay sóng địa chấn, sóng biển là sự truyền năng lượng bằng sóng cơ.

Nhiệt (Heat) là một cơ chế trao đổi năng lượng giữa hệ và môi trường do có sự khác nhau về nhiệt độ. Năng lượng truyền tới đuôi cái thìa trong hình 8.1c từ phần bị nhúng trong tách cà phê nóng là dưới dạng nhiệt.



Trao đổi chất (Matter transfer) là hình thức truyền năng lượng xuyên qua biên giới của hệ dưới dạng vật chất mang theo năng lượng. Ví dụ đổ xăng cho xe như ở hình 8.1d hay đối lưu là sự truyền năng lượng dưới dạng trao đổi chất.

Truyền điện (Electrical transmission) là sự truyền năng lượng vào hoặc ra khỏi hệ bằng dòng điện. Năng lượng cung cấp cho máy sấy tóc là nhờ sự truyền điện (hình 8.1e).

Sóng điện từ (Electromagnatic radiation) là năng lượng được trao đổi bởi sóng điện từ. Năng lượng truyền khỏi bóng đèn (hình 8.1f) là dưới dạng sóng điện từ.

Định luật bảo toàn năng lượng

# Năng lượng luôn được bảo toàn.

Điều này nghĩa là nếu năng lượng tổng cộng của một hệ thay đổi thì đã có một năng lượng truyền qua biên giới của hệ bằng một phương pháp trao đổi năng lượng nào đó. Dạng tổng quát của định luật bảo toàn năng lượng có thể được biểu diễn bằng phương trình bảo toàn năng lượng như sau:

$$
\begin{array} { l } { \Delta E _ { \mathrm { { s y s t e m } } } = \Sigma T } \\ { \ } \\ { \varDelta E s y s t e m = \sum T } \end{array}
$$

Trong đó, Esystem là tổng năng lượng của hệ, $T$ (Transfer) là năng lượng truyền qua biên giới của hệ.

Phương trình toán học của định luận bảo toàn năng lượng đối với một hệ không cô lập thể hiện đầy đủ các loại năng lượng trao đổi có thể được biểu diễn dưới dạng:

$$
{ \cal A } K + { \cal A } { \cal U } + { \cal A } { \cal E } _ { i n t } = { \cal W } + { \cal Q } + T _ { M W } + T _ { M T } + T _ { E T } + T _ { E R }
$$

Với K là động năng, U là thế năng và $\operatorname { E i n t }$ là nội năng của hệ; năng lượng truyền qua biên giới của hệ dưới dạng công là $T _ { \mathrm { w o r k } } = W _ { \mathrm { : } }$ , dưới dạng nhiệt là $T _ { \mathrm { h e a t } } = Q ,$ , TMW là năng lượng được truyền bởi sóng cơ, TMT là năng lượng trao đổi chất, $\mathrm { T _ { E T } }$ là năng lượng do truyền điện và TER là năng lượng trao đổi bởi sóng điện từ.

Trong thực tế, phương trình của định luật bảo toàn năng lượng sẽ đơn giản hơn nhiều. Ví dụ, nếu có một lực tác dụng lên hệ và sinh công và giả sử chỉ có cơ chế truyền năng lượng này làm thay đổi tốc độ của hệ thì phương trình của định luật bảo toàn năng lượng sẽ rút về phương trình của định lý công-động năng:

$$
\varDelta K = W
$$

Câu hỏi 8.1: Hãy cho biết cơ chế truyền năng lượng nào qua một hệ là: a- Một chiếc tivi, bMột máy cắt cỏ chạy xăng, c- Một cái gọt bút chì bằng tay.

Câu hỏi 8.2: Xét một cái hộp trượt có ma sát trên một bề mặt nằm ngang. i) Nếu hệ là chiếc hộp thì hệ là a- cô lập, b- không cô lập, c- không thể xác định được. ii) Nếu hệ là bề mặt nằm ngang thì hệ là a- cô lập, b- không cô lập, c- không thể xác định



được.

iii) Nếu hệ là cái hộp và bề mặt nằm ngang thì hệ là a- cô lập, b- không cô lập, c- không thể xác định được.

![](images/image2.jpg)

# Hệ cô lập

Đối với một hệ cô lập, không có bất kỳ hình thức trao đổi năng lượng nào với môi trường bên ngoài qua biên giới của hệ, thì tất cả các số hạng bên vế phải trong phương trình (8.2) đều bằng 0 do đó phương trình của định luật bảo toàn năng lượng có dạng:

Trên hình vẽ bên dưới mô tả các dạng năng lượng tồn trữ bên trong một hệ cô lập gồm có động năng, thế năng và nội năng. Các dạng năng lượng này biến đổi lẫn nhau nhưng tổng năng lượng của hệ bảo toàn.

Hình 8.2 Các dạng năng lượng tồn trữ bên trong hệ.

Esystem là tổng động năng, thế năng và nội năng của hệ.

Như vậy, năng lượng của một hệ cô lập không đổi.

# Công suất

Định nghĩa: Công suất tức thời là tốc độ truyền năng lượng theo thời gian và được tính theo công thức:

$$
P \equiv \frac { d E } { d t }
$$

Nếu năng lượng trao đổi dưới dạng công được thực hiện bởi một lực và trong khoảng thời gian t công do lực sinh ra là W thì công suất trung bình $\mathrm { P _ { a v g } }$ được xác định bởi công thức:

$$
P _ { a v g } = \frac { W } { \Delta t }
$$



Công suất tức thời là giới hạn của công suất trung bình khi Δt tiến tới 0.



# Đơn vị

Trong hệ đơn vị SI, đơn vị của công suất là watt (W).

1 watt $= 1$ joule/second = 1 kg.m2/s3

Một đơn vị công suất hay sử dụng nữa tại Mỹ là mã lực (horsepower – hp)

$$
1 \mathrm { h p } = 7 4 6 \mathrm { W }
$$

Một đơn vị của năng lượng thường bị nhầm lẫn với đơn vị công suất là kWh. Nhớ rằng kWh là đơn vị đo năng lượng, được xác định như sau:

$$
1 \ { \mathrm { k W h } } = 1 { \mathrm { k W . l h } } = ( 1 0 0 0 \ { \mathrm { W } } ) ( 3 6 0 0 \ { \mathrm { s } } ) = 3 . 6 \ { \mathrm { x } } 1 0 ^ { 6 } \ { \mathrm { J } }
$$

# Tóm tắt chương 8

Hệ không cô lập về năng lượng là một hệ có trao đổi năng lượng với môi trường qua biên giới của nó.

Hệ cô lập là một hệ không trao đổi năng lượng với môi trường qua biên giới của hệ.

Định luật bảo toàn năng lượng: Năng lượng của một hệ cô lập là không đổi.

Một lực ma sát có độ lớn fk tác dụng trên một quãng đường d thì nội năng của hệ thay đổi một lượng:

$$
\Delta \mathrm { E } _ { \mathrm { i n t } } = \mathrm { f } _ { \mathrm { k } } . \mathrm { d }
$$

Công suất là tốc độ truyền năng lượng theo thòi gian:

$$
P \equiv { \frac { d E } { d t } }
$$

Phương trình của định luật bảo toàn năng lượng đối với hệ không cô lập

$$
\bar { \Delta } \mathrm { E } _ { \mathrm { s y s t e m } } = \Sigma \mathrm { T }
$$

$$
{ \cal A } K + { \cal { A } } { \cal U } + { \cal { A } } { \cal E } _ { i n t } = { \cal W } + { \cal Q } + { \cal T } _ { M W } + { \cal T } _ { M T } + { \cal T } _ { E T } + { \cal T } _ { E R }
$$

Phương trình của định luật bảo toàn năng lượng đối với hệ cô lập

$$
\Delta \mathrm { E } _ { \mathrm { s y s t e m } } = 0
$$

$$
\Delta \mathrm { K } + \Delta \mathrm { U } + \Delta \mathrm { E i n t } = 0
$$

Nếu các lực tác dụng bên trong hệ đều là lực bảo toàn thì ta có định luật bảo toàn cơ năng

$$
\begin{array} { c } { { \Delta \mathrm { E } _ { \mathrm { m e c h } } = 0 } } \\ { { \Delta \mathrm { K } + \Delta \mathrm { U } = 0 } } \end{array}
$$

# Public_133 

Khi giải quyết một bài toán cơ học ta có thể sử dụng nhiều phương pháp khác nhau. Đối với một số bài toán nếu ta dùng phương pháp này thì sẽ phức tạp nhưng nếu ta dùng phương pháp khác thì lại trở nên dễ dàng hơn. Ví dụ trường hợp người đàn ông đứng trên băng bắn cung tên hoặc tình huống các viên bi-da va chạm với nhau.

Giả sử xét một tình huống đơn giản là cho biết vận tốc của mũi tên ngay sau khi được bắn ra và yêu cầu tính vận tốc của người bắn cung ngay khi đó. Ta không thể giải bài toán này với các mô hình động học (chương 2), động lực học (chương 5), hoặc năng lượng (chương 7). Tuy nhiên, ta có thể giải quyết bài toán này một cách dễ dàng dùng cách tiếp cận liên quan đến động lượng.

Chương này sẽ trình bày các khái niệm động lượng, xung lượng, các định lý liên quan đến động lượng, xung lượng, từ đó đưa ra phương pháp giải các bài toán cơ học liên quan đến động lượng, đặc biệt là các bài toán va chạm.

# Động lượng

Xét hệ cô lập $\mathrm { g } \dot { \mathrm { o } } \mathrm { m } 2 $ chất điểm có khối lượng m1, m2, chuyển động với các vận tốc $\vec { v _ { \mathrm { ~ 1 ~ } } }$ và $\vec { v _ { \mathrm { ~ 2 ~ } } }$ (hình 9.1). Vì hệ cô lập nên lực tác dụng lên chất điểm này là do chất điểm kia gây ra. Nếu chất điểm 1 tác dụng lên chất điểm 2 một lực $F _ { 1 2 } ^ {  }$ thì chất điểm 2 cũng tác dụng lên chất điểm 1 một lực $F ^ {  } { } _ { 2 1 }$ bằng về độ lớn nhưng ngược chiều. Các lực này tạo thành một cặp lực-phản lực theo định luật 3 Newton, $\boldsymbol { F } _ { 1 2 } = - \boldsymbol { F } _ { 2 1 }$ , nên ta có: $\boldsymbol { F } ^ {  } { } _ { 1 2 } + \boldsymbol { F } ^ {  } { } _ { 2 1 } = 0$ .

Theo định luật 2 Newton: lực tác dụng lên mỗi chất điểm bằng ????⃗ nên:

![](images/image1.jpg)  
Hình 9.1 Hai chất điểm tương tác với nhau

$$
m _ { 1 } \vec { a ^ { \mathrm { \normalsize ~ 1 } } } + m _ { 2 } \vec { a ^ { \mathrm { \normalsize ~ 2 } } } = 0
$$

Thay các gia tốc bằng biểu thức định nghĩa của nó theo phương trình 4.5, ta có:

$$
m _ { 1 } \frac { d \vec { v _ { 1 } } } { d t } + m _ { 2 } \frac { d \vec { v _ { 2 } } } { d t } = 0
$$

Nếu các khối lượng $\mathbf { m } _ { 1 }$ , $\mathbf { m } _ { 2 }$ không đổi, ta có thể đưa chúng vào trong dấu đạo hàm:

$$
\frac { d ( m _ { 1 } \vec { v _ { \ 1 } } ) } { d t } + \frac { d ( m _ { 2 } \vec { v _ { \ 2 } } ) } { d t } = 0
$$

$$
\frac { d \big ( m _ { 1 } \vec { \nu } _ { 1 } + m _ { 2 } \vec { \nu } _ { 2 } \big ) } { d t } = 0
$$



Vì đạo hàm của tổng $m _ { 1 } \vec { v _ { \ 1 } } + m _ { 2 } \vec { v _ { \ 2 } }$ theo thời gian bằng không, nên tổng này là không đổi. Đại lượng mv được gọi là động lượng của một chất điểm, và đối với hệ các chất điểm cô lập, tổng các đại lượng này được bảo toàn.

# Định nghĩa động lượng của chất điểm:

Động lượng của một chất điểm có khối lượng m chuyển động với vận tốc ??⃗ được xác định bằng tích của khối lượng và vận tốc của nó:

$$
{ \vec { p } } \equiv m { \vec { \nu } }
$$

Động lượng là một đại lượng vectơ, hướng dọc theo $v ^ {  } .$ , thứ nguyên là ML/T, đơn vị trong hệ SI là kg.m/s.

Nếu chất điểm chuyển động theo hướng bất kỳ thì động lượng $p ^ {  } \thinspace { \mathrm { c o } } \ 3$ thành phần, và phương trình (9.2) viết cho các thành phần là:

$$
p _ { x } = m v _ { x } \qquad p _ { y } = m v _ { y } \qquad p _ { z } = m v _ { z }
$$

Khái niệm động lượng giúp ta phân biệt một cách định lượng giữa các vật nặng và vật nhẹ chuyển động với cùng vận tốc. Ví dụ động lượng của một quả bóng bowling thì lớn hơn nhiều so với động lượng của một quả bóng tennis chuyển động với cùng vận tốc. Newton đã gọi ????⃗ là khối lượng chuyển động; thuật ngữ này có lẽ sinh động hơn thuật ngữ động lượng ta dùng hiện nay.

# Phân biệt động năng và động lượng:

Thứ nhất, động năng là đại lượng vô hướng còn động lượng là đại lượng vectơ. Ví dụ xét hai chất điểm có khối lượng bằng nhau chuyển động về phía nhau theo một đường thẳng với cùng tốc độ. Động năng của hệ này khác không, động lượng của hệ này bằng không.

Thứ hai là động năng có thể chuyển hóa thành các dạng năng lượng khác chẳng hạn như thế năng hoặc nội năng, còn động lượng không chuyển đổi được thành năng lượng. Các khác biệt này đủ để tạo ra các mô hình phân tích dựa vào động lượng, tách biệt với các mô hình dựa vào năng lượng, cung cấp một công cụ độc lập để sử dụng trong việc giải quyết các bài toán.

Theo định luật 2 Newton, ta có:

$$
\Sigma F ^ {  } = m a ^ {  } = m \frac { d v ^ {  } } { d t }
$$

Giả sử khối lượng m là không đổi, ta có thể đưa khối lượng m vào trong dấu đạo hàm, nên:

$$
\sum { \vec { F } } = { \frac { d \left( m { \vec { \nu } } \right) } { d t } } = { \frac { d { \vec { p } } } { d t } }
$$

Phương trình (9.3) là dạng khác của định luật 2 Newton đối với chất điểm. Phương trình này chỉ ra rằng tốc độ biến thiên theo thời gian của động lượng của chất điểm thì bằng hợp lực tác dụng lên chất điểm. Dạng này tổng quát hơn dạng đã giới thiệu ở chương 5, và có thể sử dụng để khảo sát các hiện tượng trong đó khối lượng thay đổi, ngoài các trường hợp trong đó vận tốc thay đổi. Ví dụ trường hợp khối lượng của tên lửa thay đổi do nhiên liệu bị đốt và bị phóng ra khỏi tên lửa, ta không thể sử dụng phương trình $\sum { F } ^ {  } = m \vec { a ^ { \mathrm { ~ } } } ($ để phân tích mà phải dùng cách tiếp cận động lượng như sẽ trình bày trong mục 9.9.





Câu hỏi 9.1: Hai vật có động năng bằng nhau. Độ lớn động lượng của chúng so với nhau thế nào? (a) p1 < p2 (b) ${ \sf p } _ { 1 } = { \sf p } _ { 2 }$ (c) p1 > p2 (d) không đủ thông tin để phát biểu.

Câu hỏi 9.2: Giáo viên thể dục ném một quả bóng chày về phía bạn với một tốc độ nào đó và bạn bắt lấy nó. Tiếp theo giáo viên sẽ ném một quả bóng tập nặng gấp 10 lần quả bóng chày. Bạn có các lựa chọn sau: Bạn có thể bắt được quả bóng tập được ném với (a) cùng tốc độ với quả bóng chày, (b) cùng động lượng với quả bóng chày, hoặc (c) cùng động năng với quả bóng chày. Hãy sắp xếp các lựa chọn này từ dễ đến khó để bắt.

# Mô hình phân tích: Hệ cô lập (động lượng)

Sử dụng định nghĩa động lượng, biểu thức 9.1 có thể viết là:

$$
\frac { d } { d t } ( \vec { p _ { \ 1 } } + \vec { p _ { \ 2 } } ) = 0
$$

Vì đạo hàm của động lượng toàn phần $\vec { p _ { \ t o t } } = \vec { p _ { \ t } } + \vec { p _ { \ t } }$ bằng không, nên động lượng toàn phần của hệ hai chất điểm cô lập trong hình 9.1 là không đổi:

$$
\vec { p } _ { t o t } = c o n s t
$$

Hay:

$$
\Delta \stackrel {  } { p } _ { t o t } = 0
$$

hoặc viết theo dạng khác là:

$$
\vec { p _ { \ 1 i } } + \vec { p _ { \ 2 i } } = \vec { p _ { \ 1 f } } + \vec { p _ { f } }
$$

với $\vec { p _ { \mathrm { ~ 1 } i } } , \vec { p _ { \mathrm { ~ 2 } i } }$ là các giá trị đầu và $\vec { p _ { \begin{array} { l } { 1 } / } , \vec { p _ { \begin{array} { l } { 2 } f } \end{array} } } \end{array}$ là các giá trị cuối của động lượng của hai chất điểm.

Phương trình (9.5) chứng tỏ động lượng toàn phần theo các hướng x, y, z đều được bảo toàn một cách độc lập:

$$
p _ { 1 i x } + p _ { 2 i x } = p _ { 1 \beta x } + p _ { 2 \beta } \quad p _ { 1 i y } + p _ { 2 i y } = p _ { 1 \beta y } + p _ { 2 \beta } \quad p _ { 1 i z } + p _ { 2 i z } = p _ { 1 \beta z } + p _ { 2 \beta }
$$

Phương trình (9.5) là dạng toán học của một mô hình phân tích mới, gọi là mô hình hệ cô lập (động lượng). Mô hình này có thể mở rộng cho hệ cô lập nhiều chất điểm bất kỳ như sẽ trình bày trong mục 9.7.

Từ phương trình (9.5) ta có thể phát biểu như sau: Khi hai hay nhiều chất điểm của một hệ cô lập tương tác với nhau, động lượng toàn phần của hệ luôn không đổi. Như vậy động lượng toàn phần của hệ cô lập tại các thời điểm bất kì đều bằng động lượng ban đầu của nó.





Mô hình phân tích hệ cô lập không cần xét đến ngoại lực tác dụng lên hệ, cũng như lực đó là lực bảo toàn hay không bảo toàn, lực biến thiên hay không biến thiên theo thời gian. Yêu cầu duy nhất là các lực phải là nội lực của hệ. Điều này cho thấy tầm quan trọng của mô hình mới này.

# Mô hình phân tích: Hệ cô lập (động lượng)

Giả sử ta đã xác định được hệ cần phân tích và biên của nó. Nếu không có ngoại lực nào tác dụng lên hệ thì hệ là cô lập. Khi đó động lượng toàn phần của hệ được bảo toàn:

$$
\Delta \stackrel { \longrightarrow } { p } _ { t o t } = 0
$$

Ví dụ:

• Viên bi da cái đánh vào các viên bi da khác trên bàn • Tàu vũ trụ bắn tên lửa ra và chuyển động nhanh hơn trong không gian Các phân tử chất khí ở một nhiệt độ xác định chuyển động và va chạm với nhau

![](images/image2.jpg)

# Bài tập mẫu 9.1:

Một người bắn cung đứng trên mặt băng không ma sát bắn một mũi tên nặng $0 . 0 3 \mathrm { k g }$ theo phương ngang với vận tốc đầu $8 5 \mathrm { m / s }$ . (A) Hỏi vận tốc của người sau khi mũi tên được bắn ra. (B) Điều gì xảy ra nếu mũi tên được bắn theo hướng hợp với phương nằm ngang một góc θ? Điều này sẽ làm thay đổi vận tốc giật lùi của người bắn cung như thế nào?

# Giải:

Phân tích bài toán: Hãy tưởng tượng mũi tên bị bắn đi trên một đường thẳng và người bắn cung thủ chuyển động giật lùi theo hướng ngược lại. Ta không thể giải bài toán này với các mô hình dựa trên chuyển động, lực, hoặc năng lượng. Tuy nhiên, ta có thể giải quyết vấn đề này một cách dễ dàng với cách tiếp cận liên quan đến động lượng. Ta xét hệ gồm có người bắn cung (bao gồm cả cung) và mũi tên. Hệ không cô lập vì có lực hấp dẫn và phản lực pháp tuyến từ băng tác dụng lên hệ. Tuy nhiên, các lực này theo phương thẳng đứng và vuông góc với chiều chuyển động của hệ. Không có ngoại lực tác dụng lên hệ theo phương ngang, và ta có thể áp dụng mô hình hệ cô lập (động lượng) đối với các thành phần động lượng theo hướng này.

![](images/image3.jpg)  
Hình 9.2 Bài tập mẫu 9.1 – Người bắn cung

(A) Áp dụng mô hình hệ cô lập (động lượng) theo phương ngang, động lượng theo phương ngang của hệ trước và sau khi bắn đều bằng 0. Ta chọn hướng bắn mũi tên là hướng dương của trục x. Xem người bắn cung là chất điểm 1 và mũi tên là chất điểm 2, theo phương trình 9.5 ta được:



$$
\Delta \overrightarrow { p } _ { t o t } = 0  \overrightarrow { p } _ { f } - \overrightarrow { p } _ { i } = 0  \overrightarrow { p _ { f } } = \overrightarrow { p _ { i } }  m _ { 1 } \overrightarrow { \nu _ { 1 f } } + m _ { 2 } \overrightarrow { \nu _ { 2 f } } = 0
$$



= 85i Theo đề bài ta có $\mathrm { \Delta \ m _ { 1 } = 6 0 k g }$ , m2 = 0,030 kg và v2 f m/s.

Giải phương trình này và thay số ta được:

$$
\vec { \nu } _ { { 1 f } } = - \frac { m _ { 2 } } { m _ { 1 } } \vec { \nu } _ { { 2 f } } = - 0 , 0 4 2 \vec { i } m / s
$$

Dấu trừ chỉ ra rằng người bắn cung chuyển động về phía bên trái trên hình 9.2 sau khi bắn mũi tên, phù hợp với định luật 3 Newton. Gia tốc và vận tốc của người bắn cung nhỏ hơn nhiều so với gia tốc và vận tốc của mũi tên vì khối lượng của người bắn cung rất lớn so với mũi tên.

(B) Độ lớn của vận tốc giật lùi sẽ giảm vì chỉ một thành phần của vận tốc mũi tên là theo hướng x. Sự bảo toàn động lượng theo hướng x cho ta:

$$
\begin{array} { r } { \begin{array} { l l l } { \displaystyle m \nu } & { \displaystyle + m \nu \quad \mathrm { c o s } \theta = 0 \tilde { \hat { \mathrm { a n } } } \mathrm { t } \tilde { \mathrm { o i } } \nu } & { \displaystyle _ { _ { 1 f } } = - \frac { m _ { _ 2 } } { m _ { _ 1 } } \nu } & { \displaystyle \mathrm { c o s } \theta \ . } \end{array} } \end{array}
$$

Với các giá trị $\theta \neq 0$ thì $\nu _ { 1 f }$ nhỏ hơn $\nu _ { { 1 } f } \mathrm { k h i } \ 6 = 0$ vì $\mathrm { c o s } \theta < 1$ .

# Mô hình phân tích: $\mathbf { H } \hat { \mathbf { e } }$ không cô lập (động lượng)

Đối với các khảo sát động lượng, hệ không cô lập nếu có lực tác dụng lên hệ. Ta có thể hình dung động lượng được chuyển từ môi trường đến hệ thông qua lực. Việc hiểu được lực là nguyên nhân gây ra sự biến thiên động lượng rất quan trọng khi giải quyết một số loại bài toán.

Giả sử có một hợp lực $\sum F ^ {  }$ tác dụng lên chất điểm và hợp lực này có thể biến thiên theo thời gian. Theo định luật 2 Newton:

$$
\Sigma { \cal F } ^ {  } = \frac { d p  } { d t }
$$

$$
\begin{array} { r } { d \boldsymbol { p } ^ {  } = \sum \boldsymbol { F } ^ {  } d t } \end{array}
$$

Ta có thể lấy tích phân biểu thức (9.7) để tìm độ biến thiên động lượng của chất điểm khi có lực tác dụng lên nó trong một khoảng thời gian nào đó. Nếu động lượng của chất điểm thay đổi từ $\vec { p _ { \ i } }$ tại thời điểm $t _ { i }$ tới $\vec { p _ { \ f } }$ tại thời điểm $t _ { f }$ , lấy tích phân phương trình 9.7 ta được:

$$
\begin{array} { r } { \Delta \vec { p ^ { * } } = \vec { p ^ { * } } _ { f } - \vec { p ^ { * } } _ { i } = \int \sum F ^ { \ } } \\ { \vec { d } } \end{array}
$$



Để tính tích phân này, ta cần biết hợp lực tác dụng lên chất điểm biến thiên theo thời gian như thế nào. Đại lượng ở vế phải của phương trình (9.8) được gọi là xung của hợp lực $\sum F ^ {  }$ tác dụng lên chất điểm trong khoảng thời gian $\Delta t = t _ { f } - t _ { i }$ , kí hiệu là $I ^ {  }$ :

$$
\boldsymbol { I } ^ {  } = \int _ { t _ { i } } ^ { t _ { f } } \sum \boldsymbol { F } ^ {  } d t
$$

Giả sử lực biến thiên theo thời gian như trên hình 9.3a và khác không trong khoảng thời gian $\Delta t = t _ { f } - t _ { i }$ . Vectơ xung lực $I ^ {  }$ cùng hướng với vectơ độ biến thiên động lượng $\Delta p ^ {  }$ . Xung lực có thứ nguyên của động lượng là ML/T. Xung lực không phải là một thuộc tính của chất điểm, mà là số đo mức độ ngoại lực làm thay đổi động lượng của chất điểm.

Do hợp lực truyền xung lực cho chất điểm thường thay đổi theo thời gian, nên để thuận tiện, người ta định nghĩa hợp lực trung bình theo thời gian:

Xung luc do luc truyèn cho chát dièm là dièn tich drói duòng cong

![](images/image4.jpg)  
Lyc trung binh theo thòi gian cho ta cùng giá tri xung lrc dói vói chát dièm gióng nhu lrc bién thièn theo thòi gian ō hình a)

![](images/image5.jpg)

Hình 9.3 (a) Lực tác dụng lên chất điểm biến thiên theo thời gian. (b) Giá trị của lực không đổi (đường nét đứt nằm ngang) được lấy sao cho diện tích của hình chữ nhật bằng diện tích dưới đường cong ở

$$
\left( \sum \ F ^ { \prime } \right) _ { a v g } = \frac { 1 } { \Delta t } \int \sum F ^ { \prime } d t
$$

trong đó $\Delta t = t _ { f } - t _ { i }$ . (Phương trình 9.11 là một áp dụng của định lý giá trị trung bình trong giải tích.) Do đó có thể biểu diễn phương trình 9.9 như là:

$$
\vec { I ^ { * } } = ( \sum F _ { \ a v g } ^ {  } \Delta t
$$

Lực trung bình này, như chỉ ra trên hình 9.3b, có thể xem là lực không đổi tác dụng lên chất điểm trong khoảng thời gian $\Delta t$ , có cùng xung lực với xung lực của lực biến thiên theo thời gian tác dụng lên chất điểm trong khoảng thời gian đó.

$$
\begin{array} { r l r } & { \mathrm { 1 \sum \it F ^ { * } l \dot { a } m \hat { o } t h a m \ c i a n \ t h \dot { o } i \ g i a n , c \dot { o } t h \dot { c } t i n h \ d u m \ c u m \ x u m g \ l u c t \ v i a n g \ l u m \ t r i n g \ f r i n h \ g . } }  & \\ & { \mathrm { n \ t r \ddot { o } n \hat { e } n \ r \hat { a } t d o n \ g i a n \ n \hat { e } u n h u \ l u c \ t \dot { a } c d u m g \ l \hat { e } n \ c h \dot { a } t \ d i \hat { \tilde { e } } m \ l \hat { a } \ k h \hat { o } n g \ d \hat { \tilde { o } i } \cdot \mathrm { T r o n g } } } & \\ & { \mathrm { 7 , \beta ( \sum \it F ) _ { \alpha \it F } = \sum \it F \cdot \ t r o n g \ d \hat { o } \sum \it F ^ { * } l \dot { a } \ h o p \ l v c \ k h \hat { o } n g \ d \hat { \tilde { o } i } \ t \ t \hat { a } c d u m g \ l \hat { e } u \ c h \hat { a } t \ } } & \\ & { \mathrm { t r i n h \ ( 9 . 1 1 ) t r \tilde { o } t h a n h \hat { . } } } & \\ & { \mathrm { ~ } } &  \Gamma = \sum \mathrm  \it F ^ { * } \hat { \Delta } t ^  2 5 \cdot \hat { \Sigma } ^  0 . 5 \times \hat { \Sigma } ^  0 . 5 \times \hat { \Sigma } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \hat { \ S } ^  0 . 5 \times \end{array}
$$

Kết hợp các phương trình (9.8) và (9.9) ta được định lý xung lượng-động lượng:

Độ biến thiên động lượng của một chất điểm thì bằng xung lượng của hợp lực tác dụng lên chất điểm đó:

$$
\Delta p ^ {  } = I ^ {  }
$$

Phát biểu này tương đương với định luật 2 Newton. Khi nói một xung lực được truyền cho chất điểm, ta muốn nói rằng động lượng được truyền từ một tác nhân bên ngoài tới chất điểm đó. Phương trình (9.13) có dạng tương tự với các phương trình bảo toàn năng lượng (8.1) và (8.2).

Phương trình 9.13 là phát biểu tổng quát nhất của nguyên lý bảo toàn động lượng và được gọi là phương trình bảo toàn động lượng. Trong cách tiếp cận động lượng, hệ cô lập xuất hiện thường xuyên hơn hệ không cô lập, nên phương trình (9.13) có thể xem như trường hợp đặc biệt của phương trình (9.5). Vế trái của phương trình (9.13) là độ biến thiên động lượng của hệ. Vế phải là số đo động lượng đi qua biên của hệ khi có lực tác dụng lên hệ. Phương trình (9.13) là phát biểu toán học của một mô hình phân tích mới, gọi là mô hình hệ không cô lập (động lượng). Phương trình này có dạng tương tự phương trình (8.1) nhưng có một số khác biệt khi áp dụng cho các bài toán. Trước tiên, phương trình (9.13) là phương trình vectơ, trong khi phương trình (8.1) là phương trình vô hướng. Do đó hướng là quan trọng đối với phương trình (9.13). Thứ hai, chỉ có một loại động lượng nên chỉ có một cách duy nhất để tích trữ động lượng trong hệ. Ngược lại, như thấy từ phương trình (8.2), có 3 cách để tích năng lượng cho hệ là động năng, thế năng và nội năng. Thứ ba, chỉ có một cách để truyền động lượng cho hệ là tác dụng lực lên hệ trong một khoảng thời gian. Phương trình (8.2) chỉ ra 6 cách mà ta đã biết để truyền năng lượng cho một hệ. Do đó, không có sự mở rộng phương trình (9.13) tương tự như phương trình (8.2).

Trong nhiều tình huống người ta dùng “xấp xỉ xung lực”, bằng cách giả sử một trong các lực tác dụng lên chất điểm tác dụng trong một khoảng thời gian ngắn nhưng lớn hơn nhiều so với các lực khác cùng có mặt. Khi đó, hợp lực $\sum F ^ {  }$ trong phương trình (9.9) được thay thế bằng một lực đơn $F ^ {  }$ để tính xung lực tác dụng lên chất điểm. Sự xấp xỉ này rất hữu ích khi xét các bài toán va chạm trong đó khoảng thời gian va chạm rất ngắn. Khi sử dụng xấp xỉ này, lực đơn được xem là một xung lực. Ví dụ khi quả bóng chày bị đánh bằng cái gậy, thời gian va chạm khoảng 0,01s và lực trung bình mà gậy tác dụng lên quả bóng là vài ngàn Newton. Vì lực này lớn hơn nhiều so với trọng lực tác dụng lên quả bóng và cái gậy, nên sự xấp xỉ xung lực cho thấy việc bỏ qua trọng lực là đúng đắn. Khi dùng xấp xỉ này, cần nhớ rằng $\vec { p _ { \ i } }$ và $\vec { p _ { \ f } }$ là các động lượng tức thời trước và sau khi va chạm. Do đó trường hợp phù hợp để dùng xấp xỉ xung là khi va chạm chất điểm di chuyển một đoạn rất ngắn.

Câu hỏi 9.3: Hai vật nằm yên trên một bề mặt không có ma sát. Vật 1 có khối lượng lớn hơn vật 2. (i) Khi một lực không đổi tác dụng lên vật 1, nó gia tốc vật trên quãng đường d theo một đường thẳng. Ngừng cho lực tác dụng lên vật $1 \ \mathrm { m } \dot { \mathrm { a } }$ cho nó tác dụng lên vật 2. Tại thời điểm vật 2 được gia tốc qua cùng quãng đường d, phát biểu nào đúng? (a) $\mathsf { p } _ { \mathsf { , } } < \mathsf { p } _ { 2 }$ , (b) ${ \mathsf { p } } 1 = { \mathsf { p } } 2$ , (c) $\mathsf { p } _ { 1 } > \mathsf { p } _ { 2 } , ( \mathsf { d } ) \mathsf { K } _ { 1 } < \mathsf { K } _ { 2 }$ , (e) $\mathrm { K } _ { 1 } = \mathrm { K } _ { 2 }$ , (f) $\mathrm { K } _ { 1 } > \mathrm { K } _ { 2 }$ . (ii) Khi một lực không đổi tác dụng lên vật 1, nó gia tốc vật trong một khoảng thời gian $\Delta$ t. Ngừng cho lực tác dụng lên vật $1 \ \mathrm { m } \dot { \mathrm { a } }$ cho nó tác dụng lên vật 2. Từ danh sách các lựa chọn như trên, phát biểu nào là đúng sau khi vật 2 được gia tốc trong cùng khoảng thời gian $\Delta { \sf t ? }$

Câu hỏi 9.4: Hãy xếp hạng từ lớn nhất đến nhỏ nhất một bảng điều khiển ô tô, một dây an toàn và một túi khí, mỗi cái được sử dụng một mình trong các va chạm có cùng tốc độ, về (a) xung lực và (b) lực trung bình mà mỗi cái mang lại cho một hành khách ngồi phía trước.

# Mô hình phân tích: Hệ không cô lập (động lượng)

Giả sử ta đã xác định được hệ cần phân tích và biên của nó. Nếu có ngoại lực tác dụng lên hệ thì hệ là không cô lập. Khi đó độ biến thiên động lượng toàn phần của hệ bằng xung lực tác dụng lên hệ (định lý xung lực - động lượng): $\Delta \stackrel { \longrightarrow } { p } _ { t o t } = \vec { I }$ (9.13)

Ví dụ:

• Cái gậy đánh vào quả bóng chày • Dùng sợi dây kéo một ống chỉ đặt trên bàn

![](images/image6.jpg)

# Bài tập mẫu 9.3: Cái đỡ va tốt như thế nào?

Trong một thử nghiệm va chạm, một xe hơi có khối lượng $1 5 0 0 \mathrm { k g }$ va chạm với một bức tường như trên hình 9.4. Vận tốc của xe trước và sau khi va chạm lần lượt là ${ \vec { \nu } } _ { i } = - 1 5 { \vec { i } } \mathrm { m } / \mathrm { s }$ và $\vec { \nu } _ { f } = 2 , 6 \vec { i } \mathrm { m } / \mathrm { s }$ . (A) Va chạm kéo dài trong 0.15 s, hãy tìm xung lực c ủa vụ va chạm và lực trung bình tác dụng lên xe. (B) Điều gì xảy ra nếu chiếc xe không bật ra khỏi bức tường? Giả sử tốc độ cuối cùng của xe bằng không và khoảng thời gian của va chạm vẫn ở mức 0.15 s. Điều đó có thể hiện là lực lớn hơn hoặc nhỏ hơn tác dụng lên xe không?

![](images/image7.jpg)  
Hình 9.4 Bài tập mẫu 9.3

Giải:

(A) Sử dụng công thức 9.13 để tính xung lực tác dụng lên xe hơi:

$$
\vec { I } = \Delta \vec { p } = \vec { \mathrm { p _ { f } } } - \vec { \mathrm { p _ { i } } } = m \vec { \nu _ { f } } - m \vec { \nu _ { i } } ^ { - } = m \left( \vec { \nu _ { f } } - \vec { \nu _ { i } } \right) = 2 6 4 0 0 \vec { i } \mathrm { k g . m / s }
$$

Dùng công thức (9.11) để tính lực trung bình tác dụng lên xe: (F )avg = I =176000 it

N

Lực tính được ở trên là tổng hợp của phản lực vuông góc do tường tác dụng lên xe và lực ma sát giữa các lốp xe và mặt đất khi đầu xe bị biến dạng. Nếu các bánh xe quay tự do, lực ma sát này là tương đối nhỏ.

(B) Trong tình huống trên, khi mà chiếc xe bật ra khỏi tường, lực tác dụng lên xe thực hiện hai việc trong khoảng thời gian 0.15s: (1) nó dừng xe, và (2) nó làm cho xe chuyển động ra khỏi tường với tốc độ 2.60 m/s sau khi va chạm. Nếu chiếc xe không bật ra,

lực chỉ thực hiện bước đầu tiên đó là dừng xe - đòi hỏi một lực nhỏ hơn. Trong trường hợp này, xung lực là:

I = p = p f − pi = 0 − mvi = m(vf − vi ) = 22500i kg.m/s và lực trung bình tác dụng lên xe   
là:   
$\left( \sum \vec { F } \right) _ { a v g } = \frac { T } { \Delta t } = 1 5 0 0 0 0 \Ddot { \mathrm { \uparrow } } \ \mathrm { N } .$

# Va chạm một chiều

Thuật ngữ va chạm biểu thị sự kiện hai chất điểm đi lại gần nhau và tương tác với nhau bằng các lực. Các lực tương tác được giả sử rất lớn so với các ngoại lực có mặt, nên có thể sử dụng xấp xỉ xung lực.

Va chạm không chỉ xảy ra khi có sự tiếp xúc trực tiếp giữa hai vật thể vĩ mô, như mô tả trên hình 9.5a, mà phải được hiểu tổng quát hơn. Ví dụ xét một va chạm $\dot { \mathbf { O } }$ tỉ $\mathsf { l e }$ nguyên tử giữa proton và hạt alpha (hình 9.5b). Vì cả hai hạt đều mang điện dương, chúng đẩy nhau, va chạm với nhau thông qua trường điện từ.

![](images/image8.jpg)

Khi hai vật có khối lượng m1 và m2 va chạm như trên hình 9.5, các xung lực có thể thay đổi rất phức tạp, chẳng hạn như trên hình 9.3. Tuy nhiên, bất $\mathrm { k } \mathring { \mathrm { e } }$ sự phức tạp của xung lực, lực luôn là nội lực của hệ hai vật. Do đó, hai vật tạo thành một hệ cô lập và động lượng của hệ được bảo toàn trong va chạm bất kỳ. Tuy nhiên, tổng động năng của hệ có thể bảo toàn hoặc không, tùy thuộc vào loại va chạm.

Hình 9.5 (a) Va chạm giữa hai vật như kết quả của sự tiếp xúc trực tiếp, (b) "Va chạm" giữa hai hạt tích điện.

Phân loại va chạm: Va chạm được chia thành va chạm đàn hồi hoặc va chạm không đàn hồi tùy thuộc vào việc động năng của hệ có bảo toàn hay không.

Va chạm đàn hồi gữa hai vật là va chạm mà tổng động năng và tổng động lượng của hệ trước và sau khi va chạm là như nhau. Va chạm giữa các vật trong thế giới vĩ mô, chẳng hạn giữa các quả bóng bi a, chỉ là xấp xỉ đàn hồi vì có xảy ra sự biến dạng và mất động năng. Ví dụ ta có thể nghe thấy tiếng các quả bi a va chạm nhau, như vậy có một số năng lượng từ hệ đã bị truyền đi xa bởi âm thanh. Va chạm đàn hồi phải hoàn toàn yên lặng

Va chạm không đàn hồi là va chạm mà tổng động năng của hệ trước và sau khi va chạm khác nhau (mặc dù động lượng của hệ được bảo toàn). Các va chạm không đàn hồi có hai loại. Khi các vật dính vào nhau sau khi va chạm được gọi là va chạm hoàn toàn không đàn hồi, ví dụ khi một thiên thạch va chạm với Trái đất. Khi các vật va chạm nhưng không dính vào nhau, nhưng một phần năng lượng bị chuyển sang dạng năng lượng khác hoặc bị truyền ra xa, như trường hợp quả bóng cao su va chạm với một bề mặt cứng, thì va chạm được gọi là không đàn hồi. Khi quả bóng cao su va chạm với nền cứng, một phần động năng của quả bóng bị chuyển đổi (sang nhiệt) khi quả bóng bị biến dạng trong khi nó tiếp xúc với bề mặt cứng. Các va chạm không đàn hồi được mô tả bằng cách diễn giải động lượng của mô hình

# Va chạm hoàn toàn không đàn hồi

Xét 2 vật khối lượng $\mathbf { m } _ { 1 }$ và $\mathbf { m } _ { 2 }$ , chuyển động với các vận tốc ban đầu $\vec { v _ { \ 1 i } } , \vec { v _ { \ 2 i } }$ dọc theo một đường thẳng như trên hình 9.6. Hai vật va chạm trực diện với nhau, dính vào nhau và sau va chạm chúng chuyển động với vận tốc chung $\vec { v _ { \ f } }$ . Do động lượng của một hệ cô lập được bảo toàn trong va chạm bất kì, ta có tổng động lượng trước khi va chạm bằng với động lượng của hệ hợp lại sau khi va chạm:

![](images/image9.jpg)

Hình 9.6 Giản đồ biểu diễn va chạm xuyên tâm hoàn toàn không đàn hồi giữa hai chất điểm

$$
m _ { 1 } \vec { v _ { 1 i } } + m _ { 2 } \vec { v _ { 2 i } } = ( m _ { 1 } + m _ { 2 } ) \vec { v ^ { , } } _ { f }
$$

Giải phương trình này đối với ẩn số là vận tốc sau va chạm, ta được: $m _ { 1 } \vec { v ^ { } } _ { 1 i } + m _ { 2 } \vec { v ^ { } } _ { 2 i }$

# Public_134 

Trong chương này ta sẽ phân tích kĩ chuyển động quay của một vật rắn, cụ thể là phân tích mô hình vật rắn quay với gia tốc góc không đổi, từ đó dẫn ra các phương trình động lực học của mô hình này. Lưu ý, vật rắn là vật không bị biến dạng, tức là vị trí tương đối của các chất điểm cấu tạo nên hệ luôn không đổi. Mọi vật thể thực tế đều bị biến dạng ở mức độ nào đó; tuy nhiên, trong các phân tích dưới đây ta bỏ qua sự biến dạng của vật.

# Tọa độ góc, vận tốc góc và gia tốc góc

Hình 10.1 minh họa một đĩa CD đang quay quanh trục cố định vuông góc với mặt phẳng hình vẽ và đi qua tâm O của đĩa. Một yếu tố nhỏ của đĩa được mô hình hóa như một chất điểm tại P, cách gốc O một khoảng cố định r và quay quanh O theo một vòng tròn bán kính r.

Ta biểu diễn vị trí của P theo tọa độ cực $( r , \theta )$ , với r là khoảng cách từ gốc tọa độ tới $P$ , $\theta$ là góc quay ngược chiều kim đồng hồ từ một đường cố định được chọn làm mốc (đường chuẩn) như trên hình 10.1. Góc $\theta$

![](images/image1.jpg)  
Hình 10.1 Một đĩa compact quay quanh trục cố định qua $O$ và vuông góc với mặt phẳng hình vẽ

thay đổi theo thời gian, còn r không thay đổi. Khi chất điểm chuyển động dọc theo đường tròn bắt đầu từ đường chuẩn $\theta = 0$ , nó chuyển động qua một cung có độ dài s như trên hình 10.1b. Ta có:

$$
\begin{array} { l } { { s = r \theta } } \\ { { \theta = \displaystyle \frac { s } { r } } } \end{array}
$$

Vì $\theta$ là tỉ số giữa độ dài của cung và bán kính của đường tròn nên nó là một số thuần túy (không có đơn vị). Tuy nhiên, ta thường cho đơn vị (giả) của $\theta$ là radian (rad).

Tọa độ góc θ: Vì đĩa là một vật rắn nên khi chất điểm tại P chuyển động quét qua một góc $\theta$ tính từ đường chuẩn thì mỗi yếu tố khác của vật cũng quay và quét qua một góc ??. Nên ta có thể liên kết góc $\theta$ với toàn bộ vật, cũng như liên kết với từng chất điểm riêng biệt, cho phép xác định tọa độ góc của vật rắn trong chuyển động quay. Chọn một đường chuẩn trên vật thì tọa độ góc của vật rắn là góc $\theta$ giữa đường chuẩn này và một đường chuẩn cố định khác (thường là trục x). Tọa độ góc θ trong chuyển động quay đóng vai trò tương tự như vị trí x trong chuyển động tịnh tiến.



Khi chất điểm đang xét chuyển động từ vị trí A tới vị trí B trong khoảng thời gian $\Delta t$ như trên hình 10.2, đường chuẩn gắn với vật quét được một góc $\Delta \theta = \theta _ { f } - \theta _ { i }$ . Đại lượng $\Delta \theta$ này được gọi là độ dời góc của vật rắn:

$$
\Delta \theta \equiv \theta _ { f } - \theta _ { i }
$$

Nếu vật rắn quay nhanh, độ dời này diễn ra trong một khoảng thời gian ngắn. Nếu vật rắn quay chậm, độ dời này diễn ra trong một khoảng thời gian dài hơn. Các tốc độ quay khác nhau được định lượng bởi khái niệm tốc độ góc trung bình $\omega _ { a v g }$ , là tỉ số giữa độ dời góc của vật rắn và khoảng thời gian $\Delta t$ diễn ra độ dời đó:

$$
\omega _ { a v g } = { \frac { \theta _ { f } - \theta _ { i } } { t _ { f } - t _ { i } } } = { \frac { \Delta \theta } { \Delta t } }
$$

![](images/image2.jpg)

Tốc độ góc tức thời $\pmb { \omega }$ được xác định bằng giới hạn của tốc độ góc trung bình khi $\Delta t  0$ :

Hình 10.2 Chất điểm trên vật rắn quay từ (A) tới $( B )$ dọc theo

$$
\omega \equiv \operatorname* { l i m } _ { \Delta t \to 0 } { \frac { \Delta \theta } { \Delta t } } = { \frac { d \theta } { d t } }
$$

cung tròn. Trong khoảng $\Delta t =$ $t _ { f } - t _ { i } ,$ r quét qua một góc

Đơn vị tốc độ góc là rad/s, có thể viết là $\mathbf { S } ^ { - 1 }$ vì rad không có thứ nguyên. ?? dương khi $\theta$ tăng (chuyển động cùng chiều kim đồng hồ), $\omega$ âm khi $\theta$ giảm (chuyển động ngược chiều kim đồng hồ)



Tính mômen quán tính của các vật rắn có hình dạng đơn giản (có tính đối xứng cao) là tương đối dễ với điều kiện trục quay trùng với một trục đối xứng, như trình bày trong mục 10.6 tiếp theo.

![](images/image3.jpg)  
Bảng 10.2: Mômen quán tính của các vật rắn đồng nhất có hình dạng khác nhau

Câu hỏi 10.5: Bạn tắt máy khoan điện và thấy rằng khoảng thời gian để cho mũi khoan dừng lại do mômen lực ma sát trong máy khoan là  t. Bạn thay một mũi khoan lớn hơn có mômen quán tính gấp đôi. Khi mũi khoan lớn hơn này đang quay với tốc độ góc như cái nhỏ lúc đầu và khoan được ngắt điện, mômen lực ma sát vẫn giữ nguyên như trường hợp mũi khoan nhỏ. Khoảng thời gian để mũi khoan lớn hơn dừng lại là (a) 4 t (b) 2 t (b) t (c) 0.5 t (d) 0.25

t (f) không thể xác định được.

# Định lý các trục song song:

Việc tính mômen quán tính đối với một trục quay bất kì là khó khăn, ngay cả với vật có tính đối xứng cao. Ta có thể dùng định lí các trục song song để đơn giản hóa sự tính toán. Giả sử vật trên hình 10.14a quay quanh trục z. Mômen quán tính không phụ thuộc sự phân bố khối lượng dọc trục z. Tưởng tượng làm bẹp một vật thể 3 chiều thành một vật thể 2 chiều như trên hình 10.14b. Trong quá trình này tất cả khối lượng chuyển động song song với trục z cho đến khi nó nằm trong mặt phẳng xy. Các tọa độ khối tâm của vật lúc này là xCM, yCM, $\begin{array} { r } { z _ { \mathrm { C M } } = 0 . } \end{array}$ . Xét phần tử khối lượng dm có các tọa độ (x, ${ \mathrm { y } } , 0 )$ như $\dot { \mathbf { O } }$ hình 10.14c khi nhìn từ trên trục z xuống. Vì phần tử này cách trục z một khoảng $\dot { r } = \sqrt { x ^ { 2 } + y ^ { 2 } }$ , nên mômen quán tính của vật đối với trục z là:

$$
\begin{array} { r } { I = \int r ^ { 2 } d m = \int ( x ^ { 2 } + y ^ { 2 } ) \ d m } \end{array}
$$

![](images/image4.jpg)

Trong đó tốc độ góc thay đổi từ $\omega _ { i }$ đến $\omega _ { f }$ . Phương trình (10.27) là định lý công-động năng đối với chuyển động quay. Định lý này phát biểu rằng công do ngoại lực thực hiện lên vật rắn đối xứng đang quay quanh trục cố định thì bằng độ biến thiên động năng quay của vật.

Định lý này là một dạng của mô hình hệ không cô lập (năng lượng) đã thảo luận trong chương 8. Công thực hiện lên hệ vật rắn biểu thị sự truyền năng lượng qua biên của hệ do sự tăng động năng quay của vật.

Tổng quát, có thể tổ hợp định lí này với định lí công-động năng trong chuyển động tịnh tiến ở chương 7. Cho nên công do ngoại lực thực hiện lên vật bằng độ biến thiên động năng toàn phần gồm động năng tịnh tiến và động năng quay của vật. Ví dụ khi một cầu thủ ném quả bóng thì công thực hiện bởi tay của cầu thủ lên quả bóng bằng động năng do quả bóng chuyển động trong không gian và động năng quay của quả bóng.

Ngoài định lí công-động năng, các nguyên lí năng lượng khác cũng áp dụng được cho chuyển động quay. Ví dụ vật đang quay và không có các lực không bảo toàn tác dụng lên hệ thì có thể dùng mô hình hệ cô lập và nguyên lí bảo toàn cơ năng để phân tích hệ. Độ biến thiên động năng trong phương trình bảo toàn năng lượng 8.2 sẽ gồm cả độ biến thiên động năng tịnh tiến và độ biến thiên động năng quay.

Trong một số trường hợp, nếu cách tiếp cận năng lượng không đủ thông tin để giải bài toán thì phải kết hợp với cách tiếp cận động lượng. Một trường hợp như vậy được minh họa trong ví dụ 10.14 trong mục 10.9.

Bảng 10.3 liệt kê các phương trình liên quan đến chuyển động quay cùng với các công thức tương ứng của chuyển động tịnh tiến. Lưu ý đến sự giống nhau về dạng toán học của các phương trình. Hai phương trình cuối cùng ở cột bên trái của bảng 10.3 liên quan đến mômen động lượng L sẽ được trình bày trong chương 11. Ở đây chúng được đưa vào với mục đích làm hoàn chỉnh bảng các công thức chuyển động quay và chuyển động tịnh tiến.

# Chuyển động lăn của vật rắn

Trong mục này ta xét chuyển động của vật rắn lăn trên mặt phẳng. Ví dụ, xét một khối trụ lăn trên một đường thẳng sao cho trục quay của nó luôn song song với hướng lúc đầu của nó. Như hình 10.18 cho thấy, một điểm trên vành của hình trụ chuyển động theo một đường phức tạp gọi là cycloid. Tuy nhiên ta đơn giản hóa vấn đề bằng cách chú ý đến khối tâm của vật hơn là điểm trên vành của vật đang lăn. Như thấy trên hình 10.18, khối tâm của vật chuyển động theo đường thẳng. Nếu một vật lăn không trượt trên mặt phẳng (gọi là chuyển động lăn thuần túy) thì tồn tại một mối liên hệ đơn giản giữa chuyển động tịnh tiến và chuyển động quay của nó.

![](images/image5.jpg)  
Hình 10.18 Hai điểm trên một vật đang lăn có quỹ đạo khác nhau trong không gian

Xét một khối trụ đồng nhất có bán kính R lăn không trượt trên một mặt phẳng nằm ngang (hình 10.19).

Khi trụ quay được một góc $\theta$ thì khối tâm của nó đi được một đoạn $s = R \theta$ . Do đó, tốc độ chuyển động tịnh tiến của khối tâm là:

$$
v _ { C M } = { \frac { d s } { d t } } = R { \frac { d \theta } { d t } } = R \omega
$$

trong đó $\omega$ là tốc độ góc của hình trụ. Phương trình 10.28 đúng khi khối trụ hoặc khối cầu lăn không trượt và là điều kiện đối với chuyển động lăn thuần túy.

![](images/image6.jpg)

Độ lớn gia tốc tịnh tiến của khối tâm là:

Hình 10.19 Đối với chuyển

động lăn thuần túy, khi hình trụ quay được một góc ?? thì khối tâm của nó đi được một

trong đó ?? là gia tốc góc của khối trụ.

đoạn thẳng $s = R \theta$

Tốc độ góc tức thời của chất điểm chuyển động trên đường tròn hoặc của vật rắn quay quanh trục cố định là

$$
\omega = { \frac { d \theta } { d t } }
$$

Gia tốc góc tức thời của chất điểm chuyển động trên đường tròn hoặc của vật rắn quay quanh trục cố định là

$$
\alpha = { \frac { d \omega } { d t } }
$$

Khi vật rắn quay quanh một trục cố định, các phần của vật có cùng tốc độ góc và gia tốc góc.

Độ lớn của mômen lực liên quan đến lực $\cal F ^ { \sharp }$ tác dụng lên vật tại điểm cách trục quay một khoảng r là:

$$
\tau = r F \sin \varphi = F d
$$

Trong đó $\varphi$ là góc giữa vectơ vị trí của điểm chịu tác dụng của lực và vectơ lực, d là cánh tay đòn của lực, là khoảng cách vuông góc từ trục quay tới giá của lực $\boldsymbol { F } ^ { \sharp }$ .

Mômen quán tính của một hệ chất điểm được định nghĩa là:

$$
I \equiv \sum _ { i } m _ { i } r _ { \imath } ^ { 2 }
$$

Trong đó $\mathbf { m } _ { \mathrm { i } }$ là khối lượng của chất điểm thứ i, ${ \bf { r } } _ { \mathrm { { i } } }$ là khoảng cách từ chất điểm đó đến trục quay.

# Khái niệm và nguyên lý

Khi vật rắn quay quanh trục cố định thì vị trí góc, tốc độ góc và gia tốc góc liên hệ với vị trí, tốc độ dài và gia tốc dài qua các mối liên hệ sau:

$$
\begin{array} { c } { s = r \theta } \\ { v = r \omega } \\ { a _ { t } = r \alpha } \end{array}
$$

Nếu vật rắn quay quanh trục cố định với tốc độ góc $\omega$ , động năng quay của nó là:

$$
K _ { R } = { \frac { 1 } { 2 } } I \omega ^ { 2 }
$$

trong đó I là mômen quán tính của vật đối với trục quay.

Mômen quán tính của vật rắn là:

$$
\begin{array} { r } { I = \int r ^ { 2 } d m } \end{array}
$$

Trong đó r là khoảng cách từ phần tử khối lượng dm đến trục quay.

Tốc độ sinh công của ngoại lực khi làm quay vật rắn quanh $\mathrm { m } \hat { \mathrm { 0 t } }$ trục cố định, hoặc công suất được cung cấp là:

Nếu công thực hiện lên vật rắn và kết quả duy nhất là làm quay vật rắn quanh một trục cố định thì công do các ngoại lực thực hiện khi làm quay vật bằng độ biến thiên động năng quay của vật:

$$
\Sigma W = { \frac { 1 } { 2 } } I \omega _ { f } ^ { 2 } - { \frac { 1 } { 2 } } I \omega _ { i } ^ { 2 }
$$

Động năng toàn phần của một vật rắn lăn không trượt trên mặt phẳng nghiêng thì bằng động năng quay quanh khối tâm của nó cộng với động năng tịnh tiến của khối tâm:

$$
K = \overline { { { \frac { 1 } { 2 } } } } I _ { C M } \omega ^ { 2 } + \overline { { { \frac { 1 } { 2 } } } } \overline { { { M v _ { C M } ^ { 2 } } } }
$$

# Các mô hình phân tích

# Vật rắn quay với gia tốc góc không đổi

Nếu một vật rắn quay quanh trục cố định với gia tốc góc không đổi, có thể áp dụng các phương trình động học tương tự các phương trình động học của chuyển động tịnh tiến với gia tốc không đổi:

α=constant

![](images/image7.jpg)

$$
\begin{array} { c } { \omega _ { f } = \omega _ { i } + \alpha t } \\ { \theta _ { _ { f } } = \theta _ { _ { i } } + \omega _ { _ { i } } t + \displaystyle \frac { 1 } { 2 } \alpha t ^ { 2 } } \end{array}
$$

$$
\begin{array} { c } { { \omega _ { f } ^ { 2 } = \omega _ { i } ^ { 2 } + 2 \alpha ( \theta _ { f } - \theta _ { i } ) } } \\ { { { } } } \\ { { \theta _ { f } = \theta _ { i } + \displaystyle \frac { 1 } { 2 } ( \omega _ { i } + \omega _ { f } ) t } } \end{array}
$$

# Vật rắn quay dưới tác dụng của mômen lực tổng hợp

Nếu vật rắn quay tự do quanh trục cố định và có các mômen ngoại lực tác dụng lên nó, thì vật có gia tốc góc $\alpha$ , trong đó:

$$
\sum \tau _ { e x t } = I \alpha
$$

Phương trình này trong chuyển động quay tương tự như định luật 2 Newton trong mô hình chất điểm chịu tác dụng của hợp lực.

![](images/image8.jpg)

# Public_135 

Chủ đề trung tâm của chương này là mômen động lượng, là đại lượng đóng vai trò quan trọng trong động lực học chuyển động quay. Tương tự như nguyên lý bảo toàn động lượng, ta cũng có nguyên lý bảo toàn mômen động lượng. Mômen động lượng của một hệ cô lập là không đổi. Đối với mômen động lượng, một hệ cô lập là một   
hệ không có các mômen ngoại lực tác dụng lên hệ. Nếu có mômen ngoại lực tác dụng lên hệ thì hệ đó không cô lập. Giống như định luật bảo toàn động lượng, định luật bảo toàn mômen động lượng là một định luật cơ bản của vật lý, nó cũng có giá trị đối với các hệ tương đối và lượng tử.

# Tích vectơ và mômen lực

Điều quan trọng khi xác định mômen động lượng là nhân 2 vectơ bằng toán tử tích có hướng.

Xét lực $F ^ {  }$ tác dụng lên chất điểm tại vị trí vectơ $r ^ {  }$ (hình 11.1). Như đã biết trong mục 10.6, độ lớn của mômen lực của lực này đối với một trục quay đi qua $\mathrm { g } \acute { \mathrm { o c } }$ là $r F$ sin $\varphi$ , trong đó $\varphi$ là góc giữa các vectơ $r ^ {  }$ và $F ^ {  }$ . Trục mà lực $F ^ {  } \acute { \mathbf { o } }$ xu hướng tạo ra chuyển động quay quanh nó là trục vuông góc với mặt phẳng tạo bởi các vectơ $r ^ {  }$ và $F ^ {  }$ .

Vectơ mômen lực $\tau ^ {  }$ được liên kết với các vectơ $r ^ {  }$ và $\vec { F }$ Ta có thể thiết lập một mối liên hệ toán học giữa $\tau ^ {  }$ , $r ^ {  }$ và $\vec { F }$ bởi một toán tử được gọi là tích vectơ:

$$
\vec { \tau ^ { \mathrm { ~ } } } = \vec { r ^ { \mathrm { ~ ~ } } } \times \vec { F ^ { \mathrm { ~ ~ } } }
$$

Bây giờ ta đưa ra một định nghĩa chính thức của tích vectơ. Cho trước hai vectơ $A ^ {  }$ và $B ^ {   }$ bất kì, tích vectơ $A ^ {  } \times \vec { B }$ được định nghĩa như là vectơ thứ ba $C ^ {  }$ có độ lớn bằng ??⃗??⃗⃗ sin $\theta$ , trong đó $\theta$ là góc giữa hai vectơ $A ^ {  }$ và $B ^ {   }$ . Tức $C ^ {  }$ $\boldsymbol { C } ^ {  } = \boldsymbol { A } ^ {  } \times \boldsymbol { B } ^ {  }$ là $C =$ $A B$ sin $\theta$ .

![](images/image1.jpg)

Hình 11.1: Vectơ mômen lực $\vec { \tau }$ hướng vuông góc với mặt phẳng tạo bởi vectơ vị trí ??⃗ và vectơ lực tác dụng $F ^ {  }$ . Trên hình vẽ này, ??⃗ và $F ^ {  }$ nằm trong mặt phẳng xy, nên mômen lực dọc theo trục z.

# Mô hình phân tích : $\mathbf { H } \hat { \mathbf { e } }$ không cô lập (mômen động lượng)

Hình dung một cái cột được dựng lên trên một hồ nước đóng băng (hình 11.3). Một người trượt băng trượt nhanh $\mathbf { v } \dot { \hat { \mathbf { e } } }$ phía cái cột, theo hướng hơi lệch sang bên để không va vào cái cột.



Khi cô ta trượt ngang qua cái cột, cô ta chìa tay ra bên hông và túm lấy cái cột. Hành động này làm cho cô ta chuyển động tròn xung quanh cái cột. Giống như ý tưởng về động lượng giúp ta phân tích chuyển động tịnh tiến, một sự tương tự trong chuyển động quay, mômen

Bây giờ ta có thể viết (11.9) như sau:

Mo men dōng luong $\vec { L }$ cia chát dièm dói vói truc quay là mòt vecto vuòng góc vói cà vecto vi trí $\vec { r }$ và dōng luong $\dot { P }$ cúa nó.

![](images/image2.jpg)  
Hình 11.4: Mômen động lượng $\vec { L }$ của chất điểm là một véctơ cho bởi $\scriptstyle { \vec { L } } = { \vec { r } } \times { \vec { p } }$



# Mômen động lượng của hệ chất điểm

Dùng các kỹ thuật như trong mục 9.7, ta có thể chỉ ra rằng định luật 2 Newton đối với hệ chất điểm là:

$$
\sum \stackrel {  } { F } _ { e x t } = \frac { d \stackrel {  } { P } _ { t o t } } { d t }
$$

Phương trình này cho thấy tổng ngoại lực tác dụng lên hệ chất điểm thì bằng tốc độ biến thiên theo thời gian của động lượng toàn phần của hệ.

Ta hãy xem một phát biểu tương tự như vậy có thể được thực hiện đối với chuyển động quay hay không. Mômen động lượng toàn phần của hệ chất điểm đối với một trục quay nào đó được xác định bằng tổng véctơ mômen động lượng của từng chất điểm riêng biệt:

$$
L _ { t o t } = L _ { 1 } + L _ { 2 } + L _ { 3 } + . . . + L _ { n } = \sum L _ { i }
$$

trong đó tổng vectơ được lấy trên toàn bộ n chất điểm của hệ.

Lấy đạo hàm biểu thức này theo thời gian ta có:

$$
\frac { d L _ { t o t } } { d t } = \sum \frac { d L _ { i } } { d t } = \sum \vec { \tau _ { i } }
$$

Ở đây ta đã dùng phương trình (11.11) để thay thế tốc độ biến thiên theo thời gian của mômen động lượng của mỗi chất điểm với mômen lực tác dụng lên mỗi chất điểm.



Phương trình này trong chuyển động quay tương tự với phương trình $\sum { \vec { F _ { e x t } } } = \frac { d P _ { t o t } } { d t }$ đối

với hệ chất điểm. Phương trình 11.13 là biểu diễn toán học của sự diễn tả $\mathrm { m } \hat { \mathrm { o } }$ hình hệ không cô lập mômen động lượng. Nếu hệ không cô lập theo nghĩa có mômen lực tác dụng lên nó, thì mômen lực bằng tốc độ biến thiên theo thời gian của mômen động lượng.

Mặc dù ta không chứng minh ở đây, nhưng phát biểu này là đúng bất kể chuyển động của khối tâm. Nó có thể áp dụng ngay cả khi khối tâm đang gia tốc, miễn là mômen lực và mômen động lượng được đánh giá so với một trục quay đi qua khối tâm.

Sắp xếp lại phương trình 11.13 và lấy tích phân ta được

$$
\int ( \sum _ { \tau } \vec { \tau } _ { \ e x t } ) d t = \Delta L _ { _ { t o t } }
$$

Phương trình này trong chuyển động quay tương tự với phương trình của định lí xung lực-động lượng của hệ chất điểm (9.40). Phương trình này biểu diễn định lí xung lượng của mômen lực- mômen động lượng.

# Mômen động lượng của vật rắn quay

Trong ví dụ 11.4, ta đã khảo sát mômen động lượng của một hệ có thể biến dạng. Bây giờ ta sẽ tập trung sự chú ý vào hệ không biến dạng, gọi là vật rắn. Xét vật rắn quay quanh một trục cố định trùng với trục z của hệ tọa độ như chỉ ra trên hình 11.7.

Ta hãy xác định mômen động lượng của vật này. Mỗi chất điểm của vật này quay trong một mặt phẳng xy quanh trục z với tần số góc  . Độ lớn của mômen động lượng của

![](images/image3.jpg)

Hình 11.7: Khi vật rắn quay quanh trục, mômen động lượng $\vec { L }$ cùng hướng với vectơ vận tốc góc $\vec { \omega }$ , theo mối liên hệ $\vec { L } = I \vec { \omega }$



# Mô hình phân tích: hệ cô lập (mômen động lượng)

Trong chương 9 ta đã thấy rằng động lượng toàn phần của một hệ chất điểm là không đổi nếu hệ cô lập, tức là khi ngoại lực tác dụng lên hệ bằng không. Trong chuyển động quay, ta cũng có một định luật bảo toàn tương tự:

“Mômen động lượng toàn phần của một hệ không đổi cả độ lớn và hướng (bảo toàn) nếu tổng mômen ngoại lực tác dụng lên hệ bằng không, hoặc hệ cô lập“.

Phát biểu này thường được gọi là nguyên lý bảo toàn mômen động lượng và là cơ sở cho cách diễn tả mômen động lượng của mô hình hệ cô lập.

# Chuyển động hồi chuyển và các con cù

Một kiểu chuyển động khác lạ và hấp dẫn có thể bạn đã biết là con cù quay quanh trục đối xứng của nó như trên hình 11.13a. Nếu con cù quay nhanh, trục đối xứng của nó quay quanh trục z, vẽ ra một hình nón, (Hình 11.13b). Chuyển động của trục đối xứng xung quanh trục thẳng đứng, được biết tới như là chuyển động tiến động, thường là chậm so với chuyển động quay của con cù.

![](images/image4.jpg)  
Hình 11.13. Chuyển động tiến động của con cù quay quanh trục đối xứng của nó. a) Các ngoại lực tác dụng lên con cù chỉ là phản lực pháp tuyến n và trọng lực $M \vec { g }$ . Hướng của mômen động lượng L dọc theo trục đối xứng. b) Vì $\vec { L } _ { f } = \Delta \vec { L } + \vec { L } _ { i }$ nên con cù tiến động quanh

Câu hỏi nảy sinh một cách tự nhiên ở đây là tại sao con cù không bị đổ xuống. Vì khối tâm của nó không ở ngay trên điểm trụ O, nên có một mômen lực tác dụng lên con cù đối với trục quay đi qua O, mômen lực này gây bởi trọng lực Mg . Con cù sẽ đổ xuống nếu như nó không quay. Tuy nhiên vì nó quay, nên nó có một mômen động lượng $L$ hướng dọc theo trục đối xứng của nó. Ta sẽ chỉ ra rằng trục đối xứng này chuyển động xung quanh trục z (xảy ra chuyển động tiến động) vì mômen lực làm cho hướng của trục đối xứng thay đổi. Sự minh họa này là một ví dụ tuyệt vời về tầm quan trọng của bản chất véctơ của mômen động lượng.





Biểu thức này chỉ ra rằng trong khoảng thời gian vô cùng nhỏ dt, mômen lực gây ra một độ biến thiên mômen động lượng $d \vec { L }$ , cùng hướng với  . Do đó, giống như véctơ mômen lực, dL cũng phải vuông góc với $\vec { L }$ . Hình 11.14c minh họa chuyển động tiến động của trục đối xứng của con quay. Trong khoảng thời gian dt, độ biến thiên mômen động lượng là $d \vec { L } = \vec { L _ { f } } - \vec { L _ { i } } = \tau \vec { d t }$ . Vì dL vuông góc với $\vec { L } ^ { \vec { \mathbf { \Phi } } }$ , nên độ lớn của $\bar { L }$ không thay đổi, $\left| \vec { L } _ { f } \right| = \left| \vec { L } _ { i } \right|$ . Hơn nữa, sự thay đổi chỉ là hướng của $\vec { L }$ . Vì sự thay đổi mômen động lượng dL là theo hướng của  , nằm trong mặt phẳng xy, nên con quay hồi chuyển chịu chuyển động tiến động.

![](images/image5.jpg)

Trong hrc Mg theo chièu am cia truc z, gày ra mò men hrc len con quay theo chièu durong cia truc y dóivói dièm try.

Mò men lrc gày ra dò bièn thièn mò men dòng lrong di cia con quay theo huóng song song vói mò men luc. Truc cùa con quay quét durgc góc $d \phi$ trong khoàng thòi gian dt.

Hình 11.14. a) Một con quay hồi chuyển được đặt trên một cái trụ ở đầu mút bên phải. b) Giản đồ đối với con quay chỉ ra các lực, mômen lực và mômen động lượng. c) Nhìn từ trên xuống (dọc theo trục z) các vectơ mômen động lượng của con quay tại thời điểm đầu và cuối của khoảng thời gian rất ngắn dt.

Để đơn giản hóa sự mô tả hệ, giả sử mômen động lượng toàn phần của bánh xe tiến động là tổng của mômen động lượng I do quay và mômen động lượng do chuyển động của khối tâm so với trục đứng. Trong cách xử lý này, ta bỏ qua phần đóng góp của chuyển động của khối tâm và lấy mômen động lượng toàn phần chỉ là I . Trong thực hành, sự xấp xỉ này là tốt khi  lớn.

Giản đồ véctơ trên hình 11.14c cho thấy rằng trong khoảng thời gian dt, véctơ mômen động lượng quay được một góc $d \phi$ , cũng là góc mà con quay hồi chuyển quay được. Từ tam



Chia cả 2 vế cho dt và dùng công thức L = I ta thấy rằng tốc độ trục xe quay đối với trục thẳng đứng là:

$$
\mathfrak { O } _ { P } = \frac { d \Phi } { d t } = \frac { \mathbf { M } \mathbf { g r } _ { \mathrm { C M } } } { \mathrm { I } \odot }
$$

Tần số góc ${ \mathfrak { O } } _ { P }$ gọi là tần số tiến động. Kết quả này chỉ đúng khi ${ \mathfrak { O } } _ { P } < < { \mathfrak { O } }$ . Nếu không, sẽ liên quan đến một chuyển động phức tạp hơn nhiều. Như bạn có thể thấy từ phương trình (11.20), điều kiện ${ \mathfrak { O } } P < < { \mathfrak { O } }$ thỏa mãn khi  rất lớn, tức là khi bánh xe quay rất nhanh. Hơn nữa, chú ý rằng tần số tiến động suy giảm khi  tăng, tức là khi bánh xe quay càng nhanh quanh trục đối xứng của nó.

Một ví dụ về con quay hồi chuyển, giả sử bạn đang ở trên một con tàu vũ trụ trong không gian xa xôi, và bạn cần thay đổi quỹ đạo của tàu. Để lái động cơ chạy đúng hướng, bạn cần phải xoay tàu vũ trụ. Tuy nhiên, làm thế nào để bạn xoay con tàu vũ trụ trong không gian trống rỗng? Cách thứ nhất là phải có các động cơ tên lửa nhỏ bắn ra vuông góc với tàu, cung cấp một mômen lực đối với khối tâm của tàu. Một cơ cấu như vậy là đáng mong muốn, và nhiều tàu vũ trụ có các tên lửa như vậy.

![](images/image6.jpg)  
Hình 11.15. a) Tàu vũ trụ mang theo một con quay đang đứng yên chưa quay.

![](images/image7.jpg)  
b) Con quay được điều khiển cho quay.



Tuy nhiên, ta hãy khảo sát phương pháp khác liên quan tới mômen động lượng, và không đòi hỏi tiêu thụ nhiên liệu tên lửa. Giả sử tàu vũ trụ mang một con quay hồi chuyển không quay như trên hình 11.15a. Trong trường hợp này, mômen động lượng của tàu vũ trụ đối với khối tâm của nó bằng không. Giả sử con quay được làm cho quay, cung cấp cho nó một mômen động lượng khác không. Không có mômen ngoại lực tác dụng lên hệ cô lập (tàu vũ trụ-con quay), cho nên mômen động lượng của hệ này phải bằng không theo mô hình hệ cô lập (mômen động lượng). Mômen động lượng của hệ bằng không nếu tàu vũ trụ quay theo chiều ngược với chiều quay của con quay sao cho véc tơ mômen động lượng của tàu và của con quay khử lẫn nhau. Kết quả của việc làm cho con quay quay như trên hình 11.15b là tàu quay vòng. Bằng cách bố trí ba con quay theo ba trục vuông góc với nhau, có thể thu được sự quay mong muốn trong không gian.



Hiệu ứng này tạo ra một tình huống không mong muốn đối với tàu Voyager 2 trong chuyến bay của nó. Tàu này đã mang một máy ghi âm (dùng băng) mà phần guồng (ống) của nó quay ở tốc độ rất cao. Mỗi lần máy thu băng được bật lên, guồng tác dụng như một con quay hồi chuyển và tàu bị quay theo hướng ngược lại. Sự quay này đã được Trung tâm điều khiển tàu (Mission Control) dùng các vòi phun bắn về một phía để dừng sự quay.

Câu hỏi 11.1: Cho hai quả cầu đặc và rỗng cùng khối lượng và bán kính. Chúng chuyển động quay cùng tốc độ góc. Hỏi quả cầu nào có mômen động lượng lớn hơn:

(a) Quả cầu đặc.   
(b) Quả cầu rỗng.   
(c) Bằng nhau.   
(d) Không thể xác định.

Câu hỏi 11.2: Một người thợ lặn lao ra từ tàu xuống nước với cơ thể duỗi thẳng và quay chậm. Hỏi động năng quay của cô ấy sẽ như thế nào:

(a) Tăng lên.   
(b) Giảm đi.   
(c) Không đổi.   
(d) Không thể xác định.   
Mômen động lượng $\vec { L }$ đối với một trục quay đi qua gốc O của chất điểm có động lượng   
${ \vec { p } } = m { \vec { \nu } }$ là $L \equiv { \stackrel {  } { \mathbf { r } } } \times { \stackrel {  } { \mathbf { p } } } ( 1 1 . 1 0 )$   
trong đó $\vec { r }$ là véc tơ vị trí của chất điểm so với gốc O.





1. Cho hệ gồm: một thanh nhẹ, mảnh có chiều dài $1 { = } 1 \mathrm { m }$ , hai vật (xem như chất điểm) được gắn hai đầu thanh. Hạt một khối lượng $m _ { 1 } = 4 k g$ và vật hai khối lượng $m _ { 2 } = 3 k g$ . $\mathrm { H } \hat { \mathrm { e } }$ quay quanh tâm, trong mặt phẳng xy (như hình). Tính momen động lượng của hệ so với gốc biết tốc độ của mỗi hạt là ${ 5 , 0 0 } \mathrm { m } / \mathrm { s }$ .

![](images/image8.jpg)

2. Một vật nặng có ${ \bf m } = 2 { \bf k g }$ được gắn vào đầu của một sợi dây quấn quanh ròng rọc như hình vẽ. Ròng rọc là một vành tròn bán kính R $\ l = 8 \mathrm { { c m } }$ và khối lượng $\mathbf { M } = 2 \mathrm { k g }$ . Các nan hoa có khối lượng không đáng $\mathrm { k } \mathring { \mathrm { e } }$ .

![](images/image9.jpg)

(a) Tính tổng mômen lực đối với trục ròng rọc.   
(b) Khi vật chuyển động với tốc độ v thì ròng rọc quay với tốc độ $\begin{array} { r } { \mathrm { g } \dot { \mathrm { o c } } = \frac { \mathtt { v } } { \mathtt { R } } } \end{array}$ Xác định tổng mômen động lượng của hệ đối với trục ròng rọc theo v.   
(c) Sử dụng kết quả câu a và τ = d L để tính gia tốc của ròng rọ dt

3. Một hạt $5 . 0 0 \mathrm { k g }$ bắt đầu chuyển động từ $\mathrm { g } \acute { \mathrm { o c } }$ tại $\mathbf { t } = 0 . \mathrm { V } \hat { \mathbf { a } } \mathbf { n }$ tốc cho bởi phương trình:

$$
v ^ {  } = ( 6 t ^ { 2 } l ^ {  } + 2 t \vec { \jmath ^ {  } } )
$$

Với $v ^ {  }$ tính bằng m/s và t tính bằng s.

(a) Tìm vị trí của nó theo thời gian.   
(b) Mô tả chuyển động của nó.   
(c) Tính gia tốc theo thời gian   
(d) Tính tổng ngoại lực tác động lên hạt theo thời gian,   
(e) Tính tổng momen ngoại lực so với $\mathrm { g } \acute { \mathrm { o c } }$ tác động lên hạt theo thời gian, (f) Tính mômen động lượng so với $\mathrm { g } \acute { \mathrm { o c } }$ theo thời gian   
(g) Tính động năng của hạt theo thời gian,   
(h) Tính công suất truyền cho hạt theo thời gian.

4. Một đĩa khối lượng đồng nhất $\mathrm { m } = 3 { , } 0 0 \mathrm { k g }$ và bán kính $\mathrm { \Delta r } = 0 { , } 2 0 0 \mathrm { \ m }$ quay quanh một trục cố định vuông góc với đĩa với tần số góc 6,00 rad / s. Tính độ lớn mômen động lượng của đĩa khi trục quay

(a) Đi qua khối tâm của đĩa (b) Đi qua một điểm giữa khối tâm và vành đĩa.





5. Khoảng cách giữa tâm của hai bánh xe của một xe máy là 155 cm. Khối tâm của xe máy, $\mathrm { k } \mathring { \mathrm { e } }$ cả người lái nằm trên mặt đất 88 cm và $\dot { \mathbf { O } }$ giữa 2 bánh xe. Giả sử khối lượng của mỗi bánh xe không đáng $\mathrm { k } \mathring { \mathrm { e } }$ so với người lái và xe. Động cơ chỉ lái bánh sau. Hỏi giá trị gia tốc theo phương ngang nào của xe máy sẽ làm bánh xe trước văng lên khỏi mặt đất.

6. Một bàn xoay bán kính $\mathtt { R } = 2 , 0 0 \mathrm { m } \mathrm { c } \mathrm { \dot { c } }$ mômen quán tính $\mathrm { I } = 2 5 0 \ k g m ^ { 2 }$ và quay không có ma sát ở tốc độ 10,0 vòng / phút theo một trục vuông góc với nó. Một đứa trẻ nặng 25,0 kg nhảy lên vòng xoay và ngồi xuống cạnh vòng xoay. Tìm tốc độ góc mới của vòng xoay?

7. Một học sinh ngồi trên một chiếc ghế xoay tự do cầm hai quả tạ, mỗi chiếc có khối lượng ${ 3 , 0 0 } \mathrm { k g }$ (như hình). Khi dang tay ra theo chiều ngang (hình a), tạ cách trục quay là $1 . 0 0 \mathrm { m }$ và học sinh quay với tốc độ góc là 0,750 rad / s. Tổng momen quán tính của ghế xoay và học sinh đối với trục quay là 3,00 $\mathrm { k g . m } ^ { 2 }$ và được xem như không đổi. Học sinh co tay lại theo chiều ngang tới vị trí quả tạ cách trục xoay $0 { , } 3 0 0 \mathrm { m }$ (hình b).

(a) Tìm tốc độ góc mới của học sinh.   
(b) Tìm động năng quay của hệ trước và sau khi học sinh co tay.

8. Một khối gỗ có khối lượng M đăt trên bề mặt bàn nằm ngang không ma sát được gắn vào một thanh cứng có chiều dài l và khối lượng không đáng $\mathrm { k } \mathring { \mathrm { e } }$ (hình), thanh cứng này được gắn một đầu cố định vào bàn và có thể xoay quanh đầu này. Một viên đạn chuyển động trên bề mặt mặt bàn với vận tốc v có phương vuông góc với thanh cứng đến va chạm và cắm vào khối gỗ.

![](images/image10.jpg)

(a) Tính mômen động lượng của hệ viên đạn – khối $\mathbf { g } \tilde { \hat { 0 } }$ đối với trục quay thẳng đứng đi qua điểm cố định của thanh cứng.   
(b) Tính tỷ số phần năng lượng của viên đạn đươc chuyển hóa thành nội năng của hệ sau va chạm.

9. Một viên đạn nặng 0,005kg được bắn vào cánh cửa nặng $1 8 \mathrm { k g }$ theo phương ngang với tốc độ $1 0 3 ~ \mathrm { m / s }$ , viên đạn cắm vào cửa ở vị trí các mép dưới một đoạn $1 0 \mathrm { \ c m }$ (như hình). Cánh cửa rộng 1 m và có thể xoay quanh bản lề, bỏ qua ma sát.

![](images/image11.jpg)

(a) Trước khi viên đạn chạm vào cánh cửa nó có mômen động lượng so với trục quay của cánh cửa hay không?   
(b) Nếu có hãy tính giá trị của mômen động lượng này, nếu không hãy giải thích.   
(c) Cơ năng của hệ viên đạn – cánh cửa có bảo toàn trong suốt quá trình va chạm không?



(d) Tốc độ góc của cánh cửa ngay sau khi va chạm là bao nhiêu?   
(e) Tính tổng năng lượng của hệ viên đạn – cánh cửa sau va chạm và xác định xem nó ít hơn hay bằng với động năng của viên đạn trước khi va chạm.



10. Ba vật có khối lượng bằng nhau được gắn với một thanh cứng không có khối lượng như hình. Thanh cứng đang nằm ngang, đứng yên thì bắt đầu xoay tự do trong mặt phẳng

![](images/image12.jpg)

thẳng đứng với trục quay đi qua điểm P. Giả sử m và d đã biết, hãy tìm

(a) Mômen quán tính của 3 vật này đối với trục quay qua P, (b) Mômen xoắn tác động lên hệ tại $\mathrm { t } = 0$ ,   
(c) Gia tốc góc của hệ tại $\mathrm { t } = 0$ ,   
(d) Gia tốc tiếp tuyến của vật 3 tại $\mathrm { t } = 0$ ,   
(e) Động năng cực đại của hệ,   
(f) Tốc độ góc tối đa thanh đạt được,   
(g) Mômen động lượng cực đại của hệ và   
(h) Tốc độ cực đại của vật hai.

11. Bắn một viên đạn có khối lượng m với tốc độ $v _ { i }$ về phía phải (như hình a) và đâm vào đầu thanh sắt cố định có khối lượng M, chiều dài d, xoay quanh trục không ma sát vuông góc với mặt phẳng hình vẽ qua O (như hình). Chúng ta muốn xác định được tỷ số động năng thay đổi trong hệ do va chạm.

(a) Mô hình phân tích nào thích hợp để mô tả chuyển động của viên đạn và thanh sắt?

![](images/image13.jpg)

(b) Xác định mômen động lượng của hệ trước va chạm đối với trục quay qua O? (c) Mômen quán tính của hệ đối với trục qua O sau khi m cắm vào thanh.   
(d) Nếu tốc độ góc của hệ thống sau va chạm là ω, xác định mômen động lượng của hệ sau va chạm.   
(e) Tính tốc độ góc ω sau va chạm,   
(f) Tính động năng của cơ hệ trước khi va chạm và   
(g) Tính động năng của cơ hệ sau va chạm.   
(h) Tính tỷ số động năng trước và sau va chạm.   
12. Hai phi hành gia (như hình), mỗi người có khối lượng 75kg, được nối với nhau bằng một sợi dây dài 10 m và có khối lượng không đáng kể. Xem như họ cô lập trong không gian   
và quay quanh khối tâm của họ với tốc độ 5 m/s. Xem như các phi hành gia là các chất điểm

(a) Tính độ lớn của mômen động lượng của

![](images/image14.jpg)



hệ hai phi hành gia và (b) Tính động năng quay của hệ.



Một phi hành gia kéo sợi dây thừng để rút ngắn khoảng cách giữa hai người còn $5 \textrm { m }$ . Hãy tính

(c) Mômen động lượng mới của hệ,   
(d) Tốc độ mới của phi hành gia và   
(e) Động năng quay mới của hệ thống.   
(f) Hóa năng dự trữ trong cơ thể của phi hành gia đã được chuyển đổi thành cơ năng của hệ khi anh ta rút ngắn sợi dây là bao nhiêu?

13. Hiện tượng nóng lên của Trái đất đang rất được quan tâm bởi vì ngay cả những thay đổi nhỏ trong nhiệt độ Trái đất có thể có những hậu quả đáng $\mathrm { k } \mathring { \mathbf { e } }$ . Ví dụ, nếu những tảng băng ở hai cực của Trái đất tan chảy hoàn toàn, thì nước trong các đại dương nhiều lên và làm tràn ngập nhiều vùng duyên hải.

Mô hình tảng băng ở 2 cực có khối lượng $2 . 3 \times 1 0 ^ { 1 9 } \mathrm { k g }$ và có dạng đĩa phẳng bán kính 6 $\times 1 0 ^ { 5 } \mathrm { m }$ . Giả sử các tảng băng sau khi tan chảy sẽ tạo thành lớp vỏ hình cầu là nước bao quanh Trái đất. Hỏi độ dài một ngày đêm thay đổi một lượng bao nhiêu so với hiện tại là 24 giờ/ngày? (tính theo giây và $\%$ ). Cho khối lượng Trái đất là 5,972 × 1024kg và bán kính Trái đất là $6 3 7 1 \ \mathrm { k m }$ .

# Public_136 

Cân bằng tĩnh là trạng thái chuyển động đặc biệt của vật rắn. Khi đó, vật rắn có vận tốc chuyển động tịnh tiến và vận tốc chuyển động quay đều bằng 0 trong một hệ quy chiếu quán tính. Trạng thái cân bằng tĩnh này được ứng dụng rất nhiều trong kỹ thuật dân dụng, kiến trúc và cơ khí.

# Mô hình phân tích: Vật rắn ở trạng thái cân bằng

Cân bằng có nghĩa là một vật chuyển động với vận tốc dài và vận tốc góc không đổi so với một quan sát viên trong một hệ quy chiếu quán tính.

Ở đây ta quan tâm đến trường hợp đặc biệt mà cả hai loại vận tốc này bằng không

• Trường hợp này được gọi là cân bằng tĩnh.

Cân bằng tĩnh là một tình huống thường gặp trong kỹ thuật, đặc biệt là trong xây dựng, kiến trúc và cơ khí.

# Sự đàn hồi:

Chúng ta có thể thảo luận về việc các vật bị biến dạng như thế nào trong điều kiện chịu tải.

Một vật đàn hồi sẽ trở lại hình dạng ban đầu khi không còn lực làm nó biến dạng.

Người ta định nghĩa nhiều hằng số đàn hồi khác nhau, tương ứng với mỗi kiểu biến dạng khác nhau.

Trong mô hình hạt ở trạng thái cân bằng thì một hạt chuyển động với vận tốc không đổi do hợp lực tác dụng lên nó bằng không.

Với các vật thật (dạng mở rộng) thì tình huống sẽ phức tạp hơn nhiều.

• Thường thì không thể xem các vật là các hạt.

Với một vật thật ở trạng thái cân bằng thì cần thỏa mãn một điều kiện thứ hai:

• Điều kiện này liên quan đến chuyển động quay của vật.

Một vật khi ở trạng thái cân bằng tĩnh thì: tổng ngoại lực và tổng mômen ngoại lực tác dụng lên vật bằng 0.

Các điều kiện này mô tả mô hình vật rắn ở trạng thái cân bằng.



Các lưu ý về cân bằng:

Cân bằng tịnh tiến

Điều kiện thứ nhất về cân bằng là phát biểu về cân bằng tịnh tiến.

• Gia tốc tịnh tiến của khối tâm của vật phải bằng không.   
• Điều này được áp dụng trong một hệ quy chiếu quán tính.

Cân bằng quay

• Điều kiện thứ hai về cân bằng là một phát biểu về cân bằng quay.   
• Gia tốc góc của vật bằng không.   
• Điều này phải đúng với mọi trục quay.

# Cân bằng động và cân bằng tĩnh

Trong chương này, ta tập trung vào cân bằng tĩnh.

• Vật không chuyển động. • $\mathbf { v } _ { \mathrm { C M } } = 0$ và $\omega = 0$

Mômen hợp lực bằng không không có nghĩa là vật không chuyển động quay.

Cân bằng động cũng có thể xảy ra.

• Vật có thể quay với vận tốc góc không đổi.   
• Vật có thể chuyển động với vận tốc khối tâm không đổi.

# Các phương trình trong cân bằng

Ta sẽ giới hạn các ứng dụng cho các tình huống mà các lực nằm trong mặt phẳng xy

• Các lực này được gọi là đồng phẳng vì chúng cùng nằm trong một mặt phẳng • Giới hạn này dẫn đến 3 phương trình theo các trục.

Các phương trình này là:

$\begin{array} { c } { { \Sigma \mathrm { F _ { x } } = 0 } } \\ { { \ } } \\ { { \mathrm { : } \Sigma \mathrm { F _ { y } } = 0 } } \\ { { \ } } \\ { { \Sigma \mathrm { { \tau _ { z } } = 0 } } } \end{array}$ (12.3)

Vị trí của trục của phương trình mômen quay được chọn bất kỳ.



Ví dụ về vật rắn ở trạng thái cân bằng

Chiến lược giải toán về cân bằng

Khái niệm hóa

Tìm tất cả các lực tác dụng lên vật.

Hình dung ảnh hưởng của mỗi lực đến sự quay của vật như là chỉ có lực này tác dụng lên vật.

Phân loại



Khẳng định rằng vật là một vật rắn cân bằng.

Vật phải có gia tốc tịnh tiến và gia tốc góc bằng không.

# Phân tích

Vẽ một sơ đồ.

Vẽ và đặt tên tất cả các ngoại lực tác dụng lên vật.

Mô hình hạt chịu tác dụng của hợp lực: có thể biểu diễn vật như là một điểm trong sơ đồ lực vì ta không quan tâm đến điểm tác động của lực lên vật.

Mô hình vật rắn cân bằng: Không thể biểu diễn vật bằng một điểm vì điểm tác động của các lực là quan trọng.

Lập một hệ tọa độ thuận tiện.

Tìm thành phần của các lực theo hai trục tọa độ.

Trọng tâm của hệ gồm chai rượu và giá đỡ rơi đúng vào điểm đặt của giá đỡ

![](images/image1.jpg)  
Hình 12.1: Hệ chai rượu và giá đỡ cân bằng

Áp dụng điều kiện thứ nhất về cân bằng $( \mathrm { { \Sigma F { = } 0 } } )$ .

Cẩn thận với các dấu cộng, trừ.

Chọn một trục thuận tiện cho việc tính mômen quay tổng hợp đối với vật rắn: Nhớ rằng việc chọn trục là tùy ý.

Chọn một trục sao cho các phép tính là đơn giản nhất: Lực tác dụng dọc theo đường thẳng đi qua gốc có mômen quay bằng không

Áp dụng điều kiện thứ 2 của cân bằng.

Hai điều kiện cân bằng sẽ cho ta một hệ phương trình.

Giải hệ phương trình.

# Hoàn tất

Bảo đảm rằng các kết quả là phù hợp với sơ đồ ban đầu.

Nếu lời giải cho thấy một lực âm thì lực đó ngược với chiều mà ta đã vẽ trong sơ đồ.

Kiểm tra các kết quả để bảo đảm rằng: $\sum F _ { x } = 0 , \sum F _ { y } = 0 , \sum F _ { z } = 0 \ : .$

Sự cân bằng của hệ chai rượu và giá đỡ trong hình 12.1 là một ví dụ thú vị về trạng thái cân bằng tĩnh của vật rắn. Để chai rượu có thể đứng cân bằng trên giá đỡ thì cần hai điều kiện:



tổng hợp lực và tổng mômen lực tác dụng lên hệ phải bằng không. Để điều kiện thứ hai được thỏa mãn thì trọng tâm của hệ $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ chai rượu và giá đỡ phải ở trên đường thẳng đứng đi qua điểm đặt của giá đỡ trên bàn.



# Bài tập mẫu 12.1: Người đứng trên xà ngang:

Một thanh xà đồng chất nằm ngang có chiều dài $l { = } 8 . 0 0 \mathrm { m }$ và trọng lượng $W _ { b } { = } 2 0 0 \ \mathrm { N }$ được gắn vào tường bởi một trục quay. Đầu còn lại của xà được móc vào cáp treo lập một góc $\Phi { = } 5 3 ^ { \circ }$ so với xà (hình 12.8a). Một người có trọng lượng $\mathrm { W p { = } 5 6 0 0 \mathrm { N } }$ đứng trên xà và cách tường một khoảng $\mathrm { d } { = } 2 . 0 0$ N. Tìm lực căng của cáp treo cũng như độ lớn và hướng của lực mà tường tác dụng lên xà.

Giải:

# Khái niệm hóa

Thanh xà là đồng chất.

![](images/image2.jpg)

Trọng tâm của xà là ở tâm hình học của xà (trung điểm của xà). \$\rac\$

Người đứng trên xà.

Lực căng của cáp và lực mà tường tác dụng lên xà là gì?

# Phân loại

Hệ đứng yên, phân loại bài toán như là một vật rắn nằm cân bằng.

# Phân tích

Vẽ một sơ đồ lực (hình 12.8b).

Dùng trục quay cho trong bài toán (nằm trên tường) làm trục quay: Cách này là đơn giản nhất

Lưu ý là ở đây có 3 ẩn số (đại lượng cần tìm) là T, R, .

Có thể phân tích các lực thành các thành phần.

Áp dụng 2 điều kiện cân bằng, ta thu được 3 phương trình.

Giải hệ phương trình để tìm các ẩn số.

# Hoàn tất

Giá trị của $\theta$ cho thấy hướng của $R$ trong đồ thị là đúng.

![](images/image3.jpg)

Rsin θ

![](images/image4.jpg)



# Bài tập mẫu 12.2: Thang dựng nghiêng

Một cái thang đồng chất có chiều dài l tựa vào một cái tường nhẵn, thẳng đứng (hình 12.9a). Khối lượng của thang là m và hệ số ma sát giữa thang và sàn nhà là $\scriptstyle \mu = 0 , 4 0$ . Tìm góc nghiêng nhỏ nhất $\theta _ { \mathrm { m i n } }$ để thang không bị trượt.

# Khái niệm hóa

Thang là đồng chất.

Trọng lượng của thang đặt $\dot { \mathbf { O } }$ tâm hình học của nó (cũng là trọng tâm).

Giữa thang và sàn nhà có ma sát nghỉ (ma sát tĩnh).

# Phân loại

![](images/image5.jpg)

Mô hình hóa vật như là một vật rắn nằm cân bằng: do ta không muốn thang trượt

# Phân tích

$\mathrm { V } \tilde { \mathrm { e } } \mathrm { m } \hat { \mathrm { o } } \mathrm { t }$ sơ đồ chỉ ra tất cả các lực tác động lên thang.

Lực ma sát là $f _ { \mathrm { s } } = \mu _ { \mathrm { s } } \textrm { n }$ .

Chọn O làm trục quay.

Áp dụng các phương trình của 2 điều kiện cân bằng.

Giải các phương trình.

# Public_137 

Trước năm 1687, số liệu về chuyển động của Mặt Trăng và các hành tinh đã được thu thập rất nhiều. Tuy nhiên, những chuyển động này là do loại lực nào gây ra thì vẫn là một bí ẩn. Ngay chính năm đó, Isaac Newton đã đưa ra chìa khóa cho vấn đề này.

Từ định luật I của mình, ông biết rằng có đang có một lực tổng hợp nào đó đang tác động lên Mặt Trăng vì nếu không có thì Mặt Trăng đã chuyển động với quỹ đạo thẳng chứ không phải tròn như hiện tại. Newton chỉ ra rằng chính trọng lực của Trái Đất đã tác động lên Mặt Trăng. Ông nhận ra rằng lực hút giữa Trái Đất và Mặt Trăng, giữa Mặt Trời và các hành tinh thực ra chính là trường hợp đặc biệt của lực hút giữa các vật. Nói một cách khác, lực hút làm Mặt Trăng quay quanh Trái Đất, cũng chính là lực làm làm quả táo rơi từ trên cây.

Trong chương này, chúng ta sẽ học về Định luật vạn vật hấp dẫn. Định luật này sẽ được kiểm chứng bởi các số liệu quan sát thiên văn học. Chúng ta cũng chỉ ra rằng các định luật về chuyển động của các hành tinh được trình bày bởi Johannes Kepler cũng suy ra được nhờ định luật vạn vật hấp dẫn và định luật bảo toàn moment động lượng.



### Trọng lực

Trọng lực là trường hợp riêng của lực hấp dẫn do Trái Đất tác dụng lên một vật. Độ lớn của trọng lực là:

$$
\begin{array} { r } { P = G \frac { M _ { E } m } { ( R _ { E } + h ) ^ { 2 } } } \end{array}
$$

Với:

• m: khối lượng của vật   
P: là trọng lực của Trái Đất tác dụng lên vật có khối lượng m   
• ME: khối lượng Trái Đất   
RE: bán kính của Trái Đất   
• G: hằng số hấp dẫn

### Gia tốc trọng trường

Theo định luật II Newton, trọng lực $\mathrm { P }$ do Trái đất tác dụng lên vật m sẽ làm vật m có gia tốc là g:

$$
P = m g
$$

Mặt khác theo công thức (13.2), ta có: $\begin{array} { r } { P = G \frac { M _ { E } m } { ( R _ { E } + h ) ^ { 2 } } } \end{array}$ . Từ công thức (13.2) và (13.3) suy ra:

$$
\begin{array} { r } { g = G \frac { M _ { E } } { ( R _ { E } + h ) ^ { 2 } } } \end{array}
$$

g: được gọi là gia tốc trọng trường.

# Trường hấp dẫn – Trọng trường

Định luật vạn vật hấp dẫn xem như một thành công lớn nữa của Newton vì nó giúp giải thích quy luật chuyển động của các hành tinh. Đồng thời, phạm vi ứng dụng của các định luật khác của ông cũng được mở rộng ra áp dụng cho các vật thể có kích thước và khối lượng lớn như các hành tinh trong vũ trụ. Từ năm 1687, lý thuyết của Newton đã được ứng dụng vào giải thích chuyển động của sao chổi, thí nghiệm Cavendish, quỹ đạo của Sao đôi, và sự quay của các thiên hà. Tuy nhiên, cả Newton và những người cùng thời với ông đều không thể nào lý giải được tại sao hai vật ở xa mà có thể tương tác được với nhau. Mãi sau khi ông mất thì khái

niệm về một trườn g hấp dẫn xung quan h các vật có



Riêng đối với Trái Đất, trường hấp dẫn của nó được gọi là trọng trường. Với giả thiết Trái đất là quả cầu đồng nhất thì vecto cường độ của trường hấp dẫn $\vec { \bf g } { \bf  } { \bf c } \vec { \bf o }$ công thức là:

$$
g \mathrm {  } = { \LARGE \sum _ { m } } ^ { F _ { g }  } = - { \LARGE \sum _ { r ^ { 2 } } } ^ { G M _ { E } } r \mathrm {  }
$$

$\vec { F ^ { \prime \prime } g } ^ {  } \vert \dot { \mathrm { a } }$ trọng lực tác dụng lên chất điểm có khối lượng mng số hấp dẫn $\mathbf { M } _ { \mathrm { E } }$ là khối lượng của Trái Đất • r: là khoảng cách từ tâm Trái Đất đến điểm mà ta đang khảo sát • $r \to \mathrm { { l } \dot { a } }$ vectơ đơn vị hướng từ tâm Trái Đất đến điểm khảo sát.

Đối với các điểm ở gần mặt đất thì giá trị $\mathbf { r } \approx \mathrm { R e }$ , khi đó $\vec { \pmb { g } } \mathrm {  c } \acute { 0 }$ độ lớn là g ≈ 9,8 m/s2.

# Các định luật Kepler và chuyển động của các hành tinh

Từ hàng ngàn năm trước, con người đã bắt đầu quan sát chuyển động của các hành tinh và các ngôi sao và cho rằng Trái Đất là trung tâm vũ trụ. Đây là lý thuyết xuất phát từ nhà bác học người Hy Lạp Claudius Ptolemy (100 - 170). Lý thuyết này được chấp nhận trong suốt 1400 năm sau. Mãi cho đến năm 1543, nhà bác học người Ba Lan Nicolaus Copernicus (1473 – 1543) mới đưa ra một nhận định là Trái Đất và các hành tinh khác quay quanh Mặt Trời. Sau đó, vì khao khát muốn tìm ra quy luật sắp xếp của bầu trời, nhà bác học người Đan Mạch Tycho Brahe (1546 – 1601) đã miệt mài quan sát sự chuyển động của các hành tinh và 777 ngôi sao mà mắt thường có thể nhìn thấy. Nhờ dữ liệu này mà người trợ lý của Brahe – Johannes Kepler đã bỏ ra 16 năm trời để tìm ra mô hình toán học giải thích chuyển động của các hành tinh. Tuy nhiên, vì các dữ liệu này là do quan sát chuyển động $\dot { \mathbf { O } }$ tại Trái Đất nên gây ra rất nhiều khó khăn cho Kepler trong việc tính toán. Cuối cùng, Kepler cũng đã đưa ra được mô hình chính xác nhờ vào dữ liệu của Brahe về chuyển động của Sao Hỏa xung quanh Mặt Trời. Lý thuyết của Kepler về chuyển động của các hành tinh được tóm tắt trong ba định luật:

1. Tất cả các hành tinh chuyển động theo các quỹ đạo elip trong đó Mặt Trời là một tiêu điểm.   
2. Vecto bán kính kẻ từ Mặt Trời đến một hành tinh quét được những điện tích bằng nhau trong những khoảng thời gian bằng nhau.   
3. Bình phương chu kỳ quỹ đạo của một hành tinh tỷ lệ với lập phương bán trục lớn của quỹ đạo elip của hành tinh đó.

### Định luật I Kepler

“Tất cả các hành tinh chuyển động theo các quỹ đạo elip trong đó Mặt Trời là một tiêu điểm.”



Các mô hình về hệ mặt trời lúc bấy giờ đều cho rằng quỹ đạo của các thiên thể đều là tròn. Tuy nhiên, theo định luật I Kepler, quỹ đạo tròn chỉ là một trường hợp đặc biệt, quỹ đạo elip mới là trường hợp tổng quát. Khám phá này của Kepler đã gặp rất nhiều thách thức vì



phần lớn các nhà khoa học thời đó đều tin rằng quỹ đạo của các hành tinh có hình tròn hoàn hảo.

Như ta đã biết, $\mathrm { m } \hat { \mathrm { 0 t } }$ elip (hình 13.2) sẽ được đặc trưng bởi:

• Bán kính trục lớn (a), kính trục nhỏ (b), bán tiêu cự (c), với:

$$
a ^ { 2 } = b ^ { 2 } + c ^ { 2 }
$$

• Độ lệch tâm: $e = { } ^ { c } / _ { a }$ . Độ lệch tâm là tham số có giá trị từ 0 (đường tròn) đến nhỏ hơn 1 (khi độ lệch tâm tiến tới 1, elip tiến tới dạng parabol).

![](images/image1.jpg)  
Hình 13.2: Dạng hình học quỹ đạo elip của các hành tinh

Độ lệch tâm quỹ đạo mà Kepler tính được cho Trái Đất là 0,017 vì vậy quỹ đạo của nó gần như là hình tròn. Đối với hành tinh có độ lệch tâm lớn nhất là Sao Thủy thì độ lệch tâm quỹ đạo của nó cũng chỉ là 0,21. Với các giá trị độ lệch tâm của các hành tinh thì quỹ đạo elip của các hành tinh rất khó phân biệt so với hình tròn. Chính vì lý do này mà các nghiên cứu của Kepler được đánh giá rất cao. Kể cả quỹ đạo elip của sao chổi Haley cũng được tính toán dựa trên định luật Kepler với độ lệch tâm là 0,97. Với bán kính trục lớn rất dài so với bán kính trục nhỏ, sao chổi Haley phải mất đến 76 năm mới chuyển động hết một vòng xung quanh Mặt Trời.



![](images/image2.jpg)  
Hình 13.3: Quỹ đạo của sao Thủy (hình a) và quỹ đạo của sao chổi Haley (hình b)



Định luật I Kepler là kết quả trực tiếp của tính chất tỷ lệ nghịch với bình phương khoảng cách của lực hấp dẫn. Dưới tác dụng của lực hấp dẫn gây ra bởi Mặt trời, các thiên thể có thể chuyển động theo các quỹ đạo hình elip (các hành tinh, tiểu hành tinh, sao chổi) hoặc parabol hoặc hyperbol (thiên thạch).

### Định luật II Kepler

“Vecto bán kính kẻ từ Mặt Trời đến một hành tinh quét được những điện tích bằng nhau trong những khoảng thời gian bằng nhau.”

![](images/image3.jpg)

Diện tích dA quét bởi vectơ bán kính nối từ Mặt Trời đến hành tinh $( r {  } )$ trong thời gian dt bằng nửa diện tích của hình bình hành.

Hình 13.4: - hình a: tác dụng lực hút của Mặt Trời lên hành tinh

- hình b: trong thời gian dt, hình bình hành được tạo nên bởi 2 vectơ bán kính $r {  }$ (với gốc tọa độ đặt ở Mặt Trời) và ?? ??→ = ??→ ???? (13.8)



Moment của lực hấp dẫn mà Mặt Trời tác dụng lên hành tinh đối với trục qua Mặt trời bằng không nên moment động lượng của hành tinh đối với trục qua Mặt trời được bảo toàn:



$$
U = - \begin{array} { c } { { G M _ { E } m } } \\ { { r } } \end{array}
$$

Công thức (13.21) trên chỉ đúng cho những vật nằm trên và bên ngoài bề mặt Trái Đất, tức $\mathbf { r } \geq \mathrm { R e }$ . Với gốc thế năng đã chọn $( \infty )$ thì thế năng trọng trường sẽ luôn có giá trị âm.

Ta có thể phát triển công thức (13.21) lên thành thế năng hấp dẫn tổng quát hơn của hệ hai chất điểm cách nhau một khoảng r và có khối lượng lần lượt là $\mathbf { m } _ { 1 }$ và $\mathbf { m } _ { 2 }$ như sau:

$$
U = - \frac { G m _ { \perp } m _ { 2 } } { r }
$$

Đối với hệ có ba chất điểm thì tổng thế năng hấp dẫn của cả hệ sẽ bằng:

$$
\begin{array} { r } { U _ { _ { t o t a l } } = U _ { _ { 1 2 } } + U _ { _ { 1 3 } } + U _ { _ { 2 3 } } = - G ( \frac { m _ { 1 } m _ { 2 } } { r _ { 1 2 } } + \frac { m _ { 1 } m _ { 3 } } { r _ { 1 3 } } + \frac { m _ { 2 } m _ { 3 } } { r _ { 2 3 } } ) } \end{array}
$$

Thế năng này có giá trị đúng bằng công cần thiết để tách các chất điểm của hệ ra xa nhau vô cùng.

# Năng lượng của các hành tinh và các vệ tinh

Cho hệ gồm một vật có khối lượng m chuyển động với vật tốc ν trong trường hấp dẫn của vật có khối lượng M với $ { \mathbf { M } } > >  { \mathbf { m } }$ . Hệ này có thể là mô hình cho một hành tinh chuyển động xung quanh Mặt Trời, một vệ tinh chuyển động xung quanh Trái Đất hoặc một sao chổi chuyển động ngang qua Mặt Trời. Nếu vật M được gắn cố định trong một hệ quy chiếu quán tính thì tổng cơ năng E của hệ 2 vật sẽ chỉ là cơ năng của vật m. Cơ năng này bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ động năng K và thế năng hấp dẫn U của vật m (hay thế năng của hệ hai vật):

$$
E = K + U
$$

$$
\begin{array} { r } { E = { \frac { 1 } { 2 } } m \nu ^ { 2 } - G { \frac { M m } { r } } } \end{array}
$$

Công thức 13.25 cho thấy cơ năng E của vật có khả năng mang các giá trị dương, âm hoặc bằng không phụ thuộc vào độ lớn vận tốc ν. Đối với các hệ liên kết như Mặt Trời-Trái Đất, Mặt Trăng – Trái Đất hoặc vệ tinh của Trái Đất thì cơ năng của vật sẽ có giá trị âm. Ta có thể dễ dàng kiểm chứng điều này qua chuyển động của một hành tinh có quỹ đạo được xem như tròn bất kỳ:

$$
F _ { g } = m a  \frac { G M m } { r ^ { 2 } } = \frac { m \nu ^ { 2 } } r
$$



Nếu chia hai vế của đẳng thức trên cho 2 ta sẽ được:

$$
{ \frac { m v ^ { 2 } } { 2 } } = { \frac { G M m } { 2 r } }
$$

Áp dụng công thức (13.26) vào công thức (13.25) ta được:

$$
E = { \frac { G M m } { 2 r } } - { \frac { G M m } { r } }
$$



$$
\begin{array} { r } { E = - \frac { G M m } { 2 r } \left( \mathrm { q u } \tilde { \mathrm { y } } \mathrm { d a o t r o n } \right) } \end{array}
$$

Trong quỹ đạo tròn, động năng của một vật có giá trị dương sẽ bằng $\%$ độ lớn của thế năng hấp dẫn. Vì vậy, cơ năng của vật sẽ có giá trị âm. Đây chính là năng lượng liên kết của hệ, tức năng lượng tối thiểu cần để tách riêng hai vật ra khỏi nhau xa vô cùng.

Đối với quỹ đạo elip, công thức của cơ năng sẽ giống (13.27) nhưng ta chỉ cần thay bán kính r của quỹ đạo tròn bằng bán kính trục lớn a trong quỹ đạo elip, tức là:

$$
\begin{array} { r } { E = - \frac { G M m } { 2 a } \left( { \tt q u \tilde { y } d a o e l i p } \right) } \end{array}
$$

Nếu hệ cô lập thì cơ năng này sẽ có giá trị không đổi. Vì vậy, khi vật m chuyển động từ vị trí 1 (r1) đến vị trí 2 (r2) thì cơ năng sẽ được bảo toàn:

$$
\begin{array} { r } { E = { \frac { 1 } { 2 } } m v _ { i } ^ { 2 } - G { \frac { M m } { r _ { i } } } = { \frac { 1 } { 2 } } m v _ { j } ^ { 2 } - G { \frac { M m } { r _ { j } } } } \end{array}
$$

# Câu hỏi lý thuyết chương 13

1. Sắp xếp các đại lượng năng lượng sau từ lớn nhất đến nhỏ nhất. Nếu có bằng nhau thì minh họa dấu bằng.

(a) giá trị tuyệt đối của thế năng trung bình của hệ Mặt trời – Trái đất.   
(b) động năng trung bình của Trái Đất khi chuyển động quanh Mặt trời.   
(c) giá trị tuyệt đối của tổng năng lượng của hệ Mặt trời – Trái đất.

2. Giả sử gia tốc hấp dẫn ở bề mặt của một mặt trăng A của sao Mộc là 2m/s2. Mặt trăng B có khối lượng gấp đôi và bán kính gấp đôi của mặt trăng A. Gia tốc hấp dẫn ở bề mặt của nó bằng bao nhiêu? Bỏ qua gia tốc hấp dẫn gây bởi sao Mộc.

(a) (a) $8 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ (b) (b) $4 \mathrm { m } / \mathrm { s } ^ { 2 }$ (c) (c) $2 { \mathrm { m } } / { \mathrm { s } } ^ { 2 }$ (d) (d) $1 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ (e) (e) $0 . 5 \mathrm { m } / \mathrm { s } ^ { 2 }$

3. Một vệ tinh ban đầu di chuyển theo quỹ đạo tròn với bán kính R quanh Trái đất. Giả sử nó được chuyển vào quỹ đạo tròn có bán kính 4R.

(i) Lực tác động lên vệ tinh như thế nào?   
(a) lớn gấp tám lần   
(b) lớn gấp bốn lần (c) lớn gấp 1/2 lần   
(d) lớn gấp 1/8 lần   
(e) lớn gấp 1/16 lần   
(ii) Điều gì xảy ra với tốc độ của vệ tinh? Chọn từ các khả năng tương tự (a) đến (e).





(iii) Điều gì xảy ra với chu kỳ của nó? Chọn từ các khả năng tương tự (a) đến (e).

4. $\mathrm { X } \dot { \hat { \mathrm { e } } } \mathrm { p }$ hạng độ lớn của các lực hấp dẫn sau từ lớn nhất đến nhỏ nhất. Nếu hai lực bằng nhau, minh họa dấu bằng.

(a) lực tác dụng bởi vật nặng $2 \mathrm { k g }$ lên vật nặng $3 \mathrm { k g }$ cách nhau $1 \textrm { m }$ .   
(b) lực tác động bởi vật nặng $2 \mathrm { k g }$ lên vật thể $9 \mathrm { k g }$ cách nhau $1 \textrm { m }$ .   
(c) lực tác dụng bởi vật nặng $2 \mathrm { k g }$ lên vật thể $9 \mathrm { k g }$ cách nhau $2 \mathrm { m }$ .   
(d) lực tác dụng bởi vật thể $9 \mathrm { k g }$ lên vật thể $2 \mathrm { k g }$ cách nhau $2 \mathrm { m }$ .   
(e) lực tác dụng bởi vật thể $4 \mathrm { k g }$ lên vật thể $4 \mathrm { k g }$ khác cách đó 2 m.

5. Lực hấp dẫn tác dụng lên một phi hành gia tại bề mặt Trái Đất là 650 N. Khi cô ấy đang ở trong trạm không gian quay quanh Trái Đất thì lực hấp dẫn tác dụng lên cô ấy:

(a) lớn hơn 650N,   
(b) chính xác bằng 650N,   
(c) nhỏ hơn 650N,   
(d) gần nhưng không chính xác bằng không, hoặc   
(e) chính xác bằng không?

# Bài tập chương 13

1. Ba quả cầu đồng nhất có khối lượng $ { \mathbf { m } } _ { 1 } = 2 , 0 0  { \mathrm { k g } }$ , $\mathbf { m } _ { 2 } ~ =$ $4 { , } 0 0 ~ \mathrm { k g }$ và $\mathrm { m } _ { 3 } = 6 { , } 0 0 \ \mathrm { k g }$ được đặt $\dot { \mathbf { O } }$ các vị trí như trong hình. Tính lực hấp dẫn tác dụng lên quả cầu $\mathbf { m } 2$ do hai quả cầu còn lại gây ra.

ĐS: $\Vec { F } = - 1 0 . 0 \hat { i } + 5 . 9 3 \hat { j } \times 1 0 ^ { - 1 1 } N$

2. Hai vật hút lẫn nhau với lực hấp dẫn có độ lớn $1 \times 1 0 ^ { - 8 } \mathrm { N }$ khi cách nhau 20,0 cm. Nếu tổng khối lượng của hai vật thể là $5 . 0 0 \mathrm { k g } \quad$ , tính khối lượng của mỗi vật?

![](images/image4.jpg)

3. Gia tốc rơi tự do trên bề mặt Mặt trăng là khoảng 1/6 gia tốc rơi tự do trên bề mặt Trái đất. Bán kính của Mặt trăng là khoảng $\mathrm { ~ \ i ~ { ~ 0 , 2 5 0 ~ } } R _ { E }$ $( R _ { E } = 6 , 3 7 \times 1 0 ^ { 6 } \mathrm { m }$ , $R _ { E }$ : bán kính Trái Đất). Tìm tỷ số khối lượng riêng của chúng, $\begin{array} { r } { \rho _ { M \Breve { \mathbf { a } } { t } } \mathrm { t r } \Breve { \mathbf { a } } \mathrm { n } \underline { { q } } } \\ { \rho _ { T r \Breve { \mathbf { a } } { i } } \mathrm { d } \tilde { \mathbf { a } } \mathrm { t } } \end{array}$ .

ĐS: $\rho _ { M } / \rho _ { E } = 2 / 3$

4. (a) Xác định vecto cường độ trường hấp dẫn $g $ tại P do hai quả

![](images/image5.jpg)



cầu gây ra như trong hình.

(b) Chứng minh rằng, vecto cường độ trường hấp dẫn $g $ tại P bằng $0 \mathrm { k h i r } {  } 0$ .



(c) Chứng minh rằng, vecto cường độ trường hấp dẫn $g $ tại P bằng 2GM/r2 khi ?? → ∞.

ĐS: (a) về phía khối tâm.

5. Ba quả cầu giống nhau đặt tại 3 đỉnh của hình vuông cạnh l như hình bên. Xác định vecto cường $\mathtt { d } \hat { \mathbf { \rho } }$ trường hấp dẫn $g $ tại O.

ĐS: $\scriptstyle { { \vec { g } } = { \frac { G m } { I ^ { 2 } } } \left( { \sqrt { 2 } } + { \frac { 1 } { 2 } } \right) }$ về phía góc đối diện.

![](images/image6.jpg)

6. Io, một vệ tinh của sao Mộc, có chu kỳ quỹ đạo 1,77 ngày, và bán kính quỹ đạo là $4 , 2 2 \times 1 0 ^ { 5 } \mathrm { k m }$ . Từ những dữ liệu này, xác định khối lượng của sao Mộc.

ĐS: $M _ { J } = 1 . 9 0 { \times } 1 0 ^ { 2 7 } k g$ (khoảng 316 lần khối lượng Trái Đất).

7. $\mathrm { H } \hat { \mathbf { e } }$ sao đôi của Plaskett bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ hai ngôi sao quay trên một quỹ đạo tròn có tâm là trung điểm của đoạn nối hai ngôi sao, xem như khối lượng của hai sao là bằng nhau. Giả sử tốc độ quỹ đạo của mỗi ngôi sao $\operatorname { l } \dot { \mathrm { a } } | v \rrangle | = 2 2 0 k m / s$ và chu kỳ quỹ đạo là 14,4 ngày. Tìm khối lượng M của mỗi ngôi sao so với khối lượng của mặt trời. (Biết khối lượng Mặt trời: $1 , 9 9 \times 1 0 ^ { 3 0 } k g )$ .

![](images/image7.jpg)

ĐS: $M = 1 . 2 6 { \times } 1 0 ^ { 3 2 } k g = 6 3 . 3$ khối lượng mặt trời.

8. Các ngôi sao neutron là những vật thể có khối lượng riêng cực kỳ lớn, hình thành từ những tàn dư của vụ nổ siêu tân tinh (supernova). Chúng quay rất nhanh. Giả sử khối lượng của một ngôi sao neutron hình cầu gấp đôi khối lượng Mặt trời, bán kính $1 0 { , } 0 \mathrm { k m }$ . Xác định tốc độ góc lớn nhất mà nó có thể có để cho vật chất tại bề mặt của sao trên đường xích đạo của nó chỉ được giữ trong quỹ đạo bởi lực hấp dẫn.

ĐS: w 1.63 104 rad s

9. Một vệ tinh trong quỹ đạo Trái Đất có khối lượng là 100 kg và ở độ cao $2 \times 1 0 ^ { 6 } m$ .

(a) Tính thế năng của hệ thống vệ tinh - Trái Đất? (b) Tính độ lớn của lực hấp dẫn do Trái đất tác dụng lên vệ tinh? (c) Có những lực nào do vệ tinh tác dụng lại trái đất?



ĐS: a) b) F

10. Sau khi Mặt trời sử dụng hết nhiên liệu hạt nhân của nó và Mặt trời sẽ trở thành sao lùn trắng. Khối lượng của sao lùn trắng này bằng khoảng một nửa khối lượng của Mặt trời, vật chất của nó được nén trong một thể tích hình cầu tương đối khiêm tốn, cỡ chỉ bằng kích thước trái đất, do đó vật chất của nó cực kỳ đặc. Tính:

(a) Mật độ trung bình của sao lùn trắng,



(b) Gia tốc rơi tự do và thế năng của một vật có khối lượng $1 . 0 0 \mathrm { k g } \dot { \sigma } ^ { 1 }$ bề mặt của sao lùn trắng.

$$
\rho = 1 . 8 4 \times 1 0 ^ { 9 } \frac { k g } { m ^ { 3 } } { \sf b } ) \ g = 3 . 2 7 \times 1 0 ^ { 6 } \frac { m } { s ^ { 2 } }
$$

11. Một vệ tinh $5 0 0 \mathrm { k g }$ nằm trong quỹ đạo tròn ở độ cao $5 0 0 \mathrm { k m }$ so với bề mặt Trái đất. Do ma sát không khí, vệ tinh cuối cùng rơi xuống bề mặt Trái Đất và chạm đất với tốc độ $2 { , } 0 0 \ \mathrm { k m / s }$ . Tính phần năng lượng đã được chuyển thành nội năng do ma sát với không khí.

ĐS: $\Delta E = 1 . 5 8 { \times } 1 0 ^ { 1 0 } J$

12. Một vệ tinh $1 . 0 0 0 \mathrm { k g }$ quay quanh Trái đất ở độ cao không đổi $1 0 0 \mathrm { k m } . $

(a) Tính năng lượng phải thêm vào hệ (vệ tinh – trái đất) để di chuyển vệ tinh này vào một quỹ đạo tròn với độ cao $2 0 0 \mathrm { k m ? }$   
(b) Động năng và thế năng trong hệ thay đổi như thế nào?

ĐS: (a) $\Delta E = 4 6 9 M J$

13. Một vệ tinh có khối lượng 200 kg ở độ cao $2 0 0 \mathrm { k m }$ so với bề mặtTrái Đất.

(a) Giả sử quỹ đạo là tròn, vệ tinh mất bao lâu để hoàn thành một vòng quỹ đạo?

(b) Tính tốc độ của vệ tinh?

(c) $\mathrm { V } \hat { \mathbf { e } }$ tinh xuất phát từ bề mặt trái đất, tính năng lượng tối thiểu cần thiết cung cấp cho vệ tinh này ? Bỏ qua sức cản không khí nhưng tính đến sự quay của Trái Đất quanh trục của nó.

ĐS: (a) $T = 1 . 4 7 h$ (b) $\nu = 7 . 7 9 \frac { k m } { s }$ (c) $E _ { \mathrm { m i n } } = 6 . 4 3 { \times } 1 0 ^ { 9 } J$

14. Một vệ tinh nằm trong quỹ đạo tròn quanh Trái đất ở độ cao $2 , 8 0 . 1 0 ^ { 6 } \mathrm { m }$ . Tìm:

(a) Chu kỳ quay.   
(b) Tốc độ và gia tốc của vệ tinh.

ĐS: (a) T (b) v 6.60 km ; s $a = 4 . 7 4 \frac { m } { s ^ { 2 } }$ về phía trái đất.

# Public_138 

Vật chất thông thường tồn tại $\acute { \mathbf { O } }$ ba trạng thái: rắn, lỏng, khí. Chúng ta biết rằng, ở trạng thái rắn vật chất sẽ có thể tích và hình dạng xác định, ở trạng thái lỏng thì chúng chỉ có thể tích xác định còn ở trạng thái khí thì ngay cả thể tích và hình dạng đều không xác định. Những mô tả trên chỉ cho chúng ta bức tranh cơ bản về các trạng thái tồn tại của vật chất nhưng nó không hoàn toàn chính xác. Ví dụ như nhựa đường (asphalt) và chất dẽo (plastics) thường được xem là những chất rắn nhưng sau một khoảng thời gian nó lại có xu hướng chảy như chất lỏng. Ngoài ra, trạng thái rắn, lỏng, khí của một vật chất phụ thuộc rất nhiều vào nhiệt độ và áp suất. Nói tóm lại, theo thời gian một vật chất nào đó sẽ thay đổi trạng thái rắn, lỏng, khí của nó tùy thuộc vào điều kiện bên ngoài.

Chất lưu là một hệ, gồm các phân tử sắp xếp một cách ngẫu nhiên, tương tác với nhau bằng một lực liên kết yếu và định hình được nhờ vào lực tác dụng của thành bình. Cả chất lỏng và chất khí đều là chất lưu.

Trong cơ học chất lưu, chúng ta áp dụng các định luật đã biết để nghiên cứu chất lưu ở trạng thái tĩnh và trạng thái động của chúng.

# Áp suất

Chất lưu không tác dụng lực căng hay lực kéo lên một vật, ở trạng thái tĩnh nó chỉ có một xu hướng là nén lên mọi mặt của một vật bất kỳ đặt trong nó. (Hình 14.1)

Áp suất của chất lưu có thể được đo bằng một dụng cụ rất đơn giản. Dụng cụ đo áp suất được cấu tạo bằng một xi-lanh rỗng được hút chân không nối với một pittông nhẹ bằng một lò xo. Ta có thể thấy cấu tạo của nó ở Hình 14.2.

Khi nhúng dụng cụ đo áp suất này vào chất lưu cần khảo sát thì chất lưu sẽ nén một lực F lên mặt bên ngoài của pittông. Lò xo bên dưới cũng sẽ bị nén theo cho đến khi lực nén

![](images/image1.jpg)  
Hình 14.1: Lực nén của chất lưu lên một vật đặt trong nó

F của chất lưu cân bằng với lực đàn hồi của lò xo. Đo độ lớn của lực đàn hồi thì ta sẽ biết giá trị của lực nén F. Áp suất P của chất lưu khi đó chính là tỉ số giữa lực nén F và diện tích A của pittông. Tổng quát, áp suất của chất lưu chính là lực nén của chất lưu đó lên một đơn vị diện tích của bề mặt vật khác đặt trong nó. Công thức tính áp suất khi đó là:

$$
P = { \frac { F } { A } }
$$



Nếu áp suất thay đổi trên toàn bề mặt của vật bị nén thì khi đó áp suất tại vi trí của diện tích nhỏ dA sẽ là:

$$
\begin{array} { r } { P = \frac { d F } { d A }  d F = P d A } \end{array}
$$

Vì vậy, lực tác dụng của chất lưu lên toàn diện tích bề mặt A của vật là:

![](images/image2.jpg)  
Hình 14.2: Dụng cụ đo áp suất chất lưu

$$
\textstyle F = \int d F = \int P d A
$$

Đơn vị đó áp suất trong hệ SI là $\textstyle ( \mathrm { N } / \mathrm { m } ^ { 2 } )$ hay pascal $\mathrm { ( P a ) }$ :

$$
1 \mathrm { P a } = 1 \mathrm { N } / \mathrm { m } ^ { 2 }
$$



Mỗi bên của phương trình này là công của lực tác động lên piston tương ứng. Do đó, công của lực $\mathrm { F } _ { 1 }$ trên piston đầu vào bằng công của lực $\mathrm { F } _ { 2 }$ trên piston đầu ra, vì nó phải bảo tồn năng lượng.

Các ứng dụng khác của định luật Pascal: phanh thủy lực, nâng xe hơi, đòn bẩy thủy lực, xe nâng hàng.

# Phương pháp đo áp suất khí quyển

Áp suất khí quyển là một thông số quan trọng luôn được đề cập đến trong các chương trình dự báo thời tiết. Giá trị của áp suất khí quyển này thay đổi theo từng vùng, từng thời điểm chứ không phải là giá trị áp suất khí quyển chuẩn $\mathrm { P _ { o } }$ không đổi mà ta đã đề cập ở mục 14.2. Vậy, áp suất khí quyển này được đo như nào?

# Khí áp kế Torricelli

Một trong những khí áp kế phổ biến đã được chế tạo bởi nhà bác học Evangelista Torricelli (1608–1647). Áp kế này gồm một ống thủy tinh dài chứa đầy thủy ngân, được úp ngược vào một chậu cũng chứa thủy ngân (hình 14.5). Khi đó, áp suất tại mặt trên của cột thủy ngân trong ống là $\boldsymbol { \mathrm { P } } = \boldsymbol { 0 }$ .

Áp suất tại điểm B và điểm A trong thủy ngân là như nhau và bằng áp suất khí quyển. Nếu ta đặt áp $\mathrm { k } \acute { \mathrm { e } }$ này trong điều kiện chuẩn thì áp suất tại A và B chính là áp suất khí quyển $\mathrm { { { P } _ { 0 } } }$ . Vì cột thủy ngân trong ống được cân bằng nên lực nén do áp suất thủy ngân và trọng lực của cột thủy ngân tại điểm A sẽ cân bằng nhau, tức:

![](images/image3.jpg)  
Hình 14.5: Áp kế khí thủy ngân

$$
P _ { o } = \rho _ { H g } g h
$$

$$
\begin{array} { r } { \stackrel { \triangledown } { \boldsymbol { \Psi } } _ { h } = \frac { \boldsymbol { P } _ { o } } { \rho _ { H g } g } } \end{array}
$$



![](images/image4.jpg)  
Hình 14.6: Áp kế khí chữ U

Để đo áp suất khí P của khí trong bình ta đổ vào ống chữ U một chất lỏng và để hở trong không khí. Khi đó áp suất tại A và B là bằng nhau và bằng áp suất P của chất khí trong bình. Áp dụng công thức 14.6 ta có được: $P = P _ { o } + \rho g h$

Khi đó:

• $P$ là áp suất tuyệt đối của chất khí.   
• $P - P _ { o } = \rho g h$ : được gọi là áp suất tương đối của chất khí trong bình so với khí quyển.

Thông thường nếu không cần biết giá trị thực của áp suất thì người ta thường đo áp suất tương đối của chất khí đó bằng cách đo độ cao chênh lệch h của chất lỏng. Ví dụ, áp suất khí ta đo được trong lốp xe chính là áp suất tương đối.

# Động lực học chất lưu

Ở các nội dung trước, ta đã khảo sát chất lưu ở trạng thái tĩnh. Trong đề mục này ta sẽ khảo sát chất lưu ở trạng thái chuyển động. Khi một chất lưu chuyển động thì chuyển động của nó sẽ thuộc một trong hai loại: chuyển động thành dòng (lớp) (hình 14.7) hay chuyển động rối (hình 14.8).

Trong chuyển động của chất lưu ta sẽ gặp khái niệm độ nhớt. Độ nhớt chính là đại lượng đặc trưng cho mức độ ma sát giữa các lớp chất lưu lên nhau khi chúng chuyển động. Vì chuyển động thực tế của chất lưu rất phức tạp nên trước tiên chúng ta sẽ khảo sát chuyển động của chất lưu lý tưởng với các điều kiện như sau:



![](images/image5.jpg)

Hình 14.7: Chuyển động thành lớp của chất khí khi xe chuyển động trong hầm

![](images/image6.jpg)  
Hình 14.8: Khói thuốc chuyển động trong sự chảy thành dòng ở phía dưới và trong sự chảy rối ở phía trên.

1. Trong chất lưu lý tưởng thì ma sát giữa các lớp chất lưu khi chuyển động được bỏ qua.   
2. Chất lưu lý tưởng sẽ chuyển động thành dòng. Ở chế độ chuyển động này, mọi hạt   
chất lưu qua một điểm sẽ có cùng vận tốc.   
3. Mật độ khối lượng của chất lưu là không thay đổi, hay chất lưu là không chịu nén.   
4. Chất lưu không có chuyển động xoáy.

Đường dòng là đường cong sao cho tiếp tuyến với nó tại mỗi điểm trùng với vectơ của phân tử chất lưu tại điểm đó (hình 14.9).

![](images/image7.jpg)  
Hình 14.9: Hình ảnh đường dòng của chất lưu

Một tập hợp các đường dòng tạo thành một ống dòng. Các hạt chất lưu không đi vào hay



đi ra một ống dòng.



Lưu lượng thể tích của chất lưu qua một tiết diện là đại lượng đo bằng thể tích chất lưu qua tiết diện đó trong một đơn vị thời gian. Với tiết diện có diện tích A và vuông góc với vận tốc $v $ của chất lưu (giả định vận tốc $v $ của chất lưu là như nhau tại mọi điểm thuộc tiết diện đang xét) thì lưu lượng qua tiết diện này bằng: Aν. Đơn vị của lưu lượng thể tích trong hệ SI $\mathrm { l } \dot { \mathrm { a } } \frac { \overline { { 3 } } } { s } .$

Chất lưu lý tưởng khi chuyển động sẽ tuân theo phương trình liên tục: lưu lượng thể tích chất lưu qua mọi tiết diện vuông góc với ống dòng khác nhau trong cùng một ống dòng của chất lưu đều bằng nhau, tức là:

$$
A _ { 1 } \nu _ { 1 } = A _ { 2 } \nu _ { 2 } = . . . = A _ { \mathrm { i } } \nu _ { \mathrm { i } } = { \mathrm { c o n s t } }
$$

Với $A _ { 1 } , A _ { 2 } , . . . , A _ { \mathrm { i } }$ lần lượt là diện tích của mặt cắt 1, 2, …, thứ i trong cùng một ống dòng, còn $\nu _ { 1 }$ , ν2, …, $\nu _ { 1 }$ lần lượt là vận tốc của chất lưu tại mặt cắt 1, 2, …, thứ i trong cùng một ống dòng.

# Phương trình Bernoulli

Cho chất lưu lý tưởng chuyển động trong một ống dòng như hình 14.10.

Áp suất tại mỗi điểm của chất lưu lý tưởng sẽ tuân theo phương trình Bernoulli:

$$
P + \frac { 1 } { 2 } \rho \nu ^ { 2 } + \rho g y = c o n s t a n t
$$

Với:

• y là độ cao của tiết diện đó

• P là áp suất chất lưu tại một điểm bất kỳ trong dòng chảy.

• ρ là mật độ khối lượng của chất lưu

• ν là vận tốc dòng chảy tại tiết điện đó.

![](images/image8.jpg)  
Hình 14.10: Dòng chảy của chất lưu lý tưởng qua các tiết diện khác nhau



# Các ứng dụng của động lực học chất lưu

Lý thuyết động lực học chất lưu có thể giúp ta giải thích được các hiện tượng liên quan chuyển động của các vật thể trong chất lưu. Đầu tiên ta sẽ khảo sát dòng khí chuyển động qua cánh máy bay có hình ảnh các đường dòng như hình 14.11.

Giả sử dòng khí đang chuyển động theo phương ngang từ phải sang trái với vận tốc ??→1 . Khi gặp cánh máy bay, do độ nghiêng của cánh dòng chảy của chất khí bị bẻ cong lõm xuống với vận tốc ??→ 2 . Cánh máy bay đã tác dụng một lực lên dòng khí và theo định luật III Newton, dòng khí này cũng tác dụng ngược lại lên máy bay một lực $\pmb { F } ^ { \sharp }$ cùng độ lớn nhưng ngược chiều. Lực này được phân tích thành 2 thành phần là lực nâng và lực cản. Lực nâng tác dụng vào cánh máy bay sẽ phụ thuộc vào các yếu tố như: tốc độ của máy bay, diện tích của cánh, độ cong của cách máy bay và góc giữa cánh máy bay so với phương ngang. Độ cong của cánh máy bay phải được thiết kế sao nhằm làm cho áp suất khí $\dot { \mathbf { O } }$ phía trên cánh máy bay nhỏ hơn phía dưới tuân theo định luật Bernoulli. Chính sự chênh lệch áp suất này đã giúp nâng cánh máy bay lên. Khi góc chênh lệch giữa cánh máy bay và phương ngang tăng thì sẽ làm xuất hiện các dòng chảy xoáy làm giảm lực nâng.

Cánh máy bay đã bẻ cong các dòng chảy của chất khí đang chuyển động từ phải sang trái

![](images/image9.jpg)  
Hình 14.11: Dòng chảy của khí qua cánh máy bay

Một cách tổng quát, khi một vật thể chuyển động xuyên qua một chất lưu thì nó sẽ bẻ cong các dòng chảy làm sinh ra lực nâng tác dụng lên vật đó. Một vài yếu tố ảnh hưởng lên lực nâng này là: hình dạng của vật, sự định hướng của vật so với dòng chảy, chuyển động xoáy và kết cấu bề mặt của vật thể đó.

# Ví dụ về quả banh golf:

Quả banh được cung cấp một chuyển động quay lùi. Các chỗ trũng trên mặt banh làm tăng ma sát với không khí làm cho lực nâng tăng lên. Lực nâng do chuyển động xoáy của bóng tạo ra sẽ làm cho độ tăng tầm xa lớn hơn độ giảm tầm xa gây ra bởi lực ma sát trong chuyển động tịnh tiến của quả bóng.

![](images/image10.jpg)

# Ví dụ về máy phun:

![](images/image11.jpg)

Một dòng khí chạy qua phía trên của một ống hở hai đầu. Đầu còn lại của ống được nhúng vào một chất lỏng. Dòng khí chuyển động làm giảm áp suất phía trên ống. Chất lỏng dâng lên



đến dòng khí. Chất lỏng bị phân tán vào trong ống phun dưới dạng các hạt nhỏ.



# Câu hỏi lý thuyết chương 14

1. Khi một vật được nhúng trong một chất lỏng, tại sao tổng hợp lực tác dụng lên vật theo phương ngang bằng không?

2. Hai ly uống nước có bề dày mỏng và có diện tích đáy bằng nhau nhưng hình dạng khác nhau, với các mặt cắt ngang rất khác nhau ở mặt trên của hai ly, được đổ đầy với cùng một mực nước. Theo công thức $P = P _ { o } + \rho g h$ , áp suất là như nhau ở mặt dưới (hay đáy) của cả hai ly. Theo quan điểm này, tại sao khi người ta cân thì hai ly có trọng lượng khác nhau?

3. Một con cá nằm yên ở đáy cùng của một xô nước, trong khi xô đang được đặt trên một cái cân. Khi cá bắt đầu bơi xung quanh, kim của cân có thay đổi không? Giải thích.

4. Việc cấp nước cho một thành phố thường được cung cấp từ các hồ chứa được xây dựng ở nơi đất cao. Nước chảy từ hồ chứa, qua đường ống, và vào nhà của bạn. Tại sao khi bạn bật vòi nước ở tầng trệt của một tòa nhà thì nước chảy nhanh hơn so với khi bật vòi nước trong một căn hộ ở tầng cao hơn?

5. Một con tàu đậu trong hồ nội địa sẽ nổi cao hơn hay thấp hơn khi con tàu đậu trong đại dương? Tại sao?

# Bài tập chương 14

1. Một phụ nữ $^ { 5 0 , 0 \mathrm { k g } }$ mang giày cao gót được mời vào nhà trong đó nhà bếp lót bằng sàn vinyl. Đế gót có hình tròn và bán kính 0,500 cm.

(a) Nếu người phụ nữ đứng cân bằng trên một gót chân, tính áp lực cô ấy gây ra trên sàn? (b) Chủ nhà có quan tâm không? Giải thích câu trả lời của bạn.

$$
\mathrm { D S } \colon \mathrm { a } ) P = 6 . 2 4 \times 1 0 ^ { 6 } \frac { N } { m ^ { 2 } } \ .
$$

2. (a) Máy hút bụi rất mạnh có ống hút với đường kính 2,86 cm. Đầu cuối của ống hút đặt vuông góc trên mặt phẳng của một viên gạch, trọng lượng lớn nhất của viên gạch bằng bao nhiêu để người lau dọn có thể nâng nó lên?

(b) Chuyện gì sẽ xảy ra nếu bạch tuộc sử dụng một con vòi có đường kính 2,86 cm trên mỗi hai vỏ sò để kéo vỏ ra ngoài. Tìm lực lớn nhất bạch tuộc có thể gây ra trên một vỏ sò trong nước muối sâu $^ { 3 2 , 3 \mathrm { ~ m ~ } }$ .

ĐS: a) F b) $F = 2 7 5 N$

3. Piston nhỏ của máy nâng thủy lực có diện tích mặt cắt ngang $3 { , } 0 0 c m ^ { 2 }$ , và piston lớn có diện tích mặt cắt ngang là $2 0 0 \ c m ^ { 2 }$ . Cần phải áp lực nén $F _ { 1 }$ bằng bao nhiêu lên piston nhỏ để máy nâng nâng được tải trọng $F _ { g } = 1 5 k N ?$

![](images/image12.jpg)



ĐS: $F _ { 1 }$



4. $\mathrm { B } \mathring { \boldsymbol { \mathrm { e } } }$ chứa trong hình chứa đầy nước với chiều cao $\mathrm { d } = 2 { , } 0 0 \mathrm { m }$ . Mặt bên của bể chứa có một cửa $\mathrm { s } \dot { \hat { 0 } }$ hình chữ nhật (chiều cao $\mathrm { h } { = } 1 , 0 0 \mathrm { m }$ và chiều rộng $\mathrm { w } { = } 2 , 0 0 \mathrm { m }$ ) với bản $1 \dot { \hat { \mathrm { e } } }$ đặt ở phía trên của cửa sổ.

(a) Xác định độ lớn của lực mà nước tác động lên cửa sổ. (b) Tìm độ lớn của mô-men xoắn của lực mà nước tác động lên cửa sổ đối với bản lề.

ĐS: a) $F = 2 9 . 4 k N$ b) $\tau = 1 6 . 3 k N . m$ .

![](images/image13.jpg)

5. Piston 1 trong hình bên có đường kính 0.250 in ( $\mathrm { 1 i n } { = } 2 . 5 4 \mathrm { c m }$ ). Piston 2 có đường kính 1,50 in. Xác định độ lớn của lực F, cần thiết để đỡ được tải trọng 500 lb $\scriptstyle 1 1 6 = 0 . 4 5 3 5 9 2$ ) khi không có ma sát.

ĐS: $F = 2 . 3 1 l b$

6. Blaise Pascal làm một bản sao áp $\mathrm { k } \acute { \mathrm { e } }$ của Torricelli nhưng sử dụng rượu vang đỏ Bordeaux, mật độ khối lượng $9 8 4 ~ \mathrm { k g } / m ^ { 3 }$ thay thế cho thủy ngân.

(a) Chiều cao h của cột rượu đối với áp suất bình thường của khí quyển bằng bao nhiêu?   
(b) Chân không ở phía trên cột rượu có tốt như khi dùng thủy ngân không?   
ĐS: a) $h = 1 0 . 5 m$ .

![](images/image14.jpg)

7. Đổ thủy ngân vào ống chữ U. Nhánh trái của ống có diện tích ngang $A _ { 1 }$ là $1 0 { , } 0 \ c m ^ { 2 }$ nhánh phải có diện tích ngang $A _ { 2 }$ là $5 { , } 0 0 c m ^ { 2 }$ . Đổ 100gr nước vào nhánh phải như hình.

(a) Xác định chiều dài của cột nước $\dot { \mathbf { O } }$ nhánh phải của ống chữ U. (b) Với mật độ thủy ngân là $1 3 , 6 \mathrm { g } / c m ^ { 3 }$ , chiều dài của cột thủy ngân ở nhánh bên trái sẽ tăng thêm một đoạn h bằng bao nhiêu?

ĐS: a) $h { = } 2 0 . 0 c m$ b) $\Delta h { \stackrel { } { = } } 0 . 4 9 0 c m$



![](images/image15.jpg)



8. Khối kim loại nặng $1 0 { , } 0 \mathrm { k g }$ có kích thước 12,0 cm x 10,0 cmx 10,0 cm được treo vào lực $\mathrm { k } \acute { \mathrm { e } }$ và đươc nhúng vào nước. Chiều cao của khối kim loại là $1 2 { , } 0 \ \mathrm { c m }$ , và mặt trên của khối cách mặt nước $5 . 0 0 \mathrm { c m }$ .

(a) Tính độ lớn lực tác động lên mặt trên và mặt dưới của khối?   
(b) Đọc số chỉ lực kế?   
(c) Chứng minh rằng lực nâng bằng với độ chênh lệch của hai lực trên?

ĐS: a) $F _ { t o p } = 1 . 0 1 7 9 \times 1 0 ^ { 3 } N ; F _ { b o t } = 1 . 0 2 9 7 \times 1 0 ^ { 3 } N \mathrm { ~ b } )$ (d

![](images/image16.jpg)

$$
T = 8 6 . 2 N
$$

9. Cần phải có bao nhiêu mét khối hêli để nâng một khí cầu nhẹ có treo một tải trọng 400 kg lên đến độ cao $8 0 0 0 { \mathrm { m } } ?$ Lấy khối lượng riêng của He $\rho _ { H e } = 0 , 1 7 9 \mathrm { k g } / m ^ { 3 }$ . Giả sử thể tích khí cầu không đổi và mật độ không khí giảm theo độ cao $\mathbf { Z }$ theo biểu thức $\rho _ { k h \hat { 0 } n g k h i } = \ \rho _ { 0 } e _ { \mathrm { ~ \tiny ~ , ~ } } / 8 0 0 0$ , trong đó $\mathbf { Z }$ tính bằng mét và $\rho _ { 0 } { = } 1 { , } 2 0 \mathrm { k g } / m ^ { 3 }$ là mật độ không khí $\dot { \mathbf { O } }$ mực nước biển.

ĐS: $V = 1 . 5 2 \times 1 0 ^ { 3 } m ^ { 3 }$

10. Nước chảy qua một ống có đường kính 2.74 cm, đổ đầy một thùng 25 lít trong 1.50 phút.

(a) Tốc độ của nước rời khỏi đầu ống là bao nhiêu?   
(b) Một vòi phun được gắn vào đầu ống. Nếu đường kính vòi phun bằng 1/3 đường kính của ống, tốc độ của nước rời khỏi vòi phun là bao nhiêu?

ĐS: a) $\nu = ^ { 0 . 4 7 1 } \frac { m } { s } \ \mathbf { b } ) \ \nu = ^ { 4 . 2 4 } \frac { m } { s }$

11. Nước di chuyển qua một đường ống có tiết diện nhỏ dần trong dòng chảy ổn định (lý tưởng). Tại điểm thấp hơn thể hiện trong hình, áp suất $\mathtt { | i \mathrm { P } _ { 1 } = 1 . 7 5 \mathrm { x } 1 0 ^ { 4 } }$ Pa và đường kính ống là 6,00 cm. Tại một điểm khác cao hơn một đoạn $\mathrm { y } = 0 { , } 2 5 0 \mathrm { m } .$ áp suất là $\mathrm { P } _ { 2 } = 1 \mathrm { , } 2 0 \mathrm { x } 1 0 ^ { 4 }$ Pa và đường kính ống là 3,00 cm.

(a) Tìm tốc độ dòng chảy qua các tiêt diện $\dot { \mathbf { O } }$ hai đầu của đoạn ống trên. $( \mathsf { b } ) \mathsf { T i m }$ lưu lượng nước chảy qua ống.

![](images/image17.jpg)



12. Một ống hút được sử dụng để lấy nước từ một bể như minh họa trong hình bên. Giả sử dòng chảy ổn định không có ma sát.



(a) $\mathrm { N } \hat { \ e } \mathrm { u } \mathrm { h } = 1 , 0 0 \mathrm { m }$ , hãy tìm tốc độ dòng chảy ở cuối ống hút. (b) Tìm giới hạn về chiều cao của đỉnh ống hút (y) ở phía trên đầu của ống hút. Lưu ý: đối với dòng chảy của chất lỏng liên tục, áp suất của nó không được giảm xuống dưới áp suất hơi bão hòa của nó. Giả sử nước ở $2 0 { , } 0 ^ { 0 } \mathrm { C } ,$ , tại đó áp suất hơi bão hòa là $2 { , } 3 \mathrm { k P a }$ .

$$
\begin{array}{c} \nu = ^ { 4 . 4 3 } \frac { m } { s } \ b ) \ \gamma  \\ & { \leq 1 0 . 1 m } \end{array}
$$

![](images/image18.jpg)

13. Nước bị ép ra khỏi bình chữa cháy nhờ áp suất không khí được nén trong bình như trong hình. Áp suất khí trong bình bằng bao nhiêu để nước bị ép ra khỏi bình có tốc độ ${ 3 0 } \mathrm { , 0 ~ m / s }$ , khi mực nước trong bình thấp hơn vòi phun $0 { , } 5 0 0 \mathrm { m } ?$

ĐS: $P = 4 5 5 k P a$

14. Một tia nước phun ra theo chiều ngang từ một lỗ gần đáy bể. Nếu lỗ có đường kính $3 { , } 5 0 \ \mathrm { m m }$ , chiều cao h của mực nước trong bể là bao nhiêu?

ĐS: $h { = } 9 . 0 0 c m$

![](images/image19.jpg)

# Public_139 

Chuyển động tuần hoàn là một chuyển động lặp đi lặp lại của một vật theo thời gian. Sau một khoảng thời gian nhất định, vật trở về một vị trí cho trước. Một loại chuyển động tuần hoàn đặc biệt xảy ra trong các hệ cơ học được gọi là dao động. Đặc điểm của các hệ thống này là:

• Hệ có một vị trí cân bằng bền và chuyển động qua lại hai bên vị trí đó.   
• Lực tác dụng lên hệ luôn hướng về vị trí cân bằng (thường gọi là lực hồi phục).

Chúng ta có thể gặp các dao động trong thực tế như: dây đàn ghi ta, mặt trống khi rung động, dao động của cây cầu, của nhà cao tầng.

Nếu trong hệ dao động, lực tác dụng lên vật tỉ lệ thuận với độ dời của vật (so với vị trí cân bằng) thì dao động này được gọi là dao động điều hòa.Đây là loại dao động sẽ được nghiên cứu kỹ trong chương này.Tầm quan trọng của việc nghiên cứu này là ở chỗ: các dao động trong tự nhiên và trong kỹ thuật thường có tính chất rất gần với dao động điều hòa và mọi dao động tuần hoàn có thể được biểu diễn như sự tổng hợp của các dao động điều hòa.

Lý thuyết về dao động là cơ sở quan trọng để nghiên cứu một hiện tượng vật lý khác là hiện tượng sóng.

# Chuyển động của vật gắn với lò xo

Xét một vật nhỏ có khối lượng m(xem như chất điểm) được gắn với một lò xo có một đầu cố định. Vật mcó thể chuyển động không ma sát trên mặt phẳng ngang như Hình 15.1.Khi lò xo không co giãn, vật sẽ ở đứng yên ở vị trí gọi là vị trí cân bằng.Khi truyền cho vật một vận tốc từ vị trí cân bằng, vật sẽ dao động xung quanh vị trí này.

Chọn trục x dọc theo phương của lò xo, gốc O tại vị trí cân bằng. Khi vật ở vị trí có tọa $\hat { \mathrm { d } } \hat { \mathrm { o } } x$ thì lực đàn hồi do lò xo tác dụng lên vật được xác định theo định luật Hooke:

![](images/image1.jpg)  
Hình 15.1

$$
F _ { s } = - k . x
$$

Lực $F _ { s }$ luôn hướng về vị trí cân bằng và luôn ngược dấu với tọa $\mathtt { d } \hat { \boldsymbol { \mathrm { o } } } \boldsymbol { x } . \boldsymbol { x }$ được gọi là độ dời của vật (tính từ vị trí cân bằng, dưới đây gọi là li độ).

Áp dụng định luật Newton thứ hai cho vật, ta tìm được gia tốc của vật như sau:

$$
\begin{array} { c } { { F _ { x } = m a _ { x } \qquad { \displaystyle  ~ } - k x = m a _ { x } } } \\ { { a _ { x } = { } - { \displaystyle \frac { k } { m } } x } } \end{array}
$$

Từ 15.2 ta thấy gia tốc của vật tỉ lệ thuận với độ dời và ngược dấu với độ dời của vật.



Những hệ thống hoạt động theo quy luật này sẽ thực hiện một dao động điều hòa.



Một vật thực hiện dao động điều hòa khi gia tốc của vật tỉ lệ thuận với độ dời và ngược dấu với độ dời của vật.

# Khảo sát dao động cơ điều hòa

Thay $a _ { x } = d v / d t = d ^ { 2 } x / d t ^ { 2 }$ vào 15.2 ta được phương trình:

$$
{ \frac { d ^ { 2 } x } { d t ^ { 2 } } } = - { \frac { k } { m } } x
$$

Đặt

$$
\omega ^ { 2 } = { \frac { k } { m } }
$$

thì phương trình 15.3 trở thành:

$$
\frac { d ^ { 2 } x } { d t ^ { 2 } } = - \omega ^ { 2 } x
$$

Nghiệm của phương trình 15.5 là:

$$
x ( t ) = A \cos ( \omega t + \phi )
$$

Trong đó $A$ là biên độ dao động, $\omega$ là tần số góc và $\phi$ là pha ban đầu. $A , \omega$ và $\phi$ đều là các hằng số. Biên độ $A$ và pha ban đầu $\phi$ được xác định từ các điều kiện ban đầu (độ dời và vận tốc lúc $t = 0$ ).

Đại lượng $( \omega t + \phi )$ gọi là pha của dao động.

Từ 15.4 ta có biểu thức xác địnhtần số góc dao động:

$$
\omega = \mathrm { \sqrt { \frac { \it k } { m } } }
$$

Hai đại lượng quan trọng đặc trưng cho dao động là chu kỳ và tần số dao động. Chu kỳ T của dao động là khoảng thời gian vật hoàn thành một dao động. Dựa vào tính chất tuần hoàn của hàm số x(t) cho bởi phương trình 15.6, ta tìm được:

$$
T = \frac { 2 \pi } { \omega } = ~ 2 \pi \sqrt { \frac { m } { k } }
$$

Tần số f của dao động là số dao động diễn ra trong một đơn vị thời gian:



$$
f = { \cfrac { 1 } { T } } = { \cfrac { 1 } { 2 \pi } } \sqrt { \cfrac { k } { m } }
$$

Từ 15.6 chúng ta suy ra biểu thức của vận tốc và gia tốc như sau:

$$
\begin{array} { l } { { v ( t ) = - A \omega \sin ( \omega t + \phi ) } } \\ { { a ( t ) = - A \omega ^ { 2 } \cos ( \omega t + \phi ) } } \end{array}
$$



Các phương trình 15.6, 15,10 và 15.11 cho thấy: li độ $x$ và vận tốc $\nu$ lệch pha một góc $\pi / 2$ còn li $\widehat { \mathrm { d } } \widehat { \mathrm { o } } \ x$ và gia tốc $a$ lệch pha một góc bằng $\pi$ . Ngoài ra các giá trị cực đại của vận tốc và gia tốc được suy ra từ các phương trình 15.10 và 15.11 là

$$
v _ { m a x } = \omega A = \sqrt { \frac { k } { m } } \ A
$$

$$
\begin{array} { r } { a _ { m a x } = \omega ^ { 2 } A = \frac { k } { m } A } \end{array}
$$

![](images/image2.jpg)

Câu hỏi 15.1: Một vật gắn với lò xo được kéo đến vị trí $x = A$ và được thả ra từ trạng thái nghỉ. Trong một dao động hoàn chỉnh, chiều dài quãng đường vật đi được bằng:

(a) A/2 (b) A (c) 2A (d) 4A

Hình 15.2 Đồ thị biểu diễn sự phụ thuộc theo thời gian của: a.Li độ b. Vận tốc c. Gia tốc

Câu hỏi 15.2: Một hạt dao động điều hòa có đồ thị li độ theo thời gian được cho như hình vẽ. Khi hạt ở điểm A trên đồ thị, Chúng ta có thể nói gì về li độ và vận tốc của hạt ?

(a) Li độ và vận tốc của hạt đều dương.   
(b) Li độ của hạt âm, vận tốc của hạt bằng không.   
(c) Li độ và vận tốc của hạt đều âm.   
(d) Li độ của hạt âm, vận tốc của hạt dương.

![](images/image3.jpg)  
Hình vẽ cho câu hỏi 15.2

Câu hỏi 15.3: Hình bên là đồ thị của li độtheo thời gian của hai hạt A và B dao động điều hòa. Dao động điều hòa của B

(a) có tần số góc lớn hơn và biên độ lớn hơn của A.   
(b) có tần số góc lớn hơn và biên độ nhỏ hơn của A.   
(c) có tần số góc nhỏ hơn và biên độ lớn hơn của A.   
(d) có tần số góc nhỏ hơn và biên độ nhỏ hơn của A.

Câu hỏi 15.4: Một vật khối lượng mtreo vào một lò xo rồi cho dao động. Chu kỳ của dao động này là T. Thay vậtm bằng vật có khối lượng 2m. Cho vật 2m dao động thì chu kỳ của dao động bằng:



(a) 2T (b) √2?? (c) T (d) ??/√2e.T/2

![](images/image4.jpg)  
Hình vẽ cho câu hỏi 15.3



# Năng lượng của vật dao động điều hòa

Trong nội dung này chúng ta sẽ xem xét cơ năng của hệ dao động. Vì bỏ qua tác dụng của lực ma sát nên cơ năng của hệ được bảo toàn. Chúng ta sẽ sử dụng hệ dao động con lắc lò xo để thực hiện việc khảo sát này.

Động năng của hệ dao động chỉ là động năng của vật và bằng:

$$
K = { \frac { 1 } { 2 } } ~ m v ^ { 2 } = { \frac { 1 } { 2 } } ~ m \omega ^ { 2 } A ^ { 2 } \sin ^ { 2 } ( \omega t + \phi )
$$

Thế năng đàn hồi dự trữ $\acute { \mathbf { O } }$ lò xo và bằng (Lưu ý rằng $k = m \omega ^ { 2 }$ ):

$$
U = { \frac { 1 } { 2 } } \ k x ^ { 2 } = { \frac { 1 } { 2 } } \ m \omega ^ { 2 } A ^ { 2 } \cos ^ { 2 } ( \omega t + \phi )
$$

Cơ năng của hệ dao động điều hòa bằng:

$$
E = K + U = \frac { 1 } { 2 } \ : m \omega ^ { 2 } A ^ { 2 } [ \sin ^ { 2 } ( \omega t + \phi ) + \ : \cos ^ { 2 } ( \omega t + \phi ) ]
$$

$$
E = { \frac { 1 } { 2 } } \ m \omega ^ { 2 } A ^ { 2 } = { \frac { 1 } { 2 } } \ k A ^ { 2 }
$$

Kết quả thu được cho chúng ta thấy cơ năng của hệ dao động điều hòa là một hằng số và tỉ lệ thuận với bình phương biên độ dao động. Đồ thị ở hình 15.3 minh họa sự bảo toàn năng lượng của hệ.

![](images/image5.jpg)  
Hình 15.3: a. Đồ thị biểu diễn biểu diễn sự phụ thuộc của động năng và thế năng   
theo thời gian với $\phi$ $= 0$ .



b. Đồ thị biểu diễn biểu diễn sự phụ thuộc của động năng và thế năng

theo li độ.

Ngoài ra, từ $\mathrm { k } \acute { \mathrm { e t } }$ quả thu được cho năng lượng, ta có thể suy ra vận tốc của vật:

$$
E = K + U = { \frac { 1 } { 2 } } \ m v ^ { 2 } + { \frac { 1 } { 2 } } \ k x ^ { 2 } = { \frac { 1 } { 2 } } \ k A ^ { 2 }
$$

$$
v = \pm { \sqrt { { \frac { k } { m } } ( A ^ { 2 } - x ^ { 2 } ) } } = \pm \omega { \sqrt { ( A ^ { 2 } - x ^ { 2 } ) } }
$$



# Liên hệ giữa dao động điều hòa và chuyển động tròn đều

Trong thực tế cuộc sống, có nhiều thiết bị thể hiện mối liên hệ giữa dao độngđiều hòa và chuyển động tròn đều. Ví dụ, bộ phận truyền động của máy may cơ như hình 15.4 dưới đây. Khi chân của thợ may đạp tới lui vào bàn đạp tạo ra những dao động lên xuống chogờ bàn đạp và kéo theo chuyển động tròn của bánh xe truyền động. Chuyển động tròn này được truyền vào máy may nhờ sợi dây truyền động và dẫn đến kết quả là kim khâu dao động thẳng đứng. Trong phần này chúng ta sẽ tìm hiểu mối quan hệ giữa hai loại chuyển động này.

Hình 15.5 là một bố trí thực nghiệm để chỉ ra mối liên hệ giữa chuyển động tròn đều và dao động cơ điều hòa. Một quả cầu nhỏ(được xem như một chất điểm) gắn vào vành của đĩa tròn bán kính $A$ để chuyển động cùng với đĩa khi đĩa quay. Cho đĩa tròn quay đều. Chiếu đèn vào quả cầu, ta sẽ thấy cái bóng của quả cầuthực hiện một dao động trên màn.

![](images/image6.jpg)  
Hình 15.4

Cụ thể hơn, hãy quan sát hình 15.6 trong đó chất điểm chuyển động tròn đềuvới tốc độ góc ωtrên đường tròn tâm O bán kính $\dot { \boldsymbol { A } } . \dot { \boldsymbol { \mathrm { O } } }$ thời điểm $t = 0$ chất điểm $\dot { \mathbf { O } }$ vị trí P trên đường tròn có bán kính OP tạo với trục $x$ một góc $\phi$ (Hình 15.6a). Ởthời điểm $t .$ , vị trí $\mathrm { P }$ của chất điểm trên đường tròn có bán kính OP tạo với trục x một góc?? $\mathbf { \omega } = ( \omega t + \mathbf { \beta } \phi )$ (Hình 15.6b). Gọi Q là hình chiếu của P lên trục $x .$ , thì tọa độ của $\mathrm { Q }$ được xác định như sau:

![](images/image7.jpg)

$$
x ( t ) = A { \cos } ( \omega t { \mathrm { ~ + ~ } } \phi )
$$

Chuyển động của bóng của quả cầu.

Hình 15.5

#

Kết quả này chứng tỏ chứng tỏ Q dao động điều hòa trên trục x quanh vị trí cân bằng O với biên độ là A(A là bán kính quỹ đạo tròn của P). Chúng ta cũng thấy rằng

tốc độ góc ω củaP bằng với tần số góc của Q, chu kỳ chuyển động tròn của P Q và pha ban đầu $\phi$ của Q bằng góc mà OP hợp với trục x ở thời điểm $t = 0$ .

$+ ~ \phi )$ tương ứng bằng với vận tốc và gia tốc trong

# Public_140 

Thế giới chúng ta sống tràn ngập các loại sóng. Sóng nước là ví dụ thực tế cho ta hình dung khá rõ về sóng. Bằng cách ném một viên sỏi vào mặt nước phẳng lặng,tại điểm tiếp xúc của viên sỏi và mặt nước các sóng hình tròn được tạo ra và bắt đầu mở rộng dần từ điểm tiếp xúc (viên sỏi gọi là nguồn phát sóng). Nếu quan sát kỹ một vật nhỏ

nổi trên mặt nước ở gần nguồn sóng, ta sẽ thấy vật này di chuyển theo phương thẳng đứng và phương ngang quanh một vị trí gốc nhưng thực sự không di chuyển về phía nguồn phát sóng hoặc ra xa nguồn phát sóng. Chuyển động của vật nổi trên thực ra là do chuyển động của các phần tử nước tiếp xúc với vật truyền cho vật. Mọi phần tử nước khác trên mặt nước cũng chuyển động như vậy. Điều này có nghĩa là sóng nước thì cứ chuyển động ra xa nguồn nhưng nước thì không được vận chuyển theo. Trong hiện tượng sóng, dao động của các phần tử được lan truyền, nghĩa là năng lượng cũng đã được lan truyền từ nguồn sóng.

Chúng ta sẽ khảo sát hai loại sóng: sóng cơ học và sóng điện từ. Đối với sóng cơ học, để sóng hình thành và lan truyền được cần thiết phải có môi trường vật chất. Sóng điện từ có thể lan truyền trong môi trường vật chất và cả trong chân không.

Trong chương này, chúng ta sẽ tìm hiểu rõ hơn về sóng cơ học.



# Sự lan truyền nhiễu loạn

### Sự hình thành sóng

Tất cả các sóng cơ học đều đòi hỏi phải có nguồn nhiễu loạn, môi trường vật chất để có thể truyền nhiễu loạn và một số cơ chế vật lý nhờ đó các phần tử môi trường tương tác lẫn nhau.

Để minh họa cho chuyển động sóng, chúng ta hãy xét thí nghiệm trình bày ở hình 16.1. Sau khikéo căng một sợi dây dài đã cố định một đầu, bằng cách giật nhanh tay lên và xuống đầu tự do của sợi dây ta sẽ thấy trên dây hình thành một cái bướu và nó dịch chuyển dọc trên dây. Bướu này gọi là xung. Trong thí nghiệm này, bàn tay là nguồn nhiễu loạn và sợi dây là môi trường để xung truyền đi. Các phần tử riêng biệt trên dây bị nhiễu loạn từ vị trí cân bằng của chúng và sự liên kết giữa các phần tử của dây làm cho nhiễu loạn được lan truyền dọc theo dây. Xung có chiều cao xác định và truyền dọc theo dây với tốc độ xác định. Hình dáng của xung thay đổi rất ít khi xung lan truyền dọc theo dây.

Bằng cách liên tục di chuyển lên và xuống đầu tự do của dây, chúng ta sẽ tạo ra được một sóng lan truyền trên dây. Sóng là một nhiễu loạn tuần hoàn di chuyển qua một môi trường.

Khi xung di chuyển dọc theo dây, các phần tử của dây rời khỏi vị trí cân bằng của chúng.

![](images/image1.jpg)

Hình 16.1: Mỗi lần bàn tay di chuyển một đầu dây lên và xuống sẽ tạo ra một xung truyền dọc theo dây

### Phân loại sóng

Tùy thuộc vào phương dao động của các phần tử môi trường, sóng được chia thành hai loại: sóng ngang và sóng dọc.

Sóng ngang: Khi lan truyền, sóng loại này sẽ làm cho các phần tử của môi trường chuyển động vuông góc với phương truyền sóng.Hình $1 6 . 2 ~ \mathrm { m } \hat { \mathrm { { o } } }$ tả một sóng ngang lan truyền trên sợi dây. Chuyển động của phần tử tại P được biểu diễn bằng mũi tên thẳng đứng. Hướng truyền của sóng được biểu diễn bằng mũi tên nằm ngang.

Sóng dọc:Khi sóng này truyền qua, cho các phần tử của môi trường chuyển động song song với phương truyền sóng.

Hình 16.3 là một ví dụ về sóng dọc khi tay liên tục di chuyển qua tới và lui. Một trường hợp khác cho sóng dọc là sóng âm.



![](images/image2.jpg)  
Hình 16.2



Bàn tay di chuyển tới lui để tạo ra một xung dọc .

Độ dời của các vòng lò xo là song song với phương truyền.

![](images/image3.jpg)  
Hình 16.3: Một xung lan truyền dọc theo một lò xo

Một số sóng thể hiện sự kết hợp đặc tính chuyển dời của cả sóng dọc và sóng ngang. Sóng trên mặt nước là một ví dụ. Khi sóng truyền trên mặt nước, các phần tử nước trên bề mặt di chuyển gần như thành vòng tròn. Nhiễu loạn có cả thành phần dọc và thành phần ngang.

![](images/image4.jpg)  
Hình 16.4: Sóng nước

### Hàm sóng

Khảo sát một xung lan truyền về bên phải với vận tốc vtrên một sợi dây dài như trên hình 16.5. Hình 16.5a trình bày hình dạng và vị trí của xung tại thời điểm $t = 0$ và xung này được mô tả bằng hàm số $y ( x , 0 ) = f ( x )$ . Hàm số này cho biết tọa độ y (độ dời) của phần tử có tọa độ $x$ trên dây vào thời điểm $t = 0$ . Sau khoảng thời gian $t$ , xung đi được quãng đường $\nu t$ (Hình 16.5b). Chúng ta giả sử rằng hình dạng của xung là không thay đổi theo thời gian. Trong trường hợp này,tọa $\hat { \mathrm { d } } \hat { \mathrm { 0 } } y$ của phần tử có tọa độ $x$ trên dây $\dot { \mathbf { O } }$ thời điểm $t$ bằngtọa $\mathtt { d o } y$ của phần tử có tọa độ $( x - \nu t )$ trên dây $\dot { \mathbf { O } }$ thời điểm $\mathrm { t } = 0$ :

$$
y ( x , t ) = y ( x - v t , 0 )
$$



Tóm lại: Khi xung di chuyển về bên phải (theo chiều dương trục $\mathrm { O x } {  }$ ),tọa $\hat { \mathrm { d } } \hat { \mathrm { 0 } } y$ của phần tử có tọa độ $x$ trên dây $\dot { \mathbf { O } }$ thời điểm $t$ được xác định bởi hàm số:

$$
y ( x , t ) = f ( x - v t )
$$

Tương tự: Khi xung di chuyển về bên trái, tọa $\hat { \mathrm { d } } \hat { \mathrm { 0 } } \ y$ của phần tử có tọa $\widehat { \mathrm { d } } \widehat { \mathrm { o } } \boldsymbol { x }$ trên dây $\acute { \mathbf { O } }$ thời điểm $t$ được xác định bởi hàm số:

$$
y ( x , t ) = f ( x + v t )
$$

Hàm $y ( x , t )$ được gọi là hàm sóng. Hàm số này cho biết tọa $\hat { \mathbf { d } } \hat { \mathbf { 0 } } \boldsymbol { y }$ của phần tử bất kỳ tại vị trí $x$ vào thời điểm t. Khi cố định $t .$ , hàm sóng $y ( x )$ cho biết hình dạng của sóng ở thời điểm $t$ đó.

# Sóng hình sin

![](images/image5.jpg)  
Hình 16.5: Xung một chiều truyền về phía bên phải của dây

Chúng ta sẽ xem xét một loại sóng có hình dạng như đồ thị của hàm sin, sóng loại này được gọi là sóng hình sin. Hình $1 6 . 6 ~ \mathrm { m } \hat { \mathrm { o } }$ tả một sóng hình sin đang di chuyển về phía bên phải với vận tốc v. Sóng này có thể được tạo ra trên một sợi dây như trong hình 16.1 khi đầu tự do của dây được rung để di chuyển lên xuống như một dao động điều hòa. Chúng ta chọn sóng hình sin để khảo sát vì mọi dạng sóng đều có thể xây dựng được bằng cách cộng các sóng hình sin có tần số và biên độ xác định. Sự hiểu biết về sóng hình sin là cơ sở để hiểu được các sóng có bất kỳ dạng nào.

Cần phân biệt hai loại chuyển động xảy ra khi một sóng lan truyền: chuyển động của sóng về phía bên phải theo trục Ox và dao động điều hòa của các phần tử môi trường theo trục Oy.

Chúng ta sẽ xem xét một loại sóng được đơn giản hóa như sau: sóng có một tần số duy nhất và có chiều dài vô hạn.

![](images/image6.jpg)  
Hình 16.6: Hình dạng sóng sin

### Các khái niệm và các đại lượng đặc trưng của sóng

• Đỉnh sóng là điểm trong không gian mà phần tử môi trường tại đó có vị trí cao nhất. (Hình 16.7a).



• Hõm sóng là điểm trong không gian mà phần tử môi trường tại đó có vị trí thấp nhất.

• Biên độ A của sóng: là biên độ dao động của các phần tử môi trường. $\mathrm { ( H i n h ~ 1 6 . 7 ) }$ .

• Tần số f của sóng: là số đỉnh sóng (hoặc là bất kỳ điểm nào trên sóng) đi qua một điểm cho trước trong một đơn vị thời gian. Tần số sóng bằng với tần số dao động điều hòa của các phần tử môi trường.



• Chu kỳ ${ \pmb T }$ của sóng: là khoảng thời gian để hai đỉnh sóng liền nhau đi qua một một điểm cho trước trong không gian.Chu kỳ của sóng bằng với chu kỳ dao động điều hòa của các phần tử môi trường. (Hình 16.7b).

Chu kỳ và tần số của sóng liên hệ với nhau theo công thức:

$$
\mathrm { T } = { \frac { 1 } { f } }
$$

• Bước sóng λ: là khoảng cách từ đỉnh (hõm) sóng này đến đỉnh (hõm) sóng kế tiếp. Tổng quát hơn, bước sóng là khoảng cách ngắn nhất giữa hai điểm đồng nhất trên sóng. (Phần tử môi trường tại hai điểm này dao động giống hệt nhau.)

• Tốc độ truyền sóng v: mỗi sóng sẽ lan truyền với tốc độ riêng, tốc độ này phụ thuộc vào tính chất của môi trường truyền sóng.

Tốc độ truyền sóng liên hệ với bước sóng và chu kỳ của sóng theo công thức:

$$
v = { \frac { \lambda } { T } } = \lambda . f
$$

![](images/image7.jpg)  
Hình 16.7: (a) Hình ảnh của một sóng hình sin. (b) Vị trí của một phần tử môi trường như một hàm số của thời gian.

### Hàm sóng

Giả sử xét một sóng hình sin $\acute { \mathbf { O } }$ thời điểm $t = 0$ có hình dạng như ở hình 16.7a thì hàm sóng ở thời điểm này được cho bởi hàm s $\hat { \hat { 0 } } y ( x , 0 ) = A \sin a x$ . Do tính chất tuần hoàn của hàm số này, ta suy ra được $a = 2 \pi / \lambda$ . Nên

$$
y ( x , 0 ) = A s i n { ( \frac { 2 \pi } { \lambda } x ) }
$$



Nếu sóng truyền về bên phải (theo chiều dương trục x) thì theo 16.1, hàm sóng $\acute { \mathbf { O } }$ thời điểm t là

$$
y ( x , t ) = A s i n [ \frac { 2 \pi } { \lambda } ( x - v t ) ]
$$

Nếu sóng truyền về phía bên trái thì thay $( x - \nu t )$ thành $( x + \nu t )$ trong 16.5.   
trong đó $\phi$ là pha ban đầu. sóng sin trên sợi dây.

### Sóng hình sin trên dây

Để tạo một một sóng trên dây, ta gắn một đầu dây vào một cần rung và cho cần rung dao động điều hòa (Hình 16.8). Mỗi phần tử trên dây dao động điều hòa theo phương thẳng đứng y với tần số bằng tần số của cần rung, trong khi đó sóng truyền về bên phải theo chiều dương của trục Ox với tốc độ $\nu$ .

Giả sử chọn $t = 0$ là lúc hình dạng của dây như $\dot { \mathbf { O } }$ hình 16.8a thì hàm sóng được viết là:

$$
y = A \sin ( k x - \omega t )
$$



$$
a _ { y , m a x } = \omega ^ { 2 } A _ { \mathbf { \omega } }
$$

Cần lưu ý rằng: tốc độ truyền sóng $\nu$ là hằng số đối với một môi trường đồng nhất, trong khi đó vận tốc của một phần tử trên dây $\nu _ { y }$ là một hàm sin của thời gian.

# Tốc độ của sóng trên dây

Tốc độ của sóng phụ thuộc vào tính chất vật lý của dây và lực căng dây theo công thức:

$$
v = { \sqrt { \frac { T } { \mu } } }
$$

với $\mu$ là khối lượng trên một đơn vị chiều dài của dây $( \mathrm { k g / m } )$ và $T$ là lực căng dây.

# Sự phản xạ và truyền qua của sóng

Ở nội dung này chúng ta sẽ xem xét một sóng bị ảnh hưởng như thế nào trong quá trình lan truyền khi gặp phải sự thay đổi trong môi trường.

![](images/image8.jpg)

![](images/image9.jpg)  
Hình 16.10: Sự phản xạ của một xung ở đầu tự do của sợi dây.

Hình 16.9: Sự phản xạ của một xung ở đầu cố định của sợi dây.

Hình 16.9 mô tả một xung lan truyền trên một sợi dây căng ngang có một đầu buộc vào giá cố định. Khi xung di chuyển đến giá cố định, nghĩa là đến cuối dây, thì môi trường truyền bị thay đổi đột ngột. Kết quả là xung chuyển động dọc trên dây theo chiều ngược lại tạo thành xung phản xạ. Xung phản xạ này bị đảo ngược so với xung ban đầu (xung tới) nhưng không bị thay đổi hình dạng. Sự đảo ngược của xung phản xạ so với xung tới có thể được giải thích nhờ định luật Newton thứ ba.

Trong trường hợp trên đầu cuối của dây được buộc cố định. Ở một trường hợp khác, đầu cuối dây có thể di chuyển tự do theo phương thẳng đứng như hình 16.10. Xung phản xạ lúc này không bị đảo ngược và cũng có cùng hình dạng như xung tới.





Cuối cùng là một trường hợp trung gian của hai trường hợp trên. Khi xung di chuyển đến biên giữa hai môi trường, một phần năng lượng của xung tới sẽ bị phản xạ ngược lại, một phần năng lượng sẽ truyền qua môi trường kia.

![](images/image10.jpg)

Hình 16.11: Một xung di chuyển trên một dây Hình 16.12: Một xung di chuyển trên một nhẹ đến chỗ nối với một dây nặng hơn. dây nặng đến chỗ nối với một dây nhẹ hơn.

Chẳng hạn như một sợi dây nhẹ được nối với một sợi dây nặng hơn như trên hình 16.11. Khi xung di chuyển trên dây nhẹ đến gặp điểm tiếp xúc của hai dây thì hai xung được hình thành đồng thời: xung phản xạ trở lại (bị đảo ngược và có biên độ nhỏ hơn xung tới) và xung truyền qua chuyển động trên dây nặng hơn (không bị đảo ngược). Trong trường hợp xung di chuyển trên dây nặng đến gặp điểm tiếp xúc với dây nhẹ hơn như ở hình 16.12 thì các xung phản xạ và xung truyền qua vẫn hình thành nhưng xung phản xạ không bị đảo ngược.

# Tốc độ truyền năng lượng bởi sóng sin trên dây

Chúng ta hãy xem xét sự truyền sóng hình sin theo trục x trên một sợi dây căng ngang trên như hình 16.13.

Nguồn năng lượng là tác nhân bên ngoài gắn với đầu bên trái của dây. Tác nhân này thực hiện công ở đầu bên trái của dây (bằng cách di chuyển lên xuống), nhờ đó năng lượng được truyền vào hệ và sau đó được truyền dọc theo chiều dài của dây. Xét phần tử nhỏ có tọa độ $x ,$ , chiều dài $d x$ và khối lượng dm. Phần tử này (cũng như các phần tử khác

![](images/image11.jpg)  
Hình 16.13

trên dây) thực hiện dao động điều hòa theo phương thẳng đứngyvới phương trình

$$
y = A \sin ( k x - \omega t )
$$

# Public_141 

Trong cơ học, chúng ta đã xác định khái niệm về khối lượng, lực và động năng để tạo tiền đề cho phương pháp định lượng. Tương tự như vậy, một khái niệm định lượng về các hiện tượng nhiệt đòi hỏi phải định nghĩa đầy đủ về nhiệt độ, nhiệt lượng và nội năng. Chương này bắt đầu với bài viết về nhiệt độ. Tiếp theo, chúng ta xem xét tầm quan trọng khi nghiên cứu các hiện tượng nhiệt của các chất đặc biệt. Ví dụ: các loại khí giãn nở đáng $\bar { \mathrm { k } } \bar { \hat { \mathrm { e } } }$ khi nung nóng, trong khi chất lỏng và chất rắn giãn nở ít hơn. Chương này kết thúc với một nghiên cứu về khí lý tưởng ở mức vĩ mô. Ở đây, chúng ta chỉ quan tâm đến các mối quan hệ định lượng giữa áp suất, thể tích và nhiệt độ của một chất khí.

# Nhiệt độ và nguyên lý thứ không của nhiệt động lực học

# Nhiệt độ

Chúng ta thường kết hợp các khái niệm về nhiệt độ với độ nóng hoặc lạnh một đối tượng khi chúng ta chạm vào nó. Bằng cách này, các giác quan cho ta chỉ số định tính của nhiệt độ. Tuy nhiên, giác quan của chúng ta không đáng tin cậy và thường đánh lừa chúng ta.

Ví dụ, nếu bạn đứng bằng đôi chân trần với một chân trên thảm và một chân trên sàn gạch liền kề, ta cảm thấy gạch lạnh hơn so với thảm mặc dù cả hai đều ở cùng một nhiệt độ, lý do là vì gạch trao đổi năng lượng dưới dạng nhiệt mạnh hơn so với thảm. Làn da của bạn “đo đạc” mức độ trao đổi năng lượng bằng nhiệt chứ không phải là nhiệt độ thực tế.

Những gì chúng ta cần là một phương pháp đáng tin cậy và có thể lặp lại để đo độ nóng hoặc lạnh của đối tượng chứ không phải là tỷ lệ chuyển đổi năng lượng. Các nhà khoa học đã chế tạo và phát triển các nhiệt kế khác nhau để phục vụ các phép đo định lượng như vậy.

![](images/image1.jpg)  
Hình 19.1: Nguyên lý thứ không của nhiệt động lực học, A và B cân bằng nhiệt với nhau



# Nguyên lý thứ không của nhiệt động lực học

Hai đối tượng có nhiệt độ ban đầu khác nhau cuối cùng đạt được nhiệt độ trung bình khi được đặt tiếp xúc với nhau.

Ví dụ, khi nước nóng và nước lạnh được trộn lẫn trong một bồn tắm, năng lượng được chuyển từ nước nóng đến nước lạnh và nhiệt độ cuối cùng của hỗn hợp là giá trị nào đó giữa nhiệt độ nóng và lạnh ban đầu.

Nguyên lý thứ không nhiệt động học (định luật trạng thái cân bằng) phát biểu như sau:

Nếu hai vật lần lượt cân bằng nhiệt với một vật thứ ba nào đó, thì chúng cũng cân bằng nhiệt với nhau.

Cân bằng nhiệt có nghĩa là trạng thái trong đó hai vật tiếp xúc vật lí với nhau có nhiệt độ bằng nhau.

Cái quan trọng nhất mà nguyên lý thứ không thiết lập là nhiệt độ là một tính chất căn bản và có thể đo được của vật chất.

Câu hỏi 19.1: Hai đối tượng, với các kích thước, khối lượng và nhiệt độ khác nhau, được đặt tiếp xúc nhiệt. Chiều chuyển đổi năng lượng như thế nào?

(a) Năng lượng đi từ đối tượng lớn đến đối tượng nhỏ hơn.   
(b) Năng lượng đi từ vật có khối lượng lớn đến vật có khối lượng nhỏ hơn.   
(c) Năng lượng đi từ đối tượng ở nhiệt độ cao hơn đến đối tượng ở nhiệt độ thấp hơn.

# Nhiệt kế và thang đo độ C (Celcius)

# Nhiệt kế

Nhiệt kế là thiết bị được sử dụng để đo nhiệt độ của một hệ, dựa trên nguyên lý: một số tính chất vật lý của một hệ thống thay đổi khi nhiệt độ của hệ thay đổi.

The level of the mercury in the thermometer rises as the mercury is heated by water in the test tube.

Một số tính chất vật lý thay đổi theo nhiệt độ là

• thể tích của chất lỏng,   
• các kích thước của chất rắn, áp suất của chất khí ở thể tích không đổi, thể tích của chất khí ở áp suất không đổi,   
điện trở của dây dẫn

![](images/image2.jpg)



• màu sắc của vật.

Nhiệt $\mathrm { k } \acute { \mathrm { e } }$ thông dụng có chứa một lượng chất lỏng, thường là thủy ngân hoặc rượu, có thể giãn nở trong một ống mao dẫn thủy tinh khi

Hình 19.2: Nhiệt kế thủy ngân trước và sau khi tăng nhiệt độ của nó.

bị nung nóng (Hình 19.2). Trong trường hợp này, đặc tính thay đổi là thể tích của chất lỏng.



Một sự thay đổi nhiệt độ bất kỳ trong nhiệt kế được định nghĩa là tỷ lệ thuận với sự thay đổi độ cao của cột chất lỏng. Có thể hiệu chỉnh nhiệt kế bằng cách đặt nó tiếp xúc nhiệt với một hệ tự nhiên được duy trì ở nhiệt độ không đổi.

# Thang nhiệt độ Celsius (độ C)

Thang nhiệt độ Celsius xác định nhiệt độ của vật theo độ C (viết tắt $^ { 0 } \mathrm { C }$ ), do nhà thiên văn học Anders Celsius đưa ra vào năm 1742.

Thang nhiệt độ Celsius lấy nhiệt độ của nước khi đóng băng $( 0 ^ { 0 } \mathrm { C } )$ và nhiệt độ sôi của nước $( 1 0 0 ^ { 0 } \mathrm { C } )$ làm chuẩn, trong điều kiện áp suất tiêu chuẩn. Sau đó chia nhỏ thành 100 vạch chia, mỗi vạch chia tương ứng với 1 độ.

# Nhiệt $\mathbf { k } \hat { \mathbf { e } }$ khí đẳng tích và thang nhiệt độ tuyệt đối Nhiệt kế khí đẳng tích

Tính chất vật lý được khai thác trong thiết bị này là sự thay đổi của áp suất theo nhiệt độ ứng với thể tích không đổi.

Bình P được ngâm trong nước đá và cột B chứa thủy ngân. Thể tích của khí trong bình cầu P được giữ không đổi, cột thủy ngân B có thể nâng lên hay hạ xuống để mức thủy ngân trong cột A ở điểm $" 0 "$ trên thang đo. Độ chênh lệch cột thủy ngân là h. Từ đó, ta tính được áp suất của khí $\overset { \cdot } { \mathbf { O } } \overset { 0 } { \underset { \cdot } { \mathbf { O } } } { } ^ { 0 } \overset { \cdot } { \mathbf { C } }$ bằng phương trình $P = P _ { 0 } + \rho g h$ .

Kế tiếp cho bình P ngâm trong nước sôi. Cột thủy ngân B cũng được điều chỉnh sao cho mức thủy ngân $\acute { \mathbf { O } }$ cột A ở điểm "0" trên thang đo. Tiếp tục đo độ chênh lệch cột thủy ngân và từ đó, ta tính được áp suất của khí ${ \textrm { y l } } 0 0 { \textrm { } } ^ { 0 } { \mathrm { C } }$ .

![](images/image3.jpg)  
The volume of gas in the flask is kept constant by raising or lowering reservoir $B$ to keep the mercury level in column A constant.   
Hình 19.3: Nhiệt kế khí đẳng tích

Nhiệt kế khí đẳng tích dễ dàng cho ra kết quả áp suất trên một dải nhiệt độ. Nó khá chính xác - miễn là chúng ta tránh gần với nhiệt độ ngưng tụ của khí. Thật thú vị khi ngoại suy biểu đồ này để xem ở nhiệt độ nào, áp suất bằng 0.

![](images/image4.jpg)

Độ không tuyệt đối

Hình 19.4: Đồ thị biểu diễn mối quan hệ của áp suất theo nhiệt độ của nhiệt kế



Nếu ta sử dụng nhiệt kế khí đẳng tích với các loại khí khác nhau, thực nghiệm cho thấy giá trị đọc được từ nhiệt kế không phụ thuộc vào loại khí được sử dụng. Nếu kéo dài đồ thị cho các loại khí khác nhau, áp suất luôn bằng không khi nhiệt độ là $- 2 7 3 , 1 5 ^ { \mathrm { { o } } } \mathrm { { C } }$ . Nhiệt độ này được gọi là số không tuyệt đối – không độ tuyệt đối.



Không độ tuyệt đối được sử dụng như là cơ sở của các thang nhiệt độ tuyệt đối. Kích thước thang chia độ của thang nhiệt độ tuyệt đối giống kích thước của thang chia độ trên thang nhiệt giai Celsius.

$$
\mathrm { ~ T ~ } ^ { 0 } \mathrm { C } = \mathrm { T } - 2 7 3 , 1 5
$$

![](images/image5.jpg)  
Hình 19.5: Đồ thị từ thực nghiệm biểu diễn áp suất theo nhiệt độ

# Thang nhiệt độ tuyệt đối (thang nhiệt độ Kelvin)

Thang nhiệt độ tuyệt đối được thông qua vào năm 1954 bởi Ủy ban quốc tế về Khối lượng và Đo lường, nó dựa trên hai điểm cố định mới:

• Một điểm là điểm 0 tuyệt đối, là trạng thái nhiệt động học lý tưởng của vật chất, trong đó mọi chuyển động nhiệt đều ngừng. • Điểm thứ hai là điểm ba của nước. Điểm ba của nước nghĩa là ứng với cùng một giá trị nhiệt độ và áp suất của nước, ba pha của nước (khí, lỏng, rắn) có thể cùng tồn tại trong cân bằng nhiệt động lực học. Điểm ba của nước xảy ra $^ { \mathrm { ~ \tiny ~ 5 ~ 0 ~ , 0 1 ^ { \mathrm { o } } C } }$ và $4 { , } 5 8 \ \mathrm { m m }$ thủy ngân. Nhiệt độ này được đặt bằng giá trị 273,16 trên thang nhiệt độ tuyệt đối.

Cách làm này làm cho thang độ không tuyệt đối cũ phù hợp với các thang nhiệt độ mới.

Đơn vị đo nhiệt độ trong hệ đơn vị SI là Kelvin.

Thang nhiệt độ tuyệt đối cũng được gọi là thang nhiệt độ Kelvin.

Nhiệt độ điểm ba là 273,16 K. Khi dùng kelvin thì không sử dụng ký hiệu độ.

Kelvin được định nghĩa là 1/273,16 của độ chênh lệch giữa không độ tuyệt đối và nhiệt



độ của điểm ba của nước.



# Vài ví dụ về nhiệt độ tuyệt đối

Các con số ở hình 19.6 cho biết giá trị nhiệt độ tuyệt đối của các quá trình vật lý khác nhau. Thang đo là thang logarit.

Thực tế, không thể đạt nhiệt độ không tuyệt đối. Các thí nghiệm đã đến được gần nhiệt độ này.

# Thang nhiệt độ Fahrenheit (độ F)

Đây là một thang đo thông dụng được sử dụng thường ngày ở Mỹ, đặt tên theo Daniel Fahrenheit. Nhiệt độ đóng băng của nước là 32oF, và nhiệt độ hóa hơi của nước là 212oF. Có 180 khoảng chia (độ) giữa hai điểm tham chiếu.

# Mối quan hệ giữa các thang đo

Mối quan hệ giữa độ Celsius và Kelvin

$$
T _ { C } = T - 2 7 3 , 1 5
$$

Mối quan hệ giữa độ Celsius và độ F

$$
T _ { F } = \frac { 9 } { 5 } T _ { C } + 3 2
$$

Nhiệt độ đóng băng của nước

$$
0 ^ { \circ } \mathbf { C } = 2 7 3 , 1 5 \mathbf { K } = 3 2 ^ { \circ } \mathbf { F }
$$

Nhiệt độ hóa hơi của nước

$$
1 0 0 ^ { \circ } \mathrm { C } = 3 7 3 , 1 5 \mathrm { K } = 2 1 2 ^ { \circ } \mathrm { F }
$$

Note that the scale is logarithmic.

![](images/image6.jpg)  
Hình 19.6: Nhiệt độ tuyệt đối của các quá trình vật lý khác nhau

Câu hỏi 19.2: Hãy xem xét các cặp vật liệu sau đây. Cặp nào có hai vật liệu, vật liệu này nóng gấp đôi vật liệu kia? (a) nước sôi ở $1 0 0 ^ { 0 } \mathrm { C } ,$ , một ly nước ở $5 0 ~ ^ { 0 } \mathrm { C }$ (b) nước sôi $\dot { \mathrm { ~ y ~ l ~ } } 1 0 0 ^ { \mathrm { { ~ 0 } } } \mathrm { { C } }$ , mêtan đông lạnh tại – 50 0C (c) một khối băng $\dot { \sigma } - 2 0 { } ^ { 0 } \mathrm { C }$ , ngọn lửa $2 3 3 ~ ^ { 0 } \mathrm { C }$ (d) không có cặp nào trong số đó oLARace

# Bài tập mẫu19.1:

Nhiệt độ $5 0 ~ \mathrm { { ^ { 0 } F } }$ đổi ra nhiệt độ Celcius và Kelvin bằng bao nhiêu? (Đáp số 10 0C và 283 K)

Sự giãn nở nhiệt của chất rắn và chất lỏng



# Giãn nở nhiệt

Giãn nở nhiệt là sự gia tăng kích thước của một vật khi nhiệt độ của nó tăng lên. Giãn nở nhiệt là hệ quả của sự thay đổi khoảng cách tương đối giữa các nguyên tử trong một vật. Nếu sự giãn nở tương đối nhỏ so với kích thước ban đầu của vật, sự thay đổi theo chiều bất kỳ,



Without these joints to separate sections of roadway on bridges, the surface would buckle due to thermal expansion on very hot days or crack due to contraction on very cold days.

![](images/image7.jpg)  
a

The long, vertical joint is filled with a soft material that allows the wall to expand and contract as the temperature of the bricks changes.

![](images/image8.jpg)  
Hình 19.7: Ví dụ về giãn nở nhiệt

lấy xấp xỉ, là tỷ lệ thuận với lũy thừa bậc nhất của sự thay đổi về nhiệt độ. Các ví dụ về giãn nở nhiệt được minh họa trong hình 19.7.

# Giãn nở dài

Giả sử một đối tượng có chiều dài ban đầu $L _ { i }$ . Nhiệt độ thay đổi một lượng $\Delta T = T _ { f } - T _ { i }$ , chiều dài thay đổi một lượng $\Delta L = L _ { f } - L _ { i }$ . Ta định nghĩa hệ số giãn nở dài là:

Khi vòng bị đốt nóng, kích thước theo các chiều đều tăng lên. Khoảng trống trong vòng đệm và vòng đệm giãn nở như nhau

$$
\Delta L _ { \big / }
$$

$$
\alpha = \frac { L _ { i } } { \Delta T }
$$

![](images/image9.jpg)

Hệ số giãn nở dài, α, có đơn vị là (oC)-1

Một số vật liệu giãn nở dọc theo một chiều, nhưng co lại theo các chiều khác khi nhiệt độ tăng. Do các kích thước dài thay đổi, diện tích bề mặt và thể tích cũng thay đổi theo sự thay đổi về nhiệt độ. Một lỗ hở trong một mẩu vật liệu cũng giãn nở giống như phần rỗng đã được lấp đầy bởi vật liệu ấy. Khái niệm về sự nở vì nhiệt có thể được xem là tương tự với sự phóng ảnh.



# Giãn nở khối

Sự giãn nở khối tỷ lệ thuận với khối lượng ban đầu và sự thay đổi $\mathcal { \dot { \mathbf { v } } } \dot { \hat { \mathbf { e } } }$ nhiệt độ.

$$
\Delta V = \beta V _ { i } \Delta T
$$

• $\beta$ là hệ số giãn nở khối.

Hình 19.8: Sự giãn nở vì nhiệt của một cái vòng.



• Đối với một vật rắn, $\beta = 3 a$ (Giả định vật liệu là đẳng hướng, giống nhau ở tất cả các hướng).

• Đối với một chất lỏng hoặc khí, $\beta$ được cho trong bảng.

# Bảng 19.1: Hệ số giãn nở nhiệt của một số vật liệu

Table 19.1 Average Expansion Coefficients for Some Materials Near Room Temperature   



Hình 19.9: a) Dải lưỡng kim uốn cong khi nhiệt độ thay đổi do hai kim loại có hệ số giãn nở nhiệt khác nhau và b) Một dải lưỡng kim được sử dụng trong bộ điều nhiệt để ngắt hoặc làm tiếp xúc điện.



# Sự giãn nở nhiệt của nước

• Khi tăng nhiệt độ từ $0 \mathrm { { ^ \circ C } }$ đến $4 \mathrm { { ^ \circ C } }$ , nước co lại. Mật độ của nó tăng lên. • Trên $4 \mathrm { { ^ \circ C } }$ , nước giãn nở khi nhiệt độ tăng. Mật độ của nó giảm. • Mật độ nước tối đa ( $1 0 0 0 \mathrm { g } / \mathrm { c m } ^ { 3 } )$ xảy ra ở $4 \mathrm { { ^ \circ C } }$

![](images/image10.jpg)  
Hình 19.10: Mật độ nước thay đổi theo nhiệt độ ở áp suất khí quyển.

Câu hỏi 19.3: Nếu bạn được yêu cầu làm một nhiệt kế thủy tinh rất nhạy,bạn sẽ chọn loại chất lỏng nào sau đây? (a) thủy ngân (b) rượu (c) xăng (d) glycerin

Câu hỏi 19.4: Hai khối cầu được làm bằng cùng một kim loại và có cùng bán kính, nhưng một cái rỗng và một cái đăc. Khi nhiệt độ tăng, quả cầu nào mở rộng hơn? (a) Quả cầu đặc (b) Quả cầu rỗng (c) Hai quả cầu mở rộng như nhau (d) Không có đủ thông tin.

# Bài tập mẫu 19.2:

Một đoạn đường ray làm bằng thép có chiều dài $3 0 \mathrm { m }$ khi nhiệt độ là $0 \%$ . Độ dài của   
nó bằng bao nhiêu khi nhiệt độ là $4 0 ~ ^ { 0 } \mathrm { C 2 }$   
(Đáp số: 30,013m)

# Mô tả vĩ mô về khí lý tưởng

# Khí lý tưởng

Khí lý tưởng là một loại chất khí tưởng tượng chứa các hạt giống nhau có kích thước vô cùng nhỏ so với thể tích của khối khí và không tương tác với nhau, chúng chỉ va chạm đàn hồi với tường bao quanh khối khí.



Đối với chất khí, thể tích phụ thuộc vào kích thước của bình chứa.

Phương trình trạng thái của chất khí:



Rất hữu ích để biết mối liên hệ giữa khối lượng, áp suất và nhiệt độ của khí có khối lượng m.

Phương trình mô tả sự liên hệ giữa các đại lượng này được gọi là phương trình trạng thái.

Một cách tổng quát, phương trình trạng thái là khá phức tạp. Tuy nhiên, nếu khí được duy trì ở áp suất thấp, thì phương trình trạng thái trở nên đơn giản hơn nhiều. Các phương trình trạng thái có thể được xác định từ kết quả thí nghiệm.

Khí có mật độ thấp thường được xem là khí lý tưởng. Và ta có thể dùng mô hình khí lý tưởng để đưa ra các dự đoán phù hợp để mô tả hành vi của các khí thực ở áp suất thấp.

# Mô hình khí lý tưởng

Các mô hình khí lý tưởng có thể được sử dụng để đưa ra dự đoán về các cách biến dổi của chất khí.

Nếu chất khí $\dot { \mathbf { O } }$ áp suất thấp, mô hình này mô tả đầy đủ các biến đổi của các khí thực sự.

# Mol

Lượng khí trong một thể tích nhất định được biểu diễn bởi số mol, n.

Một mol của một chất là lượng chất đó có chứa NA hạt cấu thành của chất đó. Với NA là số Avogadro: $\mathrm { N _ { A } } = 6 \ 0 2 2 \mathrm { ~ x ~ } 1 0 ^ { 2 3 }$ . Các hạt cấu thành có th $\acute { \hat { \mathbf { e } } }$ là các nguyên tử hay phân tử.

Số mol có thể được xác định từ khối lượng của các chất:

$$
n = \frac { m } { M }
$$

M là khối lượng mol của chất, có thể thu được từ bảng tuần hoàn, là khối lượng nguyên tử thể hiện trong gam/mol, m là khối lượng của mẫu, $n$ là số mol.

Ví dụ: Một người có khối lượng 4,00 u nên $\mathrm { M } = 4 { , } 0 0 \ \mathrm { g / m o l }$

# Các định luật về khí

• Khi một chất khí được giữ ở nhiệt độ không đổi, tích giữa áp suất $p$ và thể tích $V$ của nó là một hằng số hay áp suất tỷ lệ nghịch với thể tích của nó (Định luật Boyle). • Khi một chất khí được giữ ở áp suất không đổi, tỉ số giữa thể tích $V$ và nhiệt độ T không đổi hay thể tích và nhiệt độ tỉ lệ thuận với nhau (Định luật Charles và GayLussac). • Khi khối lượng của khí được giữ không đổi, tỉ số giữa áp suất $p$ và nhiệt độ $T$ không đổi hay áp suất tỷ lệ thuận với nhiệt độ (Định luật Guy-Lussac).

# Phương trình trạng thái của chất khí lý tưởng:

Phương trình trạng thái khí lý tưởng:



# ???? = ??????

$R$ là hằng số, được gọi là hằng số khí lý tưởng.

$R = 8 , 3 1 4 \mathrm { J } / \mathrm { m o l } \cdot \mathrm { K } = 0 , 0 8 2 1 4 \mathrm { ~ a t m ~ } . 1 / \mathrm { \Omega }$ $. 1 / \mathrm { m o l } \cdot \mathrm { K }$



Từ đây, bạn có thể xác định rằng 1 mol của bất kỳ chất khí ở áp suất khí quyển và $\dot { \sigma } 0 { } ^ { \mathrm { { o } } } \mathrm { C }$ là 22,4 l.

Định luật khí lý tưởng thường được viết theo tổng số của các phân tử, N, hiện diện trong mẫu.

$$
P V = n R T = ( ^ { N } / _ { ^ { \vphantom { N } } N _ { A } } ) R T = N k _ { B } T
$$



# Public_142 

Nhiệt động lực học và cơ học đã được xem là hai ngành riêng biệt của vật lý. Cho đến khoảng năm 1850, các thí nghiệm của James Joule và những người khác đã cho thấy sự liên kết giữa chúng. Mối liên kết đã được tìm thấy giữa việc trao đổi năng lượng bởi nhiệt trong các quá trình nhiệt và sự trao đổi năng lượng bởi công   
trong các quá trình cơ học.

Khái niệm về năng lượng đã được khái quát hóa để bao gồm cả nội năng.

Các nguyên lý bảo toàn năng lượng nổi lên như là một quy luật phổ quát của tự nhiên.

# Nhiệt lượng và nội năng

Trong phần này sẽ thảo luận về nội năng, nguyên lý thứ nhất của nhiệt động lực học, và các ứng dụng của nguyên lý này.

Nguyên lý thứ nhất của nhiệt động lực học mô tả các hệ mà trong đó sự thay đổi năng lượng duy nhất là nội năng. Sự trao đổi năng lượng thực hiện bởi nhiệt và công.

Ta sẽ xem xét công thực hiện bởi các hệ có thể biến dạng.

# Nội năng Eint

Nội năng là tổng năng lượng của một hệ có được từ các thành phần vi mô của nó.

The falling blocks rotate the paddles, causing the temperature of the water to increase.

• Các thành phần vi mô này là các nguyên tử và phân tử. • Hệ được quan sát từ một hệ quy chiếu đứng yên đối gắn với khối tâm của hệ.

# Nhiệt lượng Q

Nhiệt lượng được định nghĩa là năng lượng chuyển đổi qua ranh giới của một hệ do sự khác biệt nhiệt độ giữa hệ và môi trường xung quanh, được viết tắt là nhiệt.

# Đơn vị năng lượng

Trong lịch sử, calo (cal) là đơn vị được sử dụng cho năng lượng.

Một calo là lượng năng lượng trao đổi cần thiết để làm tăng nhiệt độ của 1g nước từ $1 4 . 5 ^ { \mathrm { o } } \mathrm { C }$ đến

![](images/image1.jpg)  
Hình 20.1: Thí nghiệm của Joule để xác định mối tương đương giữa cơ và nhiệt.



$1 5 . 5 \mathrm { { ^ \circ C } }$ .

1 kilocalo $= 1 0 0 0$ calo.



Theo hệ thống đo lường của Mỹ, đơn vị là một BTU (British Thermal Unit).

Một BTU là lượng năng lượng trao đổi cần thiết để làm tăng nhiệt độ 1 lb của nước từ $6 3 \mathrm { { ^ \circ F } }$ đến $6 4 \mathrm { { ^ \circ F } }$ .

Ngoài ra, đơn vị của năng lượng theo hệ SI là Joules (J)

$$
\textit { I c a l } = 4 , 1 8 6 J
$$

# Nhiệt dung riêng và phép đo nhiệt lượng

# Nhiệt dung C

Nhiệt dung, $C _ { : }$ , của một vật cụ thể được định nghĩa là lượng năng lượng cần thiết để làm tăng nhiệt độ của vật thêm $1 ^ { \circ } \mathrm { C }$ .

Nếu năng lượng Q tạo ra sự thay đổi nhiệt độ là $\Delta \mathrm { T }$ , thì

$$
\mathrm { Q } \equiv \mathrm { C } \ \Delta \mathrm { T }
$$

# Nhiệt dung riêng c

Nhiệt dung riêng, c, là nhiệt dung của mỗi khối lượng đơn vị.

Nếu trao đổi một lượng năng lượng Q để làm một vật có khối lượng m và thay đổi nhiệt độ ∆T, thì nhiệt dung riêng là:

$$
c \equiv \frac { Q } { m \Delta T }
$$

Nhiệt dung riêng của chất càng lớn, năng lượng phải thêm vào một khối lượng đã cho để tạo nên một sự thay đổi nhiệt độ cụ thể càng lớn.

Phương trình thường được viết theo thuật ngữ Q:

$$
Q = m c \Delta T
$$

# Sự thay đổi của nhiệt dung riêng theo nhiệt độ

Về mặt kỹ thuật, nhiệt dung riêng thay đổi theo nhiệt độ. Phương trình vi phân là

$$
\mathrm { T } _ { F }
$$

$$
\begin{array} { r } { 0 = \mathrm { m } \int \mathrm { c d T } } \end{array}
$$

Tuy nhiên, nếu các khoảng biến đổi nhiệt độ không quá lớn, sự thay đổi này có thể bỏ



qua và c có thể được coi như một hằng số.

# Nhiệt dung riêng của nước

Nước có nhiệt dung riêng cao nhất so với vật liệu thông thường.

# Phép đo nhiệt lượng

Muốn đo nhiệt dung riêng của một vật, ta nung nóng vật đó đến nhiệt độ $\mathrm { T _ { x } }$ , sau đó nhúng nó vào nước (khối lượng đã biết) có nhiệt độ $T _ { w } < T _ { x }$ , rồi ghi lại nhiệt độ của nước sau khi chúng cân bằng nhau. Phép đo này được gọi là phép đo nhiệt lượng. Thiết bị đo gọi là nhiệt lượng $\mathrm { k } \acute { \mathrm { e } }$ .



Hình $2 0 . 2 \ \mathrm { m } \hat { \mathrm { { o } } }$ tả vật nóng trong nước lạnh và nhiệt lượng truyền từ nhiệt độ cao đến nhiệt độ thấp. Nếu hệ vật và nước bị cô lập, sự bảo toàn năng lượng đòi hỏi nhiệt lượng thoát ra khỏi vật $\mathrm { Q } _ { \mathrm { h o t } }$ bằng với nhiệt lượng đi vào nước $\mathrm { Q _ { c o l d } }$ . Biểu thức bảo toàn năng lượng:

$$
\mathrm { Q } _ { c o l d } = - \mathrm { Q } _ { h o t }
$$

Xét một mẫu vật ta đang muốn xác định nhiệt độ. Giả sử $\mathbf { m } _ { \mathbf { X } }$ là khối lượng của nó, $\mathbf { c _ { X } }$ là nhiệt dung riêng và $\mathrm { T _ { x } }$ là nhiệt độ ban đầu. Tương tự, ta có các đại lượng mw, $\mathtt { c } _ { \mathrm { w } }$ và $\mathrm { T _ { w } }$ đại diện cho các giá trị tương ứng cho nước. Gọi $\mathrm { T _ { f } }$ là nhiệt độ cuối cùng sau khi hệ $\mathsf { \bar { g o m } }$ nước và mẫu vật) đạt trạng thái cân bằng. Phương trình (20.4) cho thấy rằng nhiệt lượng truyền cho nước là $Q _ { w } = m _ { w } c _ { w } ( T _ { f } - T _ { w } ) { > } 0$ vì $T _ { f } >$ $T _ { w }$

![](images/image2.jpg)

Hình 20.2: Trong thí nghiệm, một vật nóng có nhiệt dung riêng chưa biết được đặt trong nước lạnh trong thùng chứa cô lập với môi trường.

Nhiệt lượng truyền cho mẫu vật là $Q _ { x } = m _ { x } c _ { x } ( T _ { f } - T _ { x } ) < 0$

Từ phương trình (20.5), ta có phương trình

$$
\mathrm { m } _ { \mathrm { w } } \mathrm { c } _ { \mathrm { w } } ( \mathrm { T } _ { \mathrm { f } } - \mathrm { T } _ { \mathrm { w } } ) = - \mathrm { m } _ { \mathrm { x } } \mathrm { c } _ { \mathrm { x } } ( \mathrm { T } _ { \mathrm { f } } - \mathrm { T } _ { \mathrm { x } } ) = \mathrm { m } _ { \mathrm { x } } \mathrm { c } _ { \mathrm { x } } ( \mathrm { T } _ { \mathrm { x } } - \mathrm { T } _ { \mathrm { f } } )
$$

• Phương trình này giúp xác định nhiệt dung riêng chưa biết.

• Về mặt kỹ thuật, cần xác định khối lượng của bình chứa, nhưng nếu $m _ { \mathrm { w } } > > m _ { \mathrm { b i n h } }$ chứa , nó có thể được bỏ qua.

Bảng 20.1: Một số giá trị nhiệt dung riêng



TABLE 20.1 Specific Heats of Some Substances at $2 5 \mathrm { { ^ \circ C } }$ and Atmospheric Pressure   



Câu hỏi 20.1: Hãy tưởng tượng bạn có 1 kg sắt, thủy tinh và nước, và tất cả đều ở nhiệt độ $1 0 ^ { \circ } \mathrm { C }$ . (a) Sau khi thêm năng lượng 100J vào mỗi vật, sắp xếp các vật theo thứ tự nhiệt độ từ cao đến thấp. (b) sắp xếp các vật theo thứ tự nhiệt lượng nhận được từ nhiều đến ít nếu nhiệt độ các vật được tăng thêm $2 0 \mathrm { { } ^ { \circ } C }$ . (cd:

# Nhiệt chuyển pha

Trong một số trường hợp, mặc dù có sự trao đổi năng lượng giữa khối chất và môi trường nhưng nhiệt độ khối chất không thay đổi. Đó là khi xảy ra sự chuyển pha. Pha là một tập hợp các phần đồng tính, có tính chất như nhau của một hệ thống. Chẳng hạn nước có thể tồn tại ở pha rắn, lỏng hoặc khí. Những hình thức kết tinh khác nhau của một chất cũng là những pha khác nhau của chất đó. Sự chuyển từ pha này sang pha khác của một hệ gọi là sự chuyển pha. Nước khi hạ nhiệt độ đến $0 ^ { 0 } \mathrm { C }$ thì chuyển từ pha lỏng sang pha rắn là một ví dụ cho sự chuyển pha.

Các chất khác nhau phản ứng khác nhau đối với năng lượng truyền vào hoặc lấy đi trong quá trình chuyển pha do chúng có các sắp xếp phân tử bên trong khác nhau. Lượng năng lượng này cũng phụ thuộc vào khối lượng của chất. Khi nói đến hai pha của một chất, chúng ta sử dụng thuật ngữ chất ở pha cao hơn để chỉ chất ở nhiệt độ cao hơn. Ví dụ khi nói về hai pha của nước là nước lỏng và và nước đá thì nước lỏng là chất ở pha cao hơn.

Xét một hệ gồm hai pha của một chất đang ở trạng thái cân bằng. Gọi khối lượng ban đầu của chất ở pha cao hơn là mi. Sau khi nhận nhận nặng lượng Q khối lượng sau cùng của chất ở pha cao hơn là mf. Nhiệt chuyển pha L được định nghĩa là:



$$
L \equiv \frac { Q } { \Delta m }
$$

trong đó $\Delta m = m _ { f } - m _ { i }$ là độ biến thiên khối lượng của chất $\dot { \mathbf { O } }$ pha cao hơn. Giá trị của L phụ thuộc vào loại chuyển pha và các tính chất của chất chuyển pha.

Trong một quá trình chuyể pha, không có sự thay đổi về nhiệt độ của các chất. Nhiệt chuyển pha khi có sự chuyển pha từ rắn sang lỏng gọi là nhiệt nóng chảy. Nhiệt chuyển pha khi có sự chuyển pha từ lỏng sang khí gọi là nhiệt hóa hơi.

Nếu toàn bộ lượng vật chất ở pha thấp trải qua một sự chuyển pha, thì sự thay đổi khối lượng của vật chất ở pha cao bằng khối lượng ban đầu của vật liệu ở pha thấp. Ta cũng có thể viết lại phương trình

$$
\mathrm { Q } = \mathrm { L } \Delta \mathrm { m }
$$

Nếu năng lượng đi vào hệ:

• Sẽ dẫn đến sự nóng chảy hoặc hóa hơi • Lượng vật chất $\dot { \mathbf { O } }$ pha cao sẽ tăng • Δm và $\boldsymbol { \mathcal { Q } }$ mang dấu dương

Nếu năng lượng được rút ra khỏi hệ:

• Sẽ dẫn đến kết tinh hoặc hóa lỏng (ngưng tụ) • Lượng vật chất $\dot { \mathbf { O } }$ pha cao sẽ giảm • Δm và $\boldsymbol { \mathcal { Q } }$ mang dấu âm

Bảng 20.2: Một số giá trị của của hệ số nhiệt chuyển pha



# TABLE 20.2

Latent Heats of Fusion and Vaporization   



# Bài tập mẫu 20.2:

Tính tổng năng lượng cần cung cấp để chuyển toàn bộ 1 g nước đá $\mathrm { { \dot { \Phi } } } - 3 0 ^ { 0 } \mathrm { { C } }$ thành hơi nước ở $1 2 0 \mathrm { { } ^ { 0 } C }$ .

# Giải:

Hình $2 0 . 3 ~ \mathrm { m } \hat { \mathrm { \omega } }$ tả quá trình chuyển hóa của nước từ dạng đặc sang dạng hơi.

![](images/image3.jpg)  
Hình 20.3: Đồ thị từ nước đá sang hơi nước

Đồ thị có các phần sau

Phần A: Nước đá tăng nhiệt độ

Bắt đầu từ 1 gram nước đá $\dot { \sigma } - 3 0 \ { } ^ { \mathrm { o } } \mathrm { C }$ , trong giai đoạn A, nhiệt độ của nước đá thay đổi từ $- 3 0 \mathrm { { } ^ { \circ } C }$ đến $0 \mathrm { { ^ \circ C } }$ , dựa vào bảng 20.1, ta có phương trình ${ \mathrm { Q } } = { \mathrm { m } } _ { \mathrm { i } } { \mathrm { c } } _ { \mathrm { i } } \Delta { \mathrm { T } } =$ $( 1 \times 1 0 ^ { - 3 } ) ( 2 0 9 0 ) ( 3 0 ) = 6 2 , 7 ]$

Trong trường hợp này, hệ thu năng lượng là 62,7 J.

Phần B: băng tan

Năng lượng chuyển hóa 1g nước đá sang dạng nước (chất lỏng), dựa vào bảng 20.2, sử dụng phương trình $\mathrm { Q } = L _ { f } \Delta m _ { w } = L _ { f } m _ { i } = ( 1 \times 1 0 ^ { - 3 } ) ( 3 , 3 3 \times 1 0 ^ { 5 } ) = 3 3 3 \mid$

Năng lượng thu vào: 333 J

Phần C: nước tăng nhiệt độ

Giữa $0 \ \mathrm { { ^ \circ C } }$ và $1 0 0 ~ ^ { \mathrm { { o } C } }$ , vật liệu là chất lỏng và không có sự thay đổi trạng thái. Nước vẫn giữ nguyên pha. $\mathrm { H } \hat { \mathrm { e } }$ thu năng lượng làm tăng nhiệt độ.



Ta có $\mathrm { Q } = \mathrm { m } _ { w } \mathrm { c } _ { \mathrm { w } } \Delta \mathrm { T } = ( 1 \times 1 0 ^ { - 3 } ) ( 4 , 1 9 \times 1 0 ^ { 3 } ) ( 1 0 0 ) = 4 1 9 \ \mathrm { J }$ Năng lượng thu vào: 419 J Phần $D$ : nước sôi Tại $1 0 0 ^ { \circ } \mathrm { C }$ , sự thay đổi trạng thái xảy ra (sôi). Nhiệt độ không thay đổi.



Sử dụng $\mathrm { Q } = L _ { v } \Delta m _ { s } = ( 1 \times 1 0 ^ { - 3 } ) ( 2 , 2 6 \times 1 0 ^ { 6 } ) = 2 2 6 0 \mathrm { J }$ Năng lượng cần: 2260 J

Phần $E$ : bay hơi

Sau khi toàn bộ nước được chuyển thành hơi nước, hơi nước sẽ nóng lên. Không xảy ra thay đổi trạng thái. Hệ thu năng lượng để tăng nhiệt độ.

Khi nhiệt độ tăng từ $1 0 0 \mathrm { { ‰} }$ đến $1 2 0 \mathrm { { ‰} }$ , năng lượng cần: 40,2 J

Vậy tổng năng lượng 1gram nước đá thay đổi từ $- 3 0 \mathrm { { } ^ { \circ } C }$ đến $1 2 0 \mathrm { { } ^ { 0 } C }$ cần năng lượng tổng là 3110 J.

# Sự chậm đông

Nếu nước ở dạng lỏng được giữ đứng yên trong một bình rất sạch thì có thể giảm nhiệt độ của nước xuống dưới $0 \mathrm { { ^ \circ C } }$ mà không làm nó đóng băng. Hiện tượng này gọi là sự chậm đông.

Sự đóng băng chỉ xảy ra khi nước cần một sự nhiễu loạn theo cách nào đó để các phân tử tách nhau ra và tạo thành một cấu trúc băng rộng và mở để làm cho mật độ băng thấp hơn mật độ của nước. Nếu nước chậm động bị nhiễu loạn, nó sẽ đóng băng ngay lập tức. Hệ rơi về cấu hình năng lượng thấp của các phân tử liên kết của cấu trúc băng và năng lượng tỏa ra nâng nhiệt độ trở về $0 \ { } ^ { \mathrm { { o } } } \mathrm { { C } }$ .

# Sự quá nhiệt

Nước sạch có thể tăng nhiệt độ đến trên $1 0 0 ^ { \circ } \mathrm { C }$ mà không sôi. Hiện tượng này được gọi là sự quá nhiệt.

Sự hình thành bong bóng hơi trong nước đòi hỏi tâm hóa hơi. Tâm hóa hơi này có thể là một vết xước trên bình chứa hoặc một tạp chất trong nước. Khi bị nhiễu loạn, nước quá nhiệt có thể phát nổ. Bong bóng nước hình thành ngay lập tức, nước nóng được đẩy lên trên và trào ra ngoài bình chứa.

Câu hỏi 20.2: Giả sử có một quá trình tương tự nhằm thêm năng lượng vào cục đá như trên, nhưng thay vào đó, ta sẽ vẽ đồ thị nội năng của hệ như là một hàm của năng lượng vào. Đồ thị đó sẽ như thế nào?

Công và nhiệt trong các quá trình nhiệt động

Các biến trạng thái



Các biến trạng thái $\mathrm { m } \hat { \mathrm { o } }$ tả trạng thái của một hệ. Bao gồm: Áp suất, nhiệt độ, thể tích, nội năng.

Trạng thái của một hệ cô lập chỉ được xác định khi hệ đang $\dot { \mathbf { O } }$ trạng thái cân bằng nhiệt. Đối với chất khí trong bình chứa, mọi thành phần của chất khí phải $\dot { \mathbf { O } }$ cùng nhiệt độ và áp suất.



# Sự trao đổi năng lượng

Nhiệt lượng, $\boldsymbol { \mathcal { Q } }$ , thu vào hoặc mất đi của một hệ phụ thuộc vào quá trình biến đổi. Nguồn nhiệt là một nguồn năng lượng được xem là đủ lớn để một sự trao đổi năng lượng có giới hạn không làm thay đổi nhiệt độ của nó.

Piston được giữ cố định ở vị trí ban đầu nhờ một tác nhân bên ngoài. Bỏ qua ngoại lực tác dụng lên hệ. Piston di chuyển lên và khí sinh ra một công trên piston. Suốt quá trình giãn nở, chỉ cần năng lượng vừa đủ để chuyển hóa năng lượng nhiệt từ bình chứa sang chất khí để duy trì nhiệt độ không đổi.



# Sự chuyển hóa năng lượng, hệ cô lập

Xét chất khí trong một xy lanh có một màng như hình vẽ. Ban đầu, khí bị nhốt ở bên dưới màng ngăn $\mathrm { H } \hat { \mathrm { e } }$ hoàn toàn cách nhiệt. Khi màng bị vỡ, chất khí nhanh chóng giãn nở lấp đầy khoảng trống cho đến khi đạt được thể tích cuối cùng. Lúc này, chất khí không sinh công vì nó không tác dụng lực. Không có năng lượng được trao đổi dưới dạng nhiệt thông qua lớp vỏ cách nhiệt

![](images/image4.jpg)  
Hình 20.7: Sự trao đổi năng lượng của khí trong xylanh

Tóm lại:

• Năng lượng chuyển hóa bởi nhiệt, sinh công, phụ thuộc vào trạng thái đầu, cuối và trung gian của hệ.   
• Cả công và nhiệt đều phụ thuộc quá trình biến đổi.   
• Không thể xác định giá trị của công và nhiệt nếu chỉ dựa vào trạng thái đầu và cuối của một quá trình nhiệt động lực học.

# Nguyên lý thứ nhất của nhiệt động lực học

Nguyên lý thứ nhất của nhiệt động lực học là trường hợp đặc biệt của định luật bảo toàn năng lượng. Đó là trường hợp đặc biệt khi chỉ có sự biến đổi nội năng và chỉ có sự trao đổi năng lượng bởi nhiệt và công.

Nguyên lý thứ nhất của nhiệt động lực học

$$
\Delta E _ { i n t } = Q + W
$$

![](images/image5.jpg)



Tất cả các đại lượng phải có cùng đơn vị của năng lượng.

Một hệ quả của nguyên lý này là sự tồn tại đại lượng được biết đến như là nội năng – được xác định bởi trạng thái của hệ. Nội năng là một biến trạng thái.

Hình 20.8: Nguyên lý 1 nhiệt động lực học



Hệ cô lập là hệ không tương tác với môi trường xung quanh. Không có sự trao đổi năng lượng bằng nhiệt. Công thực hiện trên hệ bằng 0.

$$
\mathcal { Q } = W = 0 , \mathtt { n e n } \Delta E \mathrm { i n t } = 0
$$

Nội năng của hệ cô lập không đổi.

# Các chu trình

Chu trình là một tiến trình bắt đầu và kết thúc ở cùng một trạng thái.

Trên giản đồ PV, chu trình được biểu diễn như một đường cong khép kín.

Độ biến thiên nội năng bằng 0 vì nó là một biến trạng thái

Nếu $\Delta E _ { \mathrm { i n t } } = 0$ , $Q = - W$

Trong một chu trình, công thực hiện trên hệ trong mỗi chu trình có độ lớn bằng diện tích của vùng giới hạn bởi đường cong biểu diễn chu trình trên giản đồ PV.

# Một vài ứng dụng của nguyên lý thứ nhất nhiệt động lực học

### Quá trình đoạn nhiệt

Quá trình đoạn nhiệt là quá trình trong đó không có năng lượng vào hoặc ra khỏi hệ dưới dạng nhiệt.

$$
Q = 0
$$

Điều này có được do: Các thành cách nhiệt của bình, Các quá trình được thực hiện nhanh nên không có sự trao đổi nhiệt.

$$
\mathrm { V i } Q = 0 , \Delta E _ { \mathrm { i n t } } = W
$$

Nếu khí bị nén đoạn nhiệt, W mang dấu dương, $\Delta E _ { \mathrm { i n t } }$ mang dấu dương và nhiệt độ tăng.

Nếu khí giãn nở đoạn nhiệt, nhiệt độ khí giảm.

Một số ví dụ điển hình về quá trình đoạn nhiệt trong kỹ thuật:

Sự giãn nở của khí nóng trong động cơ đốt trong.   
• Khí ga hóa lỏng trong hệ thống làm mát.   
• Nén đột ngột trong động cơ diesel.

### Sự giãn nở tự do đoạn nhiệt

Đây là quá trình đoạn nhiệt vì nó diễn ra trong bình cách nhiệt. Vì chất khí giãn nở vào khoảng trống, nó không tác dụng lực lên piston và $W = 0$ .



Vì $Q = 0$ và $W { = } 0 { \Longrightarrow } \Delta E { \mathrm { i n t } } = 0$ , nghĩa là nội năng của khối khí $\dot { \mathbf { O } }$ trạng thái đầu và cuối bằng nhau.

Nếu khối khí thực hiện quá trình là khí lý tưởng thì nhiệt độ của khối khí trong quá trình này không thay đổi.



### Quá trình đẳng áp

Quá trình đẳng áp là quá trình xảy ra khi áp suất không đổi.

Có thể thực hiện bằng cách cho piston di chuyển tự do, vì vậy hệ luôn ở trạng thái cân bằng giữa lực tổng hợp từ khí đẩy lên và trọng lượng của piston cộng với lực do áp suất của không khí đẩy xuống.

Giá trị nhiệt và công nói chung đều khác 0.

Công là $W { = } { \mathcal { - P } } \left( V _ { f ^ { - } } V _ { i } \right)$ với $P$ là áp suất không đổi.

### Quá trình đẳng tích

Quá trình đẳng tích là quá trình xảy ra khi thể tích không đổi.

Thực hiện bằng cách kẹp piston $\acute { \mathbf { O } }$ vị trí cố định.

Vì thể tích không đổi, $W { = } 0$ .

Từ định luật 1, $\Delta E _ { \mathrm { i n t } } = Q$

Nếu năng lượng được truyền bởi nhiệt vào một hệ có thể tích không đổi, toàn bộ năng lượng sẽ truyền vào cho hệ và nội năng của hệ tăng lên.

### Quá trình đẳng nhiệt

Quá trình đẳng nhiệt là quá trình trong đó nhiệt độ không đổi.

Thực hiện bằng cách đặt các xylanh tiếp xúc với nguồn nhiệt có nhiệt độ không đổi.

Vì nhiệt độ không đổi, $\Delta E _ { \mathrm { i n t } } = 0$ .

Nên, $Q = - \ W$

Năng lượng bất kỳ đi vào hệ dưới dạng nhiệt phải ra khỏi hệ dưới dạng công.

![](images/image6.jpg)  
Hình 20.9: Quá trình đẳng nhiệt

Hình 20.9 mô tả giản đồ PV của quá trình giãn nở đẳng nhiệt.

Đường cong có dạng hypebol. Đường cong gọi là đường đẳng nhiệt

Phương trình:

$$
p V = n R T = \mathrm { h } \dot { \bar { \mathrm { a n g } } } \mathrm { s } \acute { \hat { 0 } }
$$

![](images/image7.jpg)



# Public_143 

# Mô hình phân tử của khí lý tưởng

Mô hình khí lý tưởng

Một số giả thiết đơn giản hóa tính chất của một hệ khí lý tưởng:

• Chất khí bao gồm một số rất lớn các phân tử. Mỗi phân tử có khối lượng và kích thước có thể bỏ qua so với khoảng cách trung bình giữa các phân tử.   
• Chuyển động của các phân tử cá thể được mô tả bằng cơ học Newton.   
• Phân tử chuyển động tự do trừ khi nó va chạm với phân tử khác hay với thành bình chứa nó. Tất cả va chạm xem là đàn hồi.   
• Bỏ qua thế năng tương tác giữa các phân tử khí.

# Số bậc tự do của phân tử khí i

Từ lý thuyết về sự phân bố đều năng lượng của hệ khí như trình bày ở trên, ta phân tích cụ thể số bậc tự do của một hệ khí bất kỳ:



• Khí đơn nguyên tử (phân tử khí có một nguyên tử): ví dụ các phân tử khí hiếm heli, neon, argon… Các phân tử khí đơn nguyên tử chuyển động tịnh tiến theo ba trục tọa độ xyz, mỗi chuyển động tịnh tiến sẽ có động năng tương ứng là $\mathbf { \Lambda } _ { I 2 k _ { B } T . }$ Chuyển động quay của phân tử khí đơn nguyên tử ứng với trục quay qua khối tâm của phân tử khí có năng lượng không đáng $\bar { \mathrm { k } } \bar { \hat { \mathbf { e } } }$ . Tóm lại, phân tử khí đơn nguyên tử có số bậc tự do $i =$ 3. Khí hai nguyên tử (hay lưỡng nguyên tử là phân tử khí có hai nguyên tử): ví dụ khí oxy, nito… Các phân tử khí lưỡng nguyên tử có ba chuyển động tịnh tiến và hai chuyển động quay quanh hai trục không đi qua hai nguyên tử của phân tử (một trục quay qua hai nguyên tử của phân tử có năng lượng không đáng kể), mỗi chuyển động này tương ứng động năng là $\prime _ { 2 } k _ { B } T .$ . Tóm lại, phân tử khí lưỡng nguyên tử có số bậc tự do $i = 5$ . Khí đa nguyên tử (phân tử khí có ba nguyên tử trở lên): Các phân tử khí đa nguyên tử có 3 chuyển động tịnh tiến và 3 chuyển động quay quanh 3 trục, mỗi chuyển động này tương ứng động năng là $\prime _ { 2 } k _ { B } T .$ . Tóm lại, phân tử khí đa nguyên tử có số bậc tự do $i =$ 6.

Tuy nhiên đối với phân tử đa nguyên tử, nhiều trường hợp i có giá trị lớn hơn do có thêm năng lượng dao động giữa các nguyên tử, phân tử.

# Nội năng của khí lý tưởng

Nội năng của một hệ khí là năng lượng bên trong hệ bao gồm động năng phân tử (năng lượng do chuyển động tự do của các phân tử), thế năng tương tác giữa các phân tử và năng lượng bên trong mỗi phân tử, nguyên tử.

Đối với khí lý tưởng, ta có thể bỏ qua thế năng tương tác giữa các phân tử do lực tương tác giữa các phân tử là rất yếu. Ngoài ra, chúng ta cũng không xét đến các quá trình biến đổi diễn ra trong từng phân tử.

Độ biến thiên nội năng của một hệ khí lý tưởng khi hệ khí thay đổi một lượng nhiệt ∆?? là:

$$
\Delta E _ { i n t } = n \frac { i } { 2 } R . \Delta T
$$

Ví dụ một vài quá trình làm thay đổi nhiệt độ của một khối khí lý tưởng như hình 21.4. Cả ba quá trình đều làm thay đổi một lượng nhiệt $\Delta T = T _ { f } - T _ { i }$ . Do $\Delta T$ là như nhau ở 3 quá trình trên nên $\Delta E _ { \mathrm { i n t } }$ cũng như nhau. Tuy nhiên công thực hiện trên chất khí là khác nhau đối với mỗi đường đi và nhiệt lượng tương ứng với mỗi đường biến đổi cũng không giống nhau. Bởi vì công và nhiệt lượng là hàm quá trình, quá trình biến đổi khác nhau thì chúng khác nhau.



# Nhiệt dung phân tử (nhiệt dung mol) của khí lý tưởng

Giả sử một khối khí lý tưởng biến đổi từ trạng thái i có các thông số $( \mathrm { { P } _ { i } , \mathrm { { V } _ { i } , \mathrm { { T } _ { i } ) } } }$ sang trạng thái $f ( \mathrm { P r } , \mathrm { V _ { f } } , \mathrm { T _ { f } } )$ có khối lượng m, phân tử gam M suy ra số mol của khối khí $\begin{array} { r } { n = \frac { m } { \dot { M } } } \end{array}$ Xét một số quá trình đặc biệt thường xảy ra như sau:

Suy ra nhiệt dung mol đẳng tích:

$$
C _ { \mathrm { V } } = { \frac { i } { 2 } } R
$$

![](images/image1.jpg)  
Hình 21.5: Năng lượng được truyền bởi nhiệt cho hệ khí theo 2 cách.

Quá trình đẳng áp: là quá trình áp suất của khí không đổi $\mathrm { P _ { i } = P _ { f } } ,$ hình 21.5 là đường thẳng nằm ngang.

• Nhiệt lượng trao đổi trong quá trình này là

$$
Q = n C _ { \mathrm { P } } \Delta T
$$

với $C _ { \mathrm { P } }$ là nhiệt dung mol đẳng áp.

• Công thực hiện trong quá trình này

$$
\begin{array} { r } { W = - \int P d V = - P \int d V = P ( V _ { i } - V _ { f } ) } \end{array}
$$

• Áp dụng nguyên lý 1 nhiệt động lực học $\Delta E _ { i n t } = W + Q$ cho quá trình đẳng tích:



$$
n \frac { i } { 2 } R . \Delta T = P ( V _ { i } - V _ { f } ) + n C _ { \mathrm { P } } \Delta T
$$

Cộng thêm từ phương trình trạng thái khí lý tưởng $P V = n R T$ thay vào phương trình trên, ta được:

$$
n \frac { i } { 2 } R . \Delta T = n R ( T _ { i } - T _ { f } ) + n C _ { \mathrm { P } } \Delta T
$$

Hay

$$
n \frac { i } { 2 } R . \Delta T = - n R \Delta T + n C _ { \mathrm { P } } \Delta T
$$

Bảng 21.2: Tỷ số nhiệt dung phân tử của một số chất khí   





# Quá trình đoạn nhiệt cho khí lý tưởng

Nhiều quá trình quan trọng diễn ra nhanh đến nỗi phần nhiệt được thêm vào cho hệ là không đáng $\mathbf { k } \acute { \hat { \mathbf { e } } }$ , đó là quá trình đoạn nhiệt. Nếu chất khí lý tưởng thực hiện một quá trình đoạn nhiệt chuẩn tĩnh, khi đó chất khí đi qua một chuỗi các trạng thái cân bằng được biểu diễn bằng đường cong trên giản $\mathtt { d \overset { \cdot } { \ o } p - \overline { { \mathtt { V } } } }$ . Ta xét một bước vô cùng nhỏ trong quá trình đoạn nhiệt $\mathrm { d Q } = 0$ .

Áp dụng định luật thứ nhất cho quá trình đoạn nhiệt:

$$
d E _ { i n t } = n C _ { V } d T = - P d V
$$

Lấy vi phân phương trình trạng thái khí lý tưởng:

$$
P V = n R T
$$

ta có

$$
P d V + V d P = n R d T
$$

![](images/image2.jpg)  
Hình 21.6: Đường biểu diễn quá trình đoạn nhiệt

# Câu hỏi lý thuyết chương 21

1. Tại sao ở cùng một nhiệt độ, lượng năng lượng trên mỗi mol của khí lưỡng nguyên tử lại lớn hơn của khí đơn nguyên tử?

2. Cái nào đậm đặc hơn: không khí khô, hay không khí bão hòa với hơi nước? Giải thích.

3. Một thùng chứa đầy khí heli và một bình khác chứa khí argon. Cả hai thùng chứa đều ở cùng nhiệt độ. Những phân tử nào có tốc độ hiệu dụng $\mathbf { V } _ { \mathrm { r m s } }$ cao hơn? Giải thích.

# Bài tập chương 21

1. Trong khoảng thời gian $3 0 ~ \mathrm { s }$ , 500 cục mưa đá tấn công tới bề mặt một cửa sổ làm bằng kính có diện tích $0 { , } 6 \mathrm { m } ^ { 2 }$ theo một góc $4 5 ^ { 0 }$ . Mỗi cục mưa đá có khối lượng $5 \mathrm { g }$ và tốc độ $8 \mathrm { m / s }$ . Giả sử các va chạm là đàn hồi, tìm (a) lực trung bình và (b) áp suất trung bình lên cửa sổ trong khoảng thời gian này.

ĐS: 0,94 N; 1,57 Pa

2. Một bình 5 lít chứa khí nitơ ở $2 7 ^ { \circ } \mathrm { C }$ và 3 atm. Tìm (a) tổng động năng chuyển động tịnh tiến của các phân tử khí và (b) động năng trung bình trên mỗi phân tử.

ĐS: 2,3 kJ; $6 { , } 2 { . } 1 0 ^ { - 2 1 }$ J

3. Trong quá trình đẳng tích, 209 J nhiệt lượng được truyền tới 1 mol khí đơn nguyên tử ở trạng thái lý tưởng, ban đầu ở 300 K. Tìm (a) công thực hiện của khí, (b) độ tăng nội năng của khí, và (c) nhiệt độ cuối cùng của nó.





4. Cho 1mol khí hydro được nung nóng ở áp suất không đổi từ 300 K đến 420 K. Tính (a) nhiệt lượng khí nhận được, (b) độ tăng nội năng của nó, và (c) công khí thực hiện .

ĐS: 3,46 kJ; 2,45 kJ; -1,01kJ

5. Một xylanh đứng với một piston nặng ở phía trên có chứa một khối không khí (xem là khí lưỡng nguyên tử) $\dot { \sigma } 3 0 0 \mathrm { K }$ . Áp suất khí ban đầu là $2 . 1 0 ^ { 5 } \mathrm { P a }$ , thể tích ban đầu $0 { , } 3 5 \mathrm { m } ^ { 3 }$ . Khối lượng mol của không khí là $2 8 , 9 \ \mathrm { g / m o l }$ . (a) Tính nhiệt dung riêng đẳng tích của khối khí theo đơn vị kJ/kg.oC. (b) Tính khối lượng của khối khí trong xylanh. (c) Giả sử piston được giữ cố định, hỏi cần truyền cho khối khí một năng lượng bằng bao nhiêu để khí tăng nhiệt độ lên 700 K. (d) Giả sử piston được tự do dịch chuyển, hỏi cần truyền cho khối khí một năng lượng bằng bao nhiêu để khí tăng nhiệt độ lên $7 0 0 \mathrm { K }$ .

ĐS: 0,719 kJ/kg.oC; 0,811 kg; 233 kJ; $3 2 7 \mathrm { k J }$ (giả sử đẳng áp)

6. Tính công cần thiết để nén 5 mol không khí ở $2 0 \mathrm { { ^ { \circ } C } }$ và 1atm đến một phần mười của thể tích ban đầu. (a) trong quá trình đẳng nhiệt? (b) trong quá trình đoạn nhiệt? (c) Tính áp suất cuối trong quá trình đẳng nhiệt? (d) Tính áp suất cuối trong quá trình đoạn nhiệt?

ĐS: $2 8 \mathrm { k J }$ ; 46 kJ; 10 atm; 25,1 atm

7. Trong quá trình sinh công của động cơ ô tô bốn thì, Piston chuyển động xuống dưới cylinder (xi-lanh) tạo ra một khoảng không trong cylinder để chứa nhiên liệu phun sương từ bộ chế hoà khí. Xem nhiên liệu gồm hỗn hợp của các sản phẩm đốt và không khí. Chúng thực hiện quá trình   
giãn đoạn nhiệt. Giả sử (1) động cơ đang chạy ở tốc độ 2500 vòng/phút; (2) áp suất đo ngay lập tức trước khi giãn nở là 20 atm; (3) thể tích của hỗn hợp ngay trước và sau khi giãn nở là $5 0 ~ \mathrm { c m } ^ { 3 }$ và $4 0 0 ~ \mathrm { c m } ^ { 3 }$ , tương ứng (Hình. P21.31); (4) khoảng thời gian cho việc giãn nỡ là một phần tư trong tổng chu kỳ; và (5) hỗn hợp hoạt động như một loại khí lý tưởng

![](images/image3.jpg)  
Figure P21.31

với tỷ lệ nhiệt cụ thể 1,4. Tìm công suất trung bình được tạo ra trong quá trình sinh công trên.

ĐS: 25 kW

# Public_144 

Trong chương này, ta sẽ bắt đầu nghiên cứu về thuyết điện từ trường. Mối liên kết đầu tiên mà ta có với các kiến thức cũ là khái niệm về lực. Lực điện từ giữa các hạt mang điện là một trong những lực cơ bản của tự nhiên. Ta bắt đầu bằng việc mô tả một số tính chất cơ bản của biểu hiện đầu tiên của lực điện từ là lực tĩnh điện. Sau đó ta sẽ nghiên cứu định luật Coulomb, một định luật chi phối tương tác điện giữa hai điện tích bất kỳ. Từ đây, ta sẽ giới thiệu khái niệm về điện trường, gắn liền với một phân bố điện tích và mô tả ảnh hưởng của nó lên các hạt mang điện khác. Ta sẽ dùng định luật Coulomb để tìm cường độ điện trường của một phân bố điện cho trước. Ngoài ra, ta cũng sẽ tìm hiểu chuyển động của một hạt mang điện trong điện trường đều.

Liên hệ thứ hai giữa thuyết điện từ với các nội dung trước đây là khái niệm về năng lượng. Nội dung này sẽ được trình bày trong chương 25

# Các tính chất của điện tích

Nhiều thí nghiệm đơn giản đã minh họa cho sự tồn tại của các lực điện. Ví dụ như khi dùng tay cọ xát một quả bóng cao su trong một ngày khô ráo thì ta có thể thấy rằng quả bóng có thể hút các mẩu giấy nhỏ. Lực hút thường là đủ lớn để làm các mẩu giấy treo lơ lửng bên dưới quả bóng.

Khi vật chất hành xử theo cách này, ta nói chúng bị nhiễm điện hay đã tích điện.

Trong một loạt thí nghiệm đơn giản, người ta tìm thấy rằng có hai loại điện tích mà Benjamin Franklin (1706–1790) gọi là điện tích dương và điện tích âm. Các electron được xem là mang điện tích âm và các proton mang điện tích dương. Để kiểm chứng sự tồn tại của hai loại điện tích, giả sử ta cọ xát một thanh cứng bằng cao su vào lông thú rồi treo nó lên trên một sợi dây như trong hình 23.1. Nếu đưa một thanh thủy tinh (đã được cọ xát vào lụa) lại gần thanh cao su thì chúng sẽ hút nhau (hình 23.1a). Mặt khác, nếu để hai thanh cao su (hoặc thủy tinh) đã nhiễm điện lại gần nhau thì chúng sẽ đẩy nhau (hình23.1b). Trên cơ sở các quan sát này, ta Biện luận rằng các điện tích cùng dấu thì đẩy nhau và các điện tích trái dấu thì hút nhau.

Mot thanh cao su tich dien àm treo trèn soi dày bi hút bòi mot thanh thiy tinh tich dièn durong.

Theo qui ước của Franklin thì điện tích trên thanh thủy tinh nói trên được gọi là điện tích dương và điện tích trên thanh cao su được gọi là điện tích âm. Vì vậy, vật tích điện nào bị hút vào thanh cao su tích điện (hoặc bị đẩy ra xa thanh thủy tinh tích điện) sẽ phải có điện tích dương.

![](images/image1.jpg)  
Mot thanh cao su tich dién àm bi dày bòi mòt thanh cao su tich dièn àm khác.

![](images/image2.jpg)  
Hình 23.1

Một khía cạnh quan trong khác về điện được rút ra từ các quan sát thực nghiệm là trong một hệ cô lập thì điện tích luôn được bảo toàn. Nghĩa là khi cọ xát vật này vào vật khác thì điện tích không được sinh ra trong quá trình này. Trạng thái nhiễm điện là do có điện tích chuyển từ vật này sang vật kia. Một vật nhận một lượng điện tích âm thì vật kia nhận một lượng điện tích dương tương ứng. Ví dụ như khi cọ xát thanh thủy tinh vào lụa thì lụa nhận một lượng điện tích âm có độ lớn bằng lượng điện tích dương mà thanh thủy tinh có được. Vận dụng hiểu biết về cấu tạo của nguyên tử thì ta có thể nói rằng trong quá trình này một số electron đã được chuyển từ thanh thủy tinh sang lụa. Tương tự như vậy, khi cọ xát cao su vào lông thú thì electron được chuyển từ lông thú sang cho cao su. Sở dĩ như vậy là do bình thường thì vật chất trung hòa về điện.



Do bào toàn dièn tích nèn mot electron sě bò sung dièn tích âm cho tám lua và mòt lrong dièn tích duong trong iíng dugc dè lai trong thanh thiy tinh

Vào năm 1909, Robert Millikan (1868–1953) khám phá ra rằng các hạt mang điện luôn luôn xuất hiện như là bội của một đện lượng e. Theo cách nói hiện đại, điện tích $q$ (ký hiệu chuẩn dùng cho điện tích) được xem là bị lượng tử hóa. Nghĩa là hạt mang điện tồn tại như là các “gói” rời rạc và ta có thể viết $q = \pm N e$ với $N$ là một số nguyên bất kỳ. Một số thí nghiệm khác vào thời gian này đã cho thấy là electron có điện tích $- e$ và proton có điện tích $+ e .$ Một số hạt khác, neutron chẳng hạn, thì không mang điện.

![](images/image3.jpg)  
Hình 23.2

Trắc nghiệm nhanh 23.1: Ba vật được đưa lại gần nhau từng đôi một. Vật A và vật B đẩy nhau. Vật B và vật C cũng đẩy nhau. Phát biểu nào sau đây có thể đúng? (a) Các vật A và C có điện tích cùng dấu. (b) Các vật A và C có điện tích trái dấu. (c) Cả ba vật này mang điện cùng dấu. (d) Một trong ba vật trung hòa về điện. (e) Cần làm thêm một vài thí nghiệm khác để xác định dấu của các điện tích.

# Nhiễm điện do cảm ứng

Việc phân loại vật chất theo khả năng di chuyển của electron trong vật chất là một cách làm thuận tiện.

Khi đó, chất dẫn điện là các vật liệu mà electron là electron tự do, không bị liên kết với các nguyên tử và có thể di chuyển tương đối tự do trong vật liệu; chất cách điện là các vật liệu mà mọi electron bị liên kết với nguyên tử và không thể di chuyển tục do trong vật liệu. Các vật liệu như thủy tinh, cao su và gỗ khô được xếp vào nhóm chất cách điện. Khi các vật liệu này bị nhiễm điện do cọ xát thì chỉ vùng bị cọ xát bị nhiễm điện và các điện tích không dịch chuyển sang các vùng khác. Ngược lại, các vật liệu như đồng, nhôm và bạc là các vật dẫn điện tốt. Khi một vùng nhỏ của các vật liệu này bị nhiễm điện thì điện tích sẽ tự phân bố trên toàn bộ bề mặt của vật chất.

Chất bán dẫn là loại vật chất thứ ba. Tính dẫn điện của nó nằm giữa chất dẫn điện và chất cách điện. Silic (Si) và germani (Ge) là những ví dụ rõ ràng về chất bán dẫn, thường dùng để sản xuất các loại vi mạch (chíp) trong máy tính, điện thoại di động và các hệ thống giải trí tại nhà. Các tính chất điện của chất bán dẫn có thể thay đổi nhiều lần bằng cách thêm vào một lượng nguyên tử của một chất khác.

Để hiểu cách làm nhiễm điện một chất dẫn điện bằng quá trình cảm ứng, ta dùng một quả cầu kim loại rỗng đặt cách điện với mặt đất như hình 23.3. Nếu điện tích của quả cầu đúng bằng 0 thì nó có một số lượng proton và electron như nhau. Khi đưa một thanh cao su nhiễm điện lại gần quả cầu, các electron ở vùng gần thanh nhất sẽ bị đẩy sang phía đối diện của quả cầu. Sự dịch chuyển này để lại một vùng mang điện dương trên quả cầu.





![](images/image4.jpg)  
Hình 23.3: Hiện tượng tích điện do cảm ứng.

a: Quả cầu có số điện tích dương và điện tích âm bằng nhau.

b: Một thanh cao su nhiễm điện được đặt gần quả cầu, không tiếp xúc với quả cầu. Các electron trong quả cầu trung hòa điện sẽ được phân bố lại.

c: Quả cầu được nối với mặt đất. Một số electron có thể rời quả cầu thông qua dây tiếp đất.

d: Bỏ dây tiếp đất. Bây giờ quả cầu sẽ có nhiều điện tích dương hơn. Điện tích không được phân bố đồng đều. Điện tích dương đã bị cảm ứng bởi quả cầu.

e: Bỏ thanh cao su. Các electron tự phân bố lại trên quả cầu. Vẫn có một tập hợp các điện tích dương trên quả cầu. Điện tích bây giờ được phân bố đồng đều trên quả cầu. Chú ý rằng thanh không mất điện tích âm trong quá trình này.

Để làm nhiễm điện một vật dẫn điện bằng cảm ứng không cần phải có sự tiếp xúc với vật cảm ứng. Điều này khác với cách làm nhiễm điện do cọ xát là cách mà cần phải có sự tiếp xúc giữa hai vật.

Một quá trình tương tự với sự cảm ứng có thể xảy ra trong vật cách điện. Trong hầu hết các phân tử trung hòa thì tâm điện âm trùng với tâm điện dương. Khi đến gần một vật mang điện, các tâm này rời xa nhau một khoảng nhỏ và làm xuất hiện điện tích âm ở một phía và điện tích dương ở phía kia. Sự sắp xếp diễn ra bên trong các phân tử này tạo ra một lớp điện tích trên bề mặt của chất cách điện như trong hình 23.4a. Từ đó làm xuất hiện lực hút giữa vật tích điện và vật cách điện. Nhờ đó ta giải thích được tại sao một thanh nhiễm điện lại có thể hút các mẩu giấy trung hòa về điện như trong hình 23.4b.



![](images/image5.jpg)  
Hình 23.4

Trắc nghiệm nhanh 23.2: Ba vật được đưa lại gần nhau, từng đôi một. Khi vật A và vật B ở gần nhau thì chúng hút nhau. Khi vật B và vật C ở gần nhau thì chúng đẩy nhau. Phát biểu nào sau đây là chắc chắn đúng? a) Vật A và C có điện tích cùng dấu. b) Vật A và C có điện tích trái dấu. c) Cả ba vật đều tích điện cùng dấu. d) Một trong ba vật trung hoà về điện. e) Cần làm thêm một vài thí nghiệm để xác định thông tin về điện tích của các vật.

# Định luật Coulomb

Charles Coulomb đã đo độ lớn của các lực điện giữa các vật tích điện bằng cân xoắn do ông chế tạo. Nguyên tắc hoạt động của cân xoắn cũng giống như thiết bị do Cavendish dùng để đo khối lượng riêng của Trái đất, trong đó, quả cầu trung hòa về điện được thay bằng một quả cầu tích điện. Lực điện giữa các quả cầu tích điện A và B trong hình 23.5 làm cho chúng hút vào nhau hoặc tách xa nhau ra. Do đó, dây treo bị xoắn lại. Vì lực xoắn của dây tỉ lệ với góc mà thanh treo quay được nên số đo góc này sẽ cho biết độ lớn của lực hút hoặc đẩy giữa các quả cầu. Lực điện có độ lớn lớn hơn nhiều so với lực hấp dẫn giữa chúng, do đó có thể bỏ qua lực hấp dẫn.



![](images/image6.jpg)

![](images/image7.jpg)  
Hình 23.5: Cân xoắn

Charles Coulomb (1736 – 1806)

Nhà vật lý người Pháp.

Charles Coulomb đã đo cường độ lực điện giữa 2 quả cầu nhỏ tích điện. Lực này tỉ lệ nghịch với bình phương khoảng cách $r$ giữa các điện tích và hướng dọc theo đường nối giữa chúng, tỉ lệ thuận với tích của các điện tích q1 và q2. Các điện tích trái dấu thì hút nhau (lực hút). Các điện tích cùng dấu thì đẩy nhau (lực đẩy).

Ông có những đóng góp lớn liên quan đến lĩnh vực tĩnh điện và từ tính.

Các lĩnh vực nghiên cứu khác •Sức bền vật liệu •Cơ học kết cấu

Trong SI, đơn vị của điện tích coulomb (C).

Trong tự nhiên giá trị điện tích nhỏ nhất là •Công thái học (Ergonomics)

$e = 1 { , } 6 0 2 1 8 \ \times \ 1 0 ^ { - 1 9 } \mathrm { C }$ . Một điện tích có độ lớn là 1 C tương ứng với 6,2460218 $\times 1 0 ^ { 1 8 }$ electron hoặc proton. Các điện tích thường gặp có giá trị khoảng vài $\mu \mathrm { C }$ .

Electron và proton giống nhau về độ lớn điện tích nhưng khác nhau về khối lượng. Proton và neutron giống nhau về khối lượng nhưng khác nhau về điện tích.

Khi sử dụng định luật Coulomb, cần nhớ rằng lực là một đại lượng vec-tơ và phải xem xét nó một cách phù hợp. Nếu biểu diễn định luật Coulomb dưới dạng vec-tơ, ta sẽ có:

$$
\vec { \mathbf { F } } _ { 1 2 } = k _ { e } \frac { q _ { 1 } q _ { 2 } } { r ^ { 2 } } \hat { \mathbf { r } } _ { 1 2 }
$$



![](images/image8.jpg)  
Hình 23.6: Lực điện tác dụng giữa các hạt mang điện

Trong đó: $\hat { \textbf { \textit { r } } _ { 1 2 } }$ là vec-tơ đơn vị, hướng từ điện tích $q _ { 1 }$ đến điện tích $q _ { 2 }$ như trong hình $2 3 . 6 _ { \cdot _ { \circ } , \vec { E } _ { 1 2 } }$ là lực điện mà điện tích $q _ { 1 }$ tác dụng lên điện tích $q _ { 2 }$ , bằng độ lớn của lực F21 (do $q _ { 2 }$ tác dụng lên điện tích $q _ { 1 }$ ).

Lưu ý về hướng của lực: Dấu của tích $q _ { 1 } q _ { 2 }$ sẽ cho biết hướng của lực điện tác dụng giữa $q _ { 1 }$ và $q _ { 2 }$ . Trong hình 23.6a, hai điện tích là dùng dấu nên lực là lực đẩy, hướng ra phía ngoài hai điện tích. Trong hình 23.6b, hai điện tích trái dấu nên lực là lực đẩy, hướng vào phía trong 2 điện tích.

Nếu có nhiều hơn 2 điện tích thì lực tác dụng giữa mỗi cặp điện tích được tính bởi (23.2). Lực tổng hợp tác dụng lên một điện tích bất kỳ sẽ bằng tổng vec-tơ của các lực tác dụng lên điện tích đó từ các điện tích còn lại. Ví dụ, nếu có 4 điện tích thì lực tổng hợp tác dụng lên điện tích thứ nhất sẽ là:



$$
\vec { \mathbf { F } } _ { 1 } = \vec { \mathbf { F } } _ { 2 1 } + \vec { \mathbf { F } } _ { 3 1 } + \vec { \mathbf { F } } _ { 4 1 }
$$

# Trắc nghiệm nhanh 23.3:

Vật A có điện tích $1 2 \mu \mathrm { C }$ và vật B có điện tích $1 6 \mu \mathrm { C }$ . Phát biểu nào dưới đây về lực điện tác dụng lên các điện tích này là đúng?

$$
\vec { \mathbf { F } } _ { \mathrm { A B } } = - 3 \vec { \mathbf { F } } _ { \mathrm { B A } } \quad \mathrm { ~  ~ \lambda ~ } _ { \mathrm { b } } ) \ \vec { \mathbf { F } } _ { \mathrm { A B } } = - \vec { \mathbf { F } } _ { \mathrm { B A } } \quad \quad \mathrm { ~  ~ \gamma ~ } \mathrm { ~  ~ c ~ } \mathrm { ~  ~ \mathrm { ~ \bf ~ 3 ~ } ~ } \vec { \mathbf { F } } _ { \mathrm { A B } } = - \vec { \mathbf { F } } _ { \mathrm { B A } } \mathrm { ~  ~ \lambda ~ } _ { \mathrm { d } } ) \ \vec { \mathbf { F } } _ { \mathrm { A B } } = 3 \vec { \mathbf { F } } _ { \mathrm { B A } }
$$

e) F = F f) 3F = F

# Bài toán mẫu 23.2:

Xét 3 điện tích điểm nằm ở 3 góc của một tam giác vuông như trong hình 23.7. Biết $q _ { 1 }$ $= q _ { 3 } = 5 { , } 0 0 \ \mu \mathrm { C } .$ $q _ { 2 } = - 2 , 0 0 ~ \mu \mathrm { C }$ và $a = 0 , 1 0 0 \mathrm { m }$ . Tìm lực tổng hợp tác dụng lên điện tích $q _ { 3 }$ .

Khái niệm hóa: Xét điện tích $q _ { 3 }$ . Vì nó nằm gần 2 điện tích còn lại nên sẽ chịu tác dụng của hai lực điện. Các lực này tác dụng theo hai hướng khác nhau (hình 23.7). Dựa vào các lực này, ta ước lượng được vec-tơ lực tổng hợp.

![](images/image9.jpg)  
Hình 23.7

Phân loại: Bài toán này thuộc dạng tính tổng vec-tơ.



$$
F _ { 2 3 x } = - F _ { 2 3 } \mathrm { c o s } ( 1 8 0 ^ { \circ } ) = - 8 , 9 9 \mathrm { N } .
$$

Từ đó tính được các thành phần của lực $\vec { \bf F } _ { 3 }$ :

$$
\begin{array} { r l } & { F _ { 3 x } = F _ { 1 3 x } + F _ { 2 3 x } = 7 , 9 4 + ( - 8 , 9 9 ) = - 1 , 0 5 \mathrm { N } } \\ & { F _ { 3 y } = F _ { 1 3 y } + F _ { 2 3 y } = 7 , 9 4 + 0 = 7 , 9 4 \mathrm { N } . } \end{array}
$$

Tức là: $\vec { \mathbf { F } _ { 3 } } = ( - 1 , 0 4 \mathbf { \hat { i } } + 7 , 9 4 \mathbf { \hat { j } } ) \mathbf { N }$

Biện luận: Lực tổng hợp tác dụng lên điện tích $q _ { 3 }$ hướng chéo lên phía trên, sang trái.

Biện luận: Về mặt toán học, phương trình nói trên có thể có một nghiệm khác là x = −3,44 m nhưng không phù hợp với bài toán. $\dot { \mathrm { ~ O ~ } }$ tọa độ này, hai lực tác dụng lên q3 cùng chiều nên không thể triệt tiêu lẫn nhau.

# Hạt trong điện trường

Trong trường hợp các lực điện, Faraday đã phát triển khái niệm về trường. Theo hướng tiếp cận này, một điện trường được cho là tồn tại trong vùng không gian xung quanh các vật tích điện, điện tích nguồn. Có thể phát hiện ra sự tồn tại của điện trường bằng cách đặt một điện tích thử vào trong trường đó và xem xét lực điện tác dụng lên nó. Ví dụ, trong hình 23.10 là một điện tích thử dương

![](images/image10.jpg)  
Hình 23.10: Điện tích thử đặt gần điện tích nguồn.

Nếu đặt một điện tích $q$ bất kỳ vào điện trường thì nó sẽ chịu một lực điện cho bởi:

$$
\vec { \bf F } = q \vec { \bf E } \left( 2 3 . 4 \right)
$$

Nếu $q$ dương, lực điện và điện trường cùng chiều nhau. Nếu $q$ âm, lực điện và điện trường ngược chiều nhau.

Công thức (23.4) có sự tương tự với công thức của vật trong trường trọng lực ${ \vec { \mathbf { F } } } = m { \vec { \mathbf { g } } } $ . Công thức này được dùng để tìm lực điện tác dụng lên một điện tích bất kỳ tại một vị trí mà ở đó đã biết điện trường.

Áp dụng định luật Coulomb ta tìm được lực điện tác dụng bởi điện tích điểm $q$ lên điện tích thử $q _ { 0 }$ đặt gần nó:

$$
{ \vec { \mathbf { F } } } = k _ { e } { \frac { q q _ { 0 } } { r ^ { 2 } } } { \hat { \mathbf { r } } }
$$

Từ đó, điện trường tại điểm đặt điện tích thử q0 sẽ là:



$$
\vec { \bf E } = k _ { e } \frac { q } { r ^ { 2 } } \hat { \bf r }
$$

Nếu điện tích $q$ dương, lực hướng ra xa $q$ . Điện trường hướng ra xa điện tích nguồn dương. Nếu $q$ âm, lực hướng lại gần $q$ . Điện trường hướng lại gần điện tích nguồn âm.

![](images/image11.jpg)  
Hình 23.11: Lực điện và điện trường do các điện tích khác nhau tạo ra

Để tính điện trường tại $\mathrm { m } \hat { \mathrm { 0 t } }$ điểm $P$ do một số hữu hạn điện tích điểm gây ra thì ta lần lượt áp dụng công thức (23.5) cho mỗi điện tích điểm $q _ { \mathrm { i } }$ rồi lấy tổng vec-tơ các điện trường thành phần này:

$$
\vec { \mathbf { E } } = k _ { e } \sum _ { i } \frac { q _ { i } } { r _ { i } ^ { 2 } } \hat { \mathbf { r } } _ { i }
$$

# Trắc nghiệm nhanh 23.4:

Một điện tích $+ 3 ~ \mu \mathrm { C }$ được đặt tại $\mathrm { d i e m } \ : P$ thì nó chịu tác dụng bởi một lực điện từ bên ngoài, hướng sang phải và có độ lớn $4 \times 1 0 ^ { 6 } \mathrm { N } / \mathrm { C }$ . Nếu thay điện tích này bằng một điện tích $- 3 ~ \mu \mathrm { C }$ thì lực điện tác dụng lên điện tích này sẽ thế nào? (a) Không bị ảnh hưởng gì; (b) Đổi hướng; (c) Lực bị thay $\mathbf { \bar { d } } \hat { \mathbf { o } } \mathbf { i }$ theo một cách không thể xác định được.

Bài toán mẫu 23.5: Một giọt nước nhỏ có khối lượng $3 , 0 0 \times 1 0 ^ { - 1 2 } \mathrm { k g }$ nằm gần mặt đất, trong không khí vào một ngày mưa bão. Một điện trường trong khí quyển có hướng thẳng đứng từ trên xuống và có độ lớn là $6 { , } 0 0 \times 1 0 ^ { 3 } \mathrm { N / C }$ trong vùng có giọt nước. Giọt nước nằm lơ lửng trong không khí. Hỏi điện tích của giọt nước là bao nhiêu?

Khái niệm hóa: Hình ảnh một giọt nước nằm lơ lửng trong không khí là không bình thường. Vậy phải có cái gì đó kéo giọt nước lên để nó không rơi xuống.

Phân loại: Bài toán này thuộc dạng bài toán cân bằng của hạt trong điện trường và trong trường hấp dẫn.

Phân tích: Từ điều kiện cân bằng của giọt nước ta có lực điện tác dụng vào giọt nước cùng phương, ngược chiều với trọng lực tác dụng lên nó: $F _ { e } = m g$ . Từ đó, ta tìm được độ lớn của điện tích là: q = mg . Do điện trường hướng thẳng đứng



$E$ xuống dưới và lực điện hướng lên trên nên điện tích của giọt nước là âm.



# Đáp số: q = −4,90  10−15 C

Bài toán mẫu 23.6: Điện trường do hai hạt mang điện tạo ra Hai điện tích $q _ { 1 }$ và $q _ { 2 }$ được đặt trên trục $x$ và lần lượt cách trục một khoảng là $a$ và $b$ . (A) Tìm các thành phần của điện trường tổng hợp tại điểm $P$ nằm tại vị trí $( 0 , y )$ .

(B) Xét trường hợp đặc biệt khi các điện tích này cùng độ lớn và $a = b$ .

(C) Xét trường hợp $P$ nằm rất xa $\mathrm { g } \acute { \mathrm { o c } }$ tọa độ, tức là $\mathbf { y } > > \mathbf { a }$

Giải:

![](images/image12.jpg)  
Hình 23.12

Khái niệm hóa: Trong bài toán này, điện trường tổng hợp do hai điện tích điểm tạo ra ở $P$ là tổng vec-tơ của điện trường do mỗi điện tích tạo ra.

Phân loại: Đây là bài toán mà ta sử dụng công thức (23.6) để giải.

# Phân tích:

a) Điện trường do $q _ { 1 }$ và $q _ { 2 }$ gây ra tại $P$ được chỉ ra trong hình 23.12. Độ lớn của chúng lần lượt là:

$$
E _ { 1 } = k _ { e } \frac { \left| q _ { 1 } \right| } { r _ { 1 } ^ { 2 } } = k _ { e } \frac { \left| q _ { 1 } \right| } { e ^ { 2 } + y ^ { 2 } } ; E _ { 2 } = k _ { e } \frac { \left| q _ { 2 } \right| } { r _ { 2 } ^ { 2 } } = k _ { e } \frac { \left| q _ { 2 } \right| } { b ^ { 2 } + x ^ { 2 } }
$$

Biểu diễn các điện trường này dưới dạng vec-tơ:

$$
\begin{array} { l } { { \displaystyle { \vec { \bf E } } _ { 1 } = k _ { e } \frac { \left| q _ { 1 } \right| } { a ^ { 2 } + y ^ { 2 } } \cos \hat { \mathrm { \bf ~ i } } + k _ { e } \frac { \left| q _ { 1 } \right| } { a ^ { 2 } + y ^ { 2 } } \mathrm { s i n } \Phi \hat { \mathrm { \bf ~ j } } } ; } \\ { { \displaystyle } } \\ { { \displaystyle { \vec { \bf E } } _ { 2 } = k _ { e } \frac { \left| q _ { 2 } \right| } { b ^ { 2 } + y ^ { 2 } } \cos \theta \hat { \mathrm { \bf ~ i } } = k _ { e } \frac { \left| q _ { 2 } \right| } { b ^ { 2 } + y ^ { 2 } } \mathrm { s i n } \theta \hat { \mathrm { \bf ~ j } } } } \end{array}
$$

Từ đó tìm được các thành phần của điện trường tổng hợp:



b) Trong trường hợp hai điện tích bằng nhau về độ lớn và $a = b$ thì các kết quả trên sẽ trở thành:

$$
E _ { x } = k _ { e } \frac { 2 \left| \boldsymbol { q } \right| } { a ^ { 2 } + y ^ { 2 } } \mathrm { c o s } \theta = k _ { e } \frac { 2 a \left| \boldsymbol { q } \right| } { \left( a ^ { 2 } + y ^ { 2 } \right) ^ { 3 / 2 } } \mathrm { v } \dot { \mathrm { a } } E _ { y } = 0
$$



c) Nếu y $> >$ a thì kết quả trên sẽ là: $E _ { x } \approx k _ { e } { \frac { 2 a \left| q \right| } { y ^ { 3 } } }$

trong đó tích phân được lấy trên toàn bộ phân bố điện. Tích phân này là một phép toán vec-tơ nên phải có cách tính phù hợp. Ta phải tính theo các thành phần tọa độ của hệ trục tọa độ không gian tương ứng với phân bố điện.

Các phân bố điện thường gặp là phân bố theo một đường, phân bố theo mặt và phân bố theo khối. Để thuận tiện trong tính toán, ta thường sử dụng khái niệm mật độ điện tích. Giả sử điện tích được phân bố đều (đồng nhất) thì:

- Đối với phân bố theo khối:  ρ  $\rho \equiv { \frac { Q } { \ d r } }$ ; tỉ số giữa tổng điện tích và thể tích của vật.   
Đơn vị của  là $\mathrm { C } / \mathrm { m } ^ { 3 }$ .   
Đối với phân bố theo mặt: $\sigma \equiv { \frac { Q } { \ A } }$ ; tỉ số giữa tổng điện tích và diện tích của vật.   
Đơn vị của $\sigma$ là $\mathrm { C } / \mathrm { m } ^ { 2 }$ .

- Đối với phân bố theo đường: $\lambda \equiv \frac { Q } { \ell }$ ; tỉ số giữa tổng điện tích và độ dài của vật Đơn vị của $\lambda$ là $\mathrm { C } / \mathrm { m }$ .

Nếu phân bố điện không đều (đồng nhất) thì điện lượng của một vi phân th $\hat { \dot { \mathbf { e } } }$ tích, diện tích và độ dài sẽ lần lượt là:

$$
d q = \rho d V d q = \partial d q = d \mathcal { A } d q = d \mathcal { A } d q = \lambda d \mathcal { \ell }
$$



# Chiến lược giải toán

1. Khái niệm hóa: Thiết lập một hình ảnh trong đầu về bài toán: suy nghĩ về các điện tích riêng biệt hoặc một phân bố điện và tưởng tượng về dạng điện trường mà chúng có thể tạo ra. Xem xét tính đối xứng của các hệ điện tích để hình dung về điện trường.

2. Phân loại: Bài toán đề cập đến hệ điện tích điểm rời rạc hay một phân bố điện liên tục? Tìm được câu trả lời cho câu hỏi này thì ta sẽ biết cách làm tiếp theo trong phần phân tích.

# Phân tích

(a) Nếu là một nhóm các điện tích riêng lẻ: Sử dụng nguyên lý chồng chất, tìm các điện trường do những điện tích riêng gây ra tại điểm khảo sát, rồi cộng chúng lại như các vec-tơ để tìm ra điện trường tổng hợp. Chú ý số lượng các vec-tơ.

(b) Nếu là một phân bố điện tích liên tục: Tổng vec-tơ để đánh giá điện trường tổng hợp tại một điểm phải được thay thế bằng tích phân vec-tơ. Chia phân bố điện tích thành nhiều phần tử nhỏ, tính vec-tơ tổng bằng cách lấy tích phân trên toàn bộ miền phân bố điện tích đó.

Lưu ý về tính đối xứng của hệ điện tích để đơn giản hóa tính toán. Sự khử của các thành phần điện trường trong bài toán mẫu 23.8 là một minh họa cho việc áp dụng tính đối xứng.

# Biện luận

- Kiểm tra xem biểu thức của điện trường có phù hợp với hình dung ban đầu hay không và có phản ánh tính đối xứng mà ta đã lưu ý trước đó không.

- Hình dung sự thay đổi các thông số để xem kết quả tính toán có thay đổi một cách hợp lý hay không.

Bài toán mẫu 23.9: Điện trường của một đĩa tròn tích điện đều

Một đĩa tròn bán kính $R$ với mật độ điện tích s. Hãy tính điện trường tại một điểm $P$ nằm trên trục của đĩa và cách tâm đĩa một khoảng $x$ (hình 23.16).

# Giải:

Khái niệm hóa: Nếu xem đĩa như là một tập hợp các vòng tròn xếp kề nhau thì ta có thể sử dụng kết quả của bài toán mẫu 23.8 – điện trường do một vòng tròn bán kính $a$ tạo ra – và tính tổng đối với tất cả các vòng tạo nên đĩa.

![](images/image13.jpg)

Phân loại: Vì đĩa là một vật liên tục nên ta phải tìm điện trường đối với một phân bố liên tục.

Phân tích: Trước tiên, cần tìm điện tích dq của một phần diện tích có dạng một vành tròn có bán kính trong là $r$ và bề rộng dr như trong hình 23.16:



$$
d q = \sigma d A = \sigma \left( 2 \pi r d r \right) = 2 \pi \sigma r d r .
$$

# ĐƯỜNG SỨC ĐIỆN TRƯỜNG

Trong các phần trước ta đã định nghĩa điện trường bằng biểu diễn toán học với phương trình (23.3). Bây giờ ta sẽ tìm cách trực quan hóa điện trường bởi một biểu diễn bằng hình ảnh. Một cách thuận tiện để trực quan hóa các mẫu điện trường là vẽ các đường gọi là đường sức điện trường (được Faraday giới thiệu đầu tiên). Đường sức điện trường có một số tính chất sau:

$^ +$ Vec-tơ điện trường tiếp tuyến với đường sức điện trường tại mỗi điểm. Hướng của đường sức cùng hướng với vec-tơ điện trường.



$+ \mathrm { \ S \hat { \rho } }$ đường sức đi qua một đơn vị diện tích bề mặt vuông góc với các đường sức tỉ lệ thuận với độ lớn của điện trường trong khu vực đó. Nếu các đường sức nằm sát nhau thì $\dot { \mathbf { O } }$ đó điện trường mạnh, nếu các đường sức nằm xa nhau thì điện trường ở đó yếu.

Các tính chất này được thể hiện trên hình 23.17. Mật độ của các đường sức đi qua mặt A lớn hơn mật độ của các đường sức đi qua mặt B. Do đó, điện trường ở mặt A lớn hơn ở mặt B. Ngoài ra, vì các đường sức ở các vị trí khác nhau có hướng khác nhau nên điện trường này là không đều.

Ta có thể kiểm chứng được rằng mối quan hệ giữa cường độ điện trường với mật độ của đường sức là phù hợp với công thức (23.5) (công thức tìm điện trường từ định luật Coulomb).

![](images/image14.jpg)  
Hình 23.17

Hình 23.18 cho thấy các đường sức biểu diễn cho điện trường của điện tích điểm trong không gian 2 chiều. Các đường sức này là các đường xuyên tâm, xuất phát từ điện tích điểm. Nếu điện tích là dương thì các đường sức hướng ra xa điện tích. Nếu điện tích là âm thì các đường sức hướng ra xa điện tích. Trong cả hai trường hợp, đường sức là dài vô hạn.

![](images/image15.jpg)  
Hình 23.18

Dưới đây là một số qui tắc để vẽ đường sức:

$^ +$ Đường sức phải xuất phát từ điện tích dương và kết thúc ở điện tích âm. Trong trường hợp số điện tích âm và dương khác nhau thì một số đường có thể xuất phát hoặc kết thúc ở rất xa.

+ Số đường sức đi vào hoặc ra khỏi một điện tích tỉ lệ với độ lớn của điện tích đó.   
$^ +$ Các đường sức không được cắt nhau.

Hình 23.19 cho thấy các đường sức đối với hệ hai điện tích điểm cùng độ lớn nhưng trái dấu (a); hai điện tích điểm dương, cùng độ lớn (b) và hệ $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ hai điện tích $2 q$ và $- q$   





(c). Hệ gồm hai điện tích điểm cùng độ lớn nhưng trái dấu được gọi là một lưỡng cực điện.

![](images/image16.jpg)  
Hình 23.19: Đường sức điện trường của các hệ điện tích điểm khác nhau

Trắc nghiệm nhanh 23.5: Trong hình 23.19, hãy xếp hạng độ lớn điện trường tại các điểm A, B và C theo thứ tự giảm dần.

# Chuyển động của hạt mang điện trong điện trường đều

Khi một hạt mang điện được đặt trong một điện trường, nó sẽ chịu một lực điện. Nếu đây là lực duy nhất đặt trên hạt mang điện thì nó chính là lực tổng hợp. Lực này sẽ gây ra gia tốc cho hạt theo định luật II Newton. Do đó

$$
\vec { \bf a } = \frac { q \vec { \bf E } } { m }
$$

Nếu điện trường là đều (có độ lớn và hướng không đổi) và hạt chuyển động tự do thì lực tác dụng lên hạt là không đổi. Ta có thể áp dụng mô hình hạt chuyển động với gia tốc không đổi đối với chuyển động của hạt mang điện. Nghĩa là trong trường hợp này, có thể dùng $3 ~ \mathrm { m } \hat { \mathrm { { o } } }$ hình cho chuyển động của hạt trong điện trường đều: hạt chuyển động trong một trường lực, hạt chuyển động dưới tác dụng của lực tổng hợp và hạt chuyển động với gia tốc không đổi.

Nếu hạt mang điện tích dương, gia tốc của nó hướng theo điện trường. Nếu hạt mang điện tích âm, gia tốc của nó ngược chiều với điện trường.

Bài toán mẫu 23.10: Electron trong điện trường đều

Một điện trường đều $\vec { \bf E }$ giữa hai bản tích điện đặt song song cách nhau một khoảng d có hướng dọc theo trục $x$ như trong hình 23.20. Một hạt mang điện dương $q$ và có khối lượng m được thả không vận tốc đầu tại điểm A gần bản dương và chuyển động nhanh dần về điểm $B$ gần bản âm.

A) Hãy tìm tốc độ của hạt tại $B$ bằng cách xem hạt mang điện như là một hạt chuyển động với gia tốc không đổi.



Giải:

Khái niệm hóa: Khi hạt mang điện dương ở tại điểm A, nó chịu tác dụng của lực điện hướng sang phải (cùng chiều với điện trường). Kết quả là nó sẽ chuyển động nhanh dần về B.

Phân loại: Có th $\dot { \hat { \mathrm { ~ e ~ } } } \mathrm { m } \hat { \mathrm { ~ } }$ hình hóa chuyển động của hạt như là hạt chuyển động với gia tốc không đổi.

Phân tích: Dùng phương trình của hạt chuyển động với gia tốc không đổi thể hiện quan hệ giữa tốc độ, gia tốc và vị trí của hạt:

$$
\nu _ { _ { f } } ^ { 2 } = \dot { \nu } _ { _ { f } } ^ { 2 } + 2 a \left( x \ _ { _ { f } } - x \ _ { _ { i } } \right) = 2 a d
$$

Ta tìm được

![](images/image17.jpg)  
Hình 23.20



$$
\nu _ { f } = \sqrt { 2 a d } = \sqrt { 2 \frac { q E } { m } d } = \sqrt { \frac { 2 q E d } { m } }
$$

B) Tìm tốc độ của hạt mang điện tại $B$ bằng cách xem hạt như là một hệ không cô lập theo phương pháp năng lượng

Phân loại: Phát biểu của bài toán cho ta biết rằng hạt mang điện là một hệ không cô lập $\nu \dot { \hat { e } }$ năng lượng. Lực điện sẽ thực hiện công lên hệ. Năng lượng được truyền vào hệ bởi công do lực điện tác dụng lên hạt. Cấu hình ban đầu của hệ là khi hạt ở trạng thái đứng yên tại $A$ và cấu hình cuối của hệ là khi hạt có tốc độ nào đó tại $B$ .

Phân tích: Viết phương trình của định lý công – động năng: $W = \Delta K$ Thay biểu thức của công và động năng ứng với các vị trí $A$ và $B$ : F d =  mv2 . Từ đó tìm ra kết quả đã có ở phần A). $F \dot { d } = \frac { 1 } { 2 } m \nu ^ { 2 } { } _ { f }$

# Public_145 

Điện trường đã được nghiên cứu $\mathbf { v } \dot { \hat { \mathbf { e } } }$ phương diện tác dụng lực trong các chương trước. Trong chương này, điện trường sẽ được khảo sát ở khía cạnh năng lượng. Bằng cách tiếp cận theo hướng năng lượng, các bài toán có thể được giải theo hướng không cần đến việc sử dụng lực. Khái niệm về thế năng có giá trị lớn trong   
các nghiên cứu về điện. Do lực tĩnh điện là lực bảo toàn, hiện tượng tĩnh điện có thể được mô tả một cách dễ dàng dưới dạng năng lượng điện thế.

# Điện thế và hiệu điện thế

Khi một điện tích $q$ đặt trong điện trường ${ \overrightarrow { E } } .$ , nó sẽ chịu tác dụng một lực bằng ${ \overrightarrow { F } } = q { \overrightarrow { E } } .$ Đây là lực bảo toàn bởi vì theo bản chất, các tương tác đều tuân theo định luật Coulomb. Hãy xem xét dưới góc độ một hệ kín các điện tích, khi điện tích $q$ chuyển động chỉ dưới tác dụng của các điện tích còn lại. Với một chuyển dời vô cùng bé $\overrightarrow { d s }$ , trường lực thế Coulomb sinh một công bằng ${ \overrightarrow { F } } \cdot { \overrightarrow { d s } }$ . Trong cơ học ta biết rằng, công do trường lực thế sinh ra bằng đúng độ suy giảm thế năng, cho nên:

$$
- d U = \overrightarrow { F } \cdot \overrightarrow { d s }
$$

Khi điện tích $q$ di chuyển từ vị trí A đến vị trí B trong điện trường, độ biến thiên thế năng bằng:

$$
\Delta U = - \int _ { ( A ) } ^ { ( B ) } \overrightarrow { F } \cdot \overrightarrow { d s } = - q \int _ { ( A ) } ^ { ( B ) } \overrightarrow { E } \cdot \overrightarrow { d s }
$$

$\mathring { \mathrm { O } }$ đây tích phân đường tính dọc theo quỹ đạo di chuyển của điện tích $q$ từ A đến B. Tuy nhiên vì trường lực bảo toàn nên dù đi theo con đường nào, giá trị của tích phân này cũng không thay đổi.

Khi đã có biểu thức tính độ biến thiên thế năng, chỉ cần chọn một điểm O nào đó làm gốc thế năng ( $U = 0$ ), ta đã có thể tính thế năng của điện tích đặt trong điện trường:

$$
U = - q \int _ { ( \mathrm { \diamond } ) } ^ { ( \mathrm { P } ) } \longrightarrow \longrightarrow ( \mathrm { \diamond } ) \stackrel { ( 0 ) } { \cal E } \cdot \longrightarrow 
$$

Thế năng của điện tích $q$ tại vị trí P bất kì trong điện trường có trị số bằng công của lực điện trường làm di chuyển điện tích $q$ đó từ $P \nu \dot { \hat { e } }$ gốc thế năng.

Thế năng tại vị trí P của một đơn vị điện tích trong điện trường $\overrightarrow { E }$ được gọi là điện thế tại điểm đó:



Điện thế tại vị trí $P$ bất kì trong điện trường có trị số bằng công của lực điện trường làm di chuyển điện tích 1 Coulomb từ $\dot { P } \nu \dot { \hat { e } }$ gốc điện thế (gốc thế năng).

Tương tự như độ biến thiên thế năng $\Delta U$ ta cũng có khái niệm hiệu điện thế giữa hai điểm B và A:

$$
\Delta V = V _ { B } - V _ { A } = - \int _ { ( A ) } ^ { ( B ) } { \overrightarrow { E } } \cdot { \overrightarrow { d s } }
$$

Từ (25.1) và (25.3), ta $\mathrm { c o } \mathrm { m } \acute { \mathrm { o } } \mathrm { i }$ liên hệ giữa độ biến thiên thế năng và hiệu điện thế:

$$
\Delta U = q \Delta V
$$

Theo định luật bảo toàn năng lượng: $\Delta U + \Delta K = 0$ , suy ra động năng mà điện tích q thu được khi di chuyển từ điểm A đến điểm B nói trên bằng độ suy giảm của thế năng:

$$
\Delta K { = } { - } \Delta U { = } { - } q \Delta V { = } q ( V _ { \it A } { - } V _ { \it B } )
$$

Điện thế và hiệu điện thế có thứ nguyên của năng lượng trên một đơn vị điện tích, được gán cho một đơn vị đặc biệt trong hệ SI – Volt: $1 \mathrm { V } = 1 \mathrm { J } / \mathrm { C }$ .

Mối liên hệ (25.2), (25.3) cũng cho ta một đơn vị khác của cường độ điện trường là $\mathrm { V } / \mathrm { m }$ $1 \mathrm { N } / \mathrm { C } = 1 \mathrm { V } / \mathrm { m }$ .

Khi một electron mang điện tích nguyên tố $- e$ chuyển động dưới tác dụng của điện trường, đi qua đoạn đường có hiệu điện thế bằng 1V, ta nói rằng electron đã thu được thêm động năng bằng 1 electron-volt:

$$
1 e V = 1 , 6 { \times } 1 0 ^ { - 1 9 } C \cdot 1 V = 1 , 6 { \times } 1 0 ^ { - 1 9 } J
$$

Câu hỏi 25.1: Hai điểm A và B nằm trong một điện trường như hình 25.1. (i) Hiệu điện thế $\Delta V _ { \widehat { \mathbf { C } } } {  } V _ { B } - V _ { A }$ có giá trị như thế nào? (a) dương (b) âm (c) bằng không. (ii) Một điện tích âm ban đầu nằm tại A, sau đó di chuyển đến vị trí B. Sự biến thiên của thế năng U có giá trị như thế nào? Lựa chọn trong các khả năng như phần trước.

![](images/image1.jpg)  
Hình 25.1: Hai điện tích điểm trong điện trường

# Hiệu điện thế trong điện trường đều

Ta tiến hành khảo sát một điện trường đều, theo đó các đường sức điện trường hướng song song và đều đặn như miêu tả trên hình 25.2a. Từ phương trình (25.3) suy ra được hiệu điện thế giữa hai điểm A và B nằm trên cùng một đường sức điện trường:



![](images/image2.jpg)

Hình 25.2: (a) Hạt mang điện tích $q$ chuyển động dọc theo đường sức điện trường đều (b) Hạt khối lượng m rơi trong trường trọng lực đều.

$$
{ \Delta } V = V - V = - \int \stackrel { ( B ) } { E } \overleftrightarrow { E } \cdot \overrightarrow { d s } = - \int \displaylimits _ { ( A ) } ^ { ( B ) } E \cdot { d s } \cdot \cos ( 0 ^ { 0 } ) = - \sum \op _ { ( A ) } ^ { ( \pm ) } E \cdot { d s }
$$

Trong điện trường đều $E$ có độ lớn không đổi nên có thể đưa ra ngoài dấu tích phân:

$$
\Delta V = - E \int _ { ( A ) } ^ { ( B ) } d s
$$

$$
\Delta V = - E d
$$

Dấu “–“ ở đây nói rằng, điện thế tại B thấp hơn điện thế tại A: $V _ { B } < V _ { A }$ . Như vậy, các đường sức điện trường luôn hướng theo chiều suy giảm của điện thế.

Khi một điện tích $q$ di chuyển từ A đến B, thế năng của hạt trong điện trường thay đổi một lượng bằng

Có nghĩa nếu hạt mang điện tích dương: $q > 0$ , thế năng sẽ giảm: U  0. Nói cách khác, khi một điện tích dương di chuyển xuôi theo chiều của đường sức điện trường, thế năng của nó sẽ giảm. Như hình 25.2a miêu tả, nếu ban đầu hạt mang điện tích dương $q$ thả tự do từ trạng thái đứng yên, nó sẽ chịu tác dụng một lực ${ \overrightarrow { F } } = q { \overrightarrow { E } }$ hướng xuống dưới, bắt đầu đi xuống và tăng tốc. Hạt dần thu động năng từ chính sự suy giảm của thế năng. Đó là minh chứng rõ ràng cho định luật bảo toàn năng lượng.

Hình 25.2b miêu tả hình ảnh tương tự, khi một hạt khối lượng $m$ rơi tự do trong trường hấp dẫn gần mặt đất. Hạt cũng chịu tác dụng của trọng lực hướng xuống và tăng tốc. Động năng tích luỹ tự sự suy giảm của thế năng trọng trường.



Phép so sánh nói trên giữa hạt mang điện tích dương trong điện trường với hạt chuyển động dưới trường trọng lực rất hữu ích cho việc hình dung về các hiện tượng tĩnh điện. Chỉ một điểm lưu ý rằng: khối lượng thì luôn dương, nhưng điện tích có thể dương, cũng có thể âm.



Với trường hợp điện tích âm, khi hạt di chuyển theo chiều của đường sức điện trường, thế năng của hạt sẽ tăng, thay vì giảm. Nếu ban đầu hạt đứng yên, nó sẽ tăng tốc về phía ngược chiều của đường sức.

Ta khảo sát trường hợp tổng quát hơn, khi hạt mang điện tích di chuyển từ vị trí A đến vị trí B trong điện trường đều, nhưng không nằm trên cùng một đường sức như hình 25.3. Lúc này hiệu điện thế giữa A và B bằng:

$$
\Delta V = V _ { _ { B } } - V _ { _ { A } } = - \int _ { ( A ) } ^ { ( B ) } \stackrel { \longrightarrow } { { \cal E } } \cdot \stackrel { \longrightarrow } { d s } = - \stackrel {  } { { \cal E } } \cdot \int \stackrel { ( B ) } { d s } = - \stackrel { \longrightarrow } { { \cal E } } \cdot s
$$

$\mathring { \mathrm { O } }$ đây vector $\overrightarrow { E }$ của điện trường đều có thể đưa ra ngoài dấu tích phân. Độ biến thiên của thế năng:

$$
\Delta U = q \Delta V = - q \overrightarrow { E } \cdot \overrightarrow { s }
$$

![](images/image3.jpg)

Tích vô hướng (25.8) có thể tính qua hình học:

$$
\Delta V = V _ { \scriptscriptstyle B } - V _ { \scriptscriptstyle A } = - E d
$$

Mặt khác hiệu điện thế giữa hai điểm A và C nằm trên cùng một đường sức:

Hình 25.3: Hạt mang điện tích chuyển động không

$$
V _ { \mathrm { ~ } } - V _ { \mathrm { ~ } } = - E d
$$

song song với đường sức của điện trường đều

Từ đây suy ra rằng $V _ { B } = V _ { C }$ . Tổng quát lên có thể thấy rằng, mọi điểm nằm trên cùng một mặt phẳng vuông góc với đường sức điện trường đều có cùng một điện thế. Ta gọi mặt phẳng chứa tất cả các điểm có cùng điện thế như vậy là một mặt đẳng thế. Đối với điện trường đều, họ các mặt đẳng thế cấu thành từ những mặt phẳng song song với nhau và cùng vuông góc với các đường sức điện trường.

![](images/image4.jpg)  
Hình 25.4: Các mặt đẳng thế



Câu hỏi 25.2: Các điểm được đánh dấu trên hình 25.4 nằm trên các mặt đẳng thế. Hãy sắp xếp công thực hiện của điện trường lên một điện tích dương theo thứ tự giảm dần, khi điện tích này di chuyển từ A sang B, từ B sang C, từ C sang D và từ D sang E.



# Bài tập mẫu 25.1: Điện trường giữa hai bản phẳng song song tích điện trái dấu

Một ắc-quy hiệu điện thế 12V mắc vào hai bản phẳng đặt song song như hình 25.5. Khoảng cách giữa hai bản $d = 0 { , } 3 \mathrm { c m }$ , đủ nhỏ để xem rằng điện trường giữa hai bản là đều. Tính cường độ điện trường giữa hai bản phẳng.

# Giải:

Dùng công thức (25.6), có thể tính cường độ điện trường giữa hai bản phẳng song song:

$$
E = \frac { \left| V _ { _ B } - V _ { _ A } \right| } { d } = \frac { 1 2 V } { 0 , 3 \times 1 0 ^ { - 2 } m } = 4 { \times } 1 0 ^ { 3 } V / m
$$

![](images/image5.jpg)  
Hình 25.5: Hai bản phẳng song song nối vào nguồn điện

# Bài tập mẫu 25.2: Chuyển động của hạt proton trong điện trường đều

Một proton được thả ra từ trạng thái đứng yên tại vị trí A trong một điện trường đều có độ lớn $8 { , } 0 { \times } 1 0 ^ { 4 } \mathrm { V / m }$ (hình 25.6). Proton di chuyển đến điểm B cách đó một đoạn $d = 0 , 5 0 \mathrm { m }$ dọc theo hướng của điện trường $\vec { E }$ . Tìm tốc độ của proton sau đoạn đường đó.

# Giải:

Khái niệm. Hình dung rằng hạt proton rơi xuống tựa như đang ở trong một trường trọng lực. Trong bài tập này, hạt cũng chịu tác dụng một gia tốc không đổi bởi lực điện trường.

Phân loại. Do hệ không tương tác với bên ngoài nên ta có thể quy vấn đề về chủ đề bảo toàn năng lượng.

![](images/image6.jpg)  
Hình 25.6: Proton tăng tốc theo hướng của điện trường

Phân tích. Áp dụng định luật bảo toàn năng lượng cho điểm A và điểm B:

Thế biểu thức của động năng và thế năng tại A và B tương ứng:

Từ đó suy ra vận tốc $\nu$ đồng thời tính $\Delta V$ theo công thức (25.6):



$$
\nu = { \sqrt { \frac { - 2 e \Delta V } { m } } } = { \sqrt { \frac { - 2 e ( - E d ) } { m } } } = { \sqrt { \frac { 2 e E d } { m } } }
$$

$$
= \sqrt { \frac { 2 ( 1 , 6 \times 1 0 ^ { - 1 9 } C ) ( 8 , 0 \times 1 0 ^ { 4 } \mathrm { V } ) ( 0 , 5 0 m ) } { 1 , 6 7 \times 1 0 ^ { 2 7 } k g } }
$$

$$
= 2 , 8 \times 1 0 ^ { 6 } m / s
$$

Nhận định. Điện th $\acute { \mathrm { e } }$ giảm theo chiều chuyển động của proton, $\Delta V < 0$ , kéo theo sự suy giảm của thế năng: $\Delta U < 0 . { \mathrm { \scriptsize ~ D } } \dot { \hat { \mathrm { e } } }$ cân bằng sự suy giảm này, proton lại tích luỹ động năng trong chuyển động có gia tốc, tuân theo định luật bảo toàn năng lượng.

# Điện thế và thế năng tạo bởi điện tích điểm

Từ trình bày $\dot { \mathbf { O } }$ chương 23, ta đã biết rằng một điện tích điểm $q > 0$ tạo ra trong không gian xung quanh một điện trường đối xứng xuyên tâm với những đường sức hướng ra ngoài. Hiệu điện thế giữa hai điểm A và B bất kì (hình 25.7) có thể tính theo công thức (25.3):

$$
V _ { _ { B } } - V _ { _ { A } } = - \int _ { ( A ) } ^ { ( B ) } \overrightarrow { E } \cdot \overrightarrow { d s }
$$

Vector cường độ điện trường $\overrightarrow { E }$ đối với điện trường của điện tích điểm có dạng

$$
\overrightarrow { E } = \frac { k _ { e } q } { r ^ { 3 } } \overrightarrow { r }
$$

![](images/image7.jpg)  
Hình 25.7: Tính hiệu điện thế giữa hai điểm bất kì trong điện trường đối xứng xuyên tâm

Thế vào thu được

$$
V _ { _ B } - V _ { _ A } = - \int _ { \left( A \right) } ^ { \left( B \right) } \frac { k _ { e } q } { r ^ { 3 } } \vec { r } \cdot \overrightarrow { d s }
$$

Lưu ý rằng gốc thế năng lấy $\acute { \mathbf { O } }$ trạng thái hai điện tích cách xa nhau vô cùng. Nếu $q _ { 1 } , q _ { 2 }$ cùng dấu, chúng có sức mạnh đẩy nhau ra xa nhất có thể, chứng tỏ hệ có mang năng lượng $U > 0$ . Ngược lại nếu $q _ { 1 } , q _ { 2 }$ trái dấu, cần phải bổ sung một năng lượng nhờ một lực bên ngoài mới tách chúng ra xa được, chứng tỏ hệ mang năng lượng âm. Nếu biện luận theo hướng cho rằng điện tích $q _ { 1 }$ nằm trong điện trường do $q _ { 2 }$ tạo ra, ta cũng đi đến kết quả như (25.13).



# Mối liên hệ giữa điện trường và điện thế

Công thức (25.3) viết lại dưới dạng vi phân

$$
d V = - \overrightarrow { E } \cdot \overrightarrow { d s }
$$

cho ta giá trị của hiệu điện thế nếu biết trước điện trường $\overrightarrow { E }$ tại các điểm trong không gian.



Có nghĩa thành phần $E _ { x }$ của vector cường độ điện trường bằng đạo hàm riêng của điện thế theo biến $x$ đảo dấu. Ta cũng thu được kết luận tương tự đối với thành phần theo $y$ và $z .$ , viết thành bộ đầy đủ:

$$
\begin{array} { r } { \boldsymbol { E } _ { \mathrm { \Delta } x } = - \displaystyle \frac { \partial \boldsymbol { V } } { \partial \boldsymbol { x } } , \boldsymbol { E } _ { \mathrm { \Delta } y } = - \displaystyle \frac { \partial \boldsymbol { V } } { \partial \boldsymbol { y } } , \boldsymbol { E } _ { \mathrm { \Delta } z } = - \displaystyle \frac { \partial \boldsymbol { V } } { \partial \boldsymbol { z } } } \\ { \quad \partial ^ { \mathrm { \Delta } } \boldsymbol { \hat { x } } } \end{array}
$$

Hình chiếu của vector $\overrightarrow { E }$ theo hướng của vector $l$ bất $\mathrm { k i }$ cũng được tính theo cách tương tự như thế:

$$
E _ { _ l } = - { \frac { d V } { d l } }
$$

Xét hai điểm lân cận nằm trên cùng một mặt đẳng thế, hiệu điện thế giữa hai điểm này: $d V = 0$ . Do vậy, hình chiếu của vector $\overrightarrow { E }$ theo phương tiếp tuyến với mặt đẳng thế cũng bằng $\overrightarrow { E }$ không. Nói cách khác, vector cường độ điện trường  luôn hướng vuông góc với mặt đẳng thế.

Hình 25.11 miêu tả họ các mặt đẳng thế trong các trường hợp khác nhau: điện trường đều, điện trường sinh ra bởi điện tích điểm và điện trường tạo bởi lưỡng cực điện. Trong tất cả các trường hợp, các mặt đẳng thế luôn vuông góc với những đường sức điện trường tại giao điểm:

• Trên mục 25.2 ta đã phân tích được rằng, họ các mặt đẳng thế trong điện trường đều là những mặt phẳng song song, cố nhiên vuông góc với đường sức điện trường. • Ở mục 25.3 ta cũng làm sáng tỏ rằng, điện thế tạo bởi điện tích điểm chỉ phụ thuộc vào khoảng cách đến điện tích điểm, nên họ các mặt đẳng thế là những mặt cầu, giao nhau vuông góc với đường sức đối xứng xuyên tâm.

![](images/image8.jpg)  
Hình 25.11: Họ các mặt đẳng thế trong các trường hợp: (a) điện trường đều (b) điện trường của điện tích điểm (c) điện trường tạo bởi lưỡng cực điện



Hãy thử suy vector $\overrightarrow { E }$ của điện trường tạo bởi điện tích điểm từ biểu thức của điện thế (25.11):

# Điện thế sinh ra bởi sự phân bố điện tích liên tục

Ở mục 25.3, chúng ta tính được điện thế sinh ra bởi tập hợp các điện tích điểm rời rạc. Mục này trình bày phương pháp tính điện thế sinh ra bởi sự phân bố điện tích liên tục, tức vật tích điện có kích thước đáng $\mathrm { k } \mathring { \mathbf { e } }$ . Có hai phương pháp tiến hành: phương pháp chia nhỏ và phương pháp dùng định lý Gauss.

# Phương pháp chia nhỏ

Ta chia vật tích điện có kích thước lớn nói trên thành những phần rất nhỏ, nhỏ đến mức có thể xem mỗi phần như thế là một điện tích điểm. Đối với mỗi điện tích điểm vừa cắt ra ấy, ta đã có thể áp dụng công thức (25.11) để tính điện thế $d V$ do nó tạo ra tại điểm P cần khảo sát:

![](images/image9.jpg)

Hình 25.12: Tính điện thế sinh ra bởi sự phân bố

$$
d V = k _ { e } { \frac { d q } { r } }
$$

điện tích liên tục

trong đó $r$ là khoảng cách từ phần nhỏ đang xét đến điểm P. Điện thế do vật sinh ra tại điểm P là sự tổng hợp của tất cả các phần nhỏ trên toàn bộ vật tích điện:

$$
V = \sum d V = \int d V = k _ { e } \int \frac { d q } { r }
$$

# Cần lưu ý ở phương pháp này rằng: gốc lấy điện thế $\boldsymbol { V } = 0 ,$ ) nằm $\scriptstyle { \vec { \pmb { \sigma } } }$ xa vô cùng $( \infty )$

# Phương pháp dùng định lý Gauss

Đối với những hệ tích điện mang tính đối xứng, ta có thể dùng định lý Gauss để tính điện trường $\overrightarrow { E }$ trước. Sau đó dùng công thức () để tính điện thế:



$$
V = \int _ { ( \Theta ) } ^ { \Theta ^ { \prime } } \overrightarrow { E } \cdot \overrightarrow { d s }
$$

trong đó $\mathrm { g } \acute { \mathrm { o c } }$ lấy điện thế $( V = 0 )$ có thể quy ước tại một điểm O nào đó.

# Bài tập mẫu 25.4: Điện thế tạo bởi vành tròn tích điện đều

(A) Tìm biểu thức của điện thế tại điểm P nằm trên trục đối xứng của một vành tròn bán kính a với điện tích $\boldsymbol { \mathcal { Q } }$ phân bố đều, cách tâm vành tròn một đoạn $x$ .

# Giải:

Chia vành tròn ra rất nhiều phần nhỏ, mỗi phần có điện tích dq nhỏ đến mức có thể xem như điện tích điểm. Áp dụng công thức (20.20), ta có thể tính điện thế tại điểm P:

![](images/image10.jpg)  
Hình 25.13: Tính điện thế tại điểm nằm trên trục của vành tròn tích điện đều

$$
V = k _ { e } \int { \frac { d q } { r } }
$$

Để ý rằng điểm P nằm cách đều tất cả các phần của vành tròn, do vậy tích phân trên dễ dàng chuyển thành:

$$
V = \frac { k _ { e } } { r } \int d q
$$

Tích phân trên thể hiện tổng toàn bộ điện tích chứa trên vành. Còn khoảng cách $r$ có thể biểu diễn thành $r = \sqrt { a ^ { 2 } + x ^ { 2 } }$

$$
V = { \frac { k _ { e } Q } { \sqrt { a ^ { 2 } + x ^ { 2 } } } }
$$

(B) Tìm biểu thức của cường độ điện trường tại P.

# Giải:

Do tính chất đối xứng, có thể kết luận rằng vector cường độ điện trường $\overrightarrow { E }$ tại điểm P phải hướng dọc theo trục x. Nói cách khác $\overrightarrow { E }$ chỉ có thành phần theo $x$ . Từ mối liên hệ (25.16) giữa cường độ điện trường và thế năng:

$$
\begin{array}{c} E ~ = - { \frac { d V } { d x } } = - k Q { \frac { d } { d x } } ^ { \Big ( } { \frac { 1 } { \sqrt { a ^ { 2 } + x ^ { 2 } } } } ~ \Big ) =  \end{array} \quad k _ { e } x \quad _ { Q }
$$



Bài tập mẫu 25.5: Điện thế tạo bởi thanh tích điện đều Một thanh có chiều dài $l$ đặt dọc theo trục x như hình vẽ. Thanh có điện tích $\boldsymbol { \mathcal { Q } }$ phân bố đều với mật độ dài . Tính điện thế tại điểm $\mathrm { P }$ nằm trên trục $y$ cách đầu thanh một đoạn bằng $a$ .

# Giải:

Điện thế tại $\mathrm { P }$ được tạo bởi các phần điện tích phân bố khắp chiều dài thanh. Xét một đoạn $d x$ rất nhỏ trên thanh, mang điện tích $d q = \lambda d x$ đủ nhỏ để có thể xem như điện tích điểm.

Điện thế do điện tích điểm dq nói trên tạo ra tại P:

![](images/image11.jpg)

Hình 25.14: Tính điện thế tạo bởi thanh tích

$$
d V = k _ { e } \frac { d q } { r } = k _ { e } \frac { \lambda d x } { \sqrt { a ^ { 2 } + x ^ { 2 } } }
$$

điện đều

Điện thế do rất nhiều điện tích điểm như thế trên toàn bộ thanh tạo ra tại P là tích phân:

$$
V = \int _ { 0 } ^ { l } k _ { e } \frac { \lambda d x } { \sqrt { a ^ { 2 } + x ^ { 2 } } }
$$

Theo đó cận tích phân lấy từ $x = 0$ cho đến $x = l .$ .

Để ý rằng $k _ { e }$ và $\lambda = Q / l$ là những số không đổi, có thể cho ra ngoài dấu tích phân:

$$
\left| \begin{array} { c c c } { { \displaystyle { l \big ( } } } & { { \displaystyle { d x } } } & { { \big Q } } \\ { { \displaystyle { V = k _ { e } \lambda \int _ { 0 } \frac { d } { \sqrt { a ^ { 2 } + x ^ { 2 } } } } = k _ { e } \frac { \mathrm { - } } { l } \mathrm { l n ( x + } } } & { { \displaystyle a ^ { 2 } + x ^ { 2 } ) } } \end{array} \right| ^ { l }
$$

$$
= \vert \kappa _ { e } \stackrel { Q } { } _ { l } \ln _ { \big \vert } \frac { l + \sqrt { a ^ { 2 } + l ^ { 2 } } } { a } \big \vert 
$$

# Điện thế tạo bởi vật dẫn tích điện

Từ chương 24, ta biết rằng đối với vật dẫn điện ở trạng thái cân bằng, điện tích chỉ phân bố trên bề mặt vật dẫn. Ngoài ra ta cũng biết rằng, điện trường chỉ tồn tại bên ngoài vật dẫn và vuông góc với bề mặt vật dẫn. Bên trong vật dẫn điện trường hoàn toàn bị triệt tiêu.

Chương này ta tiếp tục bàn đến vật dẫn điện về phương diện điện thế. Áp dụng công thức (25.3) cho hai điểm A và B bất kì nằm trong hoặc trên bề mặt vật dẫn, ta có:

$$
{ \overset { ( B ) } { \underset { E } { \longrightarrow } } } . { \overset { } { d s } } = 0
$$



$$
V _ { \scriptscriptstyle B } - V _ { \scriptscriptstyle A } = - \int _ { ( \zeta { \cal A } ) }
$$

Như vậy mọi điểm thuộc vật dẫn đều có điện thế bằng nhau.



Hình 25.15 miêu tả điện thế tại các điểm bên trong và bên ngoài quả cầu làm bằng vật liệu dẫn điện. Theo trình bày ở chương 24, việc áp dụng định lý Gauss cho ra kết quả rằng: điện trường bên ngoài quả cầu tích điện có dạng y hệt như điện trường tạo bởi điện tích điểm:

$$
E = k _ { e } \frac { q } { r ^ { 2 } }
$$

Do đó điện thế tại một điểm bất kì nằm ngoài quả cầu cũng sẽ có dạng như điện th $\acute { \mathrm { e } }$ sinh ra bởi điện tích điểm đặt tại tâm quả cầu:

$$
V = k _ { e } { \frac { q } { r } }
$$

Từ đó suy ra điện thế ngay trên bề mặt quả cầu tích điện:

$$
V = k _ { _ { e } } { \frac { q } { R } }
$$

![](images/image12.jpg)  
Hình 25.15: (a) vật dẫn hình cầu (b) điện thế (c) điện trường

với $R$ là bán kính quả cầu. Trong trường hợp quả cầu làm bằng vật liệu dẫn điện, biểu thức (25.20) cũng chính là điện thế tại mọi điểm thuộc quả cầu. Hình 25.15b diễn tả điều đó bằng đoạn nằm ngang tương ứng với các điểm bên trong quả cầu.

# Bài tập mẫu 25.6: Hai quả cầu tích điện nối nhau

Hai vật dẫn hình cầu có bán kính lần lượt bằng $r _ { 1 }$ và $r _ { 2 }$ ban đầu đặt cách xa nhau. Sau đó chúng được nối với nhau nhờ sợi dây dẫn điện như hình 25.16. Khi hệ cân bằng, điện tích trên mỗi quả cầu lần lượt bằng $q _ { 1 }$ và $q _ { 2 }$ , phân bố đều trên mỗi bề mặt. Tìm tỉ số của cường độ điện trường trên bề mặt của hai quả cầu này.

# Giải:

Do hai quả cầu đặt cách nhau đủ xa, sự ảnh hưởng lẫn nhau về điện trường là không đáng $\mathbf { k } \acute { \hat { \mathbf { e } } } ,$ , dẫn đến điện tích mỗi bên vẫn phân bố đều trên mỗi bề mặt và điện trường trên mỗi quả cầu vẫn giữ được nguyên tính đối xứng.

Việc nối hai quả cầu bằng dây dẫn làm cho điện thế cả hai bằng nhau:

![](images/image13.jpg)  
Hình 25.16: Hai quả cầu dẫn điện nối với nhau

$$
V = k _ { \mathrm { ~ } _ { e } } ^ { \mathrm { ~ } \mathcal { I } _ { 1 } } = k _ { \mathrm { ~ } _ { e } } ^ { \mathrm { ~ } \mathcal { I } _ { 2 } }
$$



hay:



$$
\displaystyle \frac { q _ { 1 } } { q _ { 2 } } = \frac { r _ { 1 } } { r _ { 2 } } ( 1 )
$$

Cường độ điện trường trên bề mặt mỗi quả cầu có độ lớn:

$$
E _ { 1 } = k _ { e } \frac { q _ { 1 } } { r ^ { 2 } } , E _ { _ 2 } = k _ { e } \frac { q _ { 2 } } { r ^ { 2 } }
$$

Lấy tỉ số của cường độ điện trường:

$$
\underbrace { E _ { _ 1 } } _ { E _ { 2 } } = \underbrace { q _ { _ 1 } r _ { _ 2 } ^ { 2 } } _ { q _ { _ 2 } r _ { _ 1 } ^ { 2 } }
$$

Thế (1) vào thu được:

$$
\begin{array} { c } { E } \\ { E _ { _ 2 } ^ { ^ 1 } = \frac 1 { r ^ { \textit { 1 } } } ^ { 2 } = \frac { r } { r } } \end{array}
$$

Từ kết quả thu được có thể thấy rằng, khi hai quả cầu nối nhau bằng dây dẫn điện, điện trường trên bề mặt của quả cầu nhỏ thì lớn hơn điện trường trên bề mặt quả cầu lớn.

# Vật dẫn rỗng ruột

Vật dẫn rỗng ruột có thể miêu tả như hình 25.17. Với loại vật dẫn hết sức đặc biệt này, ta sẽ chứng minh rằng điện trường bên trong phần rỗng của vật dẫn phải luôn luôn bằng không, dù điện trường bên ngoài có thay đổi thế nào đi nữa! Thực vậy, xét hai điểm A và B bất kì thuộc thành bên trong sát phần rỗng, theo (25.3) ta có:

$$
V _ { _ B } - V _ { _ A } = - \int _ { ( A ) } ^ { ( B ) } \overrightarrow { E } \cdot \overrightarrow { d s }
$$

Nhưng đối với vật dẫn bất kì ta cũng đã chứng minh rằng điện thế tại mọi điểm trong nó đều bằng nhau: $V _ { A } = V _ { B }$ . ENên vector cường độ điện trường buộc phải bằng không.

Vật dẫn rỗng ruột dưới dạng những hộp có vỏ bằng kim loại có nhiều ứng dụng trong việc cách ly các vật bên trong khỏi ảnh hưởng của điện trường ngoài.

Dièn trròng bèn trong óc vàt dân bi trièt tièu, cho dù vàt dān vǎn có mang dièn tich

![](images/image14.jpg)  
Hình 25.17: Vật dẫn rỗng ruột

# Tia lửa điện

Tia lửa điện thường quan sát thấy ở gần vật dẫn điện cao thế. Khi điện trường gần vật dẫn đủ lớn, các electron tự do, vốn phát sinh do sự ion hoá ngẫu nhiên của phân tử khí, sẽ được gia tốc và bị đẩy xa khỏi phân tử mẹ. Chúng chuyển động nhanh và va chạm với nhiều phân tử khí xung quanh, làm phát sinh thêm rất nhiều sự ion hoá thứ cấp, kéo theo sự xuất hiện càng lúc càng nhiều electron tự do khác. Các electron này sau đó tái kết hợp với những ion phân tử, di chuyển từ trạng thái tự do sang trạng thái liên kết ở mức năng lượng thấp hơn làm phát ra năng lượng dưới dạng ánh sáng. Đó chính là tia lửa điện.





Ở những phần nhọn của vật dẫn, điện tích tập trung nhiều hơn và sinh ra điện trường lớn hơn so với những phần khác. Do đó tia lửa điện thường hay xuất hiện ở những điểm nhọn này.

Tia lửa điện có thể được quan sát rõ hơn nhờ máy quay tử ngoại

# Thí nghiệm giọt dầu Millikan

![](images/image15.jpg)  
Hình 25.18: Thí nghiệm giọt dầu Millikan

Trong giai đoạn 1909-1913, Robert Millikan đã tiến hành phép đo điện tích của electron, xác định giá trị của điện tích nguyên tố e. Thiết bị thí nghiệm được mô tả như hình 25.18. Bộ phận chính của thiết bị gồm hai đĩa kim loại đặt song song, đấu vào hai cực của ắc quy để tạo ra điện trường giữa chúng. Millikan dùng bình phun sương phun những giọt dầu li ti vào khoảng trống giữa hai đĩa, đồng thời rọi x-quang làm ion hoá không khí, khiến cho các electron được giải phóng và dính vào những giọt dầu. Những giọt dầu được chiếu sáng, hiện giữa ống kính quan sát như những ngôi sao hiện giữa trời đêm.

Hình 25.21: Bộ lọc bụi tĩnh điện   



Hiệu điện thế giữa hai điểm A và B trong điện trường $\overrightarrow { E }$ được định nghĩa qua công thức:

$$
\Delta V \equiv \frac { \Delta U } { q } = - \int _ { ( A ) } ^ { ( B ) } \overrightarrow { E } \cdot \overrightarrow { d s }
$$

trong đó U - độ chênh lệch thế năng. Điện thế $V = U / q$ là một đại lượng vô hướng, có đơn vị Volt (V): $1 \mathrm { V } = 1 \mathrm { J } / \mathrm { C }$



# Khái niệm và nguyên lý

Khi một điện tích dương $q$ di chuyển từ vị trí A sang vị trí B trong điện trường ${ \overline { { E } } } _ { : }$ , thế năng thay đổi một lượng bằng:

$$
\Delta U = - q \int _ { ( \stackrel {  } { \langle d \rangle } } ^ { ( B ) } \stackrel {  } { \vec { E } \cdot \vec { d s } }
$$

Hiệu điện thế giữa hai điểm nằm trên cùng một đường sức của điện trường đều và cách nhau một đoạn $d$ bằng

$$
\Delta V = - E d
$$

Nếu chọn $V = 0$ tại $r = \infty$ , điện thế tạo ra bởi một điện tích điểm tại vị trí cách nó đoạn r bằng

$$
V = k _ { e } { \frac { q } { r } }
$$

Điện thế do nhiều điện tích điểm tạo thành là sự tổng hợp các thế năng của từng điện tích điểm riêng rẽ.

Thế năng của hệ tạo bởi hai điện tích điểm nằm cách nhau một khoảng r12

$$
U = k _ { e } \frac { q _ { 1 } q _ { 2 } } { r _ { 1 2 } }
$$

Thế năng của hệ cấu thành từ nhiều điện tích điểm có thể tính được bằng cách lấy tổng thế năng từ mỗi cặp trong hệ theo cách như trên.

Nếu điện thế được cho dưới dạng một hàm số phụ thuộc vào toạ độ $V = V ( x , y , z )$ , các thành phần của vector cường độ điện trường $\bar { E }$ có thể tính được bằng cách lấy đạo hàm của điện thế theo toạ độ:

$$
E _ { _ x } = - \frac { d V } { d x } , E _ { _ y } = - \frac { d V } { d y } , E _ { _ z } = - \frac { d V } { d z }
$$

Điện thế tạo ra bởi sự phân bố liên tục các điện tích được tính bằng

$$
V = k _ { _ { e } } { \int } \frac { d q } { r _ { _ { s } } }
$$

Đối với vật dẫn điện $\acute { \mathbf { O } }$ trạng thái cân bằng, mọi điểm nằm trong vật dẫn và trên bề mặt vật dẫn đều có cùng một điện thế.



# Câu hỏi lý thuyết chương 25

1. Phân biệt hai khái niệm điện thế và thế năng.

2. Hãy mô tả mặt đẳng thế trong điện trường tạo bởi một dây tích điện dài vô hạn và của một mặt cầu tích điện đều.

3. Khi hai hạt mang điện tích điểm đặt xa nhau vô cùng, thế năng của hệ được quy ước bằng không. Khi đưa các hạt tiến lại gần nhau, thế năng của hệ mang giá trị dương nếu hai điện tích cùng dấu, mang giá trị âm nếu hai điện tích trái dấu. Hãy giải thích tại sao như vậy.

# Bài tập chương 25

1. Hai bản phẳng đặt song song cách nhau $5 { , } 3 3 \ \mathrm { m m }$ , đặt dưới hiệu điện thế 600 V.

(a) Tính cường độ điện trường giữa hai bản phẳng.   
(b) Tìm lực tác dụng lên một electron đang nằm trong điện trường này.   
(c) Để di chuyển một electron từ vị trí cách bản dương $2 { , } 9 0 \mathrm { m m }$ đến bản âm cần thực hiện một công bằng bao nhiêu?

ĐS: (a) $1 , 1 3 { \times } 1 0 ^ { 5 } \mathrm { N } / \mathrm { C }$ (b) $1 , 8 { \times } 1 0 ^ { - 1 4 } \mathrm { N } \left( \mathrm { c } \right) 4 , 3 7 { \times } 1 0 ^ { - 1 7 } \mathrm { J }$

2. Một proton được gia tốc từ trạng thái đứng yên bằng hiệu điện thế 120 V. Tính tốc độ mà nó thu được sau khi gia tốc.

ĐS: $1 { , } 5 2 { \times } 1 0 ^ { 5 } \mathrm { m } / \mathrm { s }$

3. Một điện trường đều có cường độ $3 2 5 ~ \mathrm { V / m }$ hướng theo chiều âm của trục $y$ như hình vẽ. Tính hiệu điện thế $V _ { B } - V _ { A }$ giữa hai điểm A(-0,2 ;-0,3) và B(0,4 ;0,5). Gợi ý: lấy tích phân đường theo đường đứt nét như hình vẽ.

ĐS: $+ 2 6 0 \mathrm { V }$

4. Khi một electron chuyển động song song theo trục $x$ từ vị trí $x = 0$ đến vị trí $x = 2 \mathrm { c m }$ , tốc độ của nó suy giảm từ

$3 { , } 7 { \times } 1 0 ^ { 6 } \mathrm { m } / \mathrm { s }$ xuống còn 1,4105 m/s.

![](images/image16.jpg)  
Hình bài 3

(a) Tính hiệu điện thế giữa hai điểm nói trên (b) Điểm nào có điện thế lớn hơn?

ĐS: (a) -38,9 V



5. Hai điện tích điểm được bố trí cách nhau $d = 2$ cm như hình vẽ. Tính điện thế tại điểm A cách đều các điện tích một khoảng $d$ và tại điểm B nằm chính giữa hai điện tích.

ĐS: $V _ { _ A } = 5 { , } 3 9 \mathrm { k V }$ , $V _ { _ A } = 1 0 { , } 8 \mathrm { k V }$

![](images/image17.jpg)  
Hình bài 5

6. Ba điện tích điểm có giá trị lần lượt bằng $2 0 ~ \mathrm { n C }$ , $1 0 ~ \mathrm { n C }$ và - $2 0 ~ \mathrm { n C }$ được gắn cố định trên một trục thẳng đứng như hình vẽ.

(a) Tính thế năng của hệ ba điện tích gắn cố định nói trên. (b) Đặt thêm hạt có điện tích $4 0 ~ \mathrm { n C }$ và khối lượng $2 \times 1 0 ^ { - 1 3 }$ kg vào vị trí như hình vẽ. Hạt này bị đẩy và chuyển động ra xa do tương tác với ba điện tích $\mathrm { c } \acute { \alpha }$ định. Tính vận tốc của hạt khi nó bị đẩy tới xa vô cùng.

ĐS: (a) $- 4 , 5 { \times } 1 0 ^ { - 5 } \mathrm { J } \left( { \bf b } \right) 3 , 4 6 { \times } 1 0 ^ { 4 } \mathrm { m } / \mathrm { s }$

7. Hai điện tích điểm đặt cách nhau $d = 2$ cm như hình vẽ. Cho biết $\mathcal { Q } = 5 \mathrm { n C }$ . Hãy tính:

(a) Điện thế tại A.   
(b) Điện thế tại B.   
(c) Hiệu điện thế giữa B và A.

![](images/image18.jpg)  
Hình bài 6

![](images/image19.jpg)  
Hình bài 7

ĐS: (a) $V _ { _ A } = 5 , 4 3 \mathrm { k V }$ (b) $V _ { _ B } = 6 { , } 0 8 \mathrm { k V }$ (c)



V = 658V



8. Tại một vị trí P nào đó gần điện tích điểm có cường độ điện trường bằng $5 0 0 \mathrm { V / m }$ và điện thế $- 3 \ \mathrm { k V }$ . Hãy tính :

(a) Khoảng cách giữa điểm P và điện tích điểm.   
(b) Độ lớn của điện tích điểm.

ĐS: (a) $6 \mathrm { m } ( \mathrm { b } ) - 2 \mu \mathrm { C }$

9. Bốn hạt có cùng điện tích $\boldsymbol { \mathcal { Q } }$ đặt trên bốn góc của hình vuông có cạnh bằng a. Hãy tính:

(a) Điện thế ở tâm của hình vuông.   
(b) Công cần thực hiện để đưa một hạt điện tích $q$ từ xa vô cùng về tâm của hình vuông.

ĐS: (a) $4 \sqrt 2 k _ { e } { \frac { Q } { a } } \left( \mathbf { b } \right) 4 \sqrt 2 k _ { e } { \frac { q Q } { a } }$

10. Năm 1911, Rutherford cùng hai trợ lý Geiger và Marsden đã tiến hành thí nghiệm tán xạ tia alpha trên nguyên tử vàng. Mỗi hạt alpha có điện tích bằng $+ 2 e$ và khối lượng $6 { , } 6 4 \times 1 0 ^ { - 2 7 } \mathrm { k g }$ . Kết quả thí nghiệm chỉ ra rằng, hầu hết khối lượng của nguyên tử gần như tập trung vào hạt nhân với kích thước rất nhỏ, được bao quanh bởi các quỹ đạo electron.

Bắn một hạt alpha từ khoảng cách xa hướng thẳng tới hạt nhân vàng với điện tích $+ 7 9 e$ . Tốc độ ban đầu của alpha bằng $2 { , } 0 0 { \times } 1 0 ^ { 7 } \mathrm { m / s }$ . Hạt alpha có khả năng tiến lại gần nhất so với hạt nhân vàng một khoảng bằng bao nhiêu? Cho rằng hạt nhân vàng luôn nằm cố định.

ĐS: $2 { , } 7 4 { \times } 1 0 ^ { - 1 4 } \mathrm { m }$

11. Dựa vào độ thị sự phụ thuộc của điện th $\acute { \mathrm { e } }$ vào toạ độ $V ( x )$ , hãy vẽ đồ thị sự phụ thuộc của thành phần $x$ của cường độ điện trường theo toạ độ $E _ { x } ( x )$ .

![](images/image20.jpg)

12. Trong phạm vi từ $x = 0$ đến $x = 6 , 0 0 \mathrm { m }$ , điện thế có dạng hàm số $V = a + b x ,$ , với $\overset { \cdot } { a } = 1 \overset { \cdot } { 0 } , 0 \mathrm { \ v { V } }$ và $b = 7 { , } 0 0 \mathrm { V / m }$ . Hãy xác định :

(a) Điện thế tại $x = 0$ , $x = 3 , 0 0$ và $x = 6 , 0 0 \mathrm { m }$ .   
(b) Độ lớn và hướng của điện trường tại $x = 0$ , $x = 3 , 0 0$ và $x = 6 , 0 0 \mathrm { m }$ .

ĐS: (a) 10V, -11V và -32V (b) $7 \mathrm { N } / \mathrm { C }$ tại mọi điểm $x > 0$



13. Trên một vùng không gian nhất định nào đó, điện thế có dạng hàm số $V = 5 x - 3 x ^ { 2 } y + 2 y z ^ { 2 }$ .

![](images/image21.jpg)

(a) Tìm hàm số biểu diễn các thành phần $E _ { x } , E _ { y } , E _ { z }$ của vector cường độ điện trường $\overrightarrow { E }$ . (b) Tính cường độ điện trường tại điểm P có toạ độ $( 1 , 0 0 ; 0 ; - 2 , 0 0 ) \mathrm { m } .$ . ĐS: (a) $\overrightarrow { E } = ( - 5 + 6 x y ) \cdot \overrightarrow { i } + ( 3 x ^ { 2 } - 2 z ^ { 2 } ) \cdot \overrightarrow { j } - 4 y z \cdot \overrightarrow { k } \quad ( \mathbf { b } ) 7 , 0 7 \mathrm { N } / \mathrm { C }$

14. Một thanh tích điện đều dài $1 4 ~ \mathrm { c m }$ được uốn cong thành nửa cung tròn  Hình như hình vẽ. Tổng điện tích trên thanh bằng $- 7 { , } 5 ~ \mu \mathrm { C }$ . Tính điện thế tại tâm O của cung tròn.

ĐS: $- 1 { , } 5 1 { \times } 1 0 ^ { 6 } \mathrm { V }$

15. Một dây tích điện đều với mật độ điện dài $\lambda$ được uốn thành dạng như hình vẽ. Hãy tính điện thế tại điểm O.

![](images/image22.jpg)  
Hình bài 15

ĐS: $k _ { e } \lambda ( \pi + 2 \ln { 3 } )$

16. Một vật dẫn hình cầu có bán kính $1 4 \mathrm { { c m } }$ và điện tích $2 6 \mu \mathrm { C }$ . Tính cường độ điện trường và điện thế tại điểm cách tâm vật dẫn:

(a) $\begin{array} { c } { r = 1 0 \mathrm { c m } } \\ { r = 2 0 \mathrm { c m } } \\ { r = 1 4 \mathrm { c m } } \end{array}$   
(b)   
(c)   
ĐS: (a) $1 { , } 6 7 { \times } 1 0 ^ { 6 } \mathrm { V }$ (b) 1,17106V (c) 1,67106V

17. Ống Geiger-Mueller có cấu tạo $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ anode và cathode từ hai ống kim loại hình trụ lồng vào nhau như hình vẽ. Anode có bán kính $r _ { B }$ và tích điện với mật độ dài $\lambda$ . Cathode có bán kính $r _ { A }$ và tích điện với mật độ dài $- \lambda .$

(a) Chứng tỏ rằng hiệu điện thế giữa anode và cathode có dạng:

$$
\Delta V = 2 k \underset { e } { \lambda } \ln \underset { \underset { \left\lfloor \frac { 1 } { r } \right\rfloor } { \longrightarrow } } { \binom { r _ { s _ { 1 } } } { r _ { s } } }
$$

![](images/image23.jpg)



Hình bài 17



(b) Chứng tỏ rằng cường độ điện trường phụ thuộc vào khoảng cách $r$ đến trục đối xứng theo biểu thức:

$$
E = \frac { \Delta V } { \ln ( r _ { A } / \mathrm { r } _ { B } ) } \frac { 1 } { r }
$$

# Public_146 

Ánh sáng là cơ sở cho hầu như mọi sự sống trên trái đất. Ví dụ, thực vật chuyển đổi năng lượng của ánh sáng mặt trời thành năng lượng hóa học thông qua quá trình quang hợp. Ngoài ra, ánh sáng là phương tiện chính mà chúng ta có thể truyền và nhận thông tin đến và đi từ các vật thể xung quanh cũng như từ trong vũ trụ.

Ánh sáng là một dạng bức xạ điện từ, truyền năng lượng từ nguồn sáng tới người quan sát. Nhiều hiện tượng trong cuộc sống hàng ngày của chúng ta phụ thuộc vào tính chất của ánh sáng. Khi bạn xem tivi hoặc xem ảnh trên màn hình máy tính, bạn sẽ thấy hàng triệu màu được tạo thành từ sự kết hợp chỉ có ba màu là: đỏ, xanh dương và xanh lục. Màu xanh của bầu trời ban ngày, màu đỏ và màu cam trên bầu trời lúc bình minh hay hoàng hôn là kết quả của hiện tượng tán xạ ánh sáng bởi các phân tử không khí. Bạn thấy hình ảnh của mình trong gương phòng tắm buổi sáng hoặc hình ảnh của những chiếc xe khác trong gương chiếu hậu khi đang lái xe là kết quả từ sự phản xạ ánh sáng. Nếu bạn đeo kính để nhìn cho rõ thì bạn đang nhờ vào hiện tượng khúc xạ ánh sáng. Màu sắc của cầu vồng là do sự tán sắc ánh sáng khi nó đi qua những hạt mưa lơ lửng trên bầu trời sau cơn mưa. Nếu bạn đã từng nhìn thấy những vòng tròn màu của hào quang xung quanh cái bóng của chiếc máy bay bạn đang đi trên những đám mây thì bạn đang thấy kết quả của hiện tượng giao thoa ánh sáng.

Trong phần giới thiệu của chương 35, chúng ta sẽ thảo luận về lưỡng tính sóng-hạt của ánh sáng. Trong một số trường hợp, ánh sáng được mô hình như một dòng hạt; ở những trường hợp khác, mô hình sóng hoạt động tốt hơn. Chương 35 đến hết 38 tập trung vào các khía cạnh của ánh sáng được hiểu rõ nhất thông qua mô hình sóng của ánh sáng. Trong phần 6, chúng ta sẽ tìm hiểu về bản chất hạt của ánh sáng.



Chương này bắt đầu giới thiệu hai mô hình lịch sử của ánh sáng và thảo luận các phương pháp đo tốc độ ánh sáng trước đây. Tiếp theo là những hiện tượng cơ bản của quang hình học: sự phản xạ (reflection) của ánh sáng từ một bề mặt và sự khúc xạ (refraction) khi ánh sáng đi qua biên giới giữa hai môi trường. Chúng ta cũng sẽ nghiên cứu sự tán sắc (dispersion) của ánh sáng khi nó khúc xạ qua vật liệu, dẫn đến hiện tượng xuất hiện cầu vồng. Cuối cùng, chúng ta sẽ nghiên cứu hiện tượng phản xạ toàn phần (total internal reflection), là cơ sở cho hoạt động của sợi quang và công nghệ sợi quang.

## Bản chất của ánh sáng

Trong lịch sử có hai mô hình cơ bản về bản chất của ánh sáng. Trước thế kỷ thứ 19, ánh sáng được xem như một dòng hạt. Các hạt này hoặc được phát ra từ các vật hoặc xuất phát từ mắt người quan sát. Newton là người chủ xướng cho lý thuyết hạt ánh sáng. Ông cho rằng các hạt ánh sáng xuất phát từ các vật và đi đến mắt để kích thích cảm giác sáng của người quan sát.

Christian Huygens thì lại tin rằng ánh sáng có thể là một dạng sóng chuyển động nào đó. Ông đã chỉ ra rằng các tia sáng giao thoa với nhau. Những nghiên cứu khác suốt thể kỷ thứ 19 đã dẫn đến một sự thừa nhận chung về lý thuyết sóng của ánh sáng. Thomas Young là người cung cấp bằng chứng rõ ràng đầu tiên (năm 1801) về bản chất sóng của ánh sáng. Ông đã giải thích hiện tượng giao thoa của ánh sáng dựa trên nguyên lý chồng chất. Hiện tượng này không thể giải thích được bằng lý thuyết hạt ánh sáng. Maxwell đã khẳng định rằng ánh sáng là một dạng sóng điện từ có tần số cao và Hertz đã cung cấp bằng chứng thực nghiệm cho lý thuyết của Maxwell vào năm 1887.

Mặc dù mô hình sóng và lý thuyết cổ điển về điện - từ có thể giải thích được hầu hết các tính chất của ánh sáng, nhưng chúng không thể giải thích được một số kết quả thí nghiệm sau đó. Nổi bật nhất là hiệu ứng quang điện được phát hiện bởi Hertz: Khi ánh sáng bắn vào một bề mặt kim loại thì các electron có thể được thoát ra khỏi bề mặt. Các thí nghiệm cho thấy động năng của một electron thoát ra độc lập với cường độ ánh sáng. Phát hiện này mâu thuẫn với mô hình sóng. Einstein đã đề xuất một giải thích về hiệu ứng quang điện vào năm 1905 sử dụng mô hình dựa trên khái niệm lượng tử hóa được Max Planck phát triển vào năm 1900. Mô hình lượng tử giả định năng lượng của sóng ánh sáng nằm trong các hạt gọi là photon và do đó năng lượng được cho là bị lượng tử hóa. Theo lý thuyết của Einstein, năng lượng E của một photon tỉ lệ thuận với tần số f của sóng điện từ :

$$
\mathrm { E = h f }
$$

h = 6,63. 10-34 J.s là hằng số Planck.



Như vậy, ánh sáng phải có lưỡng tính sóng hạt. Trong một số hoàn cảnh ánh sáng biểu hiện các đặc trưng của sóng và trong một số hoàn cảnh khác ánh sáng lại biểu hiện các đặc trưng của hạt.

## Đo tốc độ ánh sáng

Vì ánh sáng di chuyển với tốc độ rất cao $( \mathbf { c } = 3 , 0 0 . 1 0 ^ { 8 } \mathbf { m } / \mathrm { s } )$ nên những cố gắng trước đây để đo tốc độ của nó đều không thành công. Galileo đã cố gắng đo tốc độ ánh sáng bằng cách cho hai người quan sát đứng cách nhau $1 0 ~ \mathrm { k m }$ xác định thời gian ánh sáng truyền đi qua khoảng cách giữa hai người và ông đã kết luận rằng vì thời gian phản ứng của người quan sát lớn hơn nhiều thời gian chuyển động của ánh sáng nên không thể đo được tốc độ ánh sáng bằng cách này.

### Phương pháp Roemer

Năm 1675, Ole Roemer đã sử dụng các quan sát thiên văn để ước lượng tốc độ ánh sáng. Ông đã sử dụng chu kỳ quay của Io, một mặt trăng của sao Mộc, khi sao Mộc quay xung quanh Mặt Trời. Góc quay của sao Mộc trong khoảng thời gian Trái Đất quay quanh Mặt Trời một góc $9 0 ^ { 0 }$ có thể tính được.

In the time interval during which the Earth travels $9 0 ^ { \circ }$ around the Sun (three months),Jupiter travels only about 7.5°.

Chu kỳ quay dài hơn khi Trái Đất lùi xa dần sao Mộc, ngắn hơn khi Trái Đất tiến lại gần.

Sử dụng số liệu của Roemer, Huygens đã ước tính giới hạn dưới của tốc độ ánh sáng là $2 { , } 3 { . } 1 0 ^ { 8 } ~ \mathrm { m } / \mathrm { s }$ . Đây là một kết quả rất quan trọng trong lịch sử vì nó đã cho thấy rằng ánh sáng có tốc độ hữu hạn và đã cho một ước lượng về tốc độ đó.

![](images/image1.jpg)

### Phương pháp Fizeau

Phương pháp thành công đầu tiên để đo tốc độ ánh sáng bằng các kỹ thuật thuần túy trên mặt đất được phát triển vào năm 1849 bởi nhà vật lý người Pháp Armand H. L. Fizeau.

Hình 35.2 biểu diễn một sơ đồ đơn giản của thiết bị đo. Nếu d là khoảng cách giữa nguồn sáng (được xem là vị trí của bánh xe) và gương và t là thời gian ánh sáng di chuyển từ bánh xe đến gương thì tốc độ của ánh sáng là $\mathrm { c } = 2 \mathrm { d } / \Delta \mathrm { t }$ .

![](images/image2.jpg)  
Hình 35.1: Phương pháp Roemer   
Hình 35.2: Phương pháp Fizeau

Để đo thời gian vận chuyển, Fizeau đã sử dụng một bánh xe răng cưa, chuyển đổi một chùm ánh sáng liên tục thành một loạt các xung ánh sáng. Nếu một xung ánh sáng di chuyển về phía gương và đi qua khe hở tại điểm A trong hình 35.2 và quay trở lại bánh xe tại răng B thì xung phản xạ sẽ không tới được người quan sát. Với tốc độ quay lớn hơn, điểm C có thể di chuyển vào vị trí để cho phép xung phản xạ đi tới người quan sát. Biết khoảng cách d, số răng của bánh xe và tốc độ góc của bánh xe, Fizeau đã xác định được giá trị tốc độ ánh sáng là $3 , \bar { 1 } \times 1 0 ^ { 8 }$ $\mathrm { m } / \mathrm { s }$ .





Các phép đo mang lại giá trị chính xác hơn được chấp nhận hiện tại là 2,997 924 58×108 $\mathrm { m } / \mathrm { s } .$ .

# Gần đúng tia trong quang hình học (quang học tia)

Quang học tia (Ray Optics), còn gọi là quang hình học (Geometric Optics), nghiên cứu sự lan truyền của ánh sáng. Nó sử dụng giả thuyết rằng ánh sáng truyền đi theo đường thẳng trong một môi trường đồng dạng và thay đổi hướng khi gặp bề mặt của một môi trường khác hoặc nếu như tính chất quang học của môi trường là không đồng dạng. Gần đúng tia (Ray approximation) được sử dụng để biểu diễn các chùm sáng. Các tia sáng là những đường thẳng vuông góc với mặt sóng (front wave). Với gần đúng tia, chúng ta giả thiết rằng một sóng ánh sáng truyền đi trong môi trường trên một đường thẳng theo hướng của các tia đó.

![](images/image3.jpg)

Nếu một sóng gặp một vật cản với bước sóng $\lambda < < \mathtt { d }$ thì sóng đó sẽ xuất phát từ khoảng trống và tiếp tục di chuyển theo một đường thẳng, d là đường kính của khoảng trống. Đây là một gần đúng tốt để nghiên cứu gương, kính, lăng kính ...Các hiệu ứng xảy ra đối với những khoảng trống có kích thước khác nhau.

Hình 35.3: Quang học tia

![](images/image4.jpg)  
Hình 35.4: Một sóng phẳng bước sóng  chiếu tới màn chắn có một lỗ trống đường kính d.

35.4

# Sự phản xạ ánh sáng

Một tia sáng (tia tới) di chuyển trong một môi trường khi gặp biên giới với một môi trường thứ hai thì một phần của tia tới sẽ bị phản xạ ngược lại môi trường đầu tiên, có nghĩa là nó sẽ hướng ngược lại môi trường thứ nhất. Đối với các sóng ánh sáng truyền trong không gian ba chiều thì hướng của các tia phản xạ khác với hướng của các tia tới.



Phản xạ gương (specular reflection) là sự phản xạ từ một bề mặt nhẵn. Các tia phản xạ song song với nhau.

Tất cả hiện tượng phản xạ ánh sáng trong sách này đều được giả thiết là phản xạ gương.

Sự phản xạ tràn lan (Diffuse reflection) là sự phản xạ trên một bề mặt thô. Các tia phản xạ truyền đi theo nhiều hướng khác nhau. Một bề mặt được coi là bề mặt thô nếu sự biến đổi bề mặt nhỏ hơn nhiều bước sóng ánh sáng.

# Định luật phản xạ (Law of reflection)

Pháp tuyến là một đường thẳng vuông góc với bề mặt. Nó nằm tại vị trí tia tới đập lên bề mặt. Tia tới tạo với pháp tuyến một góc 1. Tia phản xạ tạo với tia tới một góc $\boldsymbol { \theta _ { 1 } }$ .

Góc phản xạ bằng góc tới :

![](images/image5.jpg)

![](images/image6.jpg)  
Hình 35.5: Sự phản xạ gương

$$
\theta _ { 1 } = \theta _ { 1 }
$$

Mối liên hệ này được gọi là định luật phản xạ.

Tia tới, tia phản xạ và pháp tuyến đều nằm trên một mặt phẳng. Bởi vì sự phản xạ sóng là một hiện tượng phổ biến, thường xảy ra nên chúng ta sẽ đưa ra một mô hình phân tích cho trường hợp này được gọi là mô hình phân tích sóng bị phản xạ (the wave under reflection model).

Câu hỏi 35.1: Trong phim, bạn có thể nhìn thấy diễn viên nhìn vào một chiếc gương và thấy mặt mình trong đó. Có thể nói chắc chắn rằng trong cảnh đó người diễn viên nhìn thấy trong gương a) mặt anh ta b) mặt bạn c) mặt đạo diễn d) camera quay cảnh e) không thể xác định được.

# Bài tập mẫu 35.1: Phản xạ nhiều lần

Hai gương hợp nhau một góc $1 2 0 ^ { \mathrm { o } }$ như hình vẽ. Tia tới chiếu lên gương $\mathbf { M } _ { 1 }$ dưới góc $6 5 ^ { \mathrm { { \circ } } }$ , tia phản xạ hướng đến gương M2. Hãy xác định hướng của tia sáng sau khi phản xạ trên gương $\mathbf { M } _ { 2 }$ . 2025-0

# Giải:

Theo định luật phản xạ, tia phản xạ trên $\mathbf { M } _ { 1 }$ hợp với gương một góc

$$
8 = 9 0 ^ { \circ } - 6 5 ^ { \circ } = 2 5 ^ { \circ }
$$

The incident ray, the reflected ray, and the normal all lie in the same plane, and $\theta _ { 1 } ^ { \prime } = \theta _ { 1 }$

![](images/image7.jpg)

 = 180° - 25° - 120° = 35°

Hình 35.6: Định luật phản xạ   



Hình 35.7: Sự phản xạ nhiều lần



$$
\theta _ { \mathrm { M } 2 } = 9 0 ^ { \circ } - 3 5 ^ { \circ } = 5 5 ^ { \circ }
$$

Tia phản xạ trên gương ${ { \bf { M } } _ { 2 } }$ hợp với pháp tuyến một góc

$$
{ \theta } ^ { \prime } { } _ { \mathrm { M } 2 } = { \theta } _ { \mathrm { M } 2 } = 5 5 ^ { \circ }
$$

# Sự phản xạ ngược (retroreflection)

Giả sử góc hợp giữa hai gương là $9 0 ^ { \mathrm { o } }$ thì chùm tia phản xạ sẽ quay trở về nguồn phát song song với chùm tia tới ban đầu. Hiện tượng này được gọi là sự phản xạ ngược. Có nhiều áp dụng của hiện tượng này như đo khoảng cách tới Mặt Trăng, gương chiếu hậu, tín hiệu giao thông...

![](images/image8.jpg)  
Hình 35.8: Ứng dụng hiện tượng phản xạ ngược

Vào năm 1969, một bảng gồm nhiều gương phản xạ nhỏ đã được các phi hành gia tàu Apollo 11 đưa lên Mặt trăng (hình 35.8a). Một chùm tia laser từ Trái đất chiếu đến bảng gương này sẽ được phản xạ trực tiếp trở lại chính nó và thời gian di chuyển của nó có thể đo được. Từ đó có thể xác định được khoảng cách từ Trái đất đến Mặt trăng với sai số $1 5 \mathrm { { c m } }$ .



Một ứng dụng hàng ngày khác được tìm thấy trong đèn hậu ô tô. Một phần nhựa của đèn hậu được tạo thành bởi nhiều góc hình khối nhỏ (hình 35.8b) để các chùm đèn pha từ ô tô phía sau chiếu đến sẽ phản xạ lại người lái xe.

Thay vì các góc hình lập phương, các hình cầu nhỏ đôi khi được sử dụng (hình 35.8c). Những quả cầu nhỏ trong suốt được sử dụng trong một vật liệu phủ trên nhiều biển báo đường bộ. Do sự phản xạ ngược từ những quả cầu này, dấu hiệu dừng xe trong hình 35.8d sẽ sáng hơn nhiều so với khi nó chỉ đơn giản là một bề mặt phẳng, sáng bóng. Sự phản xạ ngược cũng được sử dụng cho các tấm phản quang trên giày chạy bộ và quần áo chạy để cho phép người chạy bộ được nhìn thấy vào ban đêm.

# Sự khúc xạ ánh sáng

Khi một tia sáng lan truyền trong một môi trường trong suốt đến gặp mặt phân cách với một môi trường trong suốt khác thì một phần tia tới bị phản xạ và một phần sẽ đi vào môi trường thứ hai.

All rays and the normal lie in the same plane, and the refracted ray is bent toward the normal because $u _ { 2 } < v _ { 1 }$

Tia sáng đi vào môi trường thứ hai này có hướng bị thay đổi. Sự gãy tia sáng này được gọi là khúc xạ (refraction).

Tia tới, tia phản xạ, tia khúc xạ và pháp tuyến đều nằm trong cùng một mặt phẳng. Góc khúc xạ (angle of refraction) phụ thuộc vào vật liệu và góc tới (angle of incidence).

![](images/image9.jpg)

$$
{ \frac { \sin \theta _ { 2 } } { \sin \theta _ { 1 } } } = { \frac { \mathbf { v } _ { 2 } } { \mathbf { v } _ { 1 } } }
$$

$\mathbf { V } _ { 1 }$ là tốc độ ánh sáng trong môi trường thứ nhất và $\mathbf { V } _ { 2 }$ là tốc độ ánh sáng trong môi trường thứ hai. Đường đi của tia sáng qua bề mặt khúc xạ là có thể đảo ngược. Ví dụ một tia sáng truyền từ A đến B thì nếu có một tia xuất phát từ B sẽ đi theo con đường AB để đến A.

![](images/image10.jpg)  
Hình 35.9: Sự khúc xạ ánh sáng

Câu hỏi 35.2: Trên hình 35.9, tia tới tà tia (1), hãy chỉ ra các tia phản xạ và tia khúc xạ trong những tia sáng 2, 3, 4, 5.



![](images/image11.jpg)  
Hình 35.10: (a) Sự khúc xạ ánh sáng khi đi vào. môi trường có tốc độ nhỏ hơn, a (b). môi trường có tốc độ lớn hơn

When the beam moves from glass into air, the light speeds up upon entering the air and its path is bent away from the normal.



Ánh sáng có thể khúc xạ vào trong một vật liệu mà ở đó tốc độ của nó nhỏ hơn. Góc khúc xạ nhỏ hơn góc tới. Tia sáng bị gập về phía pháp tuyến (hình 35.10.a).

Ánh sáng có thể khúc xạ vào trong một vật liệu mà ở đó tốc độ của nó lớn hơn. Góc khúc xạ lớn hơn góc tới. Tia sáng bị lệch xa khỏi pháp tuyến (hình 35.10.b).

Trong một môi trường, ánh sáng có tốc độ nhỏ hơn trong chân không. Điều đó có thể giải thích như sau. Ánh sáng đập vào một electron. Electron đó có thể hấp thụ ánh sáng, dao động và bức xạ ánh sáng. Sự hấp thụ và phát xạ có thể làm cho tốc độ di chuyển trung bình trong môi trường giảm xuống.

![](images/image12.jpg)  
Hình 35.11: Sự giảm vận tốc của tia sáng khí đi vào môi trường

### Chiết suất - Chỉ số khúc xạ

Tốc độ của ánh sáng trong một vật liệu bất kỳ đều nhỏ hơn tốc độ ánh sáng trong chân không. Chiết suất n của một môi trường được xác định như sau:

$$
n = { \frac { c } { \mathrm { ~ v ~ } } }
$$



Trong đó, c là tốc độ ánh sáng trong chân không, v là tốc độ ánh sáng trong môi trường. Đối với chân không $\mathfrak { n } = 1$ , đối với không khí n cũng được coi là bằng 1. Đối với các môi trường khác, $\mathbf n > 1$ . Chiết suất n là một số không thứ nguyên lớn hơn 1.

# Bảng 35.1: Chiết suất của một số môi trường

# Some Indices of Refraction

TABLE35.1 Indices of Refraction   

<table><tr><td>Substance</td><td>Indexof Refraction</td><td>Substance</td><td>Index of Refraction</td></tr><tr><td>Solids at20°C</td><td></td><td>Liquids at20°C</td><td></td></tr><tr><td>Cubic zirconia</td><td>2.20</td><td>Benzene</td><td>1.501</td></tr><tr><td>Diamond (C)</td><td>2.419</td><td>Carbon disulfide</td><td>1.628</td></tr><tr><td>Fluorite (CaF2)</td><td>1.434</td><td>Carbon tetrachloride</td><td>1.461</td></tr><tr><td>Fusedquartz (SiO2)</td><td>1.458</td><td>Ethylalcohol</td><td>1.361</td></tr><tr><td>Gallium phosphide</td><td>3.50</td><td>Glycerin</td><td>1.473</td></tr><tr><td>Glass,crown</td><td>1.52</td><td>Water</td><td>1.333</td></tr><tr><td>Glass,flint</td><td>1.66</td><td></td><td></td></tr><tr><td>Ice (H2O)</td><td>1.309</td><td>Gasesat0°C,1atm</td><td></td></tr><tr><td>Polystyrene</td><td>1.49</td><td>Air</td><td>1.000293</td></tr><tr><td>Sodium chloride (NaCl)</td><td>1.544</td><td>Carbon dioxide</td><td>1.00045</td></tr></table>

### Tần số ánh sáng giữa hai môi trường

# Public_147 [Type here]   



Nội dung của chương này đề cập đến các ảnh được tạo thành khi chùm tia sáng gặp các bề mặt ngăn cách giữa hai môi trường. Các ảnh được tạo ra do sự phản xạ hoặc khúc xạ gây bởi các bề mặt này. Chúng ta có thể thiết kế các gương và thấu kính để tạo ra các ảnh có các đặc điểm như mong muốn. Trong chương này, ánh

sáng được thể hiện gần đúng như các tia và giả thiết rằng ánh sáng truyền đi theo đường thẳng. Đầu tiên chúng ta xem xét quá trình tạo ảnh bởi các loại gương và thấu kính và xác định vị trí cũng như kích thước của ảnh. Sau đó chúng ta sẽ kết hợp các gương và thấu kính để tạo ra các thiết bị quang học hữu ích như kính hiển vi và kính thiên văn.

## Ảnh tạo bởi gương phẳng

Xét một nguồn sáng điểm đặt ở O trước một gương phẳng và cách gương một đoạn $p$ như trong hình vẽ. Khoảng cách $p$ được gọi là khoảng cách vật. Chùm sáng phân kỳ từ nguồn đến gương và bị phản xạ bởi gương tạo ra chùm tia phản xạ cũng là chùm tia phân kỳ. Đường kéo dài (dường đứt nét trong hình) của chùm tia phản xạ giao nhau $\dot { \mathbf { O } }$ điểm $I .$ Chùm tia phản xạ dường như được phát ra từ điểm $I \overset { \triangledown } { \mathbf { \Vec { O } } }$ sau gương. Điểm $I$ được gọi là ảnh của vật ở O. Khoảng cách $q$ từ $I$ đến gương được gọi là khoảng cách ảnh.

![](images/image1.jpg)  
Gương Hình 36.1

Một ảnh tạo bởi giao điểm của các tia sáng gọi là ảnh thật và một ảnh tạo bởi đường kéo dài của các tia sáng gọi là ảnh ảo.

Ảnh của một vật tạo bởi gương phẳng luôn là ảnh ảo. Một ảnh thật có thể hứng được trên màn ảnh, còn ảnh ảo thì không.

Để xác định ảnh của một vật có kích thước, ta cần xác định ảnh của tất cả các điểm trên vật. Mặc dù có vô hạn tia sáng đi từ một điểm trên vật, nhưng chúng ta chỉ cần xét hai tia sáng phát ra từ điểm này và vẽ các tia phản xạ tương ứng nhờ định luật phản xạ ánh sáng để xác định vị trí ảnh. Trong hình 36.2, ảnh của điểm $P$ trên vật được xác định nhờ hai tia: tia $P Q$ và PR. Do hai tam giác PQR và $P ^ { \prime } Q R$ bằng nhau nên $P Q = P Q$ , vì vậy $| p | = | q |$ . Do đó ảnh tạo bởi gương phẳng của một vật đối xứng với vật qua gương.

Hình 36.2 cũng chỉ ra rằng chiều cao $h$ của vật bằng với chiều cao h’ của ảnh. Độ phóng đại ảnh của một vật được định nghĩa như sau:

$$
M = { \frac { c h i { \hat { \mathbf { e } } } u c a o { \hat { \mathbf { a } } } n h } { c h i { \hat { \mathbf { e } } } u c a o v { \hat { \mathbf { a } } } t } } = { \frac { h ^ { \prime } } { h } }
$$

![](images/image2.jpg)  
Hình 36.2

Định nghĩa này cũng sẽ được dùng cho tất cả các loại gương và thấu kính. M sẽ có giá trị dương khi ảnh và vật cùng chiều, $M$ sẽ có giá trị âm khi ảnh và vật ngược chiều. Với gương

[Type here]   



phẳng $M = + 1$ .

Bổ sung câu hỏi 36.1 vì tất cả các câu Quick Quiz đều có khả năng ra đề thi trắc nghiệm.

# Bài tập mẫu 36.1: Các ảnh tạo bởi hai gương.

Hai gương phẳng được đặt vuông góc nhau như hình 36.3 và vật được đặt ở O. Xác định các ảnh được tạo ra.

# Giải:

Ảnh của vật qua gương 1 là $I _ { 1 }$ và qua gương 2 là $I _ { 2 }$ . Ảnh $I _ { 3 }$ là ảnh của $I _ { 1 }$ qua gương 2 và cũng là ảnh của $I _ { 2 }$ qua gương 1.

![](images/image3.jpg)  
Hình 36.3

Bổ sung phần ứng dụng trong gương chiếu hậu của ô tô (như trong giáo trình gốc).

## Ảnh tạo bởi gương cầu

Có nhiều loại gương cong khác nhau nhưng ở đây chúng ta chỉ khảo sát gương có bề mặt là một phần của mặt cầu (thường là một chỏm cầu), gọi là gương cầu.

Trong hình 36.4, tâm $C$ của mặt cầu chứa gương gọi là tâm của gương, bán kính $R$ của mặt cầu này gọi là bán kính của gương. Đường thẳng qua $C$ và $V$ (V là điểm chính giữa của gương gọi là đỉnh gương) gọi là trục chính của gương. Nếu mặt phản xạ của gương là mặt lõm thì gọi là gương cầu lõm và nếu mặt phản xạ của gương là mặt lồi thì gọi là gương cầu lồi.

![](images/image4.jpg)  
Hình 36.4

### Gương cầu lõm

Xét một nguồn sáng điểm đặt trước gương tại một điểm $O$ tùy ý trên trục chính (Hình 36.5). Hai tia sáng phân kỳ từ $O$ tới gương cho hai tia phản xạ giao nhau tại ảnh I, rồi chúng phân kỳ từ $I$ như

Các tia phản xạ giao nhau ở các điểm khác nhau trên trục chính.

thể có một nguồn sáng tại đó. Ảnh $I$ này là ảnh thật.

![](images/image5.jpg)  
Gương   
Hình 36.5

Trong chương này chúng ta chỉ xét các tia sáng đi từ vật và tạo một góc nhỏ với trục chính (điều kiện tương điểm). Tất các tia này đều cho tia phản xạ qua một điểm duy nhất và làm cho ảnh của vật rõ nét. Các tia xa trục chính cho các tia phản xạ hội tụ tại các điểm khác nhau trên trục chính, tạo ra một ảnh mờ (Hình 36.6). Hiệu ứng này gọi

![](images/image6.jpg)  
Hình 36.6

[Type here] là cầu sai.



[Type here]   



Hình 36.7 cho phép chúng ta tính được khoảng cách ảnh $q$ khi biết khoảng cách vật $p$ và bán kính $R$ của gương. Các khoảng cách $p$ và $q$ là đo từ điểm V. Các tia sáng trong hình xuất phát từ đỉnh của vật: một tia qua $C$ cho tia phản xạ truyền ngược lại và một tia tới gương tại $V$ cho tia phản xạ đối xứng tia tới qua trục chính.

Từ hình vẽ ta có: $t a n \theta = h / p$ và $t a n \theta =$ $- h ^ { \prime } / q$ ( $h ^ { \prime } < 0$ vì ảnh ngược chiều với vật). Độ phóng đại ảnh

$$
M = { \frac { h ^ { \prime } } { h } } = - { \frac { q } { p } }
$$

Mặt khác ta cũng có:

$$
t a n \alpha = \frac { - h ^ { \prime } } { R - q } v \dot { { \mathrm { a } } } t a n \alpha = \frac { h } { p - R }
$$

![](images/image7.jpg)  
Hình 36.7

Suy ra:

$$
{ \frac { h ^ { \prime } } { h } } = - { \frac { R - q } { p - R } }
$$

Từ 36.2 và 36.3 ta được:

$$
{ \frac { R - q } { p - R } } = { \frac { q } { p } }
$$

Suy ra:

$$
\frac { 1 } { p } + \frac { 1 } { q } = \frac { 2 } { R }
$$

Phương trình 36.4 gọi là phương trình gương cầu.

Nếu vật ở rất xa gương, nghĩa là $p$ rất lớn so với $R$ thì $1 / p \approx 0$ và phương trình 36.4 cho $q \approx R / 2$ . Nghĩa là khi vật $\dot { \mathbf { O } }$ rất xa gương thì ảnh ở vị trí trung điểm của đoạn $C V$ như hình 36.8. Điểm ảnh đặc biệt này gọi là tiêu điểm $F$ và khoảng cách ảnh này gọi là tiêu cự $f ,$ trong đó

$$
f = { \frac { R } { 2 } }
$$

![](images/image8.jpg)

Tiêu cự f là một thông số đặc biệt của gương và được dùng để so sánh gương này với gương khác. Dùng f phương trình 36.4 được viết lại thành:

[Type here]



Hình 36.8

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { f } }
$$

[Type here]   



### Gương cầu lồi

Hình 36.9 cho thấy ảnh của vật $\dot { \mathbf { O } }$ trước gương là một ảnh ảo và luôn cùng chiều với vật nhưng nhỏ hơn vật.

Các phương trình 36.2, 36.4 và 36.6 sử dụng được cho cả gương cầu lõm và gương cầu lồi, nhưng cần tuân theo quy ước về dấu theo bảng 36.1.

![](images/image9.jpg)  
Hình 36.9

Bảng 36.1- Quy ước dấu cho gương cầu   



Đối với gương cầu lõm, khi cho vật từ xa gương tiến đến $F$ thì ảnh thật (ngược chiều với vật) sẽ tiến ra xa gương và càng lớn dần. Khi vật ở tại $F ,$ , ảnh $\dot { \mathbf { O } }$ xa vô cùng. Khi vật $\dot { \mathbf { O } }$ giữa $F$ và gương thì ảnh là ảo, cùng chiều với vật, lớn hơn vật và cứ lớn dần lên.

Đối với gương cầu lồi, ảnh luôn là ảo, cùng chiều và nhỏ hơn vật. Khi vật tiến về phía gương thì ảnh lớn dần và tiến về phía gương.

Bổ sung câu hỏi 36.2 và 36.3 vì tất cả các câu Quick Quiz đều có khả năng ra đề thi trắc nghiệm.

# Bài tập mẫu 36.2: Một gương cầu có tiêu cự 10,0 cm.

Một gương cầu có tiêu cự $1 0 { , } 0 \mathrm { c m }$ .

(A) Xác định vị trí và mô tả ảnh của một vật đặt cách gương $2 5 \mathrm { c m }$ .   
(B)Xác định vị trí và mô tả ảnh của một vật đặt cách gương $1 0 \mathrm { c m }$ .

Giải:

(A) Theo công thức gương cầu:

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { f } } \Rightarrow q = { \frac { p f } { p - f } } = { \frac { 2 5 . 1 0 } { 2 5 - 1 0 } } = 1 6 , 7 { \mathrm { ~ c m } }
$$

Độ phóng đại ảnh:

$$
M = - { \frac { q } { p } } = - 0 { , } 6 6 7
$$

Kết luận: Ảnh thu được là ảnh thật, nhỏ hơn vật và ngược chiều với vật.

(B)

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { f } } \qquad = > q = { \frac { p f } { p - f } } = { \frac { 1 0 . 1 0 } { 1 0 - 1 0 } } \to \infty
$$

Kết luận: Ảnh ở xa vô cực, nghĩa là chùm tia xuất phát từ vật đến gương cho chùm tia phản xạ song song nhau.

Bổ sung thêm bài tập mẫu 36.4 như trong giáo trình gốc

## Ảnh tạo bởi sự khúc xạ

Xét hai môi trường trong suốt có chiết suất $n _ { 1 }$ và $n _ { 2 }$ và ngăn cách nhau bởi mặt cầu có bán kính $R$ (Hình 36.16). Giả sử nguồn sáng điểm đặt ở $O$ trong môi trường có chiết suất ??1. Một chùm sáng từ $O$ khúc xạ $\dot { \mathbf { O } }$ mặt cầu và hội tụ $\dot { \mathrm { ~ o ~ } } I ,$ , là ảnh của nguồn.

![](images/image10.jpg)

[Type here]



Với một tia sáng từ $O$ khúc xạ qua I (Hình 36.17), định luật Snell cho

$$
n _ { 1 } s i n \theta _ { 1 } = n _ { 2 } s i n \theta _ { 2 }
$$

[Type here]   



Với các góc $\theta$ nhỏ sao cho có thể sử dung gần đúng ???????? $\approx \theta$ (góc $\theta$ tính theo radian) thì phương trình trên có thể viết lại thành

![](images/image11.jpg)

$$
n _ { 1 } \theta _ { 1 } = n _ { 2 } \theta _ { 2 }
$$

Theo hình vẽ ta cũng có

$$
\theta _ { 1 } = \alpha + \beta v \mathsf { \bar { a } } \beta = \theta _ { 2 } + \gamma
$$

Kết hợp các phương trình trên để khử $\theta _ { 1 }$ và $\theta _ { 2 }$ thì thu được

$$
n _ { 1 } \alpha + n _ { 2 } \gamma = ( n _ { 2 } - n _ { 1 } ) \beta
$$

Sử dụng các tam giác trong hình vẽ chúng ta cũng thu được các kết quả

$$
t a n \alpha \approx \alpha = \frac { d } { p } ~ ; t a n \beta \approx \beta = \frac { d } { R } ~ v \dot { \mathrm { a } } ~ t a n \gamma \approx \gamma = \frac { d } { q }
$$

Thay các biểu thức này vào (36.7) rồi rút gọn thì được

$$
{ \frac { n _ { 1 } } { p } } + { \frac { n _ { 2 } } { q } } = { \frac { n _ { 2 } - n _ { 1 } } { R } }
$$

Kết quả này không phụ thuộc ?? (với $\alpha$ nhỏ) nên tất cả các tia sáng đều hội tụ tại cùng một điểm ảnh I.

Để cho thuận tiện khi xét các trường hợp khác nhau, chúng ta gọi phía mặt ngăn cách chứa chùm sáng tới là phía trước và phía bên kia gọi là phía sau. Ngược với ảnh tạo bởi gương, ảnh thực tạo bởi các tia khúc xạ xuất hiện $\acute { \mathbf { O } }$ phía sau mặt ngăn cách nên quy ước về dấu cho $q$ và $R$ sẽ ngược với quy ước dấu cho gương.

![](images/image12.jpg)

# Sự khúc xạ qua các bề mặt phẳng

Nếu bề mặt khúc xạ là phẳng thì $R \to \infty$ và phương trình 36.8 trở thành

[Type here]



[Type here]   



Phương trình (36.9) cho thấy $q$ và $p$ ngược dấu nhau nên ảnh và vật ở cùng phía so với bề mặt khúc xạ như minh họa $\dot { \mathbf { O } }$ hình 36.18, nghĩa là ảnh thu được là ảnh ảo.

Bổ sung câu hỏi 36.4 và 36.5 vì tất cả các câu Quick Quiz đều có khả năng ra đề thi trắc nghiệm.

Bài tập mẫu 36.7: Một con cá đang bơi ở độ sâu d so với mặt nước của một hồ nước.

Một con cá đang bơi ở độ sâu $d$ so với mặt nước của một hồ nước. (A) Một người quan sát con cá theo hướng vuông góc với mặt nước sẽ thấy con cá ở độ sâu biểu kiến bằng bao nhiêu?

# Giải:

Từ phương trình (36.9), suy ra

$$
q = - \frac { n _ { 2 } } { n _ { 1 } } p = - \frac { 1 , 0 0 } { 1 , 3 3 } d = - 0 , 7 5 2 d
$$

$q < 0$ nên ảnh là ảo và người sẽ thấy con cá $\acute { \mathbf { O } }$ độ sâu biểu kiến khoảng bằng 3/4 độ sâu thực sự (Hình 36.20a).

![](images/image13.jpg)

(B) Nếu mặt của người quan sát cách mặt nước một đoạn $d$ thì con cá sẽ thấy mặt người cách mặt nước một đoạn biểu kiến bằng bao nhiêu?

# Giải:

Phương trình 36.9 cho

$$
\begin{array} { r l r } { q = - \frac { n _ { 2 } } { \bf \nabla } ^ { n _ { 1 } } } & { { } } & { p = \bf { \sigma } ^ { - } } \end{array}
$$



1,33   
1,00



Ảnh của mặt người là ảo, nghĩa là ảnh trong môi trường không khí trên mặt nước (Hình 36.20b).

(C) Nếu con cá có chiều cao thực sự là $h$ (đo từ vây trên đến vây dưới của con cá) thì chiều cao biểu kiến của con cá mà người quan sát nhìn thấy bằng bao nhiêu so với h?

Giải:

Ảnh của vây trên và vây dưới của con cá ở các vị trí

$$
q _ { 1 } = - 0 , 7 5 2 d v \dot { \mathsf { a } } q _ { 2 } = - 0 , 7 5 2 ( d + h )
$$

Chiều cao biểu kiến của con cá là

$$
h ^ { \prime } = q _ { 1 } - q _ { 2 } = 0 , 7 5 2 h
$$

Vì vậy chiều cao biểu kiến của con cá chỉ bằng khoảng 3/4 chiều cao thực của con cá.

## Ảnh tạo bởi thấu kính mỏng

Thấu kính thường được dùng để tạo ảnh bởi sự khúc xạ trong các hệ thống quang học của các thiết bị như máy ảnh, kính hiển vi, kính viễn vọng. Với thấu kính, ánh sáng sẽ khúc xạ ở cả hai bề mặt của thấu kính và ảnh do sự khúc xạ ở bề mặt thứ nhất của thấu kính sẽ trở thành vật đối với mặt thứ hai. Chúng ta sẽ xem xét thấu kính dày trước rồi cho độ dày của thấu kính xấp xỉ bằng không để có kết quả cho thấu kính mỏng.

Xét một thấu kính đặt trong không khí, thấu kính có chiết suất $n$ và được giới hạn bởi hai mặt cầu có bán kính là $R _ { 1 }$ và $R _ { 2 }$ như ở hình 36.21. Một vật được đặt ở $O$ sẽ cho ảnh tạo bởi bề mặt 1 ở $I _ { 1 }$ xác định bởi $q _ { 1 }$ thỏa phương trình

$$
{ \frac { 1 } { p _ { 1 } } } + { \frac { n } { q _ { 1 } } } = { \frac { n - 1 } { R _ { 1 } } }
$$

Nếu ảnh là ảo (như trong hình 36.21a) thì $q _ { 1 } < 0$ và nếu ảnh là thật (như trong hình 36.21b) thì $q _ { 1 } > 0$ .

[Type here]



![](images/image14.jpg)  
Hình 36.21

Đối với bề mặt thứ hai, vật và ảnh xác định bởi $p _ { 2 }$ và $q _ { 2 }$ thỏa phương trình

$$
{ \frac { n } { p _ { 2 } } } + { \frac { 1 } { q _ { 2 } } } = { \frac { 1 - n } { R _ { 2 } } }
$$

Gọi $t$ là độ dày của thấu kính thì $p _ { 2 } = . - q _ { 1 } + t .$ Đối với thấu kính mỏng (bề dày rất nhỏ so với các bán kính là $R _ { 1 }$ và $R _ { 2 }$ ) thì có thể bỏ qua $t$ nên $p _ { 2 } = - q _ { 1 }$ . Phương trình 36.11 trở thành

$$
- \frac { n } { q _ { 1 } } + \frac { 1 } { q _ { 2 } } = \frac { 1 - n } { R _ { 2 } }
$$

Kết hợp hai phương trình 36.10 và 36.12 chúng ta thu được

$$
\frac { 1 } { p _ { 1 } } + \frac { 1 } { q _ { 2 } } = ( n - 1 ) ( \frac { 1 } { R _ { 1 } } - \frac { 1 } { R _ { 2 } } )
$$

Với thấu kính mỏng, gọi $p$ và $q$ lần lượt là khoảng cách ảnh và khoảng cách vật như hình 36.22 thì phương trình 36.13 được viết lại thành

$$
\frac { 1 } { p } + \frac { 1 } { q } = ( n - 1 ) ( \frac { 1 } { R _ { 1 } } - \frac { 1 } { R _ { 2 } } )
$$

![](images/image15.jpg)

Tiêu cự f của một thấu kính mỏng là khoảng cách ảnh của vật ở xa vô cùng. Theo định nghĩa này chúng ta thu được công thức để xác định $f$ là

Hình 36.22

$$
\frac { 1 } { f } = ( n - 1 ) ( \frac { 1 } { R _ { 1 } } - \frac { 1 } { R _ { 2 } } )
$$



Chúng ta có thể viết phương trình 26.14 theo f như sau

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { f } }
$$

Phương trình 36.16 được gọi là phương trình thấu kính mỏng.

[Type here]



Một thấu kính có hai tiêu điểm $F _ { 1 }$ , $F _ { 2 }$ và hai tiêu điểm này có cùng khoảng cách tới thấu kính. Có hai loại thấu kính: thấu kính hội tụ và thấu kính phân kỳ. Hình 36.23 là một số hình dạng của hai loại thấu kính này.

![](images/image16.jpg)  
Hình 36.23. (a) Thấu kính hội tụ. (b) Thấu kính phân kỳ

Bảng 36.2 - Quy ước dấu cho thấu kính.



\* Đối với thấu kính phân kỳ

[Type here]



• Tia sáng tới thấu kính song song với trục chính, tia khúc xạ qua thấu kính có phương đi qua tiêu điểm ở trước thấu kính.

• Tia sáng tới có phương qua tiêu điểm ở sau thấu kính, tia khúc xạ qua thấu kính song song với trục chính.

• Tia sáng tới qua tâm của thấu kính cho tia khúc xạ truyền thẳng.

![](images/image17.jpg)  
Hình 36.22. Ảnh của vật qua thấu kính mỏng

Chỉnh kích thước của hình lớn lên

Đánh số sai hình (không đúng thứ tự)

Bài tập mẫu 36.8: Một thấu kính hội tụ có tiêu cự 10,0 cm.

(A) Một vật đặt cách thấu kính 30,0 cm. Tìm vị trí ảnh và mô tả ảnh. Vẽ hình.

Giải:

Từ phương trình thấu kính

$$
{ \frac { 1 } { p } } + { \frac { 1 } { q } } = { \frac { 1 } { f } }
$$

Suy ra:

![](images/image18.jpg)

$$
q = \frac { p . f } { p - f } = \frac { 3 0 . 1 0 } { 3 0 - 1 0 } = 1 5 c m
$$

Độ phóng đại ảnh:

Ảnh của vật là ảnh thật $\dot { \mathbf { O } }$ sau thấu kính, ngược chiều với vật, cao bằng 0,5 lần vật.

[Type here]



(B) Một vật đặt cách thấu kính 10,0 cm. Tìm vị trí ảnh và mô tả ảnh.

Giải:

Tương tự câu a,

[Type here]



$$
q = { \frac { p . f } { p - f } } = { \frac { 1 0 . 1 0 } { 1 0 - 1 0 } } \quad \Rightarrow \quad q \to \infty
$$

Ảnh ở xa vô cùng so với thấu kính

(C) Một vật đặt cách thấu kính 5,0 cm. Tìm vị trí ảnh và mô tả ảnh. Vẽ hình.

Giải:

Từ phương trình thấu kính, suy ra:

$$
q = { \frac { p . f } { p - f } } = { \frac { 5 . 1 0 } { 5 - 1 0 } } = - 1 0 c m
$$

Độ phóng đại ảnh:

$$
M = - \frac { q } { p } = - \frac { - 1 0 c m } { 5 c m } = 2
$$

![](images/image19.jpg)

Ảnh của vật là ảnh ảo, cùng chiều với vật, cao bằng hai lần vật.

Bổ sung bài tập mẫu 36.9 đối với thấu kính phân kỳ như trong giáo trình gốc

Hệ thấu kính mỏng.

Giả sử vật được đặt trước hệ gồm hai thấu kính. Ảnh của vật được xác định theo trình tự sau:

• Xác định ảnh của vật tạo ra bởi thấu kính thứ nhất như là khi không có thấu kính thứ hai.   
• Ảnh tạo ra bởi thấu kính thứ nhất là vật của thấu kính thứ hai. Nếu vật này ở sau thấu kính thứ hai thì vật này là vật ảo (nghĩa là $p < 0$ ).

Ảnh tạo bởi thấu kính thứ hai là ảnh tạo bởi hệ thống hai thấu kính trên.

Độ phóng đại ảnh của hệ hai thấu kính:

Cách thức xác định ảnh như trên cũng được sử dụng cho hệ gồm nhiều hơn hai thấu kính.

Trong trường hợp hệ hai thấu kính được đặt sát nhau thì ảnh của vật tạo bởi hệ giống như ảnh tạo bởi một thấu kính có tiêu cự f thỏa phương trình:

tr ng đó $f _ { 1 }$ và o $f _ { 2 }$ là tiêu cự

[Type here] của hai thấu kính.



Bài tập mẫu 36.10:

$$
{ \frac { 1 } { f } } = { \frac { 1 } { f _ { 1 } } } + { \frac { 1 } { f _ { 2 } } }
$$



Hai thấu kính hội tụ mỏng có tiêu cự lần lượt là $f _ { 1 } = 1 0 , 0$ ???? và $f _ { 2 } = 2 0 , 0$ ???? được đặt cách nhau $2 0 \mathrm { c m }$ . Một vật ở bên trái thấu kính thứ nhất và cách thấu kính này $3 0 \mathrm { c m }$ . Tìm vị trí và độ phóng đại của ảnh tạo ra bởi hệ hai thấu kính.

# Giải:

Vị trí của ảnh tạo ra bởi thấu kính thứ nhất:

$$
\begin{array} { c } { { q _ { 1 } = \displaystyle { \frac { p _ { 1 } f _ { 1 } } { p \phantom { - } - f } = \displaystyle { \frac { 3 0 . 1 0 } { 3 0 - 1 0 } } } } } \\ { { \phantom { q _ { 1 } = \displaystyle { \frac { p _ { 1 } f _ { 1 } } { 1 } - 1 } } } } \\ { { \phantom { q _ { 1 } = \displaystyle { \frac { p _ { 1 } f _ { 1 } } { p \phantom { - } - f } } } } } \end{array}
$$

Độ phóng đại ảnh này bằng:

$$
M _ { 1 } = - \frac { q _ { 1 } } { p _ { 1 } } = - 0 { , } 5
$$

Vật của thấu kính thứ hai (là ảnh trên) có khoảng cách vật là:

![](images/image20.jpg)  
Hình 36.30. Ví dụ

$$
p _ { 2 } = t - q _ { 1 } = 2 0 c m - 1 5 c m = 5 c m
$$

Vị trí của ảnh tạo ra bởi thấu kính thứ hai:

$$
q _ { 2 } = { \frac { p _ { 2 } f _ { 2 } } { p \ { \stackrel { - } { F } } \ } } = { \frac { 5 . 2 0 } { 5 \ { - 2 0 } } } = - 6 . 6 7 c m
$$

Độ phóng đại ảnh này bằng:

$$
\begin{array} { c c c } { { q _ { 2 } } } & { { 6 , 6 7 c m } } \\ { { M _ { 2 } = - \displaystyle \frac { } { p _ { 2 } } = - \displaystyle \frac { } { 5 c m } = 1 , 3 3 } } \end{array}
$$

Độ phóng đại của ảnh tạo ra bởi hệ hai thấu kính:

$$
M = M _ { 1 } . M _ { 2 } = - 0 . 6 6 7
$$

Nghĩa là ảnh tạo ra bởi hệ ở trước thấu kính thứ hai, ngược chiều với vật và nhỏ hơn vật.

## Quang sai

Các kết quả phân tích của chúng ta về gương và thấu kính được thực hiện với điều kiện các tia sáng tạo với trục chính một góc nhỏ (điều kiện tương điểm) và thấu kính là mỏng. Dưới các điều kiện này, mọi tia sáng đi từ một nguồn điểm đều hội tụ tại một điểm nên ảnh thu được sẽ sắc nét. Khi các điều kiện này không được thỏa, ảnh sẽ không hoàn hảo.

[Type here]   



Để phân tích chính xác về ảnh, chúng ta cần dùng định luật Snell để xác định sự phản xạ và khúc xạ cho mỗi tia sáng khi bị phản xạ hoặc khúc xạ ở các bề mặt. Theo cách thực hiện này, một điểm trên vật sẽ không tương ứng một điểm ảnh duy nhất và như vậy ảnh bị nhòe. Sự sai lệch của ảnh thực tế so với ảnh dự đoán (nhờ các kết quả thu được $\dot { \mathbf { O } }$ các nội dung trước) được gọi là quang sai.



# Các loại quang sai Cầu sai

Các tia khúc xạ giao nhau ở các điểm khác nhau trên trục chính.

Quang sai loại này xảy ra do tiêu điểm ứng với chùm tia sáng tới càng xa trục chính của thấu kính (hoặc gương) sẽ khác với tiêu điểm ứng với chùm tia sáng tới đi gần trục chính như hình minh họa 36.31 và 36.8. Nguyên nhân gây ra cầu sai là do sử dụng các thấu kính(hoặc gương) có bề mặt hình cầu.

Nhiều máy ảnh có khẩu độ điều chỉnh được để thay đổi cường độ sáng và giảm bớt cầu sai. Bằng cách giảm khẩu độ, ảnh thu được sẽ rõ nét nhưng cần tăng thời gian phơi sáng.

![](images/image21.jpg)  
Hình 36.31

Đối với gương, để giảm cầu sai thì dùng gương parabol thay cho gương cầu.

# Sắc sai

Các tia với bước sóng khác nhau hội tụ ở các điểm khác nhau.

Sắc sai xảy do chiết suất của môi trường trong suốt phụ thuộc vào bước sóng ánh sáng. Vì vậy khi sử dụng ánh sáng trắng, tia màu tím bị khúc xạ mạnh hơn tia màu đỏ. Điều này dẫn đến kết quả là tiêu cự thấu kính giảm dần đối với ánh sáng có màu từ đỏ đến tím như hình 36.32.

Sắc sai làm mờ ảnh. Để giảm sắc sai, có thể dùng kết hợp một thấu kính hội tụ và một thấu kính phân kỳ làm bằng hai loại thủy tinh có chiết suất khác nhau.

![](images/image22.jpg)

## Máy ảnh

Máy ảnh là một thiết bị quang học đơn giản được mô tả như hình 36.33. Máy ảnh gồm một buồng tối, một thấu kính hội tụ để tạo ra ảnh thật và một bộ phận nhạy sáng (để lưu ảnh) được điều chỉnh ở đúng vị trí của ảnh.

![](images/image23.jpg)  
Cảm biến   
Hình 36.33: Máy ảnh kỹ thuật số

Máy ảnh sẽ lưu ảnh trên phim hoặc được số hóa để lưu thông tin về ảnh vào một thẻ nhớ (máy ảnh kỹ thuật số). Bằng cách thay đổi khoảng cách từ thấu kính đến bộ phận lưu ảnh cho phù hợp chúng ta sẽ thu được ảnh rõ nét của vật.

Chưa nhắc đến khẩu độ

36.7 Mắt [Type here]



Giống như máy ảnh, mắt hội tụ áng sáng và tạo ra ảnh rõ nét. Mắt điều chỉnh lượng sáng đi vào và tạo ảnh bằng một cơ chế rất phức tạp, chính xác và hiệu quả hơn rất nhiều so với một máy ảnh tinh vi. Mắt thực sự là một kỳ quan sinh lý học.Hình 36.34 trình bày các thành phần cơ bản của mắt.

![](images/image24.jpg)  
Hình 36.34: Các thành phần cơ bản của mắt

Giác mạc là một màng mỏng cứng và trong suốt cho phép ánh sáng đi vào mắt. Lòng đen điều chỉnh lượng ánh sáng vào mắt bằng cách mở rộng ra khi gặp ánh sáng yếu hoặc thu hẹp lại khi gặp ánh sáng mạnh. Hệ thống giác mạc và thủy tinh thể hội tụ ánh sáng vào võng mạc, nơi đây gồm hàng triệu tế bào cảm thụ ánh sáng. Khi bị ánh sáng kích thích, các tế bào này sẽ gửi các xung về não nhờ các dây thần kinh thị giác giúp chúng ta cảm nhận được vật. Ảnh của vật được cảm nhận rõ khi ảnh này hiện ra ở võng mạc.

Khi cần nhìn một vật, hình dạng của thủy tinh thể được thay đổi (tiêu cự của thủy tinh thể thay đổi theo) cho phù hợp nhờ cơ vòng. Quá trình này gọi là sự điều tiết. Do khả năng điều tiết bị hạn chế nên mắt chỉ thấy rõ vật khi vật được đặt trong một khoảng giới hạn gọi là giới hạn nhìn rõ của mắt. Điểm gần mắt nhất của giới hạn nhìn rõ gọi là điểm cực cận và điểm xa mắt nhất gọi là điểm cực viễn. Người có mắt bình thường thì điểm cực cận cách mắt trung bình khoảng 25 cm và điểm cực viễn ở xa vô cùng. Tuy nhiên khi người càng lớn tuổi khoảng cách từ cực cận đến mắt sẽ tăng.

Có hai loại tế bào cảm thụ ánh sáng: tế bào hình que và tế bào hình nón. Tế bào hình que rất nhạy cảm với ánh sáng giúp chúng ta nhìn trong tối nhưng không phân biệt được màu sắc. Tế bào hình nón nhạy cảm với các bước sóng khác nhau của ánh sáng. Tế bào hình nón được chia thành ba loại: đỏ, xanh lá cây và xanh dương. Nếu hai loại tế bào hình nón đỏ và xanh là cây kích thích đồng thời, bộ não sẽ hiểu là màu vàng. Nếu cả ba loại tế bào hình nón đều bị kích thích đồng thời bởi các ánh sáng đỏ, xanh lá cây và xanh dương thì bộ não sẽ hiểu là màu trắng. cả ba loại tế bào hình nón đều bị kích thích đồng thời bởi các ánh sáng với mọi màu sắc khác nhauthì bộ não cũng sẽ hiểu là màu trắng.

Các tật của mắt Viễn thị

[Type here]   



Người bị viễn thị có thể nhìn rõ các vật ở xa nhưng không thể nhìn rõ các vật ở gần. Điểm cực cận của mắt người bị viễn thị ở xa hơn so với người có mắt bình thường. Khi nhìn các vật ở gần, khả năng khúc xạ của giác mạc và thủy tinh thể không đủ để hội tụ ánh sáng trên võng mạc (Hình 36.37a). Tật này có thể khắc phục bằng cách đeo kính hội tụ (Hình 36.37b) để hội tụ ánh sáng trên võng mạc.

![](images/image25.jpg)

Cận thị

![](images/image26.jpg)  
Hình 36.38

Người bị cận thị có thể nhìn rõ các vật ở gần nhưng không thể nhìn rõ các vật ở xa. Điểm cực viễn của mắt người bị cận thị không ở xa vô cực (như mắt bình thường) và có thể cách mắt nhỏ hơn 1m. Tiêu cự lớn nhất của mắt cận thị không đủ để tạo ra ảnh rõ nét của vật ở xa trên võng mạc mà ở trước võng mạc nên mắt không nhìn rõ được vật (Hình 36.38a). Tật này có thể khắc phục bằng cách đeo kính phân kỳ (Hình 36.38b) giúp điểm hội tụ ở trên võng mạc.

# Public_148 

Quang sóng là một nghiên cứu liên quan đến hiện tượng mà không thể được giải thích một cách đầy đủ bằng quang hình học. Đôi khi được gọi là quang vật lý. Những hiện tượng này bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : giao thoa, nhiễu xạ, phân cực. Trong chương 18, chúng ta đã nghiên cứu về mô hình giao thoa sóng và thấy rằng sự chồng chất của hai sóng cơ học có thể được tăng cường hay bị triệt tiêu. Trong cấu trúc giao thoa, biên độ của sóng tổng hợp lớn hơn biên độ của sóng thành phần nếu ở đó hiện tượng giao thoa được tăng cường (cực đại giao thoa). Trong khi đó, giao thoa triệt tiêu (cực tiểu giao thoa) có biên độ tổng hợp nhỏ hơn biên độ của sóng lớn hơn (khi có hai nguồn sóng). Sóng ánh sáng cũng giao thoa với nhau. Về cơ bản, tất cả sự giao thoa liên quan đến sóng ánh sáng phát sinh khi điện từ trường tạo thành sự kết hợp các sóng đơn lẻ.

## Giao thoa

### Sơ lược lịch sử

Người đầu tiên đề ra thuyết sóng ánh sáng có sức thuyết phục là nhà vật lý người Hà Lan Christiaan Huygens năm 1678. Ưu điểm lớn của nó là giải thích được những định luật về phản xạ và khúc xạ theo thuyết sóng và ý nghĩa vật lý của chiết suất.

![](images/image1.jpg)

Hình 37.1: (a) Sơ đồ thí nghiệm giao thoa khe Young. Hai khe S1 và $\mathrm { S } _ { 2 }$ được xem như hai nguồn sóng ánh sáng $\mathrm { k } \acute { \mathrm { e t } }$ hợp tạo thành sự giao thoa trên màn chắn (hình vẽ không theo tỷ lệ). (b) Bức tranh giao thoa được phóng to từ màn chắn.



$\mathrm { N } \breve { \bf a } \mathrm { m } 1 8 0 1$ , Thomas Young là người đầu tiên xây dựng lý thuyết sóng của ánh sáng trên một cơ sở thực nghiệm vững vàng khi chứng minh rằng hai sóng ánh sáng chồng lên nhau có thể giao thoa với nhau. Sơ đồ dụng cụ thí nghiệm của Young được thể hiện như trong hình 37.1a. Sóng ánh sáng của máy bay đến một rào chắn B (chứa hai khe $\mathrm { S } _ { 1 }$ và $\mathbf { S } _ { 2 }$ ). Ánh sáng từ hai khe $\mathrm { S } _ { 1 }$ , $\mathrm { S } _ { 2 }$ tạo ra trên màn quan sát thành các dải sáng, tối (được gọi là vân giao thoa) song song và cách đều nhau (hình 37.1b). Khi tia sáng từ hai khe $\mathrm { S } _ { 1 }$ và $\mathrm { S } _ { 2 }$ hội tụ tại một điểm trên màn cùng một lúc thì chúng tăng cường lẫn nhau và tạo thành vân sáng (cực đại giao thoa) tại điểm đó. Ngược lại, khi ánh sáng từ hai khe triệt tiêu nhau tại bất cứ vị trí nào trên màn thì chúng triệt tiêu lẫn nhau và tạo thành vân tối (cực tiểu giao thoa).

### Giao thoa ánh sáng

Hình 37.2 cho thấy hình ảnh giao thoa thực sự tạo nên trên bề mặt của một bể chứa nước. Các sóng được phát đi từ hai quả cầu nối với cùng một máy rung cơ học và dao động lên xuống đối với mặt nước. Hai quả cầu này làm nhiệm vụ giống như hai khe S1 và S2 của hình 37.1, chúng là các nguồn của hai sóng chồng lên nhau để tạo nên hình ảnh giao thoa.

![](images/image2.jpg)  
Hình 37.2: Bức tranh giao thoa thu được từ các sóng nước được tạo ra từ hai nguồn rung trên bề mặt của một bể nước.

Ánh sáng từ hai khe hẹp hình thành một ảnh hiển thị trên màn quan sát. Ảnh gồm một loạt những vạch sáng tối xen kẽ song song nhau được gọi là vân.

• Giao thoa cực đại (tăng cường) sẽ xảy ra nơi mà một vân sáng xuất hiện.   
• Giao thoa cực tiểu (triệt tiêu) sẽ hình thành một vân tối.

# Cực đại giao thoa

Giả sử có hai sóng giao thoa xảy ra tại điểm O. Hai sóng lan truyền cùng một khoảng cách. Do đó, chúng đến cùng pha. Kết quả là, giao thoa xảy ra tại điểm này và một vân sáng trung tâm sẽ được quan sát (hình 37.3a).

Sóng tần số thấp hơn phải lan truyền xa hơn sóng tần số cao để đạt đến điểm P. Sóng tần số thấp hơn sẽ lan truyền một bước sóng lớn hơn. Do đó, các sóng đến cùng pha. Một vân



sáng thứ hai xảy ra tại vị trí này (hình 37.3b).



# Cực tiểu giao thoa

Sóng tần số cao lan truyền xa hơn một nửa bước sóng so với sóng có tần số thấp để đạt đến điểm R. Sóng có tần số cao trùng với đỉnh của sóng có tần số thấp hơn nên giao thoa bị triệt tiêu (hình 37.3c).

![](images/image3.jpg)  
Hình 37.3: Trong thí nghiệm giao thoa của Young, ánh sáng nhiễu xạ từ hai khe S1, S2 chồng trên nhau tạo nên các điểm giao thoa trên màn quan sát: (a) vân sáng trung tâm, (b) cực đại giao thoa, (c) cực tiểu giao thoa.

Điều kiện giao thoa: Để xuất hiện hình ảnh giao thoa trên màn quan sát từ hai nguồn phải thỏa mãn những điều kiện sau đây:

Các nguồn phát ánh sáng là nguồn kết hợp, có nghĩa là hiệu số pha dao động phải không đổi theo thời gian. Các nguồn sáng đơn sắc, có nghĩa là chúng phải có cùng một giá trị bước sóng.

# Cách tạo các nguồn kết hợp

Ánh sáng từ một nguồn đơn sắc được sử dụng để chiếu vào một rào chắn. Rào chắn chứa hai khe hở (hẹp), có hình dạng rãnh (như thí nghiệm của Young được minh họa trong hình 37.1).

Ánh sáng ló ra từ hai khe sáng tương quan nhau vì một nguồn duy nhất sẽ tạo ra chùm sáng ban đầu, đây là một phương pháp thường được sử dụng.

### Nhiễu xạ qua khe Young

Nếu ánh sáng vẫn lan truyền theo hướng ban đầu sau khi đi qua các khe thì không có hiện tượng giao thoa (hình 37.4a). Theo nguyên lý Huygens, sóng phát ra từ các khe sẽ bị lan



ra (phân kỳ) thành nhiều hướng khác nhau được gọi là nhiễu xạ (hình 37.4b).



![](images/image4.jpg)  
Hình 37.4: (a) Nếu sóng ánh sáng không lan ra sau khi đi qua các khe hẹp thì không xảy ra hiện tượng giao thoa. (b) Sóng ánh sáng từ hai khe chồng chất lên nhau khi chúng bị nhiễu xạ.

## Thí nghiệm giao thoa khe Young kép

Hình 37.5 cho thấy tia sáng truyền từ hai khe $\mathrm { S } _ { 1 }$ và $\mathrm { S } _ { 2 }$ trên màn B đến một điểm P trên màn quan sát. Màn quan sát được đặt vuông góc với khoảng cách từ màn chắn chứa hai khe một khoảng L. Trục chính được vẽ từ điểm chính giữa hai khe đến màn quan sát, P được xác định bởi góc θ với trục chính, y là khoảng cách từ điểm P đến trục chính.

![](images/image5.jpg)



Hình 37.5: (a) Cấu trúc hình học mô tả thí nghiệm giao thoa khe Young (hình vẽ không theo tỷ lệ). (b) Khi L $> > \mathrm { d }$ chúng ta xem gần đúng các tia r1 và r2 song song với nhau khi chúng đến P.

Sóng ánh sáng đi qua $\mathrm { S } _ { 2 }$ cùng pha với sóng ánh sáng đi qua $\mathrm { S } _ { 1 }$ vì hai sóng này là những phần của một sóng duy nhất dọi vào màn chắn B. Tuy nhiên, sóng đến $\mathrm { P }$ từ nguồn $\mathrm { S } _ { 2 }$ không thể cùng pha với sóng đến $\mathrm { P }$ từ $\mathrm { S } _ { 1 }$ vì rằng sóng thứ hai phải đi qua một quãng đường dài hơn sóng thứ nhất.

Điều kiện cực đại giao thoa: Nếu như hiệu quang lộ bằng không hoặc bằng một bội số nguyên lần bước sóng thì các sóng tới sẽ cùng pha với nhau và khi giao thoa sẽ tăng cường nhau, tạo thành cực đại giao thoa (vân sáng).

$$
\delta = \mathrm { d } \sin \theta = \mathrm { m } \lambda , \mathrm { v } \dot { \mathrm { o i } } \mathrm { m } = 0 , \pm 1 , \pm 2 . . . .
$$

Khi: $\mathrm { m } = 0$ , gọi là cực đại bậc không. $\mathbf { m } = \pm 1$ , gọi là cực đại bậc một. $\mathbf { m } = \pm 2$ , gọi là cực đại bậc hai.



Hiệu quang lộ  (đối với giao thoa cực đại) tương ứng với độ lệch pha $2 \pi$ rad. Hiệu quang lộ cùng tỉ lệ với $\lambda$ khi độ lệch pha $\boldsymbol { \Phi }$ bằng $2 \pi$ . Độ lệch pha giữa hai sóng tại $\mathrm { P }$ phụ thuộc vào hiệu quang lộ của chúng: $\delta = \mathbf { r } _ { 2 } - \mathbf { r } _ { 1 } = \mathrm { d } \mathrm { s i n } \theta$

$$
\Phi = \frac { 2 \pi } { \lambda } \delta = \frac { 2 \pi } { \lambda } \mathrm { d s i n } \Theta
$$

biểu thức (37.10) cho thấy, độ lệch pha $\boldsymbol { \Phi }$ phụ thuộc vào góc θ (như trong hình 37.5).

Hình 37.6 là đồ thị của phương trình (37.14) biểu thị cường độ của hình ảnh giao thoa của hai khe như một hàm của dsin . Chú ý rằng từ phương trình (37.14) cường độ biến thiên từ 0 tại vân cực tiểu đến Imax tại vân cực đại.

Với hệ nhiều hơn 2 khe hẹp (hình 37.7), ảnh nhiễu xạ chứa các cực đại chính và cực đại phụ. Đối với N khe hẹp thì cường độ của các cực đại chính lớn hơn $\mathrm { N } ^ { 2 }$ lần so với cường độ của các cực đại tạo bởi 1 khe hẹp. Khi số khe hẹp tăng lên thì cường độ của các cực đại chính cũng tăng và trở nên hẹp hơn, khi đó, các cực đại phụ giảm theo cường độ tương đối so với các cực đại chính. Số cực đại phụ bằng N−2, trong đó N là số khe hẹp. Hiện tượng giao thoa không thể sinh ra hoặc làm biến mất năng lượng mà chỉ đơn thuần là phân bố lại cường độ ánh sáng trên màn quan sát.

![](images/image6.jpg)  
Hình 37.6: Sự phụ thuộc của cường độ ánh sáng vào hiệu quang lộ giữa

hai sóng khi màn quan sát được đặt rất xa so với khoảng cách giữa hai khe hẹp ( $\mathrm { ~ L ~ } \gg \mathrm { ~ d ~ }$ ).



Hình 37.7: Hình ảnh giao thoa nhiều khe. Khi số khe N tăng lên thì cực đại chính (các đỉnh cao nhất trong mỗi biểu đồ) càng hẹp hơn nhưng vẫn giữ nguyên vị trí và số lượng cực đại phụ tăng lên.



## Gương LLOYD

Trong phương pháp giao thoa khe Young đã tạo được hai nguồn sáng kết hợp xuất phát từ một nguồn duy nhất. Phương pháp đơn giản khác cũng tạo được hai nguồn kết hợp là dùng gương Lloyd. Một nguồn sáng điểm S được đặt gần một gương phẳng và một màn quan sát được đặt ở xa và vuông góc với gương phẳng như hình 37.8. Ánh sáng đến điểm quan sát P trên màn có thể được truyền trực tiếp từ nguồn S hoặc có thể được truyền từ S tới gương, bị phản xạ rồi tới P. Tia phản xạ có thể được xem như xuất phát từ nguồn S’ là ảnh của S qua gương phẳng. S và S’ là hai nguồn sáng kết hợp, tương tự như hai khe Young. Tuy nhiên, những điểm theo lý thuyết (thí nghiệm khe Young) được dự đoán là điểm sáng thì thực tế lại là điểm tối và ngược lại. Điều này chứng tỏ hai nguồn S và S’ ngược pha với nhau.

Xét điểm P’ là giao giữa gương và màn quan sát (P’ cách đều S và S’). Nếu sự khác biệt về quãng đường dẫn đến sự khác biệt về pha thì chúng ta sẽ thấy một vân sáng tại $\mathbf { P } '$ (hiệu quang lộ bằng không), tương ứng với vân sáng trung tâm cho hệ giao thoa hai khe. Thay vào đó, một vân tối được quan sát tại P’. Vậy, khi phản xạ trên bề mặt gương, tia phản xạ ngược pha với tia tới hay quang lộ của tia phản xạ tăng thêm nửa bước sóng.

Xung phản xạ trên một sợi dây đàn hồi trải qua sự thay đổi pha $1 8 0 ^ { \mathrm { o } }$ khi bị phản xạ từ ranh giới của một sợi dây dày hoặc một trụ chống đỡ cố định, nhưng không có sự thay đổi pha khi xung được phản xạ từ sợi dây mãnh hoặc một trụ chống đỡ cố định. Tương tự, một sóng điện từ bị thay đổi pha $1 8 0 ^ { \mathrm { o } }$ (hay $\pi$ rad) khi bị phản xạ từ môi trường có chiết suất lớn hơn chiết suất của môi trường tới (hình 37.9a). Nếu phản xạ từ môi trường có chiết suất nhỏ hơn chiết suất của môi trường tới thì tia phản xạ không bị thay đổi pha (hình 37.9b). Tương tự như một xung trên một sợi dây bị phản xạ từ một cột chống đỡ.

Hinh ành giao thoa hien trèn màn quan sát là sy két hop giüa tia sáng truc tiép (1) và tia phàn xa

![](images/image7.jpg)  
Hình 37.8: Gương Lloyd. Tia phản xạ bị đổi pha $1 8 0 ^ { \mathrm { o } }$ .



![](images/image8.jpg)

Hình 37.9: So sáng sự phản xạ của sóng ánh sáng và sóng trên dây: (a) Sự biến đổi pha do phản xạ, (b) Sự biến đổi pha do đổi pha.

## Giao thoa của màn mỏng

### Giao thoa do phản xạ

Màu sắc mà chúng ta nhìn thấy được từ ánh sáng mặt trời đập trên một bong bóng xà phòng hoặc trên ván dầu là kết quả giao thoa của sóng ánh sáng phản xạ từ mặt ngoài và mặt trong của một bản mỏng trong suốt.

Giả sử các tia sáng lan truyền trong không khí hầu như vuông góc với hai bề mặt của màng mỏng. Tia phản xạ 1 bị phản xạ tại mặt trên (A) trải qua sự biến đổi pha $1 8 0 ^ { 0 }$ so với tia tới. Tia 2 bị phản xạ tại bề mặt màng dưới (B) không bị thay đổi pha vì chiết suất của không khí nhỏ hơn màng mỏng. Vì vậy, tia phản xạ 1 bị lệch pha $1 8 0 ^ { \mathrm { o } }$ so với tia phản xạ 2, khi đó hiệu quang lộ giữa chúng là $\lambda _ { \mathrm { n } } / 2$ . Tuy nhiên, tia phản xạ 2 di chuyển xa hơn tia phản xạ 1

Các yếu tố ảnh hưởng tới sự giao thoa:

• Pha có thể sẽ bị đảo ngược trong sự phản xạ • Hiệu quang lộ

# Chú ý:

• Các điều kiện sẽ thỏa mãn nếu môi trường ở bề mặt trên của màng mỏng giống với môi trường ở bề mặt dưới của nó. Nếu có những môi trường khác nhau, những điều kiện này sẽ đúng nếu chiết suất cả hai môi trường nhỏ hơn n.

• Nếu màng mỏng giữa hai môi trường, một môi trường có chiết suất nhỏ hơn màng mỏng và môi ó chiết suất cao hơn chiết suất màng mỏng, những điều kiện cho giao thoa cực đại và giao thoa cực tiểu sẽ bị đảo ngược.

![](images/image9.jpg)  
Caác tia 3 và 4 tao hieu ing giao thoa do ánh sáng truyèn



Với các vật liệu khác nhau trên 2 mặt của màng, có thể có một sự biến đổi pha $1 8 0 ^ { 0 }$ tại cả hai bề mặt hoặc không bề mặt nào, do đó phải kiểm tra hiệu quang lộ và biến đổi pha.

Hình 37.10: Giao thoa qua màn mỏng.



![](images/image10.jpg)  
Hình 37.11: Giao thoa qua màng mỏng − bong bóng xà phòng.

(a) Một màn mỏng dầu nổi trên mặt nước được thể hiện bằng các hoa văn màu sắc khi ánh sáng trắng tương tác với màn mỏng, (b) Giao thoa qua bong bóng xà phòng, màu sắc có được là do sự giao thoa giữa các tia sáng phản chiếu từ bên trong và bên ngoài bề mặt của màn xà phòng.

### Vân tròn Newton

Một phương pháp khác để quan sát giao thoa sóng ánh sáng là đặt một thấu kính phẳng − lồi lên trên tấm thủy tinh phẳng như hình 37.12a. Với sự sắp xếp này, lớp không khí giữa tấm thủy tinh và mặt cong của thấu kính tạo thành một bản mỏng không khí có bề dày thay đổi. Điểm quan sát M nằm trên bề mặt cong của thấu kính, cách quang trục của thấu kính một khoảng r và cách tấm thủy tinh một khoảng d. Nếu bán kính mặt cong R của thấu kính rất lớn so với khoảng cách r và hệ thống được quan sát từ phía trên, gần với trục chính của thấu kính thì ảnh giao thoa quan sát được là các vòng sáng, tối xen kẽ nhau (vân giao thoa quan sát bằng ánh sáng phản xạ với cách bố trí như hình 37.12b là những đường tròn đồng tâm). Ảnh giao thoa này được Newton khám phá ra nên được gọi là vân tròn Newton.

![](images/image11.jpg)

![](images/image12.jpg)



Hình 37.12: Vân tròn Newton: (a) Thí nghiệm, (b) Hình ảnh vân tròn.



Các vân tròn sáng, tối quan sát được là do hiệu ứng giao thoa của hai chùm tia phản xạ 1 và 2. Chùm tia 1 phản xạ tại bề mặt cong của thấu kính. Chùm tia này không bị đổi pha, vì chiết suất của không khí nhỏ hơn chiết suất của chất làm thấu kính. Chùm tia 2 phản xạ tại bề mặt tấm thủy tinh có chiết suất lớn hơn chiết suất không khí nên pha được tăng thêm $1 8 0 ^ { 0 }$ , hay quang lộ tăng thêm $\lambda / 2$ . Bán kính của các vân sáng, vân tối phụ thuộc vào bán kính mặt cong R và bước sóng $\lambda$ .

Vân sáng: bề dày của lớp không khí giữa hai bản thỏa mãn:

$$
\mathrm { d } = \left( 2 \mathrm { m } + 1 \right) _ { 4 } ^ { \underline { { \lambda } } }
$$

Vân tối: bề dày của lớp không khí giữa hai bản thỏa mãn:

$$
\mathbf { d } = \mathbf { m } { \frac { \lambda } { 2 } }
$$

Các vân giao thoa là các vòng tròn tại tâm O $( \mathrm { d } { < } { < } \mathrm { R } )$ . Bán kính của các vân tối thỏa mãn điều kiện:

$$
{ \bf r } ^ { 2 } = { \bf R } ^ { 2 } - \left( { \bf R } - { \bf d } { \bf \Delta } \right) ^ { 2 } \approx 2 { \bf R } { \bf d }
$$

Thay thế: d ${ \bf d } _ { \mathrm { { m } } } = { \bf m } { \frac { \lambda } { 2 } }$ vào biểu thức (37.21), ta được:

$$
{ \bf r } _ { \mathrm { m } } \approx \sqrt { { \bf m } \lambda { \bf R } / { \bf n } }
$$

Chiến thuật giải bài toán với giao thoa của màng mỏng: Khi giải bài toán giao thoa của màng mỏng cần chú ý một số vấn đề sau đây:

Đặc điểm: Nhận dạng nguồn sáng, vị trí của người quan sát.

Phân loại: Nhận dạng màng mỏng gây ra giao thoa

Phân tích:

Loại giao thoa xuất hiện được xác định bởi mối quan hệ giữa tỷ lệ bước sóng phản chiếu bên trên và bên dưới bề mặt của màng mỏng.

• Độ lệch pha thay đổi dựa vào hiệu quang lộ hoặc các biến đổi pha xảy ra nếu như phản xạ. Cả hai nguyên nhân cần được xem xét khi xác định giao thoa cực đại và giao thoa cực tiểu.



• Xác định chiết suất của môi trường để xác định các phương trình đúng.

Kiểm tra: Kiểm tra kết quả tính toán cuối cùng xem có hợp lý hay không, ý nghĩa vật lý như thế nào.



## Giao thoa $\mathbf { k } \hat { \mathbf { e } }$ Michelson

Giao thoa $\mathrm { k } \acute { \mathrm { e } }$ được phát minh bởi nhà Vật lý người Mỹ A. A. Michelson. Giao thoa kế chia ánh sáng làm hai phần và sau đó tái kết hợp các phần để tạo thành ảnh giao thoa. Thiết bị có thể được sử dụng để đo bước sóng hoặc độ dài với độ chính xác cao.

Sơ đồ nguyên lý: Một tia sáng được chia thành hai tia bởi gương M0. Gương được bố trí nghiêng $4 5 ^ { 0 }$ so với chùm tia tới. Gương đóng vai trò là bộ tách chùm tia, nó truyền qua một nửa tia sáng và phản xạ phần còn lại. Tia phản xạ đi về phía gương M1 (gương M1 có thể di chuyển được) cách $\mathrm { M } _ { 0 } \ \mathrm { m } \hat { \mathrm { ~ } } { \mathrm { t ~ } }$ đoạn L1. Tia sáng truyền qua đi về phía gương M2 cách M0 một đoạn L2. Sau khi phản xạ trên M1 và M2, các tia phản xạ tái kết hợp tại M0 và hình thành ảnh giao thoa. Ảnh giao thoa được quan sát bởi kính ngắm Telescope.

Nguyên lý hoạt động: Điều kiện giao thoa cho hai tia sáng được xác định bởi hiệu quang lộ giữa chúng. Khi dịch chuyển gương $\mathbf { M } _ { 1 }$ song song với trục chính của nó và dọc theo tia sáng ra xa một đoạn $\lambda / 4$ thì hiệu quang lộ của tia phản xạ tăng thêm  2 và hệ vân giao thoa dịch chuyển đi một nửa khoảng vân. Độ dài của bước sóng ánh sáng được đo bằng cách đếm số vân dịch chuyển cho mỗi lần dịch gương M1.

![](images/image13.jpg)  
Hình 37.14: Giao thoa kế Michelson cho thấy đường đi của ánh sáng bắt đầu từ nguồn sáng. Gương M0 tách ánh sáng thành 2 chùm phản xạ từ các gương $\mathbf { M } _ { 1 }$ và M2 trở về $\mathrm { M } _ { 0 }$ và sau đó đến kính ngắm Telescope.

Ứng dụng: Giao thoa kế Michelson đã được sử dụng để bác bỏ ý tưởng Trái đất chuyển động xuyên qua một vòng trời. Một số ứng dụng hiện đại, bao gồm: Quang phổ hồng ngoại biến đổi Fourier (FTIR) và đài quan sát sóng hấp dẫn dùng giao thoa $\mathrm { k } \acute { \mathrm { e } }$ Laser (LIGO).



Quang phổ hồng ngoại biến đổi Fourier: Được dùng để tạo một phổ với độ phân giải cao trong một khoảng thời gian rất ngắn. Kết quả là một tập hợp các dữ liệu liên quan cường độ sáng phụ thuộc vào vị trí của gương. Nó được gọi là ảnh giao thoa (interferogram). Ảnh giao thoa có thể được phân tích bởi máy tính để cung cấp tất cả các thành phần của bước sóng. Quá trình này được gọi là biến đổi Fourier.

• Đài quan sát sóng hấp dẫn dùng giao thoa kế Lazer: Thuyết tương đối rộng tiên đoán sự tồn tại của sóng hấp dẫn. Theo lý thuyết của Einstein, trọng lực tương đương với một biến đổi của không gian, những biến đổi này có thể lan truyền trong không gian. Thiết bị LEGO được thiết kế để phát hiện sự biến dạng tạo bởi một rung động khi nó băng qua gần Trái đất. Giao thoa $\mathrm { k } \acute { \mathrm { e } }$ sử dụng chùm tia lazer với hiệu quang lộ khoảng vài km. Tại điểm cuối của một nhánh của giao thoa $\mathbf { k } \acute { \hat { \mathbf { e } } } ,$ , một gương được gắn vào một con lắc lớn. Khi một sóng hấp dẫn đi qua, con lắc di chuyển và tạo ảnh giao thoa tạo bởi các chùm tia lazer từ hai nhánh sẽ thay đổi.

Nhờ giao thoa kế của Michelson mà ta so sánh được chiều dài của mét mẫu so với bước sóng ánh sáng, là cơ sở để định nghĩa mét qua bước sóng ánh sáng. Cũng chính nhờ giao thoa kế của mình, năm 1881, Michelson đã tiến hành thí nghiệm chứng tỏ rằng vận tốc ánh sáng trong chân không là bằng nhau và bằng ${ \mathrm { c } } = 3 . 1 0 ^ { 8 } { \mathrm { m } } / { \mathrm { s } }$ trong tất cả các hệ qui chiếu quán tính – là một cơ sở thực nghiệm để Einstein xây dựng lý thuyết tương đối năm 1907.

![](images/image14.jpg)

Hình 37.15: Đài quan sát sóng hấp dẫn bằng giao thoa kế Lazer (LIGO) gần Richland, Washington. Chú ý hai nhánh vuông góc của giao thoa kế Michelson.



# Tóm tắt chương 37

Định nghĩa

Giao thoa ánh sáng xuất hiện khi hai sóng (hoặc nhiều hơn) chồng lấp lên nhau tại một điểm nhất định. Hình ảnh giao thoa được quan sát khi các nguồn phát ánh sáng là nguồn kết hợp và có bước sóng xác định.

Cường độ tại một điểm trong mô hình giao thoa hai khe được xác định:

$$
\mathrm { I } = \mathrm { I } _ { \mathrm { m a x } } \cos ^ { 2 } \left( { \frac { \pi \mathrm { d } \sin \theta } { \lambda } } \right)
$$

trong đó, Imax là cường độ cực đại trên màn quan sát.

# Phân tích mô hình và giải quyết vấn đề

Thí nghiệm giao thoa khe Young đóng vai trò như một nguyên mẫu cho hiện tượng giao thoa liên quan đến bức xạ điện từ. Trong thí nghiệm này, hai khe cách nhau một khoảng a được chiếu sáng bởi nguồn ánh sáng đơn sắc. Điều kiện cho vân sáng (cực đại giao thoa) là:

Điều kiện cho vân tối (cực tiểu giao thoa) là:

$$
\delta = \mathrm { d } \mathrm { s i n } \theta = \left( \mathrm { m } + \frac { 1 } { 2 } \right) \rho , \mathrm { v } \Dot { \mathrm { o i } } \mathrm { m } = 0 , \pm 1 , \pm 2 . . . .
$$

# Câu hỏi lý thuyết chương 37

1. Một chùm ánh sáng đơn sắc có bước sóng 500 nm chiếu đến hai khe hẹp cách nhau $2 \mathrm { m }$ . Góc tạo bởi vân sáng thứ hai so với vân sáng trung tâm là?

(a) 0,05 rad (b) 0,025 rad (c) 0,1 rad (d) 0,25 rad (e) 0,01 rad

2. Một màn bong bóng xà phòng được dựng thẳng đứng trong không khí và quan sát hiện tượng phản xạ ánh sáng như trong hình 37.16. Giải thích tại sao màn bong bóng xà phòng tối ở phần đầu?

![](images/image15.jpg)  
Hình 37.16



3. (a) Trong thí nghiệm giao thoa khe Young, tại sao chúng ta dùng ánh sáng đơn sắc? (b) Nếu sử dụng áng sáng trắng thì hệ vân giao thoa trên màn sẽ thay đổi như thế nào?

4. Giải thích tại sao khi đặt hai đèn pin $\mathrm { g } \dot { \hat { \mathrm { a } } } \mathrm { n }$ nhau thì không tạo ra hệ vân giao thoa trên màn quan sát?

# Bài tập chương 37

37.1. Người ta thực hiện giao thoa ánh sáng đơn sắc bằng hai khe Young cách nhau $0 { , } 3 2 \mathrm { m m }$ với ánh sáng có bước sóng $\lambda = 5 0 0 \mathrm { n m }$ . Hãy xác định số cực đại giao thoa có được khi thay đổi góc lệch $- 3 0 ^ { 0 } < \Theta < 3 0 ^ { 0 }$ .

ĐS: 641 cực đại

37.2. Trong thí nghiệm Young về hiện tượng giao thoa ánh sáng, nguồn sáng đơn sắc có bước sóng $5 3 0 ~ \mathrm { n m }$ . Khoảng cách giữa hai khe hẹp $\mathrm { S } _ { 1 }$ và $\mathbf { S } _ { 2 }$ là $0 { , } 3 ~ \mathrm { m m }$ . Vân giao thoa được hứng trên một màn ảnh đặt sau hai khe, song song với chúng và cách chúng $2 \textrm { m }$ . Xác định khoảng cách giữa vân tối thứ nhất và thứ hai.

ĐS: 3,53 mm

37.3. Chiếu một chùm tia lazer vào hai khe hẹp cách nhau $0 { , } 2 ~ \mathrm { m m }$ , khoảng cách từ hai khe đến màn quan sát là $5 \mathrm { m }$ . Xảy ra hiện tượng giao thoa trên màn quan sát. Nếu góc hợp bởi vân sáng trung tâm và vân sáng bậc 1 là $0 { , } 1 8 1 ^ { 0 }$ thì giá trị bước sóng của nguồn sáng lazer là bao nhiêu.

ĐS: 632 nm

37.4. Thí nghiệm giao thoa khe Young được thực hiện với đèn lazer argon (màu xanh lam). Khoảng cách giữa hai khe là $0 { , } 5 \mathrm { m m }$ , khoảng cách từ hai khe đến màn quan sát là $^ { 3 , 3 \mathrm { ~ m ~ } }$ . Vân sáng đầu tiên cách vân sáng trung tâm một khoảng $\dot { \mathrm { ~ a ~ } } 3 , 4 \mathrm { ~ m m }$ . Hãy xác định giá trị bước sóng của ánh sáng lazer argon.

ĐS: 515 nm

37.5. Tại sao trường hợp sau đây không thể xảy ra? Hai khe hẹp trên một tấm kim loại đặt cách nhau 8 mm. Một chùm sóng cực ngắn được chiếu vuông góc đến tấm kim loại đi qua hai khe và được hứng ảnh trên màn quan sát. Cho biết bước sóng của bức xạ là $1 , 0 0 \mathrm { \ : \vec { c m } \pm 5 \% } ,$ , nhưng chúng ta muốn đo chính xác hơn giá trị của bước sóng. Di chuyển đầu dò sóng cực ngắn dọc theo đường thẳng song song với màn quan sát để khảo sát hình ảnh giao thoa, chúng ta đo được vị trí của vân sáng bậc 1, từ đó xác định được chính xác giá trị bước sóng của nguồn bức xạ.

ĐS: $\sin \theta _ { \mathrm { s i n g } } = 1 , 2 5$ (không thể xảy ra)

37.6. Hai khe Young $\mathrm { S } _ { 1 } \mathrm { S } _ { 2 }$ cách nhau một khoảng d được chiếu bằng ánh sáng có bước sóng là $6 2 0 ~ \mathrm { { n m } }$ . Vân sáng đầu tiên (tính từ vân sáng trung tâm) được quan sát tại một góc $1 5 ^ { 0 }$ so với phương ngang. Xác định khoảng cách d giữa hai khe.





ĐS: $2 4 0 \mu \mathrm { m }$

37.7. Thực hiện thí nghiệm Young về giao thoa ánh sáng với các thông số sau: khoảng cách giữa hai khe $0 , 1 \mathrm { m m }$ , ánh sáng được chiếu có bước sóng $5 8 9 \mathrm { n m }$ , khoảng cách từ hai khe đến màn quan sát $4 \mathrm { m }$ .

(a) Xác định hiệu quang lộ của hai sóng tới từ mỗi khe tại vị trí vân sáng bậc ba.

(b) Xác định hiệu quang lộ của hai sóng tới từ mỗi khe tại vị trí vân tối thứ ba.

ĐS: (a) $2 4 0 \mu \mathrm { m }$ , (b) $1 { , } 4 7 \mu \mathrm { m }$

37.8. Một khe sáng đơn sắc S phát ra ánh sáng có bước sóng 442 nm chiếu vào hai khe S1 và $\mathrm { \bf S } _ { 2 }$ cách nhau $0 { , } 4 \mathrm { m m }$ . Xác định khoảng cách xa nhất đặt màn quan sát, sao cho vị trí của hai vân tối đối diện với hai khe và chỉ có một vân sáng ở giữa chúng.

ĐS: 36,2 cm

37.9. Hai loa của một thùng nổ cách nhau $3 5 \ \mathrm { c m }$ . Một bộ dao động điện từ tạo ra dao động cho hai loa với cùng tần số là $2 \mathrm { k H z }$ . Xác định góc được tạo bởi đường thẳng vuông góc tại trung điểm của đường nối hai loa để người quan sát nghe được âm có cường độ lớn nhất, nhỏ nhất? Biết tốc độ truyền âm là $3 4 0 \mathrm { m / s }$ .

ĐS: âm có cường độ lớn nhất: $0 ^ { 0 }$ ; 29,10; $^ { 7 6 , 3 ^ { 0 } }$ âm có cường độ nhỏ nhất: 14,10, 46,80

37.10. Một nhà kho ven sông có một số cánh cửa nhỏ hướng ra bờ sông. Hai trong số các của này được mở (hình 37.17). Các bức tường của nhà kho được lót bằng vật liệu hấp thụ âm. Hai người đứng cách hai cánh cửa tại khoảng cách $\mathrm { L } = 1 5 0 \mathrm { m }$ . Người A đứng dọc theo một đường thẳng đi qua điểm giữa hai cánh cửa, người B đứng cách người A một khoảng $\mathrm { y } = 2 0 \mathrm { m }$ . Một chiếc tàu ven sông phát ra tiếng còi. Để người A nghe được âm thanh to và rõ, còn người B thì không nghe được âm thì khoảng cách giữa hai cánh cửa mở phải bằng bao nhiêu? Biết bước sóng của nguồn âm là $3 \mathrm { m }$ và giả sử người B đang đứng ở vị trí cực tiểu đầu tiên.

![](images/image16.jpg)



ĐS: 11,3 m



37.11. Thực hiện thí nghiệm giao thoa qua hai khe (hình 37.18) với: $\mathrm { d } = 0 , 1 5 \mathrm { m m }$ , $\mathrm { L } = 1 4 0$ cm, $\lambda = 6 4 3 ~ \mathrm { n m }$ , $_ \mathrm { y } = 1 \mathrm { , } 8$ cm. Hãy xác định:

(a) Hiệu quang lộ  của sóng từ hai khe tại điểm P.

(b) Mối quan hệ giữa hiệu quang lộ và bước sóng .

(c) Tại điểm P là điểm cực đại, cực tiểu hay trạng thái trung gian? Giải thích?

ĐS: (a) $1 { , } 9 3 \ \mu \mathrm { m }$ , (b) $\delta = 3 \lambda$ , (c) cực đại

![](images/image17.jpg)  
Hình 37.18

37.12. Thực hiện giao thoa ánh sáng như hình 37.19 (hình vẽ không theo tỷ lệ): ${ \mathrm { L } } = 1 , 2 { \mathrm { m } }$ , $\mathbf { d } = 0 , 1 2 \mathrm { ~ m m }$ , $\lambda = 5 0 0 \mathrm { n m }$ . Hãy xác định độ lệch pha giữa hai sóng tới P khi:

(a) $\theta = 0 { , } 5 ^ { 0 }$ (b) $\mathrm { y } = 5 \mathrm { m m }$

(c) Giá trị của θ là bao nhiêu khi độ lệch pha là 0,333 rad ?

(d) Giá trị của θ là bao nhiêu khi hiệu quang $1 \hat { \varrho } \ \delta = \lambda / 4$

![](images/image18.jpg)  
Hình 37.19

ĐS: (a) 13,2 rad, (b) 6,28 rad, (c) $1 { , } 2 7 { . } 1 0 ^ { - 2 }$ , (d) $5 , 9 7 . 1 0 ^ { - 2 }$



37.13. Các tia sáng $\mathrm { k } \acute { \mathrm { e } } \mathrm { t }$ hợp có bước sóng $\lambda$ chiếu vào hai khe hẹp cách nhau một khoảng d, với góc tới $\theta _ { 1 }$ theo phương ngang (hình 37.20). Các tia ló ra khỏi hai khe $\mathrm { m } \hat { \mathrm { 0 t } }$ góc $\theta _ { 2 }$ tương ứng.

![](images/image19.jpg)  
Hình 37.20

Hình ảnh giao thoa cực đại tạo thành bởi các tia sáng được hứng trên màn quan sát đặt cách hai khe khá xa. Hãy chứng minh rằng góc $\theta _ { 2 }$ được xác định như sau:

$$
\begin{array} { r } { \Theta _ { _ 2 } = \sin ^ { - 1 } \left( \sin \Theta _ { _ 2 } - \displaystyle \frac { \operatorname* { m a x } } { \operatorname* { d } } \right) } \\ { \qquad \quad \Big ( \qquad \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } \mathrm { ~ } } \mathrm { ~ }  \end{array}
$$

37.14. Hai khe hẹp đặt cách nhau $0 , 1 8 \mathrm { m m }$ . Hình ảnh giao thoa được hứng trên màn chắn cách hai khe một khoảng $8 0 ~ \mathrm { c m }$ bằng ánh sáng có bước sóng $6 5 6 { , } 3 \ \mathrm { n m }$ . Hãy xác định phần trăm cường độ cực đại tại khoảng cách $_ { \mathrm { y } } = 0 \mathrm { , 6 }$ cm so với cường độ cực đại tại vân sáng trung tâm.

ĐS: $9 6 { , } 8 \%$

37.15. Cường độ ánh sáng tại một điểm giao thoa hai khe trên màn là $6 4 { , } 0 \%$ giá trị cực đại.

(a) Xác định độ lệch pha nhỏ nhất (tính bằng rad) giữa hai nguồn.

(b) Biểu diễn độ lệch pha dưới dạng hiệu quang lộ đối với ánh sáng có bước sóng 486,1 nm.

ĐS: (a) 1,29 rad, (b)  = r − r = dsin  = $\displaystyle { \delta = { \bf r - r _ { \omega } } = \mathrm { d s i n } \theta = \frac { \phi \lambda } { 2 \pi } }$

37.16. Một màng bong bóng xà phòng (chiết suất $\mathbf { n } = 1 , 3 3 ,$ ) bay trong không khí, lớp bong bóng dạng hình cầu, bề dày 120 nm.

(a) Bước sóng của ánh sáng nhìn thấy được phản xạ mạnh nhất là?

(b) Xác định độ dày nhỏ nhất của màng xà phòng (lớn hơn 120 nm) để ánh sáng phản xạ là lớn nhất với cùng giá trị bước sóng.

ĐS: (a) 638 nm, (b) 360 nm

37.17. Cho một màng mỏng có chiết suất là 1,5. Chiếu một ánh sáng có bước sóng trong khoảng $0 , 4 \mu \mathrm { m } \leq \lambda \leq 0 , 7 5 \mu \mathrm { m }$ , góc chiếu tới là $0 ^ { 0 }$ . (a) Tìm độ dày t nhỏ nhất sao cho để ngoài ánh sáng màu vàng $( \lambda = 0 , 5 8 \mu \mathrm { m } )$ ) cho cực đại giao thoa còn có giao thoa của một ánh sáng $\lambda$



khác. (b) Xác định giá trị $\lambda$ ở câu (a).



ĐS: (a) $0 { , } 4 8 3 ~ \mu \mathrm { m }$ , (b) $0 { , } 4 1 4 \mu \mathrm { m }$

37.18. Một màng dầu mỏng $_ \mathrm { n } = 1 , 2 5 ,$ ) nằm trên mặt ván trơn và ẩm ướt. Ánh sáng đỏ có bước sóng $6 4 0 ~ \mathrm { n m }$ và ánh sáng xanh có bước sóng $5 1 2 \mathrm { n m }$ bị phản xạ mạnh nhất. Coi các tia sáng được chiếu vuông góc đến màng mỏng. Xác định bề dày của lớn màng dầu?

ĐS: 512 nm

37.19. Một vật liệu có chiết suất 1,3 được sử dụng để làm lớp phủ chống sự phản xạ trên bề mặt thủy tinh $( \mathtt { n } = 1 , 5 )$ ). Tính độ dày tối thiểu của lớp vật liệu này để sự phản xạ từ ánh sáng có bước sóng $5 0 0 \mathrm { n m }$ là nhỏ nhất.

ĐS: 96,2 nm

37.20. Một lớp màng mỏng $\mathrm { M g F } _ { 2 }$ có chiết suất 1,38 được sử dụng để phủ trên ống kính của máy ảnh.

(a) Xác định ba bước sóng dài nhất được tăng cường.

(b) Có bất kỳ bước sóng ánh sáng nào trong quang phổ có thể nhìn thấy được không?

ĐS: (a) $2 7 6 \mathrm { n m }$ , $1 3 8 \mathrm { n m }$ , ${ 9 2 , 0 \mathrm { n m } }$ , (b) không (thuộc vùng tử ngoại)

37.21. Hình 37.21 cho thấy mặt thấu kính có bán kính cong R, đặt trên một bản thủy tinh phẳng và được dọi từ trên bằng ánh sáng có bước sóng . Hình cho thấy các vân giao thoa tròn (gọi là vân tròn Newton) xuất hiện, tương ứng với độ dày thay đổi $\mathrm { { e _ { k } } }$ của lớp không khí giữa thấu kính và bản thủy tinh.

(a) Tìm bán kính r của các vân sáng, thừa nhận $\frac { \mathrm { r } } { \mathrm { R } } { \ll } 1$ (b) Chứng minh rằng hiệu bán kính các vân sáng liên tiếp cho bởi biểu thức:

![](images/image20.jpg)  
Hình 37.21

$$
\Delta \mathbf { r } = \mathbf { r } _ { \mathbf { k } + 1 } - \mathbf { r _ { \mathbf { \lambda } \mathbf { k } } } \approx \frac { 1 } { 2 } \sqrt { \frac { \lambda \mathbf { R } } { \mathbf { k } } }
$$

(c) Chứng minh rằng diện tích giữa các vân sáng liên tiếp cho bởi biểu thức:

$$
\mathbf { A } = \pi \lambda \mathbf { R } , \mathbf { v } \acute { \mathbf { o } } \mathbf { i } \mathbf { k } \gg 1
$$

(chú ý rằng diện tích này không phụ thuộc vào k)

# Public_149 

Sóng cơ (mechanical waves) đòi hỏi sự hiện diện của một môi trường trong khi đó sóng điện từ (electromagnetic waves) có thể truyền qua chân không. Các phương trình của Maxwell dựa vào lý thuyết sóng điện từ truyền trong không gian với vận tốc của ánh sáng. Herzt xác nhận những tiên đoán của Maxwell là đúng khi ông đã tạo ra và phát hiện ra sóng điện từ vào năm 1887. Sóng điện từ được tạo ra bằng cách dao động điện tích. Sóng phát ra từ những điện tích có thể dò được tại những nơi rất xa. Sóng điện từ vừa mang năng lượng, vừa mang động lượng.

## Dòng điện dịch và dạng tổng quát của định luật Ampere

### Sơ lược lịch sử

Nhà vật lý lý thuyết Scottish (1831−1879) đã phát triển lý thuyết sóng điện từ của ánh sáng, lý thuyết về động lực của khí và giải thích bản chất màu sắc tự nhiên và chu kỳ của sao Thổ.

Ông đã xây dựng thành công hệ phương trình về trường điện từ và được biết đến với tên gọi hệ phương trình Maxwell. Maxwell là người đã làm được một việc rất quan trọng là khái quát hóa định luật Ampere, đây là một đóng góp rất quan trọng.

Khả năng toán học đáng gờm kết hợp với cái nhìn sâu sắc tuyệt vời cho phép Maxwell dẫn đầu trong nghiên cứu về điện từ và lý thuyết động học. Ông chết vì ung thư trước khi ông 50 tuổi.

![](images/image1.jpg)  
James Clerk Maxwell (1831–1879)

### Sự mở rộng định luật Ampere do Maxwell thực hiện

Trong chương 30, chúng ta đã sử dụng định luật Ampere để phân tích từ trường tạo bởi dòng điện:

$$
\oint \overrightarrow { \mathbf { B } } \cdot \mathrm { d } \overrightarrow { \mathbf { S } } = \mu _ { 0 } \mathbf { I }
$$

Trong phương trình này, tích phân đường qua bất kỳ đường cong khép kín có dòng điện chạy qua, dòng điện dẫn chạy qua vòng ampere được xác định: $\boldsymbol { \mathrm { I } } = \mathrm { d } \boldsymbol { \mathrm { q } }$ dt (Trong phần này, chúng ta sử dụng thuật ngữ “dòng điện dẫn” để chỉ dòng điện được mang bởi các hạt mang điện trong dây dẫn để phân biệt nó với một loại dòng điện khác sẽ được giới thiệu sau). Biểu thức trên chỉ đúng nếu điện trường là tĩnh, tức không phụ thuộc vào thời gian. Maxwell đã ghi nhận giới hạn của định luật Ampere và thay đổi biểu thức này trong trường hợp điện



trường thay đổi theo thời gian.



Xét một tụ điện được tích điện như hình 34.1. Khi xuất hiện dòng điện dẫn thì điện tích trên bản dương của tụ thay đổi nhưng không có dòng điện nào tồn tại trong khe hỡ giữa hai bản tụ vì không xuất hiện các hạt mang điện. Bây giờ hãy xét hai mặt $\mathrm { S } _ { 1 }$ và $\mathbf { S } _ { 2 }$ được giới hạn bởi cùng một đường P, định luật Ampere nói rằng xung quanh đường dẫn P này phải bằng $\mu { _ 0 } \mathrm { I } _ { ; }$ , trong đó I là cường độ dòng điện tổng cộng qua bất kỳ bề mặt nào được bao bọc bởi đường P.

Khi đường dẫn P được coi là ranh giới của $\mathrm { S } _ { 1 }$ thì $\oint \overrightarrow { \mathbf { B } } \cdot \mathbf { d } \overrightarrow { \mathbf { s } } = \mu _ { 0 } \mathbf { I } ,$ trong đó I là dòng điện dẫn qua mặt S1. Khi đường dẫn P được coi là ranh giới của $\mathbf { S } _ { 2 }$ thì $\mathrm { \oint \vec { B } \cdot d s ^ { \prime } } = 0$ , bởi vì không có dòng điện dẫn qua mặt $\mathbf { S } _ { 2 }$ . Do đó, một trường hợp mâu thuẩn có thể xảy ra từ sự gián đoạn của dòng điện. Maxwell đã giải quyết vấn đề này bằng cách đưa ra một số hạn bổ sung $\dot { \mathbf { O } }$ phía bên phải của định luật Ampere. Số hạn cộng thêm được gọi là dòng điện dịch (displacement current, Id).

![](images/image2.jpg)

Dòng dièn dān chi di qua $\mathrm { S } _ { 1 } .$ dièu này trái nguoc vói dinh luàt Ampere khi mò phóng $\mathrm { m } { \hat { \mathrm { ~ } } } ^ { \dagger }$ dòng dién dàn qua $\mathrm { S } _ { 2 }$

Hình 34.1: Hai mặt phẳng $\mathrm { S } _ { 1 }$ và $\mathrm { S } _ { 2 }$ gần một bản của tụ điện được giới hạn bởi đường P.

$$
\begin{array} { c } { \displaystyle { \mathrm {  ~ I ~ } \equiv \varepsilon ^ { \mathrm {  ~ \ d ~ } } } } \\ { \displaystyle { \mathrm {  ~ d ~ } \mathrm {  ~ \Omega ~ } _ { 0 } \frac { \partial \mathrm {  ~ \Omega ~ } } { \partial \mathrm {  ~ \Gamma ~ } } } } \end{array}
$$

trong đó, $\varepsilon _ { \scriptscriptstyle 0 }$ là hằng số điện môi và $\Phi _ { \mathrm { E } } \equiv _ { . }$ E dA là thông lượng electron xuyên qua bề mặt được giới hạn bởi đường tích phân.

Khi tụ điện đang được tích điện (hoặc phóng điện), sự thay đổi điện trường giữa hai bản cực của tụ được coi là tương đương với dòng điện dẫn trong dây. Do đó, biểu thức dòng điện dịch (34.1) được thêm vào dòng điện dẫn trong định luật Ampere, để đi tới một định luật dạng hoàn thiện hơn mà $\dot { \mathbf { O } }$ đó từ trường được tạo bởi dòng điện dẫn và điện trường thay đổi theo thời gian (time-varying electric field). Biểu thức tổng quát của định luật Ampere (nhiều người gọi là định luật Ampere−Maxwell.

$$
\oint \overrightarrow { \mathbf { B } } \cdot \mathbf { d } \overrightarrow { \mathbf { s } } = \mu _ { 0 } \left( \mathrm { I } + \mathrm { I } _ { \mathrm { d } } \right) = \mu _ { 0 } \mathrm { I } + \mu _ { 0 } \varepsilon _ { 0 } \frac { \mathrm { d } \Phi _ { \mathrm { E } } } { \mathrm { d t } }
$$



Hình $3 4 . 2 \mathrm { m } \hat { \mathrm { 0 } }$ tả sự thay đổi điện trường E tồn tại giữa các bản của tụ điện tạo ra một thông lượng electron. Thông lượng electron qua bề mặt S được xác định: $\Phi _ { \mathrm { { E } } } \equiv \int \overrightarrow { \mathrm { E } } \cdot \mathrm { d } \overrightarrow { \mathrm { A } } = \mathrm { E } \mathbf { A }$ , trong đó A là diện tích của các bản của tụ điện và E là độ lớn của điện trường đều giữa hai



bản tụ: $\mathrm { E = q / { \bigl ( } \varepsilon _ { 0 } A { \bigr ) } }$ , trong đó q là điện tích trên bản cực dương của tụ điện, A là diện tích bản cực. Khi đó, thông lượng electron:

Dien trròng giüa các ban tao ra mot thong lrong electron qua bè mǎt S.

$$
\Phi _ { \mathrm { { E } } } = \mathrm { E A } = { \frac { \mathrm { { q } } } { \varepsilon _ { \mathrm { { 0 } } } } }
$$

Do đó, dòng điện dịch qua mặt S là:

$$
\begin{array} { r } { \mathrm { ~ I ~ } = \varepsilon \ \mathrm { d } \Phi _ { \mathrm { E } } \ = \frac { \mathrm { d } \mathbf { q } } { \mathrm { d } \varepsilon } } \end{array}
$$

Phương trình (34.3) cho thấy dòng điện dịch trong khe giữa các bản của tụ có cùng một giá trị. Bằng cách xét bề mặt S, chúng ta có thể xác định dòng điện dịch khi nguồn của từ trường trên bề mặt giới hạn. Dòng điện dịch có nguồn gốc vật lý từ điện trường thay đổi theo thời gian. Điểm chính của phần này là từ trường được tạo ra bởi dòng điện dẫn và điện trường thay đổi theo thời gian.

![](images/image3.jpg)  
Hình 34.2: Khi dòng điện dẫn tồn tại trong các dây dẫn, sự thay đổi điện trường tồn tại giữa các bản của tụ điện.

Câu hỏi 34.1: Trong một mạch RC, tụ điện bắt đầu phóng điện.

(i) Trong quá trình phóng điện, khoảng không gian giữa hai bản của tụ điện. Xuất hiện:

(a) Dòng điện dẫn nhưng không có dòng điện dịch (b) Dòng điện dịch nhưng không có dòng điện dẫn (c) Cả hai dòng điện dẫn và dòng điện dịch (d) Không xuất hiện dòng điện

(ii) Trong cùng một vùng không gian, xuất hiện:

(a) Điện trường nhưng không có từ trường (b) Từ trường nhưng không có điện trường (c) Cả hai điện và từ trường (d) Không xuất hiện điện trường hay từ trường

# Bài tập mẫu 34.1: Dòng điện dịch trong tụ điện

Một điện áp thay đổi hình sin được áp vào hai đầu một tụ điện như trong hình 34.3.



Điện dung của tụ điện là $\mathrm { C } = 8 { , } 0 0 \mu \mathrm { F }$ , tần số của điện áp là $\mathrm { f } = 3 , 0 0 \mathrm { k H z }$ , biên $\mathtt { d } \hat { \mathbf { \rho } }$ điện áp là $\Delta \mathrm { V } _ { \mathrm { m a x } } = 3 0 { , } 0 \mathrm { V } .$ . Hãy xác định dòng điện dịch giữa hai bản của tụ điện.



# Giải:

Khái niệm: Hình 34.3 biểu diễn sơ đồ mạch điện trong trường hợp này. Hình 343 cho thấy chi tiết của tụ điện và điện trường giữa hai bản tụ.

Phân loại: Chúng ta xác đinh kết quả bằng cách sử dụng các phương trình được đưa ra trong phần này, vì vậy ví dụ này được xem như điển hình.

Tần số góc của nguồn:

![](images/image4.jpg)  
Hình 34.3 (bài tập 34.1)

$$
\mathfrak { o } = 2 \pi \mathrm { f } = 2 \pi . \left( 3 , 0 0 . 1 0 ^ { 3 } \right) = 1 , 8 8 . 1 0 ^ { 4 } \mathrm { s } ^ { - 1 }
$$

Sự khác biệt về điện áp qua tụ điện như một hàm theo thời gian:

$$
\Delta \mathbf { v _ { c } } = \Delta \mathbf { V _ { m a x } } \ \mathrm { s i n o t } \ = 3 0 , 0 \mathrm { s i n } \Big ( 1 , 8 8 . 1 0 ^ { 4 } \ \mathrm { t } \Big )
$$

Điện tích của tụ điện: $\mathsf { q } = \mathbf { C } \Delta \mathbf { v } _ { \mathrm { c } }$

Từ phương trình (34.3) về định nghĩa dòng điện dịch:

$$
\mathrm { \Pi _ { \overset { . } { d } } } = \mathrm { \frac { d q } { d t } } = \mathrm { \frac { d } { d t } } \left( \mathrm { C \Delta { v } _ { \overset { . } { c } } } \right) = \mathrm { C } \mathrm { \frac { d } { d t } } \left( \Delta \mathrm { V _ { \overset { . } { m a x } } } \mathrm { s i n } \mathrm { \omega _ { \overset { . } { m } } } \right) = { \omega } \mathrm { C } \Delta \mathrm { V } \mathrm { c o s o t }
$$

Thay số:

$$
\begin{array} { r l } { \dot { \mathrm { \vert \Phi _ { d } ~ } } } & { { } = \left( 1 , 8 8 . 1 0 ^ { 4 } \mathrm { s ^ { - 1 } } \right) \left( 8 , 0 0 . 1 0 ^ { - 6 } \mathrm { C } \right) \left( 3 0 , 0 \mathrm { V } \right) \mathrm { c o s } \left( 1 , 8 8 . 1 0 ^ { 4 } \mathrm { t } \right) \ = \ 4 , 5 1 \mathrm { c o s } \left( 1 , 8 8 . 1 0 ^ { 4 } \mathrm { t } \right) \ \mathrm { s ^ { - 1 } } } \end{array}
$$

## Phương trình Maxwell và phát minh của Hertz

Trong lý thuyết thống nhất của Maxwell về điện từ cho rằng, sóng điện từ là một hệ quả tự nhiên của những định luật cơ bản của điện từ học giống như các định luật Newton về chuyển động đối với cơ học. Tuy nhiên cũng có một sự khác nhau rất quan trọng. Einstein đưa ra thuyết tương đối hẹp vào năm 1905, khoảng 200 năm sau thì xuất hiện các định luật Newton và 40 năm sau thì xuất hiện các phương trình Maxwell. Sau khi có lý thuyết tương đối, các định luật Newton phải thay đổi rất nhiều khi tốc độ tương đối đạt đến giá trị xấp xỉ vận tốc ánh sáng. Tuy nhiên, đối với phương trình Maxwell thì không cần thay đổi gì, chúng hoàn toàn phù hợp với thuyết tương đối hẹp.

Các phương trình Maxwell đại diện cho các định luật về điện và từ tính mà chúng ta đã bàn luận, nhưng chúng có hệ quả rất quan trọng. Để đơn giản, các phương trình Maxwell áp dụng cho không gian trống, tức là không có bất cứ vật liệu điện môi hoặc từ tính nào sẽ



được trình bày.



### Phương trình Maxwell 1 − Định luật Gauss

Tổng thông lượng điện (electric flux) qua bề mặt kín bất kỳ bằng tổng điện tích bên trong bề mặt kín chia cho 0. Định luật này liên quan đến sự phân bố điện tích để tạo ra điện trường.

$$
\oint \overrightarrow { \mathrm { E } } \cdot \mathrm { d } \overrightarrow { \mathrm { A } } = \frac { { \mathfrak { q } } } { \mathfrak { E } _ { 0 } }
$$

### Phương trình Maxwell 2 − Định luật Gauss trong từ trường

Từ thông (magnetic flux) toàn phần qua một mặt kín bằng không, có nghĩa là số đường sức từ đi vào phải bằng số đường sức từ đi ra khỏi một mặt kín. Điều này có nghĩa là các đường sức từ không thể bắt đầu hoặc kết thúc tại bất kỳ điểm nào. Nếu điều này đúng thì những đơn cực từ (isolated magnetic monopoles) sẽ được tìm thấy trong tự nhiên. Tuy nhiên, cho đến nay vẫn chưa tìm thấy được.

$$
\oint \overrightarrow { \mathbf { B } } \cdot \mathbf { d } \overrightarrow { \mathbf { A } } = 0
$$

### Phương trình Maxwell 3 − Định luật Faraday về cảm ứng

Phương trình này dùng để mô tả việc tạo ra điện trường bằng cách làm cho từ trường biến thiên theo thời gian. Theo điện động lực học, tích phân đường của điện trường dọc theo một đường cong khép kín bằng tốc độ biến thiên của từ thông gửi qua diện tích bề mặt được giới hạn bởi đường cong đó. Một hệ quả của định luật Faraday là tồn tại dòng điện dẫn trong vòng dây dẫn đặt trong một từ trường biến thiên theo thời gian.

$$
\oint \vec { \mathrm { E } } \cdot \mathrm { d } \vec { \mathrm { s } } = - \frac { \mathrm { d } \Phi _ { \mathrm { B } } } { \mathrm { d t } }
$$

### Phương trình Maxwell 4 − Định luật Ampere-Maxwell

Định luật Ampere-Maxwell dùng để mô tả việc tạo ra từ trường bằng điện trường biến thiên và dòng điện. Tích phân đường của từ trường dọc theo một đường cong khép kín bằng tổng của 0 nhân với dòng điện và 00 nhân với tốc độ biến thiên từ thông gửi qua diện tích bề mặt được giới hạn bởi đường cong đó:

### Lực Lorentz

Tại một điểm trong không gian tồn tại điện trường và từ trường, lực tác dụng lên một



hạt mang điện tích q có thể được tính toán từ điện và từ trường của hạt như sau:

$$
\vec { \mathrm { F } } = \mathbf { q } \overrightarrow { \mathrm { E } } + \mathbf { q } \overrightarrow { \mathrm { v } } \times \overrightarrow { \mathrm { B } }
$$



Những phương trình của Maxwell và lực Lorentz mô tả đầy đủ về tương tác điện từ trước đó. Cần chú ý tính đối xứng của hệ bốn phương trình Maxwell. Các phương trình (34.4) và (34.5) lần lượt là các tích phân mặt của E và B lấy trên một mặt kín. Phương trình (34.6) và (34.7) lần lượt là các tích phân đường của E và B lấy dọc theo một chu vi kín. Phương trình của Maxwell có tầm quan trọng cơ bản không chỉ đối với điện từ học nói riêng và ngành khoa học nói chung.

### Thí nghiệm của Hertz

Heinrich Rudolf Hertz (1857−1894) là nhà Vật lý người Đức. Ông là người đầu tiên tạo ra sóng điện từ và phát hiện ra sóng điện từ tại phòng thí nghiệm vào năm 1887. Ông cũng chỉ ra một khía cạnh sóng khác của ánh sáng. Những tia lửa điện được cảm ứng qua khoảng trống của hai điện cực của mạch thu, khi hiệu chỉnh tần số của mạch thu trùng với mạch phát. Trong một loạt các thí nghiệm khác, Herzt cũng chỉ ra bức xạ được tạo ra bởi những thiết bị này có thể thể hiện bản chất sóng. Giao thoa, nhiễu xạ, phản xạ, khúc xạ và phân cực. Ông cũng đo được vận tốc bức xạ gần đúng bằng vận tốc của ánh sáng.

![](images/image5.jpg)  
Heinrich Rudolf Hertz (1857–1894)

Mô tả thí nghiệm: Một cuộn dây cảm ứng được nối với mạch phát. Mạch phát $\mathrm { g } \dot { \mathsf { o } } \mathsf { m } 2$ cực dạng hình cầu đặt cách nhau một khoảng rất nhỏ. Cuộn dây cung cấp một điện áp tăng vọt trong một khoảng thời gian ngắn đến các điện cực. Khi đó, không khí ở khoảng giữa 2 điện cực bị oxy hóa và trở thành một dây dẫn tốt hơn. Việc xả điện giữa các điện cực tạo thành một dao động có tần số rất cao, điều này tương đương mạch LC.

Vận tốc của bức xạ điện từ trong chân không là rất quan trọng không những đối với lý thuyết điện từ của Maxwell mà còn đối với cả lý thuyết của Einstein. Trong một không gian trống rỗng ( $\mathsf { q } = 0$ và $\mathrm { { I } } = 0$ ), hai phương trình (34.6) và (34.7), Maxwell đã tiên đoán rằng ánh sáng là một dạng bức xạ điện từ (electromagnetic radiation). Thí nghiệm của Hertz cho ta một ví dụ về sự phát sóng điện từ (hình 34.4). Lõi của cuộn dây cung cấp một điện thế cho các điện cực electron, một điện cực dương và một điện cực âm. Trong thí nghiệm đó rõ ràng rằng là điện tích trên hai quả cầu biến thiên một cách tuần hoàn theo thời gian. Một tia lửa điện được tạo ra giữa hai quả cầu khi điện trường của các điện cực lớn hơn cường độ điện trường giữa hai quả cầu trong không khí $( 3 . 1 0 ^ { 6 } \ \mathrm { V / m } )$ . Các electron tự do trong điện trường mạnh được gia tốc và tích đủ năng lượng $\mathrm { d } \acute { \mathrm { e } }$ ion hóa các phân tử mà chúng va chạm. Sự ion hóa này tạo ra nhiều electron để gia tốc và gây ra các quá trình ion hóa khác. Khi không khí trong khe bị ion hóa trở thành một chất dẫn điện tốt và sự phóng điện giữa các điện cực làm xuất hiện trạng thái dao động ở tần số rất cao. Theo quan điểm mạch điện, $\mathrm { m } \hat { \mathrm { o } }$ hình thí nghiệm của Hertz tương đương với mạch LC, trong đó độ tự cảm của cuộn dây và điện dung của tụ điện được tạo ra từ các điện cực hình cầu.





Bởi vì giá trị của L và C trong thí nghiệm của Hertz là nhỏ và tần số dao động rất lớn, khoảng $1 0 0 \mathrm { M H z }$ (với $\mathrm { c o } { = } 1 / \sqrt { \mathrm { L C } }$ cho mạch dao động LC). Sóng điện từ phát ra tại giá trị tần số này là kết quả của các electron tự do di chuyển trong mạch điện. Hertz đã ghi nhận các sóng này bằng cách sử dụng một vòng dây đơn với khoảng cách giữa các tia lửa điện (máy thu). Mạch nhận sóng, có độ tự cảm L, điện dung C và tần số dao động f, được đặt cách một vài mét từ máy phát. Trong thí nghiệm của Hertz, các tia lửa điện được tạo ra giữa khoảng không gian giữa hai điện cực của máy thu khi tần số của máy thu được điều chỉnh sao cho trùng với tần số của máy phát. Từ thí nghiệm này, Hertz đã chứng minh được rằng dòng điện trong máy thu được tạo ra bởi sóng điện từ được phát ra từ máy phát.

Ngoài ra, Hertz đã thực hiện một loạt các thí nghiệm liên quan đến bức xạ được tạo ra bởi thiết bị tia lửa của mình nhằm thể hiện các tính chất sóng của hiện tượng giao thoa, nhiễu xạ, phản xạ, khúc xạ và phân cực. Đó là tất cả các tính chất của ánh sáng như chúng ta đã được biết. Sóng vô tuyến mà Hertz đã tạo ra có các tính chất tương tự như sóng ánh sáng, tuy nhiên chúng khác nhau về tần số và bước sóng. Thí nghiệm thuyết phục nhất của ông là đo tốc độ của bức xạ này. Sóng có

Máy phát bao gòm hai dièn cue hinh càu nói vói mòt cuòn càm. Cuòn cám có tác dung cung cáp dièn áp ngán dǎn dén các dièn cuc và hinh thành su dao dòng trong quá trinh phóng dièn giüa các dièn curc.

![](images/image6.jpg)  
Hình 34.4: Sơ đồ thí nghiệm của Hertz để tạo ra và ghi nhận sóng điện từ.

tần số đã biết được phản xạ từ một tấm kim loại và tạo ra mô hình giao thoa sóng. Bằng cách đo khoảng cách giữa hai điểm nút cho phép xác định được giá trị bước sóng . Sử dụng mối quan hệ ${ \bf v } = \lambda { \bf f }$ trong quá trình lan truyền sóng, Hertz đã tính được vận tốc của sóng điện từ là $\mathrm { v } = 3 . 1 0 _ { \mathrm { c } } ^ { 8 } \mathrm { m } / \mathrm { s }$ , giá trị này được biết đến như vận tốc của ánh sáng khả kiến.

## Sóng điện từ phẳng

Giả sử rằng vector điện trường và từ trường của một sóng điện từ có quan hệ không − thời gian đặc biệt, phù hợp với các phương trình của Maxwell. Giả sử một sóng điện từ truyền theo phương x với $\overrightarrow { \mathrm { E } }$ và $\mathbf { B }$ như được minh họa trong hình 34.5. Vector điện trường E hướng theo phương y và từ trường $\overrightarrow { \mathrm { B } }$ Ehướng theo phương z. Sóng mà trong đó điện trường và từ trường $\overrightarrow { \mathrm { B } }$ bị hạn chế là song song với một cặp trục vuông góc được gọi là sóng phân cực tuyến tính (linearly polarized waves). Giả sử rằng tại bất kỳ mọi điểm trong không gian thì độ lớn của E và $\overrightarrow { \mathrm { B } }$ chỉ phụ thuộc vào tọa độ x và thời gian t.





Giả sử nguồn phát sóng điện từ tại bất kỳ vị trí nào trong mặt phẳng yz. Nếu chúng ta định nghĩa tia (ray) là một đường thẳng mà sóng truyền đi thì tất cả các tia của sóng phân cực tuyến tính đều song song với nhau. Tập hợp của các sóng này được gọi là sóng phẳng (plane waves). Bề mặt nối những điểm cùng pha của tất cả các sóng phẳng gọi là mặt sóng (wave front) có dạng mặt phẳng. Tuy nhiên, khi một nguồn điểm bức xạ phát sóng theo mọi hướng thì bề mặt nối những điểm cùng pha của những vị trí này có dạng hình cầu, sóng này được gọi là sóng cầu (spherical wave).

![](images/image7.jpg)  
Hình 34.5: Điện trường và từ trường của sóng điện từ truyền với vận tốc dọc theo chiều dương của trục x.

### Điện trường cảm ứng

Bây giờ chúng ta bắt đầu với định luật Faraday từ phương trình (34.6) để chứng minh sự có mặt của sóng điện từ phẳng:

$$
\oint \vec { \mathrm { E } } \cdot \mathrm { d } \vec { \mathrm { s } } = - \frac { \mathrm { d } \Phi _ { \mathrm { B } } } { \mathrm { d t } }
$$

$$
{ \frac { \partial \mathrm { E } } { \partial \mathrm { x } } } = - { \frac { \partial \mathrm { B } } { \partial \mathrm { t } } }
$$

### Từ trường cảm ứng

Một cách tương tự, chúng ta có thể suy ra phương trình thứ hai để chứng minh sự tồn tại của sóng điện từ phẳng bằng cách xuất phát từ phương trình thứ tư của Maxwell (phương trình (34.7)).

$$
\oint \overrightarrow { \mathbf { B } } \cdot \mathrm { d } \overrightarrow { \mathbf { s } } = \mu _ { 0 } \mathrm { I } + \varepsilon _ { 0 } \mu _ { 0 } \ \frac { \mathrm { d } \Phi _ { \mathrm { E } } } { \mathrm { d t } }
$$

tích phân $\oint \overrightarrow { \mathbf { B } } \cdot \mathrm { d } \mathbf { s } ^ { \mathbf { \alpha } }$ lấy ngược chiều kim đồng hồ vòng quanh hình chữ nhật nằm trên mặt phẳng xz, có chiều rộng dx và chiều dài $\ell$ như trên hình 34.7. Chú ý rằng độ lớn của từ trường thay



Chúng ta thấy rằng sự thay đổi của thông lượng $\Phi _ { \mathrm { E } }$ sẽ cảm ứng một từ trường với các vector $\overrightarrow { \mathrm { B } } \big ( \mathrm { x } \big )$ và ${ \vec { \mathrm { B } } } ( \mathbf { x } + \mathbf { d x } )$ có hướng như được vẽ trong hình 34.7. Thông lượng electron xuyên qua hình chữ nhật ấy là $\Phi _ { \mathrm { E } } = \mathrm { E } \mathcal { \ell } \mathrm { d } \mathbf { x }$ , lấy vi phân của thông lượng electron theo thời gian ta có:

$$
\frac { \partial \Phi _ { \mathrm { E } } } { \partial \mathrm { t } } = \ell \mathrm { d } \mathrm { x } \frac { \partial \mathrm { E } } { \partial \mathrm { t } }
$$

Nếu chúng ta thay phương trình (34.12) và (34.13) vào phương trình (34.7), chúng ta tìm được:



### Sự truyền tải năng lượng

Bằng cách lấy đạo hàm phương trình (34.11) theo x sau đó kết hợp với phương trình (34.14) ta có:

Theo phurong trinh (34.11), su thay dòi dièn trròng làm phát sinh tù tròng bién thièn theo thòi gian theo huróng z.

Theo phuong trinh (34.14), sur thay dòi tùr trròng làm phát sinh dièn truòng thay dòi theo thòi gian theo hróng y.

![](images/image8.jpg)  
Hình 34.6: Khi sóng đi qua các hình chữ nhật tại điểm P, sự thay đổi từ thông qua hình chữ nhật trong mặt phẳng xy cảm ứng

![](images/image9.jpg)  
Hình 34.7: Khi sóng đi qua các hình chữ nhật tại điểm P, sự thay đổi điện thông qua hình chữ nhật trong mặt phẳng xz cảm ứng

một điện trường $\vec { \mathrm { E } } \left( \mathbf { x } \right)$ và ${ \vec { \operatorname { E } } } { \bigl ( } \mathbf { x } + \mathbf { d x } { \bigr ) }$ dọc theo các cạnh của hình chữ nhật ấy.

một từ trường $\vec { \bf B } ( { \bf x } )$ và ${ \vec { \mathrm { B } } } { \bigl ( } \mathbf { x } + \mathbf { d x } { \bigr ) }$ dọc theo các cạnh của hình chữ nhật ấy.

Tương tự, lấy đạo hàm phương trình (34.14) theo x sau đó kết hợp với phương trình (34.11) ta có:



Phối hợp phương trình (34.15) và (34.16) ta có kết quả cuối cùng:

$$
\mathsf { c } = \frac { 1 } { \sqrt { \mu _ { 0 } \varepsilon _ { 0 } } }
$$

Thay số vào ta được:

$$
\mathbf { c } = { \frac { 1 } { \sqrt { \mathsf { \mu _ { 0 } } \varepsilon _ { 0 } } } } = { \frac { 1 } { \sqrt { \left( 4 \pi . 1 0 ^ { - 7 } \operatorname { T m } / \mathbf { A } \right) \left( 8 , 8 5 4 . 1 0 ^ { - 1 2 } \mathbf { C } ^ { 2 } / \operatorname { N m } ^ { 2 } \right) } } } = 2 , 9 9 7 . 1 0 ^ { 8 } \mathbf { m } / \mathbf { s }
$$

Chúng ta đã chứng minh rằng phương trình Maxwell (34.6) và (34.7) có nghiệm dạng sóng, với hai thành phần E và B cùng thỏa mãn một phương trình sóng. Sóng điện từ truyền đi với vận tốc bằng vận tốc ánh sáng.

Nghiệm của phương trình (34.15) và (34.16) là sóng dạng hình sin, có độ lớn của vector điện trường và từ trường thay đổi theo x và t theo các biểu thức:

$$
\begin{array} { r } { \mathrm { E } = \mathrm { E } _ { \mathrm { m a x } } \cos ( \mathrm { k x - \omega t } ) } \\ { \mathrm { B } = \mathrm { B } _ { \mathrm { m a x } } \cos ( \mathrm { k x - \omega t } ) } \end{array}
$$

trong đó: $\mathrm { E } _ { \mathrm { m a x } }$ và $\mathrm { B } _ { \mathrm { m a x } }$ là các giá trị cực đại của điện trường và từ trường. Số sóng $k = 2 \pi / \lambda$ , với $\lambda$ là bước sóng. Tần số góc $\omega = 2 \pi \mathrm { f }$ , với f là tần số sóng $\left( \mathrm { H z } \right)$ . Trong quá trình truyền sóng điện từ, tỷ số  k bằng tốc độ của sóng điện từ:

$$
\frac { \omega } { \nu } = \frac { 2 \pi \mathrm { f } } { 2 \pi / \lambda } = \lambda \mathrm { f } = \alpha
$$

Mối quan hệ giữa vận tốc, tần số và bước sóng của một sóng hình sin được xác định theo biểu thức: $\mathbf { v } = \mathbf { c } = \lambda \mathbf { f }$ . Do đó, trong quá trình lan truyền sóng điện từ thì bước sóng và tần số có mối liên hệ với nhau như sau:

![](images/image10.jpg)



$$
\lambda = \sum \limits _ { \overline { { \mathrm { ~ f ~ } } } } ^ { \mathbf { c } } = \underbrace { 1 0 0 . 1 0 ^ { 8 } \mathrm { m / s } } _ { \mathrm { ~ f ~ } }
$$

Hình 34.8 biểu diễn sóng điện từ phân cực tuyến tính hình sin tại một thời điểm di chuyển theo chiều dương của trục x.

Hình 34.8: Sóng điện từ hình sin di chuyển theo chiều dương của trục x với vận tốc c.



Bằng việc lấy đạo hàm phương trình (34.18) theo x và phương trình (34.19) theo t, chúng ta có thể biểu diễn toán học quá trình di chuyển của sóng điện từ như sau:

$$
\begin{array} { r l } & { \frac { \partial \mathrm { E } } { \partial \mathrm { E } } = - \mathrm { k E } \qquad \sin \mathrm { ( k x - \omega ) } } \\ & { \hat { \sigma } \mathrm { x } } \\ & { \frac { \partial \mathrm { B } } { \partial \mathrm { m } } = \mathrm { \omega } \mathrm { B } \qquad \sin \mathrm { ( k x - \omega ) } } \\ & { \hat { \sigma } \mathrm { t } \qquad \operatorname* { m a x } } \end{array}
$$

Thay các kết quả đạo hàm vừa tìm được vào phương trình (34.11) ta được:

$$
\mathbf { k E } _ { \operatorname* { m a x } } = \mathbf { \omega } \mathbf { B } _ { \operatorname* { m a x } }
$$

$$
\frac { \mathrm { E } _ { \mathrm { m a x } } } { \mathrm { B } _ { \mathrm { m a x } } } = \frac { \omega } { \nu } = \alpha
$$

Kết hợp phương trình (34.18) và (34.19):

$$
\frac { \mathrm { E } _ { \mathrm { m a x } } } { \mathrm { B } _ { \mathrm { m a x } } } = \frac { \mathrm { E } } { \mathrm { B } } { = } { \mathrm { c } }
$$

Trong quá trình lan truyền sóng điện từ, tỷ lệ giữa độ lớn cường độ điện trường và cường độ từ trường bằng với tốc độ của ánh sáng. Cuối cùng, cần chú ý rằng sóng điện từ vẫn tuân theo nguyên lý chồng chất như sóng cơ học, bởi vì các phương trình vi phân liên quan đến E và B là các phương trình tuyến tính.

Người ta đã chứng minh được rằng đối với sóng điện từ phẳng đơn sắc:

1. Hai vector E và $\vec { \mathrm B }$ luôn vuông góc với nhau.   
2. Ba vector E ,  và c , theo thứ tự đó, hợp thành một tam diện thuận ba mặt vuôngB góc.

Câu hỏi 34.2: Một sóng điện từ lan truyền theo chiều âm của trục y. Điện trường tại một điểm trong không gian được định hướng theo chiều dương của trục x. Từ trường tại điểm đó hướng theo chiều nào?

(a) chiều âm của trục x (b) chiều dương của trục y (c) chiều dương của trục z (d) chiều âm của trục z



# Bài tập mẫu 34.2: Sóng điện từ

Một sóng điện từ hình sin có tần số $4 0 { , } 0 \mathrm { k H z }$ truyền trong không gian tự do theo trục x như hình 34.9.



(A) Hãy xác định bước sóng và chu kỳ của sóng.

Giải

Khái niệm: Hãy tưởng tượng sóng điện từ trong hình 34.9 truyền theo chiều dương của trục x, với điện trường và từ trường dao động cùng pha.

Phân loại: Chúng ta sử dụng biểu thức toán học của mô hình truyền sóng cho song điện từ.

Phân tích: Sử dụng phương trình (34.20) để tìm độ dài bước sóng:

$$
\lambda = \frac { \mathbf { c } } { \mathbf { \overline { { f } } } } = \frac { 3 , 0 0 . 1 0 ^ { 8 } \mathbf { m / s } } { 4 0 , 0 . 1 0 ^ { 6 } \mathrm { H z } } = 7 , 5 0 \mathbf { \ m }
$$

Chu kỳ của sóng là nghịch đảo của tần số:

$$
\mathrm { T = \frac { 1 } { - } = \frac { 1 } { 4 0 , 0 . 1 0 ^ { 6 } H z } = 2 , 5 0 . 1 0 ^ { - 8 } s }
$$

![](images/image11.jpg)  
Hình 34.9: (bài tập 34.2)

(B) Tại cùng một vị trí và cùng thời gian, điện trường có giá trị cực đại là $7 5 0 \mathrm { N } / \mathrm { C }$ hướng theo chiều dương của trục y. Hãy xác định cường độ và hướng của từ trường tại vị trí này.

# Giải

Sử dụng phương trình (34.21) để xác định độ lớn của từ trường:

$$
\mathbf { B } _ { \mathrm { m a x } } ^ { \mathrm { O } } = { \frac { \mathrm { E } _ { \mathrm { m a x } } } { \mathrm { c } } } = { \frac { 7 5 0 \mathrm { N / C } } { 3 , 0 0 . 1 0 ^ { 8 } \mathrm { m / s } } } = 2 { , } 5 0 . 1 0 ^ { - 6 } \mathrm { T }
$$

Bởi vì E và $\vec { \mathrm B }$ phải vuông góc với nhau và vuông góc với phương truyền sóng như trên hình 34.9 nên từ trường phải hướng theo trục z.

## Năng lượng sóng điện từ



Trong mô hình hệ không đồng nhất về năng lượng, chúng ta đã xác định bức xạ sóng điện từ như là một phương pháp truyền năng lượng qua mặt giới hạn của một hệ. Phần năng lượng sóng điện từ truyền qua được ký hiệu là $\mathrm { T } _ { \mathrm { E R } }$ . Tốc độ truyền năng lượng của sóng điện từ được mô tả bởi vector S, gọi là vector Poynting, được xác định bởi biểu thức:



Độ lớn của vector Poynting cho biết tốc độ truyền năng lượng xuyên qua một đơn vị diện tích vuông góc với phương truyền sóng. Do đó, độ lớn của $\vec { \mathsf { S } }$ đại diện cho năng lượng trên một đơn vị diện tích. Hướng của vector này dọc theo phương truyền sóng (hình 34.10). Đơn vị của vector $\vec { \mathsf { S } }$ trong hệ SI là $\dot { \mathrm { ~ J ~ } } _ { \mathrm { { S } } , \mathrm { { m } } ^ { 2 } } = \mathrm { { W } } \dot { \mathrm { ~ \Omega ~ } } _ { \mathrm { { m } } ^ { 2 } }$ .

Đối với sóng điện từ phẳng: $\left| { \vec { \mathrm { E } } } \times { \vec { \mathrm { B } } } \right| = \mathrm { E B }$ khi đó độ lớn của $\vec { \mathsf { S } }$ được xác định như sau:

![](images/image12.jpg)

Hình 34.10: Vector Poynting của sóng điện từ phẳng dọc theo phương truyền sóng.

$$
\mathrm { S = } \frac { \mathrm { E B } } { \mu _ { \mathrm { 0 } } }
$$

Bởi vì $\mathrm { B } { = } \mathrm { E } / \mathrm { c }$ , khi đó biểu thức (34.23) được viết lại như sau:

Biểu thức độ lớn của S áp dụng tại bất kỳ thời điểm nào và biểu thị cho tốc độ tức thời của năng lượng xuyên qua một đơn vị diện tích ứng với giá trị tức thời của E và B. Đối với sóng điện từ phẳng hình sin thì trung bình theo thời gian S qua một hoặc nhiều chu kỳ được gọi là cường độ sóng I. (Cường độ của sóng âm đã được nhắc đến trong chương 17.) Khi thực hiện tính giá trị trung bình này, chúng ta sẽ thu được một công thức miêu tả giá trị trung bình theo thời gian của $\cos ^ { 2 } \left( \mathrm { k x } - \omega t \right)$ và bằng 1 2. Khi đó, giá trị trung bình của S (hay nói cách khác là cường độ sóng) là:

Cường độ của sóng điện từ tỷ lệ với bình phương biên độ của cường độ điện trường hay cường độ từ trường.

Cần nhắc lại rằng năng lượng trên một đơn vị thể tích gắn liền với điện trường, được gọi là mật độ năng lượng tức thời:

và mật độ năng lượng tức thời gắn liền với từ trường:



$$
\mathbf { u } _ { \mathrm { B } } = { \frac { \mathbf { B } ^ { 2 } } { 2 \mu _ { 0 } } }
$$

Do E và B thay đổi theo thời gian đối với sóng điện từ nên mật độ năng lượng cũng thay đổi theo thời gian. Sử dụng mối liên hệ $\mathrm { B } = \mathrm { E } / \mathrm { c }$ và $\mathsf { c } = 1 \Big / \sqrt { \mu _ { 0 } \varepsilon _ { 0 } }$ , biểu thức của $\mathtt { u _ { B } }$ được viết lại như sau:

$$
\mathbf { \Psi } _ { \mathrm { ~ \tiny ~ B ~ } } = \frac { \left( \mathrm { E / c } \right) ^ { 2 } } { 2 \mu } = \frac { \mu _ { 0 } \varepsilon _ { 0 } } { 2 \mu _ { _ 0 } } \mathrm { E } ^ { 2 } = \frac { 1 } { 2 } \varepsilon _ { _ 0 } \mathrm { E } ^ { 2 }
$$

So sáng kết quả này với biểu thức của $\mathbf { u } _ { \mathrm { E } }$ , ta có:

$$
\mathbf { u } _ { \mathrm { B } } = \mathbf { u } _ { \mathrm { E } } = { \frac { 1 } { 2 } } \varepsilon _ { 0 } \mathrm { E } ^ { 2 } = { \frac { \mathbf { B } ^ { 2 } } { 2 \mu _ { 0 } } }
$$

Cuối cùng, mật độ năng lượng tức thời của sóng điện từ gắn liền với từ trường bằng với mật độ năng lượng tức thời gắn liền với điện trường. Do đó, đối với một thể tích nhất định thì năng lượng của sóng điện từ được chia đều cho hai thành phần điện trường và từ trường.

Tổng mật độ năng lượng tức thời u của sóng điện từ bằng tổng mật độ năng lượng của điện trường và từ trường:

$$
\mathbf { u } = \mathbf { u } _ { \mathrm { B } } + \mathbf { u } _ { \mathrm { E } } = \varepsilon _ { 0 } \mathrm { E } ^ { 2 } = { \frac { \mathbf { B } ^ { 2 } } { \mu } }
$$

Khi giá trị mật độ năng lượng tức thời của sóng điện từ này được tính trung bình trong một hoặc nhiều chu kỳ,

$$
\mathbf { u } _ { \mathrm { a v g } } = \varepsilon _ { 0 } \left( \mathrm { E } ^ { \mathrm { } } \right) _ { \mathrm { a v g } } \mathbf { \Sigma } _ { 2 } ^ { 1 } \mathbf { \Sigma } _ { 2 } ^ { 2 } = \frac { \mathbf { B } ^ { 2 } } { 2 \mu _ { 0 } }
$$

So sáng kết quả này với biểu thức (34.24) ta có:

$$
\mathrm { I } { = } \mathrm { S } _ { \mathrm { a v g } } { = } \mathrm { c u } _ { \mathrm { a v g } }
$$

Nói cách khác, cường độ của sóng điện từ bằng mật độ năng lượng trung bình nhân với vận tốc của ánh sáng.



Mở rộng:

Mặt trời cung cấp khoảng $1 0 ^ { 3 } \mathrm { W } / \mathrm { m } ^ { 2 }$ năng lượng đến bề mặt Trái đất thông qua bức xạ điện từ. Hãy tính toán tổng công suất chiếu lên mái nhà, kích thước mái nhà là $8 , 0 0 \mathrm { m } \times 2 0 , 0 \mathrm { m }$ . Giả sử rằng độ lớn trung bình của vector Poynting đối với bức xạ mặt trời ở bề mặt Trái đất



là $\mathrm { S } _ { \mathrm { a v g } } = 1 0 0 0 \mathrm { W } / \mathrm { m } ^ { 2 }$ . Giá trị trung bình này đại diện cho công suất trên một đơn vị diện tích, còn được gọi là cường độ sáng. Khi đó, bức xạ đến mái nhà có công suất:

$$
\mathbf { P } _ { \mathrm { a v g } } = \mathbf { S } _ { \mathrm { a v g } } \mathbf { A } = \Big ( 1 0 0 0 \mathbf { W } \big / \mathrm { m } ^ { 2 } \Big ) \big ( 8 , 0 0 \mathrm { ~ m } \times 2 0 , 0 \mathrm { ~ m } \big ) = 1 , 6 0 . 1 0 ^ { 5 } \mathbf { W }
$$

Giá trị công suất trên là lớn hơn so với công suất yêu cầu của một ngôi nhà điển hình. Nếu công suất này có thể được hấp thụ và cung cấp cho các thiết bị điện thì nó có thể cung cấp nhiều hơn năng lượng trung bình cho một ngôi nhà. Tuy nhiên, năng lượng mặt trời không dễ dàng khai thác để sản xuất điện và phát triển quy mô lớn như tính toán trong bài toán này. Ví dụ, hiệu suất chuyển đổi của pin quang điện từ năng lượng Mặt trời vào khoảng $12 - 1 8 \%$ nên công suất tiêu thụ giảm đáng $\mathrm { k } \mathring { \mathrm { e } }$ . Mặt khác, phụ thuộc vào vị trí, bức xạ không thể chiếu đến mái nhà cả ngày mà nó chỉ tồn tại trong thời gian nửa ngày. Không có năng lượng cung cấp cho hệ thống vào ban đêm và những ngày nhiều mây, điều này làm giảm đi một phần năng lượng được tích trữ trước đó. Cuối cùng, trong khi năng lượng đến với tốc độ lớn vào giữa ngày thì chúng sẽ được lưu trữ lại để sử dụng dần, cần có pin hoặc các thiết bị lưu trữ khác. Nhìn chung, sự vận hành năng lượng mặt trời trên mái nhà hiện tại không hiệu quả về chi phí cho hầu hết các ngôi nhà.

# Bài tập mẫu 34.3:

Hãy xác định độ lớn cực đại của điện trường và từ trường của ánh sáng khả kiến từ chiếc đèn để bàn chiếu đến một mặt giấy. Coi bóng đèn như một nguồn bức xạ điện từ có hiệu suất phát sáng là $5 \%$ .

# Giải

Khái niệm: Dây tóc bóng đèn phát ra bức xạ điện từ. Ánh sáng càng mạnh thì cường độ của điện trường và từ trường càng lớn.

Phân loại: Coi dây tóc bóng đèn như một nguồn sáng điểm phát ra theo mọi hướng.   
Quá trình lan truyền bức xạ điện từ có thể được mô hình hóa như sóng cầu.

Phân tích: Cường độ sóng tại một điểm cách nguồn một khoảng r được xác định: $\mathrm { I } = \mathrm { P _ { a v g } } \left/ 4 \pi \mathrm { r } ^ { 2 } \right.$ , trong đó Pavg là công suất trung bình của nguồn và 4r2 là diện tích của hình cầu bán kính r từ nguồn. Khi đó, cường độ của sóng điện từ được cho bởi công thức (34.24): 2025-0

$$
\mathrm { I } = \frac { \mathrm { P _ { a v g } } } { 4 \pi \mathrm { r ^ { 2 } } } = \frac { \mathrm { E ^ { 2 } } } { 2 \mu _ { _ { 0 } } \mathrm { c } }
$$

Giải phương trình trên để xác định cường độ điện trường cực đại:



Giả sử công suất bức xạ của bóng đèn là 60 W, với hiệu suất là $5 \%$ là $3 \mathrm { ~ W ~ }$ (phần năng lượng hao phí do dẫn nhiệt và bức xạ không nhìn thấy). Khoảng cách từ bóng đèn đến mặt cầu là $^ { 0 , 3 \mathrm { ~ m ~ } }$ . Thay số ta được:

$$
\mathrm { E } _ { \mathrm { m a x } } = { \sqrt { \frac { { \bigl ( } 4 \pi . 1 0 ^ { - 7 } \mathrm { T . m } { \bigr / } \mathrm { A } { \bigr ) } { \bigl ( } 3 . 0 0 . 1 0 ^ { 8 } \mathrm { m } { \bigr / } \mathrm { s } { \bigr ) } { \bigl ( } 3 . 0 \mathrm { W } { \bigr ) } } { 2 \pi { \bigl ( } 0 , 3 0 \mathrm { m } { \bigr ) } ^ { 2 } } } } = 4 5 \mathrm { V / m }
$$

Sử dụng biểu thức (34.21) để xác định độ lớn của cường độ từ trường:

$$
\mathrm { B } _ { \mathrm { m a x } } = \frac { \mathrm { E } _ { \mathrm { m a x } } } { \mathrm { c } } = \frac { 4 5 \mathrm { V / m } } { 3 , 0 0 . 1 0 ^ { 8 } \mathrm { m / s } } = 1 , 5 . 1 0 ^ { - 7 } \mathrm { T }
$$

Kết luận: Giá trị này của cường độ từ trường là nhỏ hơn hai bậc so với từ trường của Trái đất.

## Động lượng và áp suất bức xạ

Sóng điện từ vận chuyển động lượng cũng như năng lượng. Khi động lượng này hấp thụ bởi những bề mặt thì áp lực sẽ tác dụng lên các bề mặt này. Giả sử sóng vận chuyển với tổng năng lượng $\mathrm { T } _ { \mathrm { E R } }$ đến bề mặt trong một khoảng thời gian t thì tổng động lượng p (trường hợp hấp thụ hoàn toàn) được xác định:

$$
\displaystyle \mathfrak { p } = \frac { \mathrm { T } _ { \mathtt { E R } } } { \mathrm { c } }
$$

trong đó c là vận tốc ánh sáng. Chiều của sự biến thiên động lượng là chiều của chùm tia tới. Áp suất P gây ra trên một bề mặt được xác định bằng lực tác dụng trên một đơn vị diện tích: F A , kết hợp với định luật II Newton, ta có:

$$
\mathrm { P = } { \frac { \mathrm { F } } { \mathrm { A } } } { = } { \frac { 1 } { \mathrm { A } } } { \frac { \mathrm { d } \mathrm { p } } { \mathrm { d t } } }
$$

Thay phương trình (34.27) vào biểu thức tính áp suất:

$$
\mathrm { P = \frac { 1 } { A \ d i f } = \frac { 1 \ d f } { A \ d t } \{ \underset { \Delta } { T _ { \mathrm { E R } } } \ } _ { \mathrm { = } \mathrm { c } } \mathrm { \Lambda }  \mathrm { \Lambda } _ { \mathrm { c } } \mathrm { d } \mathrm { T } _ { \mathrm { E R } } ^ { \mathrm { E R } } \mathrm { \Lambda } _ { \mathrm { A } ^ { \prime } } \mathrm { d } \mathrm { t } ) 
$$

(dTER dt) A là tốc độ năng lượng đến bề mặt trên một đơn vị diện tích, được gọi là độ lớn



của vector Poynting. Do đó, áp suất bức xạ P gây ra trên bề mặt hấp thụ hoàn toàn được xác định:

$$
\mathrm { \bf P = \frac { S } { c } }
$$



Nếu như bề mặt phản xạ toàn phần (như gương) và bức xạ được chiếu tới thẳng góc thì độ lớn của sự biến thiên động lượng của vật dịch chuyển trong khoảng thời gian t sẽ có giá trị lớn gấp hai lần giá trị động lượng trong công thức (34.27). Điều này có nghĩa, động lượng được truyền trên một bề mặt bởi ánh sáng tới và ánh sáng phản xạ có giá trị bằng nhau là $\begin{array} { r } { \mathbf { p } = \mathrm { T } _ { \mathrm { E R } } \left/ \mathbf { c } \right. . \nabla \mathrm { i } \mathbf { v } \hat { \mathbf { a } } \mathbf { y } , } \end{array}$

$$
\displaystyle \mathsf { p } = \frac { 2 \mathsf { T } _ { \mathrm { E R } } } { \mathsf { c } }
$$

Áp suất bức xạ gây ra trên một bề mặt phản xạ toàn phần khi bức xạ được chiếu tới thẳng góc là:

$$
\mathrm { P = } \frac { 2 \mathrm { S } } { \mathrm { c } }
$$



Đối với bề mặt xảy ra phản xạ một phần, sự thay đổi áp suất nằm giữa $\mathrm { ~ S ~ } \boldsymbol { \mathscr { k } }$ và $2 \mathrm { S } / \mathrm { c }$ . Đối với ánh sáng mặt trời trực tiếp, áp suất bức xạ khoảng $5 . 1 0 ^ { - 6 } \mathrm { N } / \mathrm { m } ^ { 2 }$ .

# Bài tập mẫu 34.4: Quét ngang $\mathbf { H } \hat { \mathbf { e } }$ Mặt trời

Một lượng lớn bụi tồn tại trong không gian. Mặc dù trên lý thuyết những hạt bụi này có thể thay đổi về kích thước từ kích thước phân tử tới kích thước lớn hơn, nhưng rất ít bụi trong hệ mặt trời nhỏ hơn $0 { , } 2 \mu \mathrm { m }$ . Giải thích tại sao?

# Giải

Các hạt bụi chịu tác dụng của 2 lực chính: lực hấp dẫn kéo chúng về phía Mặt Trời và lực áp suất-bức xạ đẩy chúng ra xa khỏi Mặt Trời. Lực hấp dẫn tỷ lệ thuận với bậc 3 của bán kính của các hạt bụi hình cầu bởi vì nó tỷ lệ với khối lượng và vì vậy tỷ lệ với thể tích của hạt $4 \pi \mathrm { r } ^ { 3 } / 3$ . Áp suất bức xạ tỷ lệ thuận với bình phương bán kính bởi vì nó phụ thuộc vào tiết diện cắt ngang của hạt. Đối với các hạt lớn, lực hấp dẫn sẽ lớn hơn lực áp suất bức xạ. Đối với các hạt có bán kính nhỏ hơn $0 { , } 2 \mu \mathrm { m }$ lực gây ra từ áp suấtbức xạ sẽ lớn hơn lực hấp dẫn. Do đó, các hạt bị quét ra khỏi hệ mặt trời bởi ánh sáng mặt trời.

# Bài tập mẫu 34.5: Áp suất của bút chiếu Lazer

Khi trình bày báo cáo, nhiều người sử dụng bút laser để hướng sự chú ý của người theo dõi tới thông tin trên màn hình. Nếu một bút laser $3 { , } 0 \mathrm { m W }$ tạo ra một điểm sáng trên màn hình có đường kính $2 , 0 \mathrm { m m }$ , xác định áp suất bức xạ trên màn hình phản xạ $70 \%$ ánh sáng đập vào nó. Công suất $3 { , } 0 \mathrm { m W }$ là giá trị được lấy trung bình theo thời gian.

# Public_150 

Trong chương 37 chúng ta đã định nghĩa nhiễu xạ một cách không mấy chặt chẽ là sự loe ra của ánh sáng xuất

phát từ một khe hẹp. Tuy nhiên, không đơn giản chỉ là loe ra vì ánh sáng còn tạo nên một bức tranh giao thoa gọi là vân nhiễu xạ. Thí dụ, ánh sáng đơn sắc từ một nguồn ở xa vô cực (hay một lazer) đi qua một khe hẹp và sau đó được hứng bằng một màn quan sát, chúng sẽ tạo nên một bức tranh nhiễu xạ trên màn như trong hình 38.1. Bức tranh này bao gồm một dải sáng trung tâm mạnh, rộng (gọi là cực đại trung tâm) được bao quanh bởi một dải hẹp và yếu hơn (gọi là cực đại thứ cấp) và một loạt các dải tối xen kẽ.

![](images/image1.jpg)  
Hình 38.1: Hình ảnh nhiễu xạ hiện trên một màn quan sát khi ánh sáng đến màn, sau khi đi qua một khe hẹp dọc. Quá trình nhiễu xạ làm cho ánh sáng loe ra vuông góc với chiều dài của khe.

## Nhiễu xạ ánh sáng

Sự nhiễu xạ ánh sáng không giới hạn trong trường hợp khi ánh sáng đi qua một khoảng trống hẹp mà nó còn xảy ra khi ánh sáng đi qua một cạnh (mép) của đối tượng, chẳng hạn như hình 38.2. Chú ý rằng, các đường cực đại và cực tiểu chạy dọc gần như song song với nhau để tạo nên bức tranh dọc theo mép trái. Một lần nữa, chúng ta thấy hình ảnh các vân sáng và tối, giống như hình ảnh giao thoa trong chương 37.

![](images/image2.jpg)  
Hình 38.2: Ảnh nhiễu xạ qua cạnh của một vật.



Ánh sáng có bước sóng tương đương hoặc lớn hơn chiều rộng của một khe hẹp sẽ lan truyền mọi hướng trước khi đi qua khe. Hiện tượng này gọi là nhiễu xạ ánh sáng. Điều này chỉ ra rằng ánh sáng lan truyền hướng qua khe hẹp đến được cả những khu vực đáng ra tạo thành vùng tối nếu như ánh sáng truyền thẳng.



Phân loại: Gọi L, d là khoảng cách từ vân nhiễu xạ đến màn quan sát và nguồn sáng. Ta có hai loại nhiễu xạ:

• Nếu L, d là hữu hạn thì sóng phát ra từ S là sóng cầu: nhiễu xạ của sóng cầu được gọi là nhiễu xạ Fresnel Nếu L, d là vô hạn thì sóng phát ra từ S là sóng phẳng: nhiễu xạ của sóng phẳng được gọi là nhiễu xạ Fraunhofer.

### Chấm sáng Fresnel

Hình 38.3 cho thấy một mẫu nhiễu xạ kết hợp với bóng của một đồng xu. Một điểm sáng xuất hiện ở trung tâm, và các đường viền hình tròn mở rộng ra ngoài từ mép của bóng đồng xu. Chúng ta có thể giải thích điểm sáng trung tâm bằng cách sử dụng lý thuyết sóng ánh sáng và dự đoán xuất hiện cực đại giao thoa tại vị trí này. Từ quan điểm của tia quang học (trong đó ánh sáng được xem là tia di chuyển theo đường thẳng), chúng ta dự đoán tại tâm của ảnh nhiễu xạ là một bóng tối vì màn quan sát được che chắn hoàn toàn bởi đồng xu.

Quan điểm của Newton là quan điểm thịnh hành trong giới khoa học Pháp thời bấy giờ. Sau đó mới đến Fresnel, một kỹ sư quân đội trẻ theo đuổi sự đam mê của mình đối với quang học đến nỗi sao nhãng cả nhiệm vụ quân đội. Fresnel tin tưởng vào thuyết sóng ánh sáng và gửi một bài báo cho Viện Hàn Lâm khoa học để mô tả những thí nghiệm của mình và cách giải thích những thí nghiệm ấy bằng thuyết sóng.

Chú y diém sáng tai tàm

![](images/image3.jpg)  
Hình 38.3: Ảnh nhiễu xạ của một đồng xu. Chú ý đến những vòng nhiễu xạ đồng tâm và chấm sáng Fresnel tại tâm của ảnh nhiễu xạ.

Năm 1819 Viện Hàn Lâm mà đa số những người ủng hộ Newton nghĩ rằng để thách thức quan điểm sóng đã tổ chức một cuộc thi tranh giải về đề tài nhiễu xạ, Fresnel đã thắng. Tuy nhiên, những người ủng hộ Newton vẫn không chịu nghe theo mà cũng không chịu im lặng. Một trong những người ấy là Poisson, nếu lý thuyết Fresnel đúng thì sóng sáng sẽ nhiễu xạ vào vùng bóng tối của quả cầu khi chúng đi qua mép của quả cầu và tạo thành một chấm sáng tại tâm điểm của bóng tối đó. Trước sự ngạc nhiên của Poisson, vị trí này đã được quan sát bởi Dominique Arago ngay sau đó. Do đó, dự đoán của Poisson đã củng cố lý thuyết sóng hơn là bác bỏ nó.





### Nhiễu xạ Fraunhofer

Giả sử màn quan sát được đặt rất xa khe hẹp và các tia sáng tới khe là song song nhau (hình 38.4). Trong mô hình này, hình ảnh thu được trên màn quan sát được gọi là mẫu nhiễu xạ Fraunhofer.

Nhiễu xạ ám chỉ tới hoạt động chung của sóng khi chúng đi qua một khe hẹp. Trên thực tế, ảnh được thấy trên màn quan sát thực sự là ảnh giao thoa. Sự giao thoa giữa các phần của ánh sáng tới chiếu lên các khu vực khác nhau của khe. Một vân sáng được quan sát dọc theo trục chính $( \theta = 0 )$ ), các vân sáng và tối được quan sát xen kẽ hai bên của vân sáng trung tâm.

![](images/image4.jpg)  
Hình 38.4: (a) Hình học để phân tích nhiễu xạ Fraunhofer qua một khe, (b) Ảnh nhiễu xạ Fraunhofer.

### Nhiễu xạ qua một khe hẹp

Độ rộng hữu hạn của khe là điều kiện cho nhiễu xạ Fraunhofer. Theo nguyên lý Huygens, từng phần của khe hẹp đóng vai trò như một nguồn của sóng ánh sáng. Do đó, ánh sáng từ một phần của khe có thể giao thoa với ánh sáng từ một phần khác. Cường độ sáng sau cùng quan sát trên màn hình tùy thuộc vào hướng θ. Dựa vào những phân tích trên, hình ảnh nhiễu xạ thực sự là một ảnh giao thoa, trong đó các nguồn sáng khác nhau là các phần khác nhau của cùng một khe.

Để phân tích hình ảnh nhiễu xạ, chúng ta chia khe thành hai đới có độ rộng bằng nhau a 2 , như hình 38.5. Lưu ý rằng tất cả các sóng rời khỏi khe đều cùng pha, xét các tia 1 và 3. Tuy nhiên, tất cả sóng tới cùng pha khi chúng ló ra khỏi khe hẹp thì sóng 1 lan truyền xa hơn sóng $3 ~ \mathrm { m o t }$ đoạn bằng với hiệu quang lộ: a sin  , trong đó: a là độ rộng của khe. Tương tự, chúng ta có thể lặp lại cách phân tích trên cho từng cặp tia xuất phát từ những điểm tương ứng



![](images/image5.jpg)

Hình 38.5: Nhiễu xạ qua một khe hẹp, khi $\mathrm { L } \gg \mathrm { a }$ chúng ta có thể xem gần đúng các tia 1, 2, 3, 4, 5 song song với nhau, làm một góc θ với trục chính giữa.

Biết trước độ rộng khe a và bước sóng $\lambda$ , phương trình (38.1) cho chúng ta góc θ ứng với vân tối thứ nhất nằm trên và dưới trục chính giữa.

Bây giờ chúng ta chia khe thành bốn đới bằng nhau có độ rộng a 4 . Hiệu lộ trình giữa mỗi cặp tia xuất phát từ những điểm tương ứng trong hai đới $\mathrm { k } \dot { \hat { \mathbf { e } } }$ nhau bằng sin  . Trong trường hợp như vậy hiệu quang lộ bằng  2 nên chúng ta có: 4

$$
\frac { \mathrm { a } } { 4 } \sin \theta = \pm \frac { \lambda } { 2 }  \sin \theta = \pm 2 \frac { \lambda } { \mathrm { a } }
$$

Tương tự, khi chia khe thành sáu đới bằng nhau có độ rộng $\mathrm { a } / 6$ thì vân tối xuất hiện



trên màn quan sát khi:



Giải:

Dựa vào phương trình (38.1), độ lớn của góc nhiễu xạ θ ứng với các cực tiểu nhiễu xạ sẽ giảm khi tăng độ rộng của khe, do đó ảnh nhiễu xạ sẽ bị thu hẹp lại.

$$
2 | \mathbf { y } _ { 1 } | = 2 { \big | } \mathrm { L s i n } \ \mathbf { \theta } _ { \mathrm { t \bar { o } i } } { \big | } = 2 { \bigg | } \pm \mathrm { L } { \begin{array} { l } { \lambda } \\ { - { \big | } = 2 \mathrm { L } } \\ { { \mathrm { a } } } \end{array} } - 2 \mathrm { L } { \begin{array} { l } { \lambda } \\ { - = 2 . 2 . } \\ { { \mathrm { a } } } \end{array} } { \frac { 5 8 0 . 1 0 ^ { - 9 } } { 3 . 1 0 ^ { - 3 } } } = 7 , 7 3 . 1 0 \quad \mathrm { m } = 0 , 7 7 3 \ \mathrm { m m }
$$

Cần chú ý rằng giá trị này lớn hơn nhiều lần so với độ rộng của khe.

# Sự phân bố cường độ ảnh nhiễu xạ qua một khe

Khi chú ý đến những hiệu ứng nhiễu xạ, sự biến thiên cường độ ảnh giao thoa qua một khe được tính theo công thức:

$$
\begin{array} { r } { \mathrm { I } = \mathrm { I } _ { \mathrm { m a x } } \Big [ \frac { \sin \big ( \pi \mathrm { a s i n } \Theta , \lambda \big ) \Big ] ^ { 2 } } { \pi a \sin \theta / \lambda } } \\ { \mathrm { ~ L ~ } } \end{array}
$$

trong đó, $\mathrm { I } _ { \mathrm { m a x } } \mathrm { l } \dot { { \mathrm a } }$ giá trị lớn nhất của cường độ tại tâm của bức tranh nhiễu xạ tương ứng với $\theta = 0 , \lambda$ là bước sóng của ánh sáng chiếu đến khe hẹp. Từ điều kiện cường độ cực tiểu:

$$
\frac { \pi \mathsf { a } \mathsf { s i n } \Theta _ { \mathsf { t } \widetilde { \mathsf { o } } \mathrm { i } } } { \lambda } = \mathsf { m } \pi
$$

$$
\mathsf { s i n } \theta _ { \mathsf { t } \widetilde { \mathsf { o i } } } = \mathsf { m } \frac { \lambda } { \mathsf { a } } , \mathsf { v } \widetilde { \mathsf { o i } } \mathsf { m } = \pm 1 , \pm 2 , \pm 3 \cdots
$$



![](images/image6.jpg)  
Hình 38.6: (a) Đồ thị biểu diễn sự phụ thuộc cường độ sáng I so với $\left( \pi / \lambda \right)$ a sin  cho nhiễu xạ Fraunhofer qua một khe, (b) Ảnh nhiễu xạ Fraunhofer.

### Nhiễu xạ qua hai khe

Trong những thí nghiệm hai khe của chương 37, chúng ta đã cho rằng các khe rất hẹp so với bước sóng của ánh sáng dọi đến hai khe $a \ll \lambda$ ). Với những khe hẹp như thes cực đại chính giữa của ảnh nhiễu xạ của từng khe bao phủ toàn bộ màn quan sát. Hơn nữa sự giao thoa của áng sáng từ hai khe tạo nên những vân có cường độ xấp xỉ bằng nhau. Tuy nhiên, trong thực tế với ánh sáng khả kiến điều kiện ( $a \ll \lambda$ ) không phải bao giờ cũng thỏa mãn. Với những khe tương đối rộng, sự giao thoa của áng sáng từ hai khe tạo nên những vân sáng mà cường độ không phải tất cả đều bằng nhau. Thực tế là cường độ của chúng bị thay đổi do nhiễu xạ của ánh sáng qua mỗi khe.

# Phương trình biểu diễn cường độ của ảnh nhiễu xạ qua hai khe hẹp

# Sự phân bố cường độ ảnh nhiễu xạ qua hai khe

Ảnh nhiễu xạ của hai khe, mô tả bởi phương trình (38.3) và được thể hiện trong hình 38.7. Đường màu xanh nét đứt là ảnh nhiễu xạ qua một khe hẹp. Đường cong màu nâu là do giao thoa qua hai khe hẹp, thành phần này sẽ tạo ra tất cả các đỉnh cùng độ cao (cường độ). Chiều cao các đỉnh không đồng đều do thành phần nhiễu xạ qua mỗi khe (thừa số trong dấu ngoặc vuông).

Phương trình (37.2) cho biết điều kiện để xảy ra cực đại giao thoa là: dsin $\theta = \mathrm { m } \lambda$ , trong đó: d là khoảng cách giữa hai khe. Phương trình (38.1) cho biết cực tiểu nhiễu xạ đầu tiên xảy ra khi asin $\theta = \lambda$ , trong đó a là độ rộng của mỗi khe. Chia phương trình (37.2) cho phương trình (38.1) (với $\mathrm { m } = 1 \mathrm { \AA }$ ) cho phép chúng ta xác định cực đại giao thoa đầu tiên trùng với cực tiểu nhiễu xạ đầu tiên:



• Điều kiện cho cực đại giao thoa: dsin $\theta = \mathrm { m } \lambda$ • Điều kiện cho cực tiểu nhiễu xạ đầu tiên: a sin $\theta = \lambda$



Như vậy, cường độ sáng ở cực đại thứ 1, 2, 3… rất nhỏ hơn so với cường độ sáng của cực đại chính giữa nên trong trường hợp nhiễu xạ qua nhiều khe ta chỉ xét trong vân giữa nhiễu xạ.

![](images/image7.jpg)  
Hình 38.7: Cường độ sáng của ảnh nhiễu xạ qua nhiều khe hẹp.

### Năng suất phân giải

Khả năng của các hệ thống quang học để phân biệt giữa các nguồn ở gần nhau bị giới hạn do bản chất sóng của ánh sáng. Thực chất, các ảnh qua thấu kính đều là ảnh nhiễu xạ, điều này rất quan trọng khi chúng ta muốn phân biệt hai nguồn điểm ở xa mà khoảng cách góc giữa chúng rất nhỏ. Hình 38.8 cho thấy hai nguồn sáng cách xa một khe hẹp có độ rộng là a. Nếu hai nguồn sáng đủ xa để giữ cho các cực đại trung tâm không chồng lấn lên nhau thì ảnh có thể phân biệt được (hình 38.8a). Ngược lại, nếu hai nguồn sáng ở gần nhau thì hai cực đại trung tâm chồng lấn lên nhau và ảnh không phân giải được vì nhiễu xạ (hình 38.8b).



![](images/image8.jpg)

Hình 38.8: Hai nguồn điểm cách xa một khe hẹp tạo ra hình ảnh nhiễu xạ: (a) Ảnh phân giải được, (b) Ảnh không phân giải được.

# Tiêu chuẩn Rayleigh

Trong hình 38.9 cho thấy khoảng cách góc của hai nguồn điểm có giá trị sao cho cực đại chính giữa của ảnh nhiễu xạ của nguồn này rơi đúng vào cực tiểu thứ nhất của bức tranh nhiễu xạ của nguồn kia. Điều kiện giới hạn này được gọi là tiêu chuẩn Rayleigh về khả năng phân giải.

Theo tiêu chuẩn Rayleigh, chúng ta có thể xác định sự tách biệt góc tối thiểu $\theta _ { \mathrm { m i n } }$ giữa hai nguồn sáng tại khe trong hình 38.8 (hình ảnh đã được phân giải). Phương trình 38.1 chỉ ra rằng cực tiểu đầu tiên của ảnh nhiễu xạ một khe thỏa điều kiện:

$$
\sin \theta = \frac { \lambda } { - }
$$

Khi ảnh được phân giải thì khoảng cách góc giữa các nguồn lớn hơn $\theta _ { \mathrm { m i n } }$ , chúng ta sẽ có thể phân ly hai nguồn ấy, còn nếu nó nhỏ hơn quá nhiều thì không thể phân ly được. Các nguồn cũng phải $\mathrm { c } \acute { \mathrm { o } }$ độ sáng tương đối bằng nhau thì mới có thể dùng tiêu chuẩn Rayleigh. Thêm vào đó chúng ta thừa nhận điều kiện nhìn phải lý tưởng.



![](images/image9.jpg)  
Hình 38.9: Hình ảnh nhiễu xạ của hai nguồn (đường nét liền) và ảnh tổng hợp (đường nét đứt) khi thay đổi khoảng cách góc giữa các nguồn khi ánh sáng truyền qua một khẩu độ tròn. Đường nét đứt là tổng hợp từ hai đường cong nét liền.

Khi các nguồn sáng ở xa nhau thì ảnh được phân giải tốt. Các đường cong liền nét là các ảnh nhiễu xạ riêng biệt còn các đường đứt nét là ảnh sau cùng (hình 38.9a).

Các nguồn sáng chia cách nhau bởi một góc thỏa mãn tiêu chuẩn Rayleigh thì ảnh được phân giải. Các đường cong liền nét là ảnh nhiễu xạ riêng biệt. Các đường đứt nét là ảnh sau cùng (hình 38.9b).

Các nguồn sáng gần nhau thì ảnh không được phân giải. Các đường liền nét là ảnh nhiễu xạ riêng biệt. Các đường đứt nét là ảnh sau cùng và ảnh trông giống như một nguồn duy nhất (hình 38.8c).

Hình ảnh sao Diêm Vương và Mặt trăng Charon như trên hình 38.11 là một ví dụ về độ phân giải. Nếu như dùng kính thiên văn Trái đất thì sẽ không phân biệt được mà phải cần dùng đến kính viễn vọng Hubble mới có thể phân giải rõ ràng hai vật.



![](images/image10.jpg)  
Hình 38.11: Hình ảnh sao Diêm Vương và Mặt Trăng Charon.

## Cách tử Nhiễu xạ

### Nhiễu xạ qua cách tử

Cách tử nhiễu xạ, một dụng cụ dùng cho việc phân tích các nguồn sáng, là hệ thống gồm N khe hẹp giống hệt nhau với độ rộng của mỗi khe là a, khoảng cách giữa hai khe liền kề là d, được đặt cách đều nhau với khoảng cách giữa hai khe liên tiếp là $\mathcal { l }$ (chu kỳ của cách tử). Cách tử có cấu tạo rất tinh vi, trên mỗi milimet chiều dài có đến hàng trăm khe. Một cách tử truyền qua có thể được tạo ra bằng cách cắt các rãnh (khe) song song trên một tấm kính bằng máy khắc có độ chính xác cao. Khoảng cách giữa các rãnh trong suốt đối với ánh sáng vì vậy đóng vai trò như các khe riêng biệt. Một cách tử phản xạ có thể được tạo ra bằng cách cắt các rãnh song song trên bề mặt của một vật liệu phản xạ. Sự phản xạ của ánh sáng từ các khoảng không gian giữa các rãnh rõ hơn là sự phản xạ từ các rãnh được khắc vào bên trong vật liệu. Vì vậy, các khoảng không gian giữa các rãnh đóng vai trò giống như là các nguồn sáng phản xạ song song giống như các khe trong một cách tử truyền qua. Công nghệ hiện nay có thể sản xuất các cách tử có các khe rất nhỏ. Ví dụ: một cách tử điển hình được khắc với 5000 khe/cm có độ rộng mỗi khe $\mathbf { d } = \left( 1 / 5 0 0 0 \right) \mathbf { c m } = 2 . 1 0 ^ { - 4 } \mathbf { c m } .$

Một phần của một cách tử nhiễu xạ được minh họa trong hình 38.12. Một sóng phẳng tới từ bên trái, vuông góc với mặt phẳng cách tử. Hình dạng thu được trên màn nằm bên phải mặt cách tử là kết quả của các hiệu ứng giao thoa và nhiễu xạ được kết hợp.

Chú ý: Cách tử nhiễu xạ là một cách tử giao thoa. Giống với dạng nhiễu xạ, cách tử nhiễu xạ là một thuật ngữ sai nhưng được dùng nhiều trong ngôn ngữ vật lý. Cách tử nhiễu xạ phụ thuộc vào sự nhiễu xạ trên cùng phương khi hai khe lan truyền ánh sáng rộng ra để ánh sáng từ các khe khác nhau có thể giao thoa. Sẽ là chính xác hơn nếu gọi thiết bị này là cách tử giao thoa, nhưng cách tử nhiễu xạ lại là tên được sử dụng.



![](images/image11.jpg)  
Hình 38.12: Nhiễu xạ qua cách tử. Khoảng cách giữa các khe là d, hiệu quang lộ của hai tia sáng từ hai khe liền kề là dsin .

Sóng từ tất cả các khe đồng pha nhau khi chúng ra khỏi các khe. Đối với một hướng bất kỳ θ được xác định từ phương ngang, tuy nhiên, các sóng di chuyển những quãng đường khác nhau trước khi đập vào màn. Cần chú ý trên hình 38.12 rằng hiệu lộ trình  giữa các tia từ hai khe $\mathrm { k } \dot { \hat { \mathbf { e } } }$ nhau bất kỳ bằng dsin . Nếu sự khác nhau của quãng đường di chuyển này bằng với một bước sóng hoặc một số nguyên lần bước sóng thì sóng từ tất cả các khe sẽ đồng pha nhau tại màn và sẽ tạo thành một vân sáng. Vì vậy, điều kiện để đạt được cực đại trong hình dạng giao thoa tại góc $\boldsymbol { \theta } _ { \mathsf { s i n g } } \mathrm { l } \dot { \mathbf { a } }$

$$
\mathrm { d } \mathrm { s i n } \theta _ { \mathrm { s i n g } } = \mathrm { m } \lambda , \mathrm { v } \dot { \mathrm { o } } \mathfrak { i } \mathrm { m } = 0 , \pm 1 , \pm 2 , \pm 3 \ldots
$$

Công thức này có thể được sử dụng để tính bước sóng nếu biết được độ rộng khe d và góc $\theta _ { \mathsf { s i n g } }$ . Nếu bức xạ tới bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ nhiều bước sóng thì cực đại bậc m đối với mỗi bước sóng xảy ra tại một góc xác định. Tất cả các bước sóng tại $\theta = 0$ , tương ứng với $\mathbf { m } = 0$ là cực đại bậc 0 (cực đại trung tâm). Cực đại bậc nhất $( \mathbf { m } = 1 )$ ) được xác định tại góc thoả mãn mối liên h $\hat { \underline { { \circ } } } \ \mathrm { s i n } \theta _ { \mathrm { \mathfrak { s a n g } } } = \lambda / \mathrm { d }$ , cực đại bậc hai $( \mathbf { m } = 2$ ) được xác định tại một góc $\boldsymbol { \theta } _ { \mathsf { s i n g } }$ lớn hơn và tương tự cho các cực đại bậc cao hơn. Khi các giá trị d nhỏ điển hình trong một cách tử nhiễu xạ thì góc sáng lớn, giống như ví dụ 38.5.

### Sự phân bố cường độ qua cách tử nhiễu xạ

Sự phân bố cường độ đối với một cách tử nhiễu xạ đạt được khi sử dụng một nguồn đơn sắc được chỉ ra trong hình 38.13. Chú ý độ sắc nét của cực đại trung tâm và độ rộng của các vùng tối được so sánh với các vân sáng rộng đặc trưng của dạng giao thoa hai khe (xem hình 37.6). Bên cạnh đó cũng có thể tham khảo hình 37.7 để thấy rằng độ rộng của cực đại cường độ giảm khi số khe tăng lên. Bởi vì cực đại bậc trung tâm rất sắc nét, chúng sáng hơn nhiều cực đại giao thoa hai khe.





![](images/image12.jpg)

Hình 38.13: Đồ thị biểu diễn sự phụ thuộc của cường độ theo sinθ của cách tử nhiễu xạ. Cực đại trung tâm, bậc một, bậc hai được biểu diễn.

Đặc điểm của quang phổ cách tử:

• Quang phổ của cách tử chỉ có một vài giá trị.   
Trong quang phổ của lăng kính thì tia tím bị lệch ít nhất, tia đỏ bị lệch nhiều nhất. So với quang phổ của lăng kính thì quang phổ của cách tử có các vệt vào phân bố đều đặn hơn.

Câu hỏi 38.1: Ánh sáng cực tím có bước sóng $3 5 0 \mathrm { n m }$ đập vào một cách tử nhiễu xạ có độ  củarộng khe d và hình thành một dạng giao thoa trên màn ở khoảng cách L. Các góc sáng cực đại giao thoa có giá trị lớn. Các vị trí của vân sáng được đánh dấu trên màn. Bây giờ ánh sáng đỏ có bước sóng $7 0 0 \mathrm { n m }$ được sử dụng với một cách tử nhiễu xạ để tạo thành một dạng nhiễu xạ khác trên màn. Các vân sáng của dạng nhiễu xạ này sẽ được cố định tại các vị trí đánh dấu trên màn hay không nếu:

(a) Màn được di chuyển tới khoảng cách 2L từ cách tử nhiễu xạ.   
(b) Màn được di chuyển tới khoảng cách L/2 từ cách tử nhiễu xạ.   
(c) Cách tử nhiễu xạ được thay thế bằng một khe có độ rộng 2d.   
(d) Cách tử nhiễu xạ được thay thế bằng một khe có độ rộng d/2.   
(e) Không gì thay đổi?

Câu hỏi 38.2: Đĩa compact là một cách tử nhiễu xạ. Ánh sáng phản xạ từ bề mặt của một đĩa compact bao gồm nhiều màu như trên hình 38.14. Các màu và cường độ của chúng phụ thuộc vào hướng của CD so với mắt và so với nguồn sáng. Giải thích hiện tượng này.

# Trả lời:

Bề mặt của một CD có một rãnh hình xoắn ốc (các rãnh kề nhau có khoảng cách là $1 ~ \mu \mathrm { m } )$ . Vì vậy, bề mặt đĩa đóng vai trò như một cách tử nhiễu xạ. Ánh sáng phản xạ từ các vùng giữa các khe hẹp này chỉ giao thoa chồng

![](images/image13.jpg)

hể phụ ng của au của

đĩa CD đóng vai trò như cách tử nhiễu xạ đối với ánh sáng trắng và truyền đi các màu khác nhau, theo



các hướng

Hình 38.14: Các vạch rất mảnh, mỗi vạch có độ rộng $1 \ \mu \mathrm { m }$ , trên đĩa compact laser tác dụng như một cách tử nhiễu xạ



khác nhau. Các màu khác nhau được nhìn thấy trên một phần nào đó của đĩa sẽ thay đổi khi nguồn sáng, trong trường hợp này là CD, hoặc khi thay đổi hướng nhìn. Sự thay đổi hướng nhìn làm cho góc tới hay góc của ánh sáng nhiễu xạ bị thay đổi.

# Bài tập mẫu 38.2:

Ánh sáng đơn sắc từ một laser heli-neon $\lambda = 6 3 2 , 8 \mathrm { n m }$ ) chiếu vuông góc vào một cách tử nhiễu xạ có 6000 khe trên một centimet. Tìm các góc ứng với cực đại bậc nhất và bậc hai.

# Giải:

Quan sát hình 38.12 và tưởng tượng rằng ánh sáng tới từ bên trái phát ra từ laser helineon. Chúng ta hãy xác định các giá trị thích hợp của góc θ đối với cực đại giao thoa.

Khoảng cách giữa các khe là nghịch đảo của số khe trên mỗi centimet:

$$
\mathrm { d } = \frac { 1 } { 6 0 0 0 } \mathrm { c m } = 1 { , } 6 6 7 { . } 1 0 ^ { - 4 } \mathrm { c m } = 1 6 6 7 \mathrm { n m }
$$

Giải phương trình (38.7) đối với sinθ và cực địa bậc nhất ứng với $\mathbf m = 1$ để tìm giá trị của góc $\theta _ { 1 }$ :

$$
\sin \theta \underset { 1 } { = } \frac { 1 . \lambda } { \mathrm { d } } = \frac { 6 3 2 , 8 \mathrm { ~ n m } } { 1 6 6 7 \mathrm { ~ n m } } \Rightarrow \theta \underset { 1 } { = } 2 2 , 3 1 ^ { \circ }
$$

Lặp lại đối với cực đại bậc hai $( \mathbf { m } = 2 )$ ):

$$
\sin \theta \ _ { 2 } = \frac { 2 . \lambda } { \mathrm { ~ d ~ } } = \frac { 2 . 6 3 2 , 8 \ \mathrm { n m } } { 1 6 6 7 \ \mathrm { n m } } \Rightarrow \theta \ _ { 2 } = 4 9 , 4 1 ^ { \circ }
$$

Mở rộng: Điều gì sẽ thay đổi nếu cực đại bậc ba cần được xác định? Có thể xác định được không?

Trả lời: Với $\mathbf { m } = 3$ thì $\sin \theta _ { 3 } = 1 , 1 3 9$ . Vì sinθ luôn nhỏ hơn 1, kết quả này không phải là một kết quả hợp lí. Vì vậy, chỉ các cực đại trung tâm, bậc nhất và bậc hai có thể được xác định trong trường hợp này.

### Một số ứng dụng của cách tử nhiễu xạ

# a. Phổ kế cách tử nhiễu xạ

Hình vẽ của một thiết bị đơn giản được sử dụng để đo các góc trong một dạng nhiễu xạ được chỉ ra trên hình 38.15. Thiết bị này là một phổ kế cách tử nhiễu xạ. Ánh sáng di chuyển qua một khe, và một chùm ánh sáng được chuẩn trực chiếu vào cách tử. Ánh sáng nhiễu xạ rời khỏi cách tử tại các góc thoả mãn phương trình (38.7) và một kính viễn vọng được sử dụng để quan sát ảnh của khe. Bước sóng có thể được xác định bằng việc đo lường các góc chính xác tại đó ảnh của khe xuất hiện tại các góc khác nhau.



Phổ kế này là một thiết bị được sử dụng trong phổ $\mathrm { k } \acute { \mathrm { e } }$ nguyên tử, trong đó ánh sáng từ một nguyên tử được phân tích để tìm các thành phần bước sóng. Các thành phần bước sóng có thể được sử dụng nhận dạng nguyên tử. Các phổ nguyên tử sẽ được khảo sát trong chương 42 của phần mở rộng của giáo trình này.



![](images/image14.jpg)  
Hình 38.15: Quang phổ kế cách tử nhiễu xạ.

# b. Van cách tử nhiễu xạ

Ứng dụng khác của các cách tử nhiễu xạ là van ánh sáng cách tử − grating light valve (GLV), thiết bị này cạnh tranh với các thiết bị micromirror số (DMDs). GLV là một microchip silicon được lắp vào một dãy băng silicon nitride song song được phủ một lớp bạc mỏng (hình 38.16). Mỗi dãy dài xấp xỉ $2 0 ~ { \mu \mathrm { m } }$ , rộng $5 ~ { \mu \mathrm { m } }$ và được tách biệt với lớp silicon bởi một lớp không khí có độ dày là bậc của $1 0 0 ~ \mathrm { { n m } }$ . Khi không có điện thế, tất cả các dãy ở cùng mức nhau. Trong trường hợp này, dãy băng đóng vai trò như một bề mặt phẳng, phản xạ ánh sáng tới.

![](images/image15.jpg)

Hình 38.16: Một phần nhỏ của van ánh sáng cách tử. Băng phản chiếu xen kẽ ở các mức hoạt động khác nhau như một cách tử nhiễu xạ, cung cấp khả năng điều khiển tốc độ rất cao của hướng ánh sáng đến một thiết bị kỹ thuật số.

Khi có điện thế áp vào giữa một dãy băng và điện cực trên lớp silicon, một lực điện xuất hiện kéo dãy băng hạ xuống, gần hơn với lớp silicon. Các dãy băng có thể được luân phiên kéo xuống trong khi các khoảng không gian giữa chúng được nâng cao. Vì vậy, các dãy băng đóng vai trò như một cách tử nhiễu xạ mà ở đó sự giao thoa tăng cường đối với một bước sóng ánh sáng cụ thể có thể được hướng vào một màn hoặc các hệ hiển thị quang học





khác. Nếu ba thiết bị − một cho ánh sáng đỏ, một cho ánh sáng xanh da trời, và một cho ánh sáng xanh lá cây – được sử dụng thì việc hiển thị toàn màu có thể thực hiện.

Bên cạnh việc sử dụng trong hiển thị video, GLV còn được ứng dụng trong công nghệ cảm biến điều hướng quang học laser, việc in thương mại từ máy tính thành tấm, và các loại thiết bị chụp ảnh khác.

# c. Hologram − Kỹ thuật chụp ảnh giao thoa Lazer

Một ứng dụng thú vị khác của cách tử nhiễu xạ là phương pháp toàn ảnh (holography), sử dụng trong việc tạo ảnh ba chiều của vật. Nguyên lý vật lý của phương pháp toàn ảnh được phát triển bởi Dennis Gabor (1900-1979) vào năm 1948 và giúp ông giành giải Nobel Vật lý vào năm 1971. Sự yêu cầu về ánh sáng kết hợp cho phương pháp toàn ảnh đã trì hoãn thành phương pháp tạo ảnh của Gabor cho đến khi laser được phát triển vào những năm 1960. Hình 38.17 cho thấy một ảnh toàn ký (ảnh ba chiều – hologram) nhìn từ hai vị trí khác nhau và đặc tính ba chiều của ảnh. Lưu ý sự khác nhau khi nhìn ảnh thông qua kính khuếch đại trong các hình 38.17a và 38.17b.

![](images/image16.jpg)  
Hình 38.17: Bảng mạch được hiển thị ở hai chế độ xem khác nhau.

Hình 38.18 cho thấy cách mà một hologram được tạo ra. Ánh sáng từ nguồn laser được tách thành hai phần bởi một gương mạ bạc tại B. Một phần của chùm tia phản xạ từ vật được chụp ảnh và đập vào một phim ảnh. Phần còn lại của chùm tia bị phân kỳ bởi kính L2, phản xạ từ các gương M1 và M2, và cuối cùng đập vào phim. Hai chùm tia chồng chập lên nhau để tạo thành một dạng giao thoa cực kỳ phức tạp trên phim. Dạng giao thoa này có thể được tạo ra chỉ khi mối quan hệ về pha của hai sóng là hằng số thông qua sự phơi sáng của phim. Điều kiện này đạt được bằng việc chiếu vào màn hình chùm ánh sáng thông qua một pinhole hoặc sử dụng bức xạ laser kết hợp. Hologram thu nhận không chỉ cường độ của ánh sáng tán xạ từ vật (giống như trong phương pháp chụp ảnh truyền thống), mà còn ghi nhận sự khác biệt về pha giữa chùm tia tham chiếu (reference light) và chùm tia tán xạ từ vật. Do bởi sự khác nhau về pha này, một dạng giao thoa được hình thành và tạo thành ảnh mà trong đó tất cả thông tin ba chiều được bảo toàn.





![](images/image17.jpg)  
Hình 38.18: Phương pháp chụp ảnh Hologram.

Trong một ảnh được chụp bằng phương pháp bình thường, môt kính được sử dụng để hội tụ ảnh để mỗi điểm trên vật tương ứng với một điểm trên ảnh. Chú ý rằng kính không được sử dụng trong hình 38.18 để hội tụ ánh sáng lên phim. Vì vậy, ánh sáng từ mỗi điểm trên vật sẽ xuất hiện tại tất cả các điểm trên phim. Vì vậy, mỗi vùng của phim trong đó hologram được ghi nhận sẽ chứa đựng thông tin về tất cả các điểm được chiếu trên vật, điều này sẽ đưa đến một kết quả đáng chú ý: nếu một vùng nhỏ của hologram được cắt ra từ phim, ảnh hoàn chỉnh của vật có thể được tạo ra từ phần nhỏ này. (Chất lượng của ảnh bị giảm xuống nhưng một ảnh hoàn chỉnh được tạo thành).

Một hologram được quan sát tốt nhất bằng việc cho chùm ánh sáng kết hợp di chuyển qua một tấm phim giống như quan sát ngược lại dọc theo hướng từ đó chùm ánh sáng được phát ra. Hình ảnh giao thoa trên phim đóng vai trò như là một cách tử nhiễu xạ. Hình 38.19 cho thấy 2 tia sáng đập vào và di chuyển qua phim. Đối với mỗi tia, các tia $\mathbf { m } = 0$ và $\mathbf { m } = \pm 1$ trên hình ảnh nhiễu xạ cho thấy xuất hiện từ bên phải của phim. Các tia $\mathbf { m } = + 1$ hội tụ để tạo thành một ảnh thực của màn và đây không phải là được quan sát một cách bình thường. Bằng việc mở rộng các tia sáng tương ứng với $\mathrm { m } = - 1$ về phía sau phim, sẽ xuất hiện một ảnh ảo tại đó và ánh sáng tới từ đó sẽ giống với ánh sáng tới từ vật thật khi phim được phơi sáng. Ảnh này là ảnh được nhìn thấy khi quan sát thông qua phim toàn ảnh (holographic film).

Phương pháp toàn ảnh có một vài ứng dụng. Chúng ta có thể có một hologram trên thẻ tín dụng. Loại hologram đặc biệt này được gọi là rainbow hologram và được thiết kế để được quan sát trong ánh sáng trắng được phản xạ.



# d. Nhiễu xạ của tia X bởi các tinh thể

Về nguyên tắc, bước sóng của bất kỳ sóng điện từ có thể được xác định nếu có một cách tử thích hợp (các rãnh được chia nhỏ ở mức độ bước sóng). Tia X, được khám phá bởi



Wilhelm Roentgen (1845−1923) vào năm 1895, là sóng điện từ có bước sóng rất ngắn (ở mức $0 , 1 \mathrm { n m } )$ . Sẽ không thể tạo một cách tử có khoảng cách giữa các khe nhỏ đến mức đó bằng quá trình cắt được miêu tả ở phần mở đầu của phần 38.4. Tuy nhiên, khoảng cách ở mức độ nguyên tử trong vật rắn lại vào khoảng 0,1 nm. Năm 1913, Max von Laue (1879−1960) đề nghị rằng mạng nguyên tử bình thường trong tinh thể có thể đóng vai trò như một cách tử nhiễu xạ ba chiều đối với tia X. Những thí nghiệm sau đó đã chứng minh dự đoán này. Hình dạng nhiễu xạ từ tinh thể trông phức tạp do bởi tính chất ba chiều của cấu trúc tinh thể. Tuy nhiên, sự nhiễu xạ tia X đã chứng minh là một phương pháp hiệu quả trong việc giải thích các cấu trúc này và trong việc nghiên cứu cấu trúc vật chất.

![](images/image18.jpg)  
Hình 38.20: Nhiễu xạ tia X qua tinh thể.

Hình 38.20 cho thấy một bố trí thực nghiệm trong việc quan sát nhiễu xạ tia X từ một tinh thể. Một chùm tia X đơn sắc được chuẩn trực chiếu vào một tinh thể. Các chùm tia nhiễu xạ có cường độ mạnh trong các hướng xác định, tương ứng với sự giao thoa tăng cường từ các sóng phản xạ từ các lớp của nguyên tử trong tinh thể. Các chùm tia nhiễu xạ, có thể được ghi nhận bằng một tấm phim, tạo thành một mảng các vết được gọi là hình dạng Laue giống như trên hình 38.21a. Cấu trúc tinh thể có thể được xác định bằng việc phân tích vị trí và cường độ của các vết khác nhau trên hình ảnh nhiễu xạ này. Hình 38.21b cho thấy hình ảnh Laue từ tinh thể enzyme, sử dụng một phạm vi rộng lớn các bước sóng để hình ảnh này được tạo ra.

![](images/image19.jpg)



Hình 38.21: (a) Ảnh Laue tinh thể đơn của nguyên tố Be, (b) Ảnh Laue của enzym Rubisco.



Sự sắp xếp của các nguyên tử trong một tinh thể muối natriclorua (NaCl) được chỉ ra trên hình 38.22. Mỗi ô đơn vị (khối hình học lặp lại trong tinh thể) là một hình lập phương có độ dài cạnh là a. Một sự khảo sát cẩn thận cấu trúc NaCl cho thấy rằng các ion nằm trên các mặt phằng rời rạc (phần được bôi đen trên hình 38.22). Bây giờ giả sử rằng chùm tia X tới hợp thành một góc θ với một trong các mặt phẳng được chỉ ra trên hình 38.23. Chùm tia có thể được phản xạ từ cả mặt phẳng trên và mặt phẳng dưới nhưng chùm tia phản xạ từ mặt phẳng dưới di chuyển xa hơn chùm tia phản xạ từ mặt phẳng trên. Sự khác nhau của quãng đường hiệu dụng là 2dsin  . Hai chùm tia giao thoa tăng cường nhau khi sự khác nhau của quãng đường bằng với số nguyên lần bước sóng . Kết quả giống như vậy vẫn đúng khi ánh sáng phản xạ từ một tập hợp toàn bộ các mặt

Cáu trúc tinh thé NaC1. Chièu dài canh hinh làp phuong là $\mathrm { a } = 0 , 5 6 6 2 7 3 7 \mathrm { n m }$

![](images/image20.jpg)  
Hình 38.22: Cấu trúc lập thể của NaCl.

phẳng song song. Vì vậy, điều kiện để có giao thoa tăng cường (cực đại trên chùm tia phản xạ) là

$$
2 \mathrm { d s i n } \Theta = \mathrm { m } \lambda , \mathsf { v } \dot { \mathsf { o } } \mathsf { i } \mathsf { m } = 1 , 2 , 3 \ldots
$$

Điều kiện này còn gọi là định luật Bragg, được đặt theo tên W. L. Bragg (1890−1971), người đầu tiên rút ra được mối liên hệ này. Nếu bước sóng và góc nhiễu xạ được đo, phương trình (38.8) có th $\acute { \hat { \mathbf { e } } }$ được sử dụng để tính khoảng các giữa các mặt phẳng nguyên tử.

![](images/image21.jpg)



Hình 38.23: Một chùm tia X tới chịu sự nhiễu xạ bởi cấu trúc trong tinh thể.



## Sự phân cực của sóng ánh sáng

### Ánh sáng không phân cực

Trong chương 34, chúng ta đã miêu tả tính chất theo phương ngang của ánh sáng và tất cả các sóng điện từ. Sự phân cực, được thảo luận trong phần này, là bằng chứng cho tính chất ngang của sóng ánh sáng.

Một chùm ánh sáng bình thường chứa đựng một số lượng lớn các sóng được phát ra bởi các nguyên tử của nguồn sáng. Mỗi nguyên tử tạo ra một sóng có hướng cụ thể của vector điện trường E , tương ứng với hướng của sự dao động nguyên tử. Hướng của sự phân cực của mỗi sóng riêng lẻ được định nghĩa là hướng mà theo đó điện trường đang dao động. Trong hình

![](images/image22.jpg)  
Hình 38.24: Sự phân cực của sóng ánh sáng.

38.24, hướng này nằm dọc theo trục y. Tất cả các sóng điện từ riêng lẻ chuyển động dọc theo phương x có vector song song với mặt phẳng yz, nhưng vector này có thể hợp thành một góc bất kỳ so với trục y. Bởi vì sự dao động xảy ra theo tất cả các hướng, vì vậy sóng điện từ sau cùng là chồng chập của sóng dao động từ nhiều hướng. Kết quả là một chùm sáng không phân cực, được chỉ ra trên hình 38.25a. Hướng lan truyền của sóng trong hình này vuông góc với mặt phẳng của trang giấy. Các mũi tên cho thấy một số hướng của vector điện trường của các sóng riêng lẻ tạo thành sóng tổng hợp. Tại một điểm bất kỳ và trong một thời gian ngắn, tất cả các vector điện trường riêng lẻ này sẽ tổng hợp lại để tạo thành vector điện trường tổng.

Dáu chám màu do bièu thi vector vàn tóc có chièu di ra khói mǎt giáy.

![](images/image23.jpg)

Hình 38.25: (a) Ánh sáng không phân cực được biểu diễn theo hướng truyền. Điện trường ngang dao động theo mọi hướng có xác suất bằng nhau, (b) Một chùm ánh sáng phân cực ban đầu với điện trường dao động theo phương thẳng đứng.





Như được chú ý trong mục 34.3, một sóng được xem là phân cực tuyến tính nếu như vector điện trường được tao thành dao động theo cùng hướng tại một điểm bất kỳ tại mọi lúc như được chỉ ra trên hình 38.25b. (Ngoài ra, vector này còn được miêu tả như bị phân cực phẳng hoặc đơn giản chỉ là bị phân cực). Mặt phẳng được tạo thành bởi và hướng lan truyền được gọi là mặt phẳng lan truyền của sóng. Nếu sóng trong hình 38.24 đại diện cho sóng được tạo thành từ tất cả các sóng đơn, mặt phẳng phân cực là mặt phẳng xy.

Một chùm tia phân cực tuyến tính có thể đạt được từ một chùm tia không phân cực bằng việc bỏ đi tất cả các sóng từ chùm tia ngoại trừ các sóng có vector điện trường dao động trong một mặt phẳng đơn. Bây giờ, chúng ta sẽ thảo luận bốn quá trình được sử dụng để tạo ra ánh sáng phân cực từ ánh sáng không phân cực.

### Sự phân cực bằng sự hấp thụ có chọn lọc

Kỹ thuật thông thường nhất dùng để tạo ra ánh sáng phân cực là sử dụng một vật liệu có tính truyền sóng. Điện trường của sóng truyền qua này dao động trong một mặt phẳng song song với một hướng xác định. Bên cạnh đó, vật liệu được sử dụng này sẽ hấp thụ sóng có điện trường dao động theo các hướng khác.

Năm 1938, E. H. Land (1909−1991) đã phát hiện một loại vật liệu mà sau đó ông ấy gọi là Polaroid. Vật liệu này phân cực ánh sáng thông qua sự hấp thụ có chọn lọc. Vật liệu này được chế tạo thành các tấm hydrocarbon chuỗi dài và mỏng. Các tấm này được kéo căng trong suốt quá trình sản xuất để các phân tử chuỗi dài được căng chỉnh thẳng hàng. Sau khi nhúng các tấm hydrocarbon này vào dung dịch chứa iốt, các phân tử trở thành các vật dẫn điện tốt. Sự dẫn điện xảy ra chủ yếu dọc theo các chuỗi hydrocarbon bởi vì các electron có thể di chuyển một cách dễ dàng dọc theo các chuỗi. Nếu ánh sáng có vector điện trường song song với các chuỗi chiếu vào vật liệu, điện trường gia tốc các electron dọc theo các chuỗi và năng lương được hấp thụ từ bức xạ. Vì vậy, ánh sáng không truyền qua vật liệu. Ánh sáng có vector điện trường vuông góc với các chuỗi truyền qua vật liệu bởi vì các electron không thể di chuyển từ phân tử này tới phân tử khác. Vì vậy, khi ánh sáng không phân cực chiếu vào vật liệu, ánh sáng thoát ra bị phân cực vuông góc với các chuỗi phân tử.

Thông thường hướng vuông góc với các chuỗi phân tử được xem như là trục truyền qua. Trong một kính phân cực lý tưởng, tất cả ánh sáng với song song với trục truyền qua thì được truyền qua và tất cả ánh sáng với vuông góc với trục truyền qua thì bị hấp thụ.



![](images/image24.jpg)  
Hình 38.26: Phân cực ánh sáng bằng phương pháp hấp thụ chọn lọc.

Hình 38.26 thể hiện một chùm ánh sáng không phân cực chiếu vào một tấm phân cực đầu tiên, gọi là kính phân cực. Bởi vì trục truyền qua được định hướng theo phương thẳng đứng trong hình, ánh sáng truyền qua tấm phân cực này sẽ bị phân cực thoe phương thẳng đứng. Tấm phân cực thứ hai, được gọi là thiết bị phân tích, chắn chùm tia. Trong hình 38.26, trục truyền qua của thiết bị phân tích được đặt tại một góc θ so với trục phân cực. Vector điện trường của chùm tia truyền qua đầu tiên là $\overrightarrow { \mathrm { E } } _ { 0 }$ . Thành phần $\overrightarrow { \mathrm { E } } _ { 0 }$ vuông góc với trục phân tích sẽ bị hấp thụ hoàn toàn. Thành phần $\overrightarrow { \mathrm { E } } _ { 0 }$ song song với trục phân tích, truyền qua thiết bị phân tích, là $\mathrm { E } _ { 0 }$ cos. Bởi vì cường độ của chùm tia truyền qua thay đổi như là bình phương của biên độ nên có thể kết luận rằng cường độ I của chùm tia phân cực truyền qua thiết bị phân tích thay đổi như sau,

$$
\mathrm { I } = \mathrm { I } _ { \mathrm { m a x } } \cos ^ { 2 } \theta
$$

ở đây, $\mathrm { { I } } _ { \operatorname* { m a x } }$ là cường độ của chùm tia phân cực chiếu vào thiết bị phân tích. Công thức này, được biết đến là quy luật Malus, áp dụng đối với hai vật liệu phân cực bất kỳ có các trục truyền qua hợp với nhau thành một góc θ. Công thức này cho thấy rằng cường độ của chùm tia truyền qua đạt cực đại khi các trục truyền qua song song $\mathsf { \Omega } \cdot \mathsf { \Omega } \Theta = 0 \mathsf { h o } \mathsf { A E c } 1 8 0 ^ { \mathrm { 0 } } \mathrm { \Omega } ,$ và bằng không (hấp thụ hoàn toàn bởi thiết bị phân tích) khi các trục truyền qua vuông góc với nhau. Sự thay đổi trong cường độ truyền qua này thông qua một cặp các tấm phân cực được minh hoạ trong hình 38.27. Bởi vì giá trị trung bình của $\cos ^ { 2 } \theta = 1 / 2$ , cường độ của ánh sáng không phân cực ban đầu bị giảm bởi một hệ số của 1/2 khi ánh sáng truyền qua một kính phân cực lý tưởng.



Ánh sáng truyèn qua có cròng dò crc dai khi các truc lan truyèn tháng hàng vói nhau.

Anh sáng truyèn qua có cròng dò yéu hon khi các truc lan truyèn nàm mòt góc $4 5 ^ { \circ }$ vói nhau.

Curòng dò ánh sáng truyèn qua dat crc tiéu khi các truc lan truyèn vuòng góc vói nhau.

![](images/image25.jpg)

Hình 38.27: Cường độ ánh sáng truyền qua hai bản phân cực phụ thuộc vào tính định hướng tương đối của các trục lan truyền. Mũi tên màu đỏ biểu thị trục truyền của các bản phân cực.

### Sự phân cực bằng sự phản xạ

Khi một chùm ánh sáng không phân cực bị phản xạ từ một bề mặt, sự phân cực của ánh sáng phản xạ phụ thuộc vào góc tới. Nếu góc tới là $0 ^ { 0 }$ thì chùm tia phản xạ không phân cực. Đối với các góc tới khác ánh sáng phản xạ sẽ bị phân cực đến một mức độ nào đó, và đối với một góc tới cụ thể, ánh sáng phản xạ sẽ bị phân cực hoàn toàn. Chúng ta hãy khảo sát sự phản xạ tại góc đặc biệt đó.

Giả sử một chùm sáng không phân cực chiếu vào một bề mặt như minh hoạ trong hình 38.28a. Mỗi vector điện trường có thể được phân tích thành hai thành phần: một song song với bề mặt (và vuông góc với trang giấy như trong hình 38.28, được thể hiện bởi các chấm) và phần còn lại (được minh hoạ bởi các mũi tên màu cam) vuông góc với cả thành phần đầu tiên và với hướng lan truyền sóng. Vì vậy, sự phân cực của toàn bộ chùm tia có thể được diễn tả bởi hai thành phần điện trường theo các hướng này. Thành phần song song được minh hoạ bởi các chấm, phản xạ mạnh hơn nhiều so với thành phần còn lại được thể hiện bởi các dấu mũi tên, tạo ra một chùm tia phản xạ phân cực không hoàn toàn. Hơn nữa, chùm tia khúc xạ cũng bị phân cực không hoàn toàn.

Bây giờ giả sử rằng góc tới $\theta _ { 1 }$ thay đổi đến khi góc giữa chùm tia phản xạ và chùm tia khúc xạ là $9 0 ^ { 0 }$ như được minh hoạ trên hình 38.28b. Tại góc tới này, chùm tia phản xạ bị phân cực hoàn toàn (với vector điện trường song song với bề mặt) và chùm tia khúc xạ vẫn bị phân cực không hoàn toàn. Góc tới tại đó sự phân cực này xảy ra được gọi là góc phân cực $\theta _ { \mathrm { p } }$ .



Các chám biéu thi sur dao dòng dién trròng song song vói bè mǎt phàn xa và vuòng góc vói mǎt phǎng tòi giáy.

Các müi tèn bièu diēn dao dòng dièn trròng vuòng góc vói nhing diém dáu chám.

Các electron tai bè māt dao dòng theo hróng cia tia phàn xa (vuòng góc vói các dáu chám và song song vói müi tèn màu xanh drong) khòng truyèn nǎng lrong

![](images/image26.jpg)  
Hình 38.28: (a) Phân cực một phần, (b) Phân cực toàn phần.

# Tóm tắt chương 38

Nhiễu xạ là độ lệch hướng của ánh sáng từ một đường thẳng khi ánh sáng đi qua một khẩu độ hoặc xung quanh một chướng ngại vật. Nhiễu xạ là do bản chất sóng tự nhiên của ánh sáng.

Mô hình nhiễu xạ Fraunhofer được tạo ra bởi một khe có chiều rộng là a và đặt cách màn một khoảng không đổi, cường độ sáng của các cực đại và cực tiểu rất nhỏ hơn so với cường độ sáng của cực đại chính giữa. Các góc $\theta _ { { \ t } \widetilde { \alpha } | }$ mà tại đó hình ảnh nhiễu xạ có cường độ bằng không, tương ứng với cực tiểu nhiễu xạ, được xác định bởi:

$$
\sin \theta _ { _ { \mathsf { t o i } } } = \mathrm { m } \underset { _ { \mathsf { \Omega } } } { \overset { \lambda } { \longrightarrow } } , \mathsf { v o i } \mathsf { m } = \pm 1 , \pm 2 , \pm 3 \_
$$

Tiêu chuẩn Rayleigh, điều kiện giới hạn về độ phân giải, cho biết hai ảnh được tạo thành bởi một khẩu độ chỉ có thể phân biệt được nếu cực đại trung tâm của ảnh nhiễu xạ này rơi đúng vào cực tiểu thứ nhất của ảnh nhiễu xạ kia. Góc giới hạn của độ phân giải tối thiểu qua khe có độ rộng a là:

$$
\Theta _ { \mathrm { m i n } } = \frac { \lambda } { \lambda }
$$

Góc giới hạn của độ phân giải cho khẩu độ tròn là:



$$
\Theta _ { \mathrm { m i n } } = 1 , 2 2 \frac { { \lambda } } { \mathrm { D } }
$$

với D là đường kính của khẩu độ.

Cách tử nhiễu xạ, bao gồm một hệ thống gồm N khe hẹp giống hệt nhau với độ rộng của mỗi khe là a, khoảng cách giữa hai khe liền kề là d, được đặt cách đều nhau với khoảng cách giữa hai khe liên tiếp là $\mathcal { l }$ (chu kỳ của cách tử). Cách tử có cấu tạo rất tinh vi, trên mỗi milimet chiều dài có đến hàng trăm khe. Điều kiện để đạt cường độ cực đại trong ảnh giao thoa qua cách tử nhiễu xạ là:

$$
\mathrm { d } \sin \theta _ { \mathsf { s a n g } } = \mathrm { m } \lambda , \mathsf { v } \dot { \mathsf { o i } } \mathrm { m } = 0 , \pm 1 , \pm 2 , \pm 3 \ldots
$$

Khi ánh sáng bị phân cực có cường độ cực đại $\operatorname { I } _ { \operatorname* { m a x } }$ được phát ra bởi bộ phân cực và sau đó đến bộ phân tích, ánh sáng truyền qua bộ phân tích có cường độ $\mathrm { ~ I ~ } _ { \operatorname* { m a x } } \cos ^ { 2 } { \theta }$ , trong đó  là góc giữa trục phân cực và trục truyền phân tích.

Nhìn chung, ánh sáng phản xạ bị phân cực một phần. Tuy nhiên, ánh sáng phản xạ bị phân cực hoàn toàn khi góc tới tới (góc hợp bởi chùm tia khúc xạ và phản xạ) là $9 0 ^ { 0 }$ . Góc tới này được gọi là góc phân cực $\theta _ { p }$ khi nó thỏa mãn quy luật Brewster:

$$
\tan \Theta _ { \mathrm { _ p } } = \frac { \mathtt { n } _ { 2 } } { \mathtt { n } _ { 1 } }
$$

trong đó, $\mathbf { n } _ { 1 }$ là chiếc suất khúc xạ của môi trường ánh sáng tới, ${ \bf n } _ { 2 }$ là chiết suất khúc xạ của môi trường phản xạ.

### TASK QA
num_correct,answers
1,A
1,B
1,A
1,C
1,C
1,B
1,B
1,A
1,A
1,A
1,C
1,C
1,C
1,C
1,B
1,A
1,C
1,B
1,D
1,D
1,B
1,C
1,C
1,B
1,A
1,A
1,B
1,A
1,C
1,A
1,C
1,D
1,B
1,A
1,C
1,C
1,A
1,A
1,C
1,C
1,C
1,B
1,D
1,C
1,D
1,A
1,B
1,A
1,B
1,C
1,C
1,C
1,C
1,D
1,C
1,C
1,C
1,C
1,C
1,B
1,A
1,C
1,C
1,A
1,A
1,C
1,B
1,A
1,B
1,B
1,C
1,A
1,C
1,D
1,C
1,C
1,C
1,C
1,C
1,B
1,A
1,C
1,B
1,A
1,A
1,C
1,C
1,B
1,B
1,A
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,B
1,B
1,C
1,C
1,C
1,B
1,B
1,B
1,B
1,C
1,A
1,B
1,C
1,A
1,C
1,C
1,B
1,A
1,A
1,A
1,C
1,C
1,A
1,B
1,C
1,B
1,C
1,B
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,B
1,C
1,C
1,C
1,D
1,B
1,A
1,C
1,C
1,B
1,B
1,C
1,B
1,C
1,C
1,C
1,D
1,C
1,A
1,C
1,B
1,A
1,B
1,C
1,B
1,C
1,A
1,A
1,C
1,C
1,B
1,B
1,C
1,D
1,C
1,C
1,C
1,C
1,B
1,C
1,B
1,B
1,A
1,C
1,B
1,C
1,A
1,C
1,B
1,C
1,B
1,C
1,D
1,C
1,D
1,C
1,C
1,A
1,A
1,A
1,D
1,B
1,D
1,C
1,A
1,C
1,A
1,C
1,C
1,A
1,B
1,B
1,C
1,A
1,D
1,C
1,C
1,A
1,C
1,B
1,C
1,B
1,C
1,C
1,B
1,B
1,C
1,A
1,C
1,C
1,C
1,C
1,C
1,C
1,C
1,A
1,C
1,C
1,B
1,C
1,C
1,B
1,B
1,C
1,A
1,D
1,B
1,C
1,C
1,C
1,B
1,C
1,C
1,C
1,B
