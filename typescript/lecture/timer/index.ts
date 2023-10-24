let root_setting = document.querySelector(
  ".root_setting"
) as HTMLParagraphElement;
let minute = document.querySelector(".minute") as HTMLParagraphElement;
let second = document.querySelector(".second") as HTMLParagraphElement;
let start_button = document.querySelector(
  ".start_button"
) as HTMLParagraphElement;
let study_button = document.querySelector(
  ".study_button"
) as HTMLParagraphElement;
let break_button = document.querySelector(
  ".break_button"
) as HTMLParagraphElement;
let flag: boolean = true;
let timer_flag: boolean = true;
let interval: number;
let default_minute: string = "25";
let default_minute_break: string = "5";
let default_second: string = "00";
let default_second_break: string = "00";
let count: number;
let break_count: number;
let break_flag: boolean = false;
break_count = parseInt(localStorage.getItem("break_count") as string);
count = parseInt(localStorage.getItem("count") as string);
let switch_button: boolean = true;

if (count) {
  root_setting.innerText = `# ${count} study!!`;
} else {
  count = 1;
  localStorage.setItem("count", count.toString());
  root_setting.innerText = `# ${count} study!!`;
}

if (!break_count) {
  break_count = 1;
  localStorage.setItem("break_count", break_count.toString());
}

// event
// 시작 버튼 클릭
start_button.addEventListener("click", () => {
  if (flag) {
    start_button.innerText = "Pause";
    interval = setInterval(() => {
      if (
        parseInt(second.innerText) === 0 &&
        parseInt(minute.innerText) === 0
      ) {
        if (!break_flag) {
          count += 1;
          localStorage.setItem("count", count.toString());
          root_setting.innerText = `# ${break_count} break~~`;
          if (default_minute_break.length < 2) {
            default_minute_break = `0${default_minute_break}`;
          }
          if (default_second_break.length < 2) {
            default_second_break = `0${default_second_break}`;
          }
          second.innerText = default_second_break;
          minute.innerText = default_minute_break;
          start_button.innerText = "Start";
          break_flag = true;
        } else {
          break_count += 1;
          localStorage.setItem("break_count", break_count.toString());
          root_setting.innerText = `# ${count} study!!`;
          if (default_minute.length < 2) {
            default_minute = `0${default_minute}`;
          }
          if (default_second.length < 2) {
            default_second = `0${default_second}`;
          }
          second.innerText = default_second;
          minute.innerText = default_minute;
          start_button.innerText = "Start";
          break_flag = false;
        }
        clearInterval(interval);
        flag = true;
        // if (default_minute.length < 2) {
        //   default_minute = `0${default_minute}`;
        // }
        // if (default_second.length < 2) {
        //   default_second = `0${default_second}`;
        // }
        // minute.innerText = default_minute;
        // second.innerText = default_second;
      } else if (parseInt(second.innerText) === 0) {
        let tmp: string = (parseInt(minute.innerText) - 1).toString();
        if (tmp.length < 2) {
          minute.innerText = "0" + tmp;
        } else {
          minute.innerText = tmp;
        }
        second.innerText = "59";
      } else {
        let tmp: string = (parseInt(second.innerText) - 1).toString();
        if (tmp.length < 2) {
          second.innerText = `0${tmp}`;
        } else {
          second.innerText = tmp;
        }
      }
    }, 1000);
    flag = false;
  } else {
    start_button.innerText = "Start";
    clearInterval(interval);
    flag = true;
  }
});

// 시간 세팅
minute.addEventListener("click", () => {
  if (flag) {
    let setting_value = prompt("분 입력");
    if (setting_value) {
      if (setting_value.length < 2) {
        setting_value = `0${setting_value}`;
      }
      if (break_flag) {
        default_minute_break = setting_value;
      } else {
        default_minute = setting_value;
      }
      minute.innerText = setting_value;
    }
  }
});

second.addEventListener("click", () => {
  if (flag) {
    let setting_value = prompt("초 입력");
    if (setting_value) {
      if (setting_value.length < 2) {
        setting_value = `0${setting_value}`;
      }
      if (break_flag) {
        default_second_break = setting_value;
      } else {
        default_second = setting_value;
      }
      second.innerText = setting_value;
    }
  }
});

// study button 디폴트 세팅
study_button.addEventListener("click", () => {
  break_flag = false;
  if (default_minute.length < 2) {
    default_minute = `0${default_minute}`;
  }
  if (default_second.length < 2) {
    default_second = `0${default_second}`;
  }
  minute.innerText = default_minute;
  second.innerText = default_second;
  root_setting.innerText = `#${count} study!!`;
});

break_button.addEventListener("click", () => {
  break_flag = true;
  if (default_minute_break.length < 2) {
    default_minute_break = `0${default_minute_break}`;
  }
  if (default_second_break.length < 2) {
    default_second_break = `0${default_second_break}`;
  }
  minute.innerText = default_minute_break;
  second.innerText = default_second_break;
  root_setting.innerText = `#${break_count} break~~`;
});
