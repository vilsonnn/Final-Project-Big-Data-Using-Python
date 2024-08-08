import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from PIL import ImageTk, Image 
import mysql.connector 
from mysql.connector import Error
from datetime import datetime
from tkcalendar import Calendar 
from fpdf import FPDF 
import pyautogui 
import time
import webbrowser
import customtkinter 


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  


class pengiriman_barang():

    def __init__(self, window):
        
        self.width= window.winfo_screenwidth()
        self.height= window.winfo_screenheight()
        self.fig=None
        self.fig1=None
        self.menu_width = self.width * 1
        self.menu_width1 = self.width * 0.26
        self.menu_width2 = self.width * 0.75
        self.menu_width3 = self.width * 0.63
        self.menu_width4 = self.width * 0.5
        self.menu_height = self.height * 1
        self.menu_height2 = self.height * 0.3
        self.menu_height3 = self.height * 0.175
        self.harga_total=[]
        self.printable_page = PrintablePage()
        self.no_resi=[]
            
        def login():
            username = self.entry_username.get()
            password = self.entry_password.get()

            if username == "Vilson" and password == "apayaa":
                messagebox.showinfo("Login Berhasil", "Selamat datang di aplikasi JNE Express - Pengiriman Barang!")
                show_menu_page()
            elif username == "Ason" and password == "kirakiraapa":
                messagebox.showinfo("Login Berhasil", "Selamat datang di aplikasi JNE Express - Pengiriman Barang!")
                show_menu_page()
            elif username == "Matthew" and password == "bingungdahh":
                messagebox.showinfo("Login Berhasil", "Selamat datang di aplikasi JNE Express - Pengiriman Barang!")
                show_menu_page()
            elif username == "" or password == "":
                messagebox.showerror("Error", "Mohon lengkapi semua input")
            else:
                messagebox.showerror("Login Gagal", "Username atau password salah!")

            self.label_menu = tk.Label(self.menu_frame, text=f"Selamat Datang, {username}\n\n\n Belum di isi bagian home, rencana isi visdat", font=("Calibri", 18, 'bold'), background='#DCDCDC')
            self.label_menu.place(relx=0.45, rely=0.2, anchor=tk.CENTER)
    
            
        def show_menu_page():
            # Sembunyikan halaman login
            self.login_frame.pack_forget()
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pengiriman_barang_vilson",
                    port ="3308"
                )
                if connection.is_connected():
                    messagebox.showinfo('MySQL','Connected to MySQL database')
                else:
                    messagebox.showerror('MySQL','Not Connected to MySQL database')
            except Error as e:
                messagebox.showerror('MySQL','Error while connecting to MySQL', e)
            
            # Tampilkan halaman menu
            self.menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.menu_width, height=self.menu_height)
            self.dashboard_frame.place(relx=0.13, rely=0.5, anchor=tk.CENTER, width=self.menu_width1, height=self.menu_height) 

        def menu():
            self.menu_frame.place_forget()
            self.cek_harga_frame.place_forget()
            self.info_biaya_frame.place_forget()
            self.cek_frame.place_forget()
            self.edit_frame.place_forget()
            self.edit_tambah_frame.place_forget()
            self.edit_harga_frame.place_forget()
            self.biaya_frame.place_forget()
            self.btn_frame.place_forget()
            self.entry_tambah_kota_asal.delete(0, tk.END)
            self.dropdown_tambah.delete(0, tk.END)
            self.entry_tambah_kota_tujuan.delete(0, tk.END)
            self.entry_tambah_harga.delete(0, tk.END)
            self.dropdown_kota_asal.delete(0, tk.END)
            self.dropdown_harga.delete(0, tk.END)
            self.dropdown_kota_tujuan.delete(0, tk.END)
            self.entry_edit_harga_fix.delete(0, tk.END)
            self.dropdown_kota_asal_cek.delete(0, tk.END)
            self.dropdown_cek.delete(0, tk.END)
            self.dropdown_kota_tujuan_cek.delete(0, tk.END)
            self.entry_input_berat_cek.delete(0, tk.END)
            self.entry_input_nama_pengirim.delete(0, tk.END)
            self.entry_input_telp_pengirim.delete(0, tk.END)
            self.entry_input_alamat_pengirim.delete(0, tk.END)
            self.entry_input_email_pengirim.delete(0, tk.END)
            self.entry_input_nama_penerima.delete(0, tk.END)
            self.entry_input_telp_penerima.delete(0, tk.END)
            self.entry_input_alamat_penerima.delete(0, tk.END)
            self.entry_input_email_penerima.delete(0, tk.END)
            self.entry_input_tgl_transaksi.delete(0, tk.END)
            self.entry_input_jam_transaksi.delete(0, tk.END)
            self.entry_input_nbarang.delete(0, tk.END)
            self.entry_input_berat_barang.delete(0, tk.END)
            self.dropdown.delete(0, tk.END)
            self.dropdown_kota_asal_form.delete(0, tk.END)
            self.dropdown_kota_tujuan_form.delete(0, tk.END)
            self.dropdown1.delete(0, tk.END)
            self.selection_form.set(None)
            self.selection_form1.set(None)
            self.entry_input_bayar.delete(0, tk.END)
            self.label_kertas.config(text=None)
            self.no_resi.clear()
            self.harga_total.clear()
            self.biaya_frame.place_forget()
            self.table_frame.place_forget()
            self.table_frame1.place_forget()
            self.table_frame2.place_forget()
            self.table_frame3.place_forget()
            self.table_frame4.place_forget()
            self.table_frame5.place_forget()
            self.form_pengiriman_frame.place_forget()
            self.identitas_frame.place_forget()
            self.info_barang_frame.place_forget()
            self.halamanbiaya_frame.place_forget()
            self.menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.menu_width, height=self.menu_height)
                        
        def menu_form_pengiriman():
            self.menu_frame.place_forget()
            self.cek_harga_frame.place_forget()
            self.info_biaya_frame.place_forget()
            self.cek_frame.place_forget()
            self.edit_frame.place_forget()
            self.edit_tambah_frame.place_forget()
            self.edit_harga_frame.place_forget()
            self.biaya_frame.place_forget()
            self.btn_frame.place_forget()
            self.entry_tambah_kota_asal.delete(0, tk.END)
            self.dropdown_tambah.delete(0, tk.END)
            self.entry_tambah_kota_tujuan.delete(0, tk.END)
            self.entry_tambah_harga.delete(0, tk.END)
            self.dropdown_kota_asal.delete(0, tk.END)
            self.dropdown_harga.delete(0, tk.END)
            self.dropdown_kota_tujuan.delete(0, tk.END)
            self.entry_edit_harga_fix.delete(0, tk.END)
            self.dropdown_kota_asal_cek.delete(0, tk.END)
            self.dropdown_cek.delete(0, tk.END)
            self.dropdown_kota_tujuan_cek.delete(0, tk.END)
            self.entry_input_berat_cek.delete(0, tk.END)
            self.entry_input_nama_pengirim.delete(0, tk.END)
            self.entry_input_telp_pengirim.delete(0, tk.END)
            self.entry_input_alamat_pengirim.delete(0, tk.END)
            self.entry_input_email_pengirim.delete(0, tk.END)
            self.entry_input_nama_penerima.delete(0, tk.END)
            self.entry_input_telp_penerima.delete(0, tk.END)
            self.entry_input_alamat_penerima.delete(0, tk.END)
            self.entry_input_email_penerima.delete(0, tk.END)
            self.entry_input_tgl_transaksi.delete(0, tk.END)
            self.entry_input_jam_transaksi.delete(0, tk.END)
            self.entry_input_nbarang.delete(0, tk.END)
            self.entry_input_berat_barang.delete(0, tk.END)
            self.dropdown.delete(0, tk.END)
            self.dropdown_kota_asal_form.delete(0, tk.END)
            self.dropdown_kota_tujuan_form.delete(0, tk.END)
            self.dropdown1.delete(0, tk.END)
            self.selection_form.set(None)
            self.selection_form1.set(None)
            self.entry_input_bayar.delete(0, tk.END)
            self.label_kertas.config(text=None)
            self.no_resi.clear()
            self.harga_total.clear()
            self.biaya_frame.place_forget()
            self.table_frame.place_forget()
            self.table_frame1.place_forget()
            self.table_frame2.place_forget()
            self.table_frame3.place_forget()
            self.table_frame4.place_forget()
            self.table_frame5.place_forget()
            self.halamanbiaya_frame.place_forget()
            self.form_pengiriman_frame.place(relx=0.85, rely=0.5, anchor=tk.CENTER, width=self.menu_width2, height=self.menu_height)
            self.identitas_frame.place(relx=0.63, rely=0.3, anchor=tk.CENTER, width=self.menu_width3, height=self.menu_height2)
            self.info_barang_frame.place(relx=0.63, rely=0.45, anchor=tk.CENTER, width=self.menu_width3)
            perbarui_entri_waktu()
            

        def menu_cek_harga():
            self.menu_frame.place_forget()
            self.form_pengiriman_frame.place_forget()
            self.identitas_frame.place_forget()
            self.info_barang_frame.place_forget()
            self.halamanbiaya_frame.place_forget()
            self.btn_frame.place_forget()
            self.biaya_frame.place_forget()
            self.edit_frame.place_forget()
            self.edit_tambah_frame.place_forget()
            self.edit_harga_frame.place_forget()
            self.entry_tambah_kota_asal.delete(0, tk.END)
            self.dropdown_tambah.delete(0, tk.END)
            self.entry_tambah_kota_tujuan.delete(0, tk.END)
            self.entry_tambah_harga.delete(0, tk.END)
            self.dropdown_kota_asal.delete(0, tk.END)
            self.dropdown_harga.delete(0, tk.END)
            self.dropdown_kota_tujuan.delete(0, tk.END)
            self.entry_edit_harga_fix.delete(0, tk.END)
            self.dropdown_kota_asal_cek.delete(0, tk.END)
            self.dropdown_cek.delete(0, tk.END)
            self.dropdown_kota_tujuan_cek.delete(0, tk.END)
            self.entry_input_berat_cek.delete(0, tk.END)
            self.entry_input_nama_pengirim.delete(0, tk.END)
            self.entry_input_telp_pengirim.delete(0, tk.END)
            self.entry_input_alamat_pengirim.delete(0, tk.END)
            self.entry_input_email_pengirim.delete(0, tk.END)
            self.entry_input_nama_penerima.delete(0, tk.END)
            self.entry_input_telp_penerima.delete(0, tk.END)
            self.entry_input_alamat_penerima.delete(0, tk.END)
            self.entry_input_email_penerima.delete(0, tk.END)
            self.entry_input_tgl_transaksi.delete(0, tk.END)
            self.entry_input_jam_transaksi.delete(0, tk.END)
            self.entry_input_nbarang.delete(0, tk.END)
            self.entry_input_berat_barang.delete(0, tk.END)
            self.dropdown.delete(0, tk.END)
            self.dropdown_kota_asal_form.delete(0, tk.END)
            self.dropdown_kota_tujuan_form.delete(0, tk.END)
            self.dropdown1.delete(0, tk.END)
            self.selection_form.set(None)
            self.selection_form1.set(None)
            self.entry_input_bayar.delete(0, tk.END)
            self.label_kertas.config(text=None)
            self.no_resi.clear()
            self.harga_total.clear()
            self.biaya_frame.place_forget()
            self.table_frame.place_forget()
            self.table_frame1.place_forget()
            self.table_frame2.place_forget()
            self.table_frame3.place_forget()
            self.table_frame4.place_forget()
            self.table_frame5.place_forget()
            self.cek_harga_frame.place(relx=0.87, rely=0.5, anchor=tk.CENTER, width=self.menu_width2, height=self.menu_height)
            self.info_biaya_frame.place(relx=0.65, rely=0.35, anchor=tk.CENTER, width=self.menu_width3)
            
            
        
        def cek_harga():
            jenis_paket = self.dropdown_cek.get()
            kota_asal = self.dropdown_kota_asal_cek.get()
            kota_tujuan = self.dropdown_kota_tujuan_cek.get()

            if jenis_paket == "Paket Oke":
                query = "SELECT harga_kg FROM harga_paket_oke WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Reguler":
                query = "SELECT harga_kg FROM harga_paket_reguler WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Yes":
                query = "SELECT harga_kg FROM harga_paket_yes WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (kota_asal, kota_tujuan)

            if jenis_paket == "" or kota_asal == "" or kota_tujuan == "":
                messagebox.showerror("Error", "Mohon lengkapi semua input")
                return False

            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pengiriman_barang_vilson",
                    port="3308"
                )
                mycursor = mydb.cursor()

                berat = self.entry_input_berat_cek.get()
                harga_total = 0.0
                biayakirim_sesuaikg = 0.0

                # Hitung biaya kirim per kg
                mycursor.execute(query, params)
                result = mycursor.fetchone()
                if result:
                    result = float(result[0])
                    harga_total += result 
                    biayakirim_sesuaikg = result * float(berat)
                    harga_total *= float(berat)

                # Hitung harga asuransi
                selected_option = self.selection_cek1.get()
                if selected_option == 1:
                    harga_asuransi = float(berat) * 10000.0
                    harga_total += harga_asuransi

                # Hitung biaya packing
                selected_option1 = self.selection_cek.get()
                if selected_option1 == 1:
                    harga_total += 10000.0

                # Tampilkan hasil
                self.cek_frame.place(relx=0.6, rely=0.7, anchor=tk.CENTER)
                self.label_cek_kirim_kg = tk.Label(self.cek_frame, text=f"Biaya Kirim Per Kg                           : {str(result)}", font=("Calibri", 14, 'bold'), background='white')
                self.label_cek_kirim = tk.Label(self.cek_frame, text=f"Biaya Kirim Sesuai Berat                     : {str(biayakirim_sesuaikg)}", font=("Calibri", 14, 'bold'), background='white')
                self.label_cek_total = tk.Label(self.cek_frame, text=f"Total (jika menggunakan Asuransi dan Packing): {str(harga_total)}", font=("Calibri", 14, 'bold'), background='white')
                self.label_cek_total.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
                self.label_cek_kirim.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
                self.label_cek_kirim_kg.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
                self.btn_cek_harga_reset.grid(row=5, column=2, sticky=tk.W, padx=10, pady=5)

                messagebox.showinfo("Success", "Berikut Cek Harganya:")
                return True

            except mysql.connector.Error as error:
                print("Error executing query:", error)
                messagebox.showerror("Error", "Gagal cek harga, ada kesalahan")
                return False

            
            # Mengatur ulang pilihan dan entry cek_harga ke nilai default
        def reset():
            self.dropdown_kota_asal_cek.delete(0, tk.END)
            self.dropdown_cek.delete(0, tk.END)
            self.dropdown_kota_tujuan_cek.delete(0, tk.END)
            self.entry_input_berat_cek.delete(0, tk.END)
            self.selection_cek.set(0)  
            self.selection_cek1.set(0) 
            self.cek_frame.place_forget()

        def edit_masterdata():
            self.menu_frame.place_forget()
            self.form_pengiriman_frame.place_forget()
            self.identitas_frame.place_forget()
            self.info_barang_frame.place_forget()
            self.halamanbiaya_frame.place_forget()
            self.btn_frame.place_forget()
            self.biaya_frame.place_forget()
            self.menu_frame.place_forget()
            self.cek_harga_frame.place_forget()
            self.info_biaya_frame.place_forget()
            self.cek_frame.place_forget()
            self.edit_tambah_frame.place_forget()
            self.edit_harga_frame.place_forget()
            self.entry_tambah_kota_asal.delete(0, tk.END)
            self.dropdown_tambah.delete(0, tk.END)
            self.entry_tambah_kota_tujuan.delete(0, tk.END)
            self.entry_tambah_harga.delete(0, tk.END)
            self.dropdown_kota_asal.delete(0, tk.END)
            self.dropdown_harga.delete(0, tk.END)
            self.dropdown_kota_tujuan.delete(0, tk.END)
            self.entry_edit_harga_fix.delete(0, tk.END)
            self.dropdown_kota_asal_cek.delete(0, tk.END)
            self.dropdown_cek.delete(0, tk.END)
            self.dropdown_kota_tujuan_cek.delete(0, tk.END)
            self.entry_input_berat_cek.delete(0, tk.END)
            self.entry_input_nama_pengirim.delete(0, tk.END)
            self.entry_input_telp_pengirim.delete(0, tk.END)
            self.entry_input_alamat_pengirim.delete(0, tk.END)
            self.entry_input_email_pengirim.delete(0, tk.END)
            self.entry_input_nama_penerima.delete(0, tk.END)
            self.entry_input_telp_penerima.delete(0, tk.END)
            self.entry_input_alamat_penerima.delete(0, tk.END)
            self.entry_input_email_penerima.delete(0, tk.END)
            self.entry_input_tgl_transaksi.delete(0, tk.END)
            self.entry_input_jam_transaksi.delete(0, tk.END)
            self.entry_input_nbarang.delete(0, tk.END)
            self.entry_input_berat_barang.delete(0, tk.END)
            self.dropdown.delete(0, tk.END)
            self.dropdown_kota_asal_form.delete(0, tk.END)
            self.dropdown_kota_tujuan_form.delete(0, tk.END)
            self.dropdown1.delete(0, tk.END)
            self.selection_form.set(None)
            self.selection_form1.set(None)
            self.entry_input_bayar.delete(0, tk.END)
            self.label_kertas.config(text=None)
            self.no_resi.clear()
            self.harga_total.clear()
            self.biaya_frame.place_forget()
            self.table_frame.place_forget()
            self.table_frame1.place_forget()
            self.table_frame2.place_forget()
            self.table_frame3.place_forget()
            self.table_frame4.place_forget()
            self.table_frame5.place_forget()
            self.edit_frame.place(relx=0.6, rely=0.3, anchor=tk.CENTER)

        def selection_changed():
            selected_option = self.selection_cek.get()
            if selected_option == 1:
                print("Anda memilih YES")
            elif selected_option == 2:
                print("Anda memilih NO")
        
        def selection_changed1():
            selected_option = self.selection_cek1.get()
            if selected_option == 1:
                print("Anda memilih YES")
            elif selected_option == 2:
                print("Anda memilih NO")

        def selection_changed2():
            selected_option = self.selection_form.get()
            if selected_option == 1:
                print("Anda memilih YES")
            elif selected_option == 2:
                print("Anda memilih NO")
        
        def selection_changed3():
            selected_option = self.selection_form1.get()
            if selected_option == 1:
                print("Anda memilih YES")
            elif selected_option == 2:
                print("Anda memilih NO")

        def tambah_data():
            self.edit_frame.place_forget()
            self.edit_tambah_frame.place(relx=0.65, rely=0.22, anchor=tk.CENTER, width=self.menu_width3)
            self.table_frame.place(relx=0.65, rely=0.5, anchor=tk.CENTER,width=self.menu_width4)
            self.table_frame1.place(relx=0.55, rely=0.8, anchor=tk.CENTER,width=self.menu_width4)
            self.table_frame2.place(relx=0.85, rely=0.8, anchor=tk.CENTER,width=self.menu_width4)
            

        def edit_harga():
            self.edit_frame.place_forget()
            self.edit_harga_frame.place(relx=0.65, rely=0.22, anchor=tk.CENTER, width=self.menu_width3)
            self.table_frame3.place(relx=0.65, rely=0.5, anchor=tk.CENTER,width=self.menu_width4)
            self.table_frame4.place(relx=0.55, rely=0.8, anchor=tk.CENTER,width=self.menu_width4)
            self.table_frame5.place(relx=0.85, rely=0.8, anchor=tk.CENTER,width=self.menu_width4)
            
        def fungsi_tombol_tampilin():  
            jenis_paket = self.dropdown_harga.get()
            self.namatable = ""
            if jenis_paket == "Paket Oke":
                query = "SELECT kota_asal FROM harga_paket_oke UNION SELECT kota_tujuan FROM harga_paket_oke;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Reguler":
                query = "SELECT kota_asal FROM harga_paket_reguler UNION SELECT kota_tujuan FROM harga_paket_reguler;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Yes":
                query = "SELECT kota_asal FROM harga_paket_yes UNION SELECT kota_tujuan FROM harga_paket_yes;"
                tampilin_kota(query)
            else:
                self.namatable = ""
                self.kota_asal_values = []
                self.kota_tujuan_values = []

        def fungsi_tombol_tampilin1():  
            jenis_paket = self.dropdown_cek.get()
            self.namatable = ""
            if jenis_paket == "Paket Oke":
                self.namatable = "harga_paket_oke"
                query = "SELECT kota_asal FROM harga_paket_oke UNION SELECT kota_tujuan FROM harga_paket_oke;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Reguler":
                self.namatable = "harga_paket_reguler"
                query = "SELECT kota_asal FROM harga_paket_reguler UNION  SELECT kota_tujuan FROM harga_paket_reguler;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Yes":
                self.namatable = "harga_paket_yes"
                query = "SELECT kota_asal FROM harga_paket_yes UNION SELECT kota_tujuan FROM harga_paket_yes;"
                tampilin_kota(query)
            else:
                self.namatable = ""
                self.kota_asal_values = []
                self.kota_tujuan_values = []
        
        def fungsi_tombol_tampilin2():  
            jenis_paket = self.dropdown.get()
            self.namatable = ""
            if jenis_paket == "Paket Oke":
                self.namatable = "harga_paket_oke"
                query = "SELECT kota_asal FROM harga_paket_oke UNION SELECT kota_tujuan FROM harga_paket_oke;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Reguler":
                self.namatable = "harga_paket_reguler"
                query = "SELECT kota_asal FROM harga_paket_reguler UNION SELECT kota_tujuan FROM harga_paket_reguler;"
                tampilin_kota(query)
            elif jenis_paket == "Paket Yes":
                self.namatable = "harga_paket_yes"
                query = "SELECT kota_asal FROM harga_paket_yes UNION SELECT kota_tujuan FROM harga_paket_yes;"
                tampilin_kota(query)
            else:
                self.namatable = ""
                self.kota_asal_values = []
                self.kota_tujuan_values = []
                    
        def next():
            self.form_pengiriman_frame.place_forget()
            self.identitas_frame.place_forget()
            self.info_barang_frame.place_forget()
            self.halamanbiaya_frame.place(relx=0.63, rely=0.25, anchor=tk.CENTER,width=self.menu_width3)
            self.btn_frame.place(relx=0.8, rely=0.9, anchor=tk.CENTER)
        
        def submit():
            nama_pengirim=self.entry_input_nama_pengirim.get()
            notelp_pengirim=self.entry_input_telp_pengirim.get()
            alamat_pengirim=self.entry_input_alamat_pengirim.get()
            email_pengirim=self.entry_input_email_pengirim.get()
            nama_penerima=self.entry_input_nama_penerima.get()
            notelp_penerima=self.entry_input_telp_penerima.get()
            alamat_penerima=self.entry_input_alamat_penerima.get()
            email_penerima=self.entry_input_email_penerima.get()
            tanggal=self.entry_input_tgl_transaksi.get()
            waktu=self.entry_input_jam_transaksi.get()
            nama_barangg=self.entry_input_nbarang.get()
            berat_barang=self.entry_input_berat_barang.get()
            jenis_paket=self.dropdown.get()
            kota_asal=self.dropdown_kota_asal_form.get()
            kota_tujuan=self.dropdown_kota_tujuan_form.get()
            metode_pembayaran=self.dropdown1.get()
            

            if jenis_paket == "" or kota_asal == "" or kota_tujuan == "" or metode_pembayaran == "" or berat_barang == "" or nama_barangg == "" or waktu == "" or tanggal == "" or email_penerima == "" or alamat_penerima == "" or notelp_penerima == "" or nama_penerima == "" or email_pengirim == "" or alamat_pengirim == "" or notelp_pengirim == "" or nama_pengirim == "":
                messagebox.showerror("Error", "Mohon lengkapi semua input")
                return False

            if jenis_paket == "Paket Oke":
                query2 = "SELECT harga_kg FROM harga_paket_oke WHERE kota_asal = %s AND kota_tujuan = %s;"
                params2 = (kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Reguler":
                query2 = "SELECT harga_kg FROM harga_paket_reguler WHERE kota_asal = %s AND kota_tujuan = %s;"
                params2 = (kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Yes":
                query2 = "SELECT harga_kg FROM harga_paket_yes WHERE kota_asal = %s AND kota_tujuan = %s;"
                params2 = (kota_asal, kota_tujuan)
            id_customer = None
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pengiriman_barang_vilson",
                    port="3308"
                )
                mycursor = mydb.cursor()

                query="INSERT IGNORE INTO customer (nama_customer, telp_customer,alamat_customer,email_customer) VALUES (%s, %s,%s,%s);"
                params=(nama_pengirim,notelp_pengirim,alamat_pengirim,email_pengirim)
                execute_query(query, params)

                query_idcus="SELECT id_customer FROM customer WHERE nama_customer=%s AND telp_customer=%s AND alamat_customer=%s AND email_customer=%s"
                params_idcus=(nama_pengirim,notelp_pengirim,alamat_pengirim,email_pengirim)
                mycursor.execute(query_idcus, params_idcus)
                result1 = mycursor.fetchone()
                if result1:
                    id_customer=result1[0]

                if id_customer is not None:
                    harga_total = 0.0
                    biayakirim_sesuaikg = 0.0

                    # Hitung biaya kirim per kg
                    mycursor.execute(query2, params2)
                    result = mycursor.fetchone()
                    if result:
                        result = float(result[0])
                        harga_total += result
                        biayakirim_sesuaikg = result * float(berat_barang)
                        harga_total *= float(berat_barang)

                    # Hitung harga asuransi
                    selected_option2 = self.selection_form.get()
                    if selected_option2 == 1:
                        harga_asuransi = float(berat_barang) * 10000.0
                        harga_total += harga_asuransi
                    elif selected_option2 == 2:
                        harga_asuransi=0
                    elif selected_option2 =='':
                        harga_asuransi=0

                    # Hitung biaya packing
                    selected_option3 = self.selection_form1.get()
                    if selected_option3 == 1:
                        harga_packing=10000
                        harga_total += 10000.0
                    elif selected_option3 ==2:
                        harga_packing=0
                    elif selected_option3 =='':
                        harga_packing=0
                    

                    bayar=0
                    kembalian=0
                    query1="INSERT INTO transaksi_pengiriman (id_customer, tgl_transaksi, jam_transaksi, nama_penerima, notelp_penerima, alamat_penerima, email_penerima, nama_barang, berat_barang, jenis_paket, kota_asal, kota_tujuan, metode_pembayaran, biaya_kirim, biaya_packing, biaya_asuransi, total, bayar, kembali) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s);"
                    params1=(id_customer,tanggal,waktu,nama_penerima,notelp_penerima,alamat_penerima,email_penerima,nama_barangg,berat_barang,jenis_paket,kota_asal,kota_tujuan,metode_pembayaran,int(biayakirim_sesuaikg),int(harga_packing),int(harga_asuransi),int(harga_total),bayar,kembalian)
                    mycursor.execute(query1, params1)
                    mydb.commit()

                    no_resi = mycursor.lastrowid
                    self.harga_total.append(harga_total)
                    
                    printable_page = PrintablePage()
                    printable_page.add_page_with_title(f'Struk Pengiriman No_resi:{no_resi}')

                    printable_page.add_content(f'No Resi                : {no_resi}')
                    printable_page.add_content(f'----------------------------------------------')
                    printable_page.add_content(f'Nama Pengirim          : {nama_pengirim}')
                    printable_page.add_content(f'No Telp Pengirim       : {notelp_pengirim}')
                    printable_page.add_content(f'----------------------------------------------')
                    printable_page.add_content(f'Nama Penerima          : {nama_penerima}')
                    printable_page.add_content(f'No Telp Penerima       : {notelp_penerima}')
                    printable_page.add_content(f'Alamat Penerima        : {alamat_penerima}')
                    printable_page.add_content(f'Email Penerima         : {email_penerima}')
                    printable_page.add_content(f'----------------------------------------------')
                    printable_page.add_content(f'Nama Barang             : {nama_barangg}')
                    printable_page.add_content(f'Berat Barang            : {berat_barang}')
                    printable_page.add_content(f'Jenis Paket             : {jenis_paket}')
                    printable_page.add_content(f'Kota Asal Pengiriman    : {kota_asal}')
                    printable_page.add_content(f'Kota Tujuan Pengiriman  : {kota_tujuan}')
                    printable_page.add_content(f'Metode Pembayaran       : {metode_pembayaran}')
                    printable_page.add_content(f'----------------------------------------------')
                    printable_page.add_content(f'BIAYA PENGIRIMAN')
                    printable_page.add_content(f'Biaya Kirim             : {biayakirim_sesuaikg}')
                    printable_page.add_content(f'Biaya Asuransi          : {harga_asuransi}')
                    printable_page.add_content(f'Biaya Packing           : {harga_packing}')
                    printable_page.add_content(f'Total                   : {harga_total}')

                    file_path = f'C:/Users/vilso/OneDrive - Telkom University/Documents/KULIAH/Algoritma dan Pemograman sem 2/TUBES Vilson/output_{no_resi}.pdf'
                    printable_page.output(file_path, 'F')

                    label_text = printable_page.printable_content()
                    messagebox.showinfo("Success", "Data Berhasil masuk database")

                    printable_page.reset_title()
                    printable_page.reset_content()
                else:
                    messagebox.showerror("Error", "Failed to retrieve customer ID")
                    return False
                

                self.entry_input_nama_pengirim.delete(0, tk.END)
                self.entry_input_telp_pengirim.delete(0, tk.END)
                self.entry_input_alamat_pengirim.delete(0, tk.END)
                self.entry_input_email_pengirim.delete(0, tk.END)
                self.entry_input_nama_penerima.delete(0, tk.END)
                self.entry_input_telp_penerima.delete(0, tk.END)
                self.entry_input_alamat_penerima.delete(0, tk.END)
                self.entry_input_email_penerima.delete(0, tk.END)
                self.entry_input_tgl_transaksi.delete(0, tk.END)
                self.entry_input_jam_transaksi.delete(0, tk.END)
                self.entry_input_nbarang.delete(0, tk.END)
                self.entry_input_berat_barang.delete(0, tk.END)
                self.dropdown.delete(0, tk.END)
                self.dropdown_kota_asal_form.delete(0, tk.END)
                self.dropdown_kota_tujuan_form.delete(0, tk.END)
                self.dropdown1.delete(0, tk.END)
                self.selection_form.set(None)
                self.selection_form1.set(None)
                self.halamanbiaya_frame.place_forget()
                self.btn_frame.place_forget()
                self.biaya_frame.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
                self.label_kertas.config(text=label_text)
                self.no_resi.append(no_resi)
                

                return True

            except mysql.connector.Error as error:
                print("Error executing query:", error)
                messagebox.showerror("Error", "Gagal isi form, ada kesalahan")
                return False
            
        def submit2():
            bayar=self.entry_input_bayar.get()
            no=str(self.no_resi[0])
            total=self.harga_total[0]
            kembalian=int(bayar) - int(total)
            if kembalian < 0:
                messagebox.showerror("Error","Uang yang dibayar tidak Cukup")
            elif kembalian >= 0:
                query="UPDATE transaksi_pengiriman SET bayar=%s, kembali=%s WHERE no_resi=%s"
                params=(bayar,kembalian,no)

            if execute_query(query, params):
                messagebox.showinfo("Success", f"Data berhasil ditambah ke database\nKEMBALIAN Transaksi: {kembalian}")
            else:
                messagebox.showerror("Error", "Gagal masukin data ke Database")

            self.entry_input_bayar.delete(0, tk.END)
            self.label_kertas.config(text=None)
            self.no_resi.clear()
            self.harga_total.clear()
            self.biaya_frame.place_forget()
            self.menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=self.menu_width, height=self.menu_height)
            self.dashboard_frame.place(relx=0.13, rely=0.5, anchor=tk.CENTER, width=self.menu_width1, height=self.menu_height)
            
        def execute_query(query, params=()):
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pengiriman_barang_vilson",
                port ="3308"
                )
            mycursor = mydb.cursor()
            try:
                mycursor.execute(query, params)
                mydb.commit()
                return True
            except mysql.connector.Error as error:
                print("Error executing query:", error)
                return False
            finally:
                mycursor.close()
                mydb.close()
        
        
        def tampilin_kota(query):
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="pengiriman_barang_vilson",
                    port ="3308"
                )
                if connection.is_connected():
                    cursor = connection.cursor()
                    cursor.execute(query)
                    result = cursor.fetchall()
                    self.kota_asal_values = [row[0] for row in result]
                    self.dropdown_kota_asal["values"] = self.kota_asal_values
                    self.dropdown_kota_tujuan["values"] = self.kota_asal_values
                    self.dropdown_kota_tujuan_cek["values"] = self.kota_asal_values
                    self.dropdown_kota_asal_cek["values"] = self.kota_asal_values
                    self.dropdown_kota_asal_form["values"] = self.kota_asal_values
                    self.dropdown_kota_tujuan_form["values"] = self.kota_asal_values

                    
            except Error as e:
                print('Error while retrieving data from MySQL', e)


        def submit_tambah():
            jenis_paket = self.dropdown_tambah.get()
            kota_asal = self.entry_tambah_kota_asal.get()
            kota_tujuan = self.entry_tambah_kota_tujuan.get()
            harga = self.entry_tambah_harga.get()

            self.namatable = ""
            if jenis_paket == "Paket Oke":
                self.namatable = "harga_paket_oke"
                query = "INSERT INTO harga_paket_oke (kota_asal, kota_tujuan, harga_kg) VALUES (%s, %s, %s);"
                params = (kota_asal, kota_tujuan, harga)
            elif jenis_paket == "Paket Reguler":
                self.namatable = "harga_paket_reguler"
                query = "INSERT INTO harga_paket_reguler (kota_asal, kota_tujuan, harga_kg) VALUES (%s, %s, %s);"
                params = (kota_asal, kota_tujuan, harga)
            elif jenis_paket == "Paket Yes":
                self.namatable = "harga_paket_yes"
                query = "INSERT INTO harga_paket_yes (kota_asal, kota_tujuan, harga_kg) VALUES (%s, %s, %s);"
                params = (kota_asal, kota_tujuan, harga)
            
            if jenis_paket == "" or kota_asal == "" or kota_tujuan == "" or harga == "":
                tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
                return
        
            if execute_query(query, params):
                messagebox.showinfo("Success", "Data berhasil dimasukkan ke Database")
            else:
                messagebox.showerror("Error", "Gagal memasukkan data ke Database")

            self.entry_tambah_kota_asal.delete(0, tk.END)
            self.dropdown_tambah.delete(0, tk.END)
            self.entry_tambah_kota_tujuan.delete(0, tk.END)
            self.entry_tambah_harga.delete(0, tk.END)
            self.show_data()

        def submit_edit():
            jenis_paket = self.dropdown_harga.get()
            kota_asal = self.dropdown_kota_asal.get()
            kota_tujuan = self.dropdown_kota_tujuan.get()
            harga = self.entry_edit_harga_fix.get()

            self.namatable = ""
            if jenis_paket == "Paket Oke":
                self.namatable = "harga_paket_oke"
                query = "UPDATE harga_paket_oke SET harga_kg = %s WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (harga, kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Reguler":
                self.namatable = "harga_paket_reguler"
                query = "UPDATE harga_paket_reguler SET harga_kg = %s WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (harga, kota_asal, kota_tujuan)
            elif jenis_paket == "Paket Yes":
                self.namatable = "harga_paket_yes"
                query = "UPDATE harga_paket_yes SET harga_kg = %s WHERE kota_asal = %s AND kota_tujuan = %s;"
                params = (harga, kota_asal, kota_tujuan)
            
            if jenis_paket == "" or kota_asal == "" or kota_tujuan == "" or harga == "":
                tkinter.messagebox.showerror("Error", "Mohon lengkapi semua input")
                return
        
            if execute_query(query, params):
                messagebox.showinfo("Success", "Data berhasil diedit ke Database")
            else:
                messagebox.showerror("Error", "Gagal edit data ke Database")

            self.dropdown_kota_asal.delete(0, tk.END)
            self.dropdown_harga.delete(0, tk.END)
            self.dropdown_kota_tujuan.delete(0, tk.END)
            self.entry_edit_harga_fix.delete(0, tk.END)
        
        def back():
            self.halamanbiaya_frame.place_forget()
            self.btn_frame.place_forget()
            self.form_pengiriman_frame.place(relx=0.87, rely=0.5, anchor=tk.CENTER, width=self.menu_width2, height=self.menu_height)
            self.identitas_frame.place(relx=0.63, rely=0.3, anchor=tk.CENTER, width=self.menu_width3)
            self.info_barang_frame.place(relx=0.63, rely=0.55, anchor=tk.CENTER, width=self.menu_width3)

        def on_close():
            response=tkinter.messagebox.askyesno('Exit','Mau keluar? yakin? serius?')
            if response:
                self.window.destroy()

        def toggle_password_visibility():
            if self.show_password.get():
                self.entry_password.configure(show="")
            else:
                self.entry_password.configure(show="*")

        def on_select_jenis_paket(self, event):
            self.selected_item = event.widget.get()
            print("Pilihan Anda:", self.selected_item)

        def on_select_kota_asal(self,event):
            self.selected_item1 = event.widget.get()
            print("Pilihan Anda:", self.selected_item1)

        def on_select_kota_tujuan(self,event):
            self.selected_item2 = event.widget.get()
            print("Pilihan Anda:", self.selected_item2)

        def on_select_metode_bayar(self,event):
            self.selected_item3 = event.widget.get()
            print("Pilihan Anda:", self.selected_item3)
        
        def on_entry_username_key(event):
            if self.entry_username.get() == "Enter username":
                self.entry_username.delete(0, tk.END)

        def on_entry_password_key(event):
            if self.entry_password.get() == "Enter password":
                self.entry_password.delete(0, tk.END)
                self.entry_password.configure(show="*")

        def on_entry_username_leave(event):
            if self.entry_username.get() == "":
                self.entry_username.insert(0, "Enter username")

        def on_entry_password_leave(event):
            if self.entry_password.get() == "":
                self.entry_password.insert(0, "Enter password")
                self.entry_password.configure(show="")
        
        def perbarui_entri_waktu():
            sekarang = datetime.now()
            waktu_string = sekarang.strftime("%H:%M:%S")

            self.entry_input_jam_transaksi.delete(0, tk.END)  # Menghapus nilai sebelumnya
            self.entry_input_jam_transaksi.insert(0, waktu_string)

            self.window.after(1000, perbarui_entri_waktu)


        # Membuat window utama
        self.window = window
        self.window.title("Aplikasi JNE Express - Pengiriman Barang")
        self.window.configure(bg='#DCDCDC')
        
        #setting ukuran full screen
        self. window.geometry("%dx%d" % (self.width, self.height))

        self.style = ttk.Style()
        self.style.configure("Custom.TEntry", highlightbackground="black", highlightcolor="black", foreground="grey", insertbackground="grey")
        self.style.configure("Custom.TCheckbutton", background="white")

        # Halaman login
        self.login_frame = tk.Frame(window, background="white", width=120,height=100)
        self.login_frame.pack(padx=100, pady=500)

        self.image3 = Image.open("login icon.jpg")
        self.image3 = self.image3.resize((100, 120))
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.label_foto_logo = tk.Label(self.login_frame, image=self.photo3, background='white')
        self.label_foto_logo.grid(row=0, column=0, columnspan=2, pady=15)

        self.label_title = tk.Label(self.login_frame, text="ADMINISTRATOR", font=("Helvetica", 30, 'bold'), background='white')
        self.label_title.grid(row=1, column=0, columnspan=2, pady=15)

        self.label_username = tk.Label(self.login_frame, text="Username:", background='white')
        self.label_username.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_username = customtkinter.CTkEntry(self.login_frame, width=320)
        self.entry_username.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        self.entry_username.insert(0, "Enter username")

        self.label_password = tk.Label(self.login_frame, text="Password:", background='white')
        self.label_password.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_password = customtkinter.CTkEntry(self.login_frame, width=320)
        self.entry_password.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
        self.entry_password.insert(0, "Enter password")

        self.entry_username.bind("<Key>", on_entry_username_key)
        self.entry_password.bind("<Key>", on_entry_password_key)
        self.entry_username.bind("<FocusOut>", on_entry_username_leave)
        self.entry_password.bind("<FocusOut>", on_entry_password_leave)

        self.show_password = tk.BooleanVar()
        self.show_password_checkbox = customtkinter.CTkCheckBox(self.login_frame, text="Tampilkan Password", variable=self.show_password)
        self.show_password_checkbox.configure(command=toggle_password_visibility)
        self.show_password_checkbox.grid(row=4, column=1, sticky=tk.E, padx=10, pady=5)

        self.btn_login = customtkinter.CTkButton(self.login_frame, text="Login", command=login, width=100)
        self.btn_login.grid(row=5, columnspan=5, padx=10, pady=10)

        self.entry_password.bind("<Return>", lambda event: login())

        # Halaman Background Menu
        self.menu_frame = tk.Frame(window, background='#DCDCDC')
        self.visualisasi_frame = tk.Frame(self.menu_frame, background='#DCDCDC')
        self.visualisasi_frame.pack(fill='both', expand=True)
        
        
        # Frame dashboard
        self.dashboard_frame = tk.Frame(window)

        self.image = Image.open("logo jne.png")
        self.image = self.image.resize((250, 200))
        self.photo = ImageTk.PhotoImage(self.image)
        self.label_foto_logo = tk.Label(self.dashboard_frame, image=self.photo)
        self.label_foto_logo.place(relx=0.475, rely=0.25, anchor=tk.CENTER)
        
        self.label_menu = tk.Label(self.dashboard_frame, text="Dashboard", font=("Calibri", 18, 'bold'))
        self.label_menu.place(relx=0.2, rely=0.05, anchor=tk.CENTER)

        self.icon_image1 = Image.open("1.png")
        self.icon_resized1 = self.icon_image1.resize((26, 26))  
        self.icon_tk1 = ImageTk.PhotoImage(self.icon_resized1)
        self.btn_form_pengiriman = tk.Button(self.dashboard_frame, text="Form Pengiriman", font=("Calibri", 13), relief=tk.FLAT, command=menu_form_pengiriman, width=300, image=self.icon_tk1, compound="left")
        self.btn_form_pengiriman.place(relx=0.24, rely=0.4, anchor=tk.CENTER)
        self.btn_form_pengiriman.config(anchor=tk.W)

        self.icon_image2 = Image.open("2.png")
        self.icon_resized2 = self.icon_image2.resize((26, 26))  
        self.icon_tk2 = ImageTk.PhotoImage(self.icon_resized2)
        self.btn_cek_harga = tk.Button(self.dashboard_frame, text="Cek Harga", font=("Calibri", 13), relief=tk.FLAT, command=menu_cek_harga, width=200, image=self.icon_tk2, compound="left")
        self.btn_cek_harga.place(relx=0.17, rely=0.45, anchor=tk.CENTER)
        self.btn_cek_harga.config(anchor=tk.W)

        self.icon_image3 = Image.open("3.png")
        self.icon_resized3 = self.icon_image3.resize((26, 26))  
        self.icon_tk3 = ImageTk.PhotoImage(self.icon_resized3)
        self.btn_edit_masterdata = tk.Button(self.dashboard_frame, text="Edit Master Data", font=("Calibri", 13), relief=tk.FLAT, width=300, image=self.icon_tk3, command=edit_masterdata, compound="left")
        self.btn_edit_masterdata.place(relx=0.24, rely=0.5, anchor=tk.CENTER)
        self.btn_edit_masterdata.config(anchor=tk.W)

        #Halaman Form Pengiriman
        self.form_pengiriman_frame = tk.Frame(window, background='#DCDCDC')

        self.form_pengiriman_menu = tk.Label(self.form_pengiriman_frame, text="FORM PENGIRIMAN", font=("Helvetica", 30, 'bold'), background='#DCDCDC')
        self.form_pengiriman_menu.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        self.btn_next = customtkinter.CTkButton(self.form_pengiriman_frame, text="NEXT",command=next,width=100)
        self.btn_next.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.btn_menu = customtkinter.CTkButton(self.form_pengiriman_frame, text="MENU",command=menu,width=100)
        self.btn_menu.place(relx=0.4, rely=0.9, anchor=tk.CENTER)

        #kotak identitas
        self.identitas_frame = tk.Frame(window, background='white')
        self.label_identitas_pengirim = tk.Label(self.identitas_frame, text="Identitas Pengirim:", font=("Helvetica", 13, 'bold'),background='white') 
        self.label_identitas_pengirim.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_input_nama_pengirim = tk.Label(self.identitas_frame, text="Nama Pengirim:", background='white') 
        self.label_input_nama_pengirim.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_nama_pengirim = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_nama_pengirim.grid(row=1, column=1, padx=10, pady=5)

        self.label_input_telp_pengirim = tk.Label(self.identitas_frame, text="No Telp Pengirim:", background='white') 
        self.label_input_telp_pengirim.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_telp_pengirim = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_telp_pengirim.grid(row=2, column=1, padx=10, pady=5)

        self.label_input_alamat_pengirim = tk.Label(self.identitas_frame, text="Alamat Pengirim:", background='white') 
        self.label_input_alamat_pengirim.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_alamat_pengirim = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_alamat_pengirim.grid(row=3, column=1, padx=10, pady=5)

        self.label_input_email_pengirim = tk.Label(self.identitas_frame, text="Email Pengirim:", background='white') 
        self.label_input_email_pengirim.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_email_pengirim = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_email_pengirim.grid(row=4, column=1, padx=10, pady=5)

        #Kotak tujuan pengiriman
        
        self.label_identitas_penerima = tk.Label(self.identitas_frame, text="Identitas Penerima:", font=("Helvetica", 13, 'bold'), background='white') 
        self.label_identitas_penerima.grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)

        self.label_input_nama_penerima = tk.Label(self.identitas_frame, text="Nama Penerima:", background='white') 
        self.label_input_nama_penerima.grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
        self.entry_input_nama_penerima = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_nama_penerima.grid(row=1, column=3, padx=10, pady=5)

        self.label_input_telp_penerima = tk.Label(self.identitas_frame, text="No Telp Penerima:", background='white') 
        self.label_input_telp_penerima.grid(row=2, column=2, sticky=tk.W, padx=10, pady=5)
        self.entry_input_telp_penerima = ttk.Entry(self.identitas_frame,width=40)
        self.entry_input_telp_penerima.grid(row=2, column=3, padx=10, pady=5)

        self.label_input_alamat_penerima = tk.Label(self.identitas_frame, text="Alamat Penerima:", background='white') 
        self.label_input_alamat_penerima.grid(row=3, column=2, sticky=tk.W, padx=10, pady=5)
        self.entry_input_alamat_penerima = ttk.Entry(self.identitas_frame,width=40)
        self.entry_input_alamat_penerima.grid(row=3, column=3, padx=10, pady=5)

        self.label_input_email_penerima = tk.Label(self.identitas_frame, text="Email Penerima:", background='white') 
        self.label_input_email_penerima.grid(row=4, column=2, sticky=tk.W, padx=10, pady=5)
        self.entry_input_email_penerima = ttk.Entry(self.identitas_frame, width=40)
        self.entry_input_email_penerima.grid(row=4, column=3, padx=10, pady=5)

        #Kotak Transaksi pengiriman barang
        self.info_barang_frame = tk.Frame(window, background='white')
        self.label_info_barang = tk.Label(self.info_barang_frame, text="Informasi Barang:", font=("Helvetica", 13, 'bold'), background='white') 
        self.label_info_barang.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_input_tgl_transaksi = tk.Label(self.info_barang_frame, text="Tanggal Transaksi:", background='white') 
        self.label_input_tgl_transaksi.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_tgl_transaksi = ttk.Entry(self.info_barang_frame, width=40)
        self.entry_input_tgl_transaksi.grid(row=1, column=1, padx=5, pady=5)
        self.button_pick_tgl_transaksi = ttk.Button(self.info_barang_frame, command=self.pick_tgl_transaksi)
        self.button_pick_tgl_transaksi.grid(row=1, column=1, padx=10, pady=5, sticky=tk.E)
        image10 = Image.open("CA.png")  
        image10 = image10.resize((26, 26))  
        icon10 = ImageTk.PhotoImage(image10)

        self.button_pick_tgl_transaksi.config(image=icon10)
        self.button_pick_tgl_transaksi.image = icon10 

        self.label_input_jam_transaksi = tk.Label(self.info_barang_frame, text="Jam Transaksi:", background='white') 
        self.label_input_jam_transaksi.grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
        self.entry_input_jam_transaksi = ttk.Entry(self.info_barang_frame, width=40)
        self.entry_input_jam_transaksi.grid(row=1, column=3, padx=10, pady=5)

        self.label_input_nama_barang = tk.Label(self.info_barang_frame, text="Nama/isi Barang:", background='white') 
        self.label_input_nama_barang.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

        self.entry_input_nbarang = ttk.Entry(self.info_barang_frame, width=40)
        self.entry_input_nbarang.grid(row=2, column=1, padx=10, pady=5)

        self.label_input_berat_barang = tk.Label(self.info_barang_frame, text="Berat Barang (kg):", background='white') 
        self.label_input_berat_barang.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_berat_barang = ttk.Entry(self.info_barang_frame,width=40)
        self.entry_input_berat_barang.grid(row=3, column=1, padx=10, pady=5)

        self.label_input_kota_asal = tk.Label(self.info_barang_frame, text="Kota Asal:", background='white') 
        self.label_input_kota_asal.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_input_kota_tujuan = tk.Label(self.info_barang_frame, text="Kota Tujuan:", background='white') 
        self.label_input_kota_tujuan.grid(row=5, column=2, sticky=tk.W, padx=10, pady=5)

        self.selected_option8 = tk.StringVar()
        self.dropdown_kota_asal_form = ttk.Combobox(self.info_barang_frame, textvariable=self.selected_option8, width=37)
        self.dropdown_kota_asal_form.grid(row=5, column=1, padx=10, pady=5)

        self.dropdown_kota_asal_form.bind("<<ComboboxSelected>>", on_select_kota_asal)

        self.selected_option9 = tk.StringVar()
        self.dropdown_kota_tujuan_form = ttk.Combobox(self.info_barang_frame, textvariable=self.selected_option9,width=37)
        self.dropdown_kota_tujuan_form.grid(row=5, column=3, padx=10, pady=5)

        self.dropdown_kota_tujuan_form.bind("<<ComboboxSelected>>", on_select_kota_tujuan)

        self.jenis_paket_label = tk.Label(self.info_barang_frame, text="Pilih Jenis Paket:", background='white')
        self.jenis_paket_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

        self.options = ["Paket Oke", "Paket Reguler", "Paket Yes"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.info_barang_frame, textvariable=self.selected_option, values=self.options,width=37)
        self.dropdown.grid(row=4, column=1, padx=10, pady=5)

        self.btn_cek_tampil_kota_form = customtkinter.CTkButton(self.info_barang_frame, text="Lihat Kota",width=15, command=fungsi_tombol_tampilin2)
        self.btn_cek_tampil_kota_form.grid(row=4, column=2, sticky=tk.W, padx=10, pady=5)

        self.metode_bayar_label = tk.Label(self.info_barang_frame, text="Pilih Jenis Pembayaran:", background='white')
        self.metode_bayar_label.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)

        self.options1 = ["Cash", "Debit Card", "Kredit Card", "QRIS"]
        self.selected_option1 = tk.StringVar()
        self.dropdown1 = ttk.Combobox(self.info_barang_frame, textvariable=self.selected_option1, values=self.options1,width=37)
        self.dropdown1.grid(row=6, column=1, padx=10, pady=5)

        self.dropdown.bind("<<ComboboxSelected>>", on_select_jenis_paket)
        self.dropdown1.bind("<<ComboboxSelected>>", on_select_metode_bayar)

        #Halaman selanjutnya form
        self.halamanbiaya_frame = tk.Frame(window, background='white')
        self.label_biaya_pengiriman = tk.Label(self.halamanbiaya_frame, text="Biaya Pengirim:", font=("Helvetica", 13, 'bold'), background='white') 
        self.label_biaya_pengiriman.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_packing = tk.Label(self.halamanbiaya_frame, text="Packing:", background='white') 
        self.label_packing.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        
        self.selection_form = tk.IntVar()
        self.selection_form1 = tk.IntVar()
        

        self.yes_button_packing = customtkinter.CTkRadioButton(self.halamanbiaya_frame, text="YES", variable=self.selection_form1, value=1, command=selection_changed2)
        self.yes_button_packing.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)

        self.no_button_packing = customtkinter.CTkRadioButton(self.halamanbiaya_frame, text="NO", variable=self.selection_form1, value=2, command=selection_changed2)
        self.no_button_packing.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

        self.label_asuransi = tk.Label(self.halamanbiaya_frame, text="Asuransi:", background='white') 
        self.label_asuransi.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.yes_button_asuransi = customtkinter.CTkRadioButton(self.halamanbiaya_frame, text="YES", variable=self.selection_form, value=1, command=selection_changed3)
        self.yes_button_asuransi.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)

        self.no_button_asuransi = customtkinter.CTkRadioButton(self.halamanbiaya_frame, text="NO", variable=self.selection_form, value=2, command=selection_changed3)
        self.no_button_asuransi.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)

        self.btn_frame = tk.Frame(window, background='#DCDCDC')
        self.btn_back = customtkinter.CTkButton(self.btn_frame, text="BACK",command=back,width=100)
        self.btn_back.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.btn_submit = customtkinter.CTkButton(self.btn_frame, text="SUBMIT",command=submit,width=100)
        self.btn_submit.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        self.btn_menu = customtkinter.CTkButton(self.btn_frame, text="MENU",command=menu,width=100)
        self.btn_menu.grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)

        #Halaman tampilin biaya-biaya
        self.biaya_frame = tk.Frame(window, background='white')
        self.label_kertas = tk.Label(self.biaya_frame, text=None, anchor='w')
        self.label_kertas.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.btn_print = customtkinter.CTkButton(self.biaya_frame, text="Print",command=self.print_pdf,width=100)
        self.btn_print.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)

        self.label_bayar = tk.Label(self.biaya_frame, text="Bayar:", background='white')
        self.label_bayar.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_bayar = ttk.Entry(self.biaya_frame,width=40)
        self.entry_input_bayar.grid(row=2, column=1, padx=10, pady=5)

        self.btn_submit2 = customtkinter.CTkButton(self.biaya_frame, text="Submit",command=submit2,width=100)
        self.btn_submit2.grid(row=4, column=2, sticky=tk.W, padx=10, pady=5)
        
        #Halaman Cek harga
        self.cek_harga_frame = tk.Frame(window, background='#DCDCDC')

        self.cek_harga_menu = tk.Label(self.cek_harga_frame, text="Cek Harga", font=("Helvetica", 30, 'bold'), background='#DCDCDC')
        self.cek_harga_menu.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        self.info_biaya_frame = tk.Frame(window, background='white')
        self.cek_harga_asuransi = tk.Label(self.info_biaya_frame, text="Harga Asuransi per kg: Rp 10000", background="yellow")
        self.cek_harga_packing = tk.Label(self.info_biaya_frame, text="Harga Packing: Rp 10000", background="yellow")
        self.cek_harga_packing.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.cek_harga_asuransi.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.label_input_berat_cek = tk.Label(self.info_biaya_frame, text="Berat Barang:", background='white') 
        self.label_input_berat_cek.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_input_berat_cek = ttk.Entry(self.info_biaya_frame,width=40)
        self.entry_input_berat_cek.grid(row=2, column=1, padx=10, pady=5)

        self.label_kg = tk.Label(self.info_biaya_frame, text="kg", background='white')
        self.label_kg.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

        self.label_input_kota_asal_cek = tk.Label(self.info_biaya_frame, text="Kota Asal:", background='white') 
        self.label_input_kota_asal_cek.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_input_kota_tujuan_cek = tk.Label(self.info_biaya_frame, text="Kota Tujuan:", background='white') 
        self.label_input_kota_tujuan_cek.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

        self.selected_option6 = tk.StringVar()
        self.dropdown_kota_asal_cek = ttk.Combobox(self.info_biaya_frame, textvariable=self.selected_option6, width=37)
        self.dropdown_kota_asal_cek.grid(row=4, column=1, padx=10, pady=5)

        self.dropdown_kota_asal_cek.bind("<<ComboboxSelected>>", on_select_kota_asal)

        self.selected_option7 = tk.StringVar()
        self.dropdown_kota_tujuan_cek = ttk.Combobox(self.info_biaya_frame, textvariable=self.selected_option7,width=37)
        self.dropdown_kota_tujuan_cek.grid(row=5, column=1, padx=10, pady=5)

        self.dropdown_kota_tujuan_cek.bind("<<ComboboxSelected>>", on_select_kota_tujuan)

        self.jenis_paket_label_cek = tk.Label(self.info_biaya_frame, text="Pilih Jenis Paket:", background='white')
        self.jenis_paket_label_cek.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.options_cek = ["Paket Oke", "Paket Reguler", "Paket Yes"]
        self.selected_option1 = tk.StringVar()
        self.dropdown_cek = ttk.Combobox(self.info_biaya_frame, textvariable=self.selected_option1, values=self.options_cek,width=37)
        self.dropdown_cek.grid(row=3, column=1, padx=10, pady=5)

        self.dropdown_cek.bind("<<ComboboxSelected>>", on_select_jenis_paket)

        self.btn_cek_tampil_kota_cek = customtkinter.CTkButton(self.info_biaya_frame, text="Lihat Kota",width=15, command=fungsi_tombol_tampilin1)
        self.btn_cek_tampil_kota_cek.grid(row=3, column=2, sticky=tk.W, padx=10, pady=5)

        self.label_packing_cek = tk.Label(self.info_biaya_frame, text="Packing:", background='white') 
        self.label_packing_cek.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)
        
        self.selection_cek = tk.IntVar()
        self.selection_cek1 = tk.IntVar()

        self.yes_button_packing_cek = customtkinter.CTkRadioButton(self.info_biaya_frame, text="YES", variable=self.selection_cek, value=1, command=selection_changed)
        self.yes_button_packing_cek.grid(row=6, column=1, sticky=tk.W, padx=10, pady=5)

        self.no_button_packing_cek = customtkinter.CTkRadioButton(self.info_biaya_frame, text="NO", variable=self.selection_cek, value=2, command=selection_changed)
        self.no_button_packing_cek.grid(row=7, column=1, sticky=tk.W, padx=10, pady=5)

        self.label_asuransi_cek = tk.Label(self.info_biaya_frame, text="Asuransi:", background='white') 
        self.label_asuransi_cek.grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)

        self.yes_button_asuransi_cek = customtkinter.CTkRadioButton(self.info_biaya_frame, text="YES", variable=self.selection_cek1, value=1, command=selection_changed1)
        self.yes_button_asuransi_cek.grid(row=8, column=1, sticky=tk.W, padx=10, pady=5)

        self.no_button_asuransi_cek = customtkinter.CTkRadioButton(self.info_biaya_frame, text="NO", variable=self.selection_cek1, value=2, command=selection_changed1)
        self.no_button_asuransi_cek.grid(row=9, column=1, sticky=tk.W, padx=10, pady=5)

        self.btn_cek_harga = customtkinter.CTkButton(self.info_biaya_frame, text="Cek Harga",command=cek_harga,width=20)
        self.btn_cek_harga.grid(row=11, column=7, sticky=tk.W, padx=10, pady=5)
        self.btn_menu = customtkinter.CTkButton(self.info_biaya_frame, text="MENU",command=menu,width=100)
        self.btn_menu.grid(row=11, column=8, sticky=tk.W, padx=10, pady=5)

        self.cek_frame = tk.Frame(window, background='white')
        self.btn_cek_harga_reset = customtkinter.CTkButton(self.cek_frame, text="Reset",command=reset,width=20)

        #Halaman Edit Master Data
        self.edit_frame = tk.Frame(window, background='white')
        self.edit_menu = tk.Label(self.edit_frame, text="Menu Edit Master Data:", font=("Helvetica", 20, 'bold'), background='white')
        self.edit_menu.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

        self.btn_tambah_kota = customtkinter.CTkButton(self.edit_frame, text="Tambah Data Kota",width=250, command=tambah_data)
        self.btn_tambah_kota.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

        self.btn_edit_harga = customtkinter.CTkButton(self.edit_frame, text="Edit Data Harga",width=250,command=edit_harga)
        self.btn_edit_harga.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

        #Halaman edit tambah data kota
        self.edit_tambah_frame = tk.Frame(window, background='white')

        self.label_tambah = tk.Label(self.edit_tambah_frame, text="Tambah Data Kota", font=("Calibri", 14, 'bold'), background='white')
        self.label_tambah.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.jenis_paket_label_tambah = tk.Label(self.edit_tambah_frame, text="Pilih Jenis Paket yang ingin ditambah:", background='white')
        self.jenis_paket_label_tambah.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

        self.options_tambah = ["Paket Oke", "Paket Reguler", "Paket Yes"]
        self.selected_option2 = tk.StringVar()
        self.dropdown_tambah = ttk.Combobox(self.edit_tambah_frame, textvariable=self.selected_option2, values=self.options_tambah,width=37)
        self.dropdown_tambah.grid(row=1, column=1, padx=10, pady=5)

        self.dropdown_tambah.bind("<<ComboboxSelected>>", on_select_jenis_paket)

        self.label_tambah_kota_asal = tk.Label(self.edit_tambah_frame, text="Kota Asal yang di tambah:", background='white') 
        self.label_tambah_kota_asal.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_tambah_kota_asal = ttk.Entry(self.edit_tambah_frame,width=40)
        self.entry_tambah_kota_asal.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_tambah_kota_tujuan = tk.Label(self.edit_tambah_frame, text="Kota Tujuan yang di tambah:", background='white') 
        self.label_tambah_kota_tujuan.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_tambah_kota_tujuan = ttk.Entry(self.edit_tambah_frame, width=40)
        self.entry_tambah_kota_tujuan.grid(row=3, column=1, padx=10, pady=5)
        
        self.label_tambah_harga = tk.Label(self.edit_tambah_frame, text="Harga yang diberikan per Kg:", background='white') 
        self.label_tambah_harga.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_tambah_harga = ttk.Entry(self.edit_tambah_frame, width=40)
        self.entry_tambah_harga.grid(row=4, column=1, padx=10, pady=5)

        self.btn_submit_tambah = customtkinter.CTkButton(self.edit_tambah_frame, text="SUBMIT",width=100,command=submit_tambah)
        self.btn_submit_tambah.grid(row=6, column=8, sticky=tk.W, padx=10, pady=5)

        self.btn_menu = customtkinter.CTkButton(self.edit_tambah_frame, text="MENU",command=menu,width=100)
        self.btn_menu.grid(row=6, column=7, sticky=tk.W, padx=10, pady=5)
        self.refresh = customtkinter.CTkButton(self.edit_tambah_frame, text="Refresh Tabel", font=("Calibri", 13), width=100, command=self.refresh_treeview)
        self.refresh.grid(row=6, column=6, sticky=tk.W, padx=10, pady=5)

        self.table_frame = tk.Frame(window, background='#DCDCDC')

        self.label_tabel = tk.Label(self.table_frame, text="Tabel Jenis Paket Oke:", background='#DCDCDC') 
        self.label_tabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo = ttk.Treeview(
            self.table_frame,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo.grid(row=1,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))

        self.table_frame1 = tk.Frame(window, background='#DCDCDC')

        self.label_tabel1 = tk.Label(self.table_frame1, text="Tabel Jenis Paket Reguler:", background='#DCDCDC') 
        self.label_tabel1.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo1 = ttk.Treeview(
            self.table_frame1,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo1.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo1.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo1.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo1.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo1.grid(row=4,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))

        self.table_frame2 = tk.Frame(window, background='#DCDCDC')

        self.label_tabel2 = tk.Label(self.table_frame2, text="Tabel Jenis Paket Yes:", background='#DCDCDC') 
        self.label_tabel2.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo2 = ttk.Treeview(
            self.table_frame2,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo2.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo2.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo2.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo2.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo2.grid(row=7,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))
        self.show_data1()

        #Halaman edit harga
        self.edit_harga_frame = tk.Frame(window, background='white')

        self.label_edit_harga = tk.Label(self.edit_harga_frame, text="Edit Data Harga", font=("Calibri", 14, 'bold'), background='white')
        self.label_edit_harga.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.jenis_paket_label_edit = tk.Label(self.edit_harga_frame, text="Pilih Jenis Paket yang ingin di edit:", background='white')
        self.jenis_paket_label_edit.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

        self.options_harga = ["Paket Oke", "Paket Reguler", "Paket Yes"]
        self.selected_option3 = tk.StringVar()
        self.dropdown_harga = ttk.Combobox(self.edit_harga_frame, textvariable=self.selected_option3, values=self.options_harga,width=37)
        self.dropdown_harga.grid(row=1, column=1, padx=10, pady=5)

        self.dropdown_harga.bind("<<ComboboxSelected>>", on_select_jenis_paket)

        self.btn_cek_tampil_kota = customtkinter.CTkButton(self.edit_harga_frame, text="Lihat Kota",width=100, command=fungsi_tombol_tampilin)
        self.btn_cek_tampil_kota.grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)

        self.label_harga_kota_asal = tk.Label(self.edit_harga_frame, text="Kota Asal yang di edit harga:", background='white') 
        self.label_harga_kota_asal.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

        self.label_harga_kota_tujuan = tk.Label(self.edit_harga_frame, text="Kota Tujuan yang di edit:", background='white') 
        self.label_harga_kota_tujuan.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.selected_option4 = tk.StringVar()
        self.dropdown_kota_asal = ttk.Combobox(self.edit_harga_frame, textvariable=self.selected_option4, width=37)
        self.dropdown_kota_asal.grid(row=2, column=1, padx=10, pady=5)

        self.dropdown_kota_asal.bind("<<ComboboxSelected>>", on_select_kota_asal)

        self.selected_option5 = tk.StringVar()
        self.dropdown_kota_tujuan = ttk.Combobox(self.edit_harga_frame, textvariable=self.selected_option5,width=37)
        self.dropdown_kota_tujuan.grid(row=3, column=1, padx=10, pady=5)

        self.dropdown_kota_tujuan.bind("<<ComboboxSelected>>", on_select_kota_tujuan)

        self.label_edit_harga_fix = tk.Label(self.edit_harga_frame, text="Harga yang di edit per Kg:", background='white') 
        self.label_edit_harga_fix.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.entry_edit_harga_fix = ttk.Entry(self.edit_harga_frame, width=40)
        self.entry_edit_harga_fix.grid(row=4, column=1, padx=10, pady=5)

        self.btn_submit_edit = customtkinter.CTkButton(self.edit_harga_frame, text="SUBMIT",width=100, command=submit_edit)
        self.btn_submit_edit.grid(row=6, column=4, sticky=tk.W, padx=10, pady=5)
        self.btn_menu = customtkinter.CTkButton(self.edit_harga_frame, text="MENU",command=menu,width=100)
        self.btn_menu.grid(row=6, column=3, sticky=tk.W, padx=10, pady=5)
        self.refresh = customtkinter.CTkButton(self.edit_harga_frame, text="Refresh Tabel", font=("Calibri", 13), width=100, command=self.refresh_treeview)
        self.refresh.grid(row=6, column=2, sticky=tk.W, padx=10, pady=5)

        self.table_frame3 = tk.Frame(window, background='#DCDCDC')

        self.label_tabel = tk.Label(self.table_frame3, text="Tabel Jenis Paket Oke:", background='#DCDCDC') 
        self.label_tabel.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo3 = ttk.Treeview(
            self.table_frame3,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo3.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo3.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo3.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo3.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo3.grid(row=1,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))

        self.table_frame4 = tk.Frame(window, background='#DCDCDC')

        self.label_tabel1 = tk.Label(self.table_frame4, text="Tabel Jenis Paket Reguler:", background='#DCDCDC') 
        self.label_tabel1.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo4 = ttk.Treeview(
            self.table_frame4,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo4.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo4.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo4.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo4.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo4.grid(row=4,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))

        self.table_frame5 = tk.Frame(window, background='#DCDCDC')

        self.label_tabel2 = tk.Label(self.table_frame5, text="Tabel Jenis Paket Yes:", background='#DCDCDC') 
        self.label_tabel2.grid(row=6, column=0, sticky=tk.W, padx=10, pady=5)

        self.baganinfo5 = ttk.Treeview(
            self.table_frame5,
            columns=("id_paketoke", "kota_asal", "kota_tujuan", "harga_kg"),
            show="headings",
        )
        self.baganinfo5.heading("id_paketoke", text="Id Paket", anchor="center")
        self.baganinfo5.heading("kota_asal", text="Kota Asal", anchor="center")
        self.baganinfo5.heading("kota_tujuan", text="Kota Tujuan", anchor="center")
        self.baganinfo5.heading("harga_kg", text="Harga / Kg", anchor="center")
        self.baganinfo5.grid(row=7,column=0)
        
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold", ))
        self.show_data()


        self.window.protocol('WM_DELETE_WINDOW', on_close)

        # Menampilkan halaman login saat pertama kali dibuka
        self.login_frame.pack()
    
        
    
    def pick_tgl_transaksi(self):
        def set_tanggal():
            tanggal = cal.get_date()
            self.entry_input_tgl_transaksi.delete(0, tk.END)
            self.entry_input_tgl_transaksi.insert(0, tanggal)
            top.destroy()

        top = tk.Toplevel(self.info_barang_frame)
        cal = Calendar(top, selectmode="day", date_pattern="yyyy-mm-dd")
        cal.pack(pady=10)
        ttk.Button(top, text="Pilih", command=set_tanggal).pack()

    
    def print_pdf(self):
        no=str(self.no_resi[0])
        pdf_path = f'C:/Users/vilso/OneDrive - Telkom University/Documents/KULIAH/Algoritma dan Pemograman sem 2/TUBES Vilson/output_{no}.pdf'  # Ganti dengan path yang sesuai ke file PDF Anda
        webbrowser.open(pdf_path, new=2)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'p')
        no=None
    
    def show_data(self):
        records = self.baganinfo.get_children()
        for record in records:
            self.baganinfo.delete(record)
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pengiriman_barang_vilson",
                port ="3308"
                )
        mycursor = mydb.cursor()
        query = "SELECT * FROM harga_paket_oke"
        query1 = "SELECT * FROM harga_paket_reguler"
        query2 = "SELECT * FROM harga_paket_yes"
        try:
            mycursor.execute(query)
            data = mycursor.fetchall()
            for row in data:
                self.baganinfo.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
                self.baganinfo3.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mycursor.execute(query1)
            data1 = mycursor.fetchall()
            for row in data1:
                self.baganinfo1.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
                self.baganinfo4.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mycursor.execute(query2)
            data2 = mycursor.fetchall()
            for row in data2:
                self.baganinfo2.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
                self.baganinfo5.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mydb.commit()
            return True
        except mysql.connector.Error as error:
            print("Error executing query:", error)
            return False
        finally:
            mycursor.close()
            mydb.close()

    def show_data1(self):
        records = self.baganinfo.get_children()
        for record in records:
            self.baganinfo.delete(record)
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pengiriman_barang_vilson",
                port ="3308"
                )
        mycursor = mydb.cursor()
        query = "SELECT * FROM harga_paket_oke"
        query1 = "SELECT * FROM harga_paket_reguler"
        query2 = "SELECT * FROM harga_paket_yes"
        try:
            mycursor.execute(query)
            data = mycursor.fetchall()
            for row in data:
                self.baganinfo.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mycursor.execute(query1)
            data1 = mycursor.fetchall()
            for row in data1:
                self.baganinfo1.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mycursor.execute(query2)
            data2 = mycursor.fetchall()
            for row in data2:
                self.baganinfo2.insert("", tk.END, values=(row[0],) + tuple(row[1:]))
            mydb.commit()
            return True
        except mysql.connector.Error as error:
            print("Error executing query:", error)
            return False
        finally:
            mycursor.close()
            mydb.close()

    def refresh_treeview(self):
        self.show_data()
        self.show_data1()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
           
    
    
class PrintablePage(FPDF):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.content = ""

    def add_page_with_title(self, title):
        self.add_page()
        self.title = title

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, align='C', ln=True)

    def add_content(self, content):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.content += content + "\n"  # Tambahkan konten baru ke atribut content

    def reset_title(self):
        self.title = ""

    def reset_content(self):
        self.content = ""

    def printable_content(self):
        return self.content


# Menjalankan event loop
if __name__ == "__main__":
    app = pengiriman_barang(window=tk.Tk()) 
    app.window.mainloop()