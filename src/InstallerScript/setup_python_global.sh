#!/bin/bash

# Funzione log con colori
info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
warn() { echo -e "\033[1;33m[WARN]\033[0m $1"; }
ok()   { echo -e "\033[1;32m[DONE]\033[0m $1"; }
err()  { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# Trova automaticamente l’ultima versione stabile disponibile su pyenv
PY_VERSION=$(pyenv install -l | grep -E "^\s*[0-9]+\.[0-9]+\.[0-9]+$" | tr -d ' ' | tail -1)
info "L'ultima versione stabile di Python trovata è: $PY_VERSION"

# 1. Verifica se pyenv è installato
if ! command -v pyenv &> /dev/null; then
    info "pyenv non trovato. Lo installo..."
    curl https://pyenv.run | bash

    # Aggiunge a .bashrc se non già presente
    if ! grep -q 'pyenv init' ~/.bashrc; then
        info "Configuro pyenv nel ~/.bashrc..."
        cat <<EOF >> ~/.bashrc

# >>> pyenv setup >>>
export PATH="\$HOME/.pyenv/bin:\$PATH"
eval "\$(pyenv init --path)"
eval "\$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
# <<< pyenv setup <<<
EOF
        source ~/.bashrc
    fi

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
else
    ok "pyenv già installato."
fi

# 2. Installa Python 3.14.0 se non presente
if pyenv versions --bare | grep -q "^$PY_VERSION$"; then
    ok "Python $PY_VERSION già installato."
else
    info "Installo Python $PY_VERSION..."
    pyenv install "$PY_VERSION" || { err "Installazione fallita"; exit 1; }
fi

# 3. Imposta come globale
pyenv global "$PY_VERSION"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# 4. Verifica pip
if ! command -v pip &> /dev/null; then
    info "pip non trovato. Lo installo..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py && rm get-pip.py
else
    ok "pip già presente."
fi

# 5. Librerie da installare
REQUIRED_PKGS=(
    ipython notebook numpy pandas matplotlib seaborn scipy
    scikit-learn statsmodels beautifulsoup4 lxml openpyxl
    jupyterlab plotly tqdm requests pydantic tabulate
)

info "Controllo e installo solo le librerie mancanti..."

for pkg in "${REQUIRED_PKGS[@]}"; do
    if python -m pip show "$pkg" &> /dev/null; then
        ok "$pkg già installato"
    else
        info "Installo $pkg..."
        pip install "$pkg"
    fi
done

# 6. Riassunto
ok "Python: $(python --version)"
ok "pip: $(pip --version)"
info "Librerie installate:"
pip list

ok "Setup completato!"

# Istruzioni d'uso:

    #Se sei un MacOS user devi installare Homebrew prima:  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    # Ora puoi installare le librerie: brew install openssl readline sqlite3 xz zlib bzip2

    #chmod +x setup_python_global.sh && ./setup_python_global.sh
    #Dopo questo, il tuo script funziona anche su macOS
#---------------------------------------------------------------------------------------------------------------------------------------------------------
    #Salvare questo script come "setup_python_global.sh"
    
    #Serve per poterlo lanciare come programma "chmod +x ~/setup_python_global.sh"
    #Esegui lo script "./setup_python_global.sh"
    
# Fine