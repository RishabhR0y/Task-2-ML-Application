import streamlit as st
import pickle


def welcome():
    return 'welcome all'


def prediction(carat,cut,color,clarity,x,y,z,depth,table):
    print(prediction)
    return prediction


# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Predict the Diamond Price Using Streamlit")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:orange;padding:14px">
    <h1 style ="color:black;text-align:center;"> Diamond Price Prediction ML App </h1>
    </div>
    <h2> Enter the details </h2>
    
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    dataset = st.selectbox('Select Dataset',['diamonds.csv'])
    carat = st.number_input('Carat Weight:', min_value=0.1, max_value=10.0, value=1.0)
    cut = st.selectbox('Cut Rating:', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox('Color Rating:', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = st.selectbox('Clarity Rating:', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

    x = st.number_input('Diamond Length (X) in mm:', min_value=0.1, max_value=100.0, value=1.0)
    y = st.number_input('Diamond Width (Y) in mm:', min_value=0.1, max_value=100.0, value=1.0)
    z = st.number_input('Diamond Height (Z) in mm:', min_value=0.1, max_value=100.0, value=1.0)

    depth = st.number_input('Diamond Depth Percentage:', min_value=0.1, max_value=100.0, value=1.0)
    table = st.number_input('Diamond Table Percentage:', min_value=0.1, max_value=100.0, value=1.0)


    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(carat,cut,color,clarity,x,y,z,depth,table)
    st.success('The price of your diamond is  {}'.format(result))


if __name__ == '__main__':
    main()