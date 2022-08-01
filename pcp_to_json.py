import fitz
import json

PDF_PATH = "propuesta.pdf"
OUTPUT_PATH = "propuesta.json"

def build_json(doc):
    """
    This function transform a pymupdf to list object.

    Here we take the pymupdf object and read the information for build the wanted structure that will be transform into a json object.
    """
    information = []

    # fill the list with the chapters objects from the toc of the file.
    for chap in doc.get_toc():
        if "Capítulo" in chap[1]:
            information.append({"title": chap[1], "page": chap[2], "articles": []})

    # fill the chapters with the articles information looking into the specific pages of the chapter.
    for index, chap in enumerate(information):
        try:
            last_chap_page = information[index + 1]["page"]
        except Exception:
            last_chap_page = 145

        for page in doc.pages(chap["page"] - 1, last_chap_page, 1):
            for block in page.get_text("blocks"):
                if "Artículo" in block[4]:
                    # then is an article
                    chap["articles"].append({"title": block[4].strip(), "sections": []})
                elif len(block[4]) > 50 and not "Artículo" in block[4] and not "." in block[4][0:2] and not block[4][0:2].isnumeric():
                    # then is the continuos of the last subsection
                    try:
                        chap["articles"][-1]["sections"][-1]["content"] += " " + block[4].replace('\n',"").strip()
                    except Exception as e:
                        try:
                            chap["articles"][-1]["sections"].append({"number": 1, "content": block[4].replace('\n',"").strip(), "subsections":[]})
                        except Exception as e:
                            print("There is no article: ", block[4])
                # elif len(block[4]) > 50 and not "Artículo" in block[4] and not "." in block[4][0:2] and not block[4][0:2].isnumeric() and ")" in block[4][0:2]:
                #     # then is a subsection of subsection. Like a) or b)
                #     try:
                #         chap["articles"][-1]["subsections"][-1]["subsections"].append(block[4].replace('\n',"").strip())
                #     except Exception as e:
                #         print("No subsection")
                #         # try:
                #         #     chap["articles"][-1]["subsections"].append({"number": 1, "content": block[4].replace('\n',"").strip(), "subsections":[]})
                #         # except Exception as e:
                #         #     print("There is no article: ", block[4])
                elif len(block[4]) > 50:
                    # then is a subsection
                    try:
                        chap["articles"][-1]["sections"].append({"number": 1, "content": block[4].replace('\n',"").strip(), "subsections":[]})
                    except Exception as e:
                        print("There is no article: ", block[4])

    return information

def write_results(obj):
    """
    Write an object into a json file.
    """
    out_file = open(OUTPUT_PATH, "w")
    json.dump(obj, out_file, indent=4, ensure_ascii=False)
    out_file.close()


def main():
    """
    Main logic of the script.
    """
    doc = fitz.open(PDF_PATH)
    obj = build_json(doc)
    write_results(obj)

if __name__ == '__main__':
    main()
