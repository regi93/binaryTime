# binaryTime





## 배포 주소

~~youjunyong.shop/~~  도메인 만료 ㅠ





## 동기

 내가 자주 사용하는 어플중에 공부시간을 체크하는 어플이 있다. 하지만 딴짓하며 낭비하는 시간과 공부하는 시간을 비교해보고 싶다는 생각을 했고,  Web에서 작동한다면, 테블릿 , pc , 스마트폰에서 실시간으로 작동이 가능하다고 생각이 들어 만들어 보았다. 





## 사이트맵



### 회원가입 / 로그인

![img](https://blog.kakaocdn.net/dn/n7coU/btqFXhf07eM/X5wgQA9JqOLiphzgmvj0G1/img.png)



## Time record

![img](https://blog.kakaocdn.net/dn/xK2BQ/btqFVi1iexc/2RqC1azGELg8kivjEpRyK0/img.png)



PlusTime 과 MinusTime을 측정한다. 각 측정된 시간들은 Timeline으로 기록되며, 내용을 편집하거나 삭제 할 수 있다.

현재 Plus시간인지, Minus시간인지에 따라서 통통 튀는 공애니메이션 색깔이 바뀐다.

휴대폰에서 측정하던 도중, PC에서 로그인 했을때 카운팅 시간이 유지가 안되어서 많이 삽질했다.



### View Chart

![img](https://blog.kakaocdn.net/dn/czDJNp/btqFT8d1wEN/7Ak45rp2PrBaKBxL3f4E91/img.png)



Chart.js 라는 프레임워크를 사용했다. 파이그래프를 이용했으며, 날짜별로 정렬되도록 구현했다.

* 흰부분 : 아무것도 측정되지 않은 시간 합계
* 파란부분 : 기록된 Plus time의 합계
* 빨간부분 : 기록된 Minus time의 합계
* 노란부분 : Zero타임이라 이름붙이고 어쩔수 없이 사용되는 시간(취침, 식사)의 합이다. Defalut로 10시간이다.






## 사용 프레임워크



* Flask
* Chart.js 
* AWS EC2(배포)
* 가비아(도메인 네임 서비스)
* MongoDB (pymongo)
* 테마, CSS는 BootStrap 사용





## 파일 구성

![img](https://blog.kakaocdn.net/dn/ctE3lR/btqFT9jIme5/svQa9opPKh8lyn2uG2mD71/img.png)





### RESTful



회원가입을 제외한 모든 데이터 통신은 REST 하게 구성했다.

> app.py 일부

```
from api_v1 import api as api_v1

app = Flask(__name__)
app.register_blueprint(api_v1 , url_prefix='/api/v1')
```

flask_blueprint를 이용하여 api_v1로 모듈을 나누어 주었고, 최대한 간단하게 json을 구성해서 mongoDB로 넣어주었다.

 

> api_v1의 일부

```
from . import api
from flask import jsonify, request, Blueprint, session, redirect ,flash
from models import db , MyUser , SaveTime , LoadTime
import requests


@api.route('/plustime' , methods=["GET", "POST"])
def plustime():
    if request.method == "POST":
        timeType = request.form['timeType']
        time = request.form['Time']
        
        userEmail = session.get('userEmail', None)
        save = SaveTime
        save.saveTime(userEmail , time, timeType)
        if 'Start' in timeType :
            return jsonify({'result':'success','msg':'Plustime 시작'})
        elif 'End' in timeType :
            return jsonify({'result':'success','msg':'Plustime 끝'})
```





## 개선사항

 원페이지 + 비동기 통신을 통해서 최대한 어플같은 느낌으로 만들어보고 싶었다. 만들고 나니 역시 웹보다는 어플리케이션에 어울리고, 어플리케이션일때 편리한 기능들인것 같다.

 기록 (계획 및 설계, 그리고 개발노트?) 을 남겼더라면 좋았겠다 라는 생각을 했다. 계획을 구체적으로 세우지 않으니 그때그때 마음가는대로 변동한 사항들이 많았기 때문에 아쉬웠다. 





