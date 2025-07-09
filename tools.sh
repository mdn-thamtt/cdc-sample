#!/bin/bash

ORANGE='\033[0;33m'
GREEN='\033[1;32m'
NC='\033[0m'

main() {
  pre_run $1
  docker compose -f $1.docker-compose.yaml ${@:2}
}

pre_run() {
  if [ ! -f "$1.docker-compose.yaml" ]; then
    _die "$1.docker-compose.yaml not found!"
  fi

  if [ ! -x "$(command -v docker)" ]; then
    _die "docker is not installed!"
  fi

  export_env
}

_die() {
  _warn "$1"
  exit 1
}

_print() {
  if [ $# -eq 1 ]
  then
    echo -e "${GREEN}$1${NC}"
  else
    echo -e -n "${GREEN}$1${NC} "
  fi
}

_warn() {
  if [ $# -eq 1 ]
  then
    echo -e "${ORANGE}$1${NC}"
  else
    echo -e -n "${ORANGE}$1${NC} "
  fi
}

export_env() {
  if [ ! -f ".env" ]; then
    _die "[.env] file not found!"
  fi
  export $(grep -v '^#' .env | xargs)
}

main $@
