from pymongo import MongoClient 
from datetime import datetime, timedelta
client = MongoClient('localhost', 27017) 
db = client.dbflask

class MyUser:
    def login(userEmail):

        loginInfo = db.userInfo.find_one({'userEmail': userEmail})
        if loginInfo == None:
            return "Wrong Email"
        loginPassword = loginInfo['password']
        loginUserName = loginInfo['userName']
        return [loginPassword,loginUserName]



class TimeClass:
    def splitTime(userEmail , time , timeType):
        dayOfWeek,month,day,year,nowTime = time[:24].split()
        packedTime = {
            'userEmail' : userEmail,
            'year': year,
            'month': month,
            'day': day,
            'dayOfWeek': dayOfWeek,
            'timeType': timeType,
        }
        if 'Start' in timeType:
            packedTime['startTime'] = nowTime
            TimeClass.startTime(packedTime)
        elif 'End' in timeType:
            TimeClass.endTime(userEmail,nowTime)

    def startTime(packedTime):
        if '+' in packedTime['timeType']:
            db.plus.insert_one(packedTime)
        elif '-' in packedTime['timeType']:
            db.minus.insert_one(packedTime)

    def endTime(userEmail,nowTime):
        packedTime = dict(db.plus.find_one({'userEmail':userEmail}))
        startTime = packedTime['startTime']
        endTime = nowTime
        packedTime['endTime'] = endTime
        if '+' in packedTime['timeType']:
            packedTime['duration'] = TimeClass.tdelta(startTime,endTime)
            db.plus.update_one({'userEmail':userEmail},{"$set": packedTime})

    def tdelta(startTime, endTime):
        tdelta = datetime.strptime(endTime, '%H:%M:%S') - datetime.strptime(startTime, '%H:%M:%S')
        if tdelta.days < 0 :
            tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)

        return str(tdelta)



# 필요한 기능
# 1. ajax-start 받아온 데이터 db로 저장 / 요일 
# 2. ajax - End 가 들어오면, 총 몇시간 몇분인지 계산하여 db 수정
# 3. pie그래프에 표기할 시간 + 남은 잔여시간 계산  - 하루의 끝은 00시 ? 06시 ?






# user = db.users.find_one({'name':'bobby'})
# # 그 중 특정 키 값을 빼고 보기
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# # 생김새
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })
# # 예시 - 오타가 많으니 이 줄을 복사해서 씁시다!
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# user = db.users.find_one({'name':'bobby'})

# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})