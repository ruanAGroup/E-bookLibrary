# E-bookLibrary

### 中期检查

先贴一张运行截图吧

![image-20201012221905614](https://gitee.com/snow_zhao/img/raw/master/img/image-20201012221905614.png)

#### 已完成功能

**添加书籍**：你可以导入你的pdf电子书，程序将自动为你提取封面、作者、书名等信息

**导入文件**：软件支持导入`.docx`、`.md`文件，导入效果还行，但是目前打包出来的软件，导入`markdown`文档的时候会闪退（直接运行代码是没有问题的，应该是`markdown`库的锅，懒得改bug了:joy:，后期再弄吧）

**编辑元数据**：如果你对导入效果不满意的话，可以自行修改书籍的相关信息（但是目前软件并不会将你修改的信息写入pdf的元数据中，看后期有没有空做吧，我太懒了:joy:）

**排序**：软件支持多种方式的排序。

![image-20201012223148530](https://gitee.com/snow_zhao/img/raw/master/img/image-20201012223148530.png)

**阅读书籍**：点击该按钮后，软件将用你电脑默认的pdf阅读器打开文档。当然，我们也做了一个简易的pdf阅读器，如果你不嫌弃它不可以编辑、不可以标注的话（因为软件是用图片来展示pdf的），也可以用它来看你的pdf文档。通道：https://github.com/zhj12138/pdf-reader。目前这个也不支持直接打开我们制作的简易pdf阅读器，因为我还没有给阅读器添加命令行指令，这个功能同样看后期有没有空做吧:joy:（而且现在我也不太会弄这个命令行语句）

**格式转换**：软件支持导出`pdf`为`html`、`txt`、`docx`，其中`html`和`txt`是借助`fitz`这个库实现的，它也是我们简易阅读器的核心库之一。而`docx`则是直接调用的`pdf2docx`的接口

**移除书籍**：如果你觉得哪本书碍眼的话，就点击此按钮将它从书库中移除

**打开书库**：我们的程序在你导入书籍时会将书籍复制到我们的书库目录下，每本书放在一个单独的子目录下面，同时软件会将提取的封面也放到这个子目录下（你可以通过替换这张图片来更换书籍的封面，当然这样修改封面并不方便，但是目前软件的自动生成封面图片的功能并没有做好，所以我就先把这个功能省略了，到时候还会再程序内加入自定义封面的功能）。这个功能也许能方便你对书籍的管理。

**导出信息**：这个功能会将你书库中所有书籍的信息都导出到一个`csv`文件中

**分享**：你可以通过此功能便捷的将你的电子书发送到`kindle`，并且会将你的所有使用过的kindle邮箱记录下来，以提升你下一次的体验。

同时软件还支持将书籍分享到QQ和微信。目前只支持将文件发送过去。我们计划在后期给软件添加`分享图片`的功能，我们会根据书籍的信息自动生成一张也许很精美（:joy:）的图片，然后你可以将此图片分享给你的好友，以此来给你的好友们安利书籍，此功能计划随机生成图片，支持多个模板等等（与之前生成封面的功能是一样的）。

**支持我们**：如果你觉得我们的软件不错的话，欢迎给我们`star` :smile:

**搜索**：软件支持多方式的搜索功能

**历史搜索**：你的搜索将会被软件记录下来，最近的10条记录会被展示在历史搜索中。希望这个功能能给你带来便捷。

#### 未完成功能

软件截图中的`创建书单`、`设置`、`高级搜索`功能还没有开始做（有些功能还没想好要做成什么样)

当然严格来说，书单功能并不是完全不能用，你可以通过编辑书籍的元信息来给书籍添加书单和标签，软件将自动在

![image-20201012230917775](https://gitee.com/snow_zhao/img/raw/master/img/image-20201012230917775.png)

这一栏为你生成相应的信息，你可以通过点击来查看符合条件的书籍

差不多就这些了，记录一下现在时间：2020/10/12 23:15:46

