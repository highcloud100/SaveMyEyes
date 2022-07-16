# SaveMyEyes
---
- 눈이 너무 아파 쉴 시간을 알려주는 프로그램
  - 공부하다 공부도 안되고 눈과 목과 머리가 아퍼서 만듬
  - pyqt5 이용함

## 실행시
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/80192345/179270618-e4e0a915-bc6e-4bed-b026-51a3fa69203f.png">

- 화면 좌측에 바가 생성됨
- 시간은 1시간 기준 <- 추후 조절 가능하게 만들것
- 버튼 두개 있음
  - 하나는 끄는 버튼
  - 하나는 멈추는 버튼
  
  
## 1시간이 지나면
<img width="1920" alt="image" src="https://user-images.githubusercontent.com/80192345/179270843-fd4d1a19-61a3-44a3-9e15-d8c5d8231c2b.png">

- 쉬라고 알려줌
  - 쉬면 됨
  
 
 ## 개선할 것들 - 일단 1주일간 사용해보겠음 20220716
 
 - 여러 화면 환경 테스트
  - 지금은 임의로 모니터에 맞추어둠 <- 높이가 다른 환경에서 살짝 안맞을 것 같다. 
 - 시간 조정 기능
 - 압도적인 소리 기능
 - 이미지 랜덤화 
 
 # 실행파일 만드는 법
 ---
 - 다운 받은 폴더에서 다음 명령어를 실행
 
 ```shell
  pyinstaller -w -F myeye.py
 
 ```
 
 - dist 폴더 안에 img 폴더와 ui 파일을 욺겨준다. 
 - 이후 exe 실행
