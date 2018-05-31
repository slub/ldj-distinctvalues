# ldj-distinctvalues - distinct values and their occurence of line delimited json

ldj-distinctvalues is a commandline command (Python3 program) that outputs distinct values and their occurence numbers (sorted by their occurence numbers) of a path of a given line delimited json document.

It reads vom stdin and prints to stdout.

## Usage

```
ldj-distinctvalues:
	required arguments:
	   -path	the path of the value to examine in the line delimited json document. You can navigate by . (dot) into objects (into array elements is not possible yet). You can use * as a wildcard.
```

* example:
    ```
    ldj-distinctvalues -path [PATH TO EXAMINE] < [LINE DELIMITED JSON FILE] > [OUTPUT STATISTICS DOCUMENT]
    ```

## Requirements
No special requirements. It uses the Python standard libraries json, sys and argparse.

### Install system-wide via pip

* via pip:
    ```
    sudo -H pip3 install --upgrade [ABSOLUTE PATH TO YOUR LOCAL GIT REPOSITORY OF LDJ-DISTINCTVALUES]
    ```
    (which provides you ```ldj-distinctvalues``` as a system-wide commandline command)

