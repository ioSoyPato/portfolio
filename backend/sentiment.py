import streamlit as st
from textblob import TextBlob

def show_project():
    # Project Header
    st.markdown("""
        <div class="project-card">
            <h1>Sentiment Analysis</h1>
            <p>This tool analyzes the emotional tone of your text using Natural Language Processing. 
            Simply enter your text below and click analyze to see if the sentiment is positive, negative, or neutral.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Text Input Section
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    user_input = st.text_area(
        "Enter your text here:",
        height=150,
        placeholder="Type or paste your text here..."
    )
    
    # Analysis Button
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        analyze_button = st.button("Analyze Sentiment", use_container_width=True)
    
    # Results Section
    if analyze_button and user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        
        # Calculate confidence percentage (scaled from -1...1 to 0...100)
        confidence = abs(sentiment) * 100
        
        # Results card with custom styling
        st.markdown("""
            <div class="project-card results-card">
                <h3>Analysis Results</h3>
        """, unsafe_allow_html=True)
        
        # Display sentiment result with appropriate styling
        if sentiment > 0:
            st.markdown(f"""
                <div class="success">
                    <h2>😊 Positive Sentiment</h2>
                    <p>Confidence: {confidence:.1f}%</p>
                </div>
            """, unsafe_allow_html=True)
        elif sentiment < 0:
            st.markdown(f"""
                <div class="error">
                    <h2>😠 Negative Sentiment</h2>
                    <p>Confidence: {confidence:.1f}%</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="warning">
                    <h2>😐 Neutral Sentiment</h2>
                    <p>This text appears to be neutral in tone.</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Additional sentiment metrics
        st.markdown("""
            <div class="metrics-section">
                <h4>Detailed Metrics</h4>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Polarity", f"{sentiment:.2f}")
        with col2:
            st.metric("Subjectivity", f"{blob.sentiment.subjectivity:.2f}")
        
        # Add some context about the metrics
        st.markdown("""
            <div class="metrics-explanation">
                <p><strong>Polarity:</strong> Ranges from -1 (very negative) to 1 (very positive)</p>
                <p><strong>Subjectivity:</strong> Ranges from 0 (very objective) to 1 (very subjective)</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)  # Close results card
    
    # Add custom CSS
    st.markdown("""
        <style>
        .input-section {
            margin: 2rem 0;
        }
        .results-card {
            margin-top: 2rem;
            background: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .metrics-section {
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #eee;
        }
        .metrics-explanation {
            margin-top: 1rem;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 8px;
            font-size: 0.9rem;
        }
        .warning {
            background-color: #fff7e6;
            color: #805b10;
            border: 1px solid #ffe4b8;
            padding: 1.25rem;
            border-radius: 8px;
            margin: 1.25rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

    
if __name__ == "__main__":
    show_project()