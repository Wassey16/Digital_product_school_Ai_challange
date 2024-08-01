---
title: Ai Challange
emoji: 🐠
colorFrom: purple
colorTo: red
sdk: docker
pinned: false
license: apache-2.0
---


# Digital Product School AI Challenge

## Project Overview

This project focuses on analyzing traffic data, visualizing it, and building predictive models to forecast future trends. The primary steps include data visualization, model training, and deployment of the best-performing model.

## Project Structure

- **ai_chalange.ipynb**: This Jupyter Notebook contains the entire workflow, including:
  - Data visualization and understanding
  - Training multiple machine learning models
  - Selecting the best-performing model based on evaluation metrics

- **xg_model.pkl**: The best-performing model, an XGBoost regressor, saved for deployment.

- **app.py**: A Flask web application that serves as an endpoint for:
  - **POST method**: For predicting future values based on the input data
  - **Web interface**: For user interaction

- **requirements.txt**: Lists all the dependencies required to run the project.

- **templates/home.html**: The HTML template for the web interface of the Flask app.

## How to Run

### Prerequisites

1. Python 3.x
2. Flask
3. XGBoost

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Wassey16/Digital_product_school_Ai_challange.git

2. Navigate to the project directory:
    ```bash
        cd Digital_Product_School_AI_Challenge

3. Install the required packages:
    ```bash
        pip install -r requirements.txt

### Running the Application

1. Start the Flask app:
    bash
        python app.py

2. Access the application at http://localhost:5000 or visit [Web page](https://wassey-16-ai-challange.hf.space) to use the deployed version.

### License
This project is licensed under the Apache License Version 2.0.

### Acknowledgments
1. Digital Product School for the challenge
2. XGBoost Documentation for model insights
3. HuggingFace for hosting the application
