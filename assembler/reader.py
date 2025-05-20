def read_assembly_code():
    print("Assembly kodunu girin (bitirmek için 'END' yazın):")
    code_lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        code_lines.append(line.strip())
    return code_lines
