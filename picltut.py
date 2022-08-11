import pickle

# pickling a python file
cars = ["Mercedes", "Jaguar", "wolks wagon", "ferrari", "lamborgini", "Mclarne"]
files = "MyCars.pkl"
files_obj = open(files, "wb")
n = pickle.dump(cars, files_obj)
print(n)
files_obj.close()

files = "MyCars.pkl"
files_obj = open(files, "rb")
MyCars = pickle.load(files_obj)
print(MyCars)
# print(type(MyCars))

