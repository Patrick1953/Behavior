#!/bin/bash
######################################################################
#    ___ _                              __            _            
#   / __\ |__   ___ _ __ _ __ _   _    /__\ __   __ _(_)_ __   ___ 
#  / /  | '_ \ / _ \ '__| '__| | | |  /_\| '_ \ / _` | | '_ \ / _ \
# / /___| | | |  __/ |  | |  | |_| | //__| | | | (_| | | | | |  __/
# \____/|_| |_|\___|_|  |_|   \__, | \__/|_| |_|\__, |_|_| |_|\___|
#                             |___/             |___/              
######################################################################

# Check environment
######################################################################

function display(){
    if [ "$#" -ne 3 ]; then echo "Usage display <text> <True/False> <status>"; fi
    str="$1"
    status=""
    while [ ${#str} -ne 63 ]; do str=$str"."; done
    if [ $2 == "True" ]; then status=$status"[ $(tput bold && tput setaf 2)"; else status=$status"[ $(tput bold && tput setaf 9)"; fi
    status=$status$3

    while [ ${#status} -ne 15 ]; do status=$status'£'; done 
    status=$status"$(tput sgr0)]"
    echo $str$status | tr '£' ' '
}

function create_network(){
    network=$1
    if docker network ls | grep $network >/dev/null 2>&1; then
        display "Checking if $network exist " "True" "YES"
        if docker network rm $network >/dev/null 2>&1; then
            display "Delete $network " "True" "OK"
        else
            display "Delete $network " "False" "KO"
            exit 1
        fi
    else
        display "Checking if $network exist " "False" "NO"
    fi
    if docker network create --driver=bridge --subnet=172.28.0.0/16 $network >/dev/null 2>&1; then
        display "Create $network " "True" "OK"
    else
        display "Create $network " "False" "KO"
    fi

}

function pull_image(){ 
    image=$1
    tag=$2
    # If container running stop it
    if  docker images | grep $image >/dev/null 2>&1; then
        display "Checking if $image exist " "True" "YES"
        if docker rmi $image >/dev/null 2>&1; then
            display "Delete $image " "True" "OK"
        else
            display "Delete $image " "False" "KO"
            exit 1
        fi
    else
        display "Checking if $image exist " "False" "NO"
    fi
    if docker pull $image >/dev/null 2>&1; then
        display "Pull $image " "True" "OK"
        if docker tag $image $tag>/dev/null 2>&1; then
            display "Tag $image $tag" "True" "OK"
        else
            display "Tag $image $tag" "False" "KO"
        fi
    else
        display "Pull $image " "False" "KO"
    fi
}

function build_image(){ 
	image=$1
    cd $image
	# If container running stop it
	if  docker images $image | grep $image >/dev/null 2>&1; then
        display "Checking if $image exist " "True" "YES"
        if docker rmi $image >/dev/null 2>&1; then
        	display "Delete $image " "True" "OK"
        else
        	display "Delete $image " "False" "KO"
        	exit 1
        fi
    else
        display "Checking if $image exist " "False" "NO"
    fi
    if docker build --tag $image . >/dev/null 2>&1; then
    	display "Build $image " "True" "OK"
    else
    	display "Build $image " "False" "KO"
    fi
    cd ..
}

function remove_container(){

	container=$1
	# If container running stop it
	if  docker ps | grep $container >/dev/null 2>&1; then
        display "Checking if $container is running " "True" "YES"
        if docker stop $container >/dev/null 2>&1; then
        	display "Stop running $container " "True" "OK"
            if docker rm $container >/dev/null 2>&1; then
                display "Delete $container " "True" "OK"
            else
                display "Delete $container " "False" "KO"
                exit 1
            fi
        else
        	display "Stop running $container " "False" "KO"
        	exit 1
        fi
    else
	    display "Checking if $container is running " "False" "NO"
        # If container exist delete it
        if  docker ps -a | grep $container >/dev/null 2>&1; then
            display "Checking if $container exist " "True" "YES"
            if docker rm $container >/dev/null 2>&1; then
                display "Delete $container " "True" "OK"
            else
                display "Delete $container " "False" "KO"
                exit 1
            fi
        else
            display "Checking if $container exist " "False" "NO"
        fi
	fi
}

function run_container(){
	container=$1
	port=$2
    ip=$3
	if docker run --name $container -d -p $port:$port --network cherry-network --ip $ip $container >/dev/null 2>&1; then
		display "Running $container " "True" "OK"	
    else
    	display "Running $container " "False" "KO"
    fi
}

clear

echo "######################################################################"
echo "#    ___ _                              __            _              #"
echo "#   / __\ |__   ___ _ __ _ __ _   _    /__\ __   __ _(_)_ __   ___   #"
echo "#  / /  | '_ \ / _ \ '__| '__| | | |  /_\| '_ \ / _\` | | '_ \ / _ \  #"
echo "# / /___| | | |  __/ |  | |  | |_| | //__| | | | (_| | | | | |  __/  #"
echo "# \____/|_| |_|\___|_|  |_|   \__, | \__/|_| |_|\__, |_|_| |_|\___|  #"
echo "#                             |___/             |___/                #"
echo "######################################################################"
echo "Version 1.0.0"
echo ""
echo "Check pre-requisites" 
echo "----------------------------------------------------------------------"

# Check if docker exist
if ![ command -v docker &> /dev/null ] ;  then
	display "Checking docker " "False" "NO"
    exit 1
else
	display "Checking docker " "True" "YES"
fi	

# Check if docker is running
if ! docker info >/dev/null 2>&1; then
    display "Checking docker running " "False" "NO"
    exit 1
else
	display "Checking docker running " "True" "YES"
fi

echo ""
echo "Stop Containers  " 
echo "----------------------------------------------------------------------"
remove_container cherry-engine-master
remove_container cherry-engine-worker
remove_container cherry-engine-mqtt
echo ""
echo "Network " 
echo "----------------------------------------------------------------------"
create_network cherry-network
echo ""
echo "Images" 
echo "----------------------------------------------------------------------"
build_image cherry-engine-mqtt
build_image cherry-engine
build_image cherry-engine-master
build_image cherry-engine-worker
echo ""
echo "Start containers  " 
echo "----------------------------------------------------------------------"
run_container cherry-engine-mqtt   1883 172.28.0.10 
run_container cherry-engine-master 3000 172.28.0.11
run_container cherry-engine-worker 4000 172.28.0.12

