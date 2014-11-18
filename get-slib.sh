#!/bin/sh

if [ ! -d slib ]; then
    git clone https://github.com/sharispe/slib.git
    cd slib
    git am ../slib-patches/*
else
    cd slib
    git pull --rebase
fi
mvn package
