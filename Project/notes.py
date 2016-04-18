import requests
import os
import time

def uploadFile(file, roll, course):
	url = 'http://10.0.2.22/upload.php'
	files = {'fileToUpload': open(file, 'rb')}
	data = {'roll':roll, 'course':course}
	r = requests.post(url, files=files, data=data)
	if r.text == "Ok":
		print "Your file has been uploaded successfully!"
	else:
		print "error while uploading"

def listUploads(course):
	url = 'http://10.0.2.22/listfiles.php'
	data = {'course':course}
	r = requests.post(url, data=data)
	# print r.text
	files = r.text.split("\n")[:-1]
	icondir = 'icons/'
	fileicons = os.listdir(icondir)
	uploadedby = []
	filename = []
	icons = []
	uploadTime = []
	for i in range(0,len(files),2):
		uploadedby.append(files[i][:9])
		filename.append(files[i][9:])
		realTime = time.asctime(time.localtime(int(files[i+1])))
		uploadTime.append(str(realTime))
		# print time.asctime(time.localtime(int(files[i+1])))
		flag = 0
		for icon in fileicons:
			if files[i].split('.')[-1] in icon.split('.')[0]:
				flag = 1
				icons.append(icondir+icon)
				break
		if flag is 0:
			icons.append(icondir+'default.png')
	return icons, filename, uploadedby, uploadTime


# listUploads("CS203")
# uploadFile('exam.py')