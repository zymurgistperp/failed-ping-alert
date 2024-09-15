#!/bin/bash



pingfail=0

pingcount=0

successful_pings=0

echo "Enter the IP address to ping:"

read target



if [ -z "$target" ]; then

    echo "No IP address provided. Exiting..."

    exit 1

fi



while [ "$pingfail" -eq 0 ]; do

    ((pingcount++))

    ping -c 1 "$target" &> /dev/null # Suppress ping output

    if [ $? -ne 0 ]; then # Check if ping failed (exit status != 0)

        echo -ne "Ping $pingcount failed to $target\r"

        echo -e '\a' # Print alert sound

    else

        ((successful_pings++))

        percentage=$(awk "BEGIN {printf \"%.2f\", $successful_pings / $pingcount * 100}")

        echo -e "Ping $pingcount succeeded to $target (${percentage}%)\r"

    fi

    sleep 2

done
