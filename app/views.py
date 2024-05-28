# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *





# defining function 
def home(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# getting link from frontend 
		link = request.POST['url'] 
		video = YouTube(link) 

		title= video.title
		caption = video.captions
		thumb = video.thumbnail_url
		#stream = video.streams.all()
		#filtrer = video.streams.filter(mime_type="video/mp4")
		
		# setting video resolution 
		stream = video.streams.getlowest_resolution() 
		
		# downloads video 
		stream.download() 

		# returning HTML page 
		return render(request, 'app/form.html') 
	return render(request, 'app/form.html')
