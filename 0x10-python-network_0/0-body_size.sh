#!/bin/bash
# Get the size of the body of the curl response
curl -sI $1 | grep 'Content-Length' | cut -d: -f2- | cut -c2-
