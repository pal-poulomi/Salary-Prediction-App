# Salary-Prediction-App
Web App to predict salary of software developers using the public Stack Overflow Developer 2020 Survey dataset and creating

### Data Collection and preprocessing
1. Link to Dataset: https://insights.stackoverflow.com/survey
2. This is a publicly available dataset and I used the 2020 dataset for this project. The dataset has ~63k rows and ~60 feature columns
3. I used 5 columns from the data and chose to use only full time employees data
4. Cleaned the dataset to remove missing values, formatted the dataset columns, visualized the distribution of the different categories and label encoded the text feature columns. Decided on using salary data that's within 10k and 250k range for the countries with >=400 datapoints, since most of the datapoints fell into this range of salary

### Regression model building
1. Since we are predicting the yearly salary of software developers here, its a regression task
2. I started with separating the feature set and the target column. Then split them into train and test sets. The train set will be used to train the machine learning models and the test set will be used to evaluate the models
3. I tested on 5 popular regression models -  Linear Regression, KNeighbors Regressor, XGBoost Regressor, Random Forest Regressor and Decision Tree Regressor
4. The model with the least root mean squared error (RMSE) and max R2 score is chosen and further used for hyperparameter tuning, to find the best possible combination with the least error for that particular model

### Making a prediction
1. Once the best possible model is built, I created an instance of the new data that can be used to use this regressor model to predict the salary given the country, years of experience and education of a new data point
2. The main regressor model and the necessary transformations are saved in a pickle file
3. Next, the pickle file is read with the input of the new data point
4. Finally we get the salary predicted of the new datapoint

### Model Deployment on Streamlit
1. Used Streamlit to create a Web App that predicts salary
2. The Web App has two dropdown inputs for the country and education and a slider for the years of experience. Once you choose the values for each feature click on the Calculate Salary button to get the predicted salary 
3. On the side panel, there's also the option to either stay on the Predict page or go to Explore page where yuo can check out the visualizations of the entire preprocessed dataset
4. A pie chart showing the %distribution of data across countries. A bar chart that showcases the distribution of mean salary based on country. A line chart showcasing the distribution of salary on the years of experience
