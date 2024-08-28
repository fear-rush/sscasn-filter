
# SSCASN Filter

Membuat file excel dengan data filter formasi SSCASN sesuai jurusan 




## Examples

Ubah kode di base_url sesuai kode jurusan. Contoh kode 5101201 = S-1 Akuntansi. 

Ubah offset_number. Rumus: total data - 10. Contoh: karena total data ada 135, maka offset sampai 125


```python
kode = 5101201
offset_number = 125
```


## Installation

Python required

```bash
pip install -r requirements.txt
python main.py   
```

Jika sudah menjalankan kode, maka akan muncul file excel bernama formasi.xlsx. Contoh di repository ini merupakan contoh formasi S-1 Akuntansi. 


    
