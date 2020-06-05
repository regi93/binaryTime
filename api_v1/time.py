from . import api
from flask import jsonify, request, Blueprint, session, redirect
# import requests
from models import Myuser , TimeCheck, db


@api.route('/timecheck' , methods=["GET", "POST", "PUT", "DELETE"])
def timeCheck():

    if request.method == "POST":
        return jsonify({'result':'success','msg':'POSTsuccess'})


    elif request.method == "PUT":
        timeType = request.form['timeType']
        if timeType == 'minus':
            timecheck = TimeCheck()
            # timecheck.timeType = timeType
            # db.session.add(timecheck)  
            # db.session.commit()  
        return jsonify({'result':'success', 'msg':'PUTSuccess'})
        

            
    elif request.method == "GET":
        return jsonify({'result': 'success', 'msg': 'GETsuccess'})
            



# myuser_id
# time_type
# whatTime
# startEnd
# timeStamp