@echo off
sed -n "s/^\([a-z]*\) N:.*$/\1/p" 2of12id.txt > noun.txt
sed -n "s/^\([a-z]*[^y]\) A:.*$/\1/p" 2of12id.txt > adj.txt
