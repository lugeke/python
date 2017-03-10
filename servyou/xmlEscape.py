# 将字符串中的< > & 进行转义

text = 'http://sx.4007112366.com/?m=content&c=index&a=download&cat_id=244&menu_id=242'



from xml.sax.saxutils import escape  
print(escape(text))