# 本程序仅供测试学习，请勿用于非法
# 指路
中间人攻击的基站部分： 
https://github.com/Qmeimei10086/Openbts-gsm-mitm 
# FIXME
处于奇怪的原因我无法完整的上传修改过osmocom-bb文件，只能上传压缩包 
# 简介
此程序为gsm中间人攻击的mobile程序，对osmocombb的mobile程序就行修改，使其可以将鉴权时的rand发送至服务端并获取相对应的sres，已经完全符合gsm中间人攻击的需求 
# 编译
环境：Ubuntu16.04 
参考：https://blog.csdn.net/gibbs_/article/details/119213685 
（目前我见到国内最详细的过程，符合中国宝宝体质）
## 1.安装编译osmocombb的环境
```javascript
apt-get install build-essential libgmp3-dev libmpfr-dev libx11-6 libx11-dev texinfo flex bison libncurses5 libncurses5-dbg libncurses5-dev libncursesw5 libncursesw5-dbg libncursesw5-dev zlibc zlib1g-dev libmpfr4 libmpc-dev   subversion  git  autoconf  vim 
```
```javascript
apt-get install autoconf libtool libosip2-dev libortp-dev libusb-1.0-0-dev g++ sqlite3 libsqlite3-dev libreadline6-dev libncurses5-dev 
```
```javascript
apt-get install libfftw3-3 libfftw3-dev libfftw3-doc 
```
```javascript
apt-get install build-essential libtool libtalloc-dev shtool autoconf automake git-core pkg-config make gcc libpcsclite-dev 

```
```javascript
apt-get install libunbound-dev libusb-dev libmnl-dev libsctp-dev python3 libgnutls28-dev 
```
## 2.编译libosmocore
```javascript
cd libosmocore-1.8.0
atoreconf -i 
./configure
```
### 注意，因为下载的libosmocore默认版本是unknown所以我们需要修改版本防止接下来报错，修改完之后 
```javascript
vim Makefile
```
搜索"UNKNOWN"并所有的替换为1.8.0
```javascript
make 
make install 
ldconfig -i 
cd ..
```
## 3.编译libosmo-dsp
```javascript
git clone https://gitea.osmoxom.org/libosmo-dsp 
cd libosmo-dsp 
atoreconf -i 
./configure 
make 
make install 
ldconfig -i 
cd ..

```
## 4.配置gnuarm交叉编译环境
```javascript
tar xvf bu-2.16.1_gcc-4.0.2-c-c++_nl-1.14.0_gi-6.4_x86-64.tar.bz2 
mv gnuarm-* ~/gnuarm 
export PATH=~/gnuarm/bin:$PATH 
```
### 注意：这个gnuarm的编译环境是暂时的，以后每一次编译osmocombb程序都需要再一次实行export PATH=~/gnuarm/bin:$PATH这条命令将gnuarm环境加入环境变量 

## 5.编译刷写程序以及固件
```javascript
unzip osmocom-bb.zip 
cd osmocom-bb/src 
```
我们只需要编译刷写程序和固件

```javascript
make osmocon 
make firmware
cd .. 
```
## 6.编译mobile程序
```javascript
unzio mobile.zip
cd mobile/src
```
我们只需要编译mobile以及一些layer23的程序
```javascript
make layer23 
cd .. 
```
## 像我自己修改的openbts一样，我依然提供了编译过的程序以及所需的动态链接库文件(.so)，在/bin目录下，不过可能有缺
# 使用
## 1.刷写layer1固件
```javascript
cd osmocom-bb/src/host/osmocon
./osmocon -m c123xor -p /dev/ttyU SB0 -c ../../target/firmware/board/compal_e88/layer1.highram.bin 
```
此时短按按c118的开机键即可刷入 
## 2.启动server程序
再开一个终端
```javascript
python3 server.py 
```
使用参考我的openbts程序：https://github.com/Qmeimei10086/Openbts-gsm-mitm 
## 3.启动mobile程序
再开一个终端
```javascript
cd mobile/src/host/layer23/src/mobile 
./mobile -c default.cfg
```
即可搜索附近基站并附着
### 如果你使用已编译过的程序，过程差不多不过路径可能要改一改

# 关于作者
bilibili：https://space.bilibili.com/431312664?spm_id_from=333.1007.0.0
有问题来这里找我，本人已高三，可能不能及时回

# 参考
参考论文：张浩 基于USRP的无线移动通信网络隐蔽定点攻击研究 西安电子科技大学 June 2018  
https://www.doc88.com/p-6314772688570.html?_refluxos=a10  

参考报道：如何利用LTE4G伪基站GSM中间人攻击攻破所有短信验证，纯干货！|硬创公开课  
https://mr.baidu.com/r/1mu2ZKDWZc4?f=cp&u=eaecb9839550917e  

参考视频：GSM中间人攻击演示 科技张工  
https://b23.tv/oMYL3BO  

# Finally
本程序仅供学习，请勿用于非法 
这这只是个测试程序，还不是完整的gsm中间人攻击mobile部分的全部
这也算圆了我初一时的梦想，我从初一时接触osmocombb项目，到现在一步一步的写出中间人攻击的程序，感谢所有互联网上公开教程的那些大佬与osmocom开源社区，正是因为你们无私的互联网精神帮助着我一步一步的探索着 
虽然我知道这个程序可能被用于违法，但我依然公开了代码与教程，这正是我对互联网精神的诠释，希望能补充gsm中间人攻击这一领域的空白 
第一次写教程，若有错误，多多指教   
mobile端与伪基站结合起来的完整漏洞利用过程以及原理就等我买的另一台c118到货在更新吧！   
其实gsm中间人攻击+4g的rec重定向攻击才是适合中国现在环境完整的攻击方式，不过那个真的要等到大学了，一是实在是没时间了，马上暑假结束高三上课了，二是说需要的usrp或者其他的sdr设备我真的买不起啊啊啊啊，要是有人能送我一台就好了www，不过2g的基站我到是有便宜的实现方法，就是CalypsoBTS项目，利用c118伪造周围基站信号搭建基站，不过具体过程下次再说吧    






























