# Social Media Management Project
#### Student: Andrew R. Darnall
#### Accademic year: 2022-2023

The goal of the project was to learn about <b>Time Series Forecasting</b>
and to confront the performances of different Machine Learning models
on the aforementioned task.

The initial goal was to study the behaviour of Regressors and Multi Layer Perceptrons however, while studying the task I discovered that data scientists and data analytics professionals in general, also use the ARIMA and LSTM models so I studied said models and applied them to this task

The sample data comes from a [kaggle challenge](https://www.kaggle.com/competitions/store-sales-time-series-forecasting) where the given data is an exported database split into several .csv files.

Do note that my analysis was limited by my experience since I am a senior at my bachelor's degree course in Computer Science, however I had fun exploring this wondeful field of Data Science and overall enjoyed testing the skills aquired by this amazing AI centered course.


## Overview of the notebook

I chose to use the <b>Google Colab</b> platform for its ease of use and amazing pre-configured environment (and computational power), however with the proper configuration the same notebook can be replicated in a locally hosted jupyter notebook

I first started by adequately pre-processing the data and removing all the columns that I didn't need from the dataframe

Then i aggregated all of the store sales based on the day in order to obtain temporal data with daily frequency.

I then applied a seasonal decomposition of the temporal data to visualize the trend and the seasonality based on the year.

The first model that I used to forecast future sales was a Linear Regressor, then I used a Polynomial Regressor with Ridge Regression, I used the GridSearchCV() object to find the appropriate hyper parameters for the model, such as the poylnomial's degree.

I trained the model on the training set and made an evaluation of it based on the test set data using the Mean Squared Error metric, implemented through the scikit-learn objects MAE(), I then used a simple sliding window subroutine where I used the last 15 days of the test set and iteratively fitted the model with the temporal data and obtained a forecast, which I appended to the window (thus making the window 'slide') and once the loop finished iterating, the remaining 15 values that I saved in a linked list were only the forecasts that I was looking for.

I repeated the same process of fitting the data based on the training set, evaluated the performance of the model based on the test set and obtained the forecasts with the sliding window routine, with the remainig models presented in the notebook.

I concluded that the Polynomial Regerssor, based on my experiments and limited experience, was indeed the best model for the Time Series Forecasting task, I did however find out that with a much more complex architecture and with a different format for the data, the LSTM model would've outperformed all models, perhaps I shall find out in a future project.

#### Disclaimer

The notebook is written in Italian since my degree course is said language however google translate should offer a suitable translation.
