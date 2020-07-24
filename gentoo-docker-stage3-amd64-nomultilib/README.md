**这个文件夹装有自己阿里云服务器上面跑的 docker 镜像里面的实际配置文档信息，当然不是全部。**  
~~我寻思是不是可以再做个 bind mount~~ 大概不行。

说明：
- docker 里疑似不支持沙箱。原因暂时未知。WSL1 证实不支持，因为仅 Linux 内核受支持。WSL 2 沙箱情况良好。详见 `man 5 make.conf`
附报错信息：
`Unable to unshare: EPERM (for FEATURES="ipc-sandbox network-sandbox pid-sandbox")`
- 关于 dummy —— 应该可以顾名思义吧。
