#!/usr/bin/env bash
# Visonic Themes for Typora - macOS / Linux Installer
# https://github.com/YXX168/Visonic-Themes

set -e

echo "============================================"
echo "    Visonic Themes for Typora Installer"
echo "============================================"
echo

# Detect Operating System
OS_TYPE="$(uname -s)"
case "${OS_TYPE}" in
    Darwin*)
        THEME_DIR="${HOME}/Library/Application Support/abnerworks.Typora/themes"
        ;;
    Linux*)
        THEME_DIR="${HOME}/.config/Typora/themes"
        ;;
    *)
        echo "[ERROR] Unsupported operating system: ${OS_TYPE}"
        echo "Please install themes manually following README.md."
        exit 1
        ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="${SCRIPT_DIR}/themes"
[ ! -d "${SOURCE_DIR}" ] && SOURCE_DIR="${SCRIPT_DIR}"

# Ensure Typora theme directory exists
if [ ! -d "${THEME_DIR}" ]; then
    echo "[INFO] Creating Typora theme directory: ${THEME_DIR}"
    mkdir -p "${THEME_DIR}"
fi

echo "[1/3] Installing font assets (visonic-fonts)..."
if [ -d "${SCRIPT_DIR}/visonic-fonts" ]; then
    mkdir -p "${THEME_DIR}/visonic-fonts"
    cp -R "${SCRIPT_DIR}/visonic-fonts/"* "${THEME_DIR}/visonic-fonts/"
    echo "      [OK] Font assets installed"
else
    echo "      [WARN] visonic-fonts folder not found. Egoism themes might require font assets."
fi

echo
echo "[2/3] Installing theme files..."
COUNT=0
for f in "${SOURCE_DIR}"/visonic-*.css; do
    if [ -f "$f" ]; then
        cp -f "$f" "${THEME_DIR}/"
        COUNT=$((COUNT + 1))
    fi
done
echo "      [OK] Installed ${COUNT} Visonic theme files to ${THEME_DIR}"

echo
echo "[3/3] Setting default theme bridge (github.user.css)..."
DEFAULT_THEME="visonic-streamer-nebula"
DEFAULT_BRIDGE="${THEME_DIR}/github.user.css"
if [ -f "${THEME_DIR}/${DEFAULT_THEME}.css" ]; then
    if [ -f "${DEFAULT_BRIDGE}" ]; then
        cp -f "${DEFAULT_BRIDGE}" "${DEFAULT_BRIDGE}.bak"
    fi
    cat <<EOF > "${DEFAULT_BRIDGE}"
/* Visonic Themes auto default bridge. Delete this file to restore Typora GitHub default style. */
@import url("./${DEFAULT_THEME}.css");
EOF
    echo "      [OK] Default bridge created -> ${DEFAULT_THEME}"
    echo "           (Typora will automatically display ${DEFAULT_THEME} under GitHub theme)"
fi

echo
echo "============================================"
echo "           Installation completed!"
echo "============================================"
echo "Themes installed to: ${THEME_DIR}"
echo "Please restart Typora to apply changes."
echo
