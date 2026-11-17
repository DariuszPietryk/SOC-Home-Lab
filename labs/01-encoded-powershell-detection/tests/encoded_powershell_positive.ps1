# Benign positive test for the narrowly scoped Wazuh rule 100101.
# Intended only for an isolated Windows SOC lab VM.
$command = 'Write-Output "SOC-LAB-ENCODED-TEST"'
$encoded = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($command))
Start-Process powershell.exe -ArgumentList "-NoProfile -EncodedCommand $encoded" -Wait -NoNewWindow
