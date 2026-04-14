#!/bin/bash

# symc-machiroku.sh - Git + Hugo + Deploy per a machiroku-web
#
# Entorns Hugo:
#   development  → config/development/hugo.toml  → http://localhost:1313/
#   staging      → config/staging/hugo.toml      → https://112books.github.io/machiroku-web/
#   production   → config/production/hugo.toml   → https://machiroku.com/

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

# Servidor local (development)
do_server() {
    print_message "Servidor local → http://localhost:1313/"
    print_message "Entorn: development (config/development/hugo.toml)"
    echo ""
    hugo server --environment development
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

# Deploy a GitHub Pages (staging)
do_deploy() {
    print_message "Deploy a GitHub Pages (staging)"
    print_message "Entorn: staging (config/staging/hugo.toml)"
    print_message "URL destí: https://112books.github.io/machiroku-web/"
    echo ""

    hugo --environment staging --destination $BUILD_DIR || exit 1
    print_success "Build completat a /$BUILD_DIR"

    do_sync
    print_success "Deploy completat → https://112books.github.io/machiroku-web/"
}

# Publish al servidor real de producció
do_publish() {
    print_warning "Publicació de producció no configurada encara."
    print_message "Entorn previst: production (config/production/hugo.toml)"
    print_message "URL destí: https://machiroku.com/"
    print_message "Edita symc-machiroku.sh i descomenta la secció SSH per activar-la."

    # Quan estigui configurat, descomentar:
    # SSH_KEY="$HOME/.ssh/machiroku_deploy"
    # SSH_USER="usuari"
    # SSH_HOST="servidor.com"
    # SSH_PATH="www"
    #
    # print_message "Build Hugo producció..."
    # hugo --minify --environment production --destination $BUILD_DIR || exit 1
    #
    # print_message "Enviant fitxers via rsync..."
    # rsync -avz --delete --checksum \
    #     --exclude='.DS_Store' \
    #     -e "ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no" \
    #     ${BUILD_DIR}/ ${SSH_USER}@${SSH_HOST}:${SSH_PATH}/
    #
    # print_success "Web publicada a https://machiroku.com/"
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
    echo "1) Status    → Veure estat del repositori"
    echo "2) Server    → Servidor local  [development → localhost:1313]"
    echo "3) Pull      → Descarregar canvis de GitHub"
    echo "4) Push      → Pujar canvis locals a GitHub"
    echo "5) Deploy    → Build + publicar a GitHub Pages  [staging]"
    echo "6) Publish   → Publicar al servidor real  [production — pendent]"
    echo "7) Force     → Forçar push (perillós)"
    echo "0) Sortir"
    echo ""

    read -p "Opció: " opt
    echo ""

    case $opt in
        1) show_status ;;
        2) do_server ;;
        3) do_pull ;;
        4) do_sync ;;
        5) do_deploy ;;
        6) do_publish ;;
        7)
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
        server)  do_server ;;
        pull)    do_pull ;;
        push)    do_sync ;;
        deploy)  do_deploy ;;
        publish) do_publish ;;
        force)   do_force ;;
        *)
            print_error "Opció desconeguda: $1"
            echo "Ús: ./symc-machiroku.sh {status|server|pull|push|deploy|publish|force}"
            exit 1
            ;;
    esac
fi

print_message "Fi del procés"
