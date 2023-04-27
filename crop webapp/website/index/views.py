from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from django.http import JsonResponse

context1 = {}
def recommend(request):
     print("context1")
     context = {}
     # context['outputs']=''
     global context1
     outputs=''
     csv_data = pd.read_csv('input.csv', header=0) #to read input csv from the arduino ide
     # Convert the dataframe to a dictionary of lists
     data = csv_data.to_dict('list')

     # Print the resulting dictionary
     print("*********************",data)
     n = data['n'][-1] #taking n from the last row of the input csv
     p = data['p'][-1] #taking p from the last row of the input csv
     k = data['k'][-1] #taking k from the last row of the input csv
     temperature = data['temperature'][-1] #taking temp from the last row of the input csv
     humidity = data['humidity'][-1] #taking humidity from the last row of the input csv
     ph = data['ph'][-1] #taking ph from the last row of the input csv
     if request.method == 'POST':
        dataList = list(json.loads(request.POST['dataList']))
        dataList = list(dataList)
        dataLists = []
        for i in dataList:
             dataLists.append(float(i))
        outputs = str(model(dataList))
     context['n'] = n
     context['p'] = p
     context['k'] = k
     context['temperature'] = temperature
     context['humidity'] = humidity
     context['ph'] = ph
     context['o'] = outputs
     context1 = context
     # print(context1)
     return render(request, 'recommend.html',context1)
     

def redirect_form_data(request):
     print("Entered output()")
     outputs1 = ""
     if request.method == 'POST': #for loading data from the div tag and converting it into json
        dataList = list(json.loads(request.POST['dataList']))
        dataList = list(dataList)
        print("datalist - ", dataList)
     #    for i in dataList:
     #         dataLists.append(i)
     #    print(dataLists)
        outputs1 = str(model(dataList))
     print("outputs  - " , outputs1)
     return render(request, 'recommend.html',context1)

def index(request):
     return render(request,'home.html')

def products(request):
     return render(request,'products.html')

def model(inputlist):
     dataset=pd.read_csv('Crop_recommendation.csv') #read csv
     new_data = pd.DataFrame([{'N':inputlist[0],'P':inputlist[1],'K':inputlist[2],'temperature':inputlist[3], 'humidity':inputlist[4],'ph':inputlist[5],'rainfall':inputlist[6]}]) #input data from csv
     print(new_data.shape)
     scaler=StandardScaler()
     #data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
     data = pd.concat([dataset,pd.DataFrame(new_data)],ignore_index= True)
     scaler.fit(data.drop("label",axis=1))
     Scaler_feature=scaler.transform(data.drop("label",axis=1))
     new_dataset=pd.DataFrame(Scaler_feature,columns=data.columns[:-1])
     predict = new_dataset[-1:]
     x = new_dataset[:-1]
     y = dataset['label']
     xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state=42,test_size=0.4)
     knn = KNeighborsClassifier(n_neighbors=47)
     gnb = GaussianNB()
     bnb = BernoulliNB()
     clf = DecisionTreeClassifier()
     clf2=svm.SVC(kernel='linear')
     log = LogisticRegression()

     log.fit(xtrain, ytrain)
     clf2.fit(xtrain,ytrain)
     clf.fit(xtrain,ytrain)
     knn.fit(xtrain,ytrain)
     gnb.fit(xtrain,ytrain)
     bnb.fit(xtrain,ytrain)

     yprednew = knn.predict(predict)
     bprednew = bnb.predict(predict)
     gprednew = gnb.predict(predict)
     tree = clf.predict(predict)
     prednew = clf2.predict(predict)
     logs=log.predict(predict)

     listsOfCropsFinal = []

     listsOfCropsFinal.append(yprednew[0]) #knn
     listsOfCropsFinal.append(gprednew[0]) #Gaussian
     listsOfCropsFinal.append(bprednew[0]) #Bernoulli
     listsOfCropsFinal.append(tree[0])     #Decision Tree
     listsOfCropsFinal.append(prednew[0])  #Svm
     listsOfCropsFinal.append(logs[0])     #logistic

     max_occurrences = []
     for i in listsOfCropsFinal:
          countOfstring= listsOfCropsFinal.count(i)
          max_occurrences.append(countOfstring)
     #print(max_occurrences)
     output = listsOfCropsFinal[max_occurrences.index(max(max_occurrences))]
     #print(output)
     return output
     

def contact(request):
     return render(request,'contact.html') 

def about(request):
     return render(request,'about.html')
def output(request):
     return render(request,"output.html")



     