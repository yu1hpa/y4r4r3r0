from database import Session
from models import Book, User

db = Session()

def seed():
    book_titles = [
        'プログラミングコンテスト攻略のためのアルゴリズムとデータ構造',
        'Pythonで学ぶ音声認識'
    ]
    books = [Book(title=title) for title in book_titles]

    user = User(username='yu1hpa')
    user.books = books
    
    db.add(user)
    db.commit()

if __name__ == '__main__':
    print('Seeding data...')
    seed()