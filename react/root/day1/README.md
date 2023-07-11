## 웹 팩으로 빌드 하기

```
npm init
npm i react react-dom
npm i -D webpack webpack-cli
npm i -D babel-loader @babel/core @babel/preset-env @babel/preset-react
# @babel/preset-env가 옛날 브라우저더라도 바벨로 맞춰줌
# @babel/preset-react가 있어야 jsx를 쓸 수 있음
```

- 설치 후 webpack.config.js 만듦

  - mode 설정 development, production
  - devtools 설정 eval, hidden-source-map
  - resolve .jsx .js 넣으면 생략 가능
  - entry 최초 진입 점인 자바스크립트 파일
  - output 결과물, filename과 path 설정
  - module에는 로더나 여러가지 옵션(preset, plugin 설정)
  - preset target 브라우저 설정 시에 https://github.com/browserslist/browserslist#queries에서 찾아볼 수 있다.

- npx webpack, npm run dev로 실행
