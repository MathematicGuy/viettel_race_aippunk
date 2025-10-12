

# 1. Điện trở (Resistor)

# 1.1 Điện trở là gì? (What is a Resistor)

Điện trở (Resistor) là linh kiện điện tử thụ động tạo ra trở kháng (resistance), làm cản trở dòng chảy của các electron trong mạch điện.

Chúng được gọi là phần tử thụ động (passive) vì chỉ tiêu thụ năng lượng (consume power) mà không tạo ra năng lượng.

Điện trở thường được sử dụng trong các mạch như OP-AMP, vi điều khiển (microcontrollers) và các mạch tích hợp khác (IC – integrated circuits). Chúng dùng để hạn dòng (limit current), chia điện áp (divide voltages) và điều khiển các đường I/O (pull-up/pull-down lines).

# 1.2 Đơn vị điện trở (Resistor Units)

Đơn vị đo điện trở là Ohm ${ \bf ( \Omega _ { 0 } ) }$ , ký hiệu bằng chữ Hy Lạp Omega $( \Omega )$ . Ohm đặt theo tên nhà vật lý Georg Simon Ohm (1784–1854), người đã nghiên cứu và phát hiện mối quan hệ giữa điện áp, dòng điện và điện trở (Luật Ohm).

Trong hệ SI, các tiền tố được dùng để biểu thị điện trở lớn hoặc nhỏ: kilo $( \mathrm { k } \Omega )$ , mega (MΩ), giga (GΩ) hoặc mili $( \mathbf { m } \Omega )$ .

# Ví dụ:

• $4 . 7 0 0 \Omega = 4 . 7 \mathrm { k } \Omega$ 5.600.000 Ω = 5.6 MΩ hoặc 5,600 kΩ

Tên các điện trở trong mạch thường bắt đầu bằng chữ R, mỗi điện trở có một số duy nhất.

# 1.3 Ký hiệu điện trở trong sơ đồ mạch (Resistor Schematic Symbol)

Tất cả các điện trở có hai đầu nối. Trên sơ đồ mạch, điện trở được biểu thị theo hai tiêu chuẩn:

Hình chữ nhật: theo tiêu chuẩn IEC (International Electrotechnical Commission) Đường ngoằn ngoèo (zigzag): theo tiêu chuẩn IEEE (Institute of Electrical and Electronics Engineers)



Cả hai ký hiệu đều chấp nhận được. Hình chữ nhật thường được ưu tiên; dạng zigzag phổ biến ở Mỹ và châu $\mathrm { \AA }$ . Số đỉnh zigzag tiêu chuẩn là 7, với 4 đỉnh trên và 3 đỉnh dưới.

# 1.4 Thành phần điện trở (Resistor Composition)

Điện trở được chế tạo từ nhiều loại vật liệu, phổ biến là màng carbon, kim loại hoặc oxit kim loại. Một lớp vật liệu dẫn điện mỏng được quấn quanh và bao phủ bởi lớp cách điện.

• Màng dày: rẻ nhưng ít chính xác Màng mỏng: đắt hơn nhưng chính xác cao

Ví dụ giá trị điện trở:

• 27 Ω, 330 Ω, 3.3 MΩ

Bên trong, màng carbon quấn quanh lõi cách điện. Nhiều lớp bọc điện trở cao hơn.

# 1.5 Ý nghĩa điện trở trong mạch điện (Resistor in Circuit)

Điện trở có thể thay thế nhiều thiết bị điện như bóng đèn hoặc động cơ. Trong mạch điện đốt nóng (electric heater circuit), sợi dây đốt nóng được xem như điện trở.

Định luật Ohm:

$$
\scriptstyle \mathrm { R = V I R } = \mathrm { V / I }
$$

# Ví dụ:

Tổng điện trở bình thường: RT $\scriptstyle \mathtt { \tilde { = } } 6 0$ ΩR_T $" = 6 0 "$ \,\Omega $( 2 4 0 \div 4 = 6 0 \Omega )$ (d) Khi dòng điện giảm còn 3 A, điện trở tăng: $\mathrm { R T } = 2 4 0 \div 3 = 8 0 \Omega \mathrm { R \_ T } = 2 4 0 \div 3 =$ 80\,\Omega báo hiệu mạch có vấn đề.

# 1.6 Giá trị điện trở của dây dẫn (Resistance of Conductor)

Bốn yếu tố ảnh hưởng điện trở dây dẫn:

# 1.6.1 Vật liệu (Material)

o Dây dẫn tốt: đồng, bạc, nhôm o Cách điện: cao su, thủy tinh, sứ



# Chiều dài (L)

o Dây càng dài, điện trở càng cao. o Ví dụ: dây $2 \textrm { m } {  }$ điện trở gấp đôi dây 1 m

# Diện tích mặt cắt ngang (A)

o Mặt cắt $\mathrm { l o n } $ điện trở giảm. o Ví dụ: diện tích tăng gấp đôi điện trở giảm phân nửa

# Nhiệt độ (T)

o Nhiệt độ tăng điện trở tăng.   
o Khó dự đoán so với các yếu tố khác.

Công thức tính điện trở dây dẫn:

R=ρLAR

Trong đó:

RR: điện trở (Ω) • ρ\rho: điện trở suất của vật liệu $\left( \Omega \cdot \mathrm { m } \right)$ LL: chiều dài dây (m) • AA: diện tích mặt cắt ngang $( \mathbf { m } ^ { 2 } )$ )

# 1.7 Mạch điện trở mắc nối tiếp (Resistor Series Circuits)

Trong mạch nối tiếp, các điện trở được kết nối từ đầu đến cuối, tạo thành một đường dẫn duy nhất cho dòng điện.

Tổng điện trở mạch nối tiếp:

Ví dụ 1: 3 điện trở nối tiếp

${ \mathrm { R } } 1 = 2 \Omega , { \mathrm { R } } 2 = 4 \Omega , { \mathrm { R } } 3 = 6 \Omega { \mathrm { R } } _ { - } 1 = 2 \backslash , \cup \mathrm { O m e g a } , { \mathrm { R } } _ { - } 2 = 4 \backslash , \cup \mathrm { O m e g a } , { \mathrm { R } } _ { - } 3 = 6 \backslash , \cup \mathrm { O m e g a } , { \mathrm { R } } _ { - } 1 = 1 \backslash \mathrm { O m e g a } , { \mathrm { R } } _ { - } 1 = 1 \backslash \mathrm { O m e g a } , { \mathrm { R } } _ { - } 1 = 1 \backslash \mathrm { O m e g a } .$ ega Dòng điện $\mathrm { I } { = } 4 \mathrm { A I } = 4 \backslash , \mathrm { A }$ Tổng điện trở: ${ \mathrm { R T } } { = } 2 { + } 4 { + } 6 { = } 1 2 \ { \Omega } { \mathrm { R } } \ \mathrm { T } = 2 + 4 + 6 { = } 1 2 { \backslash } { \mathrm { , ( O m e } }$ ga Điện áp nguồn: $\mathrm { E { = } I { \cdot } R T { = } } 4 { \times } 1 2 { = } 4 8 \mathrm { V E } = \mathrm { I } \backslash \mathrm { c } \mathrm { d o t } \mathrm { R } \_ \mathrm { T } = 4$ \times $1 2 = 4 8 \backslash , \mathrm { V }$



Ví dụ 2: 3 điện trở nối tiếp với điện áp nguồn $\mathrm { E } { = } 9 \mathrm { V E } = 9 \backslash , \mathrm { V }$

• $\mathrm { R 1 } = 3 \mathrm { k } \Omega , \mathrm { R 2 } = 1 0 \mathrm { k } \Omega , \mathrm { R 3 } = 5 \mathrm { k } \Omega \mathrm { R \Omega } _ { - } 1 = 3 \backslash \mathrm { , k } \cup \mathrm { m e g a , \mathrm { R \Omega } 2 } = 1 0 \backslash \mathrm { , k } \cup \mathrm { m e g a , \mathrm { R \Omega } \cup \mathrm { k } \Omega } _ { - } $ $\mathrm { ~ R ~ } _ { - } 3 =$ 5\,k\Omega   
• Dòng điện trong mạch:

Sau đó, điện áp rơi trên mỗi điện trở:

$\mathrm { V R 1 } = \mathrm { I } { \cdot } \mathrm { R 1 } = 0 . 5 { \times } 3 { = } 1 . 5 \mathrm { V V } _ { - } \{ \mathrm { R 1 } \} = \mathrm { I } \mathrm { R } _ { - } 1 = 0 . 5 \mathrm { ~ x } 3 = 1 . 5 \backslash , \mathrm { V }$ $\mathrm { V R } 2 \mathrm { = } \mathrm { I } { \cdot } \mathrm { R } 2 \mathrm { = } 0 . 5 { \times } 1 0 { = } 5 \mathrm { V V } \_ { } \{  \mathrm { R } 2 \} = \mathrm { I } \mathrm { ~ R } \_ { } 2 = 0 . 5 \mathrm { ~ x ~ } 1 0 = 5 { \cdot } \mathrm { V }$ $\mathrm { V R 3 } = \mathrm { I } \cdot \mathrm { R 3 } = 0 . 5 \times 5 = 2 . 5 \mathrm { V V } \_ \mathrm { \& } \mathrm { \& } = \mathrm { I } \mathrm { R } \_ 3 = 0 . 5 \mathrm { \times } 5 = 2 . 5 \backslash \mathrm { , V }$

Tôi sẽ viết thêm một đoạn mở rộng về mạch điện trở song song (parallel resistor circuits) để nối tiếp tài liệu hiện tại:

# 1.8 Mạch điện trở mắc song song (Resistor Parallel Circuits)

Trong mạch điện song song, các điện trở được kết nối sao cho cả hai đầu của chúng được nối trực tiếp vào cùng hai điểm, tạo ra nhiều đường dẫn cho dòng điện chảy. Điện áp trên mỗi điện trở trong mạch song song luôn bằng nhau, nhưng dòng điện phân chia theo giá trị điện trở của từng nhánh.

# Ví dụ:

Ba điện trở mắc song song: $\mathrm { R 1 } { = } 6 \Omega \mathrm { R \_ } 1 = 6$ , ${ \mathrm { R } } 2 { = } 3 \ { \Omega } { \mathrm { R } } \ { \underline { { \ 2 } } } = 3$ , ${ \mathrm { R } } 3 { \mathrm { = } } 2 { \mathrm { ~ } } \Omega { \mathrm { R } } \_ 3 { \mathrm { = } } 2 .$ . Tổng điện trở: 1

Dòng điện tổng từ nguồn được chia theo tỉ lệ nghịch với điện trở từng nhánh:

Điều này giúp mạch giảm tổng điện trở so với bất kỳ điện trở riêng lẻ nào và tăng khả năng phân phối dòng điện cho các thiết bị nối vào nhánh khác nhau. Mạch song song phổ biến trong hệ thống chiếu sáng, mạch nguồn và điện gia dụng, nơi các tải cần hoạt động độc lập nhưng cùng điện áp.

# Ưu điểm của mạch song song:

• Nếu một nhánh hỏng, các nhánh khác vẫn hoạt động.   
• Dễ dàng điều chỉnh dòng điện cho từng nhánh bằng cách chọn điện trở phù hợp.

# Nhược điểm:

Cần tính toán tổng điện trở cẩn thận, đặc biệt khi nhiều nhánh nối song song, để tránh dòng quá tải