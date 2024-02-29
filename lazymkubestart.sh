#!/bin/bash
minikube start --mount --mount-string=${HOME}/Works/github/test-hasura:/hosthome --driver=docker