from cmath import cos
from email import message
from pyexpat import model
from pyexpat.errors import messages
from django.shortcuts import render
import pickle
import pandas as pd
import numpy as np

from polls.models import details


model = pickle.load(open('ExtraTreesRegressor.pkl','rb'))
zomato = pd.read_csv('zomato.csv')


def home(request):
    location = zomato['location'].unique()
    rest_type = zomato['rest_type'].unique()
    cuisines = zomato['cuisines'].unique()
    return render(request,"index.html",{'location' : location ,'rest_type' : rest_type, 'cuisines' : cuisines})

def predict(request):

    locations = zomato['location'].unique()
    rest_type = zomato['rest_type'].unique()
    cuisines = zomato['cuisines'].unique()

    
    online_order = request.GET['online order']
    book_table = request.GET['book table']
    votes = int(request.GET['votes'])
    locations = (request.GET['location'])
    rest_type = request.GET['rest_type']
    cuisines = request.GET['cuisines']
    cost = int(request.GET['cost'])
    # detail = details(online_order=online_order,book_table=book_table,votes=votes,locations = locations,rest_type =rest_type,cuisines=cuisines,cost=cost)
    # detail.save()
   

        
    
    prediction = model.predict(pd.DataFrame([[online_order,book_table,votes,locations,rest_type,cuisines,cost]],columns=['online_order','book_table','votes','location', 'rest_type','cuisines','cost']))
    print(prediction)
    output=round(prediction[0],2)
    return render (request,'index.html',{'text' :output})
 
