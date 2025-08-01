import cv2

# List untuk menyimpan semua koordinat yang diklik
clicked_coords_list = []

# Fungsi untuk menangani event mouse untuk mendapatkan koordinat
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Jika klik kiri mouse
        clicked_coords_list.append((x, y))  # Menyimpan koordinat klik
        print(f"Koordinat Pixel: X={x}, Y={y}")

# Memuat video
video_path = "pos.mp4"  # Ganti dengan path video Anda

cap = cv2.VideoCapture(video_path)

# Memeriksa apakah video berhasil dibuka
if not cap.isOpened():
    print("Error: Tidak dapat membuka video.")
    exit()

# Mendapatkan frame rate video
fps = cap.get(cv2.CAP_PROP_FPS)

# Mendapatkan ukuran frame video (lebar dan tinggi)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Membuat jendela resizable
cv2.namedWindow("Frame Video", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()  # Membaca frame video
    if not ret:
        print("Video selesai.")
        break
    
    # Menampilkan koordinat yang telah diklik sebelumnya di frame
    for i, coord in enumerate(clicked_coords_list):
        x, y = coord
        # Menentukan posisi teks agar tetap dalam batas frame
        text = f"({x}, {y})"
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        text_x = x + 10
        text_y = y - 10

        # Menggeser teks jika berada terlalu dekat dengan tepi video
        if text_x + text_size[0] > frame_width:  # Jika teks keluar dari sisi kanan
            text_x = frame_width - text_size[0] - 10
        if text_y - text_size[1] < 0:  # Jika teks keluar dari sisi atas
            text_y = y + 10

        # Menampilkan koordinat dalam format ({x}, {y})
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.8, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Menggambar lingkaran di titik klik
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        
        # Jika ada titik sebelumnya, gambar garis ke titik tersebut
        if i > 0:
            prev_x, prev_y = clicked_coords_list[i - 1]
            cv2.line(frame, (prev_x, prev_y), (x, y), (0, 255, 0), 2)

    # Menampilkan frame
    cv2.imshow("Frame Video", frame)
    
    # Menunggu waktu sesuai dengan frame rate video
    key = cv2.waitKey(int(1000 / fps)) & 0xFF  # Delay untuk memastikan kecepatan normal
    
    # Menunggu event mouse
    cv2.setMouseCallback("Frame Video", click_event)
    
    # Tekan 'q' untuk keluar
    if key == ord('q'):  
        break

# Menutup jendela video
cap.release()
cv2.destroyAllWindows()
