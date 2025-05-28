#!/usr/bin/env python3

import subprocess
import os
import sys
from pathlib import Path
from loguru import logger

try:
    from wand.image import Image
except ImportError:
    logger.error("Wand library not found. Please install it with: pip install Wand")
    sys.exit(1)

# Get the directory where the script is located
SCRIPT_DIR = Path(__file__).parent.absolute()

# List of all available expansions
expansions = [
    ("adventures", "adventures"),
    ("alchemy", "alchemy"),
    ("allies", "allies"),
    ("base", "base"),
    ("cornucopiaAndGuilds2ndEdition", "cornucopiaAndGuilds2"),
    ("dark ages", "dark ages"),
    ("dominion2ndEdition", "dominion2"),
    ("empires", "empires"),
    ("extras", "extras"),
    ("hinterlands2ndEdition", "hinterlands2"),
    ("intrigue2ndEdition", "intrigue2"),
    ("menagerie", "menagerie"),
    ("nocturne", "nocturne"),
    ("plunder", "plunder"),
    ("promo", "promo"),
    ("prosperity2ndEdition", "prosperity2"),
    ("renaissance", "renaissance"),
    ("risingSun", "risingSun"),
    ("seaside2ndEdition", "seaside2"),
]

def checkRequirements():
    """Check if all requirements are met"""
    # Check if dominion_dividers is installed
    try:
        subprocess.run(["dominion_dividers", "--help"], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE, 
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.error("dominion_dividers command not found. Please install it first.")
        sys.exit(1)

    # Check if config file exists
    configPath = SCRIPT_DIR / "src" / "config.txt"
    if not configPath.exists():
        logger.error(f"Config file not found at {configPath}")
        logger.error("Please make sure the config file exists in the src directory.")
        sys.exit(1)

def generateDividers(expansion, name):
    """Generate dividers for a single expansion"""
    outputFile = f"{name}.pdf"
    logger.info(f"Generating dividers for {name}...")
    
    try:
        # Run the dominion_dividers command with the config file and expansion
        subprocess.run([
            "dominion_dividers",
            "-c", str(SCRIPT_DIR / "src" / "config.txt"),
            "--outfile", outputFile,
            "--expansion", expansion,
            "--font-dir", str(SCRIPT_DIR / "src" / "minion-pro")
        ], check=True)
        logger.success(f"Successfully generated {outputFile}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Error generating dividers for {name}: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error for {name}: {e}")
        return False

def convertPdfToJpg(pdfPath, outputBaseDir):
    """Convert a PDF file to JPG images and organize them into odd/even folders."""
    try:
        # Get the name without extension
        name = Path(pdfPath).stem
        logger.info(f"Processing PDF: {name}")
        
        # Create output directories
        oddDir = Path(outputBaseDir) / name / "odd"
        evenDir = Path(outputBaseDir) / name / "even"
        oddDir.mkdir(parents=True, exist_ok=True)
        evenDir.mkdir(parents=True, exist_ok=True)
        
        # Convert PDF to JPG
        with Image(filename=pdfPath, resolution=300) as pdf:
            totalPages = len(pdf.sequence)
            logger.info(f"Found {totalPages} pages in {name}")
            
            for i, page in enumerate(pdf.sequence):
                # Create a new image for each page
                with Image(page) as img:
                    # Convert to RGB if needed
                    if img.alpha_channel:
                        img.alpha_channel = 'remove'
                    
                    # Determine if page is odd or even (1-based index)
                    isOdd = (i + 1) % 2 == 1
                    targetDir = oddDir if isOdd else evenDir
                    
                    # Save with sequential numbering
                    pageNum = (i + 1) // 2 + 1 if isOdd else (i + 1) // 2
                    oddString = "odd" if isOdd else "even"
                    outputPath = targetDir / f"{name}-{oddString}-{pageNum:03d}.jpg"
                    
                    # Save with high quality
                    img.compression_quality = 95
                    img.save(filename=str(outputPath))
                    logger.debug(f"Saved page {i+1} to {outputPath}")
        
        logger.success(f"Successfully processed {name}")
        return True
        
    except Exception as e:
        logger.error(f"Error processing {pdfPath}: {str(e)}")
        return False

def processAllPdfs(inputDir, outputDir):
    """Process all PDF files in the input directory."""
    inputPath = Path(inputDir)
    if not inputPath.exists():
        logger.error(f"Input directory not found: {inputDir}")
        return False
        
    pdfFiles = list(inputPath.glob("*.pdf"))
    if not pdfFiles:
        logger.error(f"No PDF files found in {inputDir}")
        return False
        
    logger.info(f"Found {len(pdfFiles)} PDF files to process")
    
    successCount = 0
    for pdfFile in pdfFiles:
        if convertPdfToJpg(str(pdfFile), outputDir):
            successCount += 1
            
    logger.info(f"Processed {successCount} out of {len(pdfFiles)} files successfully")
    return successCount == len(pdfFiles)

def main():
    # Configure logging
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    
    # Check requirements first
    checkRequirements()
    
    # Create output directories
    outputDir = SCRIPT_DIR / "src" / "output_group_special"
    outputSplitDir = SCRIPT_DIR / "src" / "output_split_2"
    outputDir.mkdir(parents=True, exist_ok=True)
    outputSplitDir.mkdir(parents=True, exist_ok=True)
    
    # Change to output directory
    os.chdir(outputDir)
    
    # Generate dividers for each expansion
    successCount = 0
    for expansion, name in expansions:
        if generateDividers(expansion, name):
            successCount += 1
    
    logger.info(f"Generated {successCount} out of {len(expansions)} expansions successfully")
    
    # Convert PDFs to JPGs
    if not processAllPdfs(outputDir, outputSplitDir):
        logger.error("Failed to process all PDFs")
        sys.exit(1)
    
    logger.success("All operations completed successfully!")

if __name__ == "__main__":
    main() 