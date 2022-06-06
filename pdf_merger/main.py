from argparse import ArgumentParser
from PyPDF2 import PdfMerger
import os 


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", help="target directory")
    args = vars(parser.parse_args())
    print(args)
    target_directory = args["target"]
    print("target_directory:", target_directory)
    pdfs = os.listdir(target_directory)
    pdfs.sort()
    # pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']
    print("will merge pdfs: ", pdfs)
    input("Press any button to confirm. Use ctrl + c to quit\n")

    merger = PdfMerger()

    for pdf in pdfs:
        print("... merging ...", pdf)
        merger.append(
            os.path.join(target_directory, pdf), 
            import_bookmarks=False)

    merger.write("result.pdf")
    merger.close()
    print("merged successfully, the result is result.pdf in current directory")
