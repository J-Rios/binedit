
install:
	sudo cp -a ../binedit /opt
	sudo ln -s /opt/binedit/src/binedit.py /usr/local/bin/binedit

uninstall:
	sudo rm -f /usr/local/bin/binedit
	sudo rm -rf /opt/binedit
