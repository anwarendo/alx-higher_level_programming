#!/bin/bash
curl -sI $1 | grep 'Content-Length' | cut -d: -f2- | cut -c2-

