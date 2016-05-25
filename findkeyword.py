if (messageIsRequest==0):
	keyword=['1572608274','testkeyword']
	a=messageInfo.getResponse()
	newres=helpers.analyzeResponse(a)
	offset=newres.getBodyOffset()
	body=a[offset:]
	body_string=body.tostring()
	for onekey in keyword:
		if (body_string.find(onekey)!=-1):
			print "find keyword!!!!"+onekey
			b=messageInfo.getRequest()
			print b.tostring()
			print "----------------------------------"*3
