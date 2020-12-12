from numpy.core.fromnumeric import size
import streamlit as st
from PIL import Image, ImageFilter, ImageFont, ImageDraw, ImageEnhance

st.sidebar.title("Image Manipulation")
file = st.file_uploader('Upload an image',type=['jpg','png','tif','jpeg'])
wrapper = st.empty()
isinfovisible = st.sidebar.checkbox('Show image info')

st.sidebar.header("Modify")
w = st.sidebar.number_input('Width',value= 400, min_value=0)
h = st.sidebar.number_input('Height',value= 300,min_value=0)
resizebtn = st.sidebar.button("resize image") 

st.sidebar.header('Apply filter effect')
effects = {
    'Detail':ImageFilter.DETAIL,
    'Blur':ImageFilter.BLUR,
    'Outline':ImageFilter.CONTOUR,
    'Enhance Egdes':ImageFilter.EDGE_ENHANCE,
    'Emboss':ImageFilter.EMBOSS,
    'Sharpen':ImageFilter.SHARPEN,
    'Smooth':ImageFilter.SMOOTH,
    'Box blur':ImageFilter.BoxBlur(10),
    'Gaussian blur':ImageFilter.GaussianBlur(10),
    'Inverted Outline':ImageFilter.FIND_EDGES,
}
img_effect = st.sidebar.selectbox('choose the effect filter',list(effects.keys()))

watermark_text = st.sidebar.text_input('enter text for image overlay')
textapply_btn = st.sidebar.button("apply text on image")

if file:
    wrapper.image(file.read(),use_column_width=True)
    img =  Image.open(file) # convert file data into pillow image object
    if isinfovisible:
        st.sidebar.subheader("Image info")
        st.sidebar.markdown(f'''
        - *resolution* = {img.size}
        - *mode* = {img.mode}
        - *format* = {img.format}
        ''')
        if img.info:
            st.write(img.info)
    uimg = img.filter(effects[img_effect])
    wrapper.image(uimg,caption=f'filter = {img_effect}',use_column_width=True)

if file and w and h and resizebtn:
    img =  Image.open(file) 
    uimg = img.resize(size=(w,h))
    wrapper.image(uimg, caption = f'{uimg.size}')

if file and textapply_btn:
    img =  Image.open(file) 
    fnt = ImageFont.truetype('myfont.ttf',size=60)
    imgdraw = ImageDraw.Draw(img)
    imgdraw.text((20,img.height-80),watermark_text,font=fnt)
    wrapper.image(img,use_column_width=True)



