# Update-From-Leetcode

>第一次自己因为自己的小需求写的一个小东西，还是要纪念一下。目的很简单，就是通过对粗暴爬leetcode了解到现在有多少题了，是不是该继续刷题了！（逃

##简介
***
**UFL**，我起的名字！

##遇到的问题的记录及解决方法
***
###Version 1.0

1. requests.get()方法接收到的return已经是type unicode（真正的“字符”串），这时候如果要转化为type str需要利用encode()方法。
2. encode()之后不能直接循环进行re.match()。encode之后的结果是一个str，直接循环取出的是str的每一个字符，而不是yy的一行，这里还在寻求更好的解决方法。目前的解决方法是将其存到txt中，然后再逐行读取。

*Due 2016.1.22*
