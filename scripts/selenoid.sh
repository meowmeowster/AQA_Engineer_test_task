#!/bin/bash
wget https://github.com/aerokube/cm/releases/download/1.8.5/cm_linux_amd64
chmod +x ./cm_linux_amd64
./cm_linux_amd64 selenoid start --vnc
