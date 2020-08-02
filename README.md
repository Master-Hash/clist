# DOTFILES
最常用的列表和配置文件

## USAGE
使用`git clone -b ${branch} https://github.com/Master-Hash/dotfiles.git`来获取对应分支的代码。

使用 Make 进行配置、上传等（计划中）

## DEV GUIDE
有几个重要的 `git` 命令：`git rebase` `git merge` `git branch` `git checkout` 进行分支管理。

## TODO
1. 用分支而非文件夹管理不同 profile（参考 Gentoo 的 profile）
2. 其它目录整理（包括文档）
3. 自学 Makefile，试着用此实现 apply，upload 等功能（不就是个省点的 bash 嘛）
4. 一些偏门的配置，比如 ublock origin 的自定义规则；~~rss 列表~~（雾，这个还是 go private 比较好）；~~话说我的 .vimrc 该写长一点了……~~（那我要~~他妈~~ code 干嘛）
5. （可能很久以后或者放弃）merge VirtualBox profile
6. （实验）用符号链接或者其它方案管理
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
