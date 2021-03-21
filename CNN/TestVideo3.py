import numpy as np
import tensorflow
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

"""
Giả sử:     trong bài toán phân lớp các loài động vật dựa trên 7 đặc điểm [màu lông, kích thước, cân nặng, tốc độ chạy, tiếng kêu, số lượng con sinh ra, tuổi thọ]
Quy ước:    màu lông  : trắng, vàng: 2, xám: 1, đen: 0
            kích thước: lớn: 2, vừa: 1, nhỏ: 0
            cân nặng:   lớn: 2, vừa: 1, nhỏ:0
            tốc độ:     chạy nhanh: 2, vừa: 1, chậm: 0
            tiếng kêu:  to: 2, vừa: 1, nhỏ:0
            số lượng con sinh ra: lớn:2, vừa: 1, ít: 0
            tuổi thọ:   cao:2, vừa 1, thấp:0
            
"""
# ta lấy ví dụ với 3 loài voi, sư tử, chuột
# tạo input data
datavoi = [[0, 2, 2, 1, 1, 0, 2], [0, 2, 2, 1, 1, 0, 1]]
datasutu = [[2, 1, 1, 2, 2, 0, 1], [1, 1, 1, 2, 1, 0, 1]]
datachuot = [[1, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 1, 1]]

data = datavoi + datasutu + datachuot
label = [0, 0, 1, 1, 2, 2]

# chuyển về dạng tensor
data = np.array(data)
# print("data " + str(data))
label = np.array(label)
# print("label "+ str(label))

datatestsutu = [[1, 1, 1, 1, 1, 0, 0]]
# datatestvoi = [[1,1,1,0,1,0,2]]
# datatest= np.array(datatestvoi)
datatest = np.array(datatestsutu)
print(data.shape)

# xay dung mang neural
model = Sequential()  # xay dung 1 chuoi cac lop mang

model.add(Dense(200, activation='relu', input_shape=[1, 7]))  # dense: mang don thuan ko co chuc nang dac biet
# so nut = 200
# ham kich hoat su dung: relu
# input_shape : khai bao so chieu cua du lieu dau vao
# mỗi lần huấn luyện chỉ ném vào 1 vector nên là 1, cái thứ 2 là 7: 7 thuộc tính

# thêm 1 cái dense: ý tức là có 2 lớp ẩn
model.add(Dense(100, activation='relu'))

# lớp đầu ra
model.add(Dense(3, activation='softmax'))

# xaydung lostfunciton va optimization function, metrics funtion
# lostfuntion: hàm tính lỗi của chương trình, dữ liệu đầu ra với dl chuẩn
# optimizerfuntion: thuật toán update weight với bias
# metric: tính chính xác trên tập kiểm tra
model.compile(loss='sparse_categorical_crossentropy', optimizer="Adam", metrics=['accuracy'])
model.fit(data, label, epochs=200) #so lan training

model.save_weights('phanbietdv.h5') #luu trọng số

print(model.predict(datatest))
