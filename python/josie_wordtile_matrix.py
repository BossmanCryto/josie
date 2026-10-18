#!/data/data/com.termux/files/usr/bin/python3
"""
JOSIE Compatibility Bridge: Word Tile -> QS Tile Matrix
Forwards legacy word tile calls to josie_qs_tile_matrix.py
"""
import sys
from josie_qs_tile_matrix import main

if __name__ == "__main__":
    main()
