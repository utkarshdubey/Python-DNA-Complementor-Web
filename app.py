# IMPORTS
from flask import Flask, request, url_for, render_template

# INITIALIZATION
app = Flask(__name__)

# ROUTES

# INDEX ROUTE
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hi!'



# RUN
if __name__ == '__main__':
    app.run(debug=True)
