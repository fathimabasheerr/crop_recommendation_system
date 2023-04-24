from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import random
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.linear_model import LogisticRegression



finalresult = ''
def npk():
    n = random.randint(1, 100)
    p = random.randint(1, 100)
    k = random.randint(1, 100)
    context = {
        "n": n,
        "p": p,
        "k": k,
    }
    return context

def recommend(request):
     context = npk()
     # if request.method == 'POST':
     #    n = request.POST.get('n')
     #    p = request.POST.get('p')
     #    k = request.POST.get('k')
     #    temp = request.POST.get('temp')
     #    hum = request.POST.get('hum')
     #    ph = request.POST.get('ph')
     #    rain = request.POST.get('rain')
     #    return JsonResponse({'success': True})
     # else:
     #    return JsonResponse({'success': False})
     return render(request, 'recommend.html',context)

def index(request):
     return render(request,'home.html')

def products(request):
     return render(request,'products.html')

def model(inputlist):
     dataset=pd.read_csv('Crop_recommendation.csv')
     new_data = pd.DataFrame([{'N':inputlist[0],'P':inputlist[1],'K':inputlist[2],'temperature':inputlist[3], 'humidity':inputlist[4],'ph':inputlist[5],'rainfall':inputlist[6]}])
     scaler=StandardScaler()
     data = dataset.append(new_data)
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



     