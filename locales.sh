#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Extracting messages..."
    pybabel extract -F babel.cfg -o messages.pot .

    echo "Initializing translations for English..."
    pybabel init -i messages.pot -d locales -l en

    echo "Initializing translations for Ukrainian..."
    pybabel init -i messages.pot -d locales -l uk

    echo "Removing temporary messages.pot file..."
    rm messages.pot

else
    if [ "$1" == "compile" ]; then
        echo "Compiling translations..."
        pybabel compile -d locales
    else
        echo "Invalid argument. Use no argument for extraction and initialization, or 'compile' to compile translations."
        exit 1
    fi
fi
