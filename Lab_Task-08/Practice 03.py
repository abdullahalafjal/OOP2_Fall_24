def read_file(file_name):
    try:

        f = open(file_name, "r")
        try:

            content = f.read()
            print("File Content:")
            print(content)
        except Exception as e:

            print(f"Error reading file: {e}")
        finally:

            print("Closing the file.")
            f.close()
    except FileNotFoundError as e:

        print(f"File not found: {e}")
    except Exception as e:

        print(f"An error occurred: {e}")
    finally:
        print("Execution of read_file is complete.")


try:
    read_file("example.txt")

except Exception as e:
    print(f"An unexpected error occurred in the main block: {e}")
