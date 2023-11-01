from flask import Flask, render_template, request
from textblob import TextBlob
import os

# Set the absolute path to the templates directory
template_dir = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ""
    polarity = None
    if request.method == 'POST':
        text = request.form['text']
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            sentiment = "Pos"
        elif polarity < 0:
            sentiment = "Neg"
        else:
            sentiment = "Neutral"
    return render_template('index.html', sentiment=sentiment, score=polarity)

if __name__ == '__main__':
    app.run(debug=True)
