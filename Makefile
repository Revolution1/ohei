all: dmidecode virt-what

dmidecode:
	make -C ohei/utils/dmidecode

virt-what:
	make -C ohei/utils/virt-what

clean:
	make -C ohei/utils/dmidecode clean
	make -C ohei/utils/virt-what clean

.PHONY all clean