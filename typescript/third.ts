interface Arr<T> {
  forEach(callback: (item: T) => void): void;
  map<S>(callback: (v: T) => S): S[];
  filter<S extends T>(callback: (v: T) => v is S): T[];
}

const a: Arr<number> = [1, 2, 3];
a.forEach((item) => {
  console.log(item);
});
a.forEach((item) => {
  console.log(item);
  return "3";
});

const b: Arr<string> = ["1", "2", "3"];
b.forEach((item) => {
  console.log(item);
});
b.forEach((item) => {
  console.log(item);
  return "3";
});

const c: Arr<number> = [1, 2, 3];
const c1 = c.map((v) => v + 1); // [2, 3, 4]
const c2 = c.map((v) => v.toString());
const c3 = c.map((v) => v % 2 === 0);

const d: Arr<string> = ["1", "2", "3"];
const e = d.map((v) => +v);

const f: Arr<number> = [1, 2, 3];
const f1 = f.filter((v): v is number => v % 2 === 0);

const f2: Arr<number | string> = [1, "2", 3, "4", 5];
const f3 = f2.filter((v): v is string => typeof v === "string");
const f4 = f2.filter((v): v is number => typeof v === "number");
