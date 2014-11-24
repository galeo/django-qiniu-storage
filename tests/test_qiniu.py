import httplib
import os
from os.path import dirname, join
import uuid

import qiniu.conf
import qiniu.io
import qiniu.rs
import qiniu.rsf


QINIU_ACCESS_KEY = os.environ.get('QINIU_ACCESS_KEY')
QINIU_SECRET_KEY = os.environ.get('QINIU_SECRET_KEY')
QINIU_BUCKET_NAME = os.environ.get('QINIU_BUCKET_NAME')
QINIU_BUCKET_DOMAIN = os.environ.get('QINIU_BUCKET_DOMAIN')

qiniu.conf.ACCESS_KEY = QINIU_ACCESS_KEY
qiniu.conf.SECRET_KEY = QINIU_SECRET_KEY

QINIU_PUT_POLICY= qiniu.rs.PutPolicy(QINIU_BUCKET_NAME)

def test_put_file():
    conn = httplib.HTTPConnection('up.qiniu.com')
    ASSET_FILE_NAME = 'bootstrap.min.css'
    with open(join(dirname(__file__),'assets', ASSET_FILE_NAME), 'rb') as assset_file:
        text = assset_file.read()

    print "Test text: %s" % text
    token = QINIU_PUT_POLICY.token()
    ret, err = qiniu.io.put(token, join(str(uuid.uuid4()), ASSET_FILE_NAME), text)
    if err:
        raise IOError(
            "Error message: %s" % err)