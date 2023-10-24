## 라이프 사이클

- jsx가 리액트 dom에 컴포넌트를 붙여줄때 특정한 동작을 할 수 있다.
- componentDidMount()
  - 렌더가 처음 실행되고 성공적으로 실행되었다면 실행
  - 리렌더링시 실행되지 않음
  - 비동기 요청을 많이 함
- componentDidUpdate()
  - 리렌더링 될 시에 실행
- componentWillUnMount()

  - 컴포넌트가 제거되기 직전

- 클래스의 경우

  - constructor -> render -> ref -> componentDidMount
  - (setState/props 바뀔때) -> shouldComponentUpdate(true) -> render -> componentDidUpdate
  - 부모가 나를 없앴을 때 -> componentWillUnmount -> 소멸

- 즉시실행함수, 클로저 개념 다시 공부하자

- 고차함수

  - onClick={()=>this.onClickBtn('바위')}를
  - onClick = (choice) => () => {}로 쓸 수 있다. 자주쓰는 패턴

- useEffect

  - componentDidMount, componentDidUpdate, componentWillUnmount 역할을 모두 합쳐놓음
  - return 문에 componentWillUnmount시에 실행될 내용을 넣음
  - 두번째 인수인 배열에는 바뀌는 state를 넣음
  - 빈 배열로 두면 처음에만 한번 실행되고 다시 실행되지 않음

- 함수의 경우 렌더링되면 전체가 실행된다.

- useMemo

  - 두번째 인자가 바뀌지 않는 한 다시 실행되지 않음
  - 복잡한 함수 결과값(리턴값)을 기억함, useRef의 경우는 일반 값을 기억
  - 컴포넌트도 기억할 수 있다.

- useCallback

  - 함수 자체를 기억
  - 함수 컴포넌트가 재실행되도, useCallback을 써놓은 함수자체가 재생성되지 않는다.
  - useCallback안에서 state를 사용할 것이면 두번째 인자에 state를 넣어놓아야 함
  - 두번째 인자가 바뀌면 새로 실행 됨
  - 자식에게 함수를 props로 넘길때는 useCallback을 사용해야함
  - 함수자체에는 변경점이 없는데 계속해서 생성할 위험이 있음

- hooks 사용법

  - 조건문 안에 절대로 넣으면 안됨
  - 함수나 반복문 안에도 웬만하면 안넣는게 좋다.
  - hooks는 항상 최상위로 빼서 실행순서를 지킬 수 있게 하는게 좋다.
  - useEffect를 사용하건데 componentDidMount가 아니라 componentDidUpdate일때만 실행하고 싶다면 useRef로 값을 만들어서 조건문을 걸어서 최초 렌더링시에 실행이 되지 않게끔 하자.

- useReducer

  - dispatch안에 들어가는건 action객체라고 부름, dispatch로 action을 실행, action을 해석해서 수정해주는것이 리듀서
  - state는 직접 수정할 수 없음, state를 수정하려면 action을 만들고 그 action을 dispatch해서 state를 바꿈
  - action을 어떻게 처리할지는 reducer에서 관리함
  - action의 이름은 대문자로 처리하는게 국룰! 상수로 빼서 사용하자

- Context API

  - Provider로 묶어주어야 그 아래 컴포넌트에서 데이터에 접근가능
  - 자식에게 전달해줄 데이터는 value
  - 성능 최적화 하기가 힘듬
  - <TableContext.Provider value={{ tableData: state.tableData, dispatch }}> 이런식으로 사용하면
  - 렌더링시마다 새로운 객체가 생김
  - useMemo를 사용하자

- useLayoutEffect

  - 화면을 그리기 전에 실행
  - useEffect보다 실행순서가 빨라서 state업데이트시 화면 깜빡임이 발생할때 useLayoutEffect를 가끔 사용해도 좋다.

- useTransition

  - startTransition, 업데이트를 바로 하지 않아도 괜찮은 것들을 넣음
  - loading, 로딩시 무엇인가 표시하고 싶다면

- useDeferredValue
  - useMemo에서 주로 사용
  - 업데이트가 늦게 돼도 되는

