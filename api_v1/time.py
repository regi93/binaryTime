from . import api
from flask import jsonify, request, Blueprint, session, redirect
from models import db , MyUser , TimeClass
import requests


@api.route('/plustime' , methods=["GET", "POST"])
def plustime():
    if request.method == "POST":
        timeType = request.form['timeType']
        time = request.form['Time']
        userEmail = session['userEmail']
        timeClass = TimeClass
        timeClass.splitTime(userEmail , time, timeType)
        if 'Start' in timeType :
            return jsonify({'result':'success','msg':'PlusTime 시작'})
        elif 'End' in timeType :
            return jsonify({'result':'success','msg':'PlusTime 끝'})


@api.route('/minustime' , methods=["GET", "POST"])
def minustime():
    if request.method == "POST":
        timeType = request.form['timeType']
        if 'Start' in timeType :
            return jsonify({'result':'success','msg':'minusTime 시작'})
        elif 'End' in timeType :
            return jsonify({'result':'success','msg':'minusTime 끝'})
    
@api.route('/chart' , methods = ["GET", "POST"])
def chart():
    pass