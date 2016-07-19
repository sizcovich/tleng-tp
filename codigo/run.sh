#!/bin/bash
set -x
for f in $(*.i); do
	echo "$f"
	../../SLSparser.py "-c" "$f"
done