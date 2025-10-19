## 1. Lời mở đầu

Bài toán nhận diện biển số xe Việt Nam là một bài toán không còn mới, đã được phát triển dựa trên các phương pháp xử lý ảnh truyền thống và cả những kỹ thuật mới sử dụng Deep Learning. Trong bài toán này tôi chỉ phát triển bài toán phát hiện biển số (một phần trong bài toán nhận diện biển số) dựa trên thuật toán YOLO-TinyV4 với mục đích:

- Hướng dẫn chuẩn bị dữ liệu cho bài toán Object Detection.
- Hướng dẫn huấn luyện YOLO-TinyV4 dùng darknet trên Google Colab.

## 2. Chuẩn bị dữ liệu

### 2.1 Đánh giá bộ dữ liệu

Trong bài viết tôi sử dụng bộ dữ liệu biển số xe máy Việt Nam chứa 1750 ảnh, bạn đọc có thể tải tại đây.

Image of a motorcycle license plate 0009\_02194\_b.jpg

Image of a motorcycle license plate 0009\_05325\_b.jpg

Image of a motorcycle license plate 0010\_00004\_b.jpg

Image of a motorcycle license plate 0010\_02063\_b.jpg

Image of a motorcycle license plate 0011\_00515\_b.jpg

Image of a motorcycle license plate 0012\_04539\_b.jpg

Image of a motorcycle license plate 0019\_01137\_b.jpg

Image of a motorcycle license plate 0019\_02163\_b.jpg

Image of a motorcycle license plate 0019\_06895\_b.jpg

Image of a motorcycle license plate 0020\_00536\_b.jpg

Image of a motorcycle license plate 0020\_02063\_b.jpg

Image of a motorcycle license plate 0020\_07156\_b.jpg

Hình 14.1: Ảnh biển số trong bộ dữ liệu

Ảnh biển số xe được trong bộ dữ liệu được chụp từ một camera tại vị trí kiểm soát xe ra vào trong hầm. Do vậy:

- Kích thước các biển số xe không có sự đa dạng, do khoảng cách từ camera đến biển số xe xấp xỉ gần bằng nhau giữa các ảnh.
- Ảnh có độ sáng thấp và gần giống nhau do ảnh được chụp trong hầm chung cư. =&gt; Cần làm đa dạng bộ dữ liệu.

## 2.2 Các phương pháp tăng sự đa dạng của bộ dữ liệu

### 2.2.1 Đa dạng kích thước của biển số

Đa dạng kích thước bằng 2 cách:

- Cách 1: Thu nhỏ kích thước biển bằng cách thêm biên kích thước ngẫu nhiên vào ảnh gốc, sau đó resize ảnh bằng kích thước ảnh ban đầu.
- Cách 2: Crop ảnh chứa biển số với kích thước ngẫu nhiên, sau đó resize ảnh bằng kích thước ảnh ban đầu.

```
# Cách 1 def add_boder(image_path, output_path, low, high):
# """low: kích thước biên thấp nhất (pixel) high: kích thước biên lớn nhất (pixel)
# """
# # random các kích thước biên trong khoảng (low, high)
```

2025-09-23 23.32.48\_Ai Race

# Cách2 def random\_crop(image\_path, out\_path):

image = cv2.imread(image\_path) original\_width, original\_height = image.shape[1], image.shape[0] x\_center, y\_center = original\_height//2, original\_width//2 x\_left = random.randint(0, x\_center//2) x\_right = random.randint(original\_width-x\_center//2, original\_width) y\_top = random.randint(0, y\_center//2) y\_bottom = random.randint(original\_height-y\_center//2, original\_width)

# crop ra vùng ảnh với kích thước ngẫu nhiên

cropped\_image = image[y\_top:y\_bottom, x\_left:x\_right]

# resize ảnh bằng kích thước ảnh ban đầu

cropped\_image = cv2.resize(cropped\_image, (original\_width, original\_height))

## 2.2.2 Thay đổi độ sáng của ảnh

```
def change_brightness(image_path, output_path, value):
    """value: độ sáng thay đổi"""
    img = cv2.imread(image_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(output_path, img)
```

Motorcycle with license plate 59-P1 664.80 on a concrete surface. Motorcycle with license plate 59-P1 664.80 on a concrete surface.

Hình 14.4: Độ sáng thay đổi (bên phải)

## 2.2.3 Xoay ảnh

```
import imutils
def rotate_image(image_path, range_angle, output_path):
    """range_angle: Khoảng góc quay"""
    image = cv2.imread(image_path)
    #lựa chọn ngẫu nhiên góc quay
```<|im_
```

## 2.3 Gán nhãn dữ liệu

Tool gán nhãn ở đây tôi dùng là **labelImg** , bạn đọc có thể tải và đọc hướng dẫn sử dụng tại [đây](https://github.com/aleju/labelImg) .

Screenshot of labelImg interface showing an image of a motorcycle license plate with a red light on the back and a bounding box around it. The right side shows a "Edit Label" dialog with options for editing labels and difficulty levels.

Hình 14.6: Xác định vùng biển chứa biển số

**LabelImg** hỗ trợ gán nhãn trên cả 2 định dạng PASCAL VOC và YOLO với phần mở rộng file annotation tương ứng là .xml và .txt.

Trong bài toán sử dụng mô hình YOLO, tôi lưu file annotation dưới dạng .txt.

0 0.384534 0.346535 0.201271 0.250825

Hình 14.7: Nội dung trong một file annotation Mỗi dòng trong một file annotation bao gồm:

## 3. Huấn luyện mô hình

### 3.1 Giới thiệu về YOLO-Tinyv4 và darknet

#### 3.1.1 YOLO-Tinyv4

YOLOv4 là thuật toán Object Detection, mới được công bố trong thời gian gần đây với sự cải thiện về kết quả đáng kể so với YOLOv3.

MS COCO Object Detection chart showing AP vs FPS for various models including EfficientDet, YOLOv4 (ours), YOLOv3, ATSS, ASFF*, CenterMask* with labels "EfficientDet (D0-D4)", "real-time", "YOLOv4 (ours)", "ASFF*", "ATSS", "ASFF*" and "CenterMask*". The x-axis shows FPS (V100) and the y-axis shows AP.

Hình 14.8: Sự cải thiện của YOLOv4 ( [source](https://example.com/source) )

| <!-- image -->  Ai logo   | VIETTEL AI RACE         | TD048                   |
|---------------------------|-------------------------|-------------------------|
|                           | NHẬN DIỆN VỊ TRÍ        | Lần ban hành: 1         |
| BIỂN SỐ XE MÁY VIỆT NAM   | BIỂN SỐ XE MÁY VIỆT NAM | BIỂN SỐ XE MÁY VIỆT NAM |

<!-- image -->

YOLOv4 - 64.9% AP50 vs FPS (MS COCO Object Detection)

**Hình 14.9:** YOLOv4 với YOLO-Tinyv4 ( source )

YOLOv4-tiny released: 49.2% AP50, 371 FPS (GTX 1080 Ti) / 339 FPS (RTX 2070)

- **1770 FPS** - on GPU RTX 2080Ti - (416x416, fp16, batch=4) tkDNN/TensorRT ceccocats/tkDNN#59 (comment)
- **1353 FPS** - on GPU RTX 2080TI - (416x416, fp16, batch=4) OpenCV 4.4.0 (including: transferring CPU-&gt;GPU and GPU-&gt;CPU) (excluding: nms, pre/post-processing) #6067 (comment)
- **39 FPS** - 25ms latency - on Jetson Nano - (416x416, fp16, batch=1) tkDNN/TensorRT ceccocats/tkDNN#59 (comment)
- **290 FPS** - 3.5ms latency - on Jetson AGX - (416x416, fp16, batch=1) tkDNN/TensorRT ceccocats/tkDNN#59 (comment)
- **42 FPS** - on CPU Core i7 7700HQ (4 Cores / 8 Logical Cores) - (416x416, fp16, batch=1) OpenCV 4.4.0 (compiled with OpenVINO backend) #6067 (comment)
- **28 FPS** - on CPU ARM Kirin 990 - Smartphone Huawei P40 #6091 (comment) - Tencent/NCNN library https://github.com/Tencent/ncnn
- **128 FPS** - on nVIDIA Jetson AGX Xavier - MAX\_N - Darknet framework
- **371 FPS** on GPU GTX 1080 Ti - Darknet framework

**Hình 14.10:** YOLO-Tinyv4 trên các nền tảng ( source )

**3.1.2 Darknet**