from channels.generic.websocket import WebsocketConsumer

class NotificationConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

	def receive(self,text_data):
		self.send(text_data="This is from server")

	def disconnect(self,close_code):
		self.close(close_code)