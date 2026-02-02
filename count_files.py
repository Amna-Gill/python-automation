import os

folder_path = r"C:\Users\WindowS 10\Downloads"

pdf_count = 0
image_count = 0
other_count = 0


for item in os.listdir(folder_path):
    full_path = os.path.join(folder_path, item)

    if os.path.isfile(full_path):
        if item.lower() .endswith(".pdf"):
            pdf_count += 1

        elif item.lower() .endswith((".jpg", ".png", ".jpeg")):
            image_count += 1

        else:
            other_count += 1


print("File Report:")
print(f"PDF files: {pdf_count}")
print(f"Image files: {image_count}")
print(f"Other files: {other_count}")
