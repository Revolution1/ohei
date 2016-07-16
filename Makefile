all: dmidecode virt-what

dmidecode:
	$(MAKE) -C ohei/utils/dmidecode

virt-what:
	$(MAKE) -C ohei/utils/virt-what

clean:
	$(MAKE) -C ohei/utils/dmidecode clean
	$(MAKE) -C ohei/utils/virt-what clean

.PHONY: all clean
