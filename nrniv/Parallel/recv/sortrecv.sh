#!/usr/bin/env sh
sort -k 1n,1n -k 2n,2n -k 3n,3n "$1" > "$2"
