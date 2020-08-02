## PowerShell 下执行 `notepad "$PROFILE"` 并添加，profile 的具体位置随版本有所不同，详见 MS docs。
Set-PSReadLineOption -EditMod emacs
Remove-Item Alias:\wget
Remove-Item Alias:\curl
function git() {
    wsl -d Gentoo -e git $args
}
function neofetch() {
    wsl -d Gentoo -e neofetch --disable Resolution --ascii_distro Windows10 $args
}
function fortune() {
    wsl -d Gentoo -e fortune $args # 本来这个想用 Debian 的，不过不输出
}
# 是不是 PowerShell 真的没有位置参数一说啊……
# 写个路径转换 on Windows
#function vi($file){
#    wsl -d Debian -e vi $args
