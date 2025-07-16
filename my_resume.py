import streamlit as st

# Set up page
st.set_page_config(page_title="Tushar Mazumdar - CV", layout="wide")

# CSS styling
# st.markdown("""
#     <style>
#         h1, h2, h3 {
#             color: #006d77;
#             font-family: 'Segoe UI', sans-serif;
#             text-align: center;
#         }
#         p, li {
#             font-size: 16px;
#             line-height: 1.6;
#         }
#         hr {
#             border: none;
#             border-top: 2px solid #ccc;
#             margin: 1rem 0;
#         }
#         .section {
#             background-color: #ffffff;
#             padding: 1rem 2rem;
#             border-radius: 10px;
#             margin-bottom: 30px;
#             box-shadow: 0 4px 10px rgba(0,0,0,0.05);
#         }
#         .sidebar {
#             width: 100%;
#         }
#         /* Change sidebar width */
#         [data-testid="stSidebar"] {
#             width: 360px !important;  /* Adjust the width here */
#         }
# 
#         /* Optional: Push main content accordingly */
#         [data-testid="stSidebar"] > div:first-child {
#             width: 360px !important;
#         }
#     </style>
# """, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("""
    <div class='sidebar'>
        <h1>Tushar Mazumdar</h1>
        <div style='text-align: center;'>
        📧 tushar.mazumdar2013@gmail.com 
        </br>
        📞 +91-9818761795
        <a href='https://linkedin.com/in/tushar-mazumdar' style='text-decoration: none; color: #016e77;'>🔗 LinkedIn</a>
        <a href='https://github.com/tushar2013'  style='text-decoration: none; color: #016e77;'>💻 GitHub</a>
        </div>
    </div>
""", unsafe_allow_html=True)

page = st.sidebar.radio('', [
    "📝 Summary",
    "💼 Experience",
    "📊 Projects",
    "💻 Skills",
    "🎓 Education"
])

# Optional CV download
# Todo

# Summary
if page == "📝 Summary":
    st.markdown("<h1 class='section'> Summary </h1> <p> Aspiring Data Scientist with 9+ years of experience in DevOps, automation,and quantitative operations. Currently completing a Data Science course focused on machine learning, statistical modeling, and Python-based data workflows. Passionate about transforming data into actionable insights using real-world experience in trading systems and monitoring architectures. </p>", unsafe_allow_html=True)

# Experience
elif page == "💼 Experience":
    st.markdown("<div class='section'><h1>Experience</h1>", unsafe_allow_html=True)

    st.markdown("### Kivi Capitals — Trade Operations Analyst (Apr 2024 – Nov 2024)", unsafe_allow_html=True)
    st.markdown("""
    - Deployed 20+ Airflow DAGs automating tasks — reduced manual work by 80%  
    - Built Python and Bash scripts for diagnostics and alerts — improved response by 30%  
    - Developed 3+ Streamlit dashboards  
    - Managed TIG/TICK stack for monitoring; 500k datapoints/day  
    - Created Grafana dashboards — reduced triage time by 40%  
    - Used Ansible + GitLab CI to automate provisioning of 15+ servers
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("### Purplesigma LLP — Trade Operations Analyst (Apr 2019 – Apr 2024)", unsafe_allow_html=True)
    st.markdown("""
    - Developed Python-based reconciliation system for 10k+ trades/day — cut manual effort by 95%  
    - Real-time TIG stack monitoring — reduced issue response to <5 mins  
    - Created dashboards for 25+ risk signals  
    - Automated reporting and health checks — reduced ops load by 40%  
    - Collaborated with traders to ensure compliance
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("### TEOCO — Product Support Engineer (Jul 2016 – Apr 2019)", unsafe_allow_html=True)
    st.markdown("""
    - Managed ETL pipelines for 500+ files/day  
    - Built shell/cron-based log analysis system — reduced incidents by 25%  
    - Supported Oracle PL/SQL backend — schema tuning, patching
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("### IIT Kanpur — Project Associate (Jan 2015 – Aug 2016)", unsafe_allow_html=True)
    st.markdown("""
    - Built web UI for IoT vehicle project using HTML/CSS/JS  
    - Developed Arduino-based surveillance robot
    </div>
    """, unsafe_allow_html=True)

# Projects
elif page == "📊 Projects":
    st.markdown("<div class='section'><h1>Projects</h1>", unsafe_allow_html=True)

    st.markdown("**Retail Sales Forecasting — Walmart**", unsafe_allow_html=True)
    st.markdown("""
    - Tools: Python, Pandas, Statsmodels (SARIMAX), XGBoost  
    - Modeled CPI and seasonal factors  
    - Built hybrid time-series forecast for next 12 weeks  
    - Visualized store correlations with heatmaps
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("**Energy Forecasting — Facebook Prophet**", unsafe_allow_html=True)
    st.markdown("""
    - Tools: Python, Prophet, Matplotlib, Plotly  
    - Cleaned/resampled time series; removed outliers  
    - Used Prophet decomposition plots + cross-validation  
    - Delivered <10% error over 30-day predictions
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("**Student Dropout Prediction — Decision Tree**", unsafe_allow_html=True)
    st.markdown("""
    - Tools: Scikit-Learn, Graphviz, Seaborn  
    - Built decision tree model on student data  
    - Tuned hyperparameters; visualized final tree  
    - Extracted decision paths and classification rules
    </div>
    """, unsafe_allow_html=True)

# Technologies
elif page == "💻 Skills":
    st.markdown("<div class='section'><h1> Skills </h1>", unsafe_allow_html=True)
    st.markdown("""
    - **Scripting:** Bash, Python (Pandas, Numpy, Scikit-Learn, Flask)  
    - **Configuration Management:** Ansible  
    - **CI/CD:** GitLab, Jenkins  
    - **Containerization:** Docker  
    - **Monitoring & Logging:** Prometheus, ELK, TIG Stack  
    - **Version Control:** Git  
    - **Databases:** SQL, PL-SQL, Oracle  
    - **Operating Systems:** Linux, UNIX, Windows  
    </div>
    """, unsafe_allow_html=True)

# Education
elif page == "🎓 Education":
    st.markdown("<div class='section'><h1>Education</h1>", unsafe_allow_html=True)
    st.markdown("""
    - **Data Science Certification** – Intellipaat (2024–2025)  
    - **MSc in Electronics** – UIET, Kanpur University – 65% (2011–2013)  
    - **BSc in Electronics** – DAV College, Kanpur University – 54% (2008–2011)
    </div>
    """, unsafe_allow_html=True)

