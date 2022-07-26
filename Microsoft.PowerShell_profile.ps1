Import-Module PSReadLine

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

Set-PSReadLineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadLineKeyHandler -Key DownArrow -Function HistorySearchForward