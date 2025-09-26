#!/bin/bash

devide=$(($1/$2| bc))
multiple=$(($1*$2))
add=$(($1+$2))

echo "the devided between a and b are $devide,the multiple between a and b are $multiple and adding a and b are $add "
