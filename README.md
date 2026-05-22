# Calculator Funcții Speciale 🧮

O aplicație desktop minimalistă (GUI) dezvoltată în **Python** utilizând biblioteca **PyQt5**. Aplicația permite calcularea rapidă și precisă a funcțiilor trigonometrice și logaritmice, oferind o interfață modernă (Dark Mode) și o gestionare sigură a erorilor.

## ✨ Funcționalități

* **Modul Trigonometrie**: Calculează `sin(x)`, `cos(x)`, `tan(x)` și `cot(x)`. Unghiurile sunt introduse în **grade**, iar programul face automat conversia în radiani.
* **Modul Logaritmi**: Calculează logaritmi în baza 10 (`log10(x)`), logaritm natural (`ln(x)`) și logaritm în baza 2 (`log2(x)`).
* **Gestionarea Erorilor (Error Handling)**: 
  * Afișează mesaje de eroare clare (colorate în roșu) dacă utilizatorul introduce text în loc de numere.
  * Tratează cazurile matematice nedefinite (ex: logaritm din numere negative, împărțirea la zero pentru `tan(90°)` sau `cot(0°)`).
* **Interfață "Dark Mode"**: Design elegant personalizat prin stylesheet-uri (QSS) asemănătoare CSS-ului.

## 🛠️ Cerințe preliminare

Pentru a rula această aplicație, ai nevoie de **Python 3.x** instalat pe sistemul tău, precum și de biblioteca **PyQt5**. 

Pentru a instala dependența necesară, deschide un terminal (sau Command Prompt) și rulează:
```bash
pip install PyQt5
