# Pickling iris

# pickle
# requests module to download the iris datatset
# C:\Users\hp\Downloads\iris (1).data

import pickle
import requests
# url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# iris = requests.get(url).text
# print(iris)



# file_34 = "iris"
# file__obj = open(file_34, "r")
# data = file__obj.read()
# data_into_list = data.split("\n")
# print(data_into_list)
# file__obj.close()
#
# f = "iris"
# f1 = open(f, "wb")
# pickle.dump(data_into_list, f1)
# f1.close()
#
# f2 = open(f, "rb")
# a = pickle.load(f2)
# print(a)
# f2.close()


# cars = ["Mercedes", "Jaguar", "wolks wagon", "ferrari", "lamborgini", "Mclarne"]
# files = "MyCars.pkl"
# files_obj = open(files, "wb")
# pickle.dump(cars, files_obj)
# files_obj.close()




iris_l = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(iris_l)
l1 = iris_l.split("\n")
# print(l1)
l2 = [item.split(",") for item in l1 if len(item)!=0]
# print(l2)
with open("Myiris.pkl", "wb") as f:
    pickle.dump(l2, f)

# with open("Myiris.pkl", "rb") as f:
#     print(pickle.load(f))
