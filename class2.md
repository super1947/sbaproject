클래스 하나가 단위 unit이 됩니다.
객체지향에는 디자인패턴 개념이 존재
패턴조합을 통해 큰 개념의 패턴 -> MVC 패턴이라고 함.

model, view, controller 이렇게 조합 -> Java, C언어에서 주로 사용하는 개념

model : 데이터 처리 -> API 서버 -> Python -> Tensorflow
view : 화면UI 처리 -> UI 서버 -> React
controller : model + view를 연결 -> 네트워크라고 함. -> Flask(app.py) -> RESTful 방식

이 지점에서 팀내에서 나의 역할을 고민하면 된다.
곧 취업시 자신을 어필할 수 있는 혹은 자신있는, 흥미있는 카테고리를 결정하는 게 좋다.

Backend Tier ( API 서버 구축 담당 : Java, C, Python, SQL)
Frontend Tier( UI 서버 구축 담당 : Javascript, HTML, React)

모델을 제작하고 뷰를 만들어서 컨트롤러로 연결
프로토타입
독자적으로 움직이는 모듈
5개의 모듈(개인이 작성)을 합쳤을 때, 조립이 잘 되서 작동이 잘 되면 1단계 패스.

titanic 폴더에
dataset (test.csv, train.csv)가 존재하고
entity(속성) + service(기능) = 객체(object)

def **init**(self, ...) -> 속성
def abc(): -> 기능
결국 class는 객체를 정의하는 것

class가 여러 개 (entity, service) 모여서 다시 큰 개념의 객체를 이룬다.
그때 이것은 클래스라 하지 않고 model이라고 한다.

패키지는 같은 컨셉을 공유하는 클래스의 집합..
모델에 AI 개념이 없으면 web에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 된다.

여기서 AI 개념이라고 하면 머신러닝(기계학습) 코딩의 유무..
dataset을 추가하면 이를 지도학습이라고 함
dataset이 없으면 비지도학습이라고 함
지금 타이타닉은 dataset을 모델에 넣었으므로 지도학습을 하겠다는 의미

# 외부에 있는 파이썬 파일을 import 해야 속성, 기능을 사용할 수 있다.

# 내부에서는 이것을 인스턴스화 해야 한다. entity = Entity()

# entity는 인스턴스화 된 객체, Entity는 클래스, Entity()는 생성자

# 결론 : 객체지향에서는 속성과 기능을 호출하는 구조로 두 가지 방식이 있는데,

        calc = Calculator()가 있다고 하면
        calc는 인스턴스 객체가 되고
        Calculator는 클래스 객체(스태틱)라고 한다.
        calc.sum()하면 인스턴스 호출방식 = dynamic
        Calculator.sum() 하면 클래스 호출방식 = static

from titanic.entity import Entity
from titanic.service import Service

class Controller:
def **init**(self):
self.entity = Entity()
self.service = Service()

=====================================================================

페이로드 (컴퓨팅)

this.fname = payload -> setter 할당연산자(=) 있으면 setter
this.fname 만 있으면 -> getter 할당연산자(=) 없으면 getter

- PassengerId,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
  -> 메타데이터, Schema, features, variables, properties

- 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
- 2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
  -> row, instance, raw data

  현재 크롤링은 정해진 url만 처리. -> static

  dynamic은 payload로 url을 주면
  재활용해서 서로 다른 결과를 만들 수 있다.

  ====================================================================

  MVC 코딩 하는 순서

  구조를 만든다.
  1. model -> view -> controller로 연결(network) 한다.
  model = entity + service 속성 + 기능 -> 모델객체
  

  =======================================================================

  Data 수집
  - 방법론
  - 정형 (csv) = 스키마구조가 존재하는 것 = Computer 인식
  - 비정형 (웹, 문서)= 스키마구조가 존재하지 않는 것 = Computer 인식불가
      
  Data 정제, 정형화
  Modeling
  Learning
  Machine
  Evaluation


정규 표현식 re
? : unique
* : null 허용 (all)
+ : not null
{n} : counting

1. 개발환경 설정 -> context complete!!
1.1 Model 개발환경 완료
1.2 View 개발환경 완료
1.3 Controller 개발환경


STEP 2의 목표
1. Model : Python OOP에서 reuse를 고민합니다.
2. View : React 



