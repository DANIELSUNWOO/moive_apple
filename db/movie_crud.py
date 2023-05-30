# CRUD
# - CREATE : 생성
# - READ   : 조회
# - UPDATE : 수정
# - DELETE : 삭제

# 리뷰 저장(MongoDB)

from db.connection import conn
def add_review(data):
    collection = conn()
    collection.insert_one(data) # Review 저장


# 리뷰 조회(MongoDB)
def get_reviews():
    pass