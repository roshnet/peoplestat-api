# from sklearn.tree import DecisionTreeClassifier
# import pickle
# import numpy as np


# def resume_clf(train_object):
#     """
#     :param train_object:    List-like object with training data as values
#     :return:                1 in case of any error, 0 otherwise.
#     """
#     try:
#         X_train = np.array(train_object.keys())
#         y_train = np.array([train_object[key] for key in train_object.keys()])
#         clf = pickle.load('classifier.dat')
#         clf.fit(X_train, y_train)
#         pickle.dump(clf, 'classifier.dat')
#         return 0
#     except Exception as err:
#         return 1

# Code to sync commits with deployment. Doing the needful.
