#----------------------------------
# Step1: Get INFO
#----------------------------------
import sys,configparser
 
try:
    configFile = open("config.ini","r")
except IOError:
    print("config.ini is not found")
    #input("")
    sys.exit()
 
config = configparser.ConfigParser()
config.read_file(configFile)
configFile.close()
 
# get baseurl
try:
    baseurl = config.get("INFO","baseurl")
    if baseurl[-1] != '/':
    	baseurl += '/'
except configparser.NoOptionError:
    print("url is not found under section INFO in config.ini.")
    #input("")
    sys.exit()
         
# get user
try:
    user = config.get("INFO","user")
except configparser.NoOptionError:  
    print("user is not found under section INFO in config.ini.")
    #input("")
    sys.exit()
 
# get passwd   
try:
    passwd = config.get("INFO","passwd")
except configparser.NoOptionError:
    print("passwd is not found under section INFO in config.ini.")
    #input("")
    sys.exit()
# get from_revision 
try:
    from_revision = config.getint("INFO","from_revision")
except configparser.NoOptionError:
    print("from_revision is not found under section INFO in config.ini.")
    #input("")
    sys.exit()

#get to_revision
try:
    to_revision = config.getint("INFO","to_revision")
except configparser.NoOptionError:
    print("to_revision is not found under section INFO in config.ini.")
    #input("")
    sys.exit()
relative_path = config.get("INFO","relative_path",fallback='')
#----------------------------------
# Step2: Auth
#----------------------------------
# import urllib2
# realm = "Subversion Repositories"
# auth = urllib2.HTTPBasicAuthHandler()
# auth.add_password(realm, baseurl, user, passwd)
# opener = urllib2.build_opener(auth, urllib2.CacheFTPHandler)
# urllib2.install_opener(opener)
import urllib.request
realm = 'Subversion Repositories'
auth = urllib.request.HTTPBasicAuthHandler()
auth.add_password(realm, baseurl, user, passwd)
opener = urllib.request.build_opener(auth, urllib.request.CacheFTPHandler )
urllib.request.install_opener(opener)
#----------------------------------
# Step3: Create Folder
#----------------------------------
import os
folderName = "svnFile"
if not os.path.exists(folderName):
    os.mkdir(folderName)

url = "(%s%s)" %(baseurl, relative_path)
print(url)
try:
	data = urllib.request.urlopen(url)
	print(data.read())
except urllib.request.HTTPError as e:
# HTTPError is a subclass of URLError
# need to catch this exception first
	mesg = str(e).split(" ")
	errCode = mesg[2].rstrip(":")
	if errCode == "401":
		# HTTP Error 401: basic auth failed
		print("Can not login in, please check the user and passwd in config.ini.")
	elif errCode == "404":
		# HTTP Error 404: Not Found
		print("Not Found: %s"%i)
	else:
		print(e)
except urllib.request.URLError:
	# 1.SVN server is down
	# 2.URL is not correct
	print("Please check SVN Server status and baseurl in config.ini.")
#----------------------------------
# Step4: Get Files
#----------------------------------
# fr = open(fileList,'r')
# for i in fr:
#     i = i.strip("\n")
#     i = i.strip(" ")
     
#     # ignore the blank line
#     if i != "":
#         url = "%s%s"%(baseurl,i)
 
#         try:
#             data = urllib2.urlopen(url)
 
#             fw = open("%s/%s"%(folderName,i),'w')
#             fw.write(data.read())
#             fw.close()
 
#             print "Download: %s."%i
 
#         except urllib2.HTTPError, e:
#             # HTTPError is a subclass of URLError
#             # need to catch this exception first
#             mesg = str(e).split(" ")
#             errCode = mesg[2].rstrip(":")
             
#             if errCode == "401":
#                 # HTTP Error 401: basic auth failed
#                 print "Can not login in, please check the user and passwd in config.ini."
#                 break
#             elif errCode == "404":
#                 # HTTP Error 404: Not Found
#                 print "Not Found: %s"%i
#             else:
#                 print e
#                 print "Failed to download %s"%i
 
#         except urllib2.URLError:
#             # 1.SVN server is down
#             # 2.URL is not correct
#             print "Please check SVN Server status and baseurl in config.ini."
#             break
 
# fr.close()
# raw_input("")