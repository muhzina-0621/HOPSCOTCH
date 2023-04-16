from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.


def home(request):
    return render(request, "index.html")


def reg(request):
    msg = ""
    if request.POST:
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        # get not necessary can also use request.POST["name"]
        age = request.POST.get("Age")
        grade = request.POST.get("Grade")
        password = request.POST.get("Password")
        address = request.POST.get("Address")
        if Reg.objects.filter(email=email).exists():
            msg = 'Email Already Registered'
        else:
            logqry = Login.objects.create(
                email=email, password=password, usertype='user')
            logqry.save()
            abc = Reg.objects.create(
                name=name, email=logqry, password=password, age=age, grade=grade, address=address)
            abc.save()
            masg = "Registraion Successful"
            return HttpResponseRedirect("/login?msg"+msg)

    return render(request, "register.html", {"msg": msg})


def gologin(request):
    msg = ""
    if request.POST:
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        data = Login.objects.filter(email=email, password=password)
        if data:
            print(data)
            if data[0].usertype == "user":
                d = Login.objects.get(email=email)
                request.session['uid']=email
                typ = d.status
                if typ == "pending":
                    msg = "You are not approved yet"
                elif typ == "rejected":
                    msg = "Sorry you are rejected"
                elif typ == "approved":
                    msg = "Login Successful"
                    return HttpResponseRedirect("/user?msg="+msg)
            elif data[0].usertype == "admin":
                return HttpResponseRedirect("/admin?msg="+msg)

    return render(request, "login.html", {"msg": msg})


def user(request):
    msg = request.GET.get("msg")
    return render(request, "user/user.html", {"msg": msg})

def test3(request):
    msg = request.GET.get("msg")
    msg = ""
    uid=request.session['uid']
    print(uid+"RTYUIOP{}")
    if Mark.objects.filter(emailid=uid).exists():
        pass
    else:
        abc=Mark.objects.create(emailid=uid)
    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")
        q6 = request.POST.get("q6")
        q7 = request.POST.get("q7")
        q8 = request.POST.get("q8")
        q9 = request.POST.get("q9")
        q10 = request.POST.get("q10")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None and q6 != None and q7 != None and q8 != None and q9 != None and q10 != None):
            q1= int(q1)
            q2= int(q2)
            q3= int(q3)
            q4= int(q4)
            q5= int(q5)
            q6= int(q6)
            q7= int(q7)
            q8= int(q8)
            q9= int(q9)
            q10= int(q10)
            sum = q1 + q2 + q3+ q4+ q5 + q6 +q7 + q8 + q9 + q10
            print(sum)
            query=Mark.objects.filter(emailid=uid).update(reading=sum)
            print(query,"QRYYYYYYYYYYYYY")
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/dictation?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/test3?msg="+msg)

    return render(request,"user/test3.html", {"msg": msg})

def dictation(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']
    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None ):
            q1 = q1.lower()
            q2 = q2.lower()
            q3 = q3.lower()
            q4 = q4.lower()
            q5 = q5.lower()
            sum=0
            if (q1 == "tree"):
                sum = sum +2
            else:
                sum= sum + 0
        #==================
            if (q2 == "door"):
                sum = sum +2
           

        #==================
            if (q3 == "boy"):
                sum = sum +2
        
        #==================
            if (q4 == "ice"):
                sum = sum +2
       
        #==================
            if (q5 == "ball"):
                sum = sum +2
        
            print(sum)
            query=Mark.objects.update(dictation=sum)
            query=Mark.objects.filter(emailid=uid).update(dictation=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/match?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/dictation?msg="+msg)
    return render(request,"user/dictation.html", {"msg": msg})



def match(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']
    if request.POST:
        q1 = request.POST.get("coin")
        q2 = request.POST.get("star")
        q3 = request.POST.get("hut")
        q4 = request.POST.get("bell")
        q5 = request.POST.get("car")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None ):
            q1 = int(q1)
            q2 = int(q2)
            q3 = int(q3)
            q4 = int(q4)
            q5 = int(q5)
            sum = q1 + q2 + q3+ q4+ q5
            print(sum)
            query=Mark.objects.update(match=sum)
            query=Mark.objects.filter(emailid=uid).update(match=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/comprehension?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/match?msg="+msg)
      
    return render(request,"user/match.html", {"msg": msg})

def comprehension(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']
    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        if(q1 != None and q2 != None and q3 != None  ):
            q1 = int(q1)
            q2 = int(q2)
            q3 = int(q3)
            sum = q1 + q2 + q3
            print(sum)
    
            query=Mark.objects.update(comprehension=sum)
            query=Mark.objects.filter(emailid=uid).update(comprehension=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/fill?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/comprehension?msg="+msg)

       
    return render(request,"user/comprehension.html", {"msg": msg})

def fill(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']

    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        if(q1 != None and q2 != None and q3 != None ):
            q1 = q1.lower()
            q2 = q2.lower()
            q3 = q3.lower()
            sum=0
            if (q1 == "opening"):
                sum = sum +2
            
        #==================
            if (q2 == "cooking"):
                sum = sum +2
            else:
                sum= sum + 0

        #==================
            if (q3 == "reading"):
                sum = sum +2
            else:
                sum= sum + 0
        #==================
            print(sum)
            query=Mark.objects.update(fill=sum)
            query=Mark.objects.filter(emailid=uid).update(fill=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/user?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/fill?msg="+msg)
            
    return render(request,"user/fill.html", {"msg": msg})

def count(request):
    msg=""
    uid=request.session['uid']
     
    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        if(q1 != None and q2 != None and q3 != None  ):
            q1 = int(q1)
            q2 = int(q2)
            q3 = int(q3)
            sum=0
            if (q1 == 3):
                sum = sum +2
      
        #==================
            if (q2 == 12):
                sum = sum +2
      

        #==================
            if (q3 == 5 ):
                sum = sum +2
       
        #==================
            print(sum)
            query=Mark.objects.update(count=sum)
            query=Mark.objects.filter(emailid=uid).update(count=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/currency?msg="+msg)
        else:
            msg = "Answer every Question"
        return HttpResponseRedirect("/count?msg="+msg)
    
    return render(request,"user/count.html", {"msg": msg})
    

def currency(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']

    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        if(q1 != None and q2 != None and q3 != None  ):
            q1 = int(q1)
            q2 = int(q2)
            q3 = int(q3)
            sum=0
            if (q1 == 2):
                sum = sum +2
   
        #==================
            if (q2 == 100):
                sum = sum +2
        

        #==================
            if (q3 == 10 ):
                sum = sum +2
  
        #==================
            print(sum)
            query=Mark.objects.update(currency=sum)
            query=Mark.objects.filter(emailid=uid).update(currency=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/order?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/currency?msg="+msg)

     
    return render(request,"user/currency.html", {"msg": msg})

def order(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']

    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None):
            q1 = int(q1)
            q2 = int(q2)
            q3 = int(q3)
            q4 = int(q4)
            q5 = int(q5)
            sum=0
            if(q1 ==2 and q2 ==4 and q3 ==5 and q4 ==7 and q5 ==17):
                sum=2
        #==================
            print(sum)
            query=Mark.objects.update(order=sum)
            query=Mark.objects.filter(emailid=uid).update(arithmetic=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/solve?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/order?msg="+msg)
    
    return render(request,"user/order.html", {"msg": msg})

def solve(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']

    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")
        q6 = request.POST.get("q6")
        q7 = request.POST.get("q7")
        q8 = request.POST.get("q8")
        q9 = request.POST.get("q9")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None and q6 != None and q7 != None and q8 != None and q9 != None):
            q1= int(q1)
            q2= int(q2)
            q3= int(q3)
            q4= int(q4)
            q5= int(q5)
            q6= int(q6)
            q7= int(q7)
            q8= int(q8)
            q9= int(q9)
            sum=0
            if (q1 == 8):
                sum = sum +2
     
        #==================
            if (q2 == 10):
                sum = sum +2
        

        #==================
            if (q3 == 3 ):
                sum = sum +2
        
        #==================
            if (q4 == 33):
                sum = sum +2
        
        #==================
            if (q5 == 25):
                sum = sum +2
    

        #==================
            if (q6 == 6 ):
                sum = sum +2
        
        #==================
            if (q7 == 1):
                sum = sum +2
        
        #==================
            if (q8 == 113):
                sum = sum +2
        

        #==================
            if (q9 == 34 ):
                sum = sum +2
        
        #==================
            print(sum)
            query=Mark.objects.update(arithmetic=sum)
            query=Mark.objects.filter(emailid=uid).update(arithmetic=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/compare?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/order?msg="+msg)
    
    return render(request,"user/solve.html", {"msg": msg})

def compare(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid']

    if request.POST:
        q1 = request.POST.get("q1")
        q2 = request.POST.get("q2")
        q3 = request.POST.get("q3")
        q4 = request.POST.get("q4")
        q5 = request.POST.get("q5")
        if(q1 != None and q2 != None and q3 != None and q4 != None and q5 != None):
            q1= int(q1)
            q2= int(q2)
            q3= int(q3)
            q4= int(q4)
            q5= int(q5)
            sum=0
            if (q1 == 9):
                sum = sum +2
      
        #==================
            if (q2 == 21):
                sum = sum +2
       

        #==================
            if (q3 == 5):
                sum = sum +2
      
        #==================
            if (q4 == 10):
                sum = sum +2
        
        #==================
            if (q5 == 81):
                sum = sum +2
        

        #==================
            print(sum)
            query=Mark.objects.update(compare=sum)
            query=Mark.objects.filter(emailid=uid).update(compare=sum)
            msg = "Submitted Successfully"
            return HttpResponseRedirect("/user?msg="+msg)
        else:
            msg = "Answer every Question"
            return HttpResponseRedirect("/compare?msg="+msg)

    
    return render(request,"user/compare.html", {"msg": msg})

def questionnaire(request):
    msg = request.GET.get("msg")
    msg=""
    uid=request.session['uid'] 
    if request.POST:
            q1 = request.POST.get("q1")
            q2 = request.POST.get("q2")
            q3 = request.POST.get("q3")
            q4 = request.POST.get("q4")
            m1 = request.POST.get("m1")
            m2 = request.POST.get("m2")
            m3 = request.POST.get("m3")
            m4 = request.POST.get("m4")
            if(q1 != None and q2 != None and q3 != None and q4 != None and m1 != None and m2 != None and m3 != None and m4 != None):
                q1= int(q1)
                q2= int(q2)
                q3= int(q3)
                q4= int(q4) 
                m1= int(m1)
                m2= int(m2)
                m3= int(m3)
                m4= int(m4)
      
                sum = q1 + q2 + q3+ q4+ m1 + m2+m3 +m4
                print(sum) 
                query=Mark.objects.update(questionnaire=sum)
                query=Mark.objects.filter(emailid=uid).update(questionnaire=sum)
                msg = "Submitted Successfully"
                return HttpResponseRedirect("/user?msg="+msg)
            else:
                msg = "Answer every Question"
                return HttpResponseRedirect("/compare?msg="+msg)

    return render(request,"user/questionnaire.html", {"msg": msg})

def result(request):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, accuracy_score
    from sklearn.naive_bayes import GaussianNB
    from sklearn import metrics
    import seaborn

    data=pd.read_csv("app1/static/assets/survey.csv")
    getfile()
    data1=pd.read_csv("app1/static/assets/csv_file.csv")
    # data = data.drop("Age",axis=1)
    data = data.drop("emailid",axis=1)
    data1=data1.drop("emailid",axis=1)
    # data1=data1.drop("Age",axis=1)
    x1=data1.drop("result",axis=1)
    x = data.drop('result', axis=1)
    y=data['result']

    # print(x)
    # print(y)
    x_train , x_test ,y_train , y_test = train_test_split(x,y,test_size=0.25,random_state=42)
    print(data1)
    # print(x_train,y_train)
    model = GaussianNB()
    model.fit(x_train,y_train)
    y_pred=model.predict(x1)
    print(y_pred)
    return render(request,"user/result.html",{"result":y_pred})

  
def getfile():  
    from app1.models import Mark
    import csv
    response = HttpResponse(content_type='text/csv')  
    f = open('app1/static/assets/csv_file.csv','w', encoding='UTF8', newline='')
    Marks = Mark.objects.all()  
    writer = csv.writer(f)  
    writer.writerow(["emailid","reading","dictation","match","comprehension","fill","count","currency","order","arithmetic","compare","questionnaire","result"])
    for mark in Marks:   
        writer.writerow([mark.emailid,mark.reading,mark.dictation,mark.match,mark.comprehension,mark.fill,mark.count,mark.currency,mark.order,mark.arithmetic,mark.compare,mark.questionnaire]) 
        # print(response) 
    
    f.close()

    


    

     





