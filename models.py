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



class SaveTime:
    def saveTime(userEmail , time , timeType):
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
            SaveTime.startTime(packedTime)
        elif 'End' in timeType:
            SaveTime.endTime(userEmail,nowTime,timeType)

    def startTime(packedTime):
        if '+' in packedTime['timeType']:
            db.plus.insert_one(packedTime)
        elif '-' in packedTime['timeType']:
            db.minus.insert_one(packedTime)

    def endTime(userEmail,nowTime,timeType):
        if '+' in timeType:
            # packedTime = dict(db.plus.find_one({'userEmail':userEmail}))
            packedTime = dict(db.plus.find_one({ '$and': [ { 'userEmail' : userEmail }, { 'duration':{'$exists' : 0 }} ] }, {'_id' : 0}))
            startTime = packedTime['startTime']
            endTime = nowTime
            packedTime['endTime'] = endTime
            packedTime['duration'] = SaveTime.tdelta(startTime,endTime)
            db.plus.update_one({ '$and': [ {'userEmail':userEmail }, {'duration' :{'$exists' : 0}} ] } , {"$set": packedTime})
        elif '-' in timeType:
            packedTime = dict(db.minus.find_one({ '$and': [ { 'userEmail' : userEmail }, { 'duration':{'$exists' : 0 }} ] }))
            startTime = packedTime['startTime']
            endTime = nowTime
            packedTime['endTime'] = endTime
            packedTime['duration'] = SaveTime.tdelta(startTime,endTime)
            # db.minus.update_one({'userEmail':userEmail},{"$set": packedTime})    
            db.minus.update_one({ '$and':[{'userEmail':userEmail }, {'duration' :{'$exists' : 0}} ] },{"$set": packedTime})


    def tdelta(startTime, endTime):
        tdelta = datetime.strptime(endTime, '%H:%M:%S') - datetime.strptime(startTime, '%H:%M:%S')
        if tdelta.days < 0 :
            tdelta = timedelta(days=0, seconds=tdelta.seconds, microseconds=tdelta.microseconds)
        return str(tdelta)
    
    def saveArticle(userEmail ,timeType, article, startTime, endTime):
        if '+' in timeType:
            db.plus.update_one({"$and": [{'endTime':endTime}, {'userEmail':userEmail}, {"startTime":startTime}]},
                {'$set':{'article':article}})
        else : 
            db.minus.update_one({"$and": [{'endTime':endTime}, {'userEmail':userEmail}, {"startTime":startTime}]},
                {'$set':{'article':article}})

class LoadTime():
    def loadDay(userEmail , month, day ):
        loadPlus = list(db.plus.find({'$and' : [{'userEmail':userEmail},{'month' : month},{'day':day} ]} , {'_id':0}))
        sumPlus = 0
        for i in loadPlus:
            h , m , s = i['duration'].split(':')
            sumPlus += int(h)
            sumPlus += float(m)/60
            sumPlus +=  float(s)/3600
        restOfTime = 24
        loadMinus = list(db.minus.find({'$and' : [{'userEmail':userEmail},{'month' : month},{'day':day} ]} , {'_id':0}))
        sumMinus = 0
        for i in loadMinus:
            h , m , s = i['duration'].split(':')
            sumMinus += int(h)
            sumMinus += float(m)/60
            sumMinus +=  float(s)/3600
        
        zeroTime = 8
        restOfTime -= (sumMinus + sumPlus + zeroTime)
        return sumPlus , sumMinus , zeroTime , restOfTime

    def todaysDate():
        today = str(datetime.today())
        arrMonth = ['Jan', 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul' ,'Aug' ,'Sep' ,'Oct' ,'Nov' ,'Dec']
        todayDay = today[8:10]
        todayMonth = arrMonth[int(today[5:7])-1]
        return [todayDay , todayMonth]

    def NumDateToStr(numDate):
        arrMonth = ['Jan', 'Feb' , 'Mar' , 'Apr' , 'May' , 'Jun' , 'Jul' ,'Aug' ,'Sep' ,'Oct' ,'Nov' ,'Dec']
        month, day, year = map(int, numDate.split('/'))
        month = arrMonth[month - 1]
        return [str(day) , month]
    def DelList(userEmail ,timeType, startTime, endTime):
        if '+' in timeType:
            db.plus.delete_one({"$and": [{'endTime':endTime}, {'userEmail':userEmail}, {"startTime":startTime}]},{})

        else :
            db.minus.delete_one({"$and": [{'endTime':endTime}, {'userEmail':userEmail}, {"startTime":startTime}]},{})

    def chartList(userEmail):
        dateList = list(db.plus.find({'userEmail':userEmail},{'_id':0}).sort('_id', -1))
        date = []
        for i in dateList:
            date.append(i['month']+ "-"+ i["day"])
        date = set(date)
        date = list(date)
        return date


    def NowStatus(userEmail):
        plusStatus = list(db.plus.find({'userEmail':userEmail},{'_id':0}).sort('_id', -1).limit(1))
        minusStatus = list(db.minus.find({'userEmail':userEmail},{'_id':0}).sort('_id', -1).limit(1))
        
        if (len(plusStatus) !=0) and ("endTime" not in plusStatus[0]):
            startTime = plusStatus[0]['startTime']
            return ["plus" , startTime]
        elif (len(minusStatus) !=0) and ("endTime" not in minusStatus[0]):
            startTime = minusStatus[0]['startTime']
            return ["minus" , startTime]
        else:
            return "zero"


LoadTime.chartList("abc@abc.com")


# db.getCollection('minus').find({ $and: [ { userEmail : 'abc@abc.com' }, { duration:{$exists: true }} ] })
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