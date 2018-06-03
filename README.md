# pidisplay

## Before installation

1. Install development dependencies:

	* ansible
	* make

2. Create `hosts.ini` file and populate it with the IP addresses of the target hosts (raspberry pis) - check `hosts.ini.example` for the correct format.
3. Make sure you can ssh to every target host without password - you can specify the ssh user in the `hosts.ini` file (by default "pi").

## Install

This installs the program on every target host.
```
make deploy
```

## Test

This runs the main script on every target host.
```
make run
```
