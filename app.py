from flask import Flask, render_template, request, abort, redirect
import magic, os
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
		imgPath = os.path.abspath(request.form['personalImgPath'])
		magic.upload(imgPath, imgURL, name)
		return redirect('/thankyou')
	else:
		return abort(405) #method not allowed
	# TODO: add more refinement to the type of URL being entered

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

if __name__ == '__main__':
    app.debug = True
    app.run()