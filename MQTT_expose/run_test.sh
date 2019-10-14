#!/bin/bash

sshpass -f paswd parallel-ssh -h pssh-hosts -A -I < pssh-commands
