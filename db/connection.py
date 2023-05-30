# 데이터베이스 사용 방법

# 1.Connection 맺기 (Python --- DB)
# - IP      : 컴퓨터 주소
# - Port    : 27017
# - ID & PW : 계정정보
# 2.명령 보내기 (Python ---→ DB)
# 3.결과 받기   (Python ←--- DB)
# 4.Connection 끊기 (Python XXXXX DB)

from pymongo import MongoClient


# MongoDB Connection
def conn():  #함수는 두 줄 띄기
    client = MongoClient("mongodb+srv://cnu:cnu1234@sunwoo.ktxyipj.mongodb.net/") # IP, Port, ID&PW
    db = client["moive"]

    collection = db.get_collection("moive")
    return collection
