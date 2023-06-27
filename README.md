# about
qcd is a tool to quickly change directories. 
```
PS C:\Program Files> qcd -l
1 D:\github\yolov5
2 D:\code\cxl
PS C:\Program Files> qcd
PS D:\github\yolov5> qcd
PS D:\code\cxl>

```

# Install
## Linux
copy qcd file and restart the terminal 
```
cp qcd.sh /etc/profile.d/  
cp qcd.py /usr/bin/
```

### Install in zsh
add follow line in ~/.zshrc first line
```
emulate sh -c 'source /etc/profile'
```

## Windows
run `echo $profile` in powershell to get profile,then copy content to profile
```
$Env:QCD_PATH="D:\\code\\cxl\\qcd"
function qcd()
{
    $QD=$Env:QCD_PATH+'\.qcd\tmp_dir'
    python "$Env:QCD_PATH\qcd.py" $args
    if(Test-Path $QD)
    {
        $target_path=Get-Content $QD
        Set-Location -Path "$target_path"
        del "$QD"
    }
}
```

set `QCD_PATH` to qcd.py dir

### depend
- python3
- powershell

# Use
```
qcd <num>

params：

-l list directory
rm <path> remove path
append <path> append path
-i  <path> insert path
clear clear path
-h show help
```
