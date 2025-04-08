while ($true) {
    net use \\<VM-IP>\IPC$ /user:test wrongpass
    Start-Sleep -Seconds 1
}