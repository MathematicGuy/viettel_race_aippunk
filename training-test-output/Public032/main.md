

# 1. Dòng điện một chiều (Direct Current – DC)

# 1.1 Định nghĩa (Definition)

Dòng điện một chiều (DC) là dòng điện mà các electron chảy liên tục theo một hướng trong mạch kín. Loại điện áp tạo ra dòng điện này gọi là điện áp một chiều (DC voltage), và dòng điện gọi là dòng điện một chiều (DC current).

Các nguồn DC điển hình: Pin, ắc quy, máy phát DC.

# 1.2 Định luật Ohm (Ohm’s Law)

Có một mối quan hệ xác định giữa ba đặc tính điện cơ bản: dòng điện (I), điện áp (V), điện trở (R).

Định luật Ohm do nhà vật lý người Đức Georg Simon Ohm phát hiện vào thế kỷ 19:

Trong đó:

II: dòng điện (amps – A) VV: điện áp (volts – V) RR: điện trở (ohms – Ω)

# Giải thích:

Điện áp 1 V đặt vào điện trở $1 \Omega $ dòng điện 1 A chảy qua.   
Điện trở tăng dòng điện giảm (với cùng điện áp).

# Thiết bị Ohmic và Non-Ohmic:

Ohmic: Tuân theo luật Ohm (điện trở tuyến tính, ví dụ dây dẫn, điện trở thông thường).   
Non-Ohmic: Không tuân theo (ví dụ transistor, diode).

# 1.3 Ví dụ minh họa

Ví dụ 1: Biết $\mathrm { V } { = } 1 2 \mathrm { V } \mathrm { V } = 1 2 \mathrm { V } \mathrm { ~ , } \mathrm { R } { = } 6 \Omega \mathrm { R } = 6 \Omega$ . Tìm dòng điện II:



$\mathrm { I } { = } \mathrm { V R } { = } 2 \mathrm { A }$

Ví dụ thực tế: Pin $4 . 2 \mathrm { ~ V ~ }$ cấp cho tải $0 . 5 \Omega$ :

$\mathrm { I } { = } 8 . 4 \mathrm { A }$

Nếu pin còn $3 . 7 \mathrm { V }$ , dòng điện giảm:

$\mathrm { I } { = } 7 . 4 \mathrm { A }$

Ví dụ 2: Biết $\mathrm { V } { = } 2 4 \mathrm { V } \mathrm { V } = 2 4 \mathrm { \backslash , V , I } \mathrm { = } 6 \mathrm { A I } = 6 \mathrm { , A }$ . Tìm điện trở RR:

$$
R = V I = 2 4 6 = 4 \varOmega R \ = \ V / I \ = \ 2 4 / 6 \ = \ 4 \varOmega
$$

Ví dụ 3: Biết $\mathrm { I } { = } 5 \mathrm { A I } = 5 \backslash , \mathrm { A } , \mathrm { R } { = } 8 \Omega \mathrm { R } = 8 \backslash , \Omega$ . Tìm điện áp VV:

# 1.4 Công suất điện (Power Calculation)

Công suất (P) do dòng điện tạo ra trong điện trở tính theo:

$$
P _ { \cap \mathcal { C } } = V \cdot I = V 2 R = I 2 \cdot R P \ = \ V \cdot I \ = \frac { V ^ { 2 } } { R } = \ I ^ { 2 } \cdot R
$$

Ví dụ: Pin 4.2 V, điện trở $0 . 5 \Omega$ , dòng điện 8.4 A:

Như vậy, cuộn dây $0 . 5 ~ \Omega$ với pin sạc đầy $4 . 2 \mathrm { ~ V ~ }$ sẽ kéo 8.4 A và cung cấp 35.3 W. Khi điện trở tăng dòng điện giảm công suất giảm.

2. Dòng điện xoay chiều (Alternating Current – AC)

# 2.1 Định nghĩa (Definition)

Dòng điện xoay chiều (AC) là dòng điện mà các electron thay đổi hướng liên tục theo thời gian. Điện áp AC buộc electron chảy theo một hướng, sau đó theo hướng ngược lại, tuần hoàn liên tục.

Nguồn AC: Máy phát điện.   
Ứng dụng: Cung cấp điện cho hộ gia đình, nhà máy, văn phòng.



# 2.2 Dạng sóng (Waveform)

AC có nhiều dạng sóng khác nhau. Khi kết nối nguồn AC với dao động kế và vẽ điện áp theo thời gian, các dạng sóng phổ biến:

• Sóng sin: Dạng sóng chính dùng trong dân dụng và công nghiệp.   
• Sóng vuông và sóng tam giác: Thường dùng trong mạch điện tử và điều khiển.

# 2.3 Mô tả toán học của sóng sin AC

Sóng sin AC có th $\dot { \hat { \mathrm { ~ e ~ } } } \mathrm { m } \hat { \mathrm { ~ } }$ tả bằng hàm toán học:

$$
V ( t ) = V p s i n ( 2 \pi f t + \phi ) V ( t ) = \ V _ { p } \backslash s i n ( 2 \pi f t \ + \ \phi )
$$

Trong đó:

$\mathrm { V } ( \mathrm { t } ) \mathrm { V } ( \mathrm { t } )$ : điện áp theo thời gian (V) $\mathrm { V p V } _ { \mathrm { \ell } }$ _p: biên độ (amplitude), điện áp cực đại $\pm \mathrm { V p }$ sin(): dao động hình sin tuần hoàn 2π2\pi: hằng số chuyển đổi từ chu kỳ $\left( \mathrm { H z } \right)$ sang tần số góc (rad/s) ff: tần số (Hz), số dao động trong 1 giây tt: thời gian (s) • ϕ\phi: pha (phase), dịch chuyển sóng theo thời gian, đơn vị độ $( ^ { \circ } )$

Ví dụ: Ở Mỹ, điện áp AC cho hộ gia đình: biên độ 170 V, tần số $6 0 \mathrm { H z }$ , pha $0 ^ { \circ }$ :

$$
V ( t ) = 1 7 0 \sin ( 2 \pi \cdot 6 0 \cdot t ) V ( t ) = 1 7 0 \cdot \sin ( 2 \pi \cdot 6 0 \cdot t )
$$

# 2.4 Ứng dụng (Applications)

Nguồn AC phổ biến trong nhà dân, cửa hàng, văn phòng, vì:

1. Truyền tải dễ dàng trên khoảng cách dài:

o Điện áp cao $( > 1 1 0 \mathrm { k V } ) $ dòng điện thấp giảm tổn hao năng lượng (I²R) trên đường dây. o AC có thể biến đổi điện áp bằng máy biến áp, tiện lợi cho truyền tải.

2. Cung cấp năng lượng cho động cơ điện:

o Động cơ AC chuyển năng lượng điện thành cơ học. o Máy phát điện cũng là động cơ hoạt động ngược lại (quay trục sinh điện áp). 2025



o Thiết bị sử dụng AC: máy rửa chén, tủ lạnh, máy lạnh, máy giặt, máy bơm,…

# 2.5 Điện áp hiệu dụng (RMS Voltage)

Để tính công suất thực tế của AC, sử dụng điện áp RMS (Root Mean Square):

$$
\mathrm { { V R M S } \mathrm { { = } V p 2 V \_ t e x t \{ R M S \} = \backslash f r a c \{ V \_ p \} \{ \backslash s q r t \{ 2 \} \} } }
$$

Trong đó VpV_p là biên độ cực đại.

Ví dụ: Nguồn AC 170 V (biên độ) điện áp RMS:

$$
\mathrm { V R M S } = 1 7 0 2 \approx 1 2 0 \mathrm { V V } \underline { { { \mathrm {  ~ \ t e x t } } } } \{ \mathrm { R M S } \} = \mathrm { \backslash f r a c } \{ 1 7 0 \} \{ \mathrm { \backslash ~ s q r t } \{ 2 \} \} \mathrm { \backslash ~ a p p r o x ~ 1 2 0 \backslash , \mathrm { \forall ~ s q r a ~ 1 . } ~ }
$$

Điện áp RMS cho biết mức điện áp tương đương DC tạo ra cùng công suất trên tải điện trở.

# 2.6 Công suất AC (AC Power)

# Công suất tức thời:

P(t)=V(t)⋅I(t)P(t) $=$ V(t) \cdot I(t)

Lưu ý: Đối với tải thuần trở, $\scriptstyle \phi = 0 \setminus \cosh = 0$ , công suất trung bình:

$$
\mathrm { P a v g { = } V R M S { \cdot } I R M S P \_ t e x t { \{ a v g \} } = V \_ t e x t { \{ R M S \} } \backslash c d o t { \cal I } \_ t e x t { \{ R M S \} } }
$$

# 2.7 So sánh DC và AC

# Tiêu chí

Dòng chảy điện Một hướng Thay đổi luân phiên Nguồn Pin, ắc quy, máy phát DC Máy phát AC, lưới điện Truyền tải Khó trên khoảng cách dài Dễ dàng qua máy biến áp Ứng dụng chính Điện tử, thiết bị nhỏ Nhà dân, công nghiệp, động cơ