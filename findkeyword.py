keyword='1572608274'
a=messageInfo.getResponse()
newres=helpers.analyzeResponse(a)
offset=newres.getBodyOffset()
body=a[offset:]
body_string=body.tostring()
if (body_string.find(keyword)!=-1):
	print "find keyword!!!!"
	b=messageInfo.getRequest()
	newreq=helpers.analyzeRequest(b)
	requrl=newreq.getUrl()
	print requrl