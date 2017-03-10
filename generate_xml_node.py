node = """
<rule count="" rowStart="%d" rowEnd="%d" columnStart="C" columnEnd="V" skipNode=""
	orientation="horizontal"  child="0|%d" >
	  <skipNode>
	    <Node>ewbhxh</Node>
		<Node>ewbhmc</Node>
	  </skipNode>
	</rule>
"""


for i in range(8,21):
	print(node %(i,i,i-8))