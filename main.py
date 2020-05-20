from flask import Flask, request, jsonify
from handler import getLink
from phone import Youtube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def ytDownload():
	if request.method=='POST':
		vid = str(request.form['video_id'])
		vid = vid.split('&')[0] if '&' in vid else vid
		return jsonify(getLink(vid))
	return '<h1>Hello how do you feel today?</h1>'


@app.route('/phone', methods=['GET', 'POST'])
def phoneDownload():
	if request.method == 'POST':
		if Youtube.KEY == request.form['key']:
			query = request.form['query']
			yt = Youtube(query)
			return jsonify(yt.getLink())
		return jsonify({'success': False, 'message': 'Invalid request'})
	return '<h1>Hello how do you feel today?</h1>'



if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True, port=3000)
