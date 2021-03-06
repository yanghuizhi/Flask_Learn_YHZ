# Flask 上下文
相当于一个容器，保存了Flask程序运行过程中的一些信息。上下文可以实现 `信息共享` 和 `信息隔离`

Flask中有两种上下文，`请求上下文`和`应用上下文`。

[请求上下文](#请求上下文(request context))<br/>
[应用上下文](#应用上下文(application context))<br/>
[请求钩子](#请求钩子)<br/>
[Flask装饰器路由的实现](#Flask装饰器路由的实现)<br/>






## 请求上下文(request context)
会存储一个从外部发起的请求的所有信息, request和session都属于请求上下文对象。

request：封装了HTTP请求的内容，针对的是http请求。举例：user = request.args.get('user')，获取的是get请求的参数。

session：用来记录请求会话中的信息，针对的是用户信息。举例：session['name'] = user.id，可以记录用户信息。还可以通过session.get('name')获取用户信息。





## 应用上下文(application context)
会存储一个 app 里可以全局共享里的变量, current_app和g都属于应用上下文对象。

current_app:表示当前运行程序文件的程序实例。我们可以通过current_app.name打印出当前应用程序实例的名字。

g:处理请求时，用于临时存储的对象，每次请求都会重设这个变量。比如：我们可以获取一些临时请求的用户信息。

- 当调用app = Flask(_name_)的时候，创建了程序应用对象app；
- request 在每次http请求发生时，WSGI server调用Flask.call()；然后在Flask内部创建的request对象；
- app的生命周期大于request和g，一个app存活期间，可能发生多次http请求，所以就会有多个request和g。
- 最终传入视图函数，通过return、redirect或render_template生成response对象，返回给客户端。

区别： 请求上下文：保存了客户端和服务器交互的数据。 应用上下文：在flask程序运行过程中，保存的一些配置信息，比如程序文件名、数据库的连接、用户信息等。









## 请求钩子

在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：在请求开始时，建立数据库连接；在请求结束时，指定数据的交互格式。为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。

请求钩子是通过装饰器的形式实现，Flask支持如下四种请求钩子：

- before_first_request：在处理第一个请求前运行。

- before_request：在每次请求前运行（`before_app_request`）。

- after_request：如果没有未处理的异常抛出，在每次请求后运行。

- teardown_request：在每次请求后运行，即使有未处理的异常抛出。

- teardown_appcontext：不管是否有异常，注册的函数都会在每次请求之后执行。

- template_filter：在使用Jinja2模板的时候自定义过滤器。比如可以增加一个upper的过滤器（当然Jinja2已经存在这个过滤器）：

- context_processor：上下文处理器。返回的字典中的键可以在模板上下文中使用。例如：

- errorhandler：errorhandler接收状态码，可以自定义返回这种状态码的响应的处理方法.












## Flask装饰器路由的实现

Flask有两大核心：Werkzeug和Jinja2。Werkzeug实现路由、调试和Web服务器网关接口。Jinja2实现了模板。

Werkzeug是一个遵循WSGI协议的python函数库。其内部实现了很多Web框架底层的东西，比如request和response对象；与WSGI规范的兼容；支持Unicode；支持基本的会话管理和签名Cookie；集成URL请求路由、实现密码哈希等。

Werkzeug库的routing模块负责实现URL解析。不同的URL对应不同的视图函数，routing模块会对请求信息的URL进行解析，匹配到URL对应的视图函数，以此生成一个响应信息。

routing模块内部有Rule类（用来构造不同的URL模式的对象）、Map类（存储所有的URL规则）、MapAdapter类（负责具体URL匹配的工作）；


### 密码转哈希值
作为一个附加手段，多次哈希相同的密码，你将得到不同的结果，所以这使得无法通过查看它们的哈希值来确定两个用户是否具有相同的密码。
```
# 密码加密 

>>> from werkzeug.security import generate_password_hash
>>> hash = generate_password_hash('yhz')
>>> hash
'pbkdf2:sha256:50000$s6UtL3KL$8c51fad662ec0e3d421a2c6625d646a5effce9bf0054116bfc8d7872f709447d'


# 密码解密

>>> from werkzeug.security import check_password_hash
>>> check_password_hash(hash, 'yhz')
True
>>> check_password_hash(hash, 'Yhz')
False
```