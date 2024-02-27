from flask import Flask, render_template
#import os

app = Flask(__name__)

#picFolder1 = os.path.join('static', 'pics')
#app.config['UPLOAD_FOLDER'] = picFolder1

@app.route("/")
def labtsk():
    # Here you can perform any task you want to do for the root route
    # For example, render a template:
    #pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'COMSATS_new_logo.jpg')
    
   ## imageList = os.listdir('static/pics')
    #imageList = ['pics/' + img for img in imageList]
    return render_template('labtask.html')
  

 
if __name__ == "__main__":
    app.run(debug=True)