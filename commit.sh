#!/bin/bash
set -e
cd /home/lubuntu/harold-ai-pool
git add -A
git commit -q -m "Add simple extensions system for VS Code plug-ins"
git push origin master 2>&1
echo "EXIT_OK"