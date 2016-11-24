#!/bin/bash

arm-linux-gnueabihf-as -mcpu=arm926ej-s test.S -o test.o
arm-linux-gnueabihf-objcopy -O binary -S test.o test.bin
arm-linux-gnueabihf-objdump -d test.o
