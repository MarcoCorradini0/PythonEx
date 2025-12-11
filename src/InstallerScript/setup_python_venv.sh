#!/bin/bash

# =======================================================
# Se prima vuoi pulire tutto fai come comando unico:
# Rimuovi pyenv e tutte le versioni di Python installate da pyenv
    #rm -rf ~/.pyenv
    #rm -rf ~/python_env
    #sed -i '/pyenv/d' ~/.bashrc
    #sed -i '/pyenv/d' ~/.zshrc
    #source ~/.bashrc
# =======================================================
# Controlla la tua versione
    #python --version      # deve dare l’ultima versione stabile installata
    #pip --version         # deve funzionare correttamente
    #source ~/python_env/bin/activate
    #python -m pip list    # controlla librerie installate
# =======================================================
# Datti permessi per lanciare lo script
    #chmod +x setup_python_venv.sh
    #./setup_python_venv.sh

# =======================================================
# Setup Python + venv usando pyenv su WSL/Linux/macOS
# =======================================================
# Questo script:
# 1) Installa dipendenze di sistema (Linux/WSL/macOS)
# 2) Installa pyenv (solo se non presente)
# 3) Installa l'ultima versione stabile di Python
# 4) Imposta Python tramite pyenv
# 5) Crea e attiva un virtualenv
# 6) Installa librerie Python comuni
# source ~/.bashrc o apri nuovo terminale per aggiornare
# =======================================================

info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
warn() { echo -e "\033[1;33m[WARN]\033[0m $1"; }
ok()   { echo -e "\033[1;32m[DONE]\033[0m $1"; }
err()  { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# ============================
# 0. Dipendenze di sistema
# ============================
if [ -x "$(command -v apt)" ]; then
    info "Installazione dipendenze di sistema WSL/Linux..."
    sudo apt update
    sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev git
elif [ -x "$(command -v brew)" ]; then
    info "Installazione dipendenze di sistema macOS..."
    brew install openssl readline sqlite3 xz zlib bzip2
fi

# ============================
# 1. Installa pyenv se manca
# ============================
if ! command -v pyenv &> /dev/null; then
    info "pyenv non trovato. Lo installo..."
    curl https://pyenv.run | bash

    # Aggiunge pyenv a ~/.bashrc se non presente
    if ! grep -q 'pyenv init' ~/.bashrc; then
        info "Configuro pyenv in ~/.bashrc..."
        cat <<EOF >> ~/.bashrc

# >>> pyenv setup >>>
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init --path)"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
# <<< pyenv setup <<<
EOF
    fi

    # Ricarica bashrc
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
else
    ok "pyenv già installato."
fi

# ============================
# 2. Trova ultima versione stabile Python
# ============================
PY_VERSION=$(pyenv install -l | grep -E "^\s*[0-9]+\.[0-9]+\.[0-9]+$" | tr -d ' ' | tail -1)
info "Ultima versione stabile di Python: $PY_VERSION"

# ============================
# 3. Installa Python se non presente
# ============================
if pyenv versions --bare | grep -q "^$PY_VERSION$"; then
    ok "Python $PY_VERSION già installato."
else
    info "Installazione Python $PY_VERSION..."
    pyenv install "$PY_VERSION" || { err "Installazione fallita"; exit 1; }
fi

# ============================
# 4. Imposta Python con pyenv
# ============================
info "Imposto Python $PY_VERSION come globale..."
pyenv global "$PY_VERSION"
export PATH="$HOME/.pyenv/shims:$PATH"
eval "$(pyenv init -)"

# ============================
# 5. Crea ambiente virtuale
# ============================
ENV_DIR="$HOME/python_env"
if [ -d "$ENV_DIR" ]; then
    ok "Ambiente virtuale già esistente in $ENV_DIR"
else
    info "Creo ambiente virtuale in $ENV_DIR..."
    python -m venv "$ENV_DIR"
fi

# ============================
# 6. Attiva venv
# ============================
source "$ENV_DIR/bin/activate"
ok "Virtualenv attivato"

# ============================
# 7. Aggiorna pip
# ============================
info "Aggiorno pip..."
python -m pip install --upgrade pip

# ============================
# 8. Installa librerie Python comuni
# ============================
REQUIRED_PKGS=(
    ipython notebook numpy pandas matplotlib seaborn scipy
    scikit-learn statsmodels beautifulsoup4 lxml openpyxl
    jupyterlab plotly tqdm requests pydantic tabulate
)
info "Installazione librerie nell'ambiente virtuale..."
for pkg in "${REQUIRED_PKGS[@]}"; do
    if python -m pip show "$pkg" &> /dev/null; then
        ok "$pkg già installato"
    else
        info "Installazione $pkg..."
        pip install "$pkg"
    fi
done

# ============================
# 9. Riassunto finale
# ============================
ok "Python: $(python --version)"
ok "pip: $(pip --version)"
info "Librerie installate:"
pip list

ok "Setup completato!"
info "Attiva venv: source ~/python_env/bin/activate"
info "Disattiva venv: deactivate"
