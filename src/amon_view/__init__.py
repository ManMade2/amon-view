from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app


'''
from flask import Flask, render_template
import threading
import webview

app = Flask(__name__)

# Flask route to serve your HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Function to run Flask in a separate thread
def start_flask():
    app.run(host="127.0.0.1", port=5000)

if __name__ == '__main__':
    app.run(debug=True, port=5001)


    
    # # Start Flask in a new thread
    # threading.Thread(target=start_flask).start()

    # # Create a PyWebView window to view the Flask web app
    # webview.create_window('My Flask App', 'http://127.0.0.1:5000', width=800, height=600)
    # webview.start()


'''