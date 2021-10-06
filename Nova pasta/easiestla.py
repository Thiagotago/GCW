from sklearn import tree

X = [[140, 1], [130, 1], [150, 0], [170, 0]]

Y = [5, 5, 10, 10]

cfl = tree.DecisionTreeClassifier()

cfl = cfl.fit(X, Y)


print(cfl.predict([[145, 0]]))