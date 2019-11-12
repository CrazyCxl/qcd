qcd is a tool to quickly change directories. 
===
Install
---
cp qcd.sh /etc/profile.d/  
cp qcd.py /usr/bin/

restart the terminal 

Install in zsh
---
add follow line in ~/.zshrc
```
. /etc/profile.d
```

Use
---
- qcd <数字> 切换目录
- qcd 切换到目录1或2 

参数：

-  -l 列出所有目录 
-  rm <path> 删除指定目录 
-  append <path> 追加指定目录 
-  -i  <path> 插入目录 
-  clear 清空目录 
-  -h 帮助 
