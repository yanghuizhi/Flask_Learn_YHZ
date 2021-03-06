# Welcome to Flask_Learn!
目录：<br/>
[Flask](#flask) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 基本定义 <br/>
[Python-dotenv](#python-dotenv) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 环境变量配置 <br/>
[Flask-SQLalchemy](#flask-sqlalchemy) &nbsp; &nbsp;操作数据库 <br/>
[Flask-migrate](#flask-migrate) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 管理迁移数据库 <br/>
[Flask-login](#flask-login) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 认证用户状态 <br/>
[Flask-Mail](#flask-mail) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 邮件服务 <br/>
[Flask-pyjwt](#flask-pyjwt) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 安全令牌 <br/>
[Flask-Moment](#flask-moment) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 本地化日期和时间 <br/>
[Flask-Babel](#flask-babel) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 翻译插件 <br/>
[Flask-blueprint](#flask-blueprint) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 蓝图 <br/>
[Flask-script](#flask-script) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 插入脚本，暂无 <br/>
[Flask-RESTful](#) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 开发REST API的工具，暂无 <br/>
[Flask-Bootstrap](#flask-bootstrap) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 开发REST 集成前端Twitter Bootstrap框架，暂无 <br/> 
[Flask-guess_language](#guess_language)
&nbsp; &nbsp; &nbsp; 语言检测库







## Flask

- **`render_template()`** : 该函数需要传入模板文件名和模板参数的变量列表，并返回模板中所有占位符都用实际变量值替换后的字符串结果。内部逻辑为调用 `Flask` 框架原生依赖的Jinja2模板引擎。`Jinja2` 用 `render_template()` 函数传入的参数中的相应值替换 `{{...}}` 块。

- **`redirect()`** 函数 : 指引浏览器自动重定向到它的参数所关联的URL. 

- **`flash()`** 函数 : 闪现消息，且只显示一次，将函数内的信息返回给`get_flashed_messages()`函数，它返回用flash()注册过的消息列表。

  闪现消息的一个有趣的属性是，一旦通过`get_flashed_messages()`函数请求了一次，它们就会从消息列表中移除，所以在调用flash()函数后它们`只会出现一次`。
  
- **`@errorhandler`** 装饰器 : 声明一个自定义的错误处理器

- `request.args` Flask的对象，访问查询字符串中给出的参数







## Python-dotenv
 
创建 `Flask` 之后，命令行还需进行以下配置，程序才能运行。

    mac    ：`export FLASK_APP=Flask_Learn.py`
    Window ：`set FLASK_APP=Flask_Learn.py`

在终端会话中直接设置的环境变量不会永久生效，因此你不得不在每次新开终端时设定 `FLASK_APP`  环境变量，从 1.0 版本开始，`Flask` 允许你设置只会在运行 `Flask` 命令时自动注册生效的环境变量，要实现这点，你需要安装  `python-dotenv`：

    (venv) $ pip install python-dotenv

此时，在项目的根目录下新建一个名为 `.flaskenv`  的文件，其内容是：

    FLASK_APP=microblog.py
    
通过此项设置，FLASK_APP就可以自动加载了，如果你钟爱手动设定环境变量，那也不错，只是记得每次启动终端后要设定它。

- 手动设置的环境变量 > `.env` 中设置的环境变量 > `.flaskenv` 设置的环境变量
- `.env` 存储敏感信息的环境变量
- `.flaskenv` 存储公开环境变量


  
  
  
  
  
  
  
## Flask-SQLalchemy

`flask-sqlalchemy` 是数据库软件的[ORM](https://baike.baidu.com/item/%E5%AF%B9%E8%B1%A1%E5%85%B3%E7%B3%BB%E6%98%A0%E5%B0%84/311152?fromtitle=ORM&fromid=3583252&fr=aladdin) (ORM允许应用程序使用高级实体（如类，对象和方法）而不是表和SQL来管理数据库。 ORM的工作就是将高级操作转换成数据库命令)

SQLAlchemy不只是某一款数据库软件的ORM，而是支持包含MySQL、PostgreSQL和SQLite在内的很多数据库软件。简直是太强大了，你可以在开发的时候使用简单易用且无需另起服务的SQLite，需要部署应用到生产服务器上时，则选用更健壮的MySQL或PostgreSQL服务，并且不需要修改应用代码（译者注：只需修改应用配置）。

`flask_migrate` 数据库迁移引擎.
  
    `db.Model`: 它是Flask-SQLAlchemy中所有模型的基类,字段被创建为`db.Column`类的实例，它的可选参数中允许指示哪些字段是唯一的并且是可索引的，这对高效的数据检索十分重要

### 常用的SQLAlchemy查询过滤器
```
过滤器	说明
filter()	把过滤器添加到原查询上，返回一个新查询
filter_by()	把等值过滤器添加到原查询上，返回一个新查询
limit	使用指定的值限定原查询返回的结果
offset()	偏移原查询返回的结果，返回一个新查询
order_by()	根据指定条件对原查询结果进行排序，返回一个新查询
group_by()	根据指定条件对原查询结果进行分组，返回一个新查询
```

### 常用的SQLAlchemy查询执行器
```
方法	说明
all()	以列表形式返回查询的所有结果
first()	返回查询的第一个结果，如果未查到，返回None
first_or_404()	返回查询的第一个结果，如果未查到，返回404
get()	返回指定主键对应的行，如不存在，返回None
get_or_404()	返回指定主键对应的行，如不存在，返回404
count()	返回查询结果的数量
paginate()	返回一个Paginate对象，它包含指定范围内的结果
```

#### paginate( ) 方法详解：
user.followed_posts().paginate(1, 20, False).items

需要输入三个参数来调用它：

- 从1开始的页码
- 每页的数据量
- 错误处理布尔标记，如果是True，当请求范围超出已知范围时自动引发404错误。如果是False，则会返回一个空列表。

paginate方法返回一个Pagination的实例。其items属性是请求内容的数据列表。Pagination实例还有一些其他用途，我会在之后讨论。





## Flask-migrate

管理迁移数据库
```python
flask db init                # 创建迁移数据库，产生migrations的新目录
flask db migrate -m "..."    # 创建数据库迁移
flask db upgrade             # 将更改应用到数据库
flask db downgrade           # 回滚数据库迁移
```










## Flask-login
插件用来管理用户登录状态，以便用户可以登录到应用，然后用户在导航到该应用的其他页面时，就会“记得”该用户已经登录。

插件还提供了“记住我”的功能，允许用户在关闭浏览器窗口后再次访问应用时保持登录状态。

该方式需要在用户模型上实现某些属性和方法，因此只要将这些必需项添加到模型中，Flask-Login就没有其他依赖了，它就可以与基于任何数据库系统的用户模型一起工作。


    `@login.user_loader` 装饰器: 为用户   加载功能注册函数
    `@login_required`    装饰器: 拒绝匿名用户的访问以保护某个视图函数，不允许未经身份验证的用户访问。
    
    `RotatingFileHandler()` 方法可以切割和清理日志文件，以确保日志文件在应用运行很长时间时不会变得太大。
   

必须的四项如下，通过 `UserMixin` 继承后实现下列属性 : 

    is_authenticated: 一个用来表示用户是否通过登录认证的属性，用True和False表示。
    is_active: 如果用户账户是活跃的，那么这个属性是True，否则就是False（译者注：活跃用户的定义是该用户的登录状态是否通过用户名密码登录，通过“记住我”功能保持登录状态的用户是非活跃的）。
    is_anonymous: 常规用户的该属性是False，对特定的匿名用户是True。仅当用户未登录时的值是True。
    get_id(): 返回用户的唯一id的方法，返回值类型是字符串(Python 2下返回unicode字符串).

## Flask-mail 
邮件服务 
 
## Flask-pyjwt
安全令牌，即JSON Web Tokens
    
    import jwt
    >>> token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
    >>> token
    b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhIjoiYiJ9.dvOo58OBDHiuSHD4uW88nfJikhYAXc_sfUHq1mDi4G0'
    >>> jwt.decode(token, 'my-secret', algorithms=['HS256'])
    {'a': 'b'}
    
    {'a'：'b'}字典是要写入令牌的示例有效载荷。 
    为了使令牌安全，需要提供一个秘密密钥用于创建加密签名。
     在这个例子中，我使用了字符串'my-secret'，但是在应用中，我将使用配置中的SECRET_KEY。algorithm参数指定使用什么算法来生成令牌，而HS256是应用最广泛的算法。












## Flask-Moment

Moment.js是一个小型的JavaScript开源库，它将日期和时间转换成目前可以想象到的所有格式。 
 
与其他插件不同的是，Flask-Moment与moment.js一起工作，因此应用的所有模板都必须包含moment.js。为了确保该库始终可用，可将它添加到基础模板中，可以通过两种方式完成。 

最直接的方法是显式添加一个`<script>`标签来引入库，但Flask-Moment的`moment.include_moment()`函数可以更容易地实现它，它直接生成了一个`<script>`标签并在其中包含moment.js：

    {% block scripts %}
        {{ super() }}
        {{ moment.include_moment() }}
    {% endblock %}

我在这里添加的scripts块是Flask-Bootstrap基础模板暴露的另一个块，这是JavaScript引入的地方。该块与之前的块不同的地方在于它已经在基础模板中定义了一些内容了。我想要追加moment.js库的话，就**需要使用super()语句，才能继承基础模板中已有的内容，否则就是替换。**

### Moment.js

Moment.js为浏览器提供了一个moment类。 呈现时间戳的第一步是创建此类的对象，并以ISO 8601格式传递所需的时间戳。 这里是一个例子：

`t = moment('2017-09-28T21:45:23Z')`

如果你对日期和时间不熟悉ISO 8601标准格式，格式如下：`{{ year }}-{{ month }}-{{ day }}T{{ hour }}:{{ minute }}:{{ second }}{{ timezone }}`。 我已经决定我只使用UTC时区，因此最后一部分总是将会是Z，它表示ISO 8601标准中的UTC。

moment对象为不同的渲染选项提供了几种方法。 以下是一些最常见的几种：
```python
moment('2017-09-28T21:45:23Z').format('L')
"09/28/2017"
moment('2017-09-28T21:45:23Z').format('LL')
"September 28, 2017"
moment('2017-09-28T21:45:23Z').format('LLL')
"September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('LLLL')
"Thursday, September 28, 2017 2:45 PM"
moment('2017-09-28T21:45:23Z').format('dddd')
"Thursday"
moment('2017-09-28T21:45:23Z').fromNow()
"7 hours ago"
moment('2017-09-28T21:45:23Z').calendar()
"Today at 2:45 PM"
```

此示例创建了一个moment对象，该对象被初始化为2017年9月28日晚上9:45 UTC。 你可以看到，我上面尝试的所有选项都以UTC-7时区来呈现，因为这是我计算机上配置的时区。你可以在microblog上进行此操作，只要你引入了[moment.js](https://momentjs.com/)。或者你也可以在上面尝试。

请注意不同的方法是如何创建的不同的表示。 使用format()，你可以控制字符串的输出格式，类似于Python中的strftime函数。 fromNow()和calendar()方法很有趣，因为它们会根据当前时间显示时间戳，因此你可以获得诸如“一分钟前”或“两小时内”等输出。

如果你直接在JavaScript中运行，则上述调用将返回渲染后的时间戳字符串。 然后，你可以将此文本插入页面上的适当位置，不幸的是，这需要JavaScript与DOM配合使用。 Flask-Moment插件通过启用一个类似于JavaScript上的moment对象，大大简化了对moment.js的使用，并融合了所需的JavaScript逻辑，使渲染后的时间展示在页面上。

我们来看看出现在个人主页中的时间戳。 当前的user.html模板使用Python生成时间的字符串表示。 现在我可以使用Flask-Moment渲染此时间戳，如下所示：

app/templates/user.html: 使用moment.js渲染时间戳。

    {% if user.last_seen %}
        <p>Last seen on: {{ moment(user.last_seen).format('LLL') }}</p>
    {% endif %}
                
如你所见，Flask-Moment使用的语法类似于JavaScript库的语法，其中一个区别是，moment()的参数现在是Python的datetime对象，而不是ISO 8601字符串。 从模板发出的moment()调用也会自动生成所需的JavaScript代码，以将呈现的时间戳插入DOM的适当位置。

我可以利用Flask-Moment和moment.js的第二个地方是被主页和个人主页调用的*_post.html*子模板。 在该模板的当前版本中，每条用户动态都以“用户名说：”行开头。 现在我可以添加一个用fromNow()渲染的时间戳：

app/templates/_post.html: 在用户动态子模板中渲染时间戳。

     <a href="{{ url_for('user', username=post.author.username) }}">
        {{ post.author.username }}
    </a>
    said {{ moment(post.timestamp).fromNow() }}:
    <br>
    {{ post.body }}
  



   
   
   
   
   
   
   
   
             
# Flask-Babel

### 翻译
```
# 查看本机支持的语言
pybabel --list-locales
# 生成语言目录，中文，生成对应po文件
pybabel init -i messages.pot -d app/translations -l zh
# 更新翻译：提取文本，生成pot模版，并更新生成po文件
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
# 编译po文件，生成mo文件，mo文件是加载翻译文件
pybabel compile -d app/translations


# 简化版
flask translate update
flask translate compile
```


用于简化翻译工作, 支持多语言的常规流程是在源代码中标记所有需要翻译的文本。 文本标记后，Flask-Babel将扫描所有文件，并使用gettext工具将这些文本提取到单独的翻译文件中。 不幸的是，这是一个繁琐的任务，并且是启用翻译的必要条件。

为翻译而标记文本的方式是将它们封装在一个函数调用中，该函数调用为_()，仅仅是一个下划线。最简单的情况是源代码中出现的字符串。下面是一个flask()语句的例子：

    from flask_babel import _
    # ...
    flash(_('Your post is now live!'))

`_()`函数用于原始语言文本（在这种情况下是英文）的封装。 该函数将使用由localeselector装饰器装饰的选择函数，来为给定客户端查找正确的翻译语言。 _()函数随后返回翻译后的文本，在本处，翻译后的文本将成为flash()的参数。

但是不可能每个情况都这么简单，有些字符串文字并非是在发生请求时分配的，比如在应用启动时。因此在评估这些文本时，无法知道要使用哪种语言。 一个例子是与表单字段相关的标签，处理这些文本的唯一解决方案是找到一种方法来延迟对字符串的评估，直到它被使用，比如有实际上的请求发生了。 `Flask-Babel`提供了一个称为`lazy_gettext()`的`_()`函数的延迟评估的版本：

    from flask_babel import lazy_gettext as _l

在这里，我正在导入的这个翻译函数被重命名为`_l()`，以使其看起来与原始的`_()`相似。 这个新函数将文本包装在一个特殊的对象中，这个对象会在稍后的字符串使用时触发翻译。

Flask-Login插件只要将用户重定向到登录页面，就会闪现消息。 此消息为英文，来自插件本身。 为了确保这个消息也能被翻译，我将重写默认消息，并用`_l()`函数进行延迟处理：

    _() 用于原始语言标记翻译
    _l() 针对无法提前评估的文本，进行延迟评估

### 提取文本进行翻译

一旦应用所有_()和_l()都到位了，你可以使用pybabel命令将它们提取到一个*.pot文件中，该文件代表可移植对象模板*。 这是一个文本文件，其中包含所有标记为需要翻译的文本。 这个文件的目的是作为一个模板来为每种语言创建翻译文件。

提取过程需要一个小型配置文件，告诉pybabel哪些文件应该被扫描以获得可翻译的文本。 下面你可以看到我为这个应用创建的babel.cfg：

babel.cfg：PyBabel配置文件

    [python: app/**.py]
    [jinja2: app/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_

前两行分别定义了Python和Jinja2模板文件的文件名匹配模式。 第三行定义了Jinja2模板引擎提供的两个扩展，以帮助Flask-Babel正确解析模板文件。

可以使用以下命令来将所有文本提取到* .pot *文件：

    (venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .

pybabel extract命令读取-F选项中给出的配置文件，然后从命令给出的目录（当前目录或本处的. ）扫描与配置的源匹配的目录中的所有代码和模板文件。 默认情况下，pybabel将查找_()以作为文本标记，但我也使用了重命名为_l()的延迟版本，所以我需要用-k _l来告诉该工具也要查找它 。 -o选项提供输出文件的名称。

我应该注意，messages.pot文件不需要合并到项目中。 这是一个只要再次运行上面的命令，就可以在需要时轻松地重新生成的文件。 因此，不需要将该文件提交到源代码管理。

### 生成语言目录
该过程的下一步是在除了原始语言（在本例中为英语）之外，为每种语言创建一份翻译。 我要从添加西班牙语（语言代码es）开始，所以这样做的命令是：

    (venv) $ pybabel init -i messages.pot -d app/translations -l es
    creating catalog app/translations/es/LC_MESSAGES/messages.po based on messages.pot

pybabel init命令将messages.pot文件作为输入，并将语言目录写入-d选项中指定的目录中，-l选项中指定的是翻译语言。 我将在app/translations目录中安装所有翻译，因为这是Flask-Babel默认提取翻译文件的地方。 该命令将在该目录内为西班牙数据文件创建一个es子目录。 特别是，将会有一个名为app/translations/es/LC_MESSAGES/messages.po的新文件，是需要翻译的文件路径。

如果你想支持其他语言，只需要各自的语言代码重复上述命令，就能使得每种语言都有一个包含messages.po文件的存储库。

在每个语言存储库中创建的messages.po文件使用的格式是语言翻译的事实标准，使用的格式为gettext。   

如果你跳过首段，可以看到后面的是从_()和_l()调用中提取的字符串列表。 对每个文本，都会展示其在应用中的引用位置。 然后，msgid行包含原始语言的文本，后面的msgstr行包含一个空字符串。 这些空字符串需要被编辑，以使目标语言中的文本内容被填充。

有很多翻译应用程序与.po文件一起工作。 如果你擅长编辑文本文件，量少的时候也就罢了，但如果你正在处理大型项目，可能会推荐使用专门的编辑器。 最流行的翻译应用程序是开源的poedit，可用于所有主流操作系统。 如果你熟悉vim，那么po.vim 插件会提供一些键值映射，使得处理这些文件更加轻松。

messages.po文件是一种用于翻译的源文件。 当你想开始使用这些翻译后的文本时，这个文件需要被编译成一种格式，这种格式在运行时可以被应用程序使用。 要编译应用程序的所有翻译，可以使用pybabel compile命令，如下所示：

    (venv) $ pybabel compile -d app/translations
    compiling catalog   app/translations/es/LC_MESSAGES/messages.po to
    app/translations/es/LC_MESSAGES/messages.mo

此操作在每个语言存储库中的messages.po旁边添加messages.mo文件。 .mo文件是Flask-Babel将用于为应用程序加载翻译的文件。

在为西班牙语或任何其他添加到项目中的语言创建messages.mo文件之后，可以在应用中使用这些语言。 如果你想查看应用程序以西班牙语显示的方式，则可以在Web浏览器中编辑语言配置，以将西班牙语作为首选语言。 对Chrome，这是设置页面的高级部分：

#### Chrome语言选项

如果你不想更改浏览器设置，另一种方法是通过使localeselector函数始终返回一种语言来强制实现。 对西班牙语，你可以这样做：

    app/__init__.py：选择最佳语言。
    
    @babel.localeselector
    def get_locale():
        # return request.accept_languages.best_match(app.config['LANGUAGES'])
        return 'es'

使用为西班牙语配置的浏览器运行该应用或返回es的localeselector函数，将使所有文本在使用该应用时显示为西班牙文。

### 更新翻译

处理翻译时的一个常见情况是，即使翻译文件不完整，你也可能要开始使用翻译文件。 这是非常好的，你可以编译一个不完整的messages.po文件，任何可用的翻译都将被使用，而任何缺失的部分将使用原始语言。 随后，你可以继续处理翻译并再次编译，以便在取得进展时更新messages.mo文件。

如果在添加_()包装器时错过了一些文本，则会出现另一种常见情况。 在这种情况下，你会发现你错过的那些文本将保持为英文，因为Flask-Babel对他们一无所知。 当你检测到这种情况时，会想要将其用_()或_l()包装，然后执行更新过程，这包括两个步骤：

    (venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
    (venv) $ pybabel update -i messages.pot -d app/translations

extract命令与我之前执行的命令相同，但现在它会生成messages.pot的新版本，其中包含所有以前的文本以及最近用_()或_l()包装的文本。 update调用采用新的messages.pot文件并将其合并到与项目相关的所有messages.po文件中。 这将是一个智能合并，其中任何现有的文本将被单独保留，而只有在messages.pot中添加或删除的条目才会受到影响。

messages.po文件更新后，你就可以继续新的测试了，再次编译它，以便对应用生效。

### 翻译日期和时间

现在，我已经为Python代码和模板中的所有文本提供了完整的西班牙语翻译，但是如果你使用西班牙语运行应用并且是一个很好的观察者，那么会注意到还有一些内容以英文显示。 我指的是由Flask-Moment和moment.js生成的时间戳，显然这些时间戳并未包含在翻译工作中，因为这些包生成的文本都不是应用程序源代码或模板的一部分。

moment.js库确实支持本地化和国际化，所以我需要做的就是配置适当的语言。 Flask-Babel通过get_locale()函数返回给定请求的语言和语言环境，所以我要做的就是将语言环境添加到g对象，以便我可以从基础模板中访问它：

Flask-Babel的get_locale()函数返回一个本地语言对象，但我只想获得语言代码，可以通过将该对象转换为字符串来获取语言代码。 现在我有了g.locale，可以从基础模板中访问它，并以正确的语言配置moment.js：

app/templates/base.html：为moment.js设置本地语言

    ...
    {% block scripts %}
        {{ super() }}
        {{ moment.include_moment() }}
        {{ moment.lang(g.locale) }}
    {% endblock %}

现在所有的日期和时间都与文本使用相同的语言了。  
 
此时，除用户在用户动态或个人资料说明中提供的文本外，所有其他的文本均可翻译成其他语言。













## Flask-script


Flask-Script的作用是通过命令行的形式操作Flask。

通过命令执行开发版本的服务器、执行定时任务，或者可以进行一些配置。

要使用Flask-Script可以通过 pip install flask-script进行安装。

使用方式，创建一个manage.py文件：
```
from flask_script import Manager,Server

from flask import Flask

app=Flask(__name__)

manager=Manager(app)

manager.add_command(“runserver”,Server(port=8000))

@app.route(‘/’)

def index():

return “Hello，guys！”

if __name__==”__main__”:

    manager.run()
```
然后我们就可以通过python manage.py runserver启动我们的app了。其中port=8000，表示我们要打开localhost:8000端口进行访问。

定义命令的三种方法：

1.使用@command装饰器：
```
@manager.command

def hello():

print “test”
```
然后可以使用python manage.py hello命令，就可以看到输出 “test”了。

2.使用类继承Command类：
```
from flask_script import Command

class CommandTest(Command):

print “test”

def run(self):

   print “这是run方法，必须实现”

manager.add_command(‘hello’,CommandTest())
```
使用类的方式，有三点需要注意：

(1)继承Command类   (2)必须实现run方法    (3)必须通过add_command方法添加命令。

3.使用option装饰器：如果想在使用命令时，传递参数进去，使用@option装饰器更加方便：
```
@manager.option(‘-n’,’--name’,dest=’name’)

def hello(name):

print ‘hello ’,name

这样调用：

python manage.py –n test

或者

python manage.py - -name test
```
就可以输出 hello test。

添加参数到命令中：

option装饰器：以上三种创建命令的方式都可以添加参数，下边看几个添加多个参数的方式：
```
@manager.option(‘-n’,’--name’,dest=’name’,default=’Anthony’)

@manager.option(‘-u’,’--url’,dest=’url’,default=None)

def hello(name,url):

  if url is None:

print “hello ”,name

  else:

      print “hello ”,name,”from”, url
```
类继承：类继承也可以添加参数：
```
from flask_script import Command,Manager,Option

class CommandTest(Command):

option_list=(

  Option(‘--name’,’-n’,dest=’name’),

)

def run(self,name):

   print “hello %s” % name
```
如果要在指定参数的时候，动态做一些事情，使用get_options方法：
```
class CommandTest():

def __init__(self,default_name=’Anthony’):

    self.default_name=default_name

def get_options(self):

   return [Option(‘-n’,’--name’,dest=’name’,default=self.default_name),]

def run(self,name):

   print “hello ”,name

```








## Flask-guess_language

语言检测库










## Flask-Bootstrap

最受欢迎的CSS框架之一是由Twitter推出的Bootstrap。 如果你想看看这个框架可以设计的页面类型，文档有一些示例。

这些是使用Bootstrap来设置网页风格的一些好处：

- 在所有主流网页浏览器中都有相似的外观
- 自动处理PC桌面，平板电脑和手机屏幕尺寸
- 可定制的布局
- 精心设计的导航栏，表单，按钮，警示，弹出窗口等

使用Bootstrap最直接的方法是简单地在你的基本模板中导入bootstrap.min.css文件。 可以下载此文件并将其添加到你的项目中，或直接从CDN导入。 然后，你可以根据其文档开始使用它提供的通用CSS类，以及[块的完整列表](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#available-blocks)实在是太棒了。 你可能还需要导入包含框架JavaScript代码的bootstrap.min.js文件，以便使用最先进的功能。

Bootstrap捆绑了许多常见的UI元素，所有这些元素都在地址为 https://getbootstrap.com 的Bootstrap文档中有demo和示例。 其中一个组件是Popover（弹窗），在文档中将其描述为“用于容纳辅助信息的小的覆盖窗口”。 

幸运的是，有一个名为Flask-Bootstrap的Flask插件，它提供了一个已准备好的基础模板，该模板引入了Bootstrap框架。


## Flask-blueprint 

为什么学习蓝图？
- 我们学习Flask框架，是从写单个文件，执行hello world开始的。我们在这单个文件中可以定义路由、视图函数、定义模型等等。但这显然存在一个问题：随着业务代码的增加，将所有代码都放在单个程序文件中，是非常不合适的。这不仅会让代码阅读变得困难，而且会给后期维护带来麻烦。

什么是蓝图？
- 蓝图：用于实现单个应用的视图、模板、静态文件的集合。
- 蓝图就是模块化处理的类。
- 简单来说，蓝图就是一个存储操作路由映射方法的容器，主要用来实现客户端请求和URL相互关联的功能。 在Flask中，使用蓝图可以帮助我们实现模块化应用的功能。

蓝图的运行机制：
- 蓝图是保存了一组将来可以在应用对象上执行的操作。注册路由就是一种操作,当在程序实例上调用route装饰器注册路由时，这个操作将修改对象的url_map路由映射列表。当我们在蓝图对象上调用route装饰器注册路由时，它只是在内部的一个延迟操作记录列表defered_functions中添加了一个项。当执行应用对象的 `register_blueprint()` 方法时，应用对象从蓝图对象的 defered_functions 列表中取出每一项，即调用应用对象的 add_url_rule() 方法，这将会修改程序实例的路由映射列表。
- 为了注册blueprint，将使用Flask应用实例的register_blueprint()方法。 
    在注册blueprint时，任何视图函数，模板，静态文件，错误处理程序等均连接到应用。将blueprint的导入放在app.register_blueprint()的上方，以避免循环依赖。
    """
    
其他说明
- 在Flask中，blueprint是代表应用子集的逻辑结构。
- blueprint可以包括路由，视图函数，表单，模板和静态文件等元素。
- 如果在单独的Python包中编写blueprint，那么你将拥有一个封装了应用特定功能的组件。
- Blueprint的内容最初处于休眠状态。
- 为了关联这些元素，blueprint需要在应用中注册。
- 在注册过程中，需要将添加到blueprint中的所有元素传递给应用。
- 因此，你可以将blueprint视为应用功能的临时存储，以帮助组织代码。

      blueprint的@bp.app_errorhandler装饰器和@app.errorhandler装饰器基本没区别，尽管两个装饰器最终都达到了相同的结果，但这样做的目的是试图使blueprint独立于应用，使其更具可移植性。
      
        # Blueprint必须指定两个参数，第一个表示蓝图的名称，第二个表示蓝图所在模块
        bp = Blueprint('errors', __name__)


