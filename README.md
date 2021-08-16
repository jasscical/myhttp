# 项目简介-myhttpd

本项目是基于Tinyhttpd扩展实现的web服务器，基于epoll事件驱动I/O，采用高效的Reactor模型+线程池进行客户端连接任务管理，支持高并发的Get与Post的http请求。

# 项目构建方法
1. git clone
2. cd myhttp
3. make
4. ./httpd

# 主要技术

- Epoll I/O多路复用技术

+ Reactor模式

* 线程池

- Socket网络编程相关知识
- http报文格式
- http请求命令get/post
- 动态请求解析技术cgi

+ 进程通信（管道pipe）

# 注意事项

- 端口配置在httpd.cpp 默认为14000
+ HTTP请求页面为htdocs目录下的.html与.cgi后缀文件(可以手动添加)

# 改进方向
- 添加命令行解析
+ 增加定时器删除不常用连接
- 内存池
# 参考文章
- [tinyhttpd主要源码解析](https://blog.csdn.net/qq_44688854/article/details/106578428?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_title~default-0.base&spm=1001.2101.3001.4242)
- [网络编程模式Reactor详解](https://blog.csdn.net/qq_39751437/article/details/105446909)
- [项目--搭建web服务器与客户端](https://blog.csdn.net/qq_39751437/article/details/105265301)
- [计算机网络与网络编程主要面试内容](https://blog.csdn.net/qq_39751437/article/details/104969909)
- [C++实现的高并发web服务器](https://github.com/Fizell/webServer)
- [如何实现一个服务器](https://zyearn.github.io/blog/2015/05/16/how-to-write-a-server/)
- [高性能HTTP服务器:设计和思路](https://blog.csdn.net/qq_41111491/article/details/104288554)
- 《C++服务器开发精髓》张远龙著
