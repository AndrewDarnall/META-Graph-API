#!/bin/bash

echo "Enter the access token generated from the Meta For Devs portal: "
read token
curl --request GET https://graph.facebook.com/v15.0/me?access_token=$token
echo ""