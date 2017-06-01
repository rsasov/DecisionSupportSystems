#!/usr/bin/bash
filename="$1"
i=1
while IFS='' read -r line || [[ -n "$line" ]]
do
    name="$line"
    echo "$name" > "./data/$1/file$i"
    i=$((i+1))
done < "$filename"