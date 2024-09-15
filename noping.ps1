$pingFail = 0
$pingCount = 0
$successfulPings = 0

$target = Read-Host "Enter the IP address to ping"

if ([string]::IsNullOrEmpty($target)) {
    Write-Host "No IP address provided. Exiting..."
    exit 1
}

while ($pingFail -eq 0) {
    $pingCount++
    $pingResult = Test-Connection -ComputerName $target -Count 1 -Quiet

    if (-not $pingResult) {
        Write-Host "Ping $pingCount failed to $target" -NoNewline
        [Console]::Beep()
    }
    else {
        $successfulPings++
        $percentage = [math]::Round(($successfulPings / $pingCount) * 100, 2)
        Write-Host "Ping $pingCount succeeded to $target ($percentage%)" -NoNewline
    }

    Start-Sleep -Seconds 2
    Write-Host "`r" -NoNewline
