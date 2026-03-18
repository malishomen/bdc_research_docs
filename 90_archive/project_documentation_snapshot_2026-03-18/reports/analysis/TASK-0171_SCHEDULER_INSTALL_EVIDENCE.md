# TASK-0171 Scheduler Install Evidence

- ts_utc: 2026-02-18T00:07:18Z
- task_name: BDC_HIVE_DB_BACKUP_30MIN
- interval_minutes: 30
- git_commit: cca3918
- action: "pwsh.exe -NoProfile -ExecutionPolicy Bypass -File "D:\projects\Bio_Digital_Core\Bio_digital_core\tools\hive_core_mvp\tools\backup\hive_backup.ps1""
- guidance: configured under SYSTEM account (runs whether user is logged on or not).

## schtasks /Create output
```text
SUCCESS: The scheduled task "BDC_HIVE_DB_BACKUP_30MIN" has successfully been created.
```

## schtasks /Query output
```text
Folder: \
HostName:                             WIN-JTSARSVBH32
TaskName:                             \BDC_HIVE_DB_BACKUP_30MIN
Next Run Time:                        18.02.2026 5:37:00
Status:                               Ready
Logon Mode:                           Interactive/Background
Last Run Time:                        30.11.1999 0:00:00
Last Result:                          267011
Author:                               WIN-JTSARSVBH32\user
Task To Run:                          pwsh.exe -NoProfile -ExecutionPolicy Bypass -File "D:\projects\Bio_Digital_Core\Bio_digital_core\tools\hive_core_mvp\tools\backup\hive_backup.ps1"
Start In:                             N/A
Comment:                              N/A
Scheduled Task State:                 Enabled
Idle Time:                            Disabled
Power Management:                     Stop On Battery Mode, No Start On Batteries
Run As User:                          СИСТЕМА
Delete Task If Not Rescheduled:       Disabled
Stop Task If Runs X Hours and X Mins: 72:00:00
Schedule:                             Scheduling data is not available in this format.
Schedule Type:                        One Time Only, Minute 
Start Time:                           5:07:00
Start Date:                           18.02.2026
End Date:                             N/A
Days:                                 N/A
Months:                               N/A
Repeat: Every:                        0 Hour(s), 30 Minute(s)
Repeat: Until: Time:                  None
Repeat: Until: Duration:              Disabled
Repeat: Stop If Still Running:        Disabled
```
