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
