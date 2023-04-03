import streamlit as st

import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
#=========================================================================================

df = pd.read_csv('india.csv')
# ==================================fecth the state data from dataframe============================
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

# ==============================fecth the district wise data from dataframe===========================
district_list=list(df["District"].unique())

# Page 1: Data Visualization
def page_data_viz():
    st.title('State-by-State Comparison')

    # Select primary and secondary parameters
    primary = st.selectbox('Select Primary Parameter',df.columns[6:])
    secondary = st.selectbox('Select Secondary Parameter', df.columns[6:])

    # Create a bar chart to show the primary parameter for all states
    fig1 = px.bar(df, x='State', y=primary, height=600)
    fig1.update_layout(xaxis={'categoryorder': 'total descending'})
    st.plotly_chart(fig1, use_container_width=True)


    # Create a scatter plot to show the secondary parameter vs. primary parameter for all states
    fig2 = px.scatter(df, x=primary, y=secondary, color='State', hover_name='District', height=600)
    st.plotly_chart(fig2, use_container_width=True)


#================================================================================================================

def data_visualization():
    st.sidebar.title('Data Visualization about Sencus')

    selected_state = st.sidebar.selectbox('Select a state', list_of_states)
    primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
    secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

    plot = st.sidebar.button('Plot Graph')

    if plot:

        st.text('Size represent primary parameter')
        st.text('Color represents secondary parameter')
        if selected_state == 'Overall India':
            # plot for india
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                    size_max=35,
                                    mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

            st.plotly_chart(fig, use_container_width=True)
        else:
            # plot for state
            state_df = df[df['State'] == selected_state]

            fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                    size_max=35,
                                    mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

            st.plotly_chart(fig, use_container_width=True)
#================================================================================================================





def district_wise():
    states = sorted(df["State"].unique())
    selected_state = st.selectbox("Select a state", states)

    primary = st.sidebar.selectbox('Select Primary Parameter', df.columns[6:])
    #secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns))

    if selected_state:
        district_data = df[df["State"]==selected_state].groupby("District").agg({primary: "sum"}).reset_index()
        fig = px.bar(district_data, x="District", y=primary, height=600)
        fig.update_layout(xaxis={'categoryorder':'total descending'})
        st.plotly_chart(fig, use_container_width=True)


    # Create a scatter plot to show the secondary parameter vs. primary parameter for all states
    #-fig2 = px.scatter(df, x=primary, y=secondary, color='State', hover_name='District', height=600)
    #-st.plotly_chart(fig2, use_container_width=True)

#================================================================================================================


def page_about():
    # Title
    st.title('About this Project')

    # Introduction paragraph
    st.write(''' This web application that displays data from the Indian Census, allowing users to visualize various demographic and socio-economic indicators across different states and districts. The app is built using Streamlit and Plotly, and uses data processing libraries like Pandas and NumPy.
The app provides various visualization options, including scatter plots and scatter_mapbox, to help users gain insights into the data. Users can compare different states based on primary and secondary parameters selected from a dropdown menu. The results are displayed in a bar chart and scatter plot for easy comparison.
The project was developed by Me of data enthusiasts with a passion for building interactive data visualizations. I am Data Analyst Fresher. I am made the code for the project available on [GitHub].
    ''')

    # Subheadings
    st.header('Features')
    st.subheader('Data Visualization')
    st.write('The app provides various visualization options, including scatter plots and scatter_mapbox, to help users gain insights into the data.')

    st.subheader('State-by-State Comparison')
    st.write('Users can compare different states based on primary and secondary parameters selected from a dropdown menu. The results are displayed in a bar chart and scatter plot for easy comparison.')

    st.header('A Little About Me')
    st.write('''This project was developed by me of data enthusiasts with a passion for building interactive data visualizations.''')


    # some about me
    st.write('#### Rohit Verma')
    st.write('##### Data Analyst Fresher')
    st.write('##### Skills- *Data Visualization*, *Database Management*, *Database Design*, *Python*, *Web Scraping*, *Mysql*,*Tableau*')
    st.write('##### gamil- rohitvermav0021@gmail.com')
    st.write('##### linkedin - [Rohit verma](https://www.linkedin.com/in/rohit-verma-3094b8224/)')

    # Footer
    st.write('##### For more information and view the source code, visit our project on [GitHub](https://github.com/RohitVerma0021/india_cencus_project)')
    st.write("## My Other Projects")
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image('datacleaning.jpg', use_column_width=True)
        with col2:
            st.header(
                '[Data Cleaning and Structuring in MySQL](https://github.com/RohitVerma0021/Data-Cleaning-and-Structuring-in-MySQL)')
            st.write(
                'The project focuses on cleaning and structuring large datasets in MySQL using various MySQL functions. Data cleaning is a crucial step in data analysis, where raw data is transformed into a clean and structured format, ready for further analysis. The project will use various MySQL functions to clean data such as SUBSTRING_INDEX(), LEFT(), and TRIM(). These functions can separate, remove, or replace specific parts of the data in columns, making it easier to work with the data.')

    # Second project
    with st.container():
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image('webscrapin.jpg', use_column_width=True)
        with col2:
            st.header(
                '[Web-Scraping-Project](https://github.com/RohitVerma0021/Web-Scraping-Project-Flipkart-Mobile-Data)')
            st.write(
                "In this project, I scraped mobile data from e-commerce using Python and Beautiful Soup. The goal was to gather information on 984 mobiles from Flipkart's website, including product name, price, ratings, and specifications.")


#Second project

# Create multi-page app
pages = {
    'About_project':page_about,
    'Data Visualization📶': data_visualization,
    'State-by-State Comparison 🌍': page_data_viz,
    'District_wise🗺️':district_wise
}

st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', list(pages.keys()))

# Display the selected page
pages[page]()
