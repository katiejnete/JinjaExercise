from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key93403982'

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    """Shows homepage to introduce our Madlibs app.
    Shows form and asks for all required by story."""
    return render_template("home.html", fill_ins=story.prompts)

@app.route('/story')
def show_story():
    """Shows resulting story for user's answers."""
    story_ans = {
        'place':request.args["place"],
        'noun':request.args["noun"],
        'verb':request.args["verb"],
        'adjective':request.args["adjective"],
        'plural_noun':request.args["plural_noun"],
        }
    result = story.generate(story_ans)
    return render_template("story.html",result=result)
