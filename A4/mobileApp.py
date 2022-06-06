import requests

passengerId=int(input("Enter passenger ID:"))
Pclass=int(input("Enter passenger class:"))
gender=int(input("Enter Gender(1 for male 0 for female):"))
age=int(input("Enter passenger age:"))
sibSp=int(input("Enter Sibling/Spouse status(0 or 1):"))
parch=int(input("Enter parent/child status(0 or 1):"))
fare=int(input("Enter Fare:"))
embarked=int(input("Enter Port of Embarkation(1 for Q,2 for S,3 for C):"))

# passengerId=123
# Pclass=2
# gender=0
# age=12
# sibSp=1
# parch=0
# fare=25
# embarked=2

data={
    'passengerId':passengerId,
    'Pclass':Pclass,
    'gender':gender,
    'age':age,
    'sibSp':sibSp,
    'parch':parch,
    'fare':fare,
    'embarked':embarked
}

url='http://localhost:5000/checkPassenger'
resp=requests.post(url,json=data)
survive=int(resp.content.decode("utf-8"))

# print(survive)

if survive:
    print("Survived")
else:
    print("Not Survived")