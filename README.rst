<<<<<<< HEAD
<수정사항>

-플레이어 정지
게임 플레이 중 s키를 눌러 우주선을 정지시키는 기능 추가했습니다.
(gameplay.py/input.py/objship.py)

-게임중 라운드 표시
제 버전에선 한글패치가 안된 버전이라 우선 Stage1,2,3 등으로 출력되게 했습니다.
또 stage0은 출력된 후 사라지지 않아서 0은 뜨지않도록 했습니다.
(score.py)

-게임 진행도 표시
바 형태로 게임 진행도를 표시하게 했습니다.
(hud.py)

=======
>>>>>>> bf8521a5af4ffe589903bbe11c20d1be3410706c
-한글 패치
메뉴 png를 새로 만들어서 한글로 바꾸고 한글로 바꾸면서 폰트가 너무 커지는 바람에 폰트 조절을 했습니다.
그리고 첫 화면에 나오는 우주선?이 너무 커서 메뉴 글자가 잘 안보여서 크기를 줄였습니다.
(menu_creds_on.png, menu_news_on.png, menu_quit_on.png, menu_setup_on.png, menu_start_on.png,/ ..._off.png/ ship-big.png) -> 새로 만든 png
(gamemenu.py/ gamepref.py/ gamestart.py/ gamewin.py/ txt.py/ gamecreds.py/ gamenews.py/ score.py) -> 한글 번역, 한글 폰트 크기 수정
(NanumGothic-Bold.ttf) -> 한글 폰트 추가
<<<<<<< HEAD
 
=======
>>>>>>> bf8521a5af4ffe589903bbe11c20d1be3410706c
