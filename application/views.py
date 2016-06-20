__author__ = 'chris'
from application import app
from flask import request, render_template

#Setup the cache that we'll use to hold the values open.
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

@app.route('/')
def front_page():
    from models import Sentence
    sentences = cache.get("sentence_list")
    #on the front page, we assume that if the sentences cache exists, then the default sentence is at root.
    #if not, we should create it and store it in the cache.
    if sentences:
        return render_template('index.html', sentence=sentences[0])
    else:
        current_sentence = Sentence("Once upon a time, there was a big bad wolf.")
        cache.set("sentence_list", [current_sentence], timeout=None)
        return render_template('index.html', sentence=current_sentence)


def get_sentence_object(sentence, sentences_from_cache):
    for idx, current_sentence in enumerate(sentences_from_cache):
        if sentence in current_sentence.centre:
            return current_sentence


@app.route('/sentence/<sentence_text>')
def sentence_display(sentence_text):
    """Finds the sentence object for the given text and displays it in the centre, with any child URLs
    as clickable links"""

    sentences = cache.get("sentence_list")
    current_sentence = get_sentence_object(sentence_text, sentences)

    return render_template('index.html', sentence=current_sentence)


@app.route('/add_sentence', methods=['POST'])
def add_sentence():
    """Internal functionality to add sentences to the current session cache.
    Gets the text of the new sentence and position from the submitted form,
    adds it to the current sentence using setattr and creates a new object that we can navigate
    to later."""
    from application.models import Sentence
    if request.method == 'POST':
        sentences = cache.get("sentence_list")
        current_sentence = get_sentence_object(request.form["current-sentence"], sentences)
        added_sentence = request.form['sentence']
        position = request.form['position']
        setattr(current_sentence, position, request.form['sentence'])
        sentences.append(Sentence(added_sentence))
        cache.set("sentence_list", sentences, timeout=None)
    else:
        current_sentence = cache.get("sentence_list")[0]
    return render_template('index.html', sentence=current_sentence)


"""Standard error handlers for 404/500 responses."""


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    #self.__init__()

    app.debug=True
    app.run(host='0.0.0.0')

