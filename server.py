from glob import escape
from flask import Flask, render_template, request

app = Flask(__name__) 
print(__name__) # created an instance of flask app sets name as main 

@app.route("/") # decorator to tell flask what url should call the function
def indexx(): # function to be called when the route is accessed
    return render_template("index.html")

@app.route("/index.html") # decorator to tell flask what url should call the function
def home(): # function to be called when the route is accessed
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html") # rendering a template for the contact page

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        # Here you would handle the form submission, e.g., save to a database or send an email
        data= request.form.to_dict()  # Get form data as a dictionary
        print(data)  # For debugging, you can print the data to the console
        # You can add logic to process the data, such as saving it or sending an email
        # For now, we will just render the thank you page
        return render_template("thankyou.html")
    else:
        return "something went wrong, please try again later"

@app.route("/favicon-test")
def favicon_test():
    return app.send_static_file("favicon.ico")