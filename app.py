import re
from stories import story as my_story

from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', story=my_story)
    return redirect(url_for('story'))


@app.route('/story', methods=['GET', 'POST'])
def story():
    if request.method == 'GET':
        return render_template('story.html')
    story_=my_story
    data=request.form
    return render_template('story.html', story_=story_, answers=data)
