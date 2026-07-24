# Duplicate File Removal Automation

## Description

Duplicate File Removal Automation is a Python project that scans a specified directory recursively, identifies duplicate files using the MD5 checksum algorithm, removes duplicate copies while keeping one original, generates a detailed log file, and sends the log file to a specified email address. The process repeats automatically after a user-defined time interval.

---

## Features

- Recursive directory scanning
- Duplicate detection using MD5 checksum
- Removes duplicate files
- Keeps one original copy
- Generates timestamp-based log files
- Automatically creates a "Marvellous" directory for logs
- Sends log files through email
- Executes automatically after a specified time interval
- Supports `--help, --h, --H` and `--usage, --u, --U` options
- Proper exception handling

---

## Project Structure

```
DuplicateFileRemoval/
│
├── Checksum.py
├── DirectoryScanner.py
├── DuplicateFinder.py
├── FileRemover.py
├── Logger.py
├── EmailSender.py
├── Scheduler.py
├── DuplicateFileRemoval.py
├── README.md
```

---

## Requirements

- Python 3.x
- schedule module

Install schedule:

```bash
pip install schedule
```

---

## Command

```bash
python DuplicateFileRemoval.py <DirectoryPath> <TimeInterval> <ReceiverEmail>
```

Example

```bash
python DuplicateFileRemoval.py "C:\Demo" 30 abc@gmail.com
```

---

## Help

```bash
python DuplicateFileRemoval.py --help
```

---

## Usage

```bash
python DuplicateFileRemoval.py --usage
```

---

## Working

1. Accept command line arguments.
2. Validate all arguments.
3. Scan the directory recursively.
4. Calculate MD5 checksum of every file.
5. Identify duplicate files.
6. Keep one original copy.
7. Delete remaining duplicates.
8. Create log file.
9. Send log file through email.
10. Wait for the specified interval.
11. Repeat automatically.

---

## Output

The program creates

```
Marvellous/
```

Inside it creates

```
DuplicateRemovalLog_DD_MM_YYYY_HH_MM_SS.log
```

Example

```
DuplicateRemovalLog_24_07_2026_03_15_40.log
```

---

## Modules Used

- os
- sys
- hashlib
- time
- schedule
- smtplib
- email
- datetime

---

## Author

Sahil Mahadev Patil