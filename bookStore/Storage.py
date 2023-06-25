# 上传图片
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self,location=settings.MEDIA_ROOT,base_url=settings.MEDIA_URL):

        super(ImageStorage,self).__init__(location,base_url)

    def _save(self, name, content):
        import os,time,hashlib

        ext=os.path.splitext(name)[1]

        d=os.path.dirname(name)

        fn=hashlib.md5(time.strftime('%Y%m%d%H%M%S').encode('utf-s')).hexdigest()
        name=os.path.join(d,fn+ext)

        return super(ImageStorage,self)._save(name,content)