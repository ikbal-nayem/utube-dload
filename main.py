from flask import Flask, request, jsonify
from handler import getLink

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ytDownload():
	if request.method=='POST':
		vid = str(request.form['video_id'])
		vid = vid.split('&')[0] if '&' in vid else vid
		return jsonify(getLink(vid))

	return 'yes'


if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True, port=3000)
