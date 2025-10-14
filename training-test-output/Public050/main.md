

# 1. Khái niệm độ phức tạp thuật toán

Thời gian thực hiện một giải thuật bằng chương trình máy tính phụ thuộc vào các yếu tố:

Kích thước dữ liệu đầu vào: một giải thuật hay một chương trình máy tính thực hiện trên tập dữ liệu có kích thước lớn hiển nhiên mất nhiều thời gian hơn thuật toán hoặc chương trình này thực hiện trên tập dữ liệu đầu vào có kích thước nhỏ. Phần cứng của hệ thống máy tính: hệ thống máy tính có tốc độ cao thực hiện nhanh hơn trên hệ thống máy tính có tốc độ thấp.

Tuy nhiên, nếu ta quan niệm thời gian thực hiện của một thuật toán là số các phép toán sơ cấp thực hiện trong thuật toán đó thì phần cứng máy tính không còn là yếu tố ảnh hưởng đến quá trình xác định thời gian thực hiện của một thuật toán. Với quan niệm này, độ phức tạp thời gian thực hiện của một thuật toán chỉ còn phụ thuộc duy nhất vào độ dài dữ liệu đầu vào.

Gọi độ dài dữ liệu đầu vào là $T ( n )$ . Khi đó, số lượng các phép toán sơ cấp để giải bài toán $P$ thực hiện theo thuật toán $F { = } F _ { 1 } F _ { 2 } { \ldots } F _ { \mathrm { n } }$ trên độ dài dữ liệu $T ( n )$ là $F ( T ( n ) )$ . Để xác định số lượng các phép toán sơ cấp $F \mathrm { i } ( i { = } I , 2 , . . , n )$ thực hiện trong thuật toán $F$ ta cần phải giải bài toán đếm để xác định $F ( T ( n ) )$ . Đây là bài toán vô cùng khó và không phải lúc nào cũng giải được []. Để đơn giản điều này, người ta thường tìm đến các phương pháp xấp xỉ để tính toán độ phức tạp thời gian của một thuật toán. Điều này có nghĩa, khi ta không thể xây dựng được công thức $\mathrm { d } \hat { \mathsf { e m } } F ( T ( n ) )$ , nhưng ta lại có khẳng định chắc chắn $F ( T ( n ) )$ không vượt quá một phiếm hàm biết trước $G ( n )$ thì ta nói $F ( T ( n ) )$ thực hiện nhanh nhất là $G ( n )$ .

Tổng quát, cho hai hàm $f ( x ) _ { ; }$ , $g ( x )$ xác định trên tập các số nguyên dương hoặc tập các số thực. Hàm $f ( x )$ được gọi là $O ( g ( x ) )$ nếu tồn tại một hằng số $C { > } 0$ và n0 sao cho:

$$
| f ( x ) | \leq C . | g ( x ) | { \mathrm { ~ v { \dot { \sigma } } i ~ m o i ~ } } x { \geq } n _ { 0 } .
$$

Điều này có nghĩa với các giá trị $x \ \geq n _ { 0 } \ \mathrm { { h a m } } \ f ( x )$ bị chặn trên bởi hằng số $C$ nhân với $g ( x ) . { \mathrm { N } } { \hat { \mathbf { e } } } { \mathrm { u } } f ( x )$ là thời gian thực hiện của một thuật toán thì ta nói giải thuật đó có cấp $g ( x )$ hay độ phức tạp thuật toán $f ( x )$ là $O ( g ( x ) )$ .

Ghi chú. Các hằng số $C _ { i }$ , n0 thỏa mãn điều kiện trên là không duy nhất. Nếu có đồng thời $f ( x )$ là $O ( g ( x ) )$ và $h ( x )$ thỏa mãn $g ( x ) < h ( x )$ với $x { > } n _ { 0 }$ thì ta cũng có $f ( x )$ là $O ( h ( n ) )$ .

Ví dụ 1.6. Cho $f ( x ) = a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 }$ ; trong đó, $a _ { \mathrm { i } }$ là các số thực $( \mathrm { i } = 0 , 1 , 2 , . . , \mathrm { n } )$ . Khi đó $f ( x ) = O ( x ^ { \mathrm { n } } )$ .

Chứng minh. Thực vậy, với mọi $x { > } I$ ta có:



$$
\begin{array} { r l } & { | f ( x ) = | a _ { n } x ^ { n } + a _ { n - 1 } x ^ { n - 1 } + \cdots + a _ { 1 } x + a _ { 0 } | } \\ & { \qquad \leq | a _ { n } | x ^ { n } + | a _ { n - 1 } | x ^ { n - 1 } + \cdots + | a _ { 1 } | x + | a _ { 0 } | } \\ & { \qquad \leq | a _ { n } | x ^ { n } + | a _ { n - 1 } | x ^ { n } + \cdots + | a _ { 1 } | x ^ { n } + | a _ { 0 } | x ^ { n } } \\ & { \qquad \leq x ^ { n } ( | a _ { n } | + | a _ { n - 1 } | + \cdots + | a _ { 1 } | + | a _ { 0 } | ) } \\ & { \qquad \leq C . x ^ { n } = O ( x ^ { n } ) . \mathrm { T r o n g } \mathrm { d } { \delta } , C = \left( | a _ { n } | + | a _ { n - 1 } | \right. . } \end{array}
$$

# 2. Một số quy tắc xác định độ phức tạp thuật toán

Như đã đề cập ở trên, bản chất của việc xác định độ phức tạp thuật toán là giải bài toán đếm số lượng các phép toán sơ cấp thực hiện trong thuật toán đó. Do vậy, tất cả các phương pháp giải bài toán đếm thông thường đều được áp dụng trong khi xác định độ phức tạp thuật toán. Hai nguyên lý cơ bản để giải bài toán đếm là nguyên lý cộng và nguyên lý nhân cũng được mở rộng trong khi ước lượng độ phức tạp thuật toán.

Nguyên tắc tổng: Nếu f1 $( x )$ có độ phức tạp là $\mathrm { O } ( g _ { 1 } ( x ) )$ và f2 $( x )$ có độ phức tạp là $\mathrm { O } ( g _ { 2 } ( x ) )$ thì độ phức tạp của $( f _ { 1 } ( x ) + { \mathrm { f } } _ { 2 } ( x )$ là $\operatorname { O } ( M a x ( g _ { 1 } ( x ) , g _ { 2 } ( x ) )$ .

Chứng minh. $\operatorname { V i } f _ { 1 } ( x )$ có độ phức tạp là $\mathrm { O } ( g _ { 1 } ( x )$ nên tồn tại hằng số $C _ { 1 }$ và $k _ { 1 }$ sao cho $\vert f _ { 1 } ( x ) \vert { \cdot } \vert g _ { 1 } ( x ) \vert$ với mọi $x \cdot k _ { 1 }$ . Vì $f _ { 2 } ( x )$ có độ phức tạp là $\mathrm { O } ( g _ { 2 } ( x ) )$ nên tồn tại hằng số $C _ { 2 }$ và $k _ { 2 }$ sao cho $\vert f _ { 2 } ( x ) \vert { \cdot } \vert g _ { 2 } ( x ) \vert$ với mọi $x \cdot k _ { 2 }$ .

Ta lại có :

$$
\begin{array} { r l } { \vert f _ { 1 } ( x ) + f _ { 2 } ( x ) \vert } & { \cdot \vert f _ { 1 } ( x ) \vert + \vert f _ { 2 } ( x ) \vert } \\ & { \cdot C _ { 1 } \vert g _ { 1 } ( x ) \vert + C _ { 2 } \vert g _ { 2 } ( x ) \vert } \\ & { \cdot C \vert g ( x ) \vert \operatorname { v \dot { o i } } \operatorname { m o i } x > k ; } \end{array}
$$

Trong đó, $C = C _ { 1 } + C _ { 2 } ; g ( x ) = m a x ( \ g _ { 1 } ( x ) , g _ { 2 } ( x ) ) ; k = m a x ( { k _ { 1 } , k _ { 2 } } ) .$

Tổng quát. Nếu độ phức tạp của $f _ { 1 } ( x ) , f _ { 2 } ( x ) , . . . , f _ { \mathrm { m } } ( x )$ lần lượt là $\mathrm { O } ( g _ { 1 } ( x ) )$ , ${ \mathrm { O } } ( g _ { 2 } ( x ) ) , . . .$ , $O ( g _ { \mathrm { n } } ( x ) )$ thì độ phức tạp của $f _ { 1 } ( x ) + f _ { 2 } ( x ) + . . . + f _ { \mathrm { m } } ( x )$ là $\mathrm { O } ( m a x ( g _ { 1 } ( x ) , g _ { 2 } ( x ) , . . , g _ { \mathrm { m } } ( x ) )$ .

Nguyên tắc nhân: $\operatorname { N e u } f ( x )$ có độ phức tạp là $\mathrm { O } ( g ( x )$ thì độ phức tạp của $f ^ { \mathfrak { n } } ( x )$ là $\mathrm { O } ( g ^ { \mathrm { n } } ( x ) )$ . Trong đó:

$$
\begin{array} { l c l } { { f ^ { \mathrm { n } } ( x ) } } & { { = } } & { { f ( x ) { . } f ( x ) { . } . . . f ( x ) { . } \mathrm { \quad } / \mathrm { / / n } \mathrm { \quad } \mathrm { l } \mathrm { \dot { a } n } \mathrm { \quad } f ( x ) { . } } } \\ { { } } & { { } } & { { } } \\ { { g ^ { \mathrm { n } } ( x ) = g ( x ) { . } g ( x ) { . } . . g ( x ) { . } / / n \mathrm { \ l } \mathrm { \dot { a } n } g ( x ) } } \end{array}
$$



Chứng minh. Thật vậy theo giả thiết $f ( x )$ là $\mathbf { O } ( g ( x ) )$ nên tồn tại hằng số $C$ và $k$ sao cho với mọi $x { > } k$ thì $| f ( x ) | { \cdot } \mathbf { C } { \cdot } | g ( x )$ . Ta có:

$$
\begin{array} { l } { | f ^ { n } ( x ) | = | f ^ { 1 } ( x ) . f ^ { 2 } ( x ) \dots f ^ { n } ( x ) | } \\ { \qquad \le | C . g ^ { 1 } ( x ) . C . g ^ { 2 } ( x ) \dots C . g ^ { n } ( x ) | } \\ { \qquad \le | C ^ { n } . g ^ { n } ( x ) | = O ( g ^ { n } ( x ) ) } \end{array}
$$

# 3. Một số dạng hàm được dùng xác định độ phức tạp thuật toán

Như đã đề cập ở trên, để xác định chính xác độ phức tạp thuật toán $\operatorname { f } ( \mathbf { x } )$ là bài toán khó nên ta thường xấp xỉ độ phức tạp thuật toán với một phiếm hàm $\mathbf { O } ( \mathbf { g } ( \mathbf { x } ) )$ . Dưới đây là một số phiếm hàm của $\mathrm { O } ( \mathrm { g } ( \mathrm { x } ) )$ .

Bảng 1.1. Các dạng hàm xác định độ phức tạp thuật toán   



Dưới đây là một số qui tắc xác định $\mathrm { O } ( \mathrm { g } ( \mathrm { x } ) )$ :

• Nếu một thuật toán có độ phức tạp hằng số thì thời gian thực hiện thuật toán đó không phụ thuộc vào độ dài dữ liệu. Một thuật toán có độ phức tạp logarit của $\operatorname { f } ( \mathrm { n } )$ thì ta viết $\mathrm { O } ( \log ( \mathfrak { n } ) )$ mà không cần chỉ rõ cơ số của phép logarit.   
• Với P(n) là một đa thức bậc k thì $\mathrm { O ( P ( n ) ) = O ( n ^ { k } ) }$ . Thuật toán có độ phức tạp đa thức hoặc nhỏ hơn được xem là những thuật toán thực tế có thể thực hiện được bằng máy tính. Các thuật toán có độ phức tạp hàm mũ, hàm giai thừa được xem là những thuật toán thực tế không giải được bằng máy tính.

# 4. Độ phức tạp của các cấu trúc lệnh

Để đánh giá độ phức tạp của một thuật toán đã được mã hóa thành chương trình máy tính ta thực hiện theo một số qui tắc sau.

Độ phức tạp hằng số O(1): đoạn chương trình không chứa vòng lặp hoặc lời gọi đệ qui có tham biến là một hằng số.

Ví dụ 1.7. Đoạn chương trình dưới đây có độ phức tạp hằng số.

for $( i { = } I ; i { < } = c ; i { + } + )$ { <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }

Độ phức tạp ${ \bf O } ( { \bf n } ) \colon { \bf D } \hat { \bf 0 }$ phức tạp của hàm hoặc đoạn code là O(n) nếu biến trong vòng lặp tăng hoặc giảm bởi mộ hằng số c.

Ví dụ 1.8. Đoạn code dưới đây có độ phức tạp hằng số.

for $( \mathrm { i } { = } 1 ; \mathrm { i } { < } { = } \mathrm { n } ; \mathrm { i } { = } \mathrm { i } + \mathrm { c } { \bf \Gamma } )$ { <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; } for $\mathrm { ( i { = } n ; i { > } 0 ; i = i - c \textnormal { ) } } \{$ <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }

Độ phức tạp đa thức ${ \bf O } ( { \bf n } ^ { \mathrm { c } } ) \colon { \bf D } \hat { \boldsymbol { 0 } }$ phức tạp của $c$ vòng lặp lồng nhau, mỗi vòng lặp đều có độ phức tạp O(n) là ${ \bf O } ( { \bf n } ^ { \mathrm { c } } )$ .

Ví dụ 1.9. Đoạn code dưới đây có độ phức tạp ${ \mathrm { O } } ( { \mathfrak { n } } ^ { 2 } )$ .



for $( \mathrm { i } \mathrm { - } 1$ ; $\mathrm { i } < = \mathrm { n }$ ; $\mathrm { ~ \bf ~ i ~ } = \mathrm { ~ \bf ~ i ~ } + \mathrm { ~ c ~ } )$ {   
for $( \mathrm { j = 1 } ; \mathrm { j < = n } ; \mathrm { j = j + c } ) \{$ { <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }   
}   
for $\mathrm { ( i = n ; ~ i ~ > 0 ~ ; ~ i ~ = ~ i ~ - ~ c ~ ) ~ } \left\{ \begin{array} { l l } \end{array} \right.$   
for $( \mathrm { j } = \mathrm { i } - 1 ; \mathrm { j } { > } 1 ; \mathrm { j } = \mathrm { j } - \mathrm { c } ) \{$ { <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }

Độ phức tạp logarit ${ \bf O } ( { \bf L o g ( n ) } ) \colon { \mathrm { D } } \hat { \bf { 0 } }$ phức tạp của vòng lặp là log(n) nếu biểu thức khởi đầu lại của vòng lặp được chia hoặc nhân với một hằng số c.

Ví dụ 1.10. Đoạn code dưới đây có độ phức tạp Log(n).   
for $( \mathrm { i } { = } 1 ; \mathrm { i } { < } { = } \mathrm { n } ; \mathrm { i } { = } \mathrm { i } { ^ { \ast } } \mathrm { c } ) \{$ { <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; $\begin{array} { l } { \left. \begin{array} { l } { \vdots } \\ { \operatorname { f o r } \mathrm { ( j = n ; j > 0 ~ ; j = j ~ / ~ c ~ ) } \{ } \end{array} \right\} } \end{array}$ <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }

Độ phức tạp hằng số O(Log (Log(n))): nếu biểu thức khởi đầu lại của vòng lặp được nhân hoặc chia cho một hàm mũ.

Ví dụ 1.11. Đoạn code dưới đây có độ phức tạp Log Log(n).   
for $( \mathrm { i } \mathrm { = } 1 ; \mathrm { j } \mathrm { < } \mathrm { = } \mathrm { n } ; \mathrm { j } ^ { \ast } \mathrm { = } \mathrm { P o w } ( \mathrm { i } , \mathrm { c } ) \ ) \left\{ \begin{array} { r l } \end{array} \right.$ <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; } for (j=n; j>=0; j = j- Function(j) ){ //Function(j) $= _ { \mathrm { \ell } }$ sqrt(j) hoặc lớn hơn 2. <Tập các chỉ thị có độ phức tạp ${ \cal O } ( l ) >$ ; }

Độ phức tạp của chương trình: độ phức tạp của một chương trình bằng số lần thực hiện một chỉ thị tích cực trong chương trình đó. Trong đó, một chỉ thị được gọi là tích cực trong chương trình nếu chỉ thị đó phụ thuộc vào độ dài dữ liệu và thực hiện không ít hơn bất kỳ một chỉ thị nào khác trong chương trình.

Ví dụ 1.12. Tìm độ phức tạp thuật toán sắp xếp kiểu Bubble-Sort?

Void Bubble-Sort ( int A[], int n ) { for $( \mathrm { i } { = } 1 ; \mathrm { i } { < } \mathrm { n } ; \mathrm { i } { + } { + } )$ { $\mathrm { f o r } \ : ( \mathrm { \ j = i + 1 ; j < = n ; j + + } ) \ : \{$ if $( \mathrm { A } [ \mathrm { i } ] > \mathrm { A } [ \mathrm { j } ] )$ {//đây chính là chỉ thị tích cực $\mathrm { { t = A [ i ] ; A [ i ] = A [ j ] ; A [ j ] = t ; } }$ } } } }



Lời giải. Sử dụng trực tiếp nguyên lý cộng ta có:

Với $\mathrm { i } = 1$ ta cần sử dụng n-1 phép so sánh A[i] với A[j]; Với $\dot { 1 } = 2$ ta cần sử dụng n-2 phép so sánh A[i] với A[j]; Với $\dot { \mathbf { 1 } } = \mathbf { n } - 1$ ta cần sử dụng 1 phép so sánh A[i] với A[j]; V tổng số các phép toán cần thực hiện là:

$$
\mathbf { S } = ( \mathbf { n } { - } 1 ) + ( \mathbf { n } { - } 2 ) + \ldots { } + 2 + 1 = \mathbf { n } ( \mathbf { n } { - } 1 ) / 2 \cdot \mathbf { n } ^ { 2 } = \mathbf { O } ( \mathbf { n } ^ { 2 } ) .
$$

Ghi chú. Độ phức tạp thuật toán cũng là số lần thực hiện phép toán tích cực. Phép toán tích cực là phép toán thực hiện nhiều nhất đối với thuật toán.

# 5. Quy trình giải quyết bài toán trên máy tính

Để giải quyết một bài toán hoặc vấn đề trong tin học ta thực hiện thông qua 6 bước như sau:

Bước 1. Xác định yêu cầu bài toán. Xem xét bài toán cần xử lý vấn đề gì? Giả thiết nào đã được biết trước và lời giải cần đạt những yêu cầu gì? Ví dụ thời gian, hay không gian nhớ.

Bước 2. Tìm cấu trúc dữ liệu thích hợp biểu diễn các đối tượng cần xử lý của bài toán. Cấu trúc dữ liệu phải biểu diễn đầy đủ các đối tượng thông tin vào của bài toán. Các thao tác trên cấu trúc dữ liệu phải phù hợp với những thao tác của thuật toán được lựa chọn. Cấu trúc dữ liệu phải cài đặt được bằng ngôn ngữ lập trình cụ thể đáp ứng yêu cầu bài toán.

Bước 3. Lựa chọn thuật toán. Thuật toán phải đáp ứng được yêu của bài toán và phù hợp với cấu trúc dữ liệu đã được lựa chọn Bước 1.

Bước 4. Cài đặt thuật toán. Thuật toán cần được cài đặt bằng một ngôn ngữ lập trình cụ thể. Ngôn ngữ lập trình sử dụng phải có các cấu trúc dữ liệu đã lựa chọn.

Bước 5. Kiểm thử chương trình. Thử nghiệm thuật toán (chương trình) trên các bộ dữ liệu thực. Các bộ dữ liệu cần phải bao phủ lên tất cả các trường hợp của thuật toán.

Bước 6. Tối ưu chương trình: Cải tiến để chương trình tốt hơn.

