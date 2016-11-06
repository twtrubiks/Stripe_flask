# Stripe_flask
Stripe Use Python Flask 
* [Demo]()  
 
相信大家都和我一樣覺得線上付款很酷!!

使用Python [Flask](http://flask.pocoo.org/) 搭配 [Stripe](https://stripe.com/) 網路線上付款，希望這個簡單的範例可以幫助想要學習的朋友。

## 特色
* 透過 [Stripe](https://stripe.com/) 網路線上付款 。
* 更多的文件可以參考 [Stripe Document](https://stripe.com/docs)

## 執行說明
請先確定電腦有安裝 [Python](https://www.python.org/)

使用下列指令安裝套件
``` 
pip install stripe
```

接著使用下列指令即可運行
``` 
python app.py
```

請去 [Stripe](https://stripe.com/) 註冊一組帳號，註冊完畢之後，

請到 [HERE](https://dashboard.stripe.com/account/apikeys)，去找你自己的測試KEY，如下圖，

![alt tag](http://i.imgur.com/2yeZJYw.jpg)

將自己的KEY貼到程式碼裡 

``` 
stripe_keys = {
    'secret_key': 'sk_test_fPHKYTWdK5ZhuxQ3me9TOndf',
    'publishable_key': 'pk_test_EUm15FduMZOImjeIy7dsKjdE'
}
```

P.S KEY請換自己的!!

## 執行畫面
![alt tag](http://i.imgur.com/FdI9wZf.jpg)

使用方法 : 點選 <b> Pay with Card </b> 會看到下圖

![alt tag](http://i.imgur.com/IgfOkm7.jpg)

接著輸入測試資料 (如下圖) <br>
![alt tag](http://i.imgur.com/eu3MNfG.jpg)

成功畫面如下<br>
![alt tag](http://i.imgur.com/UsdoYDO.jpg)

下方為顯示付款過的紀錄
![alt tag](http://i.imgur.com/eVYn23b.jpg)

也可以到 [Dashboard](https://dashboard.stripe.com/test/dashboard) 看付款過的紀錄



## 執行環境
* Python 3.5.2

## License
MIT license
