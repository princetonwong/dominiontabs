import os
import sys
from pathlib import Path
from loguru import logger

try:
    from wand.image import Image
except ImportError:
    logger.error("Wand library not found. Please install it with: pip install Wand")
    sys.exit(1)

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
                    pageNum = (i + 1) // 2 + 1  if isOdd else (i + 1) // 2
                    outputPath = targetDir / f"{name}-{pageNum:03d}.jpg"
                    
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

if __name__ == "__main__":
    # Configure logging
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    
    # Input directory containing PDFs
    inputDir = "src/output_group_special"
    
    # Output directory for JPGs
    outputDir = "src/output_split"
    
    # Create output directory if it doesn't exist
    Path(outputDir).mkdir(parents=True, exist_ok=True)
    
    # Process all PDFs
    if not processAllPdfs(inputDir, outputDir):
        sys.exit(1) 