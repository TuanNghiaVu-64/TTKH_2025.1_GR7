import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox


def compute_and_plot():
    try:
        # ===== 1. LẤY THAM SỐ TỪ GIAO DIỆN =====
        Fs = float(entry_fs.get())      # Tần số lấy mẫu (Hz)
        T = float(entry_t.get())        # Thời gian tín hiệu (s)

        f1 = float(entry_f1.get())      # Tần số sóng 1
        A1 = float(entry_a1.get())      # Biên độ sóng 1

        f2 = float(entry_f2.get())      # Tần số sóng 2
        A2 = float(entry_a2.get())      # Biên độ sóng 2

        # ===== 2. TẠO TRỤC THỜI GIAN =====
        N = int(Fs * T)                 # Số mẫu
        t = np.linspace(0, T, N, endpoint=False)

        # ===== 3. TẠO 2 TÍN HIỆU & CỘNG LẠI =====
        x1 = A1 * np.sin(2 * np.pi * f1 * t)
        x2 = A2 * np.sin(2 * np.pi * f2 * t)

        x = x1 + x2   # TÍN HIỆU TỔNG 

        # ===== 4. TÍNH DFT =====
        X = np.zeros(N, dtype=complex)

        for k in range(N):
            for n in range(N):
                X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)

        # ===== 5. TRỤC TẦN SỐ =====
        freqs = np.arange(N) * Fs / N
        half = N // 2                   # Giới hạn Nyquist

        magnitude = np.abs(X) / N

        # ===== 6. VẼ PHỔ TẦN SỐ =====
        plt.figure(figsize=(10, 6))
        plt.stem(freqs[:half], magnitude[:half], basefmt=" ")
        plt.xlabel("Tần số (Hz)")
        plt.ylabel("Biên độ")
        plt.title("Phổ tần số của tín hiệu gồm 2 sóng (DFT thủ công)")
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")


# ===== 7. GIAO DIỆN NHẬP THAM SỐ =====
root = tk.Tk()
root.title("DFT – 2 tín hiệu")
root.geometry("520x360")
root.resizable(False, False)

padx = 10
pady = 6

# ===== FRAME THAM SỐ CHUNG (Fs, T) =====
frame_common = tk.LabelFrame(root, text="Tham số chung", padx=10, pady=10)
frame_common.pack(fill="x", padx=15, pady=10)

tk.Label(frame_common, text="Fs (Hz):")\
    .grid(row=0, column=0, padx=padx, pady=pady, sticky="e")
entry_fs = tk.Entry(frame_common, width=12)
entry_fs.insert(0, "1000")
entry_fs.grid(row=0, column=1, padx=padx, pady=pady)

tk.Label(frame_common, text="T (s):")\
    .grid(row=0, column=2, padx=padx, pady=pady, sticky="e")
entry_t = tk.Entry(frame_common, width=12)
entry_t.insert(0, "1")
entry_t.grid(row=0, column=3, padx=padx, pady=pady)


# ===== FRAME SÓNG =====
frame_signal = tk.LabelFrame(root, text="Thành phần tín hiệu", padx=10, pady=10)
frame_signal.pack(fill="x", padx=15, pady=10)

# ---- CỘT SÓNG 1 ----
tk.Label(frame_signal, text="Sóng 1", font=("Arial", 10, "bold"))\
    .grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame_signal, text="f1 (Hz):")\
    .grid(row=1, column=0, padx=padx, pady=pady, sticky="e")
entry_f1 = tk.Entry(frame_signal, width=12)
entry_f1.insert(0, "50")
entry_f1.grid(row=1, column=1, padx=padx, pady=pady)

tk.Label(frame_signal, text="A1:")\
    .grid(row=2, column=0, padx=padx, pady=pady, sticky="e")
entry_a1 = tk.Entry(frame_signal, width=12)
entry_a1.insert(0, "1")
entry_a1.grid(row=2, column=1, padx=padx, pady=pady)


# ---- CỘT SÓNG 2 ----
tk.Label(frame_signal, text="Sóng 2", font=("Arial", 10, "bold"))\
    .grid(row=0, column=3, columnspan=2, pady=5)

tk.Label(frame_signal, text="f2 (Hz):")\
    .grid(row=1, column=3, padx=padx, pady=pady, sticky="e")
entry_f2 = tk.Entry(frame_signal, width=12)
entry_f2.insert(0, "120")
entry_f2.grid(row=1, column=4, padx=padx, pady=pady)

tk.Label(frame_signal, text="A2:")\
    .grid(row=2, column=3, padx=padx, pady=pady, sticky="e")
entry_a2 = tk.Entry(frame_signal, width=12)
entry_a2.insert(0, "0.5")
entry_a2.grid(row=2, column=4, padx=padx, pady=pady)


# ===== BUTTON =====
tk.Button(
    root,
    text="Tính DFT & Vẽ phổ",
    command=compute_and_plot,
    width=30
).pack(pady=20)

root.mainloop()
