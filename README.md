# PYROBVMailScript

## Summary

This script is to send status mail by getting required details from db and generating mail content.

## To run this script 

Create a .env file and add the required usernames and passwords in below format

```file
PYROUSERNAME = username
PYROPASSWORD = password
PYROPORT = 3300
BVUSERNAME = username
BVPASSWORD = password
BVPORT = 3301
BBUSERNAME = username
BBPASSWORD = password
BBPORT = 3302
MAILTO = johndoe@gmail.com
# if we are using BB in RDP add the path of the body.txt in you script 
FILEPATH = C:/Users/username/scriptlocation/body.txt
```
