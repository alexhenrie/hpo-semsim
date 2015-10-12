#!/bin/sh

wget http://purl.obolibrary.org/obo/hp.obo -O hp.obo

if [ ! -d slib ]; then
    git clone https://github.com/sharispe/slib.git
    cd slib
    git am ../slib-patches/*
else
    cd slib
    git pull --rebase
fi
mvn package
cd ..
ln -sf slib/slib-tools/slib-tools-sml-toolkit/target/sml-toolkit-latest.jar sml-toolkit-latest.jar
