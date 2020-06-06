from pymongo import MongoClient 
client = MongoClient('localhost', 27017) 
db = client.dbflask

class MyUser():
    def login(userEmail):

        loginInfo = db.userInfo.find_one({'userEmail': userEmail})
        if loginInfo == None:
            return "check your Email"
        loginPassword = loginInfo['password']
        loginUserName = loginInfo['userName']
        return [loginPassword,loginUserName]


class TimeCheck():
    def timePacking(userEmail , request):
        nowDate = request['nowDate'][:-1]
        timeType = request['timeType']
        nowTime= request['nowTime'][:8]
        status = request['status']
        packedTime = {'userEmail': userEmail, 'nowDate':nowDate , 'nowTime':nowTime, 'timeType':timeType,'status':status}
        db.timeRecord.insert_one(packedTime)
        return packedTime
        # day - {*UserEmail : abd@abd.com,
#            desc : { date : 2020.10.30 ,
#                        time : +150 , -230, 120} , 
#                       {date : 2020.10.31,
#                        time : 220 , - 130 , +259}

# a = {'userEmail': 'abc@abc.com',
#     "desc": [{'date': '2020-06-06', 'time': [+1,-3,4,5,6]},
#             {'date': '2020-06-05','time' : ['+33' , '-50', '+39']}]
# }

# db.timeRecord.insert_one(a)
# print(a)