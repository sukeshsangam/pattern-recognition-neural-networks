
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
from numpy import array
digits=[]
values=[]
i=0
digits.append([])
while 1:
	row=raw_input()
	if row=='lastparag = 0':
		break
while 1:
	row=raw_input()
	if row=="EOF":
		break
	else:	
		if i<32:
			for c in list(row):
				digits[-1].append(int(c))
			i+=1
		if i==32:
			number=raw_input()
			values.append(number.strip(' \t\n\r'))
			i=0
			digits.append([])
digits.pop()

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(10))
X_train, X_test, y_train, y_test = train_test_split(digits, values, test_size=0.2)

np.savetxt("training_x.txt",array(X_train))

np.savetxt("target_x.txt",array(X_test))

model = clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
target_names = ['0','1','2','3','4','5','6','7','8','9']
print classification_report(y_test, predictions, target_names=target_names)

