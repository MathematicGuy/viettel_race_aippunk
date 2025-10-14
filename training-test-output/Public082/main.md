

# 1. Giới thiệu

Biến đổi khí hậu toàn cầu đang làm gia tăng tần suất và cường độ của các hiện tượng thời tiết cực đoan: bão siêu mạnh, lũ lụt, hạn hán kéo dài, sóng nhiệt khốc liệt. Để dự báo chính xác và đưa ra cảnh báo sớm, các nhà khoa học cần mô phỏng bầu khí quyển, đại dương và đất liền ở quy mô hành tinh với độ phân giải rất cao.

Tính toán hiệu năng cao (High-Performance Computing – HPC) cung cấp siêu máy tính với hàng trăm nghìn lõi xử lý song song, giúp giải quyết các mô hình phương trình động lực học chất lưu, tương tác khí quyển–đại dương và hóa học khí quyển trong thời gian khả thi. HPC trở thành nền tảng cốt lõi cho nghiên cứu khí hậu và hệ thống dự báo thời tiết toàn cầu.

# 2. HPC là gì? High Performance Computing là gì?

HPC (High Performance Computing), hay tính toán hiệu năng cao, là một lĩnh vực sử dụng các hệ thống máy tính để giải quyết các bài toán phức tạp, đòi hỏi khối lượng tính toán lớn trong thời gian ngắn. Thông thường, HPC kết hợp nhiều máy tính hoặc các cụm máy chủ (server cluster) để làm việc đồng thời, giúp rút ngắn thời gian xử lý so với các hệ thống thông thường. HPC thường được sử dụng trong các lĩnh vực như khoa học, kỹ thuật, y tế, nghiên cứu và trí tuệ nhân tạo, nơi yêu cầu tài nguyên tính toán cao và tốc độ xử lý nhanh chóng.



# HPC

High Performance Computing hay tính toán hiéu nǎng cao, là mòt lính vurc sú dung các hé thōng máy tính dě giái quyět các bài toán phúc tap, dòi hói tính toán lón trong thòi gian ngǎn

![](images/image1.jpg)

# HPC (High Performance Computing)

# 3. Thành phần của hệ thống HPC

Cấu trúc của hệ thống HPC thường bao gồm các thành phần tương tự như một phòng máy chủ hoặc trung tâm dữ liệu, với hàng chục, hàng trăm, hoặc thậm chí hàng nghìn thiết bị ngoại vi và server được kết nối với nhau. Hệ thống này được chia thành ba loại nút chính dựa trên chức năng của chúng:

Một cụm HPC cho AI

Máy tính hoặc cụm máy tính (Compute Nodes): Đây là bộ não của hệ thống HPC, thực hiện các phép tính phức tạp và xử lý các tác vụ tính toán. Các nút tính toán chứa các máy chủ với CPU/GPU mạnh mẽ, giúp xử lý các bài toán nhanh chóng và hiệu quả.   
Hệ thống lưu trữ dữ liệu (Storage Nodes): Được thiết kế để xử lý và lưu toán với tốc độ cao. Các nút này thường sử dụng ổ SSD hoặc các hệ thống lưu trữ phân tán.

Hạ tầng mạng (Network Nodes)



• Hạ tầng mạng (Network Nodes): Sử dụng mạng tốc độ cao (như InfiniBand) để truyền tải dữ liệu nhanh chóng giữa các nút trong cụm HPC, cũng như giúp các máy chủ và nút tính toán giao tiếp với nhau và kết nối với các hệ thống bên ngoài.   
• Phần mềm quản lý: Bao gồm hệ điều hành, phần mềm lập lịch tác vụ (job scheduler) và các công cụ tối ưu hóa hiệu năng cho các ứng dụng HPC.

Một hệ thống HPC hoạt động như một siêu máy tính gắn kết, nơi tổng thể của hệ thống mạnh mẽ hơn rất nhiều so với chỉ tổng các bộ phận của nó. Hệ thống này cho phép xử lý các bài toán yêu cầu tài nguyên tính toán lớn và tốc độ xử lý nhanh trong các lĩnh vực như khoa học, nghiên cứu, kỹ thuật và trí tuệ nhân tạo.

Thành phần của hệ thống HPC

# 4. Cơ sở kỹ thuật của HPC cho mô phỏng khí hậu

• Kiến trúc siêu máy tính song song: o Hàng chục nghìn CPU/GPU kết nối bằng mạng tốc độ cao (InfiniBand). o Khả năng xử lý hàng petaflop đến exaflop.

• Phân tán miền (Domain Decomposition): o Trái Đất được chia thành các ô lưới 3D nhỏ (grid cell) cho khí quyển, đại dương. o Mỗi nút HPC xử lý một tập hợp ô lưới, truyền thông liên tục với các nút khác.

• Mô hình phương trình đạo hàm riêng: o Giải Navier–Stokes cho dòng chảy khí quyển.



o Ghép nối với mô hình hóa bức xạ, mây, aerosol, sinh học đại dương.

# 5. Ứng dụng trong mô phỏng khí hậu dài hạn

• Dự báo biến đổi khí hậu 100 năm: Mô phỏng kịch bản phát thải khác nhau (RCP, SSP) để dự đoán nhiệt độ, mực nước biển, tần suất bão. • Đánh giá tác động khu vực: Mô hình độ phân giải cao ( $1 { - } 5 \mathrm { k m } )$ cho phép dự báo lũ quét, sóng nhiệt cụ thể từng vùng. • Hỗ trợ chính sách: Cung cấp dữ liệu cho các hiệp định quốc tế như Paris Agreement, giúp chính phủ hoạch định giảm phát thải.

# 6. Ứng dụng trong dự báo thời tiết cực đoan

• Dự báo bão: HPC cho phép mô phỏng quỹ đạo và cường độ bão trong vài giờ, cải thiện độ chính xác cảnh báo sớm.   
Cảnh báo lũ và mưa lớn: Mô hình thủy văn kết hợp khí tượng chạy trên siêu máy tính để ước tính lượng mưa, mực nước sông.   
• Theo dõi cháy rừng: Mô phỏng lan truyền lửa và khói theo gió, hỗ trợ sơ tán và điều động lực lượng cứu hỏa.

# 7. Công nghệ hỗ trợ

GPU và tính toán dị thể: Kết hợp CPU và GPU tăng tốc giải phương trình động lực học. Machine Learning kết hợp HPC: Dùng AI để tinh chỉnh mô hình, giảm sai số dự báo. Cloud-HPC Hybrid: Tận dụng tài nguyên đám mây cho các chiến dịch mô phỏng lớn đột xuất.



• Hệ thống lưu trữ tốc độ cao: Cần băng thông hàng trăm GB/s để ghi nhận hàng petabyte dữ liệu đầu ra.

8. Lợi ích và tác động

• Tăng độ chính xác: Độ phân giải cao (dưới $1 \ \mathrm { k m }$ giúp dự báo chi tiết tới từng thành phố.   
• Giảm thời gian tính toán: Từ hàng tuần xuống còn vài giờ cho các kịch bản khẩn cấp.   
Hỗ trợ quyết định chiến lược: Giúp chính phủ, doanh nghiệp lập kế hoạch ứng phó thiên tai và biến đổi khí hậu.   
• Nâng cao nghiên cứu khoa học: Cho phép mô hình hóa các hiện tượng phức tạp như tương tác khí hậu–băng, khí hậu–sinh học.

# 9. Thách thức

• Chi phí đầu tư: Xây dựng và vận hành siêu máy tính tốn hàng trăm triệu USD.   
• Tiêu thụ năng lượng lớn: Yêu cầu giải pháp làm mát và nguồn điện bền vững.   
• Đồng bộ dữ liệu toàn cầu: Cần chuẩn dữ liệu chung và mạng truyền tốc độ cao giữa các trung tâm khí tượng.   
• Đào tạo nhân lực: Đòi hỏi chuyên gia lập trình song song và khoa học khí hậu.

10. Xu hướng tương lai

• Exascale Computing: Siêu máy tính đạt trên $1 0 { \mathord { \sim } } 1 8$ phép tính/giây cho mô hình toàn cầu độ phân giải vài trăm mét.



• AI-HPC kết hợp: AI học từ kết quả mô phỏng để tạo “mô hình thay thế” (surrogate models) nhanh hơn nhưng vẫn chính xác.   
• Năng lượng xanh cho HPC: Tận dụng năng lượng tái tạo, làm mát bằng chất lỏng để giảm dấu chân carbon.   
• Mô phỏng đa vật lý: Ghép khí quyển, đại dương, băng, sinh học, kinh tế để tạo dự báo toàn diện về tác động khí hậu.