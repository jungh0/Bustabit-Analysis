# Bustabit 그래프 게임 결과 예측 분석 <br>(Tensorflow 딥러닝 학습, Hash 함수)

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

(예측1)이 맞을 경우 그 알고리즘만 찾아낸다면 게임 결과를 알 수 있고 딥러닝을 통해 그 알고리즘을 찾아낼 수 있을것이다.

## .NET C#을 이용한 게임 데이터 수집
먼저 http 요청을 통해 게임 결과 데이터를 수집하였다.<br>
하지만 http response 부분에는 데이터가 없었고 자바스크립트만이 존재했다.<br>
그 자바스크립트는 해석이 불가하였다.<br>
결국 결과 자체의 화면과 소스를 이용할 수 있는 .NET의 WebBrowser을 이용하기로 했다.
### http Web Debugging
![image](https://user-images.githubusercontent.com/8678595/70587129-7537d500-1c0c-11ea-810d-9027e73d6b0f.png)
### Response 데이터 
```html
<html lang="en">
<!--header 생략-->
<body class="theme-dark">
    <div id="root"></div>
    <noscript>
        <!--style 생략-->
        <div id="container">
            <div id="header">
                <img id="logo" src="/ms-icon-310x310.png" alt="bustabit logo">
                <h1 id="brand">bustabit</h1>
            </div>
            <p id="warning">
                It looks like JavaScript is disabled or not supported by your browser. In order for bustabit to work JavaScript must be enabled!
            </p>
        </div>
    </noscript>
<script type="text/javascript" src="/static/e51deb3e08be42c5d678.js"></script></body>
</html>
```

하지만 Internet Explorer에서는 접속을 할 수 없기에 WebBrowser 사용이 불가하였다.<br>
결국 CefSharp ChromiumWebBrowser을 사용하여 크롬 제어 환경을 만들었다.<br>
각 피처는 게임번호, 게임 결과 배수, 총 배팅 금액, 이용자의 총 수익으로 정하였다.
<pre><a href="https://www.codeproject.com/Tips/1058700/Embedding-Chrome-in-your-Csharp-App-using-CefSharp">https://www.codeproject.com/Tips/1058700/Embedding-Chrome-in-your-Csharp-App-using-CefSharp</a></pre>
<img src='https://user-images.githubusercontent.com/8678595/70589167-62280380-1c12-11ea-8de5-52fc7cd03c4d.gif' width='400px'/>

15,797개의 게임 데이터 csv 파일 
<pre><a href="https://github.com/jungh0/Busted/blob/master/Files/2537203-2553000.csv">https://github.com/jungh0/Busted/blob/master/Files/2537203-2553000.csv</a></pre>

## Tensorflow를 이용한 데이터 학습

### Data Preprocessing
우리가 예측해야할것은 게임 결과의 배수이고 그 게임의 총 배팅 금액, 이용자의 총 수익은 알지 못한다.<br>
즉 우리가 알고있고 학습시켜야할 데이터는 과거의 게임 결과이다.<br>
결론적으로 선택한 최종 피처는 1,2,3,4,5,6,7,8,9,10 이전의 게임의 배수의 합과 100,50,10,5,3의 게임 이득의 합이다.<br>
input은 15개가 될것이고 output은 게임 결과의 배수로 1개가 될것이다.<br>

### Data Analysis
