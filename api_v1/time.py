from . import api
from flask import jsonify, request, Blueprint, session, redirect
from models import db , MyUser , TimeCheck

# import requests
# from models import Myuser , TimeCheck, db


@api.route('/timecheck' , methods=["GET", "POST", "PUT", "DELETE"])
def timeCheck():

    if request.method == "POST":
        timeType = request.form['timeType']
        if timeType == '-':
            # nowDate = request.form['nowDate'][:-1]
            # timeType = request.form['timeType']
            # nowTime= request.form['nowTime'][:8]
            # status = request.form['status']

            # print(nowDate, nowTime, timeType, status)
            # print(request.form)
            userEmail = session['userEmail']
            TimeCheck.timePacking(userEmail , request.form)
        return jsonify({'result':'success','msg':'POSTsuccess'})


    elif request.method == "":
        
        return jsonify({'result':'success', 'msg':'PUTSuccess'})
        

            
    elif request.method == "GET":
        return jsonify({'result': 'success', 'msg': 'GETsuccess'})
            



# myuser_id
# time_type
# whatTime
# startEnd
# timeStamp