"use strict";
// const head: Element = document.querySelector("#head");
// console.log(head);
const head = document.querySelector("#head"); // head가 무조건 있음을 보장함, 비추천!! 혹시 없을 수도 있음
const aa = "world"; // ctrl + spacebar 로 자동완성가능
const bb = `hello ${aa}`;
const aa2 = 3 /* EDirection.Up */;
const cc2 = 3 /* EDirection.Up */;
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
const ODirection2 = {
    Up: 0,
    Down: 1,
    Left: 2,
    Right: 3,
};
// 로 사용할 수 있다.
// keyof
// typeof
const obj2 = { a: "123", b: "hello", c: "world" };
