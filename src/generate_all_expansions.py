#!/usr/bin/env python3

import subprocess
import os
import sys
from pathlib import Path

# Get the directory where the script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

# List of all available expansions
expansions = [
    "adventures",
    "alchemy",
    "allies",
    "base",
    "cornucopiaAndGuilds2ndEdition",
    "dark ages",
    "dominion2ndEdition",
    "empires",
    "extras",
    "hinterlands2ndEdition",
    "intrigue2ndEdition",
    "menagerie",
    "nocturne",
    "plunder",
    "promo",
    "prosperity2ndEdition",
    "renaissance",
    "risingSun",
    "seaside2ndEdition",
]

def check_requirements():
    """Check if all requirements are met"""
    # Check if dominion_dividers is installed
    try:
        subprocess.run(["dominion_dividers", "--help"], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE, 
                      check=True)
    except subprocess.CalledProcessError:
        print("Error: dominion_dividers command not found. Please install it first.")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: dominion_dividers command not found. Please install it first.")
        sys.exit(1)

    # Check if config file exists
    config_path = SCRIPT_DIR / "config.txt"
    if not config_path.exists():
        print(f"Error: Config file not found at {config_path}")
        print("Please make sure the config file exists in the src directory.")
        sys.exit(1)

def generateDividers(expansion):
    """Generate dividers for a single expansion"""
    outputFile = f"{expansion}.pdf"
    print(f"Generating dividers for {expansion}...")
    
    try:
        # Run the dominion_dividers command with the config file and expansion
        subprocess.run([
            "dominion_dividers",
            "-c", str(SCRIPT_DIR / "config.txt"),
            "--outfile", outputFile,
            "--expansion", expansion,
            "--font-dir", str(SCRIPT_DIR / "minion-pro")
        ], check=True)
        print(f"Successfully generated {outputFile}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating dividers for {expansion}: {e}")
    except Exception as e:
        print(f"Unexpected error for {expansion}: {e}")

def main():
    # Check requirements first
    check_requirements()
    
    # Create output directory if it doesn't exist
    output_dir = SCRIPT_DIR / "output"
    if not output_dir.exists():
        output_dir.mkdir()
    
    # Change to output directory
    os.chdir(output_dir)
    
    # Generate dividers for each expansion
    for expansion in expansions:
        generateDividers(expansion)
    
    print("\nAll expansions processed!")

if __name__ == "__main__":
    main() 