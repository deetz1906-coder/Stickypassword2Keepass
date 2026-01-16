# Stickypassword2Keepass
Convert Sticky Password XML file to CSV for KeePass import.

Sticky Password no longer supports CSV format exports. Therefore, I have created a script to convert XML-formatted Sticky Password files to CSV format, which is compatible with KeePass imports.


## Usage Examples
### If xml file name is default.xml
```
python s2k.py
```

### If xml file name is 'password.xml'
```
python s2k.py password.xml
```

### Specify csv file name
```
python s2k.py password.xml out.csv
```
```
python s2k.py -o out.csv
---

## Fork notes (2026)

This fork contains fixes for newer Sticky Password XML exports on Windows.

### Fixes
- Prevents `KeyError: 'Name'` by using safe attribute access (`.get(...)`)
- Avoids crashes when entries are missing expected attributes

### Export from Sticky Password
Use the unencrypted export:
- **Sticky Password 6 XML**

### Usage
If your XML file is named `default.xml` in the current folder:

```bash
python s2k.py
```
