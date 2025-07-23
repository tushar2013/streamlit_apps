import streamlit as st

def wide_space_default():
    st.set_page_config(layout='wide')

wide_space_default()

with st.sidebar:
    topic = st.selectbox('Choose Topic',(
                'Data Science',
                'Statistics',
                'Streamlit',
            ))

if topic == 'Statistics':
    st.markdown(f'# 30 days of `{topic.upper()}`')
    day = st.selectbox('Start the Challenge', ('Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', ))
    if day == 'Day 1':
        st.markdown('# `Statistics` quantifies uncertainty by learning from.')
        st.markdown('''
            ---
            ## Two important properties of `data`:
              - #### `Center of the data`: The typical value of the data.
              - #### `Spread about the data`
        ''')
        st.image('center_and_spread.jpg', caption='Center and Spread')

        st.markdown('''
            ---
            ## `CENTER` of the Data
        ''')
        st.markdown('''- ### The `MEAN`''')
        st.latex(r'''\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i''')
        st.markdown('###### Example:')
        st.latex(r'X = [3, 5, 7, 7, 38]')
        st.latex(r'''\bar{{x}} = \frac{3 + 5 + 7 + 7 + 38}{5}''')
        st.latex(r'''\bar{{x}} = 12''')

        st.markdown('<hr style="border: 1px dashed gainsboro;">', unsafe_allow_html=True)

        st.markdown('''- ### The `MEDIAN`''')
        st.markdown('###### Example:')
        st.markdown('*For odd number of elements:* **`The middle value is the MEDIAN.`**')
        st.latex(r'X = [3, 5, 7, 7, 38]')
        st.latex(r'''{median} = {7}''')
        st.markdown('*For even number of elements:* **`The mean of the two middle values is the MEDIAN`**')
        st.latex(r'X = [3, 5, 7, 7]')
        st.latex(r'''{median} = \frac{5 + 7}{2} = {6}''')

        st.markdown('''
            ---
            ## Measures of the `SPREAD`
        ''')

        st.markdown('''
            - ### The `INTERQUARTILE RANGE`
                - IQR is based on median.
                - The idea is to divide the data into four equal groups and see how far apart the extreme groups are.
        ''')
        st.image('iqr_recpie.jpg', caption='Recipe for IQR')
        st.markdown('###### Example:')
        st.markdown('- ###### Step 1: `Arranging data in ascending order`')
        st.latex(r'X = [3, 5, 7, 7, 38]')
        st.markdown('- ###### Step 2: `Dividing data into two equal high and low groups`')
        st.latex(r'X_1 = [3, 5, 7]\, \\ X_2 = [7, 7, 38]')
        st.markdown('- ###### Step 3: `Median of low group becomes Q1`')
        st.latex(r'''Q1 = 5''')
        st.markdown('- ###### Step 3: `Median of high group becomes Q3`')
        st.latex(r'''Q3 = 7''')
        st.markdown('##### Now the InterQuartile Range or `IQR` is the difference between `Q3` and `Q1`')
        st.latex(r'''IQR = Q3 - Q1 \\ IQR = 7 - 5 \\ IQR = 2''')
        st.image('box_and_whiskers.jpg', caption='Box and Whiskers Plot', width=600)

        st.markdown('<hr style="border: 1px dashed gainsboro;">', unsafe_allow_html=True)

        st.markdown('''
            - ### The `STANDARD DEVIATION`
                - Standard deviation is based on mean.
                - To get standard deviation we calculate sample variance first.
        ''')
        st.markdown('''#### `SAMPLE VARIANCE` ''')
        st.latex(r'''\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{N} (x_i - \bar{x})^2''')
        st.markdown('###### Example:')
        st.latex(r'X = [3, 5, 7, 7, 38]') 
        st.latex(r'\bar{x} = 12')
        st.latex(r'''\sigma^2 = \frac{(3  - 12)^2 + (5  - 12)^2 + (7  - 12)^2 + (7  - 12)^2 + (38 - 12)^2}{5-1}''')
        st.latex(r'''\sigma^2 = \frac{81 + 49 + 25 + 25 + 676}{4}''')
        st.latex(r'''\sigma^2 = 214''')
        st.markdown('''
            - But a spread measure should have the same unit as original data.
            - The obvious thing to do is to take the sqaure root.
        ''')
        st.latex(r'''\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{N} (x_i - \bar{x})^2}''')
        st.latex(r'''\sigma = \sqrt{214} = 14.63''')
    elif day == 'Day 2':
        st.markdown('# `Probability` is the formal study of the laws of chances.')
    elif day == 'Day 3':
        st.markdown('# Coming Soon.....')
    elif day == 'Day 4':
        st.markdown('# Coming Soon.....')
    elif day == 'Day 5':
        st.markdown('# Coming Soon.....')
elif topic == 'Data Science':
    st.markdown(f'# 30 days of `{topic.upper()}`')
elif topic == 'Streamlit':
    st.markdown(f'# 30 days of `{topic.upper()}`')
