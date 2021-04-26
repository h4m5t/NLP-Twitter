<h1 align="center">Welcome to NLP-Twitter 👋</h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> Twitter_spider for China.

### 🏠 [Homepage](https://github.com/h4m5t/NLP-Twitter)

## Author

👤 **h4m5t**

* Website: www.h4m5t.top
* Github: [@h4m5t](https://github.com/h4m5t)



## About The Project

Introduce some ways to crawl Tweets for China Students so that they can do Scientific research or course projects.

已经实现以及未实现的功能：

> :white_check_mark:模拟浏览器操作，爬取用户信息 
>
> :white_check_mark:模拟浏览器操作，爬取推文 
>
> :white_check_mark:根据用户ID生成URL​
>
> :x: 数据读入和输出保存（CSV型、SQL型）
>
> :x: 多线程爬取



## 爬取推特方法

* **1. 借助第三方爬推特库**

  * https://github.com/twintproject/twint

  * https://github.com/bisguzar/twitter-scraper

  * https://github.com/jonbakerfish/TweetScraper

    但都会报错：

    > WARNING:root:Error retrieving https://twitter.com/: Timeout(ConnectTimeoutError(<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 
    > 0x0000023F9CCDFF10>, 'Connection to twitter.com timed out. (connect timeout=10)')), retrying

    解决方法：

    * 使用VPN（ExpressVPN\NordVPN）（缺点：比较贵）

      基于sock的一系列翻墙软件，比如SR、SSR、v2ray等，在使用twint时会出现这个错误。这是因为sock工作在TCP/IP五层网络模型的第五层的应用层和第四层的传输层之间，层级太高，有时候如果网络连接走的层级比较低就会出错。可以试一下VPN，它工作在第三层的网络层,使用twint的时候用的ExpressVPN，就没有出现问题。还有需要提醒一点的是不要把SSR和VPN弄混了，虽然都能翻墙，但是原理不一样的。所以就会出现你用SSR能翻墙上网，但是有时候在一些场景又会出错，其实就是sock的工作原理的限制。

      参考链接：

      https://github.com/twintproject/twint/issues/834

      https://github.com/twintproject/twint/issues/442

      https://github.com/twintproject/twint/pull/1146

    * 对本机设置全局代理（已尝试，不太可行）

    * 在IDE设置代理（已尝试，不太可行）

    * 设置twint的config(已尝试，不太可行)
    
      `config=twint.Config()`
    
      `config.Proxy_host = '127.0.0.1'`
    
      `config.Proxy_port = 7890`
    
      `config.Proxy_type = "socks5"`
    
    * 把脚本放在国外VPS上（可行）
    
      * digitalocean
    
      * vultr
    
      * hostwinds
    
      * Linode
    
      * 搬瓦工

* **2.使用Twitter-developer-API**

  > The Twitter APl enables programmatic access toTwitter in unique and advanced ways.Use it to analyze, learn from, and interact with Tweets,Direct Messages, users, and other key Twitter resources.

  https://developer.twitter.com/en/docs/twitter-api

* **3.借助第三方爬虫库**

  * Scrapy
  * requests
  * urllib
  * BeautifulSoup
  
* **4.借助数据采集器**

  * [octopus采集器](https://octopus.com/)
  * [八爪鱼采集器](https://www.bazhuayu.com/)
  * [后裔采集器](http://www.houyicaiji.com/)

* **5.selenium模拟浏览器操作**

  注意：

  * 安装[chromedriver](https://chromedriver.chromium.org/downloads)

    打开chrome,地址栏输入chrome://version 查看浏览器版本，安装对应版本的chromedriver

  * 控制下拉、翻页等操作，要设置相应的延迟

  * 推特对不同IP有不同的限制策略，有些地区需要登陆才可看见推文，有些不用。

  * 如果需要导入浏览器数据，使用webdriver之前需要关闭chrome，防止user_data被占用



## **requirement**

* requests
* selenium
* twint
* csv
* time
* datetime
* urllib



## 仓库说明

1. generate_url.py  根据用户ID生成对应的url,保存在url.txt

2. test*.py  用来测试相关爬虫库、代理设置、模拟浏览器操作

3. Twitter.csv  为100个涉华人员的相关信息

4. user_info.py  爬取关注者被关注者数量

5. user_tweets.py  爬取对应用户的推文



## 推特过滤规则

### Building standard queries

The best way to build a standard query and test if it’s valid and will return matched Tweets is to first try it at [twitter.com/search](https://twitter.com/search). As you get a satisfactory result set, the URL loaded in the browser will contain the proper query syntax that can be reused in the standard search API endpoint. Here’s an example:

1. We want to search for Tweets referencing @TwitterDev account. First, we run the search on [twitter.com/search](https://twitter.com/search)
2. Check and copy the URL loaded. In this case, we got: https://twitter.com/search?q=%40twitterdev
3. Replace https://twitter.com/search with https://api.twitter.com/1.1/search/tweets.json and you will get: https://api.twitter.com/1.1/search/tweets.json?q=%40twitterdev
4. Run a Twurl command to execute the search.

Please note that the API requires that the request be authenticated (check [Authentication & Authorization](https://developer.twitter.com/en/docs/basics/authentication/overview/authentication-and-authorization.html) documentation for more details on this). Note that the standard search API only serves data from the last week. If you need historical data odler than seven days, check out the [premium](https://developer.twitter.com/en/docs/tweets/search/overview/premium) and [enterprise](https://developer.twitter.com/en/docs/tweets/search/overview/enterprise) search APIs.

### Standard search operators

| **Operator**                      | Finds Tweets...                                              |
| :-------------------------------- | ------------------------------------------------------------ |
| watching now                      | containing both “watching” and “now”. This is the default operator. |
| “happy hour”                      | containing the exact phrase “happy hour”.                    |
| love OR hate                      | containing either “love” or “hate” (or both).                |
| beer -root                        | containing “beer” but not “root”.                            |
| #haiku                            | containing the hashtag “haiku”.                              |
| from:interior                     | sent from Twitter account “interior”.                        |
| list:NASA/astronauts-in-space-now | sent from a Twitter account in the NASA list astronauts-in-space-now |
| to:NASA                           | a Tweet authored in reply to Twitter account “NASA”.         |
| @NASA                             | mentioning Twitter account “NASA”.                           |
| politics filter:safe              | containing “politics” with Tweets marked as potentially sensitive removed. |
| puppy filter:media                | containing “puppy” and an image or video.                    |
| puppy -filter:retweets            | containing “puppy”, filtering out retweets                   |
| puppy filter:native_video         | containing “puppy” and an uploaded video, Amplify video, Periscope, or Vine. |
| puppy filter:periscope            | containing “puppy” and a Periscope video URL.                |
| puppy filter:vine                 | containing “puppy” and a Vine.                               |
| puppy filter:images               | containing “puppy” and links identified as photos, including third parties such as Instagram. |
| puppy filter:twimg                | containing “puppy” and a pic.twitter.com link representing one or more photos. |
| hilarious filter:links            | containing “hilarious” and linking to URL.                   |
| puppy url:amazon                  | containing “puppy” and a URL with the word “amazon” anywhere within it. |
| superhero since:2015-12-21        | containing “superhero” and sent since date “2015-12-21” (year-month-day). |
| puppy until:2015-12-21            | containing “puppy” and sent before the date “2015-12-21”.    |
| movie -scary :)                   | containing “movie”, but not “scary”, and with a positive attitude. |
| flight :(                         | containing “flight” and with a negative attitude.            |
| traffic ?                         | containing “traffic” and asking a question.                  |

注意：需要使用URL encode（可使用在线网站进行转换）

请参考：

* https://en.wikipedia.org/wiki/Percent-encoding
* https://www.w3schools.com/tags/ref_urlencode.ASP
* https://tool.chinaz.com/tools/urlencode.aspx
* https://meyerweb.com/eric/tools/dencoder/



## 参考资料

https://github.com/xs71/TwitterSpider

https://github.com/ALL-AC/tweet-analysis

https://github.com/ZekangZhouKGR/twitter_bot

https://github.com/ChangxingJiang/CxSpider

https://www.4008140202.com/pp/20191117124856_4774_3977640913/news

[如何从推特挖掘情报：一个流行工具的具体介绍 - iyouport (@iyouport)](https://matters.news/@iyouport/如何从推特挖掘情报-1-一个流行工具的具体介绍-bafyreidw6w2aee3i42o6y4jypw2vtfzxg5qpmhorltge5uxj3xkzh255zq)

[CxSpider/Twitter_Account_Post.py at master · ChangxingJiang/CxSpider](https://github.com/ChangxingJiang/CxSpider)

[Docker —— 从入门到实践](https://yeasy.gitbook.io/docker_practice/)

[python selenium设置chrome浏览器保持登录方式_小王子博客-CSDN博客_selenium 保持登录](https://blog.csdn.net/weixin_43407092/article/details/97128833)

[selenium保留chrome配置及登陆 - 简书](https://www.jianshu.com/p/fc36a7e9aca8)

[selenium设置chrome浏览器保持登录方式两种options和cookie - 豌豆ip代理](https://www.wandouip.com/t5i225026/)

[python - InvalidArgumentException: Message: invalid argument: user data directory is already in use error using --user-data-dir to start Chrome using Selenium - Stack Overflow](https://stackoverflow.com/questions/59987080/invalidargumentexception-message-invalid-argument-user-data-directory-is-alre)

[User Data Directory Is Already In Use - Katalon Studio / Web Testing - Katalon Community](https://forum.katalon.com/t/user-data-directory-is-already-in-use/40266/2)

[CRITICAL:root:twint.run:Twint:Feed:noDataExpecting value: line 1 column 1 (char 0) · Issue #915 · twintproject/twint](https://github.com/twintproject/twint/issues/915)

[Essie0715/Twitter_Data_Collection: Twitter爬虫学习](https://github.com/Essie0715/Twitter_Data_Collection)

[masonsxu/Selenium_Crawler: 一个使用selenium模块爬取（Twitter、New York Times）网站的可配置爬虫代码](https://github.com/masonsxu/Selenium_Crawler)



## Show your support

Give a ⭐️ if this project helped you!

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_