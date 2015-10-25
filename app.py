from flask import Flask, render_template, request, abort, redirect
import magic
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
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

@app.route('/startClarifaing', methods=['POST'])
def startClarifaing():
	if request.method == 'POST':
		name = request.form['name']
		imgURL = request.form['personalImgURL']
		imgFile = request.files['personalImgFile']
		score = magic.check(imgFile, imgURL,name)
		return render_template('score.html',score = score)
	else:
		return abort(405) #method not allowed
		
if __name__ == '__main__':
    app.debug = True
    app.run()