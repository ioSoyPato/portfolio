import streamlit as st
# import backend.mnist as mnist
import backend.sentiment as sentiment
import backend.regression as regression
import backend.classification as classification
import backend.temp as temp
import backend.house as house
import backend.ticket_price as ticket_price
import backend.chat as chat
import backend.dog as dog
import backend.task as task

# --------------------------
#  1. INITIAL CONFIGURATION
# --------------------------
st.set_page_config(
    page_title="Patricio's Portfolio",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS
with open('styles/main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --------------------------
#  2. NAVIGATION SIDEBAR
# --------------------------
st.sidebar.title("Patricio Villanueva Portfolio")
st.sidebar.markdown("""
    Data Science and Engineering student passionate about AI and Machine Learning.
    Based in Guadalajara, Mexico 🇲🇽
""")

# Add social links
st.sidebar.markdown("""
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/patricio-adulfo-villanueva-gio-a84288249/)
    [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ioSoyPato)
""")


st.sidebar.markdown("""
    ## 📂 Projects
    Select a project to explore
""")

page = st.sidebar.radio(
    "",
    (
        "🏠 About Me",
        # "🔢 MNIST Digit Recognition",
        "💭 Sentiment Analysis", 
        "📈 Regression Models",
        "🎯 Classification Models",
        "🌡️ Temperature Prediction",
        "🏘️ House Price Prediction",
        "✈️ Ticket Price Prediction",
        "🐶 Dog Breed Prediction",
        "📅 Task Manager",
        "💬 Chat with Me"
    )
)

# --------------------------
#  3. MAIN CONTENT
# --------------------------
if page == "🏠 About Me":
    st.title("About Me")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
            <style>
            .profile-section {
                padding: 20px;
                border-radius: 10px;
                background: white;
                margin-bottom: 20px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .profile-section:hover {
                transform: translateY(-2px);
                transition: transform 0.3s ease;
            }
            
            .section-title {
                color: #2E4057;
                font-size: 1.8em;
                margin-bottom: 15px;
                border-bottom: 2px solid #f0f0f0;
                padding-bottom: 10px;
            }
            
            .tech-stack {
                display: inline-block;
                background: #f8f9fa;
                padding: 5px 10px;
                border-radius: 15px;
                margin: 5px;
                font-size: 0.9em;
                color: #2E4057;
            }
            
            .highlight {
                color: #2E4057;
                font-weight: 500;
            }
            
            .experience-item {
                margin-bottom: 15px;
                padding: 10px;
                border-left: 3px solid #2E4057;
            }
            </style>

            <div class="profile-section">
                <h2 class="section-title">👋 Introduction</h2>
                <p>
                    Hi! I'm <span class="highlight">Patricio Villanueva</span>, a Data Science and Engineering student 
                    at ITESO University with a passion for solving complex problems through data-driven solutions. 
                    I specialize in machine learning, data analysis, and artificial intelligence applications.
                </p>
            </div>

            <div class="profile-section">
                <h2 class="section-title">🎓 Education</h2>
                <div class="experience-item">
                    <h3>B.S. in Data Science and Engineering</h3>
                    <p>ITESO University | Expected Graduation: 2025</p>
                    <p><strong>Key Achievements:</strong></p>
                    <ul>
                        <li>GPA: 3.9/4.0</li>
                        <li>Best Project Award at Data Science Class Competition 2024</li>
                        <li> Project presented at a nacional conference at IBERO</li>
                        <li> Top 100 score in Kaggle competitions</li>
                    </ul>
                </div>
            </div>

            <div class="profile-section">
                <h2 class="section-title">💼 Professional Experience</h2>
                <div class="experience-item">
                    <h3>Solutions Partner for Google</h3>
                    <p>Semantiks Pro Services | January 2025 - Present</p>
                    <ul>
                        <li>Provide expert implementation and integration solutions for Google Cloud and Zendesk platforms</li>
                        <li>Develop custom solutions leveraging AI and automation capabilities</li>
                        <li>Collaborate with enterprise clients to optimize their cloud and customer service workflows</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>AI Engineer</h3>
                    <p>Semantiks | December 2024 - Present</p>
                    <ul>
                        <li>Lead development of enterprise-grade LLM applications using RAG architectures</li>
                        <li>Design and implement AI workflows using LangChain and LangGraph frameworks</li>
                        <li>Optimize AI model performance and cost-effectiveness for production environments</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Data Engineer Mid-level</h3>
                    <p>Gio Consultores | Summer 2023</p>
                    <ul>
                        <li>Designed and implemented ETL pipelines for efficient data transfer between systems</li>
                        <li>Executed data cleaning and normalization processes across multiple database systems</li>
                        <li>Optimized database indexing resulting in 30% improvement in query performance</li>
                        <li>Streamlined data workflows for improved operational efficiency</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Data Science Research Assistant</h3>
                    <p>ITESO AI Lab | 2022-Present</p>
                    <ul>
                        <li>Leading research on computer vision applications in healthcare</li>
                        <li>Published paper at International Conference on Machine Learning 2023</li>
                        <li>Mentoring junior students in ML projects</li>
                    </ul>
                </div>
                <div class="experience-item">
                    <h3>Data Engineer Junior</h3>
                    <p>UNE Fortaleza | 2020-2022</p>
                    <ul>
                        <li>Developed basic ETL pipelines for data migration between legacy and new systems</li>
                        <li>Created and optimized SQL queries for business intelligence reporting</li>
                        <li>Maintained data quality processes across operational databases</li>
                        <li>Collaborated with analytics team to implement data access patterns</li>
                    </ul>
                </div>
            </div>

            <div class="profile-section">
                <h2 class="section-title">🌟 Featured Projects</h2>
                <p>Explore my portfolio using the sidebar to see detailed demonstrations of:</p>
                <ul>
                    <li>MNIST Digit Recognition using Deep Learning</li>
                    <li>Natural Language Processing for Sentiment Analysis</li>
                    <li>Predictive Analytics for House Pricing</li>
                    <li>Time Series Analysis for Temperature Prediction</li>
                    <li>Computer Vision for Medical Image Analysis</li>
                    <li>Chatbot Development using Natural Language Processing</li>
                    <li>AI-powered Resume Analysis</li>
                    <li>Duckify Spotify like app with machine learning for songs recommendations</li>
                    <li>IOT based temperature prediction</li>
                    <li>Task Management App with Machine Learning</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("assets/193279258.jpeg", caption="Patricio Villanueva", use_container_width=True)
        
        # Contact Information 
        st.markdown("""
            <div class="profile-section">
                <h2 class="section-title">📫 Contact</h2>
                <p><strong>Email:</strong> patricio.villanueva@iteso.mx</p>
                <p><strong>Location:</strong> Guadalajara, Mexico</p>
                <p><strong>Languages:</strong> English (Fluent), Spanish (Native)</p>
                <p><strong>Celphone:</strong> +52 33 1763 9823</p>
                <p><strong>Email:</strong> pato@semantiks.ai</p>
            </div>
                    
            <h2 class="section-title">🛠️ Technical Skills</h2>
            <div>
                <p><strong>Programming Languages:</strong></p>
                <span class="tech-stack"><i class="fab fa-python"></i> Python</span>
                <span class="tech-stack"><i class="fab fa-r-project"></i> R</span>
                <span class="tech-stack"><i class="fas fa-database"></i> SQL</span>
                <span class="tech-stack"><i class="fab fa-java"></i> Java</span>
                <span class="tech-stack"><i class="fas fa-code"></i> C</span>
                <span class="tech-stack"><i class="fas fa-code"></i> C++</span>
                <span class="tech-stack"><i class="fas fa-gem"></i> Ruby</span>
                <span class="tech-stack"><i class="fab fa-js"></i> JavaScript</span>
                <span class="tech-stack"><i class="fab fa-js"></i> TypeScript</span>
                <span class="tech-stack"><i class="fas fa-code"></i> HTML</span>
                <span class="tech-stack"><i class="fas fa-code"></i> CSS</span>
                <span class="tech-stack"><i class="fas fa-code"></i> SCALA</span>
            </div>
                    
            <div>
                    <p><strong>ML/AI Frameworks:</strong></p>
                    <span class="tech-stack"><i class="fas fa-brain"></i> TensorFlow</span>
                    <span class="tech-stack"><i class="fas fa-fire"></i> PyTorch</span>
                    <span class="tech-stack"><i class="fas fa-cogs"></i> scikit-learn</span>
                    <span class="tech-stack"><i class="fas fa-network-wired"></i> Keras</span>
                    <span class="tech-stack"><i class="fas fa-link"></i> LangChain</span>
                    <span class="tech-stack"><i class="fas fa-project-diagram"></i> LangGraph</span>
                </div>
                <div>
                    <p><strong>Data Processing & Visualization:</strong></p>
                    <span class="tech-stack"><i class="fas fa-table"></i> Pandas</span>
                    <span class="tech-stack"><i class="fas fa-calculator"></i> NumPy</span>
                    <span class="tech-stack"><i class="fas fa-chart-line"></i> Matplotlib</span>
                    <span class="tech-stack"><i class="fas fa-chart-bar"></i> Seaborn</span>
                </div>
                <div>
                    <p><strong>Tools & Platforms:</strong></p>
                    <span class="tech-stack"><i class="fab fa-git-alt"></i> Git</span>
                    <span class="tech-stack"><i class="fab fa-docker"></i> Docker</span>
                    <span class="tech-stack"><i class="fab fa-aws"></i> AWS</span>
                    <span class="tech-stack"><i class="fab fa-ship"></i> Kubernetes</span>
                    <span class="tech-stack"><i class="fas fa-bolt"></i> Apache Spark</span>
                    <span class="tech-stack"><i class="fas fa-stream"></i> Apache Kafka</span>
                    <span class="tech-stack"><i class="fas fa-wind"></i> Apache Airflow</span>
                    <span class="tech-stack"><i class="fas fa-database"></i> Apache Hadoop</span>
                </div>
            </div>
            <div class="profile-section">
                <h2 class="section-title">🏆 Certifications & Achievements</h2>
                <ul>
                    <li>AWS Certified Machine Learning - Specialty (2023)</li>
                    <li>Google Data Analytics Professional Certificate (2023)</li>
                    <li>1st Place - National Data Science Hackathon (2022)</li>
                    <li>ITESO Excellence Scholarship Recipient (2020-2024)</li>
                </ul>
            </div>
            
            <div class="profile-section">
                <h2 class="section-title">🎯 Hobbies & Interests</h2>
                <span class="tech-stack"><i class="fas fa-swimmer"></i> Swimming</span>
                <span class="tech-stack"><i class="fas fa-music"></i> Music</span>
                <span class="tech-stack"><i class="fas fa-gamepad"></i> Gaming</span>
                <span class="tech-stack"><i class="fas fa-film"></i> Anime</span>
                <span class="tech-stack"><i class="fas fa-code"></i> Coding</span>
                <span class="tech-stack"><i class="fas fa-calculator"></i> Maths</span>
                <span class="tech-stack"><i class="fas fa-brain"></i> AI</span>
                <span class="tech-stack"><i class="fas fa-calculator"></i> Physics</span>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/patricio-adulfo-villanueva-gio-a84288249/)
            [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ioSoyPato)
        """, unsafe_allow_html=True)

        # 

elif page == "🔢 MNIST Digit Recognition":
    st.title("MNIST Digit Recognition")
    st.markdown("""
        This project demonstrates a neural network's ability to recognize handwritten digits.
        
        ### Technologies Used:
        - TensorFlow/Keras
        - Convolutional Neural Networks (CNN)
        - Image Processing
    """)
    # mnist.show_project()

elif page == "💭 Sentiment Analysis":
    sentiment.show_project()

elif page == "🌡️ Temperature Prediction":
    temp.show_project()

elif page == "📈 Regression Models":
    regression.show_project()

elif page == "🎯 Classification Models":
    classification.show_project()

elif page == "🏘️ House Price Prediction":
    house.show_project()    

elif page == "✈️ Ticket Price Prediction":
    ticket_price.show_project()

elif page == "💬 Chat with Me":
    chat.show_project()

elif page == "🐶 Dog Breed Prediction":
    dog.show_project()

elif page == "📅 Task Manager":
    task.show_project()

# [Continue with other pages...]

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', unsafe_allow_html=True)
