import requests
from bs4 import BeautifulSoup as bs
import info

url = info.url2
headers = {
	'origin': info.url2,
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}


def getLink(vid):
	print(vid)
	links = {}
	title = _getTitle(vid)
	if title:
		print(title)
		for vtype in ['MP3', 'MP4']:
			print(f'Generating {vtype} link...')
			data={
				'title': title,
				'is_playlist':'False',
				'video_id': vid,
				'type': vtype,
			}
			req = requests.post(url+'/start-download', headers=headers, data=data)
			html = bs(req.text, 'html.parser')
			link = html.findAll(attrs={'class':'dl-boxes'})[0].contents[1]['href']
			links[vtype] = url+link
		print('Done')
		links['success'] = True
		return links
	return {'success': False}


def _getTitle(vid):
	print('Getting title...')
	yt_url = "https://www.youtube.com/results?search_query=" + vid
	try:
		response = requests.get(yt_url)
		soup = bs(response.text, 'html.parser')
		firstVideo = soup.findAll(attrs={'class':'yt-uix-tile-link'})[0]
		return firstVideo['title']
	except Exception as e:
		raise Exception('Error occured while searching on youtube:\n'+str(e))
		return None
