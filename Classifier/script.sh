#!/usr/bin/bash
filename="$1"
i=1
while read -r line
do
    name="$line"
    touch "file$i"
done < "$filename"