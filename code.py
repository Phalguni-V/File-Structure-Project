import time
import matplotlib.pyplot as plt 

def insert_func(place,pin):
	global d
	if place not in d:
		d[place]=[]
		d[place].append(pin)
	else:
		if pin in d[place]:
			print("This place and pin already exists")
		else:
			d[place].append(pin)

def remove_func(place):
	global d
	if place not in d:	
		print("This place does not exist")
	else:
		l=d.pop(place)
		print("Deleted %s successfully"%(place))
		print("The pins deleted are as follows:")
		for i in l:
			print(i)

def search_func(place):
	global d
	if place not in d:
		print("This place does not exist")
	else:
		l=d[place]
		print("The pin numbers of %s are as follows"%(place))
		for i in l:
			print(i)

def search_func2(pin):
	global d
	c=0
	for i in d:
		for q in d[i]:
			if(q==pin):
				c=1	
				print("The place is %s"%(i)) 
	if(c==0):
		print("The pin does not exist")		
			

def display_func():
	print("PIN NUMBER \t PLACE \t INDEX")
	global d
	c=0	
	p=sorted(d)
	for i in p:
		for x in d[i]:
			print("%s \t %s \t %d"%(x,i,c))		
			c=c+1




d={}
start = time.time()
print("Dict is being constructed")
#print(datetime.datetime.time(datetime.datetime.now()))
c=0
x=[10000,20000,40000,80000,150000]
y=[]
with open('IN.txt', 'r') as f:
	
	for line in f:
		c=c+1
		word = line.split("\t")
		place=word[2]
		pin=word[1]
		if place not in d:
			d[place]=[]
		d[place].append(pin)	
		if(c==10000):
			tm=(time.time() - start)*1000
			print("Time for 10000 records : %s ms" %(tm) )
			y.append(tm)
		if(c==20000):
			tm=(time.time() - start)*1000
			print("Time for 20000 records :%s ms " %(tm) )
			y.append(tm)
		if(c==40000):
			tm=(time.time() - start)*1000
			print("Time for 40000 records :%s ms " %(tm) )
			y.append(tm)
		if(c==80000):
			tm=(time.time() - start)*1000
			print("Time for 80000 records :%s ms " %(tm) )
			y.append(tm)
		if(c==150000):
			tm=(time.time() - start)*1000
			print("Time for 150000 records :%s ms " %(tm) )	
			y.append(tm)

						

print("Time for Data Structure to be built")
print("Total time for all records: %s ms" % ((time.time() - start)*1000))

plt.plot(y, x, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12) 
plt.xlabel('Time to store in Data structure (ms) ') 
plt.ylabel('No of records') 
plt.title('Storing Data') 
plt.show()


c = 5
while c > 0 :
	print("Enter your choice")
	print("1) Insert new place and pin")
	print("2) Delete")
	print("3) Search by place")
	print("4) Search by pin")
	print("5) Print the Indexes")
	print("0) Exit")
	c = int(input())
	if c == 1:
		pin = input("Enter the pin: ")
		place = input("Enter the place name : ")
		startI = time.time()
		insert_func(place,pin)
		print("Time for the place to be inserted :   %s ms " % ((time.time() - startI)*1000))
		print("Your data has been entered")
	elif c == 2:
		place = input("Enter the place name: ")
		startD = time.time()
		remove_func(place)
		print("Time for the place to be deleted :   %s ms " % ((time.time() - startD)*1000))

		
	elif c == 3:
		place = input("Enter the place name to be searched: ")
		startS = time.time()
		search_func(place)
		print("Time taken for the place to be searched :   %s ms " % ((time.time() - startS)*1000))

	elif c == 4:
		pin = input("Enter the pin: ")
		startS = time.time()
		search_func2(pin)
		print("Time taken for the place to be searched :   %s ms " % ((time.time() - startS)*1000))	

	elif c == 5:
		display_func()
	else :
		break