## PowerShell ��ִ�� `notepad "$PROFILE"` ����ӣ�profile �ľ���λ����汾������ͬ����� MS docs��
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
    wsl -d Gentoo -e fortune $args # ����������� Debian �ģ����������
}
# �ǲ��� PowerShell ���û��λ�ò���һ˵������
# д��·��ת�� on Windows
#function vi($file){
#    wsl -d Debian -e vi $args
