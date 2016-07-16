all: helper ia64 virt

helper:
	cc -O2 -o virt-what-cpuid-helper virt-what-cpuid-helper.c
	strip virt-what-cpuid-helper

ia64:
	arch=$(uname -p | sed -e 's/i.86/i386/' | sed -e 's/arm.*/arm/')
       [ "$arch" = "ia64" ] && \
	cc -O2 -o virt-what-ia64-xen-rdtsc-test virt-what-ia64-xen-rdtsc-test.c && \
	strip virt-what-ia64-xen-rdtsc-test

virt:
	chmod +x virt-what

clean:
	rm -f virt-what-cpuid-helper virt-what-ia64-xen-rdtsc-test

.PHONY: all clean
