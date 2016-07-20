for f in *.i; do
	../../SLSparser.py "-c" "$f" "-o" "$f.out"
done