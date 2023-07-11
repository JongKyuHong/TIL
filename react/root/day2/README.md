## 자동 빌드

```
npm i react-refresh @pmmmwh/react-refresh-webpack-plugin -D
npm i -D webpack-dev-server
```

- packages.json scripts수정

  - "dev": "webpack serve --env development"

- webpack.config.js에서 "@pmmmwh/react-refresh-webpack-plugin" require후 plugins에 넣어줌
- loader에 plugins에 'react-refresh/babel'추가

```
devServer: {
    devMiddleware: {publicPath:'/dist/'}, // 웹팩이 빌드한 파일들이 위치하는 곳
    static: {directory: path.resolve(__dirname)}, // 실제로 존재하는 정적 파일들의 경로
    hot: true,
},
// 추가
```

- client.jsx 변경사항

  - react 18 버전이라서 ReactDom을 react-dom/client에서 가져옴,
  - ReactDom.createRoot(루트노드).render(); 식으로 수정

- log

  - HMR : hot module server
  - wds : webpack dev server

- controled input
  - value에 state, onChange에 setState가 들어있는게 controlled input
  - 리액트에서는 이것을 권장
- uncontrolled input

  - 두개가 없는게 uncontrolled input
  - 만약 value값이 onSubmitForm에서만 사용된다면 고려해 볼만 하다.
  - e.target.children.word or e.target[index]로 입력값에 접근가능

- import 와 require의 차이
  - require는 commonjs문법, import는 es6문법
  - require는 어디서나 불러올 수 있지만, import는 파일 맨 위에서만 불러오기를 할 수 있음
  - 일반적으로 import가 필요한 모듈부분만 선택하고 로드 할 수 있기때문에 더 선호
  - webpack의 babel이 import를 변환해주기 때문에 jsx쪽에서는 import를 사용해도 좋다.
  - 엄밀하게는 export default와 module.exports는 다르지만 리액트에서는 호환된다는 정도로 생각하자
