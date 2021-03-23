# NLP-Twitter

### 功能说明
给出id/username，获取推文

### 过程

* 进入指定用户主页
* 爬取followers数量
* 爬取所有推文
* 保存文件

### Twint

**Twint是一个用Python写的Twitter抓取工具，允许从Twitter配置文件中抓取推文，不使用Twitter的API。**

使用Twint的一些好处：

> 1.可以获取几乎**所有的**推文（Twitter API限制只能持续3200个推文）;
>
> 2.快速初始设置; 
>
> 3.可以匿名使用，无需Twitter注册; 
>
> 4.**没有速率限制**。



### BUG

* 需要openpyxl
* 使用webdriver之前需要关闭chrome，防止user_data被占用
* class标签