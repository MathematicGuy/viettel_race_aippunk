

Nội dung chính của chương trình bày một số lược đồ thuật toán kinh điển dùng để giải lớp các bài toán liệt kê, bài toán đếm, và bài toán tối ưu và bài toán tồn tại. Mỗi lược đồ thuật toán giải quyết một lớp các bài toán thỏa mãn một số tính chất nào đó. Đây là những lược đồ thuật toán quan trọng nhằm giúp người học vận dụng nó trong khi giải quyết các vấn đề trong tin học. Các lược đồ thuật toán được trình bày trong chương này bao gồm: thuật toán sinh, thuật toán đệ qui, thuật toán quay lui, thuật toán tham lam, thuật toán nhánh cận, thuật toán qui hoạch động.

# 1. Mô hình thuật toán sinh (Generative Algorithm)

Mô hình thuật toán sinh được dùng để giải lớp các bài toán liệt kê, bài toán đếm, bài toán tối ưu, bài toán tồn tại thỏa mãn hai điều kiện:

• Điều kiện 1: Có thể xác định được một thứ tự trên tập các cấu hình cần liệt kê của bài toán. Biết cấu hình đầu tiên, biết cấu hình cuối cùng. Điều kiện 2: Từ một cấu hình chưa phải cuối cùng, ta xây dựng được thuật toán sinh ra cấu hình đứng ngay sau nó.

Mô hình thuật toán sinh được biểu diễn thành hai bước: bước khởi tạo và bước lặp. Tại bước khởi tạo, cấu hình đầu tiên của bài toán sẽ được thiết lập. Điều này bao giờ cũng thực hiện được theo giả thiết của bài toán. Tại bước lặp, quá trình lặp được thực hiện khi gặp phải cấu hình cuối cùng. Điều kiện lặp của bài toán bao giờ cũng tồn tại theo giả thiết của bài toán. Hai chỉ thị cần thực hiện trong thân vòng lặp là đưa ra cấu hình hiện tại và sinh ra cấu hình kế tiếp. Mô hình sinh kế tiếp được thực hiện tùy thuộc vào mỗi bài toán cụ thể. Tổng quát, mô hình thuật toán sinh được thể hiện như dưới đây.

Thuật toán Generation; begin

Bước1 (Khởi tạo): <Thiết lập cấu hình đầu tiên>;

# Bước 2 (Bước lặp):

while (<Lặp khi cấu hình chưa phải cuối cùng>) do <Đưa ra cấu hình hiện tại>; <Sinh ra cấu hình kế tiếp>;



# End.

Ví dụ 2.1. Vector $X = ( x _ { 1 } , x _ { 2 } , . . , x _ { \mathrm { { n } } } ) .$ , trong đó $x _ { \mathrm { i } } = 0$ , 1 được gọi là một xâu nhị phân có độ dài n. Hãy liệt $\mathrm { k } \hat { \mathrm { e } }$ các xâu nhị phân có độ dài n. Ví dụ với $\mathrm { \tt n } { = } 4$ , ta sẽ liệt $\mathrm { k } \hat { \mathrm { e } }$ được 24 xâu nhị phân độ dài 4 như trong Bảng 2.1.

Bảng 2.1. Các xâu nhị phân độ dài 4   



dưới đây. Trong đó, thuật toán sinh xâu nhị phân kế tiếp từ một xâu là hàm Next_Bits_String().

#include <iostream>   
#include <iomanip>   
#define MAX 100   
using namespace std;   
int X[MAX], n, dem $=$   
0; //sử dụng các biến   
toàn cục X[], n, OK,   
dem bool OK $=$ true;   
void Init(void){ //khởi   
tạo xâu nhị phân đầu   
tiên cout<<"Nhập $\mathfrak { n } ^ { = " }$ ; $\mathrm { c i n } { > } { > } \mathrm { n }$ ; for(int $\dot { 1 } = 1$ ; $\mathrm { i } < = \mathrm { n }$ ; $\mathrm { i } { + } { + }$ ) //thiết lập xâu với n số 0 $\mathrm { { X } [ i ] = 0 ; }$   
} void Result(void){ //đưa ra xâu nhị phân hiện   
tại cout<<"\n Xâu thứ "<<++dem<<":"; for(int $\mathrm { i } { = } 1$ ; $\mathrm { i } < = \mathrm { n }$ ; i++) cout<<X[i]<<setw(3);   
} void Next_Bits_String(void){ //thuật toán sinh xâu nhị phân kế   
tiếp int $\mathsf { i } { = } \mathsf { n }$ ; while $\mathrm { i } { > } 0$ && X[i]){ //duyệt từ vị trí bên phải nhất $\mathrm { { X } [ i ] = 0 }$ ; //nếu gặp $X [ i ] = I$ ta chuyển thành 0 i--; //lùi lại vị trí sau } if $( \mathrm { i } \mathrm { > } 0 )$ ) $\mathrm { X } [ \mathrm { i } ] { = } 1$ ; //gặp X[i] $= 0$ đầu tiên ta chuyển thành 1   
else $\mathrm { O K } =$ false; //kết thúc khi gặp xâu có n số 1   
}   
int main(void){ //đây là thuật toán sinh Init(); //thiết   
lập cấu hình đầu tiên le(OK){//lặp khi chưa Result(); //đưa ra cấu   
phải cấu hình cuối cùng   
hình hiện tại Next_Bits_String(); //sinh ra cấu hình kế tiếp



Ví dụ 2.2. Liệt $\mathrm { k } \hat { \mathrm { e } }$ các tập con $\mathrm { k }$ phần tử của 1, 2, .., n.

Lời giải. Mỗi tập con k phần tử của 1, 2, .., N là một tổ hợp chập $\mathrm { K }$ của 1, 2,.., N. Ví dụ với $\mathrm { n } { = } 5$ , ${ \mathrm { k } } = 3$ ta sẽ có $\mathrm { C } ( \mathrm { n } , \mathrm { k } )$ tập con trong Bảng 2.2.

Điều kiện 1. Ta gọi tập con $X { = } ( x 1 , { \ldots } x \mathrm { { K } } )$ là đứng trước tập con $\mathrm { Y } = \left( { { y 1 , y 2 , . . . , \gamma \mathrm { K } } } \right)$ nếu tìm được chỉ số t sao cho $x _ { 1 } = y _ { 1 } , x _ { 2 } = y _ { 2 } , . . , x _ { \mathrm { t - l } } = y _ { \mathrm { t - l } } , x _ { \mathrm { t } } < y _ { \mathrm { t - } } .$ Ví dụ tập con $X = ( l , 2 , 3 )$ đứng trước tập con $Y = ( \textit { I } , 2 , 4 )$ vì ta tìm được $\mathrm { t } { = } 3$ thỏa mãn $x _ { 1 } = y _ { 1 } , x _ { 2 } = y _ { 2 } , x _ { 3 } < y _ { 3 }$ . Tập con đầu tiên là $X = ( 1 , 2 , . . , k )$ , tập con cuối cùng là $( n { - } k { + } I , . . , N )$ . Như vậy điều kiện 1 của thuật toán sinh được thỏa mãn.

Điều kiện 2. Để ý rằng, tập con cuối cùng $( \mathrm { n - k + l } , . . . , \mathrm { n } )$ luôn thỏa mãn đẳng thức ${ \bf X } [ \mathrm { i } ] = { \bf n } - { \bf k } + \mathrm { i }$ . Ví dụ tập con cuối cùng $\mathrm { X } [ ] = ( 3 , 4 , 5 )$ ta đều có: $\mathrm { X } [ 1 ] = 3 = 5 - 3 + 1 ;$ ; $\mathrm { X } [ 2 ] = 4 = 5 - 3 + 2 ; \mathrm { X } [ 3 ] = 5 = 5 - 3 + 3 .$ . Để tìm tập con $\mathrm { k } \acute { \mathrm { e } }$ tiếp từ tập con bất kỳ ta chỉ cần duyệt từ phải qua trái tập con $\mathbf { X } [ ] = ( \mathbf { x } 1 , \mathbf { x } 2 , . . , \mathbf { x } \mathbf { k } )$ để xác định chỉ số i thỏa mãn điều kiện X[i] $\mathbf { n } - \mathbf { k } + \mathbf { i }$ . Ví dụ với $\mathrm { X } [ ] = ( 1 , 4 , 5 )$ , ta xác định được $\mathrm { i } { = } 1$ vì $X [ 3 ] = 5 = 5 - 3 + 3$ , $X [ 2 ] = 4 = 5  – 3 + 2$ , và $\mathrm { X } [ 1 ] = \ 1 \ \ 5 { - } 3 { + } 1$ . Sau khi xác định được chỉ số i, tập con mới sẽ được sinh là $\mathrm { Y } [ ] = ( \mathrm { y } 1 , . . , \mathrm { y i } , . . . , \mathrm { y k } )$ ra thỏa mãn điều kiện: $\mathbf { y } 1 = \mathbf { x } 1$ , ${ \bf y } 2 = { \bf x } 2 , \ldots$ , yi- $\mathbf { \partial } \cdot 1 = \mathbf { \ v { x i - 1 } }$ , $\mathbf { y } \mathbf { i } = \mathbf { x } \mathbf { i } + 1$ , và yj $= \mathrm { \mathbf { x } } \mathbf { t } + \mathbf { j } - \mathrm { i } \mathrm { \mathbf { v } } \dot { \mathrm { c } }$ i $\displaystyle ( \mathrm { j } = \mathrm { j } { + } 1 , . . . , \mathrm { k } )$ .

Bảng 2.2. Tập con 3 phần tử của 1, 2, 3, 4, 5   



Trong đó, thuật toán sinh tổ hợp kế tiếp có tên là Next_Combination().

#include <iostream> #include <iomanip> #define MAX 100 int X[MAX], n, k, dem $_ { \mathrm { 1 = 0 } }$ ; bool $\mathrm { O K } =$ true; using namespace std;

void Result(void){ //đưa ra tập con hiện tại cout<<"\n Kết quả "<<++dem<<":"; for(int $\mathrm { i } { = } 1$ ; $\mathrm { i } { < } \mathrm { = } \mathrm { k }$ ; $\mathrm { i } { + } { + }$ ) //đưa ra $X [ ] = ( x _ { 1 } , x _ { 2 } , . . , x _ { \mathrm { k } } )$ cout<<X[i]<<setw(3);   
}   
void Next_Combination(void){ //sinh tập con k phần tử từ tập con bất kỳ int $\dot { \mathbf { \eta } } _ { 1 } = \mathbf { k }$ ; //duyệt từ vị trí bên phải nhất của tập con while $\mathrm { i } { > } 0$ && $\mathrm { X } [ \mathrm { i } ] { = } { = } { \bf n } { - } { \bf k } { + } \mathrm { i }$ ) //tìm i sao cho $x _ { i }$ $n { - } k { + } i$ i--; if $( \mathrm { i } { > } 0 ) \{ / / n \hat { e } u$ chưa phải là tập con cuối cùng $\mathrm { X [ i ] { = } X [ i ] { + } 1 }$ ; //thay đổi giá trị tại vị trí i: $x _ { i } = x _ { i } + 1$ ; for(int j=i+1; j<=k; j++) //các vị trí j từ $i + l , . . , k$ X[j] = X[i] + j - i; // được thay đổi là $x _ { j } = x _ { i } + j - i ,$ ; } else //nếu là tập con cuối cùng OK $=$ false; //ta kết thúc duyệt   
int main(void){   
Init(); //khởi tạo cấu hình đầu tiên



while(OK){ //lặp trong khi cấu hình chưa phải cuối cùng Result(); //đưa ra cấu hình hiện tại Next_Combination(); //sinh ra cấu hình kế tiếp } }

Ví dụ 2.3. Liệt kê các hoán vị của $1 , 2 , . . , \mathtt { n }$ .

Lời giải. Mỗi hoán vị của 1, 2, .., $_ \mathrm { N }$ là một cách xếp có tính đến thứ tự của 1, 2,..,N. Số các hoán vị là N!. Ví dụ với $\mathrm { N } = 3$ ta có 6 hoán vị dưới đây.

Bảng 2.3. Hoán vị của 1, 2, 3.   



# 2. Mô hình thuật toán đệ qui (Recursion Algorithm)

Một đối tượng được định nghĩa trực tiếp hoặc gián tiếp thông qua chính nó được gọi là phép định nghĩa bằng đệ qui. Thuật toán giải bài toán $P$ một cách trực tiếp hoặc gián tiếp thông qua bài toán $P ^ { \bullet }$ giống như $P$ được gọi là thuật toán đệ qui giải bài toán $P$ . Một hàm được gọi là đệ qui nếu nó được gọi trực tiếp hoặc gián tiếp đến chính nó.



Tổng quát, một bài toán có thể giải được bằng đệ qui nếu nó thỏa mãn hai điều kiện:

Phân tích được: Có thể giải được bài toán P bằng bài toán P’ giống như P. Bài tóa P’ và chỉ khác P ở dữ liệu đầu vào. Việc giải bài toán P’ cũng được thực hiện theo cách phân tích giống như $P$ .   
Điều kiện dừng: Dãy các bài toán $P$ ’ giống như $P$ là hữu hạn và sẽ dừng tại một bài toán xác định nào đó.

Thuật toán đệ qui tổng quát có thể được mô tả như sau:

Thuật toán Recursion ( P ) {

1. Nếu $P$ thỏa mãn điều kiện dừng: <Giải P với điều kiện dừng>;

2. Nếu $P$ không thỏa mãn điều kiện dừng: <Giải P’ giống như P:Recursion $( P ^ { \prime } ) { > }$ ;

Ví dụ 2.4. Tìm tổng của n số tự nhiên đầu tiên bằng phương pháp đệ qui. Lời giải. Gọi $\mathrm { S n }$ là tổng của n số tự nhiên. Khi đó:

Bước phân tích: dễ dàng phận thấy tổng n số tự nhiên $\mathrm { S } _ { \mathrm { n } } = \mathrm { n } + \mathrm { S } _ { \mathrm { n } - 1 }$ , với n 1. • Điều kiện dừng: $\mathrm { S } _ { 0 } = 0 \mathrm { n } \acute { \hat { \mathrm { e } } u } \mathrm { n } = 0$ ;

Từ đó ta có lời giải của bài toán như sau:

int Tong (int n ) { if $( { \bf n } = = 0$ ) return(0); //Điều kiện dừng else return(n + Tong(n-1)); //Điều kiện phân tích được   
}

Chẳng hạn ta cần tìm tổng của 5 số tự nhiên đầu tiên, khi đó:

$$
\begin{array} { r l } & { \mathrm { S } = \mathrm { T o n g } ( 5 ) } \\ & { \qquad \quad \supset _ { - } ^ { \bigcirc } \bar { 5 } + \mathrm { T o n g } ( 4 ) } \\ & { \qquad = 5 + 4 + \mathrm { T o n g } ( 3 ) } \\ & { \qquad = 5 + 4 + 3 + \mathrm { T o n g } ( 2 ) } \\ & { \qquad = 5 + 4 + 3 + 2 + \mathrm { T o n g } ( 1 ) } \\ & { \qquad = 5 + 4 + 3 + 2 + 1 + \mathrm { T o n g } ( 0 ) } \end{array}
$$



$$
\begin{array} { l } { = 5 + 4 + 3 + 2 + 1 + 0 } \\ { = 1 5 } \end{array}
$$

Ví dụ 2.5. Tìm n!.

Lời giải. Gọi Sn là n!. Khi đó:

Bước phân tích: $\mathrm { S n } = \mathbf { n } ^ { * } ( \mathbf { n } { - } 1 ) !$ nếu $\mathrm { n } { > } 0$ ; Điều kiện dừng: $\mathsf { s } 0 \mathrm { = } 1$ nếu $\mathrm { \ n { = } 0 }$ . Từ đó ta có lời giải của bài toán như sau: long Giaithua (int n ) { if $( { \bf n } = = 0$ ) return(1); //Điều kiện dừng else return(n \*Giaithua(n-1)); //Điều kiện phân tích được } Ví dụ 2.6. Tìm ước số chung lớn nhất của a và b bằng phương pháp đệ qui.

Lời giải. Gọi $\mathbf { d } = \mathbf { U S C L N } ( \mathbf { a } , \mathbf { b }$ ). Khi đó:

Bước phân tích: nếu b 0 thì $\mathrm { d } = \mathrm { U S C L N ( a , b ) } = \mathrm { U S C L N ( b , r ) }$ , trong đó a =b, $\mathbf { b } = \mathbf { r } = \mathbf { a }$ mod b . Điều kiện dừng: nếu $\boldsymbol { \mathrm { b } } = \boldsymbol { 0 }$ thì a là ước số chung lớn nhất của a và b. Từ đó ta có lời giải của bài toán như sau: int USCLN (int a, int b ) { if $( \mathbf { a = } \mathbf { = } \mathbf { b }$ ) return(a); //Điều kiện dừng else { //Điều kiện phân tích được int $\mathbf { r } = \mathbf { a } \ \%$ b; $\mathtt { a } = \mathtt { b }$ ; $\mathbf { b } = \mathbf { r } ;$ ; return(USCLN(a, b)); //giải bài toán USCLN(a, b) } }