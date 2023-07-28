- 소수 계산

  - 컴퓨터는 이진법으로 계산하기 때문에
  - 0.1 + 0.2 는 0.3이라고 생각하지만 실제로는 0.30000000000000004이 나온다.
  - 소수끼리 계산할때는 정수로 바꿔준다음에 다시 소수로 돌리는 방식을 사용하면 된다.
  - 0.3 - 0.1 = 0.19999999999999998
  - (0.3*10 - 0.1*10) / 10 = 0.2

- 객체

  - {}를 사용해 객체를 표현한것을 객체 리터럴이라고 한다.
  - 객체명.속성 = 값; 으로 새로운 값을 넣거나 수정할 수 있다.
  - delete 객체명.속성; 으로 삭제
  - 함수나 배열이 객체인 이유는 객체의 성질을 모두 다 사용할 수 있기 때문이다.

- 원시 값은 값이 같으면 같다, 객체는 변수에 저장해놓지않으면 생김새가 같아도 다른 객체임

- prompt 사용자로부터 값을 받음
- alert 사용자에게 경고 메시지 표시
- confirm 사용자의 확인을 요구

- border-box border를 기준으로 크기지정
- 함수가 함수를 리턴하는 함수를 고차함수라고 부른다. high order function
- removeEventListener 를 사용하려면 함수를 변수에 저장한 후에 add, remove해야함

- this

  - ES6에서는 use strict모드가 자동 적용
  - this는 함수가 호출될때 정해진다.

  ```
    const obj = {
      name : 'jonyku',
      sayName: function(){
        console.log(this.name);
      },
    };

    obj.sayName() ---> 'jongkyu'
    const aaa = obj.sayName;
    aaa() ---> 'window'
  ```

  - this가 바뀌는 경우 (기본적으로는 window)

    - new붙여서 호출하는 경우
    - 앞에 객체가 붙어서 객체의 메소드를 호출하는 경우
    - bind, apply, call

  - 그렇다면

  ```
    const obj = {
      name:'jongkyu',
      sayName(){ // sayName: function()하고 같음
        console.log(this.name);
        function inner(){
          console.log(this.name);
        }
        inner();
      }
    }
    obj.sayName(); //의 출력값은?
  ```

  - 첫번째 console.log()에서는 jongkyu가 출력되고, 두번째 console.log()에서는 window가 출력됨(빈칸)
  - inner를 호출할 당시 this를 바꾸는 행동을 안했기 때문에
  - 또 다른 예제

  ```
    const obj = {
      name:'jongkyu',
      sayName(){ // sayName: function()하고 같음
        console.log(this.name);
        const inner = () => {
          console.log(this.name);
        }
        inner();
      }
    }
    obj.sayName(); //의 출력값은?
  ```

  - inner를 화살표 함수로 바꿈
  - 이때 출력은 둘다 jongkyu로 나옴
  - 왜그럴까??

    - 화살표 함수는 부모의 this를 사용, 여기서 호출이 obj.sayName()으로 호출 되었기 때문에 this는 jongkyu를 가리킬수 있게 됨

  - this를 분석할 수 없는 케이스
    - addEventListener('click',function(){console.log(this)})와 같이 내부에서 함수를 어떻게 호출하는지 모르면 this를 알 수 없다.
    - addEventListener('click', ()=>{console.log(this)}) 와 같이 그냥 화살표함수를 사용하면 화살표함수는 부모의 this를 따라가기 때문에 this를 알 수 있다.
    - 선언과 호출 구분을 잘합시다.

- 프로미스

  - 콜백 헬을 방지하기 위함
  - 내용이 실행이 되었지만 결과를 아직 반환하지 않은 객체
  - Then을 붙이면 결과를 반환함
  - 실행이 완료되지 않았으면 완료된 후에 Then 내부 함수가 실행됨
  - Resolve(성공 리턴 값) -> Then으로 연결
  - Reject(실패 리턴 값) -> catch로 연결
  - Finally 부분은 무조건 실행됨
  - Promise.all(배열)로 여러 개의 프로미스를 동시에 실행 가능함 -> allSettled로 실패한 것만 추려낼 수 있어서 allSettled 사용
  - 프로미스는 실행됐는데 결괏값을 나중에 쓸 수 있음 <- 큰 장점

- async/await

  - A싱크라고 읽어라!
  - ajax
  - 변수 = await 프로미스; 인경우 프로미스가 resolve된 값이 변수에 저장
  - async함수에서 리턴한 값은 then으로 받아야함 혹은 const name = await main()처럼 await를 붙여야함
  - 대신 await은 catch가 없기 때문에 try/catch문을 사용해야 함 ,, reject가 없어서

- 비동기

  - 동시가 아닌 순서의 문제
  - 동기코드는 위에서 아래 왼쪽에서 오른쪽
  - 비동기코드는 코드순서랑 실제 실행 순서가 다르다.
  - 자바스크립트는 싱글스레드라서 동시라는 개념이 없다.
  - 백그라운드(브라우저, OS, 자바스크립트 엔진)에 들어가는 작업들은 동시에 가능 (자바스크립트가 아니므로, setTimeout의 timer, promise, ajax요청, eventListener 등 백그라운드에 들어감, 비동기면 백그라운드를 거의 거친다고 보면 됨)
  - 백그라운드에 들어간 작업은 task queue (macro, micro) 를 거쳐서 call stack으로 올라감
  - 이벤트 루프는 큐에서 호출스택으로 작업을 하나씩 올려줌 (호출스택이 비어있을경우)

- task queue

  - micro
    - promise
    - process.nextTick
    - micro가 우선순위가 높아서 먼저 실행된다.
  - macro
    - 나머지 모두

- 무지성 await 연달아 쓰기 금지!
  - 굳이 순차적으로 할 필요 없는 작업들은 요청을 동시에 보내버리고 Promise.allSettled로 받는 것이 시간상 이득이다.
  - async 사용할 때 무지성 await 사용 금지!
