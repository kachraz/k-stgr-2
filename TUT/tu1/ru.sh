#!/usr/bin/env bash
set -euo pipefail

################################################
# Commands for running the streamlit application
################################################

# Colors
RE='\e[0;31m'
GR='\e[0;32m'
BL='\e[0;34m'
YL='\e[0;33m'
NC='\e[0m'

# Variables
c_d=$(date)

# Commands
b1() {
    clear
    echo -e "${BL} $c_d"
    echo -e "┌──────────────────────────────────────┐"
    echo -e "│   ┌──────────────────────────────┐   │"
    echo -e "│   │   Install pks and execute    │   │"
    echo -e "│   │   streamlit application      │   │"
    echo -e "│   └──────────────────────────────┘   │"
    echo -e "└──────────────────────────────────────┘"
    echo -e "${NC}"
}

c1() {
    echo -e ""
    echo -e "Instllation scripts"
    echo -e "${GR}uv add streamlit pandas matplotlib rich${NC}"
    echo -e "${GR}uvx streamlit run panty.py${NC}"
    echo -e "Executing...."
    uv add streamlit pandas matplotlib rich
    uv tree
    uvx streamlit run panty.py
}

# Execution sequence
b1
c1
