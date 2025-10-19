

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