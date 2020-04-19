import warnings
warnings.filterwarnings("ignore")

from flask import Flask,render_template,url_for,request,redirect
import json, random
from werkzeug.utils import secure_filename

import pandas as pd
import numpy as np
import pickle
import time

from Model.preprocess import data_preprocessed
from sklearn.externals import joblib

app = Flask(__name__)

validation = pd.read_csv('./data/validation.csv')
x = pd.read_csv('./data/train.csv',  parse_dates=['Date'])
store_data =  pd.read_csv('./data/store.csv')
sales_by_date = x.groupby('Date').agg({'Sales':['mean', 'std']})
sales_by_date = sales_by_date['2015']
data = sales_by_date['Sales'].reset_index()

temp = pd.merge(x, store_data, on="Store")
temp_1 = pd.DataFrame(temp['StoreType'].value_counts()).reset_index()
temp_2 = pd.DataFrame(temp['Assortment'].value_counts()).reset_index()

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]


@app.route("/")
def chart():

    legend = 'Moyennes Ventes'
    legend_1 = 'Ecart-Type Ventes'
    labels = data['Date']
    lab_1 = data['Date']
    values = data['mean']
    val_1 = data['std']


    chart_lab = ['Store Type ' + t for t in temp_1['index']]
    chart_val = temp_1['StoreType']


    lab_2 = ['Assortiment ' + t for t in temp_2['index']]
    val_2 = temp_2['Assortment']
    legend_2 = 'Total'

    return render_template('index.html', \
        values=values, labels=labels, legend=legend,\
         val_1 = val_1, lab_1 = lab_1, legend_1 = legend_1,\
         val_2 = val_2, lab_2 = lab_2, legend_2 = legend_2,\
          set=zip(chart_val, chart_lab, colors))


@app.route('/pie')
def load_second_page():
   return render_template('pie_chart.html', values = validation['Sales'], \
    labels = validation['Date'],legend = 'Réelle', \
    val_1 = validation['Pred'], lab_1 = validation['Date'], legend_1 = 'Predictions')


rf = joblib.load("./Model/model_rf.pkl")

@app.route('/pred', methods = ['GET', 'POST'])
def predict():
    f = request.files['file']

    if f.filename.split('.')[-1] == 'csv':
        f.save('./data/' + secure_filename(f.filename))
        _ = pd.read_csv('./data/' + secure_filename(f.filename))

        a = data_preprocessed('./data/' + secure_filename(f.filename))
        _['pred'] = list(rf.predict(a.processing()))
        _.to_csv('./Predictions/Predictions.csv')

        data_1 = _[_['Store'] == _['Store'].iloc[0]]
        values = data_1['pred']
        labels = data_1['Date']
        legend = 'Prediction Store' + str(_['Store'].iloc[0])

        data_2 = _[_['Store'] == _['Store'].iloc[1]]
        values_1 = data_2['pred']
        labels_1 = data_2['Date']
        legend_1 = 'Prediction Store ' + str(_['Store'].iloc[1])

        return render_template('pred.html', values = values, labels = labels,legend = legend, \
                        values_1 = values_1, labels_1 = labels_1,legend_1 = legend_1)

    else:
        return render_template('pie_chart.html', prediction_text='Return a valid file')


@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
