// const head: Element = document.querySelector("#head");
// console.log(head);

const head = document.querySelector("#head")!; // head가 무조건 있음을 보장함, 비추천!! 혹시 없을 수도 있음
type World = "world" | "hell";
const aa: World = "world"; // ctrl + spacebar 로 자동완성가능

const bb = `hello ${aa}`;

type Greeting = `hello ${World}`; // 이런식으로 정교한 타입을 만들 수도 있다.

// enum
// 여러개의 변수들을 하나의 그룹으로 묶고싶을때 사용
// 자바스크립트에 남지않음
const enum EDirection {
  Up = 3,
  Down = 5,
  Left,
  Right,
}

const aa2 = EDirection.Up;
const cc2 = EDirection.Up;

const ODirection = {
  Up: 0,
  Down: 1,
  Left: 2,
  Right: 3,
};
// 자바스크립트에 남음
// 남길지 말지 고민되면 남겨라
// 위의 코드를 사용하면 타입스크립트는 Number로 추론한다.
// 있는 값을 그대로 사용하고 싶으면 뒤에 as const를 붙이거나 (상수로 사용하겠다, readonly로 고정됨)

const ODirection2: { Up: 0; Down: 1; Left: 2; Right: 3 } = {
  Up: 0,
  Down: 1,
  Left: 2,
  Right: 3,
};

// 로 사용할 수 있다.

// keyof
// typeof
const obj2 = { a: "123", b: "hello", c: "world" } as const;
type Key = keyof typeof obj2; // typeof의 key를 뽑아낸다.
type Key2 = (typeof obj2)[keyof typeof obj2]; // 값을 뽑아낸다. obj2에 as const사용해야함 사용안하면 널널하게 string으로 추론함
