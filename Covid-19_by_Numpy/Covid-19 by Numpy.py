from numpy import genfromtxt
import numpy as np

provinces = np.array(['กระบี่', 'กรุงเทพมหานคร', 'กาญจนบุรี', 'กาฬสินธุ์', 'กำแพงเพชร',
       'ขอนแก่น', 'จันทบุรี', 'ฉะเชิงเทรา', 'ชลบุรี', 'ชัยนาท',
       'ชัยภูมิ', 'ชุมพร', 'ตรัง', 'ตราด', 'ตาก', 'นครนายก', 'นครปฐม',
       'นครพนม', 'นครราชสีมา', 'นครศรีธรรมราช', 'นครสวรรค์', 'นนทบุรี',
       'นราธิวาส', 'น่าน', 'บึงกาฬ', 'บุรีรัมย์', 'ปทุมธานี',
       'ประจวบคีรีขันธ์', 'ปราจีนบุรี', 'ปัตตานี', 'พระนครศรีอยุธยา', 'พะเยา',
       'พังงา', 'พัทลุง', 'พิจิตร', 'พิษณุโลก', 'ภูเก็ต', 'มหาสารคาม',
       'มุกดาหาร', 'ยะลา', 'ยโสธร', 'ระนอง', 'ระยอง', 'ราชบุรี', 'ร้อยเอ็ด',
       'ลพบุรี', 'ลำปาง', 'ลำพูน', 'ศรีสะเกษ', 'สกลนคร', 'สงขลา', 'สตูล',
       'สมุทรปราการ', 'สมุทรสงคราม', 'สมุทรสาคร', 'สระบุรี', 'สระแก้ว',
       'สิงห์บุรี', 'สุพรรณบุรี', 'สุราษฎร์ธานี', 'สุรินทร์', 'สุโขทัย',
       'หนองคาย', 'หนองบัวลำภู', 'อำนาจเจริญ', 'อุดรธานี', 'อุตรดิตถ์',
       'อุทัยธานี', 'อุบลราชธานี', 'อ่างทอง', 'เชียงราย', 'เชียงใหม่',
       'เพชรบุรี', 'เพชรบูรณ์', 'เลย', 'แพร่', 'แม่ฮ่องสอน'])
       
dates = np.array(open('data.csv').readlines()[0].strip().split(','))
data = genfromtxt('data.csv', delimiter=',',skip_header=1).astype('int32')

def find_max_min_on_date(provinces,dates,data,date):
       dod = data[::, list(dates).index(date)]
       return {'max': list(provinces[np.where(dod == np.max(dod))[0]]), 'min': list(provinces[np.where(dod == np.min(dod))[0]])}

def find_max_min_in_province(provinces,dates,data,province):
       dop = data[list(provinces).index(province)]
       return {'max': list(dates[np.where(dop == np.max(dop))[0]]), 'min': list(dates[np.where(dop == np.min(dop))[0]])}

def find_average_growth(provinces,data,n):
       ndata = data[::,-n::]
       odata = data[::,-n-1:-1:]
       c = 0.000000001
       ndata = (ndata-odata)/(odata+c)
       return sorted([(sum(ndata[i])/3.0, provinces[i]) for i in range(len(provinces))])

def normalize(data):
       return data/np.max(data, axis=1).reshape((len(data),1))

print(find_max_min_on_date(provinces,dates,data,'2021-11-07'))
print(find_max_min_on_date(provinces,dates,data,'2021-08-15'))
print("-------------------------------------------------------------------------------------------------")
print(find_max_min_in_province(provinces,dates,data,'บึงกาฬ'))
print(find_max_min_in_province(provinces,dates,data,'นครปฐม'))
print("-------------------------------------------------------------------------------------------------")
print(find_average_growth(provinces,data,3))
print(find_average_growth(provinces,data,4))
print("-------------------------------------------------------------------------------------------------")
print(normalize(data))


import plotly.graph_objects as go

fig = go.Figure()
n_data = normalize(data)

for i in range(data.shape[0]):
  fig.add_trace(go.Scatter(y=n_data[i,:], x=dates, name=provinces[i]))
fig.show()
