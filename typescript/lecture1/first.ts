const a: number = 5;
const b: string = "5";
const c: boolean = true;
const d: undefined = undefined;
const e: null = null;
const h: any = "123"; // 아무거나 다됨, 하지만 any를 쓰면 아무의미가 없다.
// const f: symbol = Symbol.for("abc");
// const g: bigint = 1000000n

// function add(x: number, y: number): number {
//   // 매개변수 바로뒤가 리턴값 타입
//   return x + y;
// }
// type Add = (x: number, y: number) => number;
// const add: Add = (x, y) => x + y;

interface Add {
  (x: number, y: number): number;
}
const add: Add = (x, y) => x + y;
const obj: { lat: number; lon: number } = { lat: 37.5, lon: 127.5 };
const arr: string[] = ["123", "456"];
const arr2: number[] = [123, 456];
const arr3: Array<number> = [123, 456]; // 제네릭 방식으로도 가능
const arr4: [number, number, string] = [123, 456, "hello"];

// 자바스크립트 변수, 매개변수, 리턴값에 타입을 붙이는것!
// 타입스크립트는 에러메시지가 굉장히 친절하다. 꼭 읽어보고 해결할 생각을 하자
// 타입 추론이 잘못되면 그때 고치면 됨, 타입추론을 any로하면 바꿔주면 된다. 매개변수는 반드시 타이핑 해주어야함

// js 변환시 as(as type1 as type2, 타입변환)가 사라진다.
