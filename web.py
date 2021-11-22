from time import time
import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input
import time
from PIL import Image
import pandas as pd

st.set_page_config(page_title='BPLDID', page_icon='🍃', layout='wide')
st.title("BELL PEPPER LEAF DISEASE IMAGE DETECTION WEB SYSTEM")
st.markdown('##')
img = Image.open('leafy.jpg')
st.sidebar.image(img, width=None, use_column_width=None)
img = Image.open('leafy.jpg')
st.image(img, width=None, use_column_width=None)
st.sidebar.title("NAVIGATION BAR")
st.markdown('##')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

choice=st.sidebar.selectbox("Choose Here.",["HOME","IMAGE DETECTION","ABOUT US","CONTACT"])


if choice == "HOME":
    with st.spinner('Loading Please Wait...'):
        time.sleep(2)

        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
        }
        .big-font {
            font-family: Times New Roman !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: center;'>WELCOME TO THE HOME PAGE</h1>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h1 style='text-align: center; '>BELL PEPPER LEAF DISEASE INFORMATIONS</h1>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h1 style='text-align: center; '>Bacterial Spots</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; '>Description </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Bacterial spot is one of the most devastating diseases of pepper and tomato. The disease occurs worldwide where pepper and tomato are grown in warm, moist areas. When it occurs soon after transplanting and weather conditions remain favorable for disease development, the results are usually total crop loss.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Cause </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Bacterial leaf spot on peppers is a devastating disease that can cause disfiguration of the leaves and fruit. In severe cases, the plants may die. There is no cure once the disease takes hold, but there are several things you can do to prevent it and keep it from spreading, Causes lesions on the leaves that look as though they are soaked with water. These lesions normally begin on the lower leaves. As the disease progresses, it leaves a dark, purple-brown spot with a light brown center. Bacterial leaf spot on peppers causes spotting and raised cracks in the fruit. The cracks provide an opening for other disease pathogens.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Solution/Treatment </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Seed can be treated with hot water or calcium hypochlorite to kill the pathogen. Hot water treatment is more thorough than calcium hypochlorite because it can kill bacteria inside the seed as well as those on the surface.</p>', unsafe_allow_html=True)
        st.markdown('##')

        st.markdown('##')
        st.markdown("<h1 style='text-align: center;'>Cercospora Leaf Spots</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Description </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Any of several fungus diseases of plants caused by Cercospora species and characterized by areas of discoloration on the leaves. as individual, circular spots that are tan to light brown with reddish purple borders. As the disease progresses, individual spots coalesce. Heavily infected leaves first become yellow and eventually turn brown and necrotic.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Cause </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">This disease is caused by the fungus Cercospora hydrangea and is perhaps the most common disease seen on this ornamental during the months of July through October. The disease rarely kills the plant, but if it is severe, it can reduce overall plant vigor by repeated defoliation.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Solution/Treatment </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">One of them is to Avoid overwatering or watering in the late evening to reduce free moisture. Another is to Avoid overhead watering where the water can dislodge and disperse spores to uninfected plants. Or space out the plants to encourage air movement and reduce high humidity levels.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('##')
        st.markdown("<h1 style='text-align: center;'>Powdery Mildew</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Description </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Powdery mildew, plant disease of worldwide occurrence that causes a powdery growth on the surface of leaves, buds, young shoots, fruits, and flowers. Powdery mildew is causedby many specialized races of fungal species in the genera Erysiphe, Microsphaera, Phyllactinia, Podosphaera, Sphaerotheca, and Uncinula.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Cause </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Powdery mildew, mainly caused by the fungus Podosphaera xanthii, infects all cucurbits, including muskmelons, squash, cucumbers, gourds, watermelons and pumpkins. In severe cases, powdery mildew can cause premature death of leaves, and reduce yield and fruit quality.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Solution/Treatment </h2>", unsafe_allow_html=True)
        st.markdown('<p class="big-font">Combine one tablespoon baking soda and one-half teaspoon of liquid, non-detergent soap with one gallon of water, and spray the mixture liberally on the plants. Mouthwash. The mouthwash you may use on a daily basis for killing the germs in your mouth can also be effective at killing powdery mildew spores. Also along with using Fungicides that are highly effective with low toxicity, no residue, and long duration.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('##')


if choice == "IMAGE DETECTION":
    with st.spinner('Loading Please Wait...'):
        time.sleep(7)
        st.header("BELL PEPPER LEAF DISEASE IMAGE DETECTION")
        st.markdown('##')
        main_container = st.container()
        if "counter" not in st.session_state:
            st.session_state.counter = 0
        #if st.button("Reset"):
            #st.session_state.counter = 0    

        model = tf.keras.models.load_model("saved_model/mdl_wt.hdf5") 

        uploaded_file = st.file_uploader("Choose a image file", type="jpg")

        map_dict = {0: 'Not Healthy, Bacterial Spot',
                    1: 'Not Healthy, Cercospora Spot',
                    2: 'Healthy', 
                    3: 'Not Healthy, Powdery Mildew'}


        if uploaded_file is not None:
            # Convert the file to an opencv image.
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8) 
            opencv_image = cv2.imdecode(file_bytes, 1)
            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
            resized = cv2.resize(opencv_image,(224,224))
            # Now do something with the image! For example, let's display it:
            st.image(opencv_image, channels="RGB")

            resized = mobilenet_v2_preprocess_input(resized)
            img_reshape = resized[np.newaxis,...]

            Genrate_pred = st.button("Identify Image")    
            if Genrate_pred:
                prediction = model.predict(img_reshape).argmax()
                st.title("The Image Result Is {}".format(map_dict [prediction]))
                main_container.write(st.session_state.counter)
                st.session_state.counter + 1
             
            df = pd.read_csv("data/result.csv")
            st.write(df)
            options = st.header("Options")
            options_form = st.form("options_form")
            options.write("Please Fill Up The Form Below:")
            user_result = options_form.text_input("Image Result")
            user_age = options_form.text_input("Your Age")
            add_data = options_form.form_submit_button()
            if add_data:
                st.write(user_result,user_age)
                new_data = {"result": user_result , "age" : int(user_age)}
                st.write(new_data)
                df = df.append(new_data, ignore_index=True)
                df.to_csv("data/result.csv", index=False)
                st.success("Thank You! Please Head To Home Page For More Info")


if choice=="ABOUT US":
    with st.spinner('Loading Please Wait...'):
        time.sleep(1)
        
        st.markdown("""
        <style>
        .big-font {
            font-size:20px !important;
        }
        .big-font {
            font-family: Times New Roman !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: center;'>WELCOME TO ABOUT US PAGE</h1>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>About Us</h2>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('<p class="big-font">This web system is a system entitled Bell Pepper Leaf Disease Image Detection B-P-L-D-I-D which purpose is to help user to easily identify what kind of bell pepper leaf disease their photo have. This system is made to help user to lessen the hassle of identifying those kinds of bell pepper leaf disease by themselves. Here in this Web System it is composed of the Home page, Image Detection page, About page and Contact page.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('##')

        st.markdown("<h1 style='text-align: center;'>System Features:</h1>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Home Page:</h2>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('<p class="big-font">This is the main page and front page of the web system where you can move to other forms using the navigation bar and also in the main page is where you can find informations about the bell pepper leaf diseases.</p>', unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Image Detection Page:</h2>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('<p class="big-font">In this page of the system is where the users can input images of bell pepper leaf in order to identify whether it is healthy or what kind of disease the bell pepper leaf image have. Futhermore, it also have a navigation bar within this page that can allow users to go to other forms of the system.</p>', unsafe_allow_html=True)
        st.markdown('##')

        st.markdown("<h2 style='text-align: center;'>About Page:</h2>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('<p class="big-font">In this page it gives brief explanation of every features of this web system including the developers information. Futhermore, it also have a navigation bar within this page that can allow users to go to other forms of the system.</p>', unsafe_allow_html=True)
        st.markdown('##')

        st.markdown("<h2 style='text-align: center;'>Contact Page:</h2>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown('<p class="big-font">In this page you can find all the contacts that you can use to reach each of the people and developers behind this web system. Futhermore, it also have a navigation bar within this page that can allow users to go to other forms of the system.</p>', unsafe_allow_html=True)
        st.markdown('##')


if choice=="CONTACT":
    with st.spinner('Loading Please Wait...'):
        time.sleep(4)
    
        st.markdown("""
        <style>
        .big-font {
            font-size:22px !important;
        }
        .big-font {
            font-family: Times New Roman !important;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("<h1 style='text-align: center;'>WELCOME TO CONTACT PAGE</h1>", unsafe_allow_html=True)
        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>YOU CAN CONTACT US THROUGH</h2>", unsafe_allow_html=True)
        st.markdown('##')

        
        st.markdown("<h2 style='text-align: center;'>Contacts For:</h2>", unsafe_allow_html=True)
        st.subheader("Bryan Christopher C. Colis")
        st.markdown('##')
        b=st.selectbox("Contacts:",["Click Here","Phone Number","Personal Email","Gsuite Email"])
        if b=="Click Here":
            st.write("")
            st.markdown('<p class="big-font">Good Day Dear User!</p>', unsafe_allow_html=True)
        if b=="Phone Number":
            st.text("")
            st.markdown('<p class="big-font">09386732327</p>', unsafe_allow_html=True)   
        if b=="Personal Email":
            st.text("")
            st.markdown('<p class="big-font">colisbryan15@gmail.com</p>', unsafe_allow_html=True)
        if b=="Gsuite Email":
            st.text("")
            st.markdown('<p class="big-font">bryanchristopher.colis@g.batstate-u.edu.ph</p>', unsafe_allow_html=True)

        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Contacts For:</h2>", unsafe_allow_html=True)
        st.subheader("Denzl Eian A. Magtalas")
        st.markdown('##')
        d=st.selectbox("Contacts:",["Click  Here","Phone  Number","Personal  Email","Gsuite   Email"])
        if d=="Click  Here":
            st.write("")
            st.markdown('<p class="big-font">Good Day Dear User!</p>', unsafe_allow_html=True)
        if d=="Phone  Number":
            st.text("")   
            st.markdown('<p class="big-font">09557627411</p>', unsafe_allow_html=True)
        if d=="Personal  Email":
            st.text("")
            st.markdown('<p class="big-font">magtalas.denzl@gmail.com</p>', unsafe_allow_html=True)
        if d=="Gsuite  Email":
            st.text("")
            st.markdown('<p class="big-font">denzleian.magtalas@g.batstate-u.edu.ph</p>', unsafe_allow_html=True)


        st.markdown('##')
        st.markdown("<h2 style='text-align: center;'>Contacts For:</h2>", unsafe_allow_html=True)
        st.subheader("Rogell A. Gutierrez ")
        st.markdown('##')        
        r=st.selectbox("Contacts:",["Click   Here","Phone   Number","Personal   Email","Gsuite   Email"])
        if r=="Click   Here":
            st.write("")
            st.markdown('<p class="big-font">Good Day Dear User!</p>', unsafe_allow_html=True)
        if r=="Phone   Number":
            st.text("")
            st.markdown('<p class="big-font">09517106014</p>', unsafe_allow_html=True)
            
        if r=="Personal   Email":
            st.text("")
            st.markdown('<p class="big-font">gutierrezrogell1@gmail.com</p>', unsafe_allow_html=True)
        if r=="Gsuite   Email":
            st.text("")
            st.markdown('<p class="big-font">rogell.gutierrez@g.batstate-u.edu.ph</p>', unsafe_allow_html=True)

st.markdown("##")
img = Image.open('leafy.jpg')
st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.markdown("##")
st.sidebar.image(img, width=None, use_column_width=None, caption="Copyright: © 2021 Bell Pepper Leaf Disease Image Detection Web System.")
st.markdown("##")
st.markdown("##")
st.markdown("##")
img = Image.open('leafy.jpg')
st.image(img, width=None, use_column_width=None, caption="Copyright: © 2021 Bell Pepper Leaf Disease Image Detection Web System.")
