from django.shortcuts import render
import joblib
import os
from django.conf import settings
# Create your views here.

model = joblib.load(os.path.join(settings.BASE_DIR, 'model','spam_classifier_model.joblib'))
vectorizer = joblib.load(os.path.join(settings.BASE_DIR, 'model','tfidf_vectorizer.joblib'))

def home(request):
    context={}
    if request.method =="POST":
        message=request.POST.get('message')
        X=vectorizer.transform([message])
        prediction=model.predict(X)[0]
        probas=model.predict_proba(X)[0]
        confidence=round(max(probas)*100,2)
        context={'message':message,'prediction':prediction,'confidence':confidence}

    return render(request,'home.html',context)
    
    
