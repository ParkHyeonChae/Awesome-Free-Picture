# Awesome Free Picture

#### Python Flask 기반으로 [Pixabay](https://pixabay.com/ko/), [Iconmonstr](https://iconmonstr.com) 사이트 크롤링 웹 만들기
---
### 1. Main
![main](https://user-images.githubusercontent.com/52586888/64865343-07fbbe80-d674-11e9-9fed-e75e41039f8c.PNG)
메인템플릿 - [HTML5UP](https://html5up.net/eventually)

bg IMG - [Unsplash](https://unsplash.com/developers) 제공 API 사용 ``` https://source.unsplash.com/1920x1200/?background ``` 지속적으로 랜덤배경 변환

---
### 2. Imglist
![list](https://user-images.githubusercontent.com/52586888/64865344-092ceb80-d674-11e9-8338-4d5964401ec8.PNG)
템플릿 - [Bootstrap](https://bootswatch.com/sandstone/)

BeautifulSoup로 픽사베이의 페이지 별 src, data-lazy 속성 값 추출 후 3x3으로 출력, 내부적으로 페이징 구현

![lightbox](https://user-images.githubusercontent.com/52586888/64865348-0a5e1880-d674-11e9-8748-e3d63b5936f9.PNG)
``` Jquery lightbox-plus-jquery.min ``` 사용

``` img.find('a').find('img')['src'][:-8]+'1280.jpg ``` 1280x 로 크기 강제 조정 후 append. (Pixabay만 가능)

---
### 3. Iconlist
![iconlist](https://user-images.githubusercontent.com/52586888/64865352-0b8f4580-d674-11e9-8abb-d33649948d70.PNG)
[Iconmonstr](https://iconmonstr.com) 크롤링.

[Flaticon](https://www.flaticon.com) 사이트를 크롤링 해오고 싶었지만, 상업성 이용에 제한, 라이센스 표기 제한이 존재.

---
### 4. Videolist
![videolist](https://user-images.githubusercontent.com/52586888/64865354-0cc07280-d674-11e9-9fe9-9d27bcf3ee42.PNG)
픽사베이 동영상 크롤링.

---
## Review
대학교 프리캡스톤 기능 구현 중 하나로 시작했지만 욕심이 나서 프론트 공부 겸 웹으로 제작.

원래는 Unsplash 사이트 베이스로 구현하고 싶었지만 사이트 서버구조가 HELL.... 따로 API 제공하기는 하지만 제약이 많다. (시간당 요청 제한)

현재 우클릭으로 로컬에 다운은 가능하지만 후에 ajax와 javascript 공부 더 하고 모달창 내에 다운로드 버튼 구현, 회원db 추가한 다음 my image 폴더 개별 생성 후 선택된 이미지 서버상에 저장, 다운 구현이 목표.

저장된 이미지 횟수별, 인기순 등으로 정렬기능도 추가해야겠다.

이게 1000장 이상으로 긁어오면 로딩이 아주 조금 걸리는데 개선할 방법찾아봐야함. (지금은 300장만)
