- Version：200202
- Maintainer：weachy（维奇）
如果你想了解更多关于 NUC8ixBE 豆子峡谷黑苹果相关知识，请查阅我的文章 http://u.nu/nuc8
If you want to learn more about hackintosh with Intel Bean Canyon. Please visit: http://u.nu/nuc8


- 内置了2套 plist 配置文件，区别如下：
 config.plist：默认配置文件，适配 4k 屏幕
 config-1080p.plist：适合 4k 以下屏幕
注意，以上配置均不显示 OpenCore 引导菜单，希望开机出现菜单的用户，只需要开机时长按 Option（Mac）/alt（Win）键，直到出现引导菜单。另外，双系统用户也可在 MacOS “系统偏好设置”中的“启动磁盘”切换系统。
使用白果的用户对此操作一定不陌生，OpenCore 的理念正是尽可能的模拟白果的原生操作习惯，同时这也是 OC 暂不考虑加入主题的原因之一。


- Clover 迁移 OpenCore 方法：
1、备份出 EFI 分区中的文件
2、EFI 分区内的文件全部删除（双系统的保留 /EFI/Microsoft 文件夹），将解压出的 EFI 文件夹放入 EFI 分区
3、OpenCore 目前没有很好的摇号工具，还是建议沿用 Clover 的摇号方法，如已在 Clover 完成摇号，再自行替换三码到 OpenCore 的配置，参考“三码迁移方法”


- 手动迁移三码方法：（建议缺乏动手能力的小白用户，直接使用豪客制作的“三码迁移工具”，可到群共享下载）
三码的配置名在 Clover 和 OpenCore 略有区别，对应关系如下：
	BoardSerialNumber 或 MLB	-> MLB
			    ROM	-> ROM
	  	   SerialNumber -> SystemSerialNumber
    		     CustomUUID	-> SystemUUID
使用文本编辑器分别打开上一步中备份的 Clover 的 config.plist，以及 OpenCore 的 config.plist 配置文件。将以上四个值复制到对应字段的下一行，注意复制时要包含“值类型定义”一起复制替换（“<>”的部分），例如 Clover 中如下配置：
<key>ROM</key>
<data>ExcM+qxi</data>
需要复制 <data>ExcM+qxi</data> 替换到 OC 配置文件中，不能只复制 ExcM+qxi。


- Intel 板载蓝牙驱动使用说明：
首先强烈建议先阅读我的文章（http://u.nu/nuc8）中关于蓝牙的部分（问题 3.1）充分了解其利弊。如你已充分考虑好使用板载蓝牙，步骤如下：
1、如果之前未使用蓝牙相关功能，可直接查看第 3 步。删除所有已配对蓝牙设备，并删除 /Library/Preferences/com.apple.Bluetooth.plist 文件
2、移除现有USB蓝牙或拆机卡蓝牙，重启进入 bios，开启板载蓝牙（device--onboard--bluetooth）
3、将 /EFI/intel板载蓝牙驱动/ 文件夹下的三个 kext 复制到 /EFI/OC/Kexts/ 文件夹下
4、覆盖 OC 配置文件：在 /EFI/intel板载蓝牙驱动/ 文件夹下有已适配好板载蓝牙驱动的两个 plist 配置
  config-板载蓝牙.plist：适合 4k 屏幕
  config-1080p-板载蓝牙.plist：适合 4k 以下屏幕
选择适合自己的显示器分辨率的 plist，重命名为 config.plist 并覆盖 /EFI/OC/config.plist 文件，重启即可。


- Changelog：

2020-02-02
1、开启原生 NVRAM（支持使用 OC 启动菜单进入 Recovery 系统以及清除 NVRAM，双系统用户可直接使用系统偏好设置中的“启动磁盘”切换系统）（感谢 @HCLOK168 制作 SSDT）
2、加入 NVMeFix 补丁，可降低 NVME SSD 的待机功耗和温度（对于原本 NVMe SSD 温度就不高的用户可能不明显，我这里测试降低 5～10 度）
3、加入 Intel 板载蓝牙支持（默认关闭，自行开启，详见上述《Intel 板载蓝牙驱动使用说明》）

2020-01-15
1、更新 OpenCore 0.5.4正式版（OC 选择系统页面现已支持上下方向键、以及通过 Ctrl+Enter 键设置默认启动盘）
2、更新 acidanthera 全家桶（Lilu、WhateverGreen、AppleALC 等）
3、加入内核补丁禁止 rtc 定时唤醒，修复 10.15.2 不能自动睡眠的 bug。
4、声卡layout-id改为14（0E），解决音量过小的问题。

2019-12-16
1、采用与豆子峡谷同款 CPU 的 Macbook Pro 13' 2018 款的 CPU 变频策略，从测试结果来看，调度更优秀，低频更低、待机更省电（感谢 @HCLOK168）
2、去除“关于本机”中 2048 MB 显存的修改，恢复成默认（1536 MB）

2019-12-08
1、修复 Mac mini 2018 机型在“关于本机”不显示内存页的问题
2、大幅精简了整个引导的体积（感谢 @豪客）

2019-12-04
1、更新 OpenCore 0.5.3正式版
2、更新 acidanthera 全家桶（Lilu、WhateverGreen、AppleALC等）


- 天佑中华，希望疫情早日结束。
