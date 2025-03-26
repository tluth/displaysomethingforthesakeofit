install:
	./scripts/setup.sh

start:
	systemctl start co2-monitor

stop:
	systemctl stop co2-monitor

status:
	./scripts/check_status.sh

enable:
	systemctl enable co2-monitor