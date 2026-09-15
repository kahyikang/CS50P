f = input("File name: ").lower().strip()

ex = f[f.rfind(".")+1:]

match ex:
    case "gif" | "png":
        print("image/" + ex)
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + ex)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
