class letter:
	count_of_following_letter=[0]*27
	probs_of_following_letter=[0]*27
	sum=0
	letter=''
	children=[0]*27

	fill(self,l):
		print self.letter
		x=open('txt').read()
		for i,j,k in zip(x,x[1:],x[2:]):
			if i==l and j==self.letter:
				if k==' ':
					count_of_following_letter[-1]+=1
				else:
					self.count_of_following_letter[ord(k)-97]+=1
		self.sum=reduce(lambda x,y:x+y, self.count_of_following_letter)
		self.probs_of_following_letter=map(lambda x:x/self.sum,self.count_of_following_letter)

def char_range(c1, c2):
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)


tape=[]
for char in char_range('a','z'):
	tape.append(letter())
	tape[-1].letter=char
tape.append(letter())
tape[-1].letter=' '

for i in tape:
	for char in char_range('a','z'):
		i.children.append(letter())
		i.children[-1].letter=char

for i in tape:
	i.children.append(letter())
	i.children[-1].letter=' '

for i in letters:
	for child in i.children:
		child.fill(i.letter)
print hi
