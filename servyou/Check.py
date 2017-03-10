



#判断表达式括号配对
def checkParenthesis(s):
	n = 0
	for x in s:
		if x == "(": n += 1
		if x == ")": n -= 1
	return n == 0


s= '''

((LS(ST(A000000,C7),2)&lt;'01')or(LS(ST(A000000,C7),2)&gt;'05')) and ((T(A107020,C7)&lt;&gt;0)or(T(A107020,D7)&lt;&gt;0)or(T(A107020,E7)&lt;&gt;0)or(T(A107020,F7)&lt;&gt;0)or(T(A107020,G7)&lt;&gt;0)or(T(A107020,H7)&lt;&gt;0)or(T(A107020,I7)&lt;&gt;0)or(T(A107020,C8)&lt;&gt;0)or(T(A107020,D8)&lt;&gt;0)or(T(A107020,E8)&lt;&gt;0)or(T(A107020,F8)&lt;&gt;0)or(T(A107020,G8)&lt;&gt;0)or(T(A107020,H8)&lt;&gt;0)or(T(A107020,I8)&lt;&gt;0)or(T(A107020,C9)&lt;&gt;0)or(T(A107020,D9)&lt;&gt;0)or(T(A107020,E9)&lt;&gt;0)or(T(A107020,F9)&lt;&gt;0)or(T(A107020,G9)&lt;&gt;0)or(T(A107020,H9)&lt;&gt;0)or(T(A107020,I9)&lt;&gt;0)or(T(A107020,C10)&lt;&gt;0)or(T(A107020,D10)&lt;&gt;0)or(T(A107020,E10)&lt;&gt;0)or(T(A107020,F10)&lt;&gt;0)or(T(A107020,G10)&lt;&gt;0)or(T(A107020,H10)&lt;&gt;0)or(T(A107020,I10)&lt;&gt;0)or(T(A107020,C11)&lt;&gt;0)or(T(A107020,D11)&lt;&gt;0)or(T(A107020,E11)&lt;&gt;0)or(T(A107020,F11)&lt;&gt;0)or(T(A107020,G11)&lt;&gt;0)or(T(A107020,H11)&lt;&gt;0)or(T(A107020,I11)&lt;&gt;0)or(T(A107020,C12)&lt;&gt;0)or(T(A107020,D12)&lt;&gt;0)or(T(A107020,E12)&lt;&gt;0)or(T(A107020,F12)&lt;&gt;0)or(T(A107020,G12)&lt;&gt;0)or(T(A107020,H12)&lt;&gt;0)or(T(A107020,I12)&lt;&gt;0)or(T(A107020,C13)&lt;&gt;0)or(T(A107020,D13)&lt;&gt;0)or(T(A107020,E13)&lt;&gt;0)or(T(A107020,F13)&lt;&gt;0)or(T(A107020,G13)&lt;&gt;0)or(T(A107020,H13)&lt;&gt;0)or(T(A107020,I13)&lt;&gt;0)or(T(A107020,C14)&lt;&gt;0)or(T(A107020,D14)&lt;&gt;0)or(T(A107020,E14)&lt;&gt;0)or(T(A107020,F14)&lt;&gt;0)or(T(A107020,G14)&lt;&gt;0)or(T(A107020,H14)&lt;&gt;0)or(T(A107020,I14)&lt;&gt;0)or(T(A107020,C15)&lt;&gt;0)or(T(A107020,D15)&lt;&gt;0)or(T(A107020,E15)&lt;&gt;0)or(T(A107020,F15)&lt;&gt;0)or(T(A107020,G15)&lt;&gt;0)or(T(A107020,H15)&lt;&gt;0)or(T(A107020,I15)&lt;&gt;0)or(T(A107020,C16)&lt;&gt;0)or(T(A107020,D16)&lt;&gt;0)or(T(A107020,E16)&lt;&gt;0)or(T(A107020,F16)&lt;&gt;0)or(T(A107020,G16)&lt;&gt;0)or(T(A107020,H16)&lt;&gt;0)or(T(A107020,I16)&lt;&gt;0)or(T(A107020,C17)&lt;&gt;0)or(T(A107020,D17)&lt;&gt;0)or(T(A107020,E17)&lt;&gt;0)or(T(A107020,F17)&lt;&gt;0)or(T(A107020,G17)&lt;&gt;0)or(T(A107020,H17)&lt;&gt;0)or(T(A107020,I17)&lt;&gt;0)or(T(A107020,C18)&lt;&gt;0)or(T(A107020,D18)&lt;&gt;0)or(T(A107020,E18)&lt;&gt;0)or(T(A107020,F18)&lt;&gt;0)or(T(A107020,G18)&lt;&gt;0)or(T(A107020,H18)&lt;&gt;0)or(T(A107020,I18)&lt;&gt;0)or(T(A107020,C19)&lt;&gt;0)or(T(A107020,D19)&lt;&gt;0)or(T(A107020,E19)&lt;&gt;0)or(T(A107020,F19)&lt;&gt;0)or(T(A107020,G19)&lt;&gt;0)or(T(A107020,H19)&lt;&gt;0)or(T(A107020,I19)&lt;&gt;0)or(T(A107020,C20)&lt;&gt;0)or(T(A107020,D20)&lt;&gt;0)or(T(A107020,E20)&lt;&gt;0)or(T(A107020,F20)&lt;&gt;0)or(T(A107020,G20)&lt;&gt;0)or(T(A107020,H20)&lt;&gt;0)or(T(A107020,I20)&lt;&gt;0)or(T(A107020,C21)&lt;&gt;0)or(T(A107020,D21)&lt;&gt;0)or(T(A107020,E21)&lt;&gt;0)or(T(A107020,F21)&lt;&gt;0)or(T(A107020,G21)&lt;&gt;0)or(T(A107020,H21)&lt;&gt;0)or(T(A107020,I21)&lt;&gt;0))

'''
print(checkParenthesis(s))