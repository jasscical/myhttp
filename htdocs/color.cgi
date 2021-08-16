#!/bin/bash
read -n $CONTENT_LENGTH key_value  # color=xxx
array=(${key_value//=/ })

echo "Content-Type: text/html"
echo
echo "<!doctype html>"
echo "<html>"
echo "<head><title>${array[1]}</title></head>"
echo "<body style=\"background-color:${array[1]};\" ><h1>this is ${array[1]}</h1></body>"
echo "</html>"