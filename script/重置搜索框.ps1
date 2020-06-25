# 直接上传微软的脚本不知道有没有版权问题
# 所以我来假打一番a
Remove-Item alias:\curl
curl -O "https://download.microsoft.com/download/c/b/5/cb56cadd-1de8-4a8a-9fb0-71796d3a0596/ResetWindowsSearchBox.ps1"
.\ResetWindowsSearchBox.ps1
