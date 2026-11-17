# Benign negative test; expected not to match encoded-command rule 100101.
Start-Process powershell.exe -ArgumentList '-NoProfile -Command "Write-Output SOC-LAB-NEGATIVE-TEST"' -Wait -NoNewWindow
