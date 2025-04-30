# 📌 Tổng quan dữ liệu gốc

- Số dòng: 1000
- Số cột: 22
- Các cột:
  - eventID 
  - case Spend area text
  - case Company
  - case Document Type
  - case Sub spend area text
  - case Purchasing Document
  - case Purch. Doc. Category name
  - case Vendor
  - case Item Type
  - case Item Category
  - case Spend classification text
  - case Source
  - case Name
  - case GR-Based Inv. Verif.
  - case Item
  - case concept:name
  - case Goods Receipt
  - event User
  - event org:resource
  - event concept:name
  - event Cumulative net worth (EUR)
  - event time:timestamp

# 🧹 Chi tiết các bước làm sạch

- Phát hiện 10 dòng thiếu dữ liệu ở 3 cột: `case Spend area text`, `case Sub spend area text`, `case Spend classification text`.
- Điền missing values bằng giá trị mode (phổ biến nhất).
- Không phát hiện dòng trùng lặp.
- Chuẩn hóa kiểu dữ liệu:
  - `event time:timestamp` → datetime.
  - `event Cumulative net worth (EUR)` → float.

# 📊 Biểu đồ phân phối và nhận xét

## eventID 
**Loại biểu đồ**: Histogram
![eventID ](plots/eventID .png)
> Nhận xét: Biểu đồ histogram cho thấy phân phối giá trị của `eventID `, giúp nhận diện outlier hoặc xu hướng tập trung.


## case Spend area text
**Loại biểu đồ**: Bar Chart (Categorical)
![case Spend area text](plots/case Spend area text.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Spend area text`.


## case Company
**Loại biểu đồ**: Bar Chart (Categorical)
![case Company](plots/case Company.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Company`.


## case Document Type
**Loại biểu đồ**: Bar Chart (Categorical)
![case Document Type](plots/case Document Type.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Document Type`.


## case Sub spend area text
**Loại biểu đồ**: Bar Chart (Categorical)
![case Sub spend area text](plots/case Sub spend area text.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Sub spend area text`.


## case Purchasing Document
**Loại biểu đồ**: Histogram
![case Purchasing Document](plots/case Purchasing Document.png)
> Nhận xét: Biểu đồ histogram cho thấy phân phối giá trị của `case Purchasing Document`, giúp nhận diện outlier hoặc xu hướng tập trung.


## case Purch. Doc. Category name
**Loại biểu đồ**: Bar Chart (Categorical)
![case Purch. Doc. Category name](plots/case Purch. Doc. Category name.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Purch. Doc. Category name`.


## case Vendor
**Loại biểu đồ**: Bar Chart (Categorical)
![case Vendor](plots/case Vendor.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Vendor`.


## case Item Type
**Loại biểu đồ**: Bar Chart (Categorical)
![case Item Type](plots/case Item Type.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Item Type`.


## case Item Category
**Loại biểu đồ**: Bar Chart (Categorical)
![case Item Category](plots/case Item Category.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Item Category`.


## case Spend classification text
**Loại biểu đồ**: Bar Chart (Categorical)
![case Spend classification text](plots/case Spend classification text.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Spend classification text`.


## case Source
**Loại biểu đồ**: Bar Chart (Categorical)
![case Source](plots/case Source.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Source`.


## case Name
**Loại biểu đồ**: Bar Chart (Categorical)
![case Name](plots/case Name.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Name`.


## case GR-Based Inv. Verif.
**Loại biểu đồ**: Bar Chart (Bool)
![case GR-Based Inv. Verif.](plots/case GR-Based Inv. Verif..png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case GR-Based Inv. Verif.`.


## case Item
**Loại biểu đồ**: Histogram
![case Item](plots/case Item.png)
> Nhận xét: Biểu đồ histogram cho thấy phân phối giá trị của `case Item`, giúp nhận diện outlier hoặc xu hướng tập trung.


## case concept:name
**Loại biểu đồ**: Bar Chart (Categorical)
![case concept:name](plots/case concept:name.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case concept:name`.


## case Goods Receipt
**Loại biểu đồ**: Bar Chart (Bool)
![case Goods Receipt](plots/case Goods Receipt.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `case Goods Receipt`.


## event User
**Loại biểu đồ**: Bar Chart (Categorical)
![event User](plots/event User.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `event User`.


## event org:resource
**Loại biểu đồ**: Bar Chart (Categorical)
![event org:resource](plots/event org:resource.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `event org:resource`.


## event concept:name
**Loại biểu đồ**: Bar Chart (Categorical)
![event concept:name](plots/event concept:name.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `event concept:name`.


## event Cumulative net worth (EUR)
**Loại biểu đồ**: Histogram
![event Cumulative net worth (EUR)](plots/event Cumulative net worth (EUR).png)
> Nhận xét: Biểu đồ histogram cho thấy phân phối giá trị của `event Cumulative net worth (EUR)`, giúp nhận diện outlier hoặc xu hướng tập trung.


## event time:timestamp
**Loại biểu đồ**: Bar Chart (Categorical)
![event time:timestamp](plots/event time:timestamp.png)
> Nhận xét: Bar chart cho thấy sự phân bố của các giá trị phân loại trong `event time:timestamp`.



# 💡 Các insight nổi bật

- Một số cột có giá trị chiếm ưu thế rõ rệt (vd: `case Company`, `case Vendor`).
- Các cột numerical như `event Cumulative net worth (EUR)` có nhiều giá trị nhỏ, một số trường hợp outlier đáng chú ý.