import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):
    model=tf.keras.models.load_model("trained_model.keras")
    image=tf.keras.preprocessing.image.load_img(image_path,target_size=(128,128))
    input_arr=tf.keras.preprocessing.image.img_to_array(image)
    input_arr=np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index=np.argmax(prediction)
    return result_index

st.sidebar.title("Dashboard")
app_mode=st.sidebar.selectbox("select page",["Home","About","Disease Recognition"])

if(app_mode=="Home"):
    st.header("PLANTPAL")
    image="41335f5672f945e62e245dd843a69d30.jpg"
    st.image(image,use_column_width=True)
    st.markdown("""
                Welcome to the PlantPal! 🌿🔍
               
                Our mission is to help in identifying plant diseases efficiently. Upload an image of a plant, and our system will analyze it to detect any signs of diseases. Together, let's protect our crops and ensure a healthier harvest!
                हमारा मिशन पौधों की बीमारियों को पहचानने में मदद करना है। किसी पौधे की तस्वीर अपलोड करें, और हमारी सिस्टम उसे विश्लेषित करेगी ताकि किसी भी बीमारी के लक्षणों को पहचान सके। हम साथ मिलकर अपनी फसलों की सुरक्षा करेंगे और एक स्वस्थ परिपत्रक हासिल करेंगे!
                
                ### How It Works
                  1. **Upload Image:** Go to the **Disease Recognition** page and upload an image of a plant with suspected diseases.
                  2. **Analysis:** Our system will process the image using advanced algorithms to identify potential diseases.
                  3. **Results:** View the results and recommendations for further action.
                
                 1.**तस्वीर अपलोड करें:** **रोग पहचान** पृष्ठ पर जाएं और संदिग्ध बीमारियों वाले एक पौधे की तस्वीर अपलोड करें।
                 2. **विश्लेषण:** हमारी सिस्टम उन्नत एल्गोरिदम का उपयोग करके छवि को प्रसंस्कृत करेगी ताकि संभावित बीमारियों की पहचान कर सके।
                 3. **परिणाम:** परिणाम और आगे की कार्रवाई के लिए सिफारिशों को देखें।
               
                
                 ### Why Choose Us?
                 - **Accuracy:** Our system utilizes state-of-the-art machine learning techniques for accurate disease detection.
                 - **User-Friendly:** Simple and intuitive interface for seamless user experience.
                 - **Fast and Efficient:** Receive results in seconds, allowing for quick decision-making.
                
                 -**शुद्धता: हमारी सिस्टम उच्चतम गुणवत्ता के मशीन लर्निंग तकनीकों का उपयोग करती है जिससे बीमारी की सटीक पहचान हो सके।
                 -**उपयोगकर्ता-मित्रपूर्ण: सरल और संज्ञानात्मक इंटरफ़ेस जो सेमलेस उपयोगकर्ता अनुभव के लिए है।
                 -**तेज और कुशल: कुछ सेकंडों में परिणाम प्राप्त करें, जो त्वरित निर्णय लेने की अनुमति देता है।
                
                
                ### Get Started
                 Click on the **Disease Recognition** page in the sidebar to upload an image and experience the power of PlantPal!
                 साइडबार में रोग पहचान पृष्ठ पर क्लिक करें और एक तस्वीर अपलोड करें, और प्लांटपैल की शक्ति का अनुभव करें!
              
                
                ### About Us
                  Learn more about the project, our team, and our goals on the **About** page.
""")
elif(app_mode=="About"):
     st.header("About")
     st.markdown("""
    2022 BATCH
     VIT BHOPAL       
    """)

elif(app_mode=="Disease Recognition"):
    st.header("Disease Recognition")
    image_path=st.file_uploader("Choose an Image:")
    if (st.button("Show Image")):
        st.image(image_path,width=4,use_column_width=True)     
   
    if (st.button("Predict")):
        st.write("Our Prediction")
        result_index=model_prediction(image_path)
        class_name=['Healthy rice',
 '_BrownSpot',
 '_Healthy rice',
 '_Hispa',
 '_LeafBlast',
 'septoria',
 'stripe_rust']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))  

    