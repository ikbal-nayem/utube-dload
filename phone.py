import requests
from bs4 import BeautifulSoup as bs

class Youtube:
	KEY = 'a20be49340d5fb483d02be34482f6b5d'
	url = 'https://online.freemusicdownloads.world'
	headers = {
		'origin': 'https://online.freemusicdownloads.world',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
	}

	
	def __init__(self, query):
		self.query = query
		self.title = None
		self.vid = None
		self.thumb = None
		self.video_time = None
		self.published = None
		self.views = None
		self.success = False
		self.message = None
			
	
	def _getVID(self, link):
		if 'youtube.com' in link:
			sp = link.split('=')
			if len(sp)>2 and '&' in sp[1]:
				return sp[1].split('&')[0]
			return sp[-1]
		elif 'youtu.be' in link:
			return link.split('/')[-1]
		else:
			return link

	def _getVideoInfo(self, query):
		print('Getting info for {}'.format(query))
		yt_url = "https://www.youtube.com/results?search_query=" + query
		try:
			response = requests.get(yt_url)
			soup = bs(response.text, 'html.parser')
			content = soup.findAll('div', attrs={'class':'yt-lockup'})[0]
			self.thumb = content.img['src']
			self.video_time = str(content.find('span', attrs={'class': 'video-time'}).text).strip()
			self.title = content.find('a', attrs={'class': 'yt-uix-tile-link'})['title']
			self.published, self.views = (ele.text.strip() for ele in content.find('ul', attrs={'class': 'yt-lockup-meta-info'}).findAll('li'))
			href = content.find('a', attrs={'class': 'yt-uix-tile-link'})['href']
			self.vid = self._getVID('https://www.youtube.com' + href)
			self.success = True
			self.message = 'video not found'
		except Exception as e:
			self.success = False
			raise Exception('Error occured while getting info from youtube :\n'+str(e))
	

	def getLink(self):
		if 'youtube.com' in self.query or 'youtu.be' in self.query:
			self._getVideoInfo(self._getVID(self.query))
		else:
			self._getVideoInfo(self.query)
		print('Getting link...')
		links = {}
		for vType in ['MP3', 'MP4']:
			data={
				'title': self.title,
				'is_playlist':'False',
				'video_id': self.vid,
				'type': vType,
			}
			try:
				req = requests.post(Youtube.url+'/start-download', headers=Youtube.headers, data=data)
				html = bs(req.text, 'html.parser')
				link = html.findAll(attrs={'class':'dl-boxes'})[0].contents[1]['href']
				links[vType.lower()] = Youtube.url+link
				self.success = True
			except Exception as e:
				self.success = False
				self.message = 'download link not found'
				raise Exception('Error occured while getting download link:\n'+str(e))
		
		if self.success:
			return {
				"success": self.success,
				"vid": self.vid,
				"title": self.title,
				"thumb": self.thumb,
				"video_time": self.video_time,
				"published": self.published,
				"views": self.views,
				"links": links
			}
		else:
			return {
				"success": self.success,
				"message": self.message
			}
