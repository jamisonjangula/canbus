from data_processor import ProcessCanData
from file_manager import FileManager


def main():
    clean_file_name: str = input("Please provide a file name for the clean data: ")
    split_file_name: str = input("Please provide a file name for the split raw data ")
    file_manager = FileManager(clean_file_name=clean_file_name,
                               split_file_name=split_file_name)
    file_manager.process_raw_filenames()

    data_processor = ProcessCanData(scope_data=file_manager.scope_data)
    data_processor.basic_stats()


if __name__ == '__main__':
    main()


