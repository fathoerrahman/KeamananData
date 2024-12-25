from stegano import lsb
import os


def get_image_path():
    while True:
        image_path = input("D:\Alamak\JustinDidier.jpg")
        if os.path.exists(image_path) and image_path.endswitch(('.png','.jpeg','.jpg')):
            return image_path
        else:
            print("Path gambar tidak valid. Silakan coba lagi.")


def hide_message():
    image_path = get_image_path()
    message = input("Masukkan pesan yang ingin Anda sematkan: ")
    try:
        secret = lsb.hide(image_path, message)
        save_path = input("D:\Hidden\HiddenImage.jpg")

        if not os.path.exists(os.path.dirname(save_path)):
            print("Folder tujuan tidak ada. Silahkan coba lagi")
            return
            
        secret.save(save_path)
        print(f"File berhasil disembunyikan dalam gambar. Gambar disimpan di: {save_path}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan gambar: {e}")


def show_message():
    image_path = get_image_path()
    try:
        clear_message = lsb.reveal(image.path)
        if clear_message:
            print(f"Pesan tersembunyi: {clear_message}")
        else:
            print(f"Tidak ada pesan tersembunyi dalam gambar")
    except Exception as e:
        print(f"Gagal menampilkan pesan dari gambar: {e}")


def main():
    while True:
        print("\nSteganography Tool - Terminal Version")
        print("1. Sembunyikan Pesan")
        print("2. Tampilkan Pesan")
        print("3. Keluar")
        choice = input("Pilih opsi (1/2/3): ")

        if choice == '1':
            hide_message()
        elif choice == '2':
            show_message()
        elif choice == '3':
            print("Keluar dari Program")
            break
        else:
            print("Opsi tidak valid")


if __name__ == "__main__":
    main()