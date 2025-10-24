# PDF Digital Signature Remover

Automatyczny skrypt w Pythonie do usuwania podpisów cyfrowych z plików PDF poprzez renderowanie dokumentów (symulacja "Print to PDF").

## 📋 Opis

Skrypt przetwarza pliki PDF z wybranego folderu, usuwając z nich podpisy cyfrowe i metadane poprzez renderowanie każdej strony do obrazu wysokiej jakości i utworzenie nowego dokumentu PDF. Proces jest w pełni automatyczny i nie wymaga interakcji użytkownika.

### ✨ Funkcjonalności

- ✅ Automatyczne przetwarzanie wielu plików PDF
- ✅ Usuwanie podpisów cyfrowych i metadanych
- ✅ Zachowanie wysokiej jakości dokumentu (300 DPI)
- ✅ Szczegółowy pasek postępu i statystyki
- ✅ Obsługa błędów i duplikatów
- ✅ Raport z czasem przetwarzania i zmianami rozmiaru plików

## 🚀 Instalacja

### Wymagania

- Python 3.7 lub nowszy
- pip (menedżer pakietów Python)

### Instalacja zależności

```bash
pip install -r requirements.txt

### 📖 Użycie
Podstawowe użycie
Sklonuj repozytorium:
Bash

git clone https://github.com/yourusername/pdf-signature-remover.git
cd pdf-signature-remover
Edytuj ścieżki folderów w pliku pdf_signature_remover.py:
Python

input_folder = r"C:\sciezka\do\folderu\wejsciowego"
output_folder = r"C:\sciezka\do\folderu\wyjsciowego"
Uruchom skrypt:
Bash

python pdf_signature_remover.py
Przykład wyjścia
text

======================================================================
SKRYPT USUWANIA PODPISÓW CYFROWYCH Z PDF
======================================================================

📁 Znaleziono plików PDF: 5
📂 Folder wejściowy: C:\input
📂 Folder wyjściowy: C:\output

🔧 Metoda przetwarzania:
   • RENDER - Renderuje każdą stronę do obrazu (jak drukowanie)
   • Usuwa wszystkie podpisy cyfrowe i metadane
   • Wyższa jakość, wolniejsze przetwarzanie

======================================================================

[1/5] Przetwarzanie: dokument1.pdf
   📄 Rozmiar wejściowy: 245.50 KB
   ⏳ Przetwarzanie w toku...
   ✓ Pomyślnie przetworzono
   📄 Rozmiar wyjściowy: 312.75 KB
   ⏱️  Czas: 3.45 s
   📊 Zmiana rozmiaru: +27.4%
   📊 Postęp ogólny: [████████░░░░░░░░] 20.0%

...

======================================================================
PODSUMOWANIE
======================================================================
✓ Plików przetworzonych pomyślnie: 5
📊 Łącznie plików do przetworzenia: 5
⏱️  Całkowity czas wykonania: 18.23 sekund (0.30 minut)
⚡ Średni czas na plik: 3.65 sekund
======================================================================
⚙️ Konfiguracja
Zmiana jakości renderowania
W pliku pdf_signature_remover.py, znajdź linię:

Python

mat = fitz.Matrix(300/72, 300/72)  # 300 DPI
Możliwe opcje:

150 DPI - szybsze przetwarzanie, mniejszy rozmiar, niższa jakość
300 DPI - zalecane - dobra równowaga jakości i rozmiaru
600 DPI - najwyższa jakość, duże pliki, wolne przetwarzanie
Zmiana metody przetwarzania
Skrypt oferuje dwie metody:

'render' (domyślna) - Renderuje strony do obrazów

Gwarantuje usunięcie wszystkich podpisów
Wyższa jakość
Wolniejsze
'clean' - Usuwa tylko adnotacje

Szybsze
Może nie usunąć wszystkich typów podpisów
Zmiana metody:

Python

success = process_pdf(input_path, output_pdf, method='clean')  # zamiast 'render'
📁 Struktura projektu
text

pdf-signature-remover/
│
├── pdf_signature_remover.py    # Główny skrypt
├── requirements.txt             # Zależności Python
├── README.md                    # Ten plik
├── LICENSE                      # Licencja MIT
└── .gitignore                  # Pliki ignorowane przez Git
🛠️ Jak to działa
Skanowanie - Skrypt znajduje wszystkie pliki PDF w folderze wejściowym
Renderowanie - Każda strona PDF jest renderowana do obrazu w wysokiej rozdzielczości (300 DPI)
Tworzenie nowego PDF - Z obrazów tworzony jest nowy dokument PDF
Zapis - Nowy plik (bez podpisów cyfrowych) jest zapisywany w folderze wyjściowym
Ten proces skutecznie usuwa:

✅ Podpisy cyfrowe
✅ Metadane dokumentu
✅ Ukryte informacje
✅ Adnotacje i komentarze
🐛 Rozwiązywanie problemów
ImportError: No module named 'fitz'
Bash

pip install --upgrade PyMuPDF
Błąd: "Folder wejściowy nie istnieje"
Upewnij się, że ścieżki folderów są poprawne i używaj surowych stringów (prefix r):

Python

input_folder = r"C:\Users\nazwa\Documents\pdfs"
Pliki wyjściowe są zbyt duże
Zmniejsz rozdzielczość renderowania do 150 DPI:

Python

mat = fitz.Matrix(150/72, 150/72)
Skrypt działa bardzo wolno
Zmniejsz rozdzielczość (patrz wyżej)
Użyj metody 'clean' zamiast 'render' (mniej skuteczna)
Rozważ przetwarzanie mniejszej liczby plików naraz
🤝 Wkład w projekt
Zapraszamy do zgłaszania problemów (Issues) i pull requestów!

Jak dodać wkład:
Sforkuj projekt
Utwórz branch z nową funkcjonalnością (git checkout -b feature/AmazingFeature)
Commituj zmiany (git commit -m 'Add some AmazingFeature')
Push do brancha (git push origin feature/AmazingFeature)
Otwórz Pull Request
📝 Changelog
v1.0.0 (2024)
Pierwsza publiczna wersja
Usuwanie podpisów cyfrowych poprzez renderowanie
Wsparcie dla przetwarzania wsadowego
Szczegółowe raportowanie postępu
⚠️ Uwagi prawne
WAŻNE: Ten skrypt usuwa podpisy cyfrowe z dokumentów PDF. Używaj go tylko z dokumentami, do których masz pełne prawa. Usuwanie podpisów cyfrowych z dokumentów bez odpowiedniego upoważnienia może być nielegalne w Twojej jurysdykcji.

Autor nie ponosi odpowiedzialności za niewłaściwe użycie tego oprogramowania.
