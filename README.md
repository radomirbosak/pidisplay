# pidisplay



## Before installation

1. Create `hosts.ini` file and populate it with the IP addresses of the target hosts (raspberry pis) - check `hosts.ini.example` for the correct format.
2. Make sure you can ssh to every target host without password - you can specify the ssh user in the `hosts.ini` file (by default "pi").

## Install

This installs the program on every target host.
```
make deploy
```

## Test

This runs the test example on every target host.
```
make run
```
