from flask import Flask, render_template, request
import pickle
import seaborn as sns
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
import sklearn
sns.set_style('whitegrid')

app = Flask(__name__)

# rm = pickle.load(open('RandomForest.pkl', 'rb'))
dt = pickle.load(open("DecisionTree.pkl", "rb"))
lr = pickle.load(open("logistic.pkl", "rb"))
mnb = pickle.load(open("MultinomialNB.pkl", "rb"))
scv = pickle.load(open("LinearSVC.pkl", "rb"))
knn = pickle.load(open("KNeighbors.pkl", "rb"))
cv = pickle.load(open("Vector.pkl", "rb"))




def clean_str(string, reg=RegexpTokenizer(r'[a-zA-Z0-9]+')):
    string = string.lower()
    tokens = reg.tokenize(string)
    return " ".join(tokens)


stemmer = PorterStemmer()


def stemming(txt):
    return ''.join([stemmer.stem(word) for word in txt])

#
#
#
#

ff="fdfdfsđs"
f = [ff]
vect_1 = cv.transform(f).toarray()
print(dt.predict(vect_1))
#
# result = prediction_1[0]
#
# print(result)
def score(score):
 if(score==1):
     return "Mail rac"
 elif(score==0):
     return "Mail thuong"

@app.route('/')
def home():
    # msg = request.form['email_txt']
    # txt1 = clean_str(msg)
    # txt2 = stemming(txt1)
    # data = [txt2]
    # vect_1 = cv.transform(data).toarray()
    # if request.form["predict"]:
    #     prediction_1 = dt.predict(vect_1)
    # result = prediction_1[0]
    return render_template('home.html')
@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        msg = request.form['email_txt']
        txt1 = clean_str(msg)
        txt2 = stemming(txt1)
        data = [txt2]
        vect_1 = cv.transform(data).toarray()
        msgs = request.form['classifier']
        if(msgs=="dt"):
            prediction_1 = dt.predict(vect_1)
        elif (msgs=="lr"):
            prediction_1 = lr.predict(vect_1)
        elif (msgs=="mnb"):
            prediction_1 = mnb.predict(vect_1)
        out = score(prediction_1[0])

        return render_template('result.html',out=out)

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
