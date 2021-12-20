# JavaScript基础全套教程
[千锋2021最新版JavaScript基础全套教程](https://www.bilibili.com/video/BV1W54y1J7Ed)

## JavaScript的书写位置

**行内式** － 直接把代码书写在标签身上
```html
<body>
    <!-- a 标签书写代码 － 书写在 href 属性上-->
    <a href = "javascript: JS代码 ;">点我一下</a>
    
    <!-- 非 a 标签书写代码 － 书写在行为属性上 -->
    <div onclick=" alert('hello world')">点我一下</div>
    <!-- 点击行为属性 -->
</body>
```

**内嵌式** － 直接把代码书写在一个 script 标签对内
```html
<body>
    <script>
        alret('hellow world')
        // 内嵌式JS代码，不需要依赖任何行为，打开页面就会执行
    </script>
</body>
```

**外链式** － 把代码书写在一个 .js 文件内
```html
<body>
    <script src="./test.js"></script>
    <!-- 外链式JS代码，不需要依赖任何行为，打开页面就会执行 -->
</body>
```

---

## JavaScript的数据类型

**数值类型 Number**
- 十进制数字、科学计数法、其它进制表示方式的数字

**字符串类型 String**
- 单引号或者双引号包裹的一切内容

**布尔类型 Boolean**
- true 和 false

**空类型 Undefined**
- undefined

**空类型 Null**
- null

使用 typeof 关键字进行基本数据类型的检测  
```html
<body>
    <script>
        var n1 = 100
        var result = typeof n1
        console.log(result)  // number
    </script>
</body>
```

---

## JavaScript 数据类型转换

转数值
```html
<!-- 
1. Number();
语法：Number(要转换的内容)
结果：转换好数值类型的结果
-->
<script>
    // 准备一个变量，赋值为字符串类型内容
    var s1 = '100'
    console.log(s1)  // 100
    console.log(typeof s1)  // string

    // 使用Number()方法进行一下转换
    var n1 = Number(s1)
    console.log(n1)  // 100
    console.log(typeof n1)  // number
</script>

<!-- 
2. parseInt();
语法：parseInt(要转换的内容)
结果：转换好数值类型的结果
-->
<script>
    // 准备一个变量，赋值为字符串类型内容
    var s1 = '100abc'
    console.log(s1)  // 100
    console.log(typeof s1)  // string

    // 使用parseInt()方法进行一下转换
    var n1 = parseInt(s1)
    console.log(n1)  // 100
    console.log(typeof n1)  // number
</script>

<!-- 
3. parseFloat();
语法：parseFloat(要转换的内容)
结果：转换好数值类型的结果
-->
<script>
    // 准备一个变量，赋值为字符串类型内容
    var s1 = '100.234'
    console.log(s1)  // 100
    console.log(typeof s1)  // string
    
    // 使用parseInt()方法进行一下转换
    var n1 = parseInt(s1)
    console.log(n1)  // 100
    console.log(typeof n1)  // number

    // 使用parseFloat()方法进行一下转换
    var n2 = parseFloat(s1)
    console.log(n2)  // 100.234
    console.log(typeof n2)  // number
</script>
```


转字符串
```html
<!-- 
1. String();
语法：String(要转换的内容)
结果：转换好字符串类型的结果
-->
<script>
    // 准备一个变量，赋值为布尔类型内容
    var b1 = true
    console.log(b1)  // true
    console.log(typeof b1)  // boolean

    // 使用String()方法进行一下转换
    var s1 = String(b1)
    console.log(s1)  // true
    console.log(typeof s1)  // string
</script>

<!-- 
2. toString();
语法：要转换的内容.toString()
结果：转换好字符串类型的结果
-->
<script>
    // 准备一个变量，赋值为布尔类型内容
    var b1 = true
    console.log(b1)  // true
    console.log(typeof b1)  // boolean

    // 使用String()方法进行一下转换
    var s1 = b1.toString()
    console.log(s1)  // true
    console.log(typeof s1)  // string
</script>
```

转布尔

```html
<!-- 
1. Boolean();
语法：要转换的内容.Boolean()
结果：转换好布尔类型的结果
-->
<script>
    // 准备一个变量，赋值为字符串类型内容
    var s1 = 'abc'
    console.log(s1)  // abc
    console.log(typeof s1)  // string

    // 使用Boolean()方法进行一下转换
    var b1 = Boolean(s1)
    console.log(b1)  // true
    console.log(typeof b1)  // boolean
</script>
```

只有五个内容会被转换为False:

- 0
- NaN
- ''
- undefined
- null 

其它都会被转换成True

```javascript
console.log(Boolean(0))  // false
console.log(Boolean(NaN))  // false
console.log(Boolean(''))  // false
console.log(Boolean(undefined))  // false
console.log(Boolean(null))  // false

```

---

## 条件分支语句 - if
```javascript
if(){ ... }
// 条件满足就执行，不满足就不执行

if(){ ... } else { ...}
// 条件满足就执行 if 的 {}，不满足就执行 else 的 {}

if(){ ... } else if () { ... }
// 满足哪一个 if 就执行哪一个 if 的 {}， 前面有条件满足了，就不考虑后面的

if(){ ... } else if () { ... } else { ...}
// 所有条件都不满足的时候，就会执行 else 后面的 {}
```

---

## 条件分支语句 - switch

1. 找到和已知条件 **完全匹配** 的选项执行
2. 执行完毕代码需要写 break ，不然会 **向下穿透**
3. 可以书写一个 default ， 会在所有选项 **都不匹配** 的时候执行
4. 当发生穿透效果的时候，会从 **第一个满足条件** 的选项开始向下穿透

```javascript
switch( 已知条件 ){
    case 选项一 :
        ...
        break
    case 选项二 :
        ...
        break  
    default:
        ...  
}
```

---

## 循环结构语句 - while
```javascript
// 定义初始变量 n
var n = 0
// 条件判断 n < 总数
while (n < 3) {
    // 一段重复的代码
    console.log('走一个石板')
    // 改变初始值
    n++
}
// 后续代码
console.log('继续走后面的路')
```

---
## 循环结构语句 - dowhile

当初始变量在条件 **以内** 的时候，while和dowhile循环是一样的

当初始变量在条件**以外**的时候
- while循环一次都 **不执行**
- dowhile循环会 **执行一次**
```javascript
// while循环
while (条件){
    会被重复执行的代码
    ...
}

// do-while循环
do {
    会被重复执行的代码
    ...
} while (条件)
```

---

## 循环结构语句 - for
```javascript
for (定义初始变量①; 条件判断②; 改变初始值④){
    重复执行的代码③
    ...
}

// for 循环结构语句
for (var i = 0; i < 3; i++){
    console.log('走了一个石板路')
}

// 循环结束之后执行的代码
console.log('继续走后面的路')
```

---

## JavaScript 的函数

```javascript
定义：
    function fn(形参){
        装在盒子里面的代码
        ...
        return 返回值
    }

调用：
    函数名(实参)

```

```html
<script>
    // 定义一个函数
    function fn(n){
        var total = 1
        // 结束： 1
        while (n >= 1){
            将每一个数字阶乘到 total 变量
            total *= n
            // 修改初始值
            n--
        }
        // 把计算结果作为函数的返回值
        return total
    }

    // 调用这个函数，求12的阶乘，把结果赋值给 r1
    var r1 = fn(12)
    // 调用这个函数，求10的阶乘，把结果赋值给 r2
    var r2 = fn(10)

    console.log(r1, r2)  // 479001600 3628800
</script>
```

---

## 对象数据类型 - Object

创建
```javascript
var obj = {hair:'没招', eye:'没招'}
```

操作
```javascript
// 增
obj.key = value
obj['key'] = value

// 删
delete obj.key
delete obj['key']

// 改
obj.key = value
obj['key'] = value

// 查
obj.key
obj['key']
```

---

## 数组数据类型 - Array

```javascript
// 创建
var arr = [100, 200, 300, 400, 500]

// 排列
索引： 从 0 开始，依次 + 1

// 长度操作
数组.length  // 访问
数组.length = 数字  // 设置

// 数据操作
数组[索引]  // 访问
数组[索引] = 值  // 设置

// 遍历
利用循环进行遍历，开始为 0， 结束为 小于长度，步长为 1 使用循环控制变量当做索引来访问数组里面的每一个数据

e.g：

    // 准备一个数组
    var arr = [100, 200, 300, 400, 500]
    // 输出数组
    console.log(arr)  // [100, 200, 300, 400, 500]

    // 书写循环
    for (var i = 0; i < arr.length; i++){
        // 输出循环控制变量
        console.log(arr[i])
    }
    // 100
    // 200
    // 300
    // 400
    // 500
```

---

## 数组常用方法

```javascript
// 准备一个原始数组
var arr = [100, 200, 300, 400]

// 1. 从后面追加
语法： 数组.push()
作用： 将数据 追加 到数组的 末尾
返回值： 追加数据后数组 最新的长度

var res = arr.push('追加的')
console.log(arr)  // [100, 200, 300, 400, "追加的"]
console.log(res)  // 5

// 2. 从后面删除
语法： 数组.pop()
作用： 删除数组 最后一个 数据
返回值： 被删除的数据

var res = arr.pop()
console.log(arr)  // [100, 200, 300]
console.log(res)  // 400

// 3. 从前面添加
语法： 数组.unshift(数据)
作用： 将数据 添加 到数组的 最前
返回值： 添加数据后数组 最新的长度

var res = arr.unshift('添加的')
console.log(arr)  // ["添加的", 100, 200, 300, 400]
console.log(res)  // 5

// 4. 从前面删除
语法： 数组.shift()
作用： 删除数组 最前一个 数据
返回值： 被删除的数据

var res = arr.shift()
console.log(arr)  // [200, 300, 400]
console.log(res)  // 100

// 5. 反转数组
语法： 数组.reverse()
作用： 将数组 反转
返回值： 反转后的数组

var res = arr.reverse()
console.log(arr)  // [400, 300, 200, 100]
console.log(res)  // [400, 300, 200, 100]

// 6. 截取并添加
语法： 数组.splice(开始索引， 多少个，要插入的数据)
    开始索引： 默认是 0
    多少个： 默认是 0
    要插入的数据： 默认是 没有
作用： 删除 数组中若干数据，并选择是否 插入 新的数据
返回值： 以新数组的形式返回被删除的数据

var res = arr.splice()  
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // [] 空数组表明没有删除也没有插入

var res = arr.splice(1, 1)  
console.log(arr)  // [100, 300, 400]
console.log(res)  // [200]

var res = arr.splice(1, 1， '新来的')  
console.log(arr)  // [100, "新来的", 300, 400]
console.log(res)  // [200]

// 7. 数组排序
语法： 
    数组.sort()
    数组.sort(function(a, b){return a - b})
    数组.sort(function(a, b){return b - a})
作用： 对数组进行 排序
返回值： 排序好后的数组

// 准备一个原始数组
var arr = [11, 1, 22, 13, 45, 32]

var res = arr.sort()
console.log(arr)  // [1, 11, 13, 2, 22, 32, 45]
console.log(res)  // [1, 11, 13, 2, 22, 32, 45]

var res = arr.sort(function(a, b){return a - b})
console.log(arr)  // [1, 2, 11, 13, 22, 32, 45]
console.log(res)  // [1, 2, 11, 13, 22, 32, 45]

var res = arr.sort(function(a, b){return b - a})
console.log(arr)  // [45, 32, 22, 13, 11, 2, 1]
console.log(res)  // [45, 32, 22, 13, 11, 2, 1]

// 8. 数组连接为字符串
语法： 数组.join(连接符)
作用： 将数组用 连接符 连接成为一个 字符串
返回值： 连接好的 字符串

// 准备一个原始数组
var arr = [100, 200, 300, 400]

var res = arr.join('-')
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // 100-200-300-400


// 9. 拼接数组
语法： 数组.concat(其它数组)
作用： 将其它数组和原始数组 拼接 在一起
返回值： 拼接好的 新数组

var res = arr.concat([500, 600])
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // [100, 200, 300, 400, 500, 600]

// 10. 截取数组
slice()
语法： 数组.slice(开始索引，结束索引)
    开始索引： 默认是 0
    结束索引： 默认是 数组长度
作用： 截取 数组中的某些数据
返回值： 以 新数组 的形式返回截取出来的数据

var res = arr.slice()
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // [100, 200, 300, 400]

var res = arr.slice(1)
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // [200, 300, 400]

var res = arr.slice(1, 3)
console.log(arr)  // [100, 200, 300, 400]
console.log(res)  // [200, 300]

// 11. 查找数据在数组中的索引
语法： 数组.indexOf(数据)
作用： 查找 数据 在数组中的 索引 位置
返回值： 
    有该数据，返回 第一次出现 的索引位置
    没有该数据，返回 -1

// 准备一个原始数组
var arr = [100, 200, 300, 200]

var res = arr.indexOf(200)
console.log(arr)  // [100, 200, 300, 200]
console.log(res)  // 1

var res = arr.indexOf(400)
console.log(arr)  // [100, 200, 300, 200]
console.log(res)  // -1

// 12. 遍历数组
语法： 数组.forEach(function(item, index, arr){})
作用： 遍历 数组
返回值： 无

// 准备一个原始数组
var arr = [100, 200, 300, 400]

arr.forEach(function(item, index, arr){
    // item 就是数组的每一项
    console.log(item)
    // index 就是索引
    console.log(index)
    // arr 就是原始数组
    console.log(arr)
    // 输出一个分隔线
    console.log('--------------')
})

输出结果：
100
0
[100, 200, 300, 400]
--------------
200
1
[100, 200, 300, 400]
--------------
300
2
[100, 200, 300, 400]
--------------
400
3
[100, 200, 300, 400]
--------------

// 13. 映射数组
语法： 数组.map(function(item, index, arr){})
作用： 映射 数组
返回值： 映射后的 新数组

arr.map(function(item, index, arr){
    // 以 return 的方式书写映射条件
    return item * 10
})

console.log(res)  // [1000, 2000, 3000, 4000]

// 14. 过滤数组
语法： 数组.filter(function(item, index, arr){})
作用： 过滤 数组
返回值： 过滤后的 新数组

arr.filter(function(item, index, arr){
    // 以 return 的方式书写条件
    return item > 150
})

console.log(res)  // [200, 300, 400]

// 15. 判断是否全部满足条件
语法： 数组.every(function(item, index, arr){})
作用： 判断数组是不是 每一项 都满足条件
返回值： 一个 布尔值

arr.every(function(item, index, arr){
    // 以 return 的方式书写条件
    return item > 150
})

console.log(res)  // false

arr.every(function(item, index, arr){
    // 以 return 的方式书写条件
    return item > 50
})

console.log(res)  // true

// 16. 判读是否有满足条件的项
语法： 数组.some(function(item, index, arr){})
作用： 判断数组是不是有 某一项 满足条件
返回值： 一个 布尔值

arr.some(function(item, index, arr){
    // 以 return 的方式书写条件
    return item > 150
})

console.log(res)  // true

arr.some(function(item, index, arr){
    // 以 return 的方式书写条件
    return item > 500
})

console.log(res)  // false
```

---

## 字符串常用方法

```javascript
// 1. 按照索引获取字符
语法： 字符串.charAT(索引)
作用： 获取对应索引位置的字符
返回值： 对应索引位置的字符

var str = '你好，微型计算机'

var res = str.charAt(3)
console.log(res)  // 微

// 2. 转小写
语法： 字符串.toLowerCase()
作用： 将字符串内的字母全部转换成 小写
返回值： 转换好的字符串

var str = 'Hello, Rilla'

var res = str.toLowerCase()
console.log(res)  // hello, rilla

// 3. 转大写
语法： 字符串.toUpperCase()
作用： 将字符串内的字母全部转换成 大写
返回值： 转换好的字符串

var res = str.toUpperCase()
console.log(res)  // HELLO, RILLA

// 4. 替换字符串
语法： 字符串.replace(换下内容， 换上内容)
作用： 将字符串内 第一个 满足换下内容的片段替换成换上内容
返回值： 替换好的字符串

var str = '你好，微型计算机，微型计算机'

var res = str.replace('微型', '个人')
console.log(res)  // 你好，个人计算机，微型计算机

// 5.去除首尾空格
语法： 字符串.trim()
作用： 去除字符串手尾的空格
返回值： 去除空格后的字符串

var str = '     你好，世界      '

var res = str.trim()
console.log(res)  // 你好，世界

// 6.切割字符串
语法： 字符串.split(分隔符)
作用： 按照分隔符将字符串切割成为一个数组
返回值： 切割后的数组

var str = '2070-3-22'

var res = str.split('-')
console.log(res)  // ["2070","3","22"]

// 7.截取字符串
语法： 字符串.substr(开始索引，多少个)
作用： 截取字符串
返回值： 截取出来的字符串

// 8.截取字符串
语法： 字符串.substring(开始索引，结束索引)
作用： 截取字符串
返回值： 截取出来的字符串

// 9.截取字符串
语法： 字符串.slice(开始索引，结束索引)
作用： 截取字符串
返回值： 截取出来的字符串

var str = '你好，微型计算机'

var res1 = str.substr(1, 6)
console.log(res1)  // 好，微型计算
var res2 = str.substring(1, 6)
console.log(res2)  // 好，微型计
var res3 = str.slice(1, 6)
console.log(res3)  // 好，微型计
```

---

## 数字常用方法
```javascript
// 1. 0 ~ 1 之间的随机小数
语法： Math.random()
作用： 获取 0 ~ 1 之间的随机小数，包含 0，但是不包含 1
返回值： 0 ~ 1 之间的随机小数

var res = Math.random()
console.log(res)  // 0.2550728782763293

// 2.四舍五入取整
语法： Math.round()
作用： 对数字进行 四舍五入 取整
返回值： 四舍五入后的整数

var res1 = Math.round(10.4)
console.log(res1)  // 10

var res2 = Math.round(10.5)
console.log(res2)  // 11

// 3.向上取整
语法： Math.ceil(数字)
作用： 对数字进行 向上 取整
返回值： 向上取整后的整数

var res1 = Math.ceil(10.4)
console.log(res1)  // 11

// 4.向下取整
语法： Math.floor(数字)
作用： 对数字进行 向下 取整
返回值： 向下取整后的整数

var res2 = Math.floor(10.5)
console.log(res2)  // 10

// 5.取幂
语法： Math.pow(底数，指数)
作用： 对数字进行 取幂 运算
返回值： 取幂后的结果

var res = Math.pow(2, 5)
console.log(res)  // 32

// 6.二次方根
语法： Math.sqrt(数字)
作用： 对数字进行 二次方根 运算
返回值： 二次方根后的结果

var res = Math.sqrt(4)
console.log(res)  // 2

// 7.取绝对值
语法： Math.abs(数字)
作用： 对数字进行 绝对值 运算
返回值： 绝对值运算后的结果

var res = Math.abs(-10)
console.log(res)  // 10

// 8.取最大值
语法： Math.max(数字1, 数字2, 数字3, ...)
作用： 获取若干数字的最大值
返回值： 若干个数字中的最大值

var res = Math.max(-10, 20, -19, 35, 22, 31)
console.log(res)  // -5

// 9.取最小值
语法： Math.min(数字1, 数字2, 数字3, ...)
作用： 获取若干数字的最小值
返回值： 若干个数字中的最小值

var res = Math.max(-10, 20, -19, 35, 22, 31)
console.log(res)  // -19

// 10.近似 π 的值
语法： Math.PI
作用： 得到一个近似 π 的值
返回值： 若干个数字中的最小值

var res = Math.PI
console.log(res)  // 3.141592653589793
```

---

## 时间常用方法 - Date

```javascript
// 创建一个时间对象
var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:02:39 GMT-0500 (Eastern Standard Time)

// 创建一个指定时间节点的时间对象
var time = new Date(年,月,日,时,分,秒)  // 0表示1月 11表示12月

var time = new Date(2002, 1, 23, 11, 22, 18)  // 2002年2月23日11点22分18秒
console.log(time)  // Sat Feb 23 2002 11:22:18 GMT-0500 (Eastern Standard Time)
```

获取

```javascript
// 1. 获取到时间对象中的 年份 信息
时间对象.getFullYear()

// 创建一个时间对象
var time = new Date()
// 获取时间对象中的年份信息
var year = time.getFullYear()
// 输出年份信息
console.log(year)  // 2021

// 2. 获取到时间对象中的 月份 信息
时间对象.getMonth()
// 注意这里依旧是0表示1月 11表示12月

var month = time.getMonth()
console.log(month)  // 11

// 3. 获取到时间对象中的 日期 信息
时间对象.getDate()

var date = time.getDate()
console.log(date)  // 9

// 4. 获取到时间对象中的 小时 信息
时间对象.getHour()

var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:16:28 GMT-0500 (Eastern Standard Time)
var hours = time.getHours()
console.log(hours)  // 8

// 5. 获取到时间对象中的 分钟 信息
时间对象.getMinutes()

var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:16:50 GMT-0500 (Eastern Standard Time
var minutes = time.getMinutes()
console.log(minutes)  // 16

// 6. 获取到时间对象中的 秒钟 信息
时间对象.getSeconds()

var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:18:31 GMT-0500 (Eastern Standard Time)
var seconds = time.getSeconds()
console.log(seconds)  // 31

// 7. 获取到时间对象中的 星期 信息
时间对象.getDay()
// 0表示周日 1-6分别表示周一到周六

var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:20:21 GMT-0500 (Eastern Standard Time)
var week = time.getDay()
console.log(week)  // 4

// 8. 获取到时间对象中的 时间戳 信息
时间对象.getTime()
// 与 格林威治时间 1970-1-1 0:0:0 相差的 毫秒数

var time = new Date()
console.log(time)  // Thu Dec 09 2021 08:22:32 GMT-0500 (Eastern Standard Time)
var ms = time.getTime()
console.log(ms)  // 1639056152619
```

设置

```javascript
// 1. 设置时间对象中的 年份 信息
时间对象.setFullYear(数字)

// 2. 设置时间对象中的 月份 信息
时间对象.setMonth(数字)
// 注意这里依旧是0表示1月 11表示12月

// 3. 设置时间对象中的 日期 信息
时间对象.setDate(数字)

// 4. 设置时间对象中的 小时 信息
时间对象.setHour(数字)

// 5. 设置时间对象中的 分钟 信息
时间对象.setMinutes(数字)

// 6. 设置时间对象中的 秒钟 信息
时间对象.setSeconds(数字)

// 7. 设置时间对象中的 时间戳 信息
时间对象.setTime(数字)
// 与 格林威治时间 1970-1-1 0:0:0 相差的 毫秒数

示例一:
// 创建一个时间对象
var time = new Date()

// 输出一次
console.log(time)  // Thu Dec 09 2021 08:31:48 GMT-0500 (Eastern Standard Time)

// 设置年份信息
var year = time.setFullYear(2002)
// 设置月份信息
var year = time.setMonth(2)
// 设置日期信息
var year = time.setDate(23)
// 设置小时信息
var year = time.setHours(11)
// 设置分钟信息
var year = time.setMinutes(22)
// 设置秒钟信息
var year = time.setSeconds(18)

// 再次输出时间对象
console.log(time)  // Sat Mar 23 2002 11:22:18 GMT-0500 (Eastern Standard Time)


示例二:

// 创建一个时间对象
var time = new Date()

// 输出一次
console.log(time)  // Thu Dec 09 2021 08:33:31 GMT-0500 (Eastern Standard Time)

// 使用时间戳直接定位时间节点
time.setTime(1016853738151)

// 再次输出时间对象
console.log(time)  // Fri Mar 22 2002 22:22:18 GMT-0500 (Eastern Standard Time)
```
