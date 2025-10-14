### TASK EXTRACT


# Public_001
Công nghệ ứng dụng vào mô hình nhà thông minh dựa trên Internet vạn vật (IoT - Internet of Things) phần lớn bị hạn chế và phân tán. Các đánh giá trong bài viết được thực hiện để phân loại bối cảnh nghiên cứu về ứng dụng IoT xây dựng mô hình nhà thông minh, nhằm cung cấp những hiểu biết có giá trị về công nghệ và hỗ trợ các nhà nghiên cứu hiểu các nền tảng có sẵn và các lỗ hổng trong lĩnh vực này. Chúng tôi tiến hành tìm kiếm các bài viết liên quan đến (1) nhà thông minh, (2) ứng dụng và (3) IoT trong ba cơ sở dữ liệu chính, cụ thể là: Web of Science, ScienceDirect và IEEE Explore. Các cơ sở dữ liệu này chứa tài liệu về các ứng dụng nhà thông minh sử dụng IoT. Tập dữ liệu thu được bao gồm 229 bài báo được chia thành bốn lớp. Lớp đầu tiên bao gồm các bài viết đánh giá và khảo sát liên quan đến IoT trong mô hình xây dựng nhà thông minh, lớp thứ hai bao gồm các tài liệu ứng dụng IoT và việc sử dụng chúng, lớp thứ ba chứa các đề xuất để phát triển và vận hành các ứng dụng IoT, lớp cuối cùng bao gồm các nghiên cứu thực tế để phát triển IoT ứng dụng nhà thông minh. Sau đó xác định các đặc điểm cơ bản của lĩnh vực mới này theo các khía cạnh: sử dụng IoT vào nhà thông minh cùng những thách thức và các đề xuất để cải tiến.

# 1. Nội dung chính

# 1.1 Giới thiệu

Nhà thông minh cổ điển, IOT, điện toán đám mây (Cloud Computing) và xử lý sự kiện dựa trên quy tắc, là những nền tảng của nhà thông minh tiên tiến. Mỗi nền tảng đóng góp các thuộc tính và công nghệ cốt lõi của nó. IoT thì kết nối internet và quản lý từ xa các thiết bị di động, được tích hợp với nhiều loại cảm biến. Cảm biến có thể được gắn vào các thiết bị gia đình chẳng hạn như máy lạnh, đèn và các thiết bị khác. Điện toán đám mây cung cấp khả năng tính toán, không gian lưu trữ, phát triển các ứng dụng, duy trì, thực thi các dịch vụ và truy cập các thiết bị gia đình ở bất kỳ đâu vào bất kỳ thời điểm nào. (D. Halabi, S. Hamdan và S. Almajali, 2018).

Phần này giải thích sự tích hợp các nền tảng nhà thông minh cổ điển, IoT và điện toán đám mây. Các phần còn lại sẽ trình bày chi tiết về các nền tảng. Phần $2 \mathrm { s } \tilde { \mathrm { e } } \mathrm { m } \hat { \mathrm { o } }$ tả ngôi nhà thông minh cổ điển, phần 3 giới thiệu IOT, phần 4 trình bày điện toán đám mây, phần 5 sẽ trình bày mô-đun xử lý sự kiện, phần ó mô tả nhà thông minh tiên tiến kết hợp các nền tảng này, cuối cùng phần 7 cung cấp một số thông tin thực tế và các lựa chọn liên quan xây dựng, triển khai nhà thông minh tiên tiến thực tế. Mô tả thử nghiệm qua ba ví dụ cho thấy bản chất sự tích hợp sẽ được trình bày trong phần 8. Cuối cùng, xác định các vấn đề mở và hướng đi trong tương lai của các nền tảng ứng dụng vào nhà thông minh tiên tiến. (Q. Lyu, N. Zheng, H. Liu, C. Gao, S. Chen và J. Liu, 2019).



# 1.2 Nhà thông minh trước năm 2010

Năm 2008, nhà thông minh là một ý tưởng tự động hóa ngôi nhà, liên quan đến việc kiểm soát, tự động hóa tất cả công nghệ tích hợp trong nó. Nó xác định nơi có các thiết bị, ánh sáng, hệ thống sưởi, điều hòa không khí, TV, máy tính, hệ thống giải trí, thiết bị gia dụng lớn như máy giặt/ máy sấy và tủ lạnh/ tủ đông, hệ thống an ninh và camera có khả năng giao tiếp với nhau và được điều khiển từ xa bằng thời gian biểu, điện thoại, di động hoặc internet. Các hệ thống này bao gồm các công tắc và cảm biến được kết nối tới trung tâm được điều khiển bởi con người bằng thiết bị đầu cuối hoặc thiết bị di động được kết nối với các dịch vụ đám mây. (Funk, M., Chen, L.-L, Yang, S.-W.., & Chen, Y.-K., 2018).

Vào năm 2009, nhà thông minh được cung cấp nhằm mục đích an ninh, sử dụng năng lượng hiệu quả, chi phí vận hành thấp và tiện lợi. Việc lắp đặt các sản phẩm thông minh mang lại sự tiện lợi và tiết kiệm thời gian, tiền bạc và năng lượng. Các hệ thống như vậy có thể thích ứng và điều chỉnh để đáp ứng nhu cầu thay đổi liên tục của chủ nhà. Trong hầu hết các trường hợp, cơ sở hạ tầng của nó đủ linh hoạt để tích hợp với nhiều loại thiết bị từ các nhà cung cấp với nhiều tiêu chuẩn khác nhau. (Ghajargar, M., Wiberg, M., & Stolterman, E., 2018).

Năm 2010, sự phổ biến của nhà thông minh phát triển với tốc độ cao, nó đã trở thành một phần của xu hướng hiện đại hóa và giảm các chi phí bằng cách tích hợp khả năng duy trì nhật ký các sự kiện, thực hiện các quy trình học máy để cung cấp. (AC Jose và R. Malekian, 2018).

# 1.2.1 Dịch vụ nhà thông minh

# 1.2.1.1. Đo điều kiện nhà

Năm 2010, nhà thông minh được trang bị một bộ cảm biến để đo các điều kiện trong nhà, chẳng hạn như: nhiệt độ, độ ẩm, ánh sáng và khoảng cách. Mỗi cảm biến thực hiện một chức năng riêng nhằm ghi lại một hoặc nhiều phép đo. Nhiệt độ và độ ẩm có thể được đo bởi một cảm biến hoặc các cảm biến khác tính toán tỷ lệ ánh sáng cho một khu vực nhất định và khoảng cách từ nó đến mỗi đối tượng tiếp xúc với nó. Tất cả các cảm biến đều cho phép lưu trữ dữ liệu và hiển thị trực quan để người dùng có thể xem ở bất kỳ đâu và bất kỳ lúc nào. Để làm như vậy, cần có một bộ xử lý tín hiệu, một giao thức truyền thông và một máy chủ lưu trữ trên cơ sở hạ tầng đám mây. (N. Ghosh, S. Chandra, V. Sachidananda và Y. Elovici, 2019).



# 1.2.1.2. Quản lý thiết bị gia dụng

Năm 2010, các dịch vụ đám mây được tạo ra để quản lý và lưu trữ dữ liệu các thiết bị gia dụng. Việc quản lý cho phép người dùng kiểm soát đầu ra của thiết bị truyền động thông minh liên quan đến các thiết bị gia dụng, chẳng hạn như đèn và quạt. Thiết bị truyền động thông minh là các thiết bị, chẳng hạn như van và công tắc, thực hiện các hành động như bật hoặc tắt hoặc điều chỉnh hệ thống hoạt động. Bộ truyền động cung cấp nhiều chức năng khác nhau, chẳng hạn như dịch vụ van bật/ tắt, định vị tỷ lệ phần trăm mở, điều chỉnh để kiểm soát các thay đổi về điều kiện dòng chảy, tắt khẩn cấp (ESD). Để kích hoạt thiết bị truyền động, lệnh ghi kỹ thuật số được cấp cho thiết bị truyền động. (Jenkins, T., 2015).

# 1.2.1.3. Kiểm soát việc ra vào nhà

Năm 2010, công nghệ truy cập vào ngôi nhà thông minh thường được sử dụng cho các cửa ra vào công cộng. Hệ thống này thường sử dụng cơ sở dữ liệu với các thuộc tính nhận dạng những người có quyền truy cập. Khi một người đang tiếp cận hệ thống kiểm soát truy cập, các thuộc tính nhận dạng của người đó được thu thập ngay lập tức và so sánh với cơ sở dữ liệu. Nếu nó khớp với dữ liệu cơ sở dữ liệu, quyền truy cập được cho phép, nếu không, quyền truy cập bị từ chối. Đối với một hệ thống phân tán rộng, sẽ sử dụng các dịch vụ đám mây để thu thập và xử lý dữ liệu của người muốn truy cập. Một số sử dụng thẻ từ hoặc thẻ nhận dạng, số khác sử dụng hệ thống nhận dạng khuôn mặt, vân tay và RFID. (A. Yang, C. Zhang, Y. Chen, Y. Zhuansun và H. Liu, 2020)

Ví dụ trong một triển khai, thẻ RFID và đầu đọc RFID đã được sử dụng. Những người được ủy quyền đều có thẻ RFID. Người này quét thẻ qua đầu đọc RFID đặt gần cửa. ID được quét và gửi qua internet đến hệ thống đám mây. Hệ thống đã đăng ID lên dịch vụ kiểm soát để so sánh ID đã quét với các ID được ủy quyền trong cơ sở dữ liệu. (Manzini, E., & Vezzoli, C., 2GG3).

# Các thành phần chính

Cảm biến để thu thập dữ liệu bên trong và bên ngoài ngôi nhà và đo các điều kiện trong nhà. Các cảm biến này được kết nối với chính ngôi nhà và với các thiết bị gắn liền trong nhà. Những cảm biến này không phải là cảm biến IoT, được gắn vào các thiết bị gia dụng. Dữ liệu của cảm biến được thu thập và liên tục chuyển qua mạng cục bộ đến máy chủ của nhà thông minh. (Pandey, S., 2GiS).



Bộ xử lý để thực hiện các hành động cục bộ và tích hợp. Nó cũng có thể được kết nối với đám mây cho các ứng dụng yêu cầu tài nguyên mở rộng. Dữ liệu của cảm biến sau đó được xử lý bởi các quy trình của máy chủ cục bộ. (Roos, G., 2Gi6).

Một tập hợp các phần mềm được đóng gói dưới dạng API, cho phép các ứng dụng bên ngoài thực thi nó và truyền các tham số đã được xác định trước. Một API như vậy có thể xử lý dữ liệu cảm biến hoặc quản lý các hành động cần thiết.

Bộ truyền động cung cấp và thực hiện các lệnh trong máy chủ hoặc các thiết bị điều khiển khác. Nó chuyển hoạt động bắt buộc sang cú pháp lệnh mà thiết bị có thể thực thi. Trong quá trình xử lý dữ liệu của cảm biến đã nhận, nó có nhiệm vụ kiểm tra xem các quy tắc đúng hoặc sai và khởi chạy một lệnh tới bộ xử lý thiết bị thích hợp. (Ryan, A., 2Gi4).

Cơ sở dữ liệu lưu trữ các thông tin thu thập từ các cảm biến và các dịch vụ đám mây, nó được sử dụng để phân tích, trình bày và hiển thị dữ liệu. Dữ liệu đã xử lý được lưu trong cơ sở dữ liệu để sử dụng trong tương lai. (Ryan, W., Stolterman, E., Jung, H., Siegel, M., Thompson, T., & Hazlewood,WR., 2GG9).

# 1.3 Tổng quan về Internet vạn vật

Mô hình Internet of things (IoT) đề cập đến các đối tượng thiết bị được kết nối với internet. Các thiết bị như cảm biến và thiết bị truyền động được trang bị giao diện, bộ xử lý, bộ nhớ và các phần mềm. Nó cho phép tích hợp các đối tượng vào internet, thiết lập sự tương tác giữa con người và thiết bị, giữa các thiết bị với nhau. Công nghệ quan trọng của IoT bao gồm nhận dạng tần số vô tuyến (RFID), công nghệ cảm biến và công nghệ thông minh. RFID là nền tảng và cốt lõi của việc xây dựng IoT. Khả năng xử lý và giao tiếp cùng với các thuật toán của nó cho phép tích hợp nhiều thành phần khác nhau để hoạt động như một thể thống nhất, đồng thời cũng cho phép dễ dàng bổ sung và loại bỏ các thành phần, việc này làm cho IoT trở nên mạnh mẽ và linh hoạt để tiếp nhận các thay đổi. Để giảm thiểu việc sử dụng băng thông, nó đang sử dụng JSON, một phiên bản nhẹ gọn của XML, cho các thành phần và tin nhắn ngoài hệ thống. (Sayar, D. & Er, Ö., 2GiS).

# 1.4 Điện toán đám mây và đóng góp của nó cho IoT và nhà thông minh

Điện toán đám mây là một nhóm tài nguyên máy tính được chia sẻ sẵn sàng cung cấp nhiều loại dịch vụ điện toán ở các cấp độ khác nhau, từ cơ sở hạ tầng đến các dịch vụ ứng dụng phức tạp nhất, dễ dàng phân bổ và phát hành hoặc tương tác với nhà cung cấp dịch vụ. Trên thực tế, nó quản lý tài nguyên máy tính, lưu trữ và truyền thông được nhiều người dùng chia sẻ trong một môi trường ảo hóa và cô lập. (MR Alam, MBI Reaz và MAM Ali, 2018).



IoT và nhà thông minh có thể tận dụng được các lợi ích từ các tài nguyên và chức năng rộng lớn của đám mây để bù đắp hạn chế của nó trong lưu trữ, xử lý, giao tiếp, hỗ trợ theo nhu cầu, sao lưu và phục hồi. Ví dụ: đám mây có thể hỗ trợ quản lý, dịch vụ IoT và thực thi các ứng dụng bổ sung bằng cách sử dụng dữ liệu do nó tạo ra. Nhà thông minh có thể được cô đọng, chỉ tập trung vào các chức năng cơ bản và quan trọng, do đó, giảm thiểu tài nguyên cục bộ do dựa vào các khả năng tài nguyên đám mây. Nhà thông minh và IoT sẽ tập trung vào thu thập dữ liệu, xử lý cơ bản và truyền thông tin lên đám mây để xử lý tiếp. Với các thách thức bảo mật, đám mây bảo mật cao với dữ liệu riêng tư và các dữ liệu khác sẽ công khai. (A. Bassi và G. Horn, Internet of things năm 2020).

IoT, nhà thông minh và điện toán đám mây không chỉ là sự hợp nhất của các công nghệ. Đúng hơn, là sự cân bằng giữa tính toán cục bộ và tập trung cùng với việc tối ưu hóa việc sử dụng tài nguyên. Một tác vụ điện toán có thể được thực hiện trên IoT và các thiết bị gia đình thông minh hoặc được thuê ngoài trên đám mây. Việc tính toán phụ thuộc vào sự cân bằng tổng chi phí, tính khả dụng của dữ liệu, mức độ phụ thuộc của dữ liệu, lưu lượng vận chuyển dữ liệu, mức độ phụ thuộc vào truyền thông và các bảo mật. Một mặt, mô hình điện toán liên quan đến ba thành phần là đám mây, IoT và nhà thông minh sẽ giảm thiểu chi phí của toàn bộ hệ thống, thường tập trung hơn vào việc giảm tài nguyên trong ngôi nhà. (Verbeek, P.-P., 2015).

Một số ví dụ về các dịch vụ chăm sóc sức khỏe được cung cấp bởi tích hợp đám mây và IoT: quản lý thông tin đúng cách, chia sẻ hồ sơ chăm sóc sức khỏe điện tử cho phép các dịch vụ y tế chất lượng cao; quản lý dữ liệu cảm biến chăm sóc sức khỏe, làm cho thiết bị di động phù hợp để cung cấp dữ liệu y tế, bảo mật quyền riêng tư và độ tin cậy bằng cách nâng cao bảo mật dữ liệu y tế, tính khả dụng của dịch vụ và dự phòng, các dịch vụ hỗ trợ sinh hoạt thời gian thực và thực thi trên đám mây các dịch vụ y tế dựa trên truyền thông đa phương tiện. (Verbeek,P., 2016).

Xử lý sự kiện tập trung, một hệ thống dựa trên quy tắc

Nhà thông minh và IoT rất phong phú với các cảm biến, tạo ra luồng dữ liệu lớn dưới dạng tin nhắn hoặc sự kiện. Xử lý dữ liệu này vượt quá khả năng của con người. Do đó, các hệ thống xử lý sự kiện đã được phát triển và sử dụng để phản hồi nhanh hơn với các sự kiện đã phân loại. Trong phần này, tập trung vào các hệ thống quản lý quy tắc gắn liền với các sự kiện để thực hiện những thay đổi hệ thống khi sự kiện xảy ra. Người dùng có thể xác định quy tắc kích hoạt sự kiện và kiểm soát việc cung cấp dịch vụ thích hợp không. Quy tắc bao gồm các điều kiện của sự kiện, mẫu sự kiện và thông tin liên quan đến tương quan có thể được kết hợp để tạo mô hình cho các tình huống phức tạp. Nó đã được thực hiện trong một ngôi nhà thông minh điển hình và đã chứng minh sự phù hợp của nó đối với một hệ thống hướng đến dịch vụ. (I. Androutsopoulos, J. Koutsias, KV Chandrinos, G. Paliouras và CD Spyropoulos, 2019).



Hệ thống có thể xử lý một lượng lớn sự kiện, thực thi các chức năng giám sát, điều hướng và tối ưu hóa các quy trình với thời gian thực. Nó phát hiện và phân tích các điểm bất thường hoặc ngoại lệ và tạo ra các phản ứng chủ động/ thích ứng, chẳng hạn như cảnh báo và ngăn chặn các hành động thiệt hại. Các tình huống được mô hình hóa bởi giao diện thân thiện với người dùng cho các quy tắc do sự kiện kích hoạt. Khi cần thiết, nó sẽ chia chúng thành các yếu tố đơn giản, dễ hiểu. Mô hình đề xuất có thể được tích hợp liền mạch vào nền tảng xử lý sự kiện phân tán và hướng dịch vụ. (Apple, 2018).

Quá trình đánh giá được kích hoạt bởi các sự kiện cung cấp trạng thái mới nhất và thông tin từ môi trường liên quan. Kết quả là một biểu đồ quyết định đại diện cho các quy tắc. Nó có thể chia nhỏ các tình huống phức tạp thành các điều kiện đơn giản và kết hợp chúng với nhau, tạo ra các điều kiện phức tạp. Đầu ra là một sự kiện phản hồi được đưa ra khi một quy tắc được kích hoạt. Các sự kiện đã kích hoạt có thể được sử dụng làm đầu vào cho các quy tắc khác để đánh giá thêm.

Hành động tạo ra các sự kiện phản hồi, kích hoạt các hoạt động phản hồi. Các mẫu sự kiện có thể khớp với chuỗi sự kiện theo thời gian, cho phép mô tả các tình huống có liên quan đến sự xuất hiện của các sự kiện. Ví dụ, khi cửa mở quá lâu. (R. Petrolo, V. Loscrì và N. Mitton, 2017).

Những thách thức được biết đến với mô hình này: cấu trúc cho các sự kiện và dữ liệu đã xử lý, cấu hình dịch vụ và bộ điều hợp cho các bước xử lý, bao gồm các thông số đầu vào và đầu ra của chúng, giao diện với hệ thống bên ngoài để cảm nhận dữ liệu và phản hồi bằng cách thực hiện các giao dịch, cấu trúc cho các sự kiện và dữ liệu đã xử lý, biến đổi dữ liệu, phân tích dữ liệu và tính bền bỉ. Nó cho phép mô hình hóa các sự kiện nào sẽ được xử lý bởi dịch vụ quy tắc và cách các sự kiện phản hồi sẽ được chuyển tiếp đến các dịch vụ sự kiện khác. Quá trình này rất đơn giản: dữ liệu được thu thập và nhận từ các bộ điều hợp chuyển tiếp các sự kiện tới các dịch vụ sự kiện sử dụng chúng. (ZB Celik, E. Fernandes, E. Pauley, G. Tan và P. McDaniel, 2019).



# 1.4.1 Ngôn ngữ xử lý sự kiện

Xử lý sự kiện liên quan đến việc nắm bắt và quản lý các sự kiện được xác định trước theo thời gian thực. Nó bắt đầu từ việc quản lý các thực thể của các sự kiện ngay từ khi sự kiện xảy ra, thậm chí xác định, thu thập dữ liệu, liên kết quy trình và kích hoạt hành động phản hồi. Để cho phép xử lý sự kiện nhanh chóng và linh hoạt, một ngôn ngữ xử lý sự kiện được sử dụng, cho phép cấu hình nhanh các tài nguyên cần thiết để xử lý chuỗi hoạt động dự kiến cho mỗi loại sự kiện. Nó bao gồm hai mô-đun, ESP và CEP. ESP xử lý hiệu quả sự kiện, phân tích nó và chọn sự kiện thích hợp. CEP xử lý các sự kiện tổng hợp. Ngôn ngữ sự kiện mô tả các kiểu sự kiện phức tạp được áp dụng trên bản ghi sự kiện. (N. Panwar, S. Sharma, S. Mehrotra, L. Krzywiecki và N. Venkatasubramanian, 2019).

# Khám phá lại quy trình làm việc từ các sự kiện

Trong một số trường hợp, các quy tắc liên quan đến sự khác biệt trong chuỗi sự kiện trong quy trình làm việc. Trong những trường hợp như vậy, bắt buộc phải hiểu chính xác quy trình làm việc và các sự kiện liên quan. Để khắc phục điều này, đề xuất quy trình thiết kế ngược để tự động xem lại quy trình công việc từ nhật ký sự kiện được thu thập theo thời gian, giả sử các sự kiện này được sắp xếp theo thứ tự và mỗi sự kiện đề cập đến một tác vụ đang được thực thi cho một trường hợp. Quá trình xem lại có thể được sử dụng để xác nhận trình tự quy trình làm việc bằng cách đo lường sự khác biệt giữa các mô hình mô tả và các lần thực thi quy trình thực tế. Quá trình xem lại bao gồm ba bước sau: (1) xây dựng bảng phụ thuộc/ tần suất. (2) Quy nạp đồ thị phụ thuộc/ tần số. (3) Tạo lưới WF từ đồ thị D/ F. (S. Zhihua, 2016).

# 1.5 Nhà thông minh từ sau năm 2010

Trong phần này sẽ tập trung vào sự tích hợp của nhà thông minh, IoT và điện toán đám mây để xác định một mô hình điện toán mới. Có thể tìm thấy trong phần tài liệu các cuộc khảo sát và nghiên cứu về nhà thông minh, IoT và điện toán đám mây, các thuộc tính, tính năng, công nghệ và nhược điểm của chúng. (KR Sollins, 2019).

Vào năm 2011, mô tả các thành phần chính của ngôi nhà thông minh tiên tiến và khả năng kết nối giữa chúng. Ở khối bên trái, môi trường nhà thông minh, có thể thấy các thiết bị điển hình được kết nối với mạng cục bộ (LAN). Điều này cho phép giao tiếp giữa các thiết bị và môi trường bên ngoài. Kết nối với mạng LAN là một máy chủ và cơ sở dữ liệu của nó. Máy chủ kiểm soát các thiết bị, ghi nhật ký hoạt động của nó, cung cấp báo cáo, trả lời các truy vấn và thực hiện các lệnh thích hợp. Đối với các tác vụ toàn diện hoặc phổ biến hơn, máy chủ nhà thông minh, chuyển dữ liệu lên đám mây và kích hoạt từ xa các tác vụ bằng cách sử dụng API, quy trình giao diện lập trình ứng dụng. (Y. Meng, W. Zhang, H. Zhu và XS Shen, 2018).



Năm 2012, để chứng minh những lợi ích của ngôi nhà thông minh tiên tiến, sử dụng RSA, một thuật toán mật mã bất đối xứng mạnh mẽ, tạo ra một khóa công khai và riêng tư để mã hóa/ giải mã các tin nhắn. Sử dụng khóa công khai, mọi người đều có thể mã hóa một tin nhắn, nhưng chỉ những người giữ khóa riêng tư mới có thể giải mã tin nhắn đã gửi. Việc tạo ra các khóa và mã hóa/ giải mã các thông điệp, bao gồm các tính toán mở rộng, đòi hỏi không gian bộ nhớ và sức mạnh xử lý đáng kể. Do đó, nó thường được xử lý trên các máy tính mạnh được xây dựng để đáp ứng các tài nguyên cần thiết. Tuy nhiên, do tài nguyên có hạn, việc chạy RSA trong một thiết bị IoT gần như là không thể, và do đó, tạo ra một lỗ hổng về bảo mật trên Internet. Giải quyết vấn đề bảo mật bằng cách kết hợp sức mạnh của các bộ xử lý nhà thông minh cục bộ để tính toán một số phép tính RSA và chuyển tiếp các tác vụ điện toán phức tạp hơn lên trên đám mây xử lý. Sau đó, kết quả sẽ được chuyển trở lại cảm biến IoT để được biên dịch và lắp ráp lại với nhau, nhằm tạo ra mã giải mã/mã hóa RSA. Ví dụ minh họa luồng dữ liệu giữa các thành phần nhà thông minh tiên tiến. Trong đó, mỗi thành phần thực hiện ngăn xếp hoạt động của riêng mình để tạo ra đầu ra duy nhất của nó. Tuy nhiên, trong trường hợp các nhiệm vụ phức tạp và diễn ra trong thời gian dài, nó sẽ chia nhiệm vụ thành các tác vụ con để thực thi bởi các thành phần mạnh hơn. Đề cập đến ví dụ RSA, thiết bị IoT bắt đầu yêu cầu tạo khóa mã hóa và gửi một thông báo yêu cầu đến ứng dụng RSA chạy trong máy tính trong ngôi nhà thông minh với p và q là các số nguyên tố, khi p và q được chấp nhận, mã mã hóa được tạo. Trong giai đoạn sau, thiết bị IoT đưa ra yêu cầu mã hóa tin nhắn cho máy tính, sử dụng khóa mã hóa RSA được tạo gần đây. Sau đó, thông điệp được mã hóa sẽ được chuyển trở lại thiết bị IoT để thực hiện thêm. Một kịch bản tương tự có thể xảy ra theo hướng ngược lại, khi một thiết bị IoT nhận được thông báo, nó có thể yêu cầu nhà thông minh giải mã nó. (P. Rajiv, R. Raj, và M. Chandra, 2016).

Năm 2014, các kịch bản RSA mô tả việc sử dụng sức mạnh của điện toán đám mây, khả năng tính toán bảo mật của ngôi nhà thông minh và cuối cùng là sức mạnh của thiết bị IoT. Nó chứng minh rằng nếu không có sự hợp tác tự động này, RSA sẽ không thể được thực thi ở cấp độ IoT. (E. Fernandes, J. Jung và A. Prakash, 2016), (H. Lee, CR Ahn, N. Choi, T. Kim và H. Lee, 2019).

Vào năm 2015, một ví dụ thực tế là một số thiết bị tách rời, chẳng hạn như lò nướng, nồi nấu và chảo trên bếp ga đang hoạt động. Người dùng rời khỏi nhà mà không tắt các thiết bị này. Trong trường hợp này các IoT có liên quan đã được điều chỉnh để tự động tắt dựa trên các quy tắc được xác định trước. Nếu không, ngôi nhà thông minh nhận ra nhà không có ai $\dot { \mathbf { O } }$ nhà bằng cách xác định (cửa nhà được mở và sau đó khóa, nhà để xe được mở, ô tô rời đi, cổng chính được mở và sau đó đóng lại) và sẽ tắt tất cả các thiết bị đang hoạt động được phân loại là rủi ro trong trường hợp vắng mặt và nó sẽ gửi một tin nhắn đến danh sách gửi thư được xác định trong trường này. (A. Jacobsson, M. Boldt và B. Carlsson, 2016), (H. Lee, CR Ahn, N. Choi, T. Kim và H. Lee, 2019).



1.6 Các khía cạnh thực tế và cân nhắc triển khai cho IoT và nhà thông minh Nhà thông minh có ba thành phần: phần cứng, phần mềm và giao thức truyền thông. Nó có nhiều ứng dụng kỹ thuật số cho người dùng. Một số lĩnh vực tự động hóa ngôi nhà đã kích hoạt kết nối IoT, chẳng hạn như: điều khiển ánh sáng, làm vườn, an toàn và an ninh, chất lượng không khí, giám sát chất lượng nước, trợ lý giọng nói, công tắc, khóa, đồng hồ đo năng lượng và nước. (S. Madakam và H. Date, 2016).

Các thành phần nhà thông minh tiên tiến bao gồm: cảm biến IoT, cổng, giao thức, phần sụn, điện toán đám mây, cơ sở dữ liệu, phần mềm trung gian và cổng. Đám mây IoT có thể được chia thành nền tảng dưới dạng dịch vụ (PaaS) và cơ sở hạ tầng dưới dạng dịch vụ (IaaS). Trình bày các thành phần chính của ngôi nhà thông minh tiên tiến được đề xuất và kết nối với luồng dữ liệu giữa các thành phần của nó. (S. Madakam và H. Date, (2016)), (H. Lee, CR Ahn, N. Choi, T. Kim và H. Lee, 2019).

Ứng dụng nhà thông minh cập nhật cơ sở dữ liệu ngôi nhà trên đám mây để cho phép những người ở xa truy cập và nhận được trạng thái mới nhất của ngôi nhà. Một nền tảng IoT điển hình bao gồm: bảo mật và xác thực thiết bị, quản trị thiết bị, giao thức, thu thập dữ liệu, trực quan hóa, khả năng phân tích, tích hợp với các dịch vụ web khác, khả năng mở rộng, API cho luồng thông tin thời gian thực và thư viện nguồn mở. Cảm biến IoT cho tự động hóa ngôi nhà được biết đến với khả năng cảm biến của chúng, chẳng hạn như: nhiệt độ, độ sáng, mực nước, thành phần không khí, camera giám sát video, giọng nói/ âm thanh, áp suất, độ ẩm, gia tốc kế, hồng ngoại, rung động và siêu âm. Một số cảm biến nhà thông minh được sử dụng phổ biến nhất là cảm biến nhiệt độ, hầu hết là cảm biến kỹ thuật số kết quả cực kỳ chính xác. Ví dụ như cảm biến Lux đo độ sáng. (K. Markantonakis, RN Akram và MG Msgna, 2015).

Cảm biến thành phần không khí được các nhà phát triển sử dụng để đo các thành phần cụ thể trong không khí: giám sát CO, đo mức khí hydro, đo nitơ oxit, mức khí nguy hiểm. Hầu hết chúng đều cần một thời gian nhất định trước khi đưa ra các giá trị chính xác. Máy quay video được sử dụng để giám sát và phân tích, được kết nối tốc độ cao. Nên sử dụng bộ xử lý Raspberry Pi vì mô-đun máy ảnh của nó rất hiệu quả do có đầu nối linh hoạt, được kết nối trực tiếp với bo mạch. (P. Kumar, A. Gurtov, J. Iinatti, M. Ylianttila, và M. Sain, 2016).



Máy dò âm thanh được sử dụng rộng rãi cho mục đích giám sát, phát hiện âm thanh và hành động phù hợp. Một số thậm chí có thể phát hiện mức độ tiếng ồn cực thấp và tinh chỉnh giữa các mức độ tiếng ồn khác nhau.

Cảm biến độ ẩm cảm nhận mức độ ẩm trong không khí cho nhà thông minh. Độ chính xác của nó phụ thuộc vào thiết kế và vị trí cảm biến. Một số cảm biến nhất định như DHT22, được chế tạo để tạo mẫu nhanh, sẽ luôn hoạt động kém hơn khi so sánh với các cảm biến chất lượng cao như HIH6100. (H. Lee, CR Ahn, N. Choi, T. Kim và H. Lee, 2019).

Giao thức giao tiếp thông minh trong nhà như: bluetooth, Wi-Fi hoặc GSM. Bluetooth thông minh hoặc giao thức không dây năng lượng thấp với khả năng phân phối lưới và các thuật toán mã hóa dữ liệu. Zigbee là giao thức dựa trên tần số vô tuyến tuần suất thấp được nối mạng cho IoT. Giao thức X10 sử dụng hệ thống dây điện để truyền tín hiệu và điều khiển. Giao tiếp Insteon, không dây và có dây. Z-wave chuyên về tự động hóa ngôi nhà an toàn. UPB, sử dụng đường dây điện hiện có. ANT là một giao thức năng lượng cực thấp để xây dựng các cảm biến công suất thấp với khả năng phân phối lưới cao. Các giao thức được ưu tiên là bluetooth năng lượng thấp, sóng Z, Zigbee và luồng. Việc kết nối cổng bao gồm: kết nối đám mây, các giao thức được hỗ trợ, độ phức tạp tùy chỉnh và hỗ trợ tạo mẫu. (M. Bassoli, V. Bianchi, và I. De Munari, 2018).

Mô-đun: các gói phần mềm, được quản lý trong lúc chạy, định hướng dịch vụ, quản lý sự phụ thuộc giữa các gói, lớp; kiểm soát vòng đời của các gói, lớp dịch vụ; xác định mô hình giao tiếp động giữa các mô-đun khác nhau, các dịch vụ thực tế - đây là lớp ứng dụng. Lớp bảo mật: tùy chọn, tận dụng kiến trúc bảo mật của Java 2 và quản lý quyền từ các mô-đun khác nhau. (GV Vivek và MP Sunil, 2015).

OpenHAB là một khuôn khổ, kết hợp tự động hóa các thiết bị gia đình và cổng kết nối IoT cho ngôi nhà thông minh. Các tính năng của nó: công cụ quy tắc, cơ chế ghi nhật ký và trừu tượng hóa giao diện người dùng.

Việc triển khai blockchain vào mạng gia đình có thể dễ dàng thực hiện với Raspberry Pi.
cần phải cải tiến lớn với mã hiện có.



# 1.7 Ví dụ về nhà thông minh và IoT

Có thể tìm thấy trong các tài liệu và báo cáo thực tế, nhiều triển khai tích hợp khác nhau giữa ba phần chính: nhà thông minh, IoT và điện toán đám mây.

# 1.7.1 Phát hiện rò rỉ nước và cách phòng ngừa

Bước đầu tiên là triển khai cảm biến nước dưới mọi nguồn rò rỉ tiềm ẩn hợp lý và cảm biến van nước chính tự động cho toàn bộ ngôi nhà, điều này có nghĩa là ngôi nhà được coi như một IoT.

Trong trường hợp cảm biến nước phát hiện rò rỉ nước, nó sẽ gửi một sự kiện đến trung tâm, sự kiện này sẽ kích hoạt ứng dụng “tắt van”. Sau đó, ứng dụng điều khiển gia đình sẽ gửi lệnh “tắt” đến tất cả các thiết bị IoT được xác định với việc ngừng nước và sau đó gửi lệnh “tắt” đến van nước chính. Thông báo cập nhật được gửi qua hệ thống nhắn tin. Thiết lập này giúp bảo vệ khỏi các trường hợp nguồn nước là từ hệ thống ống nước trong nhà. Cấu hình cơ bản giả định tích hợp thông qua tin nhắn và lệnh giữa nhà thông minh và hệ thống điều khiển IoT. Nó thể hiện sự phụ thuộc và những kết quả có lợi của việc kết hợp nhà thông minh và IoT. (YAN Wenbo, WANG Quanyu, và GAO Zhenwei, 2015).

# Đầu báo khói

Giả sử các ngôi nhà đã có các đầu báo khói nhưng không có cầu nối để gửi dữ liệu từ cảm biến đến trung tâm điều khiển nhà thông minh. Việc kết nối các cảm biến này với ứng dụng nhà thông minh cho phép hệ thống phát hiện khói toàn diện. Mở rộng hơn là để thông báo cho cảm biến thang máy chặn việc sử dụng do tình trạng cháy, thậm chí cho bất kỳ cảm biến IoT nào có thể được kích hoạt do cảnh báo khói được phát hiện. (C Y. Chang, C.-H. Kuo, J.-C. Chen và T.-C. Wang, 2015).

# Quản lý sự cố để kiểm soát các thiết bị gia dụng

Hãy xem xét tình huống rời khỏi nhà trong khi một số thiết bị vẫn đang hoạt động. Trong trường hợp vắng mặt đủ lâu, một số thiết bị có thể quá nóng và sắp bị xì. Để tránh những trường hợp như vậy kết nối tất cả các cảm biến của thiết bị IoT với ứng dụng gia đình, để khi tất cả rời khỏi nhà, nó sẽ tự động điều chỉnh tất cả các cảm biến của thiết bị cho phù hợp, để tránh hư hỏng. Lưu ý rằng chỉ báo nhà trống được tạo bởi ứng dụng Nhà thông minh, trong khi chỉ báo “bật” của thiết bị do IoT tạo ra. Do đó, kịch bản này có thể xảy ra do sự tích hợp giữa nhà thông minh và các hệ thống IoT. (U. Guin, A. Singh, M. Alam, J. Canedo và A. Skjellum, 2018), (C. Lachner và S. Dustdar, 2019).

# 1.8 Kết luận



Nhiều kỹ thuật IoT đã được cài đặt trong các ngôi nhà thông minh để cải thiện chất lượng cuộc sống. Để thiết kế và triển khai một hệ thống kiểm soát ngôi nhà, bao gồm ba phần: phần cứng, máy chủ có độ bảo mật cao và ứng dụng web. Phần cứng nút IoT được thiết kế để thử nghiệm trong đời thực và nhận thông tin IoT từ bất kỳ thiết bị nào. Một máy chủ được thiết kế và triển khai để kiểm soát các nút IoT trong hệ thống. Cuối cùng, một ứng dụng sử dụng mọi lúc mọi nơi trên điện thoại thông minh hoặc trình duyệt web thông qua liên kết kết nối giao tiếp Wi-Fi đã được xây dựng để điều khiển hệ thống thông minh IoT theo thời gian thực. Ứng dụng này cho phép điều khiển chức năng cả tự động và thủ công, điều này rất linh hoạt cho người dùng. Hệ thống IoT tiên tiến được lắp đặt tại Đại học Tôn Đức Thắng, Việt Nam. Kết quả cho thấy những lợi ích tiềm năng rõ ràng cho một ngôi nhà thông minh, bao gồm bảo mật mạnh mẽ và chi phí thấp. Trên hết, nghiên cứu này nhằm chứng minh tiềm năng to lớn mà tất cả công nghệ kỹ thuật số mang lại cho ngôi nhà thông minh.

# Public_002


# 1. Học phần

# 1.1 Bộ Môn Hệ Thống Thông Tin

Cơ sở dữ liệu Cấu trúc học phần: 3(2:1:6)

Mô tả học phần: Học phần này trang bị cho người học những kiến thức cơ bản về cơ sở dữ liệu và kiến thức chuyên sâu về mô hình dữ liệu quan hệ: quan hệ, phụ thuộc hàm, các ràng buộc trên quan hệ, siêu khóa, khóa chính, khóa dự tuyển, khóa ngoại, bao đóng của tập phụ thuộc hàm, bao đóng của tập thuộc tính, phủ tối tiểu của tập phụ thuộc hàm, thuật toán tìm bao đóng của tập thuộc tính, thuật toán xác định khóa, các dạng chuẩn và tính chất tương ứng. Trang bị cho người học kiến thức về mô hình thực thể kết hợp để thiết kế CSDL.

# Hệ quản trị cơ sở dữ liệu

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này trang bị cho người học về nguyên lý của DBMS. Cách sử dụng ngôn ngữ lập trình PL/SQL, các định nghĩa và ứng dụng của thủ tục nội tại, bẫy lỗi, chỉ mục, lập trình CSDL, các quản lý truy cập trong DBMS, các nguyên lý quản lý giao tác, quản lý truy xuất cạnh tranh, phục hồi sau sự cố.

# Phân tích thiết kế HTTT

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này trang bị cho người học các kiến thức cơ bản về hệ thống thông tin, các thành phần của một hệ thống thông tin. Học phần cung cấp cho người học các kỹ thuật thu thập thông tin, phân tích hoạt động của hệ thống thông tin; các khái niệm có liên quan, ý nghĩa và tầm quan trọng của chúng. Về hoạt động thiết kế, học phần cung cấp cho người học kiến thức và kỹ năng trong việc xác định cấu trúc, các thành phần cần thiết để xây dựng và triển khai một hệ thống thông tin.

# 1.1.4 Khai phá dữ liệu

Cấu trúc học phần: 3(2:1:6)



Mô tả học phần:

Học phần này trang bị cho người học những kiến thức cơ bản về các khái niệm, thuật toán và ứng dụng của khai phá dữ liệu. Ngoài ra, người học còn có cơ hội trải nghiệm các thư viện, công cụ mã nguồn mở để cài đặt và thử nghiệm thuật toán khai phá dữ liệu. Các chủ đề được đề cập đến trong học phần bao gồm: các khái niệm cơ bản, các ứng dụng và quá trình khai phá dữ liệu, các vấn đề liên quan đến quá trình tiền xử lý dữ liệu, các thuật toán khai phá luật kết hợp (Apriori, FP-Growth, …), các thuật toán phân loại (k-NN, cây quyết định, Naive Bayes, ...), các thuật toán gom cụm (gom cụm phân hoạch k-means, gom cụm phân cấp gộp AGNES, gom cụm dựa trên mật độ DBSCAN, …), các thuật toán phân tích ngoại biên (dựa trên thống kê, dựa trên xấp xỉ, dựa trên gom cụm, dựa trên phân loại), và các độ đo và phương pháp đánh giá các thuật toán khai phá dữ liệu.

# Cơ sở dữ liệu nâng cao

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này giới thiệu những kiến thức tổng quát về một số loại cơ sở dữ liệu (CSDL) mở rộng: CSDL hướng đối tượng, CSDL bán cấu trúc XML, CSDL NoSQL, CSDL phân cấp (blockchain)... Học phần tập trung vào Big Data và CSDL NoSQL, so sánh CSDL quan hệ truyền thống với CSDL NoSQL, phân loại các loại CSDL NoSQL (key-value, document-based, column-based, graph), cài đặt một CSDL NoSQL cụ thể (VD: MongoDB, Cassandra, CouchDB...), thực hiện tạo lập, lưu trữ, quản lý và thao tác dữ liệu trên cơ sở dữ liệu này.

# Phân tích dữ liệu lớn

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần cung cấp cho sinh viên kiến thức về kiến trúc của các hệ thống và các công cụ phục vụ cho hoạt động phân tích dữ liệu lớn. Với mỗi công cụ, môn học giới thiệu các kiến thức cơ bản và nâng cao cũng như phương thức tối ưu hóa hiệu suất hệ thống sử dụng công cụ này. Cùng với các bài tập lập trình, môn học hướng đến mục tiêu giúp người học có thể hình thành ý tưởng, thiết kế và hiện thực hóa hoạt động phân tích dữ liệu trong các hệ thống dữ liệu lớn.



# Bảo mật cơ sở dữ liệu

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này trang bị cho người học những kiến thức nền tảng về cả lý thuyết lẫn thực hành để có thể hiểu được những cơ chế, mô hình và kỹ thuật bảo mật cơ sở dữ liệu, cụ thể: các kiểu tấn công, các cấp độ bảo mật và các phương pháp bảo vệ tương ứng; bảo mật cơ sở dữ liệu bằng phương pháp kiểm soát truy cập (Access Control) với các mô hình DAC, MAC, RBAC; bảo mật bằng phương pháp mã hóa dữ liệu; vấn đề kiểm định (Audit); cách thức hiện thực các mô hình và các công nghệ hỗ trợ bảo mật trong các hệ quản trị cơ sở dữ liệu; nguyên lý thiết kế và cài đặt các cơ chế bảo mật; các mô hình bảo vệ tính toàn vẹn dữ liệu

# 1.1.8 Thương mại điện tử

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần giới thiệu về thương mại điện tử và cung cấp cho người học ba mảng kiến thức chủ đạo: các mô hình kinh doanh thương mại điện tử, các hoạt động marketing cho thương mại điện tử, và các vấn đề chủ đạo khi thiết kế, xây dựng, và vận hành nền tảng thương mại điện tử.

# 1.1.9 Học máy

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học giới thiệu cho sinh viên về lĩnh vực học máy và các giải thuật học máy phổ biến. Sinh viên sẽ thực hiện các bài tập lập trình bằng ngôn ngữ lập trình Python, và phân tích, đánh giá các giải thuật này. Sinh viên cũng sẽ thực tập hình thành ý tưởng, thiết kế và hiện thực hóa một hệ thống học máy đơn giản trong đồ án môn học xuyên suốt học kỳ.

Chuyên đề 2 (Hệ hỗ trợ ra quyết định) Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:



Học phần này cung cấp cho sinh viên các kiến thức về tiến trình ra quyết định, cấu trúc và các thành phần của hệ hỗ trợ ra quyết định, cách quản lý và khai thác dữ liệu, các mô hình được sử dụng trong hệ hỗ trợ ra quyết định… Ngoài ra, sinh viên được trang bị kỹ năng sử dụng các công cụ để giải quyết các bài toán ra quyết định, lưu trữ và khai thác dữ liệu hiệu quả. Sau khi học xong học phần này, sinh viên có khả năng phân tích, thiết kế và xây dựng các hệ hỗ trợ ra quyết định trên nền tảng các hệ thống thông tin quản lý.

# Kho dữ liệu

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học cung cấp cho sinh viên những kiến thức cơ bản về kho dữ liệu. Trong khóa học này, người học sẽ học các khái niệm cơ bản về kho dữ liệu, kiến trúc kho dữ liệu và các mô hình đa chiều. Họ sẽ được thực hành về thiết kế kho dữ liệu và sử dụng các công cụ phổ biến tạo các luồng công việc tích hợp dữ liệu (data integration workflows). Bên cạnh đó, những người học cũng sẽ học cách sử dụng các phần mở rộng của SQL được hỗ trợ bởi các hệ quản trị cơ sở dữ liệu quan hệ để trả lời các câu hỏi phân tích trong kinh doanh.

# Truy tìm thông tin

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần cung cấp kiến thức nền tảng giúp người học hiểu được cách làm việc cũng như cách xây dựng một hệ thống truy tìm (tìm kiếm) thông tin, đặc biệt là thông tin ở dạng văn bản. Cụ thể, sau khi hoàn thành học phần, người học sẽ trình bày được kiến trúc tổng quát của một hệ thống truy tìm thông tin, quá trình tiền xử lý và xây dựng chỉ mục tài liệu. Đặt biệt, người học sẽ có cơ hội được cài đặt các mô hình truy tìm thông tin quan trọng (như mô hình không gian vector, mô hình xác suất, mô hình ngôn ngữ) và các kỹ thuật phản hồi và mở rộng truy vấn. Người học cũng sẽ được trang bị kiến thức về phương pháp đánh giá thực nghiệm một hệ thống truy tìm thông tin để có thể đánh giá và so sánh các thuật toán, mô hình. Ngoài ra, cách hoạt động của một hệ thống tìm kiếm thông tin trên web (web search engine) cũng sẽ được trình bày.



# Nhập môn dữ liệu lớn

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này thuộc nhóm môn học cơ sở ngành, nhằm cung cấp cho người học các kiến thức tổng quan về cơ sở dữ liệu lớn, những ứng dụng của cở sở dữ liệu lớn. Ngoài ra, người học còn được cung cấp những kiến thức về các kỹ thuật cơ bản trong lưu trữ và xử lý, phân tích cơ sở dữ liệu lớn. Về mặt kỹ năng, người học được trang bị khả năng sử dụng một số công cụ phân tích cơ sở dữ liệu lớn thông dụng. Bên cạnh đó, người học cũng được trang bị một số kỹ năng mềm bao gồm: kỹ năng tìm kiếm, chọn lọc và tổng hợp tài liệu, kỹ năng viết và trình bày báo cáo, kỹ năng làm việc nhóm.

# 1.2 Bộ Môn Mạng Máy Tính

Kiến trúc máy tính và hợp ngữ Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần cung cấp cho người học những kiến thức liên quan tới kiến trúc của máy tính cũng như tập lệnh của vi xử lý và lập trình hợp ngữ cho vi xử lý, cụ thể:

Cung cấp kiến thức về các hệ số đếm dùng trong máy tính Kiến trúc tổng quát của bộ xử lý, hiệu suất máy tính, các loại bộ nhớ, các loại xuất nhập, ngắt

Cung cấp kiến thức về các cách biểu diễn dữ liệu trong máy tính

Giới thiệu kiến trúc một số họ vi xử lý của Intel : thanh ghi của họ x86, x86-64

Cung cấp các kiến thức về việc sử dụng tập lệnh x86, x86-64

Cung cấp kiến thức về lập trình hợp ngữ trên linux x64, các lời gọi hệ thống, gọi hợp ngữ từ ngôn ngữ cấp cao.

# Hệ điều hành

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:



Học phần này trang bị cho người học những kiến thức cơ bản về Hệ điều hành, bao $\mathrm { g } \dot { \hat { \mathrm { o } } } \mathrm { m }$ : Mô hình tổng quát, cấu trúc, chức năng, các thành phần cơ bản của hệ điều hành. Các nguyên lý cơ bản để xây dựng Hệ điều hành. Tìm hiểu cấu trúc và việc ứng dụng các nguyên lý cơ bản trong các hệ điều hành cụ thể. Tìm hiểu và mô phỏng điều khiển thiết bị của Hệ điều hành thông qua lập trình hệ thống.

# Mạng máy tính căn bản

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung các các khái niệm cơ bản trong mạng máy tính, đặc điểm cơ bản của các loại mạng; kiến thức về nguyên lý hoạt động của các thiết bị mạng, các kỹ thuật phổ biến triển khai trên hạ tầng mạng, các giao thức phổ biến hoạt động trong hệ thống mạng; các kiến thức về thiết kế, cấu hình và vận hành hệ thống mạng đơn giản.

# 1.2.5 Mật mã học

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này cung cấp các khái niệm cơ bản về mã hóa thông tin, giới thiệu các phương pháp mã hóa, giải mã và ứng dụng của chúng trong bảo mật thông tin, các cơ chế và nghi thức bảo mật: Xác thực, chữ ký số. Ngoài ra, học phần này cũng cung cấp khả năng vận dụng kiến thức về mã hóa thông tin đã học để giải quyết một số bài toán bảo mật trong thực tế. Bên cạnh đó, sinh viên được làm việc trong các nhóm và thuyết trình các vấn đề nâng cao sử dụng các phương tiện trình chiếu.

# Mạng máy tính nâng cao

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung cấp kiến thức về công nghệ định tuyến, phân loại và đặc điểm của các giao thức định tuyến; cung cấp kiến thức về cấu hình một số giao thức phổ biến; cung cấp kiến thức về VLAN, ACL, NAT, các công nghệ WAN.

# An toàn thông tin

Cấu trúc học phần: 3(2:1:6)



Mô tả học phần:

Môn học cung cấp cho sinh viên chuyên ngành Công nghệ Thông tin kiến thức cơ bản về An toàn thông tin trên máy tính như CIA, An toàn trên phần mềm, An toàn trên HĐH, An toàn trên Cơ sở dữ liệu; các vấn đề về An toàn trên mạng máy tính như Malware, Firewall, IDS/IPS; các vấn đề về mã hoá thông tin, các thuật toán hash, MAC, RSA, quản lý khóa trong các giao thức truyền trên mạng.

# Tấn công mạng và phòng thủ Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học cung cấp cho sinh viên chuyên ngành Công nghệ Thông tin kiến thức cơ bản về kỹ thuật Tấn công Mạng và Bảo vệ hệ thống mạng trước các loại tấn công; các vấn đề về mã hoá thông tin, các thuật toán hash, MAC, RSA, quản lý khóa trong các giao thức truyền trên mạng.

# Thiết kế mạng

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung cấp kiến thức về những đặc điểm cơ bản khi thiết kế một hệ thống mạng;kiến thức về quy trình các giai đoạn thiết kế mạng, phương pháp thiết kế theo mô hình phân lớp; kiến thức về thiết kế mạng LAN, WLAN, WAN; và thiết kế mạng đảm bảo tính bảo mật, tính sẵn sàng của hệ thống.

# An ninh mạng

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung cấp kiến thức về các kỹ thuật an ninh mạng; kiến thức về các kỹ thuật và công cụ phân tích các lỗ hổng trong hệ thống mạng; các kỹ thuật tấn công mạng; các giao thức bảo mật và kỹ thuật bảo mật ứng dụng mạng; các kỹ thuật bảo mật hạ tầng mạng như Firewall, IDS/IPS.

# Hệ thống nhúng



Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này cung cấp cho người học những kiến thức liên quan tới hệ thống nhúng, bao gồm: Những khái niệm tổng quan về mô hình hệ thống nhúng, tính chất, các ứng dụng của hệ thống nhúng; Các thành phần cơ bản của một hệ thống nhúng; Các phương pháp thiết kế hệ thống nhúng; Vi điều khiển ARM; Tập lệnh của vi điều khiển ARM; Kiến thức về nguyên tắc lập trình nhúng, các công cụ lập trình phần mềm nhúng.

# Lý thuyết thông tin

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần cung cấp cho người học những kiến thức cơ bản của lý thuyết thông tin, bao gồm: Độ đo lượng tin (Measure of Information); Sinh mã tách được (Decypherable Coding); Kênh truyền tin rời rạc không nhớ (Discrete Memoryless Channel); Sửa lỗi kênh truyền (Error Correcting Coding).

Hệ thống giám sát an toàn mạng Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung cấp kiến thức về các thành phần trong hệ thống giám sát mạng; kiến thức về phương pháp tổ chức triển khai một hệ thống giám sát, các giao thức dùng trong giám sát mạng; kiến thức về các công cụ trong giám sát, các hình thức cảnh báo khi hệ thống mạng có sự cố xảy ra.

An toàn mạng không dây và di động Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Học phần này cung cấp cho người học những kiến thức liên quan tới: kênh truyền thông không dây, kiến trúc và các giao thức mạng không dây, tấn công trên mạng không dây, các kỹ thuật bảo vệ.



# Quản trị trên môi trường cloud

Mô tả học phần:

Môn học này cung cấp kiến thức về công nghệ cloud và triển khai cài đặt, cấu hình, quản trị trên môi trường cloud. Trong đó bao gồm việc triển khai các máy ảo, cài đặt các ứng dụng và dịch vụ trên cloud, quản trị tài nguyên, giám sát các hoạt động của hệ thống trên môi trường cloud.

# Pháp lý kỹ thuật số

Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học cung cấp cho sinh viên những nguyên lý và kỹ thuật trong lĩnh vực pháp lý số. Sinh viên sẽ được cung cấp những kiến thức và qui trình thu thập chứng cứ trên Linux và Windows; kiến thức xây dựng và phân tích được các báo cáo pháp lý số.

# Chuyên đề 3 (Internet kết nối vạn vật - IoT) Cấu trúc học phần: 3(2:1:6)

Mô tả học phần:

Môn học này cung cấp cho người học những kiến thức liên quan tới Hệ thống IoT, cụ thể là: các khái niệm liên quan và kiến trúc hệ thống IoT, kiến trúc hệ thống IoT, chồng giao thức cho IoT, các thành phần hardware, software, một số platform cho hệ thống IoT, công nghệ RFID, sensor...

# Chuyên đề doanh nghiệp (CNTT)

Cấu trúc học phần: 2(2:0:4)

Mô tả học phần:

Môn học này trang bị cho sinh viên các kiến thức cập nhật thực tế về các công nghệ mới trong lĩnh vực công nghệ thông tin, cũng như một số kiến thức về kỹ năng mềm, kỹ năng làm việc trong môi trường doanh nghiệp, dưới hình thức chuyên đề khách mời – là những chuyên gia có kinh nghiệm làm việc trong các doanh nghiệp.

# Thực tập tốt nghiệp (CNTT)

Cấu trúc học phần: 2(2:0:4)



Mô tả học phần:

Môn học này trang bị cho sinh viên các kiến thức thực tế liên quan tới môi trường làm việc tại doanh nghiệp, sử dụng kiến thức đã học trong việc tham gia các dự án thực tế tại doanh nghiệp, hoặc tiếp thu một số công nghệ mới và vận dụng chúng trong việc triển khai, vận hành hệ thống công nghệ thông tin. Đồng thời qua việc thực tập sinh viên có thể phát triển tư duy trong tương lai với vai trò quản lý.

# Lãnh đạo và kinh doanh trong kỹ thuật (CNTT) Cấu trúc học phần: 0(0:0:0)

Mô tả học phần:

Học phần giúp sinh viên hình thành tư duy sáng tạo và truyền đạt, trang bị kỹ năng xây dựng, lãnh đạo tổ chức, quản lý dự án. Trang bị cho sinh viên kỹ năng làm việc nhóm, kỹ năng phát triển ý tưởng mới. Cung cấp các kiến thức về việc thành lập, quản lý doanh nghiệp và tiếp thị sản phẩm, quản lý sở hữu trí tuệ.

# Public_003


Dịch máy là một trong những hướng nghiên cứu quan trọng trong xử lý ngôn ngữ tự nhiên. Trong những năm gần đây, dịch máy nơ ron đã và đang được nghiên cứu phổ biến hơn trong cộng đồng dịch máy vì hiện tại nó cho chất lượng dịch tốt hơn so với phương pháp dịch máy thống kê truyền thống. Tuy nhiên, dịch máy nơ ron lại cần lượng lớn dữ liệu song ngữ để huấn luyện. Hệ dịch sẽ cho chất lượng bản dịch tốt hơn khi nó được thử nghiệm trong cùng miền với miền dữ liệu mà nó được huấn luyện, ngược lại thì chất lượng bản dịch sẽ bị sụt giảm, mức độ sụt giảm phụ thuộc vào mức độ khác biệt giữa dữ liệu miền huấn luyện và dữ liệu miền thử nghiệm. Hiện nay, các kĩ thuật thích ứng miền cho dịch máy nơ ron đã được công bố chủ yếu được thực hiện trên một số cặp ngôn ngữ phổ biến giàu tài nguyên, và chưa có nhiều nghiên cứu đã được công bố về thích ứng miền trong dịch máy nơ ron cho cặp ngôn ngữ Anh - Việt.

Trong bài báo này, chúng tôi đề xuất một phương pháp thích ứng miền mới cho dịch máy nơ ron, áp dụng cho cặp ngôn ngữ Anh - Việt. Ý tưởng chính của bài báo là kết hợp dữ liệu đơn ngữ ngoài miền ở ngôn ngữ nguồn (tiếng Anh) với bản dịch của nó ở ngôn ngữ đích (tiếng Việt) để làm dữ liệu huấn luyện hệ dịch. Các thực nghiệm đã chứng minh rằng phương pháp chúng tôi đề xuất dễ thực hiện, khai thác được những ưu điểm của dữ liệu đơn ngữ như luôn có sẵn, chi phí xây dựng thấp và đặc biệt là chất lượng của hệ dịch được và tăng 2,21 điểm BLEU trong thử nghiệm của chúng tôi.

# 1. Nội dung chính

# 1.1 GIỚI THIỆU

Mục tiêu của dịch máy là nghiên cứu các phương pháp, kĩ thuật để xây dựng được một hệ thống có thể dịch tự động các câu từ một ngôn ngữ tự nhiên này sang ngôn ngữ khác, đây là một trong những hướng nghiên cứu quan trọng trong trí tuệ nhân tạo, đặc biệt trong xử lý ngôn ngữ tự nhiên. Dịch máy là một nhánh nhỏ của xử lý ngôn ngữ tự nhiên, và vì xử lý ngôn ngữ tự nhiên là lĩnh vực liên ngành giữa khoa học máy tính và ngôn ngữ học, chính đặc điểm đó nên các nghiên cứu về dịch máy có thể chia thành hai nhóm phương pháp chính là các phương pháp dựa trên luật và các phương pháp dựa trên ngữ liệu. Trong số đó, các phương pháp dựa trên ngữ liệu có thể được chia thành các phương pháp dựa trên thống kê và các phương pháp dựa trên ví dụ. Trong những năm gần đây, với sự phát triển của internet, dịch máy đã đạt được những kết quả tốt cả về học thuật và trong công nghiệp.

Gần đây, các nghiên cứu về dịch máy đã dịch chuyển dần từ các phương pháp dịch thống kê (Statistical Machine Translation) sang dịch máy nơ ron (Neural Machine Translation), hiện tại đây được coi là một hệ dịch cho chất lượng dịch vượt trội so với các phương pháp truyền thống trước đây. Tuy nhiên, các hệ dịch nơ ron lại yêu cầu nhiều dữ liệu song ngữ hơn để huấn luyện hệ dịch, điều này ít ảnh hưởng tới chất lượng bản dịch của hệ dịch dành cho các cặp ngôn ngữ phổ biến và giàu tài nguyên nhưng nó lại là thách thức lớn đối với các cặp ngôn ngữ có ít tài nguyên.



Thông thường, hệ dịch được huấn luyện trên lượng lớn dữ liệu song ngữ và dữ liệu đơn ngữ của ngôn ngữ đích đối với dịch máy thống kê và dữ liệu song ngữ đối với dịch máy nơ ron, trong bản thân những dữ liệu huấn luyện này có thể bao gồm các chủ đề đồng nhất hoặc không đồng nhất và thường thì mỗi chủ đề đó sẽ có tập các từ thuật ngữ riêng biệt. Chất lượng của bản dịch phụ thuộc rất lớn vào dữ liệu huấn luyện, nếu miền dữ liệu huấn luyện và miền thử nghiệm giống nhau hoặc có sự tương đồng càng lớn thì chất lượng bản dịch thu được sẽ càng tốt so với việc miền dữ liệu dùng để huấn luyện và miền thử nghiệm dặc biệt khác nhau hoặc có ít sự tương đồng hơn. Ví dụ, nếu hệ dịch được huấn luyện với dữ liệu thuộc miền tin tức thì khi dịch các văn bản cũng thuộc miền tin tức sẽ cho chất lượng bản dịch tốt, nhưng nếu đem hệ dịch đó để dịch các văn bản thuộc miền khác với miền tin tức như miền y tế, tin học, luật, v.v... thì chất lượng của bản dịch sẽ bị giảm đột ngột, mức độ giảm tùy thuộc vào mức độ tương đồng của miền dữ liệu dùng để huấn luyện hệ dịch so với miền dữ liệu dùng để thử nghiệm.

Các miền dữ liệu song ngữ trong thực tế thường rất hiếm hoặc bị giới hạn về số lượng, đặc biệt đối với các cặp ngôn ngữ ít phổ biến như ngôn ngữ Anh - Việt, nhất là các miền dữ liệu đặc thù. Để đạt được chất lượng bản dịch tốt nhất thì dữ liệu huấn luyện phải thuộc cùng một miền, cùng một thể loại và cùng một phong cách với miền mà hệ dịch được áp dụng nhưng tế để có được lượng dữ liệu huấn luyện đủ lớn trong mỗi miền mà thỏa mãn những đặc điểm trên là rất khó, hoặc cần phải trả một chi phí rất lớn để xây dựng dữ liệu huấn luyện. Vì vậy, trong bài báo này chúng tôi trình bày một phương pháp thích ứng miền mới cho dịch máy nơ ron, áp dụng cho cặp ngôn ngữ Anh - Việt với chiều dịch từ tiếng Anh sang tiếng Việt. Các thử nghiệm được tiến hành trên hai miền dữ liệu là miền tổng quan và miền pháp lý, chất lượng dịch trên miền tổng quan làm cơ sở để so sánh, đánh giá chất lượng hệ dịch khi được áp dụng trong miền pháp lý cũng như đánh giá hiệu quả của phương pháp được đề xuất. Qua thử nghiệm cho thấy, phương pháp này dễ thực hiện, tận dụng được lượng lớn dữ liệu đơn ngữ luôn có sẵn với chi phí thấp và khả quan khi đã cải tiến được chất lượng bản dịch tăng 2,21 điểm BLEU [6] (từ 22,17 điểm lên 24,38 điểm).

Bài báo này được trình bày cấu trúc như sau: Tiếp theo, phần 2 sẽ giới thiệu các nghiên cứu trước đây có liên quan; phần 3 trình bày tổng quan phương pháp chúng tôi đề xuất; phần 4 trình bày các thử nghiệm và các kết quả; phần 5 là kết luận và hướng phát triển; và cuối cùng phần 6 là một số tài liệu tham khảo.

# 1.2 CÁC NGHIÊN CỨU LIÊN QUAN

Những năm gần đây, thích ứng miền là một trong những chủ đề đã giành được rất nhiều sự quan tâm của các nhà khoa học trên thế giới. Hiện nay, đã có nhiều phương pháp được đề xuất để thích ứng cho dịch máy thống kê cũng như dịch máy nơ ron, nhưng các đề xuất đó chủ yếu áp dụng cho một số cặp ngôn ngữ phổ biến trên thế giới như Anh - Pháp, Anh - Nhật, Anh - Tây Ban Nha,... Các phương pháp đã đề xuất được công bố đều thuộc một trong ba hướng chính, đó là: (1) bổ sung thêm nhiều dữ liệu hơn; (2) các kĩ thuật để có dữ liệu chất lượng hơn và (3) các kĩ thuật để có mô hình chất lượng hơn. Với hướng tiếp cận (1) và (2), đã có nhiều công bố đề xuất sử dụng dữ liệu đơn ngữ để cải tiến chất lượng hệ dịch khi dịch trong miền mới, các đề xuất này chủ yếu đã được chứng minh bằng thực nghiệm trong dịch máy thống kê, và chưa có nhiều đề xuất đối với dịch máy nơ ron.



Trong [2], kỹ thuật thích ứng giữa các miền được đề xuất để áp dụng cho dịch máy thống kê dựa vào cụm từ về nhiệm vụ Europarl1 [3], để dịch các bình luận tin tức từ tiếng Pháp sang tiếng Anh. Cụ thể, một phần nhỏ dữ liệu song ngữ miền được khai thác để thích ứng mô hình ngôn ngữ và mô hình dịch bằng kỹ thuật nội suy tuyến tính. Việc thích ứng các mô hình dịch, mô hình đảo trật tự từ được thực hiện qua việc sinh thêm dữ liệu song ngữ từ dữ liệu đơn ngữ.

Công bố [9] đã đề xuất một số phương pháp thích ứng khá phức tạp dựa trên việc bổ sung thêm dữ liệu song ngữ được tổng hợp từ các tập dữ liệu dùng để tối ưu tham số và thử nghiệm. Ngoài ra, trong [10], đề xuất một phương pháp nhằm khai thác nguồn tài nguyên dữ liệu đơn ngữ miền bằng cách tổng hợp dữ liệu song ngữ từ việc dịch dữ liệu đơn ngữ miền sang ngôn ngữ đích. Phương pháp này chủ yếu liên quan đến kĩ thuật được đề xuất trong [2] nhưng khác nhau ở dữ liệu dùng để thích ứng miền, cụ thể ở [10] chỉ sử dụng dữ liệu đơn ngữ miền.

Các đề xuất trên được công bố cho dịch máy thống kê. Tuy nhiên, năm 2016 có công bố [11] đã đề xuất thích ứng miền cho dịch máy nơ ron dựa vào sinh dữ liệu song ngữ cho hệ dịch bằng việc dịch ngược các dữ liệu đơn ngữ trong miền đích. Trong bài báo này, phương pháp chúng tôi đề xuất có phần giống với phương pháp [9] vì chúng tôi có sử dụng thêm một tập dữ liệu miền pháp lý để tối ưu tham số của hệ dịch cơ sở theo định hướng miền đích, nhưng cũng liên quan nhiều đến phương pháp được đề xuất trong [10] và [11].

Nhìn chung, các phương pháp về thích ứng miền nói chung cho dịch máy đã được công bố khá phức tạp, thử nghiệm công phu và sử dụng nhiều mô hình toán học. Tuy nhiên, các thử nghiệm mới chỉ áp dụng cho một số cặp ngôn ngữ phổ biến như Anh - Pháp, Anh - Nhật, Anh - Tây Ban Nha,... Hiện vẫn chưa có công bố nào áp dụng cho cặp ngôn ngữ Anh - Việt.

# 1.3 PHƯƠNG PHÁP ĐỀ XUẤT

# 1.3.1 Tổng quan về dịch máy nơ ron

Đối với phương pháp dịch máy truyền thống như dịch máy thống kê dựa vào cụm thì hệ dịch thực hiện phân tách câu nguồn thành nhiều từ hoặc cụm từ riêng biệt, sau đó dịch tuần tự từng từ hoặc cụm từ một rồi sắp xếp lại trật tự các từ theo đúng trật tự trong ngôn ngữ đích. Vì thế, nên bản dịch không được trôi chảy và các dịch này không giống như cách con người dịch, để dịch, chúng ta sẽ đọc trọn vẹn một câu nguồn, hiểu ý nghĩa của nó rồi mới tiến hành dịch câu đó sang ngôn ngữ đích. Dịch máy nơ ron thực hiện dịch tương tự như cách của con người.



![](images/image1.jpg)
Hình 1. Kiến trúc Encoder - Decoder

Cụ thể, đầu tiên hệ dịch nơ ron sử dụng bộ mã hóa (Encoder) để đọc toàn bộ câu nguồn và mã hóa nó dưới dạng một vectơ biểu diễn ý nghĩa. Sau đó, bộ giải mã (Decoder) sẽ đọc và giải mã vec tơ biểu diễn câu nguồn này để sinh ra bản dịch tương ứng sang ngôn ngữ đích, quá trình mã hóa - giải mã được minh họa như ở hình 1 và hình 2 [5]. Theo cách dịch này, hệ dịch nơ ron có thể giải quyết được vấn đề dịch cục bộ trong phương pháp dịch dựa vào cụm truyền thống, đó là: nó có thể nắm bắt được các phụ thuộc xa hơn trong các ngôn ngữ và tạo ra các bản dịch trôi chảy hơn nhiều so với hệ dịch thống kê dựa vào cụm truyền thống.

Bộ mã hóa - Bộ mã hóa đọc câu nguồn $X = ( x I , x 2 , . . . , x T )$ và chuyển đổi nó thành một chuỗi các trạng thái ẩn $h = ( h I , h 2 , . . . , h T )$ sử dụng mạng nơ ron hồi quy hai chiều (bi-directional RNN). Tại mỗi thời điểm t, trạng thái ẩn ht được xác định như là một kết hợp các trạng thái ẩn của mạng nơ ron hồi quy theo chiều xuôi (forward RNN) và theo chiều ngược

Bộ giải mã - Bộ giải mã sử dụng mạng nơ ron hồi quy khác để sinh ra bản dịch $\boldsymbol { Y } = ( y I , y 2 , . . . , y T ^ { \prime } ) .$ dựa trên các trạng thái ẩn h được sinh bởi bộ mã hóa. Tại mỗi thời điểm i, xác suất có điều kiện của mỗi từ yi trong tập từ vựng $V y$ của ngôn ngữ đích được tính bởi công thức:

$$
P ( y i | y { < } i , h ) { = } g ( y i { - } I , z i , c i ) ,
$$

với điều kiện zi là trạng thái ẩn ith của bộ giải mã, và được tính dựa vào trạng thái ẩn trước zi-1, từ trước yi-1 và vectơ ngữ cảnh nguồn ci: $Z i = R N N ( z i - { I } , y i - { I } , c i ) .$ .



# Phương pháp đề xuất

Trong thực tế, dữ liệu song ngữ thường không có sẵn, đặc biệt đối với các miền dữ liệu thuộc các lĩnh vực, chuyên ngành đặc thù, còn nếu muốn xây dựng dữ liệu song ngữ cho từng miền thì chi phí phải trả sẽ rất cao nhưng dữ liệu đơn ngữ thì lại luôn có sẵn với bất cứ miền dữ liệu nào. Trong dịch máy, dữ liệu đơn ngữ thường được dùng để làm mịn câu, khiến bản dịch của câu trôi chảy hơn và đọc lên thấy tự nhiên nhất. Dữ liệu đơn ngữ cũng đã được chứng minh có nhiều lợi ích trong việc cải tiến chất lượng dịch của cả hệ dịch máy thống kê và dịch máy nơ ron, đặc biệt trong nhiệm vụ thích ứng trong trường hợp nguồn tài nguyên bị hạn chế, nguồn dữ liệu song ngữ không đủ lớn. Hiện nay, cũng đã có một số đề xuất sử dụng dữ liệu đơn ngữ cho việc cải tiến chất lượng dịch, trong đó có đề xuất sinh dữ liệu song ngữ từ dữ liệu đơn ngữ cho dịch máy nhưng chưa có đề xuất, thử nghiệm hay khảo sát nào được công bố về sử dụng dữ liệu đơn ngữ để thích ứng miền áp dụng cho cặp ngôn ngữ Anh – Việt.

Như đã trình ở phần 2, phương pháp chúng tôi đề xuất có liên quan tới các công bố [9]; [10] và [11]. Theo [11], để sinh dữ liệu song ngữ thì việc dịch theo chiều ngược là cũng một giải pháp để có thể tận dụng được nguồn dữ liệu đơn ngữ miền. Để dịch theo chiều ngược hay theo chiều xuôi thì khá đơn giản và dễ áp dụng vì nó không yêu cầu phải thay đổi các thuật toán huấn luyện của hệ dịch.

Xuất phát từ ý tưởng trên, chúng tôi đề xuất một phương pháp mới để sinh dữ liệu song ngữ cho nhiệm vụ thích ứng miền áp dụng cho cặp ngôn ngữ Anh - Việt với chiều dịch từ Anh sang Việt, phương pháp của chúng tôi chỉ sử dụng dữ liệu đơn ngữ trong miền đích của ngôn ngữ đích. Phương pháp của chúng tôi khác với công bố trong [9]; [10] vì các công bố này chỉ thực nghiệm, áp dụng cho dịch máy thống kê dựa vào cụm còn phương pháp của chúng tôi là áp dụng cho dịch máy nơ ron. Ngoài ra, công bố [11] cũng khá liên quan tới phương pháp của chúng tôi khi cũng áp dụng cho dịch máy nơ ron, nhưng sử dụng kĩ thuật dịch ngược. Còn phương pháp của chúng tôi, cùng với các thử nghiệm, đánh giá hệ dịch dựa trên cách dịch xuôi dữ liệu đơn ngữ trong miền đích của ngôn ngữ đích. Phương pháp chúng tôi đề xuất được mô tả như hình 3, $\mathrm { g } \dot { \mathsf { o } } \mathrm { m } 3$ giai đoạn:

• Giai đoạn 1: Giai đoạn này chúng tôi sử dụng dữ liệu song ngữ Anh – Việt thuộc miền tổng quan để huấn luyện một hệ dịch nơ ron làm cơ sở để so sánh, đánh giá hiệu quả của phương pháp chúng tôi đề xuất (đặt tên là Baseline NMT như mô tả trong Hình 3 , trong các thử nghiệm gồm các hệ dịch Baseline_L và Baseline_G);
Giai đoạn 2: Sau khi đã có hệ dịch Baseline NMT ở giai đoạn 1, chúng tôi sử dụng hệ dịch này để dịch các văn bản đơn ngữ thuộc miền pháp lý trong tiếng Anh sang ngôn ngữ đích là tiếng Việt;
• Giai đoạn 3: Sau khi có kết quả dịch ở giai đoạn 2, chúng tôi sử dụng kết quả dịch này kết hợp với các văn bản đơn ngữ bằng tiếng Anh $\dot { \mathbf { O } }$ giai đoạn 2



để huấn luyện một hệ dịch nơ ron khác (đặt tên là Adaptation NMT như mô tả trong Hình 3, trong các thử nghiệm là hệ dịch Adapt_System), hệ dịch này được sử dụng để cải tiến chất lượng dịch của các văn bản thuộc miền pháp lý.

Bằng thực nghiệm, các kết quả so sánh thông qua cách đánh giá bằng điểm BLEU [6] đã chỉ ra rằng phương pháp chúng tôi đề xuất là cách tiếp cận khả quan, dễ thực hiện và đã cho kết quả dịch cải tiến hơn so với hệ dịch cơ sở ban đầu.

# 1.4 THỰC NGHIỆM VÀ KẾT QUẢ

Để so sánh, đánh giá phương pháp đề xuất, chúng tôi tiến hành huấn luyện ba hệ dịch nơ ron, lần lượt là (1) Baseline_G - là hệ dịch cơ sở được huấn luyện với tập dữ liệu huấn luyện và tập tối ưu tham số (tập dữ liệu G_train và tập dữ liệu G_val) cùng thuộc miền tổng quan; (2) Baseline_L - là hệ dịch được huấn luyện với tập dữ liệu huấn luyện thuộc miền tổng quan (G_train), còn tập tối ưu tham số thuộc miền luật $( L _ { _ { \overline { { \lambda } } } } \nu a l ) _ { _ { 1 } }$ ; (3) Adapt_System - là hệ dịch được huấn luyện với dữ liệu song ngữ được tổng hợp $\dot { \mathbf { O } }$ giai đoạn 2 của hình 3 và dữ liệu tối ưu tham số thuộc miền luật $( L \_ { v a l } )$ .

Tiếp theo, chúng tôi sẽ mô tả về các tập dữ liệu, các bước tiền xử lý đối với dữ liệu huấn luyện của từng hệ dịch trên, đồng thời chúng tôi cũng trình bày cụ thể các bước thực nghiệm và kết quả tương ứng.

# 1.4.1 Dữ liệu

Để huấn luyện hệ dịch, trong các thử nghiệm của chúng tôi có hai loại dữ liệu miền khác nhau, ở góc độ bài toán mà chúng tôi giải quyết đó là tận dụng dữ liệu đơn ngữ thuộc miền cần dịch và một hệ dịch có sẵn thuộc miền tổng quan để nâng cao chất lượng dịch theo miền (miền pháp lý trong các thực nghiệm của chúng tôi). Để thống nhất, chúng tôi gọi dữ liệu thuộc miền tổng quan để huấn luyện hệ dịch là dữ liệu trong miền và dữ liệu không thuộc miền huấn luyện là dữ liệu ngoài miền.

# Thống kê dữ liệu

a) Dữ liệu trong miền: Chúng tôi sử dụng tập dữ liệu được cung cấp bởi hội nghị IWSLT $2 0 1 5 ^ { 2 } .$ , tập dữ liệu này thuộc miền tổng quan gồm 131.000 cặp câu song ngữ tiếng Anh - tiếng Việt dành cho nhiệm vụ về dịch máy, tập dữ liệu này

được gọi là tập G_train và được sử dụng để huấn luyện các hệ dịch cơ sở (Baseline_G và Baseline_L). Để tối ưu các tham số của hệ dịch trong miền tổng quan, chúng tôi sử dụng tập dữ liệu gồm 745 cặp câu song ngữ thuộc miền tổng quan và gọi là tập G_val. Để đánh giá chất lượng của các hệ dịch khi dịch trong miền tổng quan, chúng tôi sử dụng 1.046 cặp câu song ngữ Anh – Việt thuộc miền tổng quan.



b) Dữ liệu ngoài miền: Chúng tôi sử dụng 100.000 câu đơn ngữ tiếng Anh thuộc miền pháp lý và dùng hệ dịch cơ sở Basline_NMT theo mô tả ở giai đoạn 2 của hình 3 để dịch nhằm tạo ra bản dịch gồm 100.000 câu tiếng Việt tương ứng. Để đánh giá chất lượng của các hệ dịch trong miền pháp lý, chúng tôi sử dụng 2.000 cặp câu song ngữ Anh - Việt cùng thuộc miền pháp lý.

# Tiền xử lý dữ liệu

Tiền xử lý dữ liệu là bước xử lý không thể thiếu trong các bài toán dịch. Sau khi thu thập được đầy đủ các tập dữ liệu, chúng tôi tiến hành chuẩn hóa. Đầu tiên, chúng tôi thực hiện tách từ trong văn bản, đối với văn bản tiếng Anh thì cần quan tâm tới việc tách các dấu ". , ’ ; ? " và các kí tự đặc biệt khác ra khỏi các từ trong văn bản. Để thực hiện việc này, chúng tôi sử dụng công cụ tách từ Tokenizer có sẵn trong hệ dịch mã nguồn mở Moses [4] do Koehn và cộng sự phát triển (2007). Đối với tiếng Việt, vì dấu cách không phải là dấu hiệu để phân biệt các từ, mà một từ trong tiếng Việt được cấu tạo bởi một hoặc nhiều âm tiết. Chính vì vậy, để tiến hành tách từ cho văn bản tiếng Việt, chúng tôi sử dụng công cụ tách từ dành riêng cho tiếng Việt khá phổ biến là VnTokenizer [1].

Sau đó, chúng tôi thực hiện chuyển tất cả các kí tự hoa trong các tập dữ liệu về dạng kí tự thường và loại bỏ những cặp câu có độ dài quá lớn trong dữ liệu, trong các thực nghiệm này chúng tôi chỉ chọn những câu có độ dài nhỏ hơn 80.

# Các thực nghiệm

Để huấn luyện các hệ dịch nơ ron, chúng tôi sử dụng công cụ OpenNMT3 [7], đây là hệ dịch mã nguồn mở hoàn thiện, nổi tiếng, được công bố năm 2017 của nhóm Harvard NLP và SYSTRAN, công cụ này được nhiều người nghiên cứu trong cộng đồng dịch máy sử dụng. Các hệ dịch được huấn luyện với cùng các tham $\mathrm { s } \hat { \hat { 0 } } \mathrm { \ m } \breve { \mathrm { a c } }$ định, bao gồm hai tầng mạng LSTM với 500 nút ẩn và có sử dụng mô hình attention theo kiến trúc của Thang Luong [8]. Để so sánh, đánh giá chất lượng của các hệ dịch với nhau, chúng tôi sử dụng cách đánh giá tự động dựa vào điểm BLEU [6], đây cũng là cách đánh giá phổ biến trong bài toán dịch máy. Như mô tả ở hình 3:

Giai đoạn 1: Chúng tôi huấn luyện các hệ dịch cơ sở Baseline NMT, các hệ dịch này được huấn luyện với dữ liệu song ngữ thuộc miền tổng quan, nhưng được tối ưu tham số trong các miền dữ liệu khác nhau, cụ thể:

Hệ dịch Baseline_G: Sử dụng tập dữ liệu G_train và G_val (mô tả trong bảng 1) để huấn luyện, hệ dịch cơ sở này được huấn luyện với dữ liệu song ngữ và tối ưu các tham số trong cùng một miền tổng quan.



Hệ dịch Baseline_L: Sử dụng tập dữ liệu G_train và L_val (mô tả trong bảng 1) để huấn luyện, hệ dịch cơ sở này được huấn luyện với dữ liệu song ngữ thuộc miền tổng quan nhưng các tham số của hệ dịch được tối ưu trong miền pháp lý.

Việc lựa chọn hệ dịch có chất lượng bản dịch tốt, để từ đó tiến hành dịch xuôi và tổng hợp được dữ liệu song ngữ có chất lượng tốt. Chúng tôi tiến hành đánh giá, so sánh chất lượng bản dịch của hai hệ dịch cơ sở này khi dịch trong cùng một miền dữ liệu tổng quan và miền dữ liệu pháp lý. Kết quả thử nghiệm được đánh giá thông qua điểm BLEU được thể hiện như bảng 2. Ở bảng 2, ta thấy:

Khi dịch với cùng tập dữ liệu là G_test thuộc miền tổng quan, hệ dịch Baseline_G cho điểm BLEU $= 2 9 \overline { { , 3 } } 4$ trong khi Baseline_L có điểm BLEU $= 2 9 { , } 5 6$ .
Khi dịch với cùng tập dữ liệu L_test thuộc miền pháp lý thì hệ dịch Baseline_G cho điểm BLEU $= 2 2 , 1 7$ và hệ dịch Baseline_L cho điểm $\mathrm { B L E U } = \overline { { 2 } } 3 \mathrm { , 0 1 }$ .

Như vậy, khi hệ dịch cơ sở Baseline_L được tối ưu tham số trong miền pháp lý đã cải tiến được chất lượng của bản dịch khi dịch trong miền pháp lý, cụ thể đã tăng 0.84 điểm BLEU (điểm $B L E U = 2 3 , 0 I$ so với 22,17 của hệ dịch Baseline_G). Căn cứ vào kết quả so sánh này, chúng tôi lựa chọn hệ dịch cơ sở Baseline_L để thực hiện các bước trong giai đoạn 2.

Giai đoạn 2: Chúng tôi dùng hệ dịch Baseline_L ở trên để dịch tập dữ liệu đơn ngữ gồm 100.000 câu tiếng Anh thuộc miền pháp lý sinh ra bản dịch tương ứng gồm 100.000 câu tiếng Việt.



Giai đoạn 3: Chúng tôi sử dụng cặp dữ liệu đơn ngữ ở giai đoạn 2 (gồm 100.000 tiếng Anh và bản dịch của nó gồm 100.000 tiếng Việt) để huấn luyện hệ dịch Adapt_System, hệ dịch này được tối ưu tham số với tập dữ liệu L_val thuộc miền pháp lý. Các thử nghiệm cho kết quả điểm BLEU = 26,56 khi dịch tập dữ liệu G_test thuộc miền tổng quan, và điểm BLEU = 24,38 khi dịch tập dữ liệu L_test thuộc miền pháp lý.

Như vậy, hệ dịch Adapt_System cho chất lượng dịch trong miền pháp lý cao hơn so với các hệ dịch cơ sở Baseline_G và Baseline_L. Cụ thể, điểm BLEU cao hơn 2,21 điểm so với Baseline_G (cải tiến từ 22,17 điểm tăng lên 24,38 điểm) và cao hơn 1,37 điểm so với Baseline_L (cải tiến từ 23,01 điểm tăng lên 24,38 điểm). Các kết quả thử nghiệm được thể hiện trong bảng 2 và sự biến đổi về chất lượng của bản dịch được thể hiện như biểu đồ trong hình 4.

Các kết quả thử nghiệm đã cho thấy phương pháp mà chúng tôi đề xuất là cách tiếp cận khả quan, dễ thực hiện và đã cho kết quả dịch khi dịch trong miền pháp lý cải tiến hơn so với hệ dịch cơ sở ban đầu.

# 1.5 KẾT LUẬN

Trong bài báo này, chúng tôi đã đề xuất một phương pháp thích ứng miền mới cho dịch máy nơ ron, phương pháp này đặc biệt hiệu quả đối với các miền dữ liệu có ít tài nguyên của cặp ngôn ngữ Anh - Việt, trong các thử nghiệm của chúng tôi, chúng tôi sử dụng dữ liệu thuộc miền pháp lý. Qua thực nghiệm cho thấy, cách tiếp cận này là khả quan, dễ thực hiện và đã cho kết quả dịch có điểm BLEU tăng 2,21 điểm (từ 22,17 điểm lên 24,38 điểm). Như vậy, chất lượng dịch sau khi thích ứng đã có cải tiến hơn so với hệ dịch cơ sở ban đầu.

Trong tương lai, chúng tôi sẽ tiến hành thử nghiệm mở rộng thêm trên cả hai chiều dịch đối với một số miền dữ liệu khác, và khảo sát với các tình huống khi dữ liệu đơn ngữ theo miền có sự thay đổi về lượng thì chất lượng dịch của hệ thống lúc này sẽ thay đổi như thế nào, và lượng dữ liệu đơn ngữ này thay đổi như thế nào là vừa đủ đối với từng miền dữ liệu.

# 2. TÀI LIỆU THAM KHẢO

[1] Phuong-Le Hong, Huyen-Nguyen Thi Minh, Azim Roussanaly and Vinh-Ho Tuong (2008). A Hybrid Approach to Word Segmentation of Vietnamese Texts.In Proceedings of the 2nd International Conference on Language and Automata Theory and Applications, Springer, LNCS 5196.

[2] Philipp Koehn and Josh Schroeder. 2007. Experiments in domain adaptation for statistical machine translation. In Proceedings of the Second Workshop on Statistical



Machine Translation, pages 224–227, Prague, Czech Republic. [3] Philipp Koehn. 2002. Europarl: A multilingual corpus for evaluation of machine translation. Unpublished, http://www.isi.edu/ $\sim$ koehn/europarl.

[4] P. Koehn, H. Hoang, A. Birch, C. Callison-Burch, M. Federico, N. Bertoldi, B. Cowan, W. Shen, C. Moran, R. Zens, C. Dyer, O. Bojar, A. Constantin, and E. Herbst. 2007. Moses: Open source toolkit for statistical machine translation. In Proceedings of the 45th Annual Meeting of the Association for Computational Linguistics Companion Volume Proceedings of the Demo and Poster Sessions, pages 177– 180, Prague, Czech Republic.

[5] Philipp Koehn. 2017. Neural machine translation. CoRR, abs/1709.07809.

[6] Kishore Papineni, Salim Roukos, Todd Ward, and WeiJing Zhu. 2002. BLEU: a method for automatic evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association of Computational Linguistics (ACL), pages 311– 318, Philadelphia, PA.

[7] Guillaume Klein, Yoon Kim, Yuntian Deng, Jean Senellart, Alexander M. Rush. 2017. OpenNMT: Open-Source Toolkit for Neural Machine Translation. Proceedings of AMTA 2018, vol. 1: MT Research Track.

[8] Minh-Thang Luong, Hieu Pham, and Christopher D Manning. 2015. Effective approaches to attention-based neural machine translation. EMNLP.

[9] Nicola Ueffing, Gholamreza Haffari, and Anoop Sarkar. 2007. Semi-supervised model adaptation for statistical machine translation. Machine Translation, 21(2):77– 94.

[10] Nicola Bertoldi, Marcello Federico. 2009. Domain Adaptation for Statistical

Machine Translation with Monolingual Resources. Proceedings of the 4th EACL Workshop on Statistical Machine Translation , pages 182–189.

[11] Rico Sennrich, Barry Haddow, and Alexandra Birch. 2016. Improving neural machine translation models with monolingual data. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 86–96, Berlin, Germany, August. Association for Computational Linguistics.

# Public_004


Ngành xây dựng không ngừng tìm kiếm những cách thức mới để nâng cao hiệu quả, nhiều công nghệ mới đã và đang được ứng dụng. Tuy nhiên, phương pháp xây dựng truyền thống vẫn không thay đổi trong nhiều thập kỷ qua, làm cho quá trình xây dựng kéo dài, không tối ưu nguồn lực dẫn đến giảm hiệu quả đầu tư xây dựng. Công nghệ in 3D là một công nghệ mới đầy hứa hẹn góp phần nâng cao hiệu quả đầu tư xây dựng và hạn chế tác động tiêu cực đến môi trường. Công nghệ in 3D sử dụng vật liệu bê tông là công nghệ có thể cho phép sản xuất cấu kiện kiến trúc, xây dựng mà không cần sử dụng ván khuôn, giúp mang lại nhiều lợi ích hơn so với phương pháp truyền thống. Trong khi công nghệ in 3D đã được áp dụng thành công trong một loạt các lĩnh vực như y tế, giáo dục, hàng không vũ trụ, ô tô v.v., thì ứng dụng của công nghệ này trong ngành xây dựng vẫn còn ở giai đoạn đầu. Trong vài năm qua, nhiều loại công nghệ in bê tông 3D khác nhau đã được phát triển và ứng dụng.

# 1. Nội dung chính

# 1.1 GIỚI THIỆU

Những thách thức trong ngành xây dựng hiện nay như tốc độ xây dựng chậm, quá trình thi công xây dựng gồm nhiều bước, mỗi bước đều tốn nhiều thời gian và công sức, công nghệ thi công hiện nay đang sử dụng nhiều nhân công lao động và tình trạng mất an toàn lao động là rất đáng quan ngại, ngoài ra các phương pháp thi công xây dựng và vật liệu xây dựng hiện tại không thân thiện với môi trường. Toàn bộ quá trình xây dựng, bao gồm sản xuất chế tạo sẵn, vận chuyển vật liệu, thi công xây dựng trên công trường đã thải ra một lượng lớn khí nhà kính và tiêu thụ một lượng lớn năng lượng, gây ô nhiễm môi trường. Do đó vấn đề đặt ra là phải áp dụng những công nghệ tiên tiến trong ngành xây dựng, trong đó công nghệ in bê tông 3D đang cho thấy những ưu điểm rõ rệt.

Kể từ khi phát hiện ra bê tông hiện đại vào thế kỷ 19, nhiều nhà nghiên cứu đã tìm cách tự động hóa việc xây dựng sử dụng vật liệu bê tông. Nhiều công nghệ xây dựng sử dụng vật liệu bê tông đã được phát triển, như công nghệ bơm bê tông và công nghệ phụ gia. Một nỗ lực lớn gần đây đối với ngành xây dựng dựa trên ý tưởng mới là các kỹ thuật sản xuất bồi đắp. Sản xuất bồi đắp được định nghĩa là quy trình ghép các lớp vật liệu để tạo các vật thể từ dữ liệu mô hình số 3D, trái ngược với các phương pháp sản xuất trừ (như điêu khắc). Trong đó nổi bật là công nghệ in 3D sử dụng vật liệu bê tông.

Công nghệ in bê tông 3D đề cập đến một quy trình sản xuất bồi đắp tự động, trong đó các đối tượng in được tạo ra bằng cách liên kết các lớp vật liệu kế tiếp chồng lên nhau. Quá trình bắt đầu với việc tạo ra một mô hình 3D bằng phần mềm CAD (Computer Aided Design). Mô hình sau đó được nhập vào máy in bê tông 3D bằng định dạng tệp .STL



(Stereolithography Language) là định dạng tệp phổ biến hiện nay, từ đây mô hình được chia thành các lớp có thể liên kết với nhau để tạo thành đối tượng in 3D. Trong những năm gần đây, công nghệ in bê tông 3D đã nhận được rất nhiều sự chú ý từ ngành xây dựng như một phương pháp thi công xây dựng đầy triển vọng. Công nghệ in bê tông 3D giúp tiết kiệm thời gian, vật liệu, nhân công bằng cách giảm hao hụt vật liệu, hạn chế hoặc không sử dụng ván khuôn từ đó giúp giảm chi phí. Ngoài ra, công nghệ này cũng hạn chế việc sao chép, giúp các nhà thiết kế có thể làm cho công trình trở có tính chất riêng so với các công trình khác.

Hiện nay việc áp dụng công nghệ in bê tông 3D trong ngành xây dựng vẫn gặp nhiều rào cản nhất định như còn nhiều hạn chế về mặt công nghệ, chi phí đầu tư cũng như chất lượng của các sản phẩm được chế tạo bằng công nghệ này.

Tuy nhiên, với sự phát triển của khoa học công nghệ, việc áp dụng các tiến bộ khoa học công nghệ trong ngành xây dựng là tất yếu. Trong đó, việc áp dụng công nghệ in bê tông 3D trong xây dựng có thể giải quyết những vấn đề nan giải hiện nay của ngành xây dựng. Bài báo giới thiệu các công nghệ in bê tông 3D và so sánh tính khả thi của các công nghệ này ứng dụng trong ngành xây dựng Việt Nam.

# 1.2 TỔNG QUAN

Ứng dụng của công nghệ in bê tông 3D trong ngành xây dựng là để chế tạo các cấu kiện kiến trúc, xây dựng. Mặc dù việc ứng dụng công nghệ in bê tông 3D vẫn còn ở giai đoạn đầu, tuy nhiên những nỗ lực nhằm đưa công nghệ này ứng dụng có hiệu quả hơn trong ngành xây dựng đã và đang được thực hiện trên toàn thế giới. Công nghệ in bê tông 3D là một công nghệ mới, nhằm mục đích giảm thiểu thời gian của quá trình xây dựng bằng cách loại bỏ một số quy trình tốn thời gian của phương pháp truyền thống, giảm các chi phí thông qua việc giảm thiểu khối lượng phát sinh, giảm nhân công lao động, đồng thời dễ dàng tạo ra những cấu kiện có hình dạng phức tạp với độ chính xác cao mà khó có thể thực hiện được bằng phương pháp truyền thống, cải thiện tác động tiêu cực của ngành xây dựng lên môi trường. Công nghệ in bê tông 3D có khả năng chế tạo cấu kiện kiến trúc, xây dựng được thiết kế trước bằng cách liên kết các lớp vật liệu chồng lên nhau theo một quy tắc nhất định.

Hiện nay, việc ứng dụng công nghệ in bê tông 3D trong ngành xây dựng còn nhiều vấn đề nan giải. Các nghiên cứu trên thế giới đã chỉ ra một số rào cản về vấn đề này như khả năng làm việc của cấu kiện được sản xuất bằng công nghệ in bê tông 3D hiện nay còn nhiều hạn chế về khả năng chịu lực so với các phương pháp sản xuất cấu kiện bê tông truyền thống tính đến thời điểm hiện tại. Những thách thức hiện tại trong thương mại hóa công nghệ in bê tông 3D như thiếu tiêu chuẩn, chi phí đầu tư lớn, các cấu kiện được chế tạo chưa đảm bảo chất lượng. Tuy nhiên lợi ích của công nghệ này đối với ngành xây dựng là rất to lớn như hạn chế hao hụt vật liệu, giảm đáng kể nhân công, đồng thời giảm thời gian thi công xây dựng. Nhiều nghiên cứu cũng đề cập đến khả năng áp dụng của các công nghệ in bê tông 3D trong xây dựng như việc áp dụng công nghệ Contour Crafting trong thi công xây dựng và khẳng định công nghệ Contour Crafting là một trong số rất ít các công nghệ khả thi có thể áp dụng trong ngành xây dựng [1]. S. Lim và cộng sự đã sử dụng công nghệ in bê tông 3D trong việc sản xuất các cấu kiện xây dựng quy mô lớn và đánh giá lợi ích của công nghệ này so với công nghệ xây dựng truyền thống [2].



Các nghiên cứu về việc chế tạo, kiểm định vật liệu in và cấu kiện in đã được thực hiện trong nhiều năm qua, như đánh giá và sửa đổi chất lượng in, độ ổn định hình dạng của hỗn hợp vật liệu in [3], sử dụng các vật liệu in khác nhau để chế tạo và kiểm tra khả năng tạo ra các cấu kiện có cấu trúc phức tạp cũng như cường độ của sản phẩm được chế tạo bằng công nghệ in bê tông 3D [4], nghiên cứu tối ưu hóa vật liệu và máy in chế tạo các cấu kiện phù hợp để ứng dụng trong quy mô nhỏ, qua đó chứng minh công nghệ in bê tông 3D này không chỉ là một công cụ đầy hứa hẹn cho thiết kế kết cấu, mà còn là một công cụ tiềm năng cho thiết kế kiến trúc [5]. Phát triển phương pháp để tạo ra các cấu kiện dựa trên geopolyme được sử dụng trong các máy in 3D sử dụng kỹ thuật lắng đọng bột có bán trên thị trường cho các ứng dụng xây dựng [6].

Nhìn chung, các nghiên cứu trên đã chỉ ra một số phạm vi áp dụng, lợi ích, khả năng áp dụng cũng như rào cản của công nghệ in bê tông 3D trong ngành xây dựng trên thế giới.

# 1.3 CÁC CÔNG NGHỆ IN BÊ TÔNG 3D

Trong những năm qua, nhiều công nghệ in bê tông 3D khác nhau đã được phát triển để ứng dụng trong ngành xây dựng. Những công nghệ in bê tông 3D này chủ yếu dựa trên hai kỹ thuật chính, đó là kỹ thuật ép đùn (Extrusion-Based Technique) và kỹ thuật lắng đọng bột (Powder-Based Technique).

# Công nghệ in bê tông 3D dựa trên kỹ thuật ép đùn

Công nghệ in bê tông 3D dựa trên kỹ thuật ép đùn tương tự như phương pháp nóng chảy lắng đọng FDM (Fused Deposition Modelling). Theo đó, vật liệu in sẽ đi qua từ một đầu in được gắn trên cần trục hoặc cánh tay robot để in một đối tượng theo từng lớp vật liệu. Các công nghệ in bê tông 3D dựa trên kỹ thuật này tiêu biểu như:



# 1.3.1.1. \* Công nghệ Contour Crafting

Contour Crafting là một phương pháp của quy trình sản xuất nhiều lớp sử dụng polymer, bùn $\mathrm { g } \mathrm { \acute { o } m }$ , bê tông, và một loạt các vật liệu và hỗn hợp khác để xây dựng các vật thể quy mô lớn với bề mặt mịn. Những ưu điểm chính của công nghệ này là tốc độ chế tạo nhanh hơn và khả năng tích hợp với các phương pháp khác để lắp đặt các bộ phận như đường ống, dây điện và cốt thép. Công nghệ Contour Crafting cho ra sản phẩm có bề mặt hoàn thiện vượt trội và tốc độ sản xuất được tăng cường đáng $\mathrm { k } \mathring { \mathrm { e } }$ .

# 1.3.1.2. \* Công nghệ Concrete Printing

Công nghệ Concrete Printing đã được nghiên cứu và phát triển tại Đại học Loughborough ở Vương quốc Anh. Công nghệ này cũng sử dụng kỹ thuật dựa trên ép đùn và ở một mức độ nào đó tương tự như công nghệ Contour Crafting. Tuy nhiên, công nghệ Concrete Printing đã được phát triển cho phép kiểm soát tốt hơn cấu trúc của sản phẩm in. Ngoài ra, vật liệu được sử dụng trong in bê tông là bê tông cốt liệu sợi tổng hợp cường độ cao nên tính chất của vật liệu vượt trội so với các vật liệu được sử dụng trong công nghệ Contour Crafting [2].

# 1.3.1.3. \* Công nghệ Concrete On-Site 3D Printing

Công nghệ Contour Crafting và Concrete Printing ngoài những ưu điểm so với các công nghệ truyền thống thì vẫn tồn tại một số hạn chế như sự cần thiết phải sử dụng máy móc mới và tiên tiến, kích thước cốt liệu nhỏ (thường sử dụng vữa tổng hợp thay vì bê tông thông thường) và kích thước hạn chế của sản phẩm in (tức là kích thước của máy in 3D phải lớn hơn kích thước của phần tử được in). Để khắc phục những hạn chế này, một công nghệ mới là công nghệ Concrete On-Site 3D Printing, được phát triển tại TU Dresden, Đức. Ưu điểm chính của công nghệ này là tính linh hoạt hình học cao và ít phụ thuộc vào nhân công lành nghề [7].

Một trong những ưu điểm của công nghệ in bê tông 3D tại chỗ không chỉ là phát triển quy trình xây dựng tiên tiến hiệu quả về thời gian, lao động và tài nguyên mà còn làm cho quy trình mới có hiệu quả kinh tế trong khi đạt được sự chấp nhận rộng rãi hơn trong ngành xây dựng. Điều này đạt được bằng cách sử dụng các kỹ thuật sản xuất và xây dựng hiện có càng nhiều càng tốt và bằng cách điều chỉnh quy trình mới với các hạn chế của công trường xây dựng [7].



1.3.1.4. \* Công nghệ in bê tông 3D quy mô lớn sử dụng bê tông cường độ cao (Large-Scale 3DCP using Ultra-High Performance Concrete) Qua việc nghiên cứu những hạn chế của các công nghệ Contour Crafting và công nghệ Concrete Printing đã đề cập ở trên, một công nghệ mới đã được một nhóm nghiên cứu ở Pháp giới thiệu với quy mô áp dụng lớn, sử dụng bê tông cường độ cao (UHPC). Công nghệ này được phát triển dựa trên kỹ thuật ép đùn để in bê tông cường độ cao theo từng lớp thông qua một đầu in đùn được gắn trên cánh tay robot. Ưu điểm chính của công nghệ này là cho phép sản xuất cấu kiện với hình dạng phức tạp với quy mô lớn mà không cần ván khuôn [8].

# Công nghệ in bê tông 3D dựa trên kỹ thuật lắng đọng bột (Powder-based Technique)

Công nghệ in bê tông 3D dựa trên kỹ thuật lắng đọng bột là một quy trình chế tạo cộng điển hình khác tạo ra các cấu kiện với hình học phức tạp bằng cách lắng đọng chất lỏng kết dính một cách chọn lọc. Kỹ thuật này là một quy trình ngoài công trường được thiết kế để sản xuất các cấu kiện đúc sẵn. Một số công nghệ in bê tông 3D dựa trên kỹ thuật lắng đọng bột được liệt kê dưới đây.

1.3.2.5. \* Công nghệ in ba chiều (D-Shape) Công nghệ D-Shape được phát triển bởi Enrico Dini sử dụng kỹ thuật dựa trên kỹ thuật lắng đọng bột để làm cứng một lớp vật liệu quy mô lớn. Xi măng cát và magiê oxychloride (còn được gọi là xi măng Sorel) được sử dụng làm vật liệu xây dựng và chất kết dính tương ứng [9].

1.3.2.6. \* Công nghệ đối tượng mới (Emerging Objects) Công nghệ đối tượng mới (Emerging Objects) được phát triển ở Hoa Kỳ sử dụng kỹ thuật lắng đọng bột để làm cứng có chọn lọc một công thức hỗn hợp xi măng bằng cách lắng đọng một tác nhân liên kết.

1.3.2.7. \* Công nghệ in bê tông 3D dựa trên kỹ thuật lắng đọng bột sử dụng Geopolymer (Powder-based 3DCP using Geopolymer)

Công nghệ in bê tông 3D dựa trên kỹ thuật lắng đọng bột sử dụng Geopolymer có khả năng sản xuất các cấu kiện xây dựng với chi tiết và hình dạng phức tạp. Công nghệ dựa trên lắng đọng bột có tiềm năng để sản xuất các cấu kiện xây dựng với độ bền cao và tốc độ hợp lý để đáp ứng nhu cầu sản xuất quy mô công nghiệp [10].

# 1.4 KẾT LUẬN



Ưu điểm chính của công nghệ in ba chiều là sản phẩm tạo ra có kết cấu chắc chắn nhưng có nhược điểm là công nghệ này tốn nhiều công sức và rắc rối. Công nghệ Contour Crafting và Concrete Printing đều dựa trên kỹ thuật ép đùn, điều này làm cho chúng rất giống nhau, lợi thế của công nghệ Contour Crafting so với công nghệ Concrete Printing là độ mịn của bề mặt sản phẩm, tuy nhiên sản phẩm được sản xuất bằng công nghệ Concrete Printing có kết cấu chắc chắn hơn so với công nghệ Contour Crafting, nhưng sản phẩm sản xuất bằng công nghệ Concrete Printing lại có kích thước hạn chế hơn.

Dựa trên các phân tích ở trên, mặc dù công nghệ in bê tông 3D vẫn là một công nghệ mới nổi, khả năng ứng dụng trong xây dựng còn hạn chế, đặc biệt là đối với quy mô sản xuất tại chỗ trên công trường, nhưng với phát triển nhanh chóng của công nghệ này, việc in các cấu kiện bê tông ở quy mô lớn sẽ thành hiện thực trong tương lai gần.

# 2. TÀI LIỆU TRÍCH DẪN

[1]. P. Sharma, "Automated Construction by Contour Crafting," Journal of advance research in mechanical & civil engineering, 2015.

[2]. S. Lim, R. A. Buswell, T. T. Le, S. A. Austin, A. G. .. F. Gibb and T. Thorpe, "Developments in construction-scale additive manufacturing processes," Automation in construction, vol. 21, pp. 262-268, 2012.

[3]. A. Kazemian, X. Yuan, R. Meier and B. Khoshnevis, "Performance-based testing of Portland cement concrete for construction-scale 3D printing," 3D Concrete Printing Technology, pp. 13-35.

[4]. B. P, J. Scott Z, B. Isaiah R and P. Max A, "Towards the formulation of robust and sustainable cementitious binders for 3D additive construction by extrusion," 3D Concrete Printing Technology, pp. 307-331, 2019.

[5]. Z. Malaeb, F. AlSakka and F. Hamzeh, "3D concrete printing: machine design, mix proportioning, and mix comparison between different machine setups," 3D concrete printing technology, pp. 115-136, 2019.

[6]. B. Nematollahi, M. Xia, P. Vijay and J. G. Sanjayan, "Properties of extrusionbased 3D printable geopolymers for digital construction applications," 3D Concrete Printing Technology, pp. 371-388, 2019



[7]. N. V.N, K. M, N. M and M. V, CONPrint3D - 3D printing technology for onsite construction, Concrete in Australia, 2016.

[8]. Y. JunNam, Y. Kwang, H. Woon and P. MookLim, "Fiber-reinforced cementitious composite design with controlled distribution and orientation of fibers using threedimensional printing technology," 3D Concrete Printing Technology, pp. 59-72, 2019.

[9]. G. Cesaretti, E. Dini, X. Kestelier, V. Colla and L. Pambaguian, "Building components for an outpost on the Lunar soil by means of a novel 3D printing technology," Acta Astronautica, vol. 93, pp. 430-450, 2014.

[10]. M. Xia and J. Sanjayan, "Method of formulating geopolymer for 3D printing for construction applications," Materials & Design, vol. 110, pp. 382-390, 2016

# Public_005


Chuyển đổi số các cơ sở giáo dục đào tạo đang là một nhiệm vụ cấp bách và Học viện Ngân hàng cũng không nằm ngoài guồng quay của cuộc cách mạng công nghệ này. Để quá trình chuyển đổi số được thuận lợi thì quá trình số hóa dữ liệu cần được ưu tiên đẩy mạnh. Trong bài báo này, tác giả nghiên cứu những giải pháp phù hợp cho việc số hóa dữ liệu văn bản đã và đang lưu hành trong Học viện Ngân hàng. Cụ thể, tác giả giới thiệu các công nghệ cốt lõi trong số hóa tài liệu như Nhận dạng ký tự quang học, Xử lý văn bản thông minh, khảo sát các giải pháp tiêu biểu trên thị trường ở Việt Nam để lựa chọn giải pháp khả thi và tiến hành cài đặt thử nghiệm giải pháp FPT. AI Reader với bộ dữ liệu tự thu thập từ một số phòng ban tại Học viện. Kết quả thực nghiệm cho thấy tỷ lệ sai số $\acute { \sigma }$ mức từ đạt $27 \%$ và chỉ $16 \%$ từ bị sai ở các tiêu đề, đơn vị ban hành, loại văn bản. Giải pháp hoàn toàn có thể được nghiên

# 1. Nội dung chính

# 1.1 Đặt vấn đề

Thực hiện chuyển đổi số (CĐS) trong lĩnh vực giáo dục đào tạo là một trong những hoạt động nhận được nhiều sự quan tâm và ưu tiên của nhiều nước trên thế giới. Hoạt động CĐS trong lĩnh vực giáo dục không chỉ tập trung vào hoạt động dạy và học trong thay đổi phương pháp dạy và học mà còn diễn ra ở rất nhiều nghiệp vụ khác như phát triển hệ thống hỗ trợ hoạt động quản lý điều hành, quản lý hoạt động khoa học công nghệ. Trên cơ sở Quyết định số 131/ QĐ-TTg năm 2022 của Thủ tướng Chính phủ phê duyệt Đề án “Tăng cường ứng dụng công nghệ thông tin và chuyển đổi số trong giáo dục và đào tạo giai đoạn 2022-2025, định hướng đến năm 2030” (Thủ tướng Chính phủ, 2022), Học viện Ngân hàng cũng đã có những hành động thiết thực để thích ứng với bối cảnh phát triển chung của giáo dục đại học.

Liên quan đến chuyển đổi số, khá nhiều thuật ngữ với hậu tố “số” có thể gây nhầm lẫn, như “công nghệ số”, “kinh tế số”, “kỹ thuật số”. Đặc biệt thuật ngữ tiếng Anh cũng có những thuật ngữ gần giống nhau như Digitization, Digitalization, vậy vai trò của chúng đối với CĐS như thế nào? Theo Phạm Huy Giao (2020) quá trình CĐS bao gồm ba giai đoạn như Hình 1.

Theo đó, một tổ chức muốn thực hiện CĐS, trước hết cần trải qua giai đoạn đầu tiên: Số hóa (Digitization). Đây là quá trình chuyển đổi các thực thể trong quy trình hoạt động từ dạng vật lý sang dạng số, có thể lưu trữ và xử lý trên máy tính điện tử. Chẳng hạn hồ sơ của một nhân viên từ bản sơ yếu lý lịch trên giấy được lưu trữ thành các trường thông tin trong cơ sở dữ liệu như Họ tên, Ngày sinh, Quê quán. Các số liệu kinh doanh từ việc lưu cả tập hóa đơn, chứng từ và kiểm kê lại khi cần thì được tổ chức thành các bảng số liệu trong Microsoft Excel. Hay chỉ đơn giản là lưu trữ các tệp tin (file) trong máy tính chứa các dữ liệu hoạt động của tổ chức cũng có thể phần nào được coi là số hóa.



Tại Học viện Ngân hàng, một số phòng ban đã có phần mềm quản lý và vận hành khá ổn định. Chẳng hạn Phòng Đào tạo có phần mềm Quản lý đào tạo, phòng Quản lý người học thực hiện quản lý trên Cổng thông tin sinh viên, Phòng Quản trị có phần mềm MISA, Tạp chí Khoa học và Đào tạo Ngân hàng cũng sử dụng phần mềm quản lý bài viết trực tuyến. Điều này giúp một lượng lớn dữ liệu tác nghiệp của Học viện được chuyển hóa vào các cơ sở dữ liệu tương ứng. Tuy nhiên, theo quan sát thực tế vẫn còn không ít dữ liệu vẫn đang lưu hành bản cứng, như các quyết định, tờ trình cũ khi chưa áp dụng phần mềm quản lý, hoặc các đơn từ, đặc biệt là đơn từ của sinh viên thì chưa có hình thức lưu trữ điện tử phù hợp. Khi cần phải tra cứu chỉ có thể đến tận nơi và tìm theo các tủ hồ sơ vật lý hoặc tra cứu trong máy tính cục bộ của chuyên viên phụ trách. Một số tài liệu được đăng tải trên website của đơn vị, nhưng chỉ có thể tra cứu theo tiêu đề văn bản (nếu được đặt tiêu đề chính xác) chứ các nội dung thường được đóng gói trong mã nhúng file PDF chỉ cho phép đọc chứ không thể truy cập chi tiết. Đây là một thách thức trong quá trình số hóa nói riêng và chuyển đổi số nói chung tại Học viện, thôi thúc các nghiên cứu tìm kiếm giải pháp thích hợp nhằm biến đổi các văn bản thô còn tồn đọng thành những tài liệu định dạng kỹ thuật số.

Từ thực trạng trên, tác giả đặt ra ba câu hỏi nghiên cứu chính:

● Những công nghệ cần thiết cho việc số hóa dữ liệu văn bản là gì? Có những giải pháp nào trên nền tảng những công nghệ đó thích hợp với số hóa dữ liệu văn bản tại Việt Nam? Những văn bản đã và đang lưu hành tại Học viện khi áp dụng thử nghiệm các giải pháp này cho kết quả như thế nào?

Để tìm kiếm lời giải cho các câu hỏi trên, tác giả đề xuất nghiên cứu và đánh giá các giải pháp và công nghệ hiện đại liên quan đến việc số hóa tài liệu, văn bản. Cụ thể tác giả đặt ra một số mục tiêu nghiên cứu sau:

Nghiên cứu tổng quan các công nghệ số hóa dữ liệu văn bản như nhận dạng ký tự quang học (OCR) hay xử lý văn bản thông minh (IDP). Đây đều là những công nghệ đóng vai trò rất quan trọng trong công cuộc chuyển đổi số.



Khảo sát các giải pháp sẵn có trên thị trường ở Việt Nam, lựa chọn giải pháp khả thi cũng như cài đặt thử nghiệm với dữ liệu thực tế tại Học viện.

Thu thập dữ liệu thực tế từ các phòng ban chức năng và khoa chuyên ngành của Học viện. Dữ liệu được thu thập đảm bảo sự đa dạng về thể loại (các loại văn bản khác nhau lưu hành ở Học viện như nghị quyết, quyết định, thông báo), nguồn gốc (đơn vị phụ trách biên soạn hoặc ban hành văn bản), định dạng tài liệu (hình ảnh chụp từ điện thoại, ảnh quét từ máy scan, file pdf được chuyển từ văn bản MS Word).

Đánh giá mức độ hiệu quả về khả năng bóc tách tài liệu và nhận dạng ký tự của giải pháp đề xuất trên bộ dữ liệu đã thu thập.

Để đạt mục tiêu nghiên cứu, tác giả thực hiện tổng quan nhằm làm rõ cơ sở lý thuyết về công nghệ nhận dạng ký tự quang học; quan sát và trải nghiệm thực tế nhằm hệ thống các giải pháp nhận dạng ký tự quang học tại Việt Nam; và thực hiện thử nghiệm với tài liệu tại Học viện Ngân hàng.

# 1.2 Cơ sở lý thuyết về công nghệ nhận dạng ký tự quang học

Công nghệ Nhận dạng ký tự quang học-Optical Character Recognition (OCR) là một loại công nghệ cho phép máy tính điện tử tự động nhận biết các ký tự (chữ cái, số, dấu câu, ký tự đặc biệt) trên những hình ảnh được cung cấp (Ravina Mithe, 2013). Không giống như bộ não con người, thứ có thể dễ dàng đọc được các ký tự, câu chữ từ hình ảnh, máy tính không đủ thông minh và khả năng trừu tượng để nhận biết được loại thông tin này. Máy tính chỉ hiểu hình ảnh là các điểm ảnh (pixel) đại diện bởi các con số chỉ mã màu sắc ở pixel đó. Bởi vậy, nghiên cứu về công nghệ OCR vẫn đang là một chủ đề rất được quan tâm trong cộng đồng nghiên cứu Trí tuệ nhân tạo.

Cách thức hoạt động chung của OCR được mô tả ở Hình 2. Theo đó máy quét sẽ quét biểu mẫu chứa hình ảnh ký tự, sau đó công cụ nhận dạng tiến hành đọc hiểu các hình ảnh và chuyển chúng thành dữ liệu ASCII (các ký tự máy có thể đọc được). Có nhiều yếu tố ảnh hưởng đến chất lượng văn bản đầu ra của hệ thống OCR như chất lượng hình ảnh đầu vào (độ phân giải cao/thấp, góc chụp nghiêng/thẳng, độ sáng, độ bóng...), mật độ văn bản trên hình ảnh đầu vào (ví dụ giấy tờ cá nhân thì mật độ văn bản ít hơn so với các quy định pháp luật), phông chữ của tài liệu gốc (chữ viết tay, chữ in hoa, loại phông chữ) hay ngôn ngữ của tài liệu gốc (tiếng Việt, tiếng Anh hay nhiều ngôn ngữ cùng trong một văn bản).



Quá trình xử lý của hệ thống OCR thường được chia thành $3$ giai đoạn: phát hiện văn bản (text detection), nhận dạng văn bản (text recognition) và trích xuất thông tin (information extraction). Các giai đoạn này lại áp dụng nhiều kỹ thuật, thuật toán phức tạp của thị giác máy tính (Computer Vision) và xử lý ngôn ngữ tự nhiên (Natural Language Processing). Chẳng hạn với riêng bài toán trích xuất thông tin từ hóa đơn bán hàng tiếng Việt trong cuộc thi MC-OCR Challenge tổ chức năm 2021, mô hình nhận dạng ký tự tốt nhất được xây dựng dựa trên mạng nơ ron Faster R-CNN kết hợp với mạng nơ ron TransformerOCR (Vu Xuan-Son, 2021).

Cùng với OCR, gần đây, thuật ngữ Nhận dạng ký tự thông minh (Intelligent Character Recognition- ICR) (Raymond Ptucha, 2019) được sử dụng để mô tả quá trình đọc hiểu dữ liệu hình ảnh, cụ thể là văn bản chữ và số. ICR là một mô-đun của OCR, có khả năng biến hình ảnh viết tay hoặc các ký tự in thành dữ liệu ASCII.

OMR (Optical Mark Reader- Nhận dạng dấu quang học) (Krisana Chinnasarn, 1999) là một phương pháp điện tử thu thập dữ liệu do con người xử lý bằng cách xác định một số dấu hiệu nhất định trên tài liệu. Thông thường, quá trình nhận dạng dấu quang học được thực hiện với sự hỗ trợ của máy quét kiểm tra truyền tải hoặc phản xạ ánh sáng qua giấy; những nơi có đánh dấu sẽ phản xạ ít ánh sáng hơn phần giấy trắng, dẫn đến độ tương phản kém hơn. OMR thường được ứng dụng để xử lý dữ liệu từ phiếu điều tra hay chấm các bài thi trắc nghiệm. Ngoài ra, nhiều doanh nghiệp công nghệ cũng đưa ra thuật ngữ Xử lý văn bản thông minh (Intelligent Document Processing-IDP) là một công cụ tự động thu thập, trích xuất dữ liệu từ các tài liệu bán cấu trích xuất nội dung từ ảnh chụp mẫu văn bản có sẵn (giấy chứng minh nhân dân, bằng lái xe, thẻ bảo hiểm y tế, hóa đơn), hoặc theo bất kì định dạng văn bản tùy biến (hợp đồng, chứng từ, quy định...), nhằm số hóa tài liệu một cách nhanh chóng và thuận tiện. FPT.AI Reader được các chuyên gia trong lĩnh vực trí tuệ nhân tạo của FPT Smart Cloud nghiên cứu và phát triển. Giải pháp này áp dụng công nghệ nhận dạng ký tự quang học (OCR) và Xử lý văn bản thông minh (IDP), kết hợp kỹ thuật xử lý ảnh nâng cao và Xử lý ngôn ngữ tự nhiên (NLP), cho phép người dùng số hóa văn bản chính xác trong thời gian ngắn (chỉ tới vài giây) (FPT.AI, 2022). Hình 3 dưới đây là một ví dụ về trích xuất các thông tin cần thiết như họ tên, số căn cước công dân, giới tính, quốc tịch, quê quán, địa chỉ từ ảnh chụp mặt trước của một căn cước công dân theo mẫu hiện tại ở Việt Nam.

Đặc biệt, FPT.AI Reader cho phép người dùng tự định nghĩa mẫu văn bản mới, chưa có trong các mẫu có sẵn của hệ thống để tự tạo mô hình OCR của riêng mình. Chẳng hạn ta cần số hóa thẻ sinh viên, có thể tạo một dự án mới trong bảng điều khiển của FPT.AI (https://console.fpt.ai/), tải lên một trúc (semi-structured data) và phi cấu trúc (unstructured data) và chuyển chúng thành tài liệu có cấu trúc (structured data) để sử dụng (Akabot, 2022). IDP là sự kết hợp giữa nhiều công nghệ bao gồm Xử lý ngôn ngữ tự nhiên (Natural Language Processing-NLP), Thị giác máy tính (Computer Vision), Học máy (Machine Learning- ML) và OCR nhằm tăng cường việc nhận diện, phân loại, phân tích, trích xuất dữ liệu và đánh giá dữ liệu để nâng cao độ chính xác và hiệu quả. Ở Việt Nam, nhiều nghiên cứu đã được thực hiện nhằm áp dụng các công nghệ này cho từng loại nghiệp vụ khác nhau, chẳng hạn trích xuất và nhận dạng thông tin trên chứng minh nhân dân của người Việt (Duc Phan, 2021), trích xuất thông tin trên hóa đơn bán hàng (Vu Xuan-Son, 2021), nhận dạng biển số xe (Trần Thị Hương, 2021), trích xuất văn bản từ bìa sách (Phan Thi Thanh Nga, 2017). Tuy nhiên đến nay chưa có nghiên cứu nào áp dụng các công nghệ trên với các tài liệu ở cơ sở giáo dục đại học. Đây cũng là nội dung trọng tâm mà bài báo này hướng đến khi áp dụng thử nghiệm tại Học viện Ngân hàng.



# 1.3 Kết quả thử nghiệm công nghệ nhận dạng ký tự quang học cho số hóa tài liệu tại Học viện Ngân hàng

# 1.3.1 Các giải pháp nhận dạng ký tự quang học tại Việt Nam

1.3.1.1. FPT.AI Reader

FPT.AI Reader là ứng dụng nhận dạng và số ảnh mẫu và nhập vào một số trường thông tin quan trọng muốn trích xuất từ ảnh để huấn luyện mô hình OCR (minh họa ở Hình 4).

FPT.AI Reader cũng cho phép tích hợp ứng dụng OCR vào hệ thống của doanh nghiệp thông qua việc đăng ký tài khoản và nhận “API key” từ bảng điều khiển của FPT.AI (Console.fpt.ai). Mỗi API key này cho phép gửi và nhận kết quả đến 50 lần và có thể được mở rộng tùy vào quy mô xử lý dữ liệu của hệ thống.

# 1.3.1.2. Viettel OCR

Viettel OCR là giải pháp được phát triển bởi bộ phận Trí tuệ nhân tạo của Tập đoàn Viettel, cho phép chuyển đổi tài liệu dạng ảnh (máy quét, máy ảnh, file PDF được chuyển hóa từ file ảnh) thành văn bản như file text (.txt), file Word (.docx). Theo báo cáo trên trang web chính thức, Viettel OCR có khả năng nhận diện văn bản ở dạng bố cục tự do (free layout), có thể tùy chỉnh một cách nhanh chóng để phù hợp với từng bài toán cụ thể của doanh nghiệp. Giải pháp này có thể nhận file đầu vào ở nhiều định dạng khác nhau như PNG, JPEG, cho phép phân tích và trả về kết quả cho nhiều hình ảnh cùng 1 lúc (tối đa 10 ảnh) với độ chính xác tương đối cao (trong báo cáo không ghi rõ độ chính xác).



Tuy nhiên trên website chính thức của giải pháp này chưa cho phép người dùng thử nghiệm mà phải liên hệ với tổng đài để đặt lịch tư vấn trực tiếp (Viettel AI, 2021).

# 1.3.1.3. Google Vision AI

Google Vision AI là dịch vụ đám mây của Google cho phép người dùng khởi tạo các ứng dụng phân tích hình ảnh và video trong thời gian ngắn, huấn luyện các mô hình máy học phân loại hình ảnh bằng AutoML hoặc các mô hình tùy chỉnh. Google Vision AI có khả năng phát hiện đối tượng, đọc chữ viết tay và tạo siêu dữ liệu hình ảnh có giá trị bằng các API được đào tạo trước. Một ưu điểm của giải pháp này là dễ dàng tích hợp với BigQuery, Cloud Function và máy ảnh để kích hoạt hành trình từ đầu đến cuối. Google Vision AI là một giải pháp khá linh hoạt, không tạo sẵn các mẫu tài liệu như FPT.AI Reader và Viettel OCR. Tốc độ xử lý của Google Vision AI khá nhanh. Tuy nhiên, quá trình thử nghiệm tính năng OCR của Google Vision AI với một vài tài liệu tiếng Việt cho kết quả chưa tốt (Hình 5).

# 1.3.1.4. Lựa chọn giải pháp

Ngoài 3 giải pháp thương mại kể trên, một số doanh nghiệp công nghệ ở Việt Nam cũng cung cấp các gói dịch vụ số hóa tài liệu với giải pháp riêng mà họ xây dựng. Tuy nhiên qua quá trình tìm hiểu và trải nghiệm, tác giả quyết định lựa chọn FPT. AI Reader làm giải pháp thử nghiệm trong bài báo này với các nguyên nhân:

FPT.AI Reader cung cấp nền tảng sử dụng miễn phí với tất cả người dùng cuối (enduser), chỉ hạn chế số lượng tài liệu xử lý mỗi ngày (50 requests) và có thể mở rộng linh hoạt tùy vào quy mô của doanh nghiệp.

Mô hình OCR huấn luyện sẵn của FPT. AI Reader có khả năng xử lý dữ liệu tiếng Việt tốt (theo báo cáo của FPT.AI đạt trên $9 6 \%$ cho các loại giấy tờ như chứng minh nhân dân, hộ chiếu (FPT.AI, 2022).

Giải pháp FPT.AI Reader đã được rất nhiều khách hàng sử dụng, đa dạng về ngành nghề lĩnh vực như TP Bank, Home Credit, Tiki, EVN, Sendo (FPT.AI, 2022).

# 1.3.2 Thử nghiệm với tài liệu tại Học viện Ngân hàng

# 1.3.2.1. Thu thập tài liệu

Tác giả chọn lọc từ 150 email cá nhân gần nhất có địa chỉ gửi đến từ các đơn vị của Học viện, trích chọn ra những email có tệp đính kèm là các file pdf. Những file này được chọn lọc để đảm bảo đa dạng về nguồn gốc (Học viện ban hành, cơ quan khác ban hành), về



định dạng (scan từ máy quét ra hình ảnh, chuyển đổi từ văn bản MS Word), về thể loại (quyết định, phiếu trình, nghị định, thông báo...). Chi tiết số liệu thống kê về bộ tài liệu thử nghiệm được trình bày trong Bảng 1.

# 1.3.2.2. Cài đặt giải pháp

Giải pháp OCR của FPT.AI được truy cập trên nền tảng điện toán đám mây tại địa https:// reader.fpt.ai/. Để tạo ứng dụng mới, FPT.AI Reader cho phép ta chọn trong thư viện những mẫu văn bản có sẵn hoặc tạo ứng dụng tùy chỉnh. Trong thư viện các văn bản có sẵn đã bao gồm:

Giấy tờ tài chính ngân hàng (như Báo cáo tài chính, Đăng ký kinh doanh...);
Giấy tờ bảo hiểm và bệnh viện (Giấy ra viện, Phiếu khám, Bảng kê viện phí...);
Giấy tờ quốc tế (Giấy đăng ký xe, Bằng lái xe của một số nước);
Giấy tờ tùy thân Việt Nam;
Giấy tờ khác (Sơ yếu lý lịch, Giấy tờ vận tải, Giấy chứng nhận, Vé máy bay).

Nhận thấy các mẫu văn bản có sẵn trong thư viện không phù hợp với các văn bản trong bộ dữ liệu thử nghiệm, tác giả lựa chọn cài đặt ứng dụng tùy chỉnh. Có 3 mô hình có thể lựa chọn là Bóc tách dữ liệu (từ văn bản có cấu trúc), Mô hình Crop (phát hiện vùng ảnh cần quan tâm) và Phân loại (Gán nhãn phù hợp cho văn bản), tác giả chọn mô hình Bóc tách dữ liệu và sử dụng mô hình Bóc tách dữ liệu OCR có sẵn của FPT.AI chứ không huấn luyện mô hình mới, công việc này sẽ dành cho nghiên cứu trong tương lai với lượng dữ liệu chuẩn bị nhiều và đa dạng hơn.

Trong phần sử dụng mô hình, ta chọn Tải lên để tải văn bản muốn bóc tách, có thể chọn nhiều văn bản cùng lúc, đợi đến khi trạng thái của tất cả văn bản hiện “Thành công” để xem kết quả (minh họa ở Hình 6). Để xem kết quả chi tiết của mỗi tài liệu, ta chọn View ở phần OCR. Một cửa sổ khác sẽ hiện lên hiển thị toàn bộ các trường dữ liệu bóc tách được từ văn bản đầu vào (Hình 7). Trong cửa sổ này ta có thể xem được chi tiết mô hình đã phát hiện được bao nhiêu “box” (vùng ảnh) chứa chuỗi ký tự có thể là văn bản. Click vào chi tiết mỗi box, ta có thể đánh dấu giá trị văn bản phát hiện được trong đó là sai hay đúng, thuộc loại nào (trong trường hợp này chưa định nghĩa loại box nên không hiển thị).

# 1.3.2.3. Phương pháp đánh giá

Với kết quả nhận được từ ứng dụng vừa xây dựng, tác giả đánh giá bằng cả phương pháp định lượng và định tính theo các tiêu chí sau:



Số box phát hiện được có đúng không (có bỏ sót hay phát hiện thừa vùng ảnh nào hay không).

Tỷ lệ sai số theo đơn vị từng từ ở mỗi box (chẳng hạn mô hình dự đoán “Học viện Ngan hàng” so với kết quả đúng là “Học viện Ngân hàng” thì sai số là $2 5 \%$ ). Do số lượng từ là quá lớn nên tác giả chỉ thống kê trên trang đầu của mỗi văn bản để kiểm tra những thông tin quan trọng nhất.

Phân tích các trường hợp sai thường gặp theo từng loại văn bản.

1.3.2.4. Kết quả thực nghiệm Với các tiêu chí kể trên, mô hình của FPT.

AI Reader cho kết quả rất tốt. Cụ thể:

Số box phát hiện được có độ chính xác $9 8 \%$ , không bỏ sót box nào trên các tài liệu. Tuy nhiên một số box bị thừa, đặc biệt là các box ở vùng ảnh chứa con dấu đỏ.

Tỷ lệ sai số khá ấn tượng: $2 7 \%$ với 210 từ bị sai trên tổng số 781 từ (chỉ tính những trang đầu của 20 tài liệu).

Các lỗi sai thường gặp chủ yếu là lỗi dấu câu (“Hoc”- “Học”, “Xã hồi”- “Xã hội”...), viết hoa (“đơn VI”- “đơn vị”), và các số quyết định trên phần đầu của văn bản (do là số viết tay).

Các văn bản được chuyển đổi từ file MS Word có tỷ lệ sai số thấp hơn hẳn (trong thực tế những file này có thể chuyển đổi trực tiếp về lại dạng văn bản với các thư viện lập trình phù hợp).

Các trường thông tin quan trọng như đơn vị ban hành văn bản, loại văn bản (thông báo, nghị định, quyết định...), chủ đề phụ của văn bản (về việc điều động, về việc tổ chức...) và đối tượng nhận văn bản có tỷ lệ sai số thấp hơn trung bình chỉ $1 6 \%$ .

Thời gian xử lý của mô hình FPT.AI Reader cũng tương đối nhanh, theo quan sát thực tế, mỗi văn bản 3 trang tốn khoảng trên dưới 5 giây để hoàn thành. Trong thực tế, số trang và dung lượng của văn bản có thể đa dạng và lớn hơn, nhưng để đáp ứng nhu cầu số hóa cơ bản, tức là bóc tách được các trường thông tin quan trọng (thường nằm ở trang đầu văn bản) thì có thể có biện pháp tiền xử lý trước khi đưa vào mô hình.



# 1.4 Kết luận và hướng phát triển

# 1.4.1 Kết luận

Trong bài báo này, tác giả đã nêu tầm quan trọng của việc số hóa dữ liệu, khảo sát sơ bộ thực trạng số hóa tài liệu văn bản tại Học viện Ngân hàng. Qua đó tác giả đặt ra 4 mục tiêu nghiên cứu và đã giải quyết lần lượt từng mục tiêu. Có thể tóm tắt một số đóng góp chính của bài báo như sau:

Giới thiệu các công nghệ cốt lõi như nhận dạng ký tự quang học (OCR), nhận dạng dấu quang học (OMR), xử lý văn bản thông minh (IDP) và những ứng dụng trên nhiều lĩnh vực của các công nghệ này.

Tìm hiểu và khảo sát một số giải pháp thương mại cho số hóa tài liệu phổ biến ở Việt Nam như FPT.AI Reader, ViettelOCR, Google Vision AI. Trên cơ sở đó tác giả so sánh đánh giá và lựa chọn FPT.AI Reader để cài đặt ứng dụng thử nghiệm tại Học viện Ngân hàng.

Thu thập dữ liệu văn bản từ 150 email nội bộ của Học viện, chọn lọc 20 file pdf đính kèm trong các email đó sao cho đảm bảo có các loại văn bản khác nhau, các định dạng khác nhau và các phòng ban phụ trách khác nhau.

Cài đặt thử nghiệm hệ thống OCR trên nền tảng FPT.AI Reader để áp dụng với bộ dữ liệu văn bản vừa thu thập. Kết quả thử nghiệm cho thấy mô hình nhận dạng ký tự của FPT.AI hoạt động khá tốt với $2 7 \%$ sai số ở mức từ và thời gian xử lý chỉ khoảng 5 giây cho mỗi văn bản 3 trang, chỉ tồn tại một vài sai số ở những ký tự viết tay hoặc bị mờ do chất lượng scan tài liệu.

# 1.4.2 Hướng phát triển

Với kết quả thử nghiệm trình bày như trên, tác giả đề xuất Học viện Ngân hàng đẩy mạnh áp dụng các công nghệ mới cho quá trình số hóa dữ liệu, đặc biệt là dữ liệu văn bản. Giải pháp của FPT.AI tuy còn một số tồn tại, sai số, nhưng có thể được cải thiện bằng cách huấn luyện hoặc tinh chỉnh mô hình OCR với bộ dữ liệu đầy đủ và đa dạng hơn của Học viện. Điều này sẽ cần các nghiên cứu chuyên sâu về công nghệ OCR trong tương lai. ■

# 2. TÀI LIỆU THAM KHẢO

Akabot (2022), Sự khác biệt giữa OCR và IDP, Truy cập ngày 20 tháng 4 năm 2023, từ https://akabot.com/vi/tai-nguyen/ blog/su-khac-biet-giua-ocr-va-idp/



ALS (2021), Quy trình các bước số hóa tài liệu lưu trữ doanh nghiệp, Truy cập ngày 20 tháng $4  { \mathrm { n } }  { \mathrm { \breve { a } m } } 2 0 2 3$ , từ https://als. com.vn/quy-trinh-cac-buoc-so-hoa-tai-lieu-luu-trudoanh-nghiep

Duc Phan Van Hoai, Huu-Thanh Duong, Vinh Truong Hoang (2021), “Text recognition for Vietnamese identity card based on deep features network”, International Journal on Document Analysis and Recognition (IJDAR), số 24, trang 123–131.

FPT.AI (2022), FPT.AI Reader - Vietnamese Passport Recognition, Truy cập ngày 20 tháng $4  { \mathrm { n } }  { \mathrm { \breve { a } m } } 2 0 2 3$ , từ https://docs. fpt.ai/docs/en/vision/documentation/licenserecognition

FPT.AI (2022), “FPT AI Read - Trích xuất dữ liệu vượt mọi giới hạn”, Truy cập ngày 20 tháng 4 năm 2023, từ https:// fpt.ai/vi/reader

FPT.AI (2022), Hướng dẫn sử dụng FPT.AI Reader - phần mềm ocr trích xuất thông tin từ ảnh chụp, Truy cập ngày 20 tháng 4 năm 2023, từ https://fpt.ai/vi/huong-dan-su-dungfptai-reader-phan-mem-ocr-trich-xuat-thong-tin-tu-anh-chup

Geewook Kim, Teakgyu Hong, Moonbin Yim, JeongYeon Nam, Jinyoung Park, Jinyeong Yim, Wonseok Hwang, Sangdoo Yun, Dongyoon Han, Seunghyun Park (2022), “OCR-Free Document Understanding Transformer”, Computer Vision – ECCV, số 13688, trang 498–517.

Học viện Ngân hàng (2023), Tờ trình số 694/TTr-HVNH ngày $2 8 / 3 / 2 0 2 3 \ \mathrm { K } \hat { \hat { \mathrm { e } } }$ hoạch Chuyển đổi số tại Học viện Ngân hàng. Krisana Chinnasarn, Yuttapong Rangsanseri (1999), “Image-processing-oriented optical mark reader”. Applications of Digital Image Processing XXII, số 3808.

Noman Islam, Zeeshan Islam,Nazia Noor (2016), “A Survey on Optical Character Recognition System”, Journal of Information & Communication Technology-JICT, số 10, trang 1-4

Phạm Huy Giao (2020), “Chuyển đổi số: Bản chất, thực tiễn và ứng dụng”, Tạp chí Dầu khí, số 12, trang 12-16. Phan Thi Thanh Nga, Nguyễn Thị Huyền Trang, Nguyễn Văn Phúc, Thái Duy Quý, Võ Phương Bình (2017), “Vietnamese

text extraction from book covers”. Tạp chí Khoa học Đại học Đà Lạt”, số 7, trang 142– 152.



Ravina Mithe, Supriya Indalkar, Nilam Divekar (2013), “Optical Character Recognition”, International Journal of Recent Technology and Engineering (IJRTE), số 2, trang 72-75.

Raymond Ptucha, Felipe Petroski Such, Suhas Pillai, Frank Brockler, Vatsala Singh, Paul Hutkowski (2019), “Intelligent character recognition using fully convolutional neural networks”, Pattern Recognition, số 88, trang 604-613.

Thủ tướng Chính phủ (2022), Quyết định số 131/QĐ-TTg ngày 25/01/2022 của Thủ tướng Chính phủ: Phê duyệt Đề án “Tăng cường ứng dụng công nghệ thông tin và chuyển đổi số trong giáo dục và đào tạo giai đoạn 2022-2025, định hướng đến năm 2030”

Trần Thị Hương, Ngô Thị Kiều Hằng (2021), “Kỹ thuật nhận dạng biển số xe và ứng dụng vào bài toán quản lý bãi giữ xe tại trường đại học Hà Tĩnh”. Tạp chí Khoa học Đại học Đồng Tháp, số 3, trang 115-120.

Viettel AI (2021), “Nhận dạng ký tự quang học”, Truy cập ngày 20 tháng 4 năm 2023, từ https://viettelgroup.ai/service/ocr

Vu Xuan-Son, Bui Quang-Anh, Nguyen Nhu-Van, Hai Nguyen Thi Tuyet, Vu Thanh (2021), “MC-OCR Challenge:

Mobile-Captured Image Document Recognition for Vietnamese Receipts”, RIVF International Conference on Computing and Communication Technologies, IEEE, trang 1-6.

### TASK QA
num_correct,answers
1,B
1,B
1,C
1,C
1,B