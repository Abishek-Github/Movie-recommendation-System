
Movie Recommendation System

This project is a comprehensive movie recommendation system that leverages both content-based and collaborative filtering approaches to provide personalized movie suggestions. To further enhance recommendation accuracy, neural network models are also implemented. The system ultimately selects the best-performing model for movie recommendations.

Dataset: MovieLens 100k

The **MovieLens 100k** dataset is used for training and testing the recommendation system. 

- **Data Overview**: The dataset contains 100,000 ratings (on a scale of 1 to 5) provided by 943 users across 1,682 movies.
- **User Data**: Each user has rated at least 20 movies, and the dataset includes basic demographic information for each user.

**Technology Stack*

- **PySpark**: Used for implementing recommendation models efficiently, leveraging Spark’s distributed computing capabilities.
- **Streamlit**: Utilized to develop an interactive web application for users to explore and receive movie recommendations.
- **Python**: The code is compatible with Google Colab, Jupyter Notebook, and any environment that supports Python, allowing for flexible development and testing.

## Running the Application

To launch the web application:

1. Ensure you have Streamlit installed.
2. Run the following command in your terminal or command prompt:

   ```bash
   streamlit run Streamlit.py
   ```

   (Replace `Streamlit.py` with the actual file name if it differs.)

## Project Highlights

- **Hybrid Recommendation System**: Combines content-based and collaborative filtering methods to create robust recommendations.
- **Neural Network Enhancements**: Neural networks are implemented to improve model performance and recommendation accuracy.
- **Model Selection**: The final recommendation model is selected based on performance metrics to ensure optimal results.

This project provides a powerful movie recommendation system, easily accessible through an interactive web interface.
