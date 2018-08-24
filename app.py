# IMPORTS
from flask import Flask, request, url_for, render_template
import re
# INITIALIZATION
app = Flask(__name__)


# FUNCTIONS



# ROUTES

# INDEX ROUTE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        result = request.form['value']
        return render_template("result.html", result=result)
    else:
        return render_template("index.html")


# RUN
if __name__ == '__main__':
    app.run(debug=True)
