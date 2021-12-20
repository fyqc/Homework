# JavaScript 进阶

## JavaScript BOM 操作

BOM - Browser Object Model

1. 获取浏览器窗口尺寸

```javascript
// 获取浏览器可视窗口的宽度
var w = window.innerWidth

// 获取浏览器可视窗口的高度
var h = window.innerHeight

// 输出一下
console.log(w)  // 1196
console.log(h)  // 487
```

2. 浏览器的弹出层

```javascript
提示框： 
    window.alert('欢迎光临')

询问框： 
    var res = window.confirm('你爱我吗？')
    // 输出返回值
    console.log(res)  // 点确定是 true，点取消是 false

输入框：
    var res = window.prompt('请输入您的银行卡密码')
    // 输出返回值
    console.log(res)  // 点确定是 输入的内容，点取消是 null
```

3. 开启和关闭标签页
```javascript
开启：
    window.open('地址')

关闭：
    window.close()
```
```html
<body>
    <button id = "on">开启</button>
    <button id = "off">关闭</button>

    <script>
        // 开启按钮的点击事件
        on.onclick = function(){
            // 开启标签页
            window.open('https://www.google.com/')
        }
        // 关闭按钮的点击事件
        off.onclick = function(){
            // 关闭标签页
            window.close()
        }
    </script>
</body>
```

4. 浏览器常见事件

```javascript
资源加载完毕： 
    window.onload = function(){
        console.log('资源已经加载完毕')
    }

可视尺寸改变： 
    window.onresize = function(){
        console.log('窗口尺寸发生改变了')
    }

滚动条位置改变： 
    window.onscroll = function(){
        console.log('滚动条位置改变了')
    }
```

5. 浏览器的历史记录操作

```javascript
回退页面： 
    window.history.back()

前进页面： 
    window.history.forward()
```

6. 浏览器卷去的尺寸
```javascript
卷去的高度：
    document.documentElement.scrollTop  // 有 !DOCTYPE 时用
    document.body.scrollTop  // 没有 !DOCTYPE 时用

兼容写法：
    // 滚动条位置变化
    window.onscroll = function(){
        // 兼容的写法
        var height = document.documentElement.scrollTop || document.body.scrollTop

        console.log(height)
    }

卷去的宽度：
    document.documentElement.scrollLeft  // 有 !DOCTYPE 时用
    document.body.scrollLeft  // 没有 !DOCTYPE 时用

兼容写法：
    // 滚动条位置变化
    window.onscroll = function(){
        // 兼容的写法
        var width = document.documentElement.scrollLeft || document.body.scrollLeft

        console.log(width)
    }
```

7. 浏览器滚动到

```javascript
滚动到： window.scrollTo()
    
    参数方式 1： window.scrollTo(left, top)
        left: 浏览器卷去的宽度 
        top: 浏览器卷去的高度

    参数方式 2： window.scrollTo({
        left: xx,
        top: yy,
        behavior: 'smooth'
    })


```
```javascript

```
