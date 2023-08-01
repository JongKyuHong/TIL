## SPA를 왜 사용하는가?

- 웹앱
  - 앱 같은 느낌이 나는 사이트들
  - 단순히 외관상 뿐만 아니라 기능적으로도 웹 애플리케이션들이 기능적으로 많은 것들을 제공함
  - 대표적으로 Gmail이 있음
  - 기존 웹사이트들 보다 데이터가 더 많다.
  - 데이터가 바뀌면 화면도 맞춰서 바뀌어야 하는데 단순 JavaScript로 구현하기는 상당히 힘들다.
  - 그렇기 때문에 react를 사용함
  - vue, angular도 다 다른 방식으로 이를 해결한 것

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
