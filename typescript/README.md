## typescript를 쓰는이유

1. javascript보다 안정적임
   - 에러가 덜난다.
   - javascript의 모든 에러를 막아주지는 않지만 실수들을 많이 막아줌
   - 자유도는 조금 떨어진다.

## 타입스크립트 기본 지식

    - 타입스크립트는 언어이자 컴파일러(tsc)이다. 컴파일러는 ts코드를 js로 바꿔준다.
    - tsc는 타입검사 역할도 한다.

## 설치

    - npm init -y
        - -y는 default값으로 설정된 package.json을 설정한다는 뜻
    - npm i typescript
    - npx tsc --init
        - tsconfig.json생성됨
    - npx tsc --noEmit
        - 단순히 타입검사만 하는경우
    - npx tsc
        - 타입 검사와 코드 변환까지

# tsconfig.json

    - target : 환경 지정, ES5로 지정하면 인터넷 익스플로러로도 실행가능
    - module : 어떤 모듈시스템을 사용할 것인지

# union, intersection

    - union : 모든속성중 하나만 있으면 됨
    - intersection : 모두 있어야 됨

# 타입 애일리어스와 인터페이스의 상속

        type Animal = {breath: true};
        type Mammalia = Animal & {breed: true};
        type Human = Mammalia & {think: true};

        const me: Human = {breath: true, breed: true, think: true};

        interface A {
            breath: true
        }

        interface B extends A {
            breed: true
        }

        const b: B = {breath:true, breed:true};
        const me2: Human = {breath:true, breed:true, think:true};

    - interface는 같은 이름으로 여러번 선언할 수 있는데
    - 선언할때마다 합쳐짐 ( 확장하기가 좋다 )
    - 남의 라이브러리 코드를 수정하든지 확장하여 사용하기가 좋다.
    - interface앞에는 I, type앞에는 T, enum앞에는 E를 붙이는게 국룰이였지만 지금은 안붙이는게 추세

# void

    - function기준 함수의 리턴값이 없는 경우
    - undefined는 리턴가능 (그 반대의 경우는 불가능하다)
    - 그냥 return; 만 쓰는것도 가능하다.
    - function으로 선언할때, method로 선언할때, parameter로 선언할때 다름
    - 매개변수가 void인 함수는 리턴값이 있어도됨, method도 리턴값이 존재해도 됨 ( 리턴값을 사용하지 않겠다는 의미 )
    - 함수에 직접적인 리턴값이 void인 경우에만 리턴값이 없어야한다.
    - declare function : 타입만 사용하게 끔, 외부에서 만들어진 function을 타입선언할때

# unknown과 any

    - any의 문제점
        - type검사를 안한다는 포기선언
    - unknown
        - 지금 당장 타입이 뭔지 모르겠을때
        - 나중에 쓸때 직접 타입을 정해줌
        - 타입스크립트또한 Error를 unknown으로 해놓음 (원래 any)
        - unknown일때와 남이 만든 타입이 이상하게 지정할때는 제외하면 as는 거의 쓰지않아야한다.

## 타입가드 ( 타입 좁히기 )

    function numOrNumArray(a: number | number[]) {
        if (Array.isArray(a)){
            a.concat(4);
        } else { // number
            a.toFixed(3);
        }
    }

    numOrStr(1);
    numOrStr([1,2,3]);


    class A {
        aaa() {}
    }
    class B {
        bbb() {}
    }
    function aOrB(param: A|B){
        if (param instanceof A){
            param.aaa()
        } else {
            param.bbb()
        }
    }
    aOrB(new A());
    aOrB(new B());

    type B = {type:'b', bbb:string};
    type C = {type:'c', ccc:string};
    type D = {type:'d', ddd:string};

    function typeCheck(a: B|C|D){
        if (a.type === 'b'){
            a.bbb;
        } else if (a.type === 'c'){
            a.ccc;
        } else {
            a.ddd;
        }
    }

    function valCheck(a: B|C|D){
        if (bbb in a){
            a.bbb;
        } else if (ccc in a){
            a.ccc;
        } else {
            a.ddd;
        }
    }
    // 객체를 만들때 type이라는 속성을 따로 만들어서 사용하는것이 좋음


    // 나중에 복잡해지면 커스텀 타입 추론 함수를 만들어서 사용해야 하는 경우도 있음 is가 아니면 판별이 안되는 경우도 있음

    interface Dog { bow: number }
    interface Cat { meow: number }
    function catOrDog(a: Cat | Dog): a is Dog {
        if ((a as Cat).meow) { return false }
        return true;
    }

    function pet(a: Cat | Dog) {
        if (catOrDog(a)){
            console.log(a.bow);
        } else {
            console.log(a.meow);
        }
    }

# {}와 Object

    - {}, Object는 모든 타입 ( null과 undefined 제외 )
    - 객체는 object
    - unknown = {} | null | undefined

# readonly, 인덱스드 시그니처, 맵드 타입스

        interface A {
            readonly a: string,
            b: string
        }
        const aaaa: A = {a: 'hello', b:'hello'}
        aaaa.a = '123' // <- readonly라서 불가능


        // 인덱스드 시그니처
        type A = {[key:string]: number};
        const aaaaa: A = {a:3, b:5, c:7, d:123};

        // 맵드 타입스
        type B = 'Human' | 'Mammal' | 'Animal';
        type A = {[key in B]: B};
        const aaaa5: A = {Human: 'Animal' , Mammal:'Human', Animal:'Mammal'}

# class

    - class에 private, protected 추가
    - 기본은 public
    - private 클래스 안에서만 사용가능
    - protected 상속받은 곳에서도 사용가능
    - implement로 interface구현
    - abstract class, method존재
    - 클래스를 상속받을때 abstract method는 반드시 구현해야함

# optional

        function abc(a: number, b?: number, c: number?) {}
        abc(1)
        abc(1, 2)
        abc(1, 2, 3)

        let obj: { a: string, b?: string }  = { a: 'hello', b: 'world' }
        obj = { a: 'hello' };

# 제네릭

    * 타입에 대한 함수
        function add<T>(x: T, y: T): T { return x + y }
        add<number>(1, 2);
        add(1, 2);
        add<string>('1', '2');
        add('1', '2');
        add(1, '2');


        // 제네릭 선언 위치 기억하기
        function a<T>() {}
        class B<T>() {}
        interface C<T> {}
        type D<T> = {};
        const e = <T>() => {};

        // 제네릭 기본값, extends
        function add<T extends string>(x: T, y: T): T { return x + y }
        add(1, 2);
        add('1', '2')

# 공변성 반공변성

    * 리턴값은 더 넓은 타입이면 대입가능
    * 매개변수는 더 좁은 타입이면 대입가능

# Partial

    * 필수값들을 옵셔널로 사용할 수 있음

# Pick

    * 특정 속성만 가져올 수 있음

# Omit

    * 특정 속성만 거를 수 있음
