## 라이프 사이클

- jsx가 리액트 dom에 컴포넌트를 붙여줄때 특정한 동작을 할 수 있다.
- componentDidMount()
  - 렌더가 처음 실행되고 성공적으로 실행되었다면 실행
  - 리렌더링시 실행되지 않음
  - 비동기 요청을 많이 함
- componentWillUnMount()

  - 컴포넌트가 제거되기 직전

- 클래스의 경우

  - constructor -> render -> ref -> componentDidMount
  - (setState/props 바뀔때) -> shouldComponentUpdate(true) -> render -> componentDidUpdate
  - 부모가 나를 없앴을 때 -> componentWillUnmount -> 소멸

- 즉시실행함수, 클로저 개념 다시 공부하자
