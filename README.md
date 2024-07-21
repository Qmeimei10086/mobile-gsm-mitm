# 本程序仅供测试学习，请勿用于非法
# FIXME
处于奇怪的原因我无法完整的上传修改过osmocom-bb文件，只能上传压缩包 
# 简介
此程序为gsm中间人攻击的mobile程序，对osmocombb的mobile程序就行修改，使其可以将鉴权时的rand发送至服务端并获取相对应的sres，已经完全符合gsm中间人攻击的需求 
# 编译
环境：Ubuntu16.04 
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
### 注意，因为下载的libosmocore默认版本是unknown所以我们需要修改版本防止接下来报错 
```javascript
vim Makefile
```
