"""
This module implements a Flask web application for emotion detection.
It provides an index page and an API endpoint for detecting emotions from text input.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Renders the index.html file for the home page.
    """
    return render_template('index.html')  # This serves the index.html file

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detection():
    """
    Handles emotion detection requests.

    - GET: Extracts 'textToAnalyze' from query parameters.
    - POST: Extracts 'text' from form data.

    Returns:
        JSON response containing the detected emotions or an error message if input is invalid.
    """
    if request.method == 'GET':
        # Extract the 'textToAnalyze' parameter from the query string
        user_input = request.args.get('textToAnalyze', '')

    # Handle POST request
    elif request.method == 'POST':
        # Extract the 'text' parameter from the form data
        user_input = request.form['text']

    # Get the emotions as a dictionary from the emotion detection function
    emotions = emotion_detector(user_input)


    # Return the response as JSON

    # Check if dominant_emotion is None
    if emotions["dominant_emotion"] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    # Format the output
    output = f"For the given statement, the system response is " \
             f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, " \
             f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and " \
             f"'sadness': {emotions['sadness']}. The dominant emotion " \
             f" is {emotions['dominant_emotion']}"
    return jsonify({"response": output})

if __name__ == '__main__':
    app.run(debug=True)
