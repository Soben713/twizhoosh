from ..base import base_handler
import random

class NobodyCares(base_handler.BaseHandler):
	
	def timeline_update(self, data):
		do_reply = (random.randint(0, 20) < 19)
		if not do_reply or not 'text' in data:
			return
		
		photo = open ('assets/nobody_cares.jpg', 'rb')
		
		try:
			photo = self.twitter.upload_media(photo)
			self.reply_to(data, status='...', media_ids=[photo['media_id']])
		except TwythonError as e:
			print e