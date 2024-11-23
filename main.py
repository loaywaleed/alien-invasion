#!/usr/bin/env python3
"""
Game entry point
"""
from core.alien_invasion import MilleniumFalcon


def main():
    """Main function"""
    game = MilleniumFalcon()
    game.run_game()


if __name__ == '__main__':
    main()
