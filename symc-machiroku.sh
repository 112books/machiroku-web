#!/bin/bash

# sync-web.sh - Git + Hugo + Deploy per a machiroku-web

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Configuració
BRANCH="main"
REMOTE="origin"
BUILD_DIR="docs"          # GitHub Pages llegeix /docs a main

# Servidor de producció (per configurar quan calgui)
# SSH_KEY="$HOME/.ssh/machiroku_deploy"
# SSH_USER="usuari"
# SSH_HOST="servidor.com"
# SSH_PATH="www"

# Missatges
print_message() { echo -e "${BLUE}[sync-web]${NC} $1"; }
print_success() { echo -e "${GREEN}[✓]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[!]${NC} $1"; }
print_error()   { echo -e "${RED}[✗]${NC} $1"; }

# Verificar que som dins d'un repo Git
check_git_repo() {
    if ! git rev-parse --git-dir > /dev/null 2>&1; then
        print_error "No és un repositori Git"
        exit 1
    fi
}

# Capçalera
show_header() {
    echo ""
    echo "======================================"
    echo " Projecte: $(basename $(pwd))"
    echo " Branca:   $(git branch --show-current)"
    echo "======================================"
    echo ""
}

# Estat del repo
show_status() {
    print_message "Estat del repositori"
    echo ""
    if [[ -n $(git status -s) ]]; then
        print_warning "Canvis locals:"
        git status -s
    else
        print_success "Repositori net"
    fi
    echo ""
}

# Pull
do_pull() {
    print_message "Pull..."
    git pull $REMOTE $BRANCH --rebase || exit 1
    print_success "Pull correcte"
}

# Sync: commit (si cal) + pull --rebase + push
do_sync() {
    print_message "Sincronitzant amb el remot..."

    if [[ -n $(git status -s) ]]; then
        print_warning "Canvis detectats:"
        git status -s
        echo ""
        read -p "Missatge del commit: " msg
        if [[ -z "$msg" ]]; then
            msg="update"
        fi
        git add .
        git commit -m "$msg"
    fi

    print_message "Pull --rebase..."
    if ! git pull $REMOTE $BRANCH --rebase; then
        print_error "Error en el pull --rebase. Resol els conflictes i torna a intentar-ho."
        exit 1
    fi

    print_message "Push..."
    if ! git push $REMOTE $BRANCH; then
        print_error "Error en el push."
        exit 1
    fi

    print_success "Push correcte"
}

# Deploy a GitHub Pages (build → /docs → push a main)
do_deploy() {
    print_message "Deploy a GitHub Pages"

    print_message "Build Hugo (environment: staging)..."
    hugo --environment staging --destination $BUILD_DIR || exit 1

    print_success "Build completat a /$BUILD_DIR"
    do_sync

    print_success "Deploy completat → https://112books.github.io/machiroku-web/"
}

# Publish al servidor real (per configurar quan calgui)
do_publish() {
    print_warning "Publicació al servidor extern no configurada encara."
    print_message "Edita sync-web.sh i descomenta la secció SSH per activar-la."

    # Quan estigui configurat, descomentar:
    # print_message "Build Hugo producció..."
    # hugo --minify --environment production --destination $BUILD_DIR || exit 1
    #
    # print_message "Enviant fitxers via rsync..."
    # rsync -avz --delete --checksum \
    #     --exclude='.DS_Store' \
    #     -e "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no" \
    #     ${BUILD_DIR}/ ${SSH_USER}@${SSH_HOST}:${SSH_PATH}/
    #
    # print_success "Web publicada"
}

# Force push (perillós)
do_force() {
    print_warning "Forçarà el repositori remot"
    git push $REMOTE $BRANCH --force-with-lease
    print_success "Force push completat"
}

# Menú interactiu
interactive_menu() {
    show_header
    show_status

    echo "Què vols fer?"
    echo ""
    echo "1) Status   → Veure estat del repositori"
    echo "2) Pull     → Descarregar canvis de GitHub"
    echo "3) Push     → Pujar canvis locals a GitHub"
    echo "4) Deploy   → Build + publicar a GitHub Pages"
    echo "5) Publish  → Publicar al servidor real (pendent de configurar)"
    echo "6) Force    → Forçar push (perillós)"
    echo "0) Sortir"
    echo ""

    read -p "Opció: " opt
    echo ""

    case $opt in
        1) show_status ;;
        2) do_pull ;;
        3) do_sync ;;
        4) do_deploy ;;
        5) do_publish ;;
        6)
            print_warning "Això pot trencar el repositori remot"
            read -p "Segur? (s/N): " confirm
            if [[ "$confirm" =~ ^[Ss]$ ]]; then
                do_force
            else
                print_message "Cancel·lat"
            fi
            ;;
        0)
            print_message "Sortint..."
            exit 0
            ;;
        *)
            print_error "Opció no vàlida"
            ;;
    esac
}

# Main
check_git_repo

if [ -z "$1" ]; then
    interactive_menu
else
    case $1 in
        status)  show_status ;;
        pull)    do_pull ;;
        push)    do_sync ;;
        deploy)  do_deploy ;;
        publish) do_publish ;;
        force)   do_force ;;
        *)
            print_error "Opció desconeguda: $1"
            echo "Ús: ./sync-web.sh {status|pull|push|deploy|publish|force}"
            exit 1
            ;;
    esac
fi

print_message "Fi del procés"