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

def **init**(self, ...)
