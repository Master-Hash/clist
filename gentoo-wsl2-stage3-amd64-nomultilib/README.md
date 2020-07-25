# wsl2 安装 Gentoo

自己先把博客炸掉，又把台机炸掉，只好四海为家了。当作测评文。

和 Debian 相比，Gentoo 自带的 Prompt 和编辑器高亮都要好看得多。  
直接导入 tar 包，真的是无比的灵活。最后发现`eselect rc list`还可以正确显示 wsl 的自动配置。

[教程](https://developer.moe/gentoo-on-wsl-2)  
这个教程显然需要一些勘误。

## Introduction
Windows 10 2004 已经 release，所以无需上测试版的船。（我今天上船是因为新版的开始菜单。另外新版的 wsl --install 也还行。GUI 不知道什么时候来，不过已经不重要了。）

## Enabling WSL 2 support
对应的功能中文名为~~`无中文名`~~和`虚拟机平台`。build 20150 起用 wsl --install （在前者未开启时）可以将二者一并开启。  
至于上面说的这个 Bug，

    Activating Hyper-V breaks ALL VirtualBox Machines!

    VirtualBox 6.1.4 works again with Windows 10 19564,
    but it runs unusable slow and crashes frequently.

现在应该不存在了。今年寒假至清明前测试 build 19041（2004 release，但彼时还相当于 rc）和彼时最新的 VirtualBox（越 6.1.2/4），旧虚拟机普遍崩溃，新虚拟机性能也不如开启 hyper-v 之前的旧虚拟机。二者都比不过 openSUSE host 的 VirtualBox。  
当时有这样一篇[教程](https://www.rehtt.com/index.php/archives/225)和官方论坛的一则[讨论](https://forums.virtualbox.org/viewtopic.php?t=90853)

今天测试较少，参考价值不大。总体来说，很稳。

## Installation of the Gentoo userspace
也就是安装 stage3。
目前 gentoo stage3 格式为 tar.xz，Windows 下推荐使用 7-zip 解压成 **tar（不要解包！）**

## Changing the Gentoo option displayed in the Windows Terminal app
本人修改配置已经轻车熟路了。听说过几个月图形化的设置界面就上线了。

我只加了 icon，把 Debian 和 Gentoo 从两只呆企鹅变成了各自的 logo（也差评，一个底色难看，一个分辨率太低）。.ico 来自`/favicon.ico`。

**剩下的，熟手自己动手配置下，生手就先降低些标准，能跑就行，慢慢改，又不要求你自己编译内核，已经很不错了。**  
**沙箱无需禁用**

## /usr/src 配置
我即将写个 ebuild 自动处理。此前还是委屈下。

## 修改默认目录
https://blog.csdn.net/qq_29384639/article/details/90518491

## 修改默认用户
先创建用户，修改密码，配好 wheel 组，再
~~`> <发行版名> config --default-user <用户名>`~~

[教程](https://www.jianshu.com/p/468dfa4f365d)  
实际上，只有从商店安装的 WSL 才会自带一个执行文件，所以 import 的只能自己改注册表。
我并不知道是 HKEY_USERS 的哪一个子项，所以直接搜索了 LXSS，直达。
补充：[教程](https://www.cnblogs.com/oboth-zl/p/12769220.html)

话说至于为什么都是 1000。。。自己考证去，我昏的，没看清楚。


## 内核
[从此查看发行](https://docs.microsoft.com/zh-cn/windows/wsl/kernel-release-notes)  
[从此下载](https://github.com/microsoft/WSL2-Linux-Kernel/releases)

releases 界面给的是 tar.gz 包（zip 的不要，权限有锅）  
个人的方案是 `tar xzvfp 2020-07-24-12-20-02-WSL2-Linux-Kernel-4.19.121-microsoft-standard.tar.gz`，出来的是一个文件夹。名字显然不是 Gentoo 的规范（规范是什么，我也不知道，明天快查）

总体不是太吃内存。check 时 CPU 30% 左右，编译时 70%~80%，内存最高的时候 1200M。当然全过程没有 gcc llvm 之类的重型包。。。
