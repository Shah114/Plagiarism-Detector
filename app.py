from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="PlagiarismDetection") # add folder path

model = pickle.load(open('model.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html') # exact file name, not with folder path
@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form['text']

    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)
    result = "Plagiarism Detected!" if result[0] == 1 else "No Plagiarism!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)