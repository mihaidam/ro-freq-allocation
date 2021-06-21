# ro-freq-allocation

This project presents some data extracted from the frequency allocation chart of Romania, that can be found [here](https://www.ancom.ro/tnabf_3998).

## Interactive version
- [here](https://mihaidam.github.io/ro-freq-allocation/)

What you can find in the repo:
- [pdf_data.pdf](./pdf_data.pdf) -> the PDF used to extract data, **latest version at the time of writing, may not be accurate in the future**
- [raw_csv_to_clean.py](./raw_csv_to_clean.py) -> takes just certain columns from input_sanitized_\*.csv, tries to clean them and creates a new csv with the name \*hz_clean_aux.csv
- [csv_to_graph.py](./csv_to_graph.py) -> makes a graph with the data from \*hz_clean.csv
- input_sanitized_\*.csv -> raw data extracted from the PDF provided by ANCOM, classified on kHz, MHz, GHz
- \*hz_clean_aux.csv -> data from input_sanitized_\*.csv, cleaned by raw_csv_to_clean.py, classified on kHz, MHz, GHz
- \*hz_clean.csv -> data from \*hz_clean_aux.csv, cleaned by hand, classified on kHz, MHz, GHz

---
## Requirements
- [pandas](https://pypi.org/project/pandas/)
- [plotly](https://pypi.org/project/plotly/)

---
## Live test
- [kHz frequencies graph](./khz_graph.html)
- [MHz frequencies graph](./mhz_graph.html)
- [GHz frequencies graph](./ghz_graph.html)

---

*Mihai Damian, Marian Neagul, FMI@UVT, Spring 2021*
