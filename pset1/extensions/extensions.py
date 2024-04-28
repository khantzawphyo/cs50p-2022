def get_media_type(filename):
    filename = filename.lower()
    extensions = {
      ".gif": "image/gif",
      ".jpg": "image/jpeg",
      ".jpeg": "image/jpeg",
      ".png": "image/png",
      ".pdf": "application/pdf",
      ".txt": "text/plain",
      ".zip": "application/zip",
  }
    for ext, media_type in extensions.items():
        if filename.endswith(ext):
            return media_type
    return "application/octet-stream"

def main():
    file_name = input("File name: ")
    print(get_media_type(file_name))

if __name__ == "__main__":
    main()