interface Profile {
  name: string;
  age: number;
  married: boolean;
}

// type P<T> = {
//   [Key in keyof T]?: T[Key];
// };

const jongkyu: Profile = {
  name: "jongkyu",
  age: 28,
  married: false,
};

// const newJongkyu: P<Profile> = {
//   name: "jongkyu",
//   age: 28,
// };

type P<T, S extends keyof T> = {
  [Key in S]: T[Key];
};

const newJongkyu: P<Profile, "name" | "age"> = {
  name: "kongkyu",
  age: 28,
};
