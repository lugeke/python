



import xlrd
import re


rcText = '''
((TBNBJ('A107040',R4C4)<>0) or 
	(TBNBJ('A107040',R5C4)<>0) or
	 (TBNBJ('A107040',R6C4)<>0) or
   (TBNBJ('A107040',R7C4)<>0) or 
   (TBNBJ('A107040',R8C4)<>0) or 
   (TBNBJ('A107040',R9C4)<>0) or 
   (TBNBJ('A107040',R10C4)<>0) or
    (TBNBJ('A107040',R11C4)<>0) or 

'''

rcPattern = re.compile(r'[r|R](\d+)[c|C](\d+)')
print(re.findall(rcPattern, rcText))
#R26C4 --> D26
def ToXlsFormat(rc):
	pass


