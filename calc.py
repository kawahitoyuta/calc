import ui
from decimal import Decimal

num1 = ""

def push_0(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '0'
	else:
		main.text += '0'
def push_1(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '1'
	else:
		main.text += '1'

def push_2(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '2'
	else:
		main.text += '2'
	
def push_3(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '3'
	else:
		main.text += '3'
	
def push_4(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '4'
	else:
		main.text += '4'
	
def push_5(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '5'
	else:
		main.text += '5'
	
def push_6(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '6'
	else:
		main.text += '6'
	
def push_7(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '7'
	else:
		main.text += '7'
	
def push_8(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '8'
	else:
		main.text += '8'
	
def push_9(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text = '9'
	else:
		main.text += '9'

def push_dot(sender):
	main = sender.superview['main']
	if main.text == "0":
		main.text += '.'
	else:
		main.text += '.'

def push_plus(sender):
	global num1
	main = sender.superview['main']
	if main.text != "":
		num1 = [main.text,'plus']
		main.text = ''
		
def push_minus(sender):
	global num1
	main = sender.superview['main']
	if main.text != "":
		num1 = [main.text,'minus']
		main.text = ''
		
def push_times(sender):
	global num1
	main = sender.superview['main']
	if main.text != "":
		num1 = [main.text,'times']
		main.text = ''

def push_divide(sender):
	global num1
	main = sender.superview['main']
	if main.text != "":
		num1 = [main.text,'divide']
		main.text = ''
	
def push_ac(sender):
	main = sender.superview['main']
	main.text = ''

def push_del(sender):
	main = sender.superview['main']
	if main.text != "":                   
		main.text = main.text[:-1]

def push_equal(sender):
	global num1
	main = sender.superview['main']
	if main.text != "0":
		if '.' in main.text or '.' in num1[0]:
			num_1 = Decimal(num1[0])
			cal = num1[1]
			num_2 = Decimal(main.text)
		else:
			num_1 = int(num1[0])
			cal = num1[1]
			num_2 = int(main.text)
		print(num_1)
		print(num_2)
		if cal == "plus":
			print(num_1)
			print(num_2)
			anser = num_1 + num_2
		elif cal == "minus":
			anser = num_1 - num_2
		elif cal == "times":
			anser = num_1 * num_2
		elif cal == "divide":
			anser = num_1 / num_2
	main.text = str(anser)
	anser = 0

v = ui.load_view()
v.present('sheet')



