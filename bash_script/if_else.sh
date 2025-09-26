#!/bin/bash
echo "insert x"
read x 

if [ $x -gt 10 ]
then 
	echo "it's expensive"
	exit 0
else 
	echo "it's cheap"
	exit 1
fi
