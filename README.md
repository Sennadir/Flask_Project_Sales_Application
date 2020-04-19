# Visual Application for our Sales Prediction tool
It will help us interact easily with our model and easily try it.


# Environment and tools
1. scikit-learn
2. pandas
3. numpy
4. flask
5. werkzeug
6. pickle
7. time

# Usage

## Application Launch

* First start by installing the requirement :
`pip install scikit-learn pandas numpy flask werkzeug pickle time`

* Browse using the terminal to the folder containing the project:
`cd Application`

* Next, and in case it's the first time using the model, you will have to train it :
`python model.py`

* Then you should launch the app in a terminal.
`python app.py`

* And finally, through the terminal you will get a link to your application. By default it's : http://127.0.0.1:5000/.

## Model Usage

* In order to use the model, you will have to browse a Test Set which has exactly the same columns as the Training Set (Without the Labels of course :-)).

* Because we can't display the totality of the prediction for the different stores, we have chosen to only display 2 Stores (The ones with the majority of samples) and the predicted values for all stores could be found in a generated CSV File that could be found in the Prediction Folder.


# File Structure

The folder containing the project should be structured as follows :

* [static] (It's the folder containing the different CSS and JS files)
* [Model] (It's the Model Construction Files and the Model itself)
* [Prediction] (It's the folder containing the predictions that would be generated for the user)
* [templates] (It's the folder containing the different HTML Files)
* [data] (It's the folder containing the data)

# About the project
## Context
The context of the project is purely educational. It's a project that have been conducted in the context of the Course Machine Learning Business Case deserved in the M2 Data Science of Ecole Polytechnique.

## Authors :
* Clotilde MIURA
* Manon RIVOIRE
* Rym GASSI
* Alexis GERBAUX
* Sofiane ENNADIR
