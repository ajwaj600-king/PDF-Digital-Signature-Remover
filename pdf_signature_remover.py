import os
import time
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import io

# ===== KONFIGURACJA =====
# Ustaw poniższe ścieżki do swoich folderów
input_folder = r"C:\path\to\input\folder"
output_folder = r"C:\path\to\output\folder"

# Ustawienia jakości renderowania
DPI = 300  # 150, 300, lub 600
# =========================

def remove_digital_signatures(input_pdf, output_pdf):
    """
    Usuwa podpisy cyfrowe z PDF poprzez renderowanie i ponowne utworzenie
    (symuluje wydrukowanie do PDF)
    
    Args:
        input_pdf (str): Ścieżka do pliku wejściowego
        output_pdf (str): Ścieżka do pliku wyjściowego
        
    Returns:
        bool: True jeśli sukces, False w przeciwnym razie
    """
    try:
        # Otwórz PDF
        pdf_document = fitz.open(input_pdf)
        
        # Utwórz nowy PDF
        pdf_writer = fitz.open()
        
        # Przetwórz każdą stronę
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            
            # Renderuj stronę do obrazu (to usuwa podpisy cyfrowe)
            mat = fitz.Matrix(DPI/72, DPI/72)
            pix = page.get_pixmap(matrix=mat, alpha=False)
            
            # Konwertuj pixmap do obrazu PIL
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Zapisz obraz do bufora
            img_buffer = io.BytesIO()
            img.save(img_buffer, format='PDF', resolution=float(DPI), quality=95)
            img_buffer.seek(0)
            
            # Otwórz tymczasowy PDF z obrazu
            temp_pdf = fitz.open(stream=img_buffer, filetype="pdf")
            
            # Dodaj stronę do nowego dokumentu
            pdf_writer.insert_pdf(temp_pdf)
            temp_pdf.close()
        
        # Zapisz nowy PDF
        pdf_writer.save(output_pdf, garbage=4, deflate=True)
        pdf_writer.close()
        pdf_document.close()
        
        return True
        
    except Exception as e:
        print(f"   Błąd podczas przetwarzania: {e}")
        return False

def remove_signatures_method2(input_pdf, output_pdf):
    """
    Alternatywna metoda - usuwa podpisy poprzez przepisanie treści
    (szybsza, ale może być mniej skuteczna)
    
    Args:
        input_pdf (str): Ścieżka do pliku wejściowego
        output_pdf (str): Ścieżka do pliku wyjściowego
        
    Returns:
        bool: True jeśli sukces, False w przeciwnym razie
    """
    try:
        # Otwórz PDF
        pdf_document = fitz.open(input_pdf)
        
        # Usuń wszystkie adnotacje (w tym podpisy)
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            
            # Usuń wszystkie
