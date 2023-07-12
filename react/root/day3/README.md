- map

  - key를 반드시 넣어야함 (성능 최적화 등에 사용)
    - 고유한 값을 key로 지정
      - 예시로 v.fruit + v.taste를 사용함 (고유한 값)
    - 요소가 추가만 되는 배열이면 key값에 i를 써도 되긴 함
      - react에서 key를 기준으로 엘리멘트를 추가하거나 수정 삭제 판단하기 때문에 배열의 순서가 바뀌면 문제가 생김

- 화살표 함수는 소괄호를 지워서 return을 안써줘도 됨
- 화살표 함수를 사용하지 않으면 this문법을 사용할 수 없음

  - constructor안에 this.method = this.method.bind(this)를 통해 바인딩 해주어야 하는데 화살표함수를 사용하면 상관없다.

- 컴포넌트 분리

  - 재사용성
  - 가독성

- react불변성 때문에 array에 push를 사용하면 안됨 변경을 감지하지 못함
- 기존배열을 복사하고 const array2 = [...array1, 2] 새로운 값을 넣어야함
- react는 state의 참조값이 바뀌어야 렌더링을 하는데 push로 넣으면 참조가 바뀌지 않기 때문에 렌더링이 일어나지 않음

- useState

  - 값을 그냥 넣을때 알아서 들어감
  - 함수를 넣을때는 함수의 리턴값이 들어감, 그 다음부터는 리렌더링 되어도 함수가 실행되지 않음 ()를 사용하지 않으면 된다 ()를 사용하면 무시되어 값이 바뀌지는 않지만, 함수가 계속 호출되기 때문에 ()를 빼주자

- props의 문제점

  - 렌더링이 자주 일어나는 문제가 있다.
  - react devtools 크롬 확장 프로그램을 설치하고 Component탭의 setting에서 highlight updates when components render를 체크하면 렌더링 되는 컴포넌트가 보인다.
  - 리렌더링 조건은 props가 바뀌었을때, state가 바뀌었을때 뿐만아니라
  - 부모 컴포넌트가 리렌더링되면 자식 컴포넌트도 자동으로 리렌더링

- 해결법

  - PureComponent사용
  - memo사용 (부모가 바뀔때 자식이 바뀌는것을 막아줌)

- createRef

  - class형 일때 사용
  - const inputRef = createRef();
  - this.inputRef.current.focus();

- props는 자식에서 바꾸면 안된다. 부모에서 바꿔야 함, 실무에서 props를 바꾸는 경우가 있는데 그럴때 props를 state에 넣어서 state를 바꿈
- Context
  - A -> B -> C
  - A에서 C로 props를 넘기고 싶을때, B에게 먼저 넘기고 C로 넘겨야함
  - A -> B -> C -> D -> E -> F -> G
  - 컴포넌트 갯수가 많아지면 쓸데없는 렌더링이 생길 위험이 있어서 A에서 바로 G로 옮기는 법이 컨텍스트
