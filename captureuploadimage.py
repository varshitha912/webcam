from numbers import Number
from tracemalloc import Snapshot
from unittest import result
import cv2
import dropbox
import time
import random
start_time=time.time()

def takesnapshot():
    number=random.randint(0,100)
    videoCapobj=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCapobj.read()
        imgname="img"+str(number)+".jpg"
        cv2.imwrite(imgname,frame)
        start_time=time.time
        result=False
    return imgname
    print ("snapshot taken")
def upload_file(img) :
    access_token='sl.BH5YK5HwcY0k4NLPtASwTS5IchoUhb23nMANn1Gx3PnDw-r16pP7Wj7UVmZ-yorzPVW6sPkbFSQsQzx-3owzXCDH2iKhE8xXoqIF-FYuTWq07pfVkxJU8pUnat36nSezynyjnYr_3mHe'
    file=img
    file_from=file
    file_to="/myImages/"+(img)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("fileupload")
def main():
    while(True):
        if((time.time()-start_time)>=300):
            name=takesnapshot()
            upload_file(name)
main()
    
