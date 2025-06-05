$sourcePath = "C:\Users\monica\Documents\xwechat_files\qingchen536521_c584\msg\file\2025-06"
$desktopPath = [Environment]::GetFolderPath("Desktop")

$keywords = @("新范本", "店小秘 非BW", "店小秘 BW")

foreach ($keyword in $keywords) {
    $matchingFiles = Get-ChildItem -Path $sourcePath -Filter "*.xlsx" -Recurse |
        Where-Object { $_.Name -like "*$keyword*" } |
        Sort-Object LastWriteTime -Descending

    if ($matchingFiles.Count -gt 0) {
        $latestFile = $matchingFiles[0]
        $destination = Join-Path -Path $desktopPath -ChildPath $latestFile.Name
        Copy-Item -Path $latestFile.FullName -Destination $destination -Force
        Write-Host "已复制 $($latestFile.Name) 到桌面"
    } else {
        Write-Host "未找到包含 '$keyword' 的文件"
    }
}
