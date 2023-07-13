import streamlit as st

st.title('Các loại toán tử')

st.subheader('Toán tử số học')

a, b = 5, 2
# st.write('a =', a)
# st.write('b =', b)
# st.write('Tổng =', a+b)
# st.write('Hiệu =', a-b)
# st.write('Tích =', a*b)
# st.write('Lũy thừa =', a**b)
# st.write('Thương =', a/b)
# st.write('Chia lấy dư =', a%b)
# st.write('Chia lấy nguyên =', a//b)

st.subheader('Toán tử so sánh')
st.write('a==b: ',a==b)
st.write('a!=b: ',a!=b)
st.write('a>b: ',a>b)
st.write('a<b: ',a<b)
st.write('a>=b: ',a>=b)
st.write('a<=b: ',a<=b)

st.write('10 <= 10.0:', 10 <= 10.0)

st.subheader('Toán tử logic')
tuoi = 19
suc_khoe = 'tốt'
st.write("được học lái xe: ", tuoi >= 18 and suc_khoe=='tốt')

diem = 7.5
hanh_kiem = 'Tốt'
st.write("Được học sinh giỏi", diem >= 8 and hanh_kiem=='tốt')

hoa_don = 250000
tien_mat = 1000000
the = 200000
vi_dt = 150000
