# Nginx Log Parser

A practical, memory-efficient Python CLI utility designed to parse large server log files, extract critical data, and generate error reports without overloading system RAM.

---

## 🚀 Features

- **Memory Optimization:** Uses Python generators (`yield`) to read files line-by-line, allowing the processing of multi-gigabyte logs.
- **Regex Parsing:** Accurately extracts IP addresses and HTTP status codes using the `re` module.
- **Analytics:** Uses `collections.Counter` to aggregate data and display the top 3 IP addresses generating HTTP errors (status >= 400).
- **CLI Interface:** Built with `argparse` for seamless terminal integration and auto-generated help menus.
- **Error Handling:** Graceful error management preventing system crashes when files are missing.

---

## 🛠️ Technologies

- **Python 3**
- **Standard Libraries**: `re`, `argparse`, `collections`, `sys`

---

## ⚙️ Usage 

Run the script directly from the terminal, providing the path to your log file via the `--logfile` argument.

```bash
# Analyze a specific log file
python log_parser.py --logfile server.log

# Display help and available arguments
python log_parser.py --help