
install:
	sudo cp -a ../binedit /opt
	sudo ln -s /opt/binedit/src/binedit.py /usr/local/bin/binedit
	sudo ln -s /opt/binedit/scripts/binedit_* /usr/local/bin/

uninstall:
	sudo rm -f /usr/local/bin/binedit
	sudo rm -f /usr/local/bin/binedit_*
	sudo rm -rf /opt/binedit
