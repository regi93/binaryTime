from . import api
from flask import jsonify, request, Blueprint, session, redirect ,flash
from models import db , MyUser , SaveTime , LoadTime
import requests


@api.route('/plustime' , methods=["GET", "POST"])
def plustime():
    if request.method == "POST":
        timeType = request.form['timeType']
        time = request.form['Time']
        userEmail = session['userEmail']
        save = SaveTime
        save.saveTime(userEmail , time, timeType)
        if 'Start' in timeType :
            return jsonify({'result':'success','msg':'PlusTime 시작'})
        elif 'End' in timeType :
            return jsonify({'result':'success','msg':'PlusTime 끝'})


@api.route('/minustime' , methods=["GET", "POST"])
def minustime():
    if request.method == "POST":
        timeType = request.form['timeType']
        time = request.form['Time']
        userEmail = session['userEmail']
        save = SaveTime
        save.saveTime(userEmail , time, timeType)
        if 'Start' in timeType :
            return jsonify({'result':'success','msg':'MinusTime 시작'})
        elif 'End' in timeType :
            return jsonify({'result':'success','msg':'MinusTime 끝'})

@api.route('/chart' , methods = ["GET", "POST"])
def chart():
    userEmail = session['userEmail']
    loadtime = LoadTime
    if request.method == 'GET':
        a = loadtime.loadDay(userEmail, 'Jun' , '16')
        return jsonify({'result': 'success','msg':'list 연결되었습니다!' , 'timeInfo' : a })

    elif request.method == 'POST':
        date = request.form['date']
        day = loadtime.NumDateToStr(date)[0]
        month = loadtime.NumDateToStr(date)[1]
        a = loadtime.loadDay(userEmail, month , day)
        print(a)
        return jsonify({'result': 'success','msg':'GET!!' , 'timeInfo' : a})

    
