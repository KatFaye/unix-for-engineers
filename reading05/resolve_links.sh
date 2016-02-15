#!/bin/bash
#prints where symbolic link resolves to

echo $@ links to $(readlink $@)
