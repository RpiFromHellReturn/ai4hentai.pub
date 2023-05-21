import opencc

def convert_simplified_to_traditional(input_file, output_file):
    converter = opencc.OpenCC('s2t.json')

                with open(input_file, 'r', encoding='utf-8') as file:
                    simplified_text = file.read()

                                    traditional_text = converter.convert(simplified_text)

                                            with open(output_file, 'w', encoding='utf-8') as file:
                                                file.write(traditional_text)

                                                        input_file = '简体字小说.txt'
                                                        output_file = '繁体字小说.txt'
                                                        convert_simplified_to_traditional(input_file, output_file)

