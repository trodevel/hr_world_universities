#!/bin/bash

checkout()
{
    local repo=$1
    local dir=$2
    local branch=$3

    [[ -z $dir ]] && dir=$( echo "$repo" | sed "s~.*/\([a-zA-Z0-9_\-]*\)~externals/\1~") #"

    if [[ ! -d $dir ]]
    then
        git clone $repo $dir
        if [[ -n $branch ]]
        then
            cd $dir; git checkout $branch; cd - >/dev/null;
        fi
    else
        echo "$dir"
        cd $dir; git pull; cd - >/dev/null;
    fi
}

checkout git@github.com:trodevel/world-universities-csv    ""
