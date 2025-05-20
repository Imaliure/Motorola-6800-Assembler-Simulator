from assembler.reader import read_assembly_code
from assembler.parser import validate_code
from assembler.address_resolver import resolve_addresses
from assembler.code_generator import generate_object_code

def main():
    # 1. Assembly kodlarını oku
    assembly_code = read_assembly_code()

    # 2. Geçerli komut kontrolü
    validation_results = validate_code(assembly_code)

    print("\n--- Komut Kontrolü Sonucu ---")
    for line_num, line, is_valid in validation_results:
        status = "✅ GEÇERLİ" if is_valid else "❌ GEÇERSİZ"
        print(f"{line_num:02d}: {line} --> {status}")

    # 3. Adres çözümlemesi
    address_map, label_map = resolve_addresses(assembly_code)

    print("\n--- Adres Haritası (Komutlara Göre) ---")
    for addr, line in address_map.items():
        print(f"${addr:04X}: {line}")

    print("\n--- Label Haritası ---")
    for label, addr in label_map.items():
        print(f"{label} = ${addr:04X}")

    # 4. Kod üretimi
    object_code = generate_object_code(assembly_code, label_map)

    print("\n--- Assembly ➜ Object Code ---")
    for machine_code, source in object_code:
        print(f"{machine_code:10} ; {source}")


if __name__ == "__main__":
    main()
