#디비 처리, 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql as my

class DBHelper:
    '''
    멤버변수 : 커넥션
    '''
    conn = None
    '''
    생성자
    '''
    def __init__(self):
        self.db_init()
    '''
    멤버 함수
    '''

    def db_init(self):
        self.conn = my.connect(
                            host='localhost',
                            user='root',
                            password='1234',
                            db='pythonDB',
                            charset='utf8',
                            cursorclass=my.cursors.DictCursor)

    def db_free(self):
        self.conn.close()
        
    #검색 키워드 가져오기 => 웹에서 검색    
    def db_selectKeyword(self):
        #커서 오픈
        #with => 닫기 처리를 자동으로 처리해준다 => I/O 계열에 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            #print(rows)
        return rows
        

    def db_insertCrawlingData(self, title, price, period, contents, keyword):
        with self.conn.cursor() as cursor:
            sql = '''
            insert into `tbl_crawlingdata`
            (title, price, period, contents, keyword)
            values(%s,%s,%s,%s,%s)
            '''
            cursor.execute(sql,(title, price, period, contents, keyword))
        self.conn.commit()    

#단독으로 수행됐을때만 수행
if __name__=='__main__':
    db = DBHelper()
    print(db.db_selectKeyword())
    db.db_free()