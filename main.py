from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir=os.path.join(os.path.dirname(__file__),'templates')
jinja_env=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),  autoescape=True)
app=Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def display_signup():
    #template=jinja_env.get_template('index.html')
    #return template.render()
    return render_template('index.html')

@app.route("/", methods=["POST"])

def validate_user():
    user=request.form["user"]
    erruser=""
    pass1=request.form["pass"]
    errpass1=""
    pass2=request.form["vpass"]
    errpass2=""
    email=request.form["email"]
    errmail=""

    if user=="":
        erruser="Username is required"
    elif 3>len(user):
        erruser="Username lenght min 3 characteres"
    elif 20<len(user):
        erruser="Username lenght max 20 characteres"
    elif " " in user:
        erruser="User not valid (spaces nor permit)"


    if pass1=="":
        errpass1="Password is required"
    elif 3>len(pass1):
        errpass1="Password lenght min 3 characteres"
    elif 20<len(pass1):
        errpass1="Password lenght max 20 characteres"
    elif " " in pass1:
        errpass1="Password not valid (spaces nor permit)"
    
    if pass2=="":
        errpass2="Password Validation is required"
    elif not pass1==pass2:
        errpass2="Password validation need to match"

    if email:
        check1 = "@" 
        check2="."
        check=" "
        if email.count(check1)>1:
            errmail="Email not valid"
        if not check1 in email or not check2 in email or check in email:
            errmail="Email not valid"



    if not erruser and not errpass1 and not errpass2 and not errmail:
        #template=jinja_env.get_template('welcome.html')
        #return template.render(username=user)
        return render_template('welcome.html',username=user)

    else:
        #template=jinja_env.get_template('index.html')
        #return template.render(username=user, erruser=erruser, pass1='', errpass1=errpass1, pass2='', errpass2=errpass2, mail=email, errmail=errmail )
        #return render_template('index.html',username=user, erruser=erruser, pass1='', errpass1=errpass1, pass2='', errpass2=errpass2, mail=email, errmail=errmail )
        return render_template('index.html',username=user, erruser=erruser, errpass1=errpass1, errpass2=errpass2, mail=email, errmail=errmail )




app.run()
