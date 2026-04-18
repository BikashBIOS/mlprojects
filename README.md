# END 2 END MACHINE LEARNING PROJECT

## CREATE GITHUB REPO:
1. Create a git hub repo
2. Create your project folder - "ML"
3. open vs code in that folder
4. go to cmd terminal
5. create env -> python -m venv venv
6. inside venv -> git init , git add . , git commit, git push
7. You can see the readme file in your repository. 

## ADD YOUR REQUIREMENTS : 
1. Create a requirements.txt file. 
2. Mention all the required Python libraries that you required for building your project.
3. Create new setup.py file in ML. (setup.py - python script included with Python written libraries to ensure that the program is installed correctly). 
4. Configure all the code and get the requirements() by pulling all the required libraries by requirements.txt
5. Then create a 'src' folder in ML. Then create a new file - '__init__.py'
6. Push your code to GitHub.

## ADD FILES : 
1. In src, add components folder and then create : 
data_ingestion.py
data_transformation.py
model_trainer.py
2. In src, add pipeline folder and then create :
__init__py
exception.py
logger.py
utils.py

## ADD EXCEPTIONS:
1. In exceptions.py, write the necessary code to create custom exceptions - to return the exceptions if any , while writing the code. 
2. error_message_detail - error function to get the error from sys along with line number
3. Define the Custom exception class to retrieve the error from above function.

## ADD LOGGER:
1. In logger.py, write the necessary code for logging your important processes while going through out the project. 
2. In such complex projects involving 1000 processes, you need to track each and every process if they are completing fine or not. 
3. LOG_FILE - creates a time data log file in your logs folder. 
4. Code for creating the log path to create the LOG_FILE in your logs folder. 
5. logging.basicconfig - sets the rules for your logs on how it's written - enhances the time and date for each logging statement. 

## JUPYTER NOTEBOOK (EDA & MODEL TRAINING) 
1. Create notebook folder and data folder inside it. 
2. Put your dataset inside data folder. 
3. Create 2 .ipynb files in notebook folder. 1 for EDA and 1 for Model training. 
4. Write the necessary code for both the files : 
### EDA :
- Read the Data
- Data Cleansing
- Visualisation
### MODEL TRAINING : 
- Train test split
- Encode categorical values & Scale your numerical values
- define evaluate_model() for calculating mse, mae and r2
- Apply all ML models - predict data, get the above scores from evaluate_model()
- Compare the R2 scores for all the models
- Train your model on the best model and predict the data. 
- Plot/Compare Actual and Predicted graph and draw the best fit line. 


## DATA INGESTION : 
1. Above ipynb files were just for our learning purposes, but we need to apply that same logic in our data_ingestion.py file with professional project coding. 
2. It is the entry point of a typical Machine Learning pipeline. In industry terms, "Data Ingestion" is the process of taking raw data from a source and preparing it for the next stages.
3. dataclass is a concise way to create classes that primarily store data - acts as a folder manager - tells the code to save output into Artifacts folder. 
4. DataIngestion Class :
- Pass the dataclass into the ingestion_config.
- In initiate_data_ingestion() - read the data,
creates the artifacts folder (checks if exists or not), 
creates the csv file for raw data. 
- Train test split 
- Create the csv file for train data and test data.
- Return the train and test data path. 
5. Run the class using __main__ and initiate_data_ingestion() 



## DATA TRANSFORMATION
1. dataclass to save your preprocessor pickle file with all the rules to apply through out your code.
2. get_transformer_object() - create the pipeline to apply OneHotEncoder to categorical values and StandardScaler to the numerical values. Output is the preprocessor obj. 
3. initiate_transformation() - Take X and y - divide into training and test data. And then fit/transform with help of preprocessor. 
4. Here, after fit/transforming the training data and test data, we concatenate it with the target data(math score) using np.c_ (column wise concatenation). Then we get train_arr and test_arr.
5. Now your normalized data is now ready to use - train_arr, test_arr.
6. Save your preprocessor object in the pickle file. Use save_object() function that we need to write it in utils.py to call from there. Pass the file path from preprocessor_obj_path that we initialized in @dataclass to save in artifacts folder. (saving this for using it in web app for real time predictions). 
7. All things set, now to run this classes and functions, call it in the __main__ function in data_ingestion.py. Call the DataTransformation() and the initiate_data_transformation() with the train and test data we prepared in data_ingestion file. 


## MODEL TRAINER :
1. Create dataclass to initialize and save your pkl file in the artifacts folder when created.
2. Create ModelTrainer clas with initiate_model_trainer() function to input the train and test arr. 
3. Slice the X train and X test, y train and y test. Create the dict of models to apply. 
4. Train all your models based on your training and testing data in model_report with help of evaluate_models() which we have to add in utils.py - This evaluate_model() helps to train your data on that model, predict the values, and also evaluate the r2 score. 
5. This report_model then returns a dictionary where the keys are model names and the values are their R² scores.
6. Then find the best model score by evaluating the max score from model_report values.
7. Find the best model name based upon the keys for the best model score. 
8. save_object() - save your trained model config in the mentioned path in @dataclass.
9. predict your values in the best model and return the r2 score.
10. Now edit the main Data ingestion file. Import model_trainer.py and then call ModelTrainer() along with initiate_model_trainer(). 


## HYPER PARAMETER TUNING
1. Add the hyperparameters and implement GridSearchCV in utils.py (Comment the previous model training code as we are implementing the grid search training).
2. Pass the params in the evaluate_model().
3. Add the same params value in the model_report in model_trainer.py where you are calling evaluate_model().
4. Add the Hyperparameters of different models in a new dict - params in model_trainer.py.
5. Execute the data ingestion.py again with the new hyperparameter codes and it will give you a better output of your r2 score from the previous models. 