# pyknp: Python Module for JUMAN++/KNP

This repository forked from https://github.com/ku-nlp/pyknp.

Python Binding for JUMAN++ and KNP

> ⚠️: I did not confirm JUMAN and python2 compatibility.

## Confirmed platforms

- Pattern1
    - Windows 10 Home 1904
    - Python 3.8.3rc1
    - Juman++ Version: 2.0.0-rc2
    - knp 4.11 (64bit)
    - juman 7.0(just for dic/ directory. PATH do not include juman.exe) (64bit)

## Requirements

- Python
    - Verified Versions: 3.8.3rc1
- 形態素解析器 [JUMAN++](http://nlp.ist.i.kyoto-u.ac.jp/index.php?JUMAN++)
    - Verified Versions: 2.0.0-rc2
        - I recommend following [This issue in jumanpp repository](https://github.com/ku-nlp/jumanpp/issues/91#issuecomment-395245900) to install jumanpp.
        - Perhaps, 2.0.0-rc3 is not ready for windows (2020/05/09).
- 構文解析器 for windows binary [KNP](http://nlp.ist.i.kyoto-u.ac.jp/index.php?KNP) 
    - Verified Versions: 4.11 (64bit)

## Install

```
git clone https://github.com/yusanish/pyknp
cd pyknp
python setup.py install --record installed_file.txt
```

## Uninstall

```
cd pyknp
cat installed_file.txt | xargs rm -rf
```

## How to use

You need to set command and option when Juman() and KNP constracted.

```python
#jumanpp
jumanpp = Juman(command="jumanpp_v2.exe", option="--model=[path to jumandic.jppmdl]")

#knp
knp = KNP(command="knp.exe", jumancommand="jumanpp_v2.exe", jumanoption="--model=[path to jumandic.jppmdl]")
```

Official Document 👉 https://pyknp.readthedocs.io/en/latest/

## Authors/Contact

The original pyknp library created by
- 京都大学 黒橋・河原研究室 (contact@nlp.ist.i.kyoto-u.ac.jp)
- John Richardson, Tomohide Shibata, Yuta Hayashibe, Tomohiro Sakaguchi

## 免責事項 / Disclaimer

公式のものとの動作が同じになる保証はございません。  
there is no guarantee that it will work the same as the official version.
