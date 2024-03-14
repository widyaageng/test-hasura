#!/bin/bash
minikube start --mount --mount-string=${HOME}/works/github/hasura:/hosthome --driver=docker