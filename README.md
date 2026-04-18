## END 2 END MACHINE LEARNING PROJECT

CREATE GITHUB REPO:
1. Create a git hub repo
2. Create your project folder - "ML"
3. open vs code in that folder
4. go to cmd terminal
5. create env -> python -m venv venv
6. inside venv -> git init , git add . , git commit, git push
7. You can see the readme file in your repository. 

ADD YOUR REQ : 
1. Create a requirements.txt file. 
2. Mention all the required Python libraries that you required for building your project.
3. Create new setup.py file in ML. (setup.py - python script included with Python written libraries to ensure that the program is installed correctly). 
4. Configure all the code and get the requirements() by pulling all the required libraries by requirements.txt
5. Then create a 'src' folder in ML. Then create a new file - '__init__.py'
6. Push your code to GitHub.

ADD FILES : 
1. In src, add components folder and then create : 
data_ingestion.py
data_transformation.py
model_trainer.py
2. In src, add pipeline folder and then create :
__init__py
exception.py
logger.py
utils.py

ADD EXCEPTIONS:
1. In exceptions.py, write the necessary code to create custom exceptions - to return the exceptions if any , while writing the code. 
2. error_message_detail - error function to get the error from sys along with line number
3. Define the Custom exception class to retrieve the error from above function.

ADD LOGGER:
1. In logger.py, write the necessary code for logging your important processes while going through out the project. 
2. In such complex projects involving 1000 processes, you need to track each and every process if they are completing fine or not. 
3. LOG_FILE - creates a time data log file in your logs folder. 
4. Code for creating the log path to create the LOG_FILE in your logs folder. 
5. logging.basicconfig - sets the rules for your logs on how it's written - enhances the time and date for each logging statement. 

JUPYTER NOTEBOOK (EDA & MODEL TRAINING) 
1. Create notebook folder and data folder inside it. 
2. Put your dataset inside data folder. 
3. Create 2 .ipynb files in notebook folder. 1 for EDA and 1 for Model training. 
4. Write the necessary code for both the files : 
EDA :
- Read the Data
- Data Cleansing
- Visualisation
MODEL TRAINING : 
- Train test split
- Encode categorical values & Scale your numerical values
- define evaluate_model() for calculating mse, mae and r2
- Apply all ML models - predict data, get the above scores from evaluate_model()
- Compare the R2 scores for all the models
- Train your model on the best model and predict the data. 
- Plot/Compare Actual and Predicted graph and draw the best fit line. 


DATA INGESTION : 
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



