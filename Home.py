import streamlit as st
import chapter3 as c3
import numpy as np
from PIL import Image
import cv2
import streamlit.components.v1 as stc
#link file css
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")
def main():
    
    HTML_BANNER = """
    <div style="display:flex;justify-content: center;background-color:#fc4a1a;padding:10px;border-radius:10px;">
        <div style="margin:0 20px">
            <img style="width:150px;height:150px;object-fit: contain;" src="https://ucarecdn.com/7b1dbf45-e692-417c-8b7e-3b4f2e4bbaea/" alt="">
        </div>
        <div style="padding-bottom:20px;">
            <h1 style="color:white;text-align:center;">Project cuối kì Xử lí Ảnh</h1>
            <h2 style="color:white">Giảng Viên Trần Tiến Đức</h2>
           
            
        </div>
       

        </div>
    """

    stc.html(HTML_BANNER)
	


    
    # Đặt tiêu đề và mô tả cho ứng dụng

    # Hiển thị thông tin cá nhân
    st.text("Sinh viên thực hiện: ")
    st.text("Trần Đình Hải    20110640")
    st.text("Nguyễn Thành Đa    20110169")
    st.text("Giáo viên hướng dẫn: Thầy Trần Tiến Đức")
    st.text("Tên bộ môn: Xử lý ảnh")

    st.markdown("Chuyển đổi hình ảnh")

    # Danh sách các hàm
    function_list = [c3.Negative, c3.Logarit, c3.Power, c3.PiecewiseLinear, c3.Histogram, c3.HistEqual, c3.HistEqualColor, c3.LocalHist, c3.HistStat, c3.BoxFilter, c3.BoxFilter2, c3.Threshold]

    # Dropdown chứa danh sách các chức năng
    selected_function = st.selectbox("Chọn chức năng", function_list, format_func=lambda func: func.__name__)

    if selected_function:
        st.subheader(selected_function.__name__)

        # Tải hình ảnh đầu vào
        uploaded_file = st.file_uploader("Tải lên hình ảnh", type=["png", "jpg", "tif","bmp","gif"])
        if uploaded_file is not None:
            # Đọc hình ảnh đầu vào
            img_pil = Image.open(uploaded_file)
            img = np.array(img_pil)

            # Hiển thị ảnh ban đầu
            st.write("Ảnh ban đầu:")
            if len(img.shape) == 3:  # Ảnh màu (RGB)
                st.image(img, channels="RGB")
            else:  # Ảnh xám
                st.image(img, channels="L")

            # Áp dụng chức năng được chọn cho hình ảnh
            img_out = selected_function(img)

            # Hiển thị ảnh kết quả
            st.write("Kết quả:")
            if len(img_out.shape) == 3:  # Ảnh màu (RGB)
                st.image(img_out, channels="RGB")
            else:  # Ảnh xám
                st.image(img_out, channels="L")

if __name__ == "__main__":
    main()


