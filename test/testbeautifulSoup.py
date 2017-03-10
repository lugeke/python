html = '''<a href="http://www.btava.com/magnet/detail/hash/9EA510B7D803B66B4D8B3ACBDA2EA1068B0576D8" title="ABP-339.avi">
<div class="col-xs-12 col-sm-8 col-lg-9 file"><em>ABP</em>-<em>339</em>.avi</div>
<div class="col-xs-12 size-date visible-xs-block">Size:2.2GB / Convert Date:2015-08-14</div></a>'''
import types
from  bs4 import BeautifulSoup
import urllib.request
import bs4
import re
soup = BeautifulSoup(html,'html.parser')
tag=soup.a

