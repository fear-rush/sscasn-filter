import json

with open('raw_data', 'r') as file:
    raw_data = file.read()

data = json.loads(raw_data)
output_file = 'kode_instansi.txt'

with open(output_file, 'w') as file:
    for item in data:
        nama = item['nama']
        kode = item['cepat_kode']
        
        file.write(f'nama: {nama} | kode: {kode}\n')

print(f'End {output_file}')
