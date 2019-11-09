#!/bin/bash
cd /home/pi/git_code
tmux kill-session -t test
tmux new-session -d -s test 'python3 test_text_buffer.py'
