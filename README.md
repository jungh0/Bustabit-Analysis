# Bustabit 결과 예측 분석 (Tensorflow 딥러닝 학습, Hash 함수)

## 개요
페이스북이나 기타 SNS을 통해 그래프 게임이라는 불법도박 사이트의 존재을 알고있을것이다.<br>
모든 도박 사이트는 당연히 개발자가 무조건 수익을 얻는 구조로 되어있고, 사용자는 결국 돈을 잃게 될것이다.<br>
Bustabit은 Hash 함수를 이용하여 절대 개발자가 미래 게임 결과를 조작할 수 없고 모든 게임은 이미 정해져 있다 하였다.<br>
개발자는 자신있게 소스를 공개하였고 질문도 남길수 있게 하였다.
<pre><a href="https://bitcointalk.org/index.php?topic=2807542.0">https://bitcointalk.org/index.php?topic=2807542.0</a></pre>
분명 어떠한 트릭이 있을거라 생각했다.<br>
완전한 랜덤이라면 특정경우에는 분명 개발자가 돈을 잃을수도 있는 상황인것이다.<br>
그리하여 두가지 예측을 해보았다.
- (예측1) 개발자는 게임 결과를 조작하고 있고 어떠한 알고리즘의 의해 유지되고 있다.<br>
특정 상황(많은 금액의 베팅)에서는 무조건 이용자의 돈을 잃게 한다던지<br>
특정 상황(개발자의 수익이 일정량 이상이 되었을때)에서는 이용자의 게임 승률을 높인다.<br>
- (예측2) 정말 랜덤하게 짜여진 공평한 게임이다.<br>

(예측1)이 맞을 경우 그 알고리즘만 찾아낸다면 게임 결과를 알 수 있고 딥러닝을 통해 학습이 가능할 것이다.

## .NET C#을 이용한 게임 데이터 수집
아래 사진과 같이 일반적인 http 요청으로는 웹데이터를 수정할 수 없었기에<br>
결과 자체의 화면과 소스를 이용할 수 있는 .NET의 WebBrowser을 이용하기로 했다.

하지만 Internet Explorer에서는 접속을 할 수 없기에 WebBrowser 사용이 불가하였다.<br>
결국 CefSharp ChromiumWebBrowser을 사용하여 크롬 제어 환경을 만들었다.
<pre><a href="https://www.codeproject.com/Tips/1058700/Embedding-Chrome-in-your-Csharp-App-using-CefSharp">https://www.codeproject.com/Tips/1058700/Embedding-Chrome-in-your-Csharp-App-using-CefSharp</a></pre>

15,797개의 게임 데이터 csv 파일 
<pre><a href="https://github.com/jungh0/Busted/blob/master/Files/2537203-2553000.csv">https://github.com/jungh0/Busted/blob/master/Files/2537203-2553000.csv</a></pre>
