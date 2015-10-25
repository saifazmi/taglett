from flask import Flask, render_template, request, abort, redirect
import magic
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	error = None
	if request.method == 'POST':
		name = request.form['name']
		imgURL = request.form['personalImgURL']
		imgFile = request.files['personalImgFile']
		magic.upload(imgFile, imgURL, name)
		return redirect('/thankyou')
	else:
		return abort(405) #method not allowed
	# TODO: add more refinement to the type of URL being entered

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

@app.route('/letsClarifai')
def letsClarifai():
	return render_template('letsClarifai.html')

@app.route('/startClarifaing')
def startClarifaing():
	error = None
	if request.method == 'POST':
		imgURL = request.form['personalImgURL']
		imgFile = request.files['personalImgFile']
		magic.check(imgFile, imgURL)
		return redirect('/thankyou')
	else:
		return abort(405) #method not allowed
		
if __name__ == '__main__':
    app.debug = True
    app.run()