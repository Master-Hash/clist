**这个文件夹装有自己阿里云服务器上面跑的 docker 镜像里面的实际配置文档信息，当然不是全部。**  
~~我寻思是不是可以再做个 bind mount~~ 大概不行。

说明：
- docker 里疑似不支持沙箱。原因暂时未知。WSL1 证实不支持，因为仅 Linux 内核受支持。WSL 2 沙箱情况良好。详见 `man 5 make.conf` [在线文档](https://dev.gentoo.org/~zmedico/portage/doc/man/make.conf.5.html)  
附报错信息：  
`Unable to unshare: EPERM (for FEATURES="ipc-sandbox network-sandbox pid-sandbox")`
- 关于 dummy —— 应该可以顾名思义吧。

关于阿里云：没有原生的 Gentoo 镜像很遗憾。听说用 memdisk 装镜像可以重装（找不到链接了），不过我还是放弃吧。Gentoo Prefix 还更简单呢。
服务器的思维和桌面很不同……现在掌握的都很少。

~~记着 run 的时候把 `/usr/src` 挂到 `/usr/src` 上面。（很不爽）~~实测 Debian 的`/usr/src/`里面是一堆 headers，不能直接用。我还是学学写 ebuild 吧。
