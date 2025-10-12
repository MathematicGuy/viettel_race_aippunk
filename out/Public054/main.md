

# 1. Thuật toán Bubble Sort

Thuật toán sắp xếp kiểu sủi bọt được thực hiện đơn giản bằng cách tráo đổi hai phần từ liền kề nhau nếu chúng chưa được sắp xếp. Thuật toán được mô tả chi tiết trong Hình 3.3.

# 1.1 Biểu diễn thuật toán

Thuàt toán Bubble-Sort:   
Input: · Day cac aói tuong (các só) : Arr[0], Arr[1],.,Arr[n-1]. · Só luong các doi tuong càn sap xép: n.   
Output: · Day các aói turong da duoc sáp xép (các só) : Arr[0], Arr[1].,Arr[n-1].   
Formats: Insertion-Sort(Arr, n);   
Actions: for $( \mathsf { i } = 0 ; \mathsf { i } < \mathsf { n } ; \mathsf { i } + + ) \{ / / | \check { \mathsf { a } } { p } \mathsf { \ } i = 0 , \mathrm { ~ } \mathrm { } \mathrm { } \mathrm { } \mathrm { } , \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { . } \mathrm { } \mathrm { } \mathrm { } \mathrm { } \mathrm { ~ }$ for $( \mathrm { j } = 0$ ; j<n-i-1; j++ ) {/ǎρj =0, 1,.., n-i-1 iff $( \mathsf { A r r } [ \mathsf { j } ] > \mathsf { A r r } [ \mathsf { j } + 1 ]$ ) { lnéu Arrjij>Arr[ji+1] thi doi chō temp $\underline { { \underline { { \mathbf { \delta \pi } } } } }$ Arr[j; $\mathsf { A r r } [ \mathsf { j } ] = \mathsf { A r r } [ \mathsf { j } + 1 ] ;$ $\textstyle \mathsf { A r r } [ \ j + 1 ] =$ temp; } } }   
End.

# 1.2 Độ phức tạp thuật toán

Độ phức tạp thuật toán là $\mathrm { O } ( \mathrm { N } ^ { 2 } )$ , với $_ \mathrm { N }$ là số lượng phần tử. Bạn đọc tự tìm hiểu phương pháp ước lượng và chứng minh độ phức tạp thuật toán Bubble Sort trong các tài liệu liên quan.

# 1.3 Kiểm nghiệm thuật toán



Kièm nghièm thuàt toán: $\mathsf { A r r } [ ] = \{ \ : 9 , 7 , 1 2 , 8 , 6 , 5 \ : \} , \mathsf { n } = 6 .$



int $\mathbf { n } =$ sizeof(arr)/sizeof(arr[0]); bubbleSort(arr, n); printArray(arr, n); }

# 2. Thuật toán Quick Sort

Thuật toán sắp xếp Quick-Sort được thực hiện theo mô hình chia để trị (Divide and Conquer). Thuật toán được thực hiện xung quanh một phần tử gọi là chốt (key). Mỗi cách lựa chọn vị trí phần tử chốt trong dãy sẽ cho ta một phiên bản khác nhau của thuật toán. Các phiên bản (version) của thuật toán Quicksort bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ :

• Luôn lựa chọn phần tử đầu tiên trong dãy làm chốt.   
• Luôn lựa chọn phần tử cuối cùng trong dãy làm chốt.   
• Luôn lựa chọn phần tử $\dot { \mathbf { O } }$ giữa dãy làm chốt. Lựa chọn phần tử ngẫu nhiên trong dãy làm chốt.

Mấu chốt của thuật toán Quick-Sort là làm thế nào ta xây dựng được một thủ tục phân đoạn (Partition). Thủ tục Partition có hai nhiệm vụ chính:

Định vị chính xác vị trí của chốt trong dãy nếu được sắp xếp; Chia dãy ban đầu thành hai dãy con: dãy con ở phía trước phần tử chốt bao gồm các phần tử nhỏ hơn hoặc bằng chốt, dãy ở phía sau chốt có giá trị lớn hơn chốt.

Thuật toán Partition được mô tả chi tiết trong Hình 3.4 với khóa chốt là phần tử cuối cùng của dãy. Phiên bản Quick Sort tương ứng được mô tả chi tiết trong Hình 3.5.



# 2.1 Biểu diễn thuật toán

Thuat toán Partition:

• Day Arrl] bát dàu tai vi trí I và két thúc tai h. · Càn duói cúa day con: I   
· Càn trèn cúa day con: h

# Output:

· Vi trí chinh xác cúa Arr[h] néu dãy Arr] duroc sáp xép.

Formats: Partition(Arr 1, h);

Actions: $\mathsf { x } = \mathsf { A r r } [ \mathsf { h } ]$ ;  II chon x la chót c a day Arr[,Arr[+1],., Arr[h] $\mathrm { i } = ( \mathrm { I } - 1 )$ ;lli là chi só cúa các phàn tú nhǒ hon chót x. for $( \ j = 1 ; \ j < = { \mathsf { h } } . \ 1 ; \ j + + ) \ ,$ {llduyet các chi sój=1, 1+1, …., h-1. if (Arr[i] $\scriptstyle < = x$ ){ linéu Arrli] nhó hon hoǎc bàng chót x. $\mathrm { i } { + } { + }$ ; litǎng vi trí các phàn tú nhó hon chót swap(&Arr[ij, &Arril); II doi chō Arr[i] cho Arr[ij. } } swap(&Arr[i + 1], &Arr[h]); II döi chō Arr[i+1] cho Arr[h]. return $( \mathfrak { i } + \mathbb { 1 } )$ ; /l/vitri $i + 1$ chinh là vi trí chót néu dāy duroc sáp xép   
End.

Hình 3.4. Thuật toán Partition với chốt là vị trí cuối cùng của dãy

Thuàt toán Quick-Sort:

Input:

• Day Arrl gòm n phàn tú. • Càn duói cua dāy: I. · Càn trèn cǔa dǎy : h

Output: · Day Arr] duoc sáp xép.

Formats: Quick-Sort(Arr, 1, h);

Actions: if( l<h) { ll Néu càn durói còn nho hon càn trèn p $=$ Partition(Arr, I, h); //thyc hien Partition() chót h. Quick-Sort(Arr, I, p-1); //thuc hien Quick-Sort núra ben trái. Quick-Sort(Arr, $\mathsf { p } { + } \mathsf { 1 }$ , h);//thuc hien Quick-Sort núra bēn phai }   
End.

# 2.2 Độ phức tạp thuật toán

Độ phức tạp thuật toán trong trường hợp xấu nhất là $\mathrm { O } ( \mathrm { N } ^ { 2 } )$ , trong trường hợp tốt nhất là



$\mathrm { O ( N . L o g ( N ) ) }$ , với $_ \mathrm { N }$ là số lượng phần tử. Bạn đọc tự tìm hiểu và chứng minh độ phức tạp thuật toán Quick Sort trong các tài liệu liên quan.

# 2.3 Kiểm nghiệm thuật toán

Kièm nghiem thuat toán Quick-Sort: Quick-Sort(Arr, 0, 9); Arr[ $=$ {10, 27, 15, 29, 21, 11, 14, 18, 12, 17}; Càn durói $_ { | = 0 }$ ,càn trèn ${ \mathfrak { h } } = { \mathfrak { g } }$



return $( \mathrm { i } + 1 )$ ; //đây là vị trí của chốt } void quickSort(int arr[], int l, int h){ if $( \mathrm { l } < \mathrm { h } ) \{$ { int ${ \mathfrak { p } } ^ { = }$ partition(arr, l, h); // tìm vị trí của chốt quickSort(arr, l, p - 1);//trị nửa bên trái quickSort(arr, $\mathfrak { p } + 1 , \mathrm { h }$ );//trị nửa bên phải } } void printArray(int arr[], int size){ //thủ tục in kết quả int i; cout<<"\n Dãy được sắp:"; for $( \mathrm { i } { = } 0 ; \mathrm { i } < \mathrm { s i z e } ; \mathrm { i } { + } + )$ cout<<arr[i]<<setw(3); } int main(){ //chương trình chính int $\mathrm { a r r [ ] } = \{ 1 0 , 2 7 , 1 5 , 2 9 , 2 1 , 1 1 , 1 4 , 1 8 , 1 2 , 1 7 \} \mathrm { . }$ ; int $\mathbf { n } =$ sizeof(arr)/sizeof(arr[0]); quickSort(arr, 0, n-1); printArray(arr, n); }

# 3. Thuật toán Merge Sort

Giống như Quick-Sort, Merge-Sort cũng được xây dựng theo mô hình chia để trị (Divide and Conquer). Thuật toán chia dãy cần sắp xếp thành hai nửa. Sau đó gọi đệ qui lại cho mỗi nửa và hợp nhất lại các đoạn đã được sắp xếp. Thuật toán được tiến hành theo 4 bước dưới đây:

Tìm điểm giữa của dãy và chia dãy thành hai nửa.   
Thực hiện Merge-Sort cho nửa thứ nhất.   
• Thực hiện Merge-Sort cho nửa thứ hai. Hợp nhất hai đoạn đã được sắp xếp.



![](images/image1.jpg)

Mấu chốt của thuật toán Merge-Sort là làm thế nào ta xây dựng được một thủ tục hợp nhất (Merge). Thủ tục Merge thực hiện hòa nhập hai dãy đã được sắp xếp để tạo thành một dãy cũng được sắp xếp. Bài toán có thể được phát biểu như sau:

Bài toán hợp nhất Merge: Cho hai nửa của một dãy $\mathrm { A r r } [ 1 , . . . , \mathrm { m } ]$ và $\mathrm { A } [ \mathrm { m } { + } 1 , . . . , \mathrm { r } ]$ đã được sắp xếp. Nhiệm vụ của ta là hợp nhất hai nửa của dãy Arr[1,..,m] và $\mathrm { A r r } [ \mathrm { m + 1 , . . , r } ]$ để trở thành một dãy Arr[1, 2,..,r] cũng được sắp xếp.

Thuật toán Merge được mô tả chi tiết trong Hình 3.6. Thuật toán Merge Sort được mô tả chi tiết trong Hình 3.7.

Biểu diễn thuật toán:

Hình 3.6. Thuật toán hợp nhất hai đoạn đã được sắp xếp.   



![](images/image2.jpg)

![](images/image3.jpg)  
Hình 3.7. Thuật toán Merge Sort

# 3.1 Độ phức tạp thuật toán

Độ phức tạp thuật toán là O(N.Log(N)) với N là số lượng phần tử. Bạn đọc tự tìm hiểu và chứng minh độ phức tạp thuật toán Merge Sort trong các tài liệu liên quan.



# 3.2 Kiểm nghiệm thuật toán

Kièm nghièm thuàt toán Merge-Sort: Merge-Sort(Arr,0,7) Input :Arr[] $=$ {38, 27, 43, 3, 9, 82, 10}; ${ \mathsf { n } } = 7$



$\operatorname { a r r } [ \mathbf { k } ] = \mathbf { R } [ \mathrm { j } ] ;$ ; j++; k++; } } void mergeSort(int arr[], int l, int r){ //thuật toán Merge Sort if $( 1 < { \bf r } ) \{$ //nếu cận dưới còn bé hơn cận trên int $\mathbf { m } = 1 + ( \mathbf { r } { - } 1 ) / 2$ ; //tìm vị trí $\acute { \sigma }$ giữa đoạn l, r mergeSort(arr, l, m); //trị nửa thứ nhất mergeSort(arr, $\mathrm { m } { + } 1$ , r); //trị nửa thứ hai merge(arr, l, m, r); //hợp nhất hai đoạn đã được sắp } } void printArray(int $\mathrm { A r r } [ ]$ , int size){ //in kết quả int i;cout $\leq < " \ln$ Dãy được sắp:"; for $( \mathrm { i } { = } 0 ; \mathrm { i } < \mathrm { s i z e } ; \mathrm { i } { + } + )$ cout<<Arr[i]<<setw(3); } int main(){ int $\mathrm { a r r } [ ] = \{ 3 8 , 2 7 , 4 3 , 3 , 9 , 8 2 , 1 0 \}$ ; int arr_size $=$ sizeof(arr)/sizeof(arr[0]); mergeSort(arr, 0, arr_size - 1); printArray(arr, arr_size); }

# 4. Thuật toán Heap Sort

Thuật toán Heap-Sort được thực hiện dựa trên cấu trúc dữ liệu Heap. Nếu ta muốn sắp xếp theo thứ tự tăng dần ta sử dụng cấu trúc Max Heap, ngược lại ta sử dụng cấu trúc Min-Heap. Vì Heap là một cây nhị phân đầy đủ nên việc biểu diễn Heap một cách hiệu quả có thể thực hiện được bằng mảng. Nếu ta xem xét phần tử thứ i trong mảng thì phần tử $2 ^ { * } \mathrm { i } + 1$ , $2 ^ { * } \mathrm { i } + 2$ tương ứng là node con trái và node con phải của i.

Tư tưởng của Heap Sort giống như Selection Sort, chọn phần tử lớn nhất trong dãy đặt vào vị trí cuối cùng, sau đó lặp lại quá trình này cho các phần tử còn lại. Tuy nhiên, điểm khác biệt ở đây là phần tử lớn nhất của Heap luôn là phần tử đầu tiên trên Heap và các phần tử node trái và phải bao giờ cũng nhỏ hơn nội dung node gốc.

Thuật toán được thực hiện thông qua ba bước chính như sau:



Xây dựng Max Heap từ dữ liệu vào. Ví dụ với dãy $\mathrm { A } [ ] = \{ 9 , 7 , 1 2 , 8 , 6 , 5 \}$ thì Max Heap được xây dựng là $A [ ] = \{ 1 2 , 8 , 9 , 7 , 6 , 5 \}$ .

● Bắt đầu tại vị trí đầu tiên là phần tử lớn nhất của dãy. Thay thế, phần tử này cho phần tử cuối cùng ta nhận được dãy $\mathrm { A } [ ] = \{ 5 , 8 , 9 , 7 , 6 , 1 2 \}$ .