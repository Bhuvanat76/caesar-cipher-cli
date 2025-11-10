# Caesar Cipher CLI

A simple and beginner-friendly command-line tool that implements the classic Caesar Cipher encryption technique.  
This project supports **encryption**, **decryption**, **brute-force cracking**, **file input**, and **stdin input**.  
Built in Python for quick learning and easy extensibility.

---

## 🚀 Features

- ✅ Encrypt text using a shift value  
- ✅ Decrypt encrypted text using the same shift  
- ✅ Brute-force mode to try all 26 possible keys  
- ✅ Works with:
  - Direct text (`-t`)
  - Files (`-i`)
  - Standard input (`echo "msg" | ./caesar.py`)
- ✅ Preserves uppercase and lowercase letters  
- ✅ Non-alphabet characters remain unchanged  
- ✅ Clean and simple CLI using `argparse`  

---

## 📌 Usage

### **Encrypt**
```bash
./caesar.py -e -k 3 -t "HELLO WORLD"
