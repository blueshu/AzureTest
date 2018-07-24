import time
import datetime
import json
import requests
import threading
import os
import shutil

# need to find something python3 compatible  
# import urllib2

from azure.storage.blob import ContentSettings,AppendBlobService

class Sim(object):
    '''
    INS simulation engine.
    '''
    def __init__(self, dirPath, pathName):
        self.dirPath = dirPath
        self.pathName = pathName
        self.index = 0
        self.totalFiles = 0
        self.filse = []
        self.readFils()

    def readFils(self):
        n = 0
        filse = []
        filesName = self.dirPath + self.pathName
        for root, dirs, files in os.walk(filesName):
            for name in files:
                if(name.endswith(".csv")):
                    n += 1
                    filse.append(name)
        self.totalFiles = n
        self.filse = filse

    def begin_update_files(self):
        if self.totalFiles > 0:
            self.update_files()

    def processCall(self,process,total):
        if process == total:
            if self.index < self.totalFiles-1:
                self.index += 1
                self.update_files()
            else: 
                self.clear_files()

    def update_files(self):
        try:
            fileName = self.filse[self.index]
            f = open(self.dirPath + self.pathName + '/' + fileName, "r")
            text = f.read()    
            name = 'test/' + fileName
            append_blob_service = AppendBlobService(account_name='navview', account_key='+roYuNmQbtLvq2Tn227ELmb6s1hzavh0qVQwhLORkUpM0DN7gxFc4j+DF/rEla1EsTN2goHEA1J92moOM/lfxg==', protocol='http')
            append_blob_service.create_blob(container_name='data', blob_name=name,content_settings=ContentSettings(content_type='text/plain'))
            append_blob_service.append_blob_from_bytes(container_name='data',blob_name=name,blob=text,progress_callback=self.processCall)
        except Exception as e:
            print(e)

    def clear_files(self):
        shutil.rmtree(self.dirPath + self.pathName)
        print('end')
 
if __name__ == "__main__":
    updateFil = Sim('./','2018-07-23-14-34-41')
    updateFil.begin_update_files()