def çıktı_al(çıktı):
    if çıktı > 0.7 and çıktı < 1:
        print("\nMetni taradık, genel tutum SON DERECE İYİ. Skor: ", round(çıktı,2))
    elif çıktı > 0.4 and çıktı < 0.7:
        print("\nMetni taradık, genel tutum ÇOK İYİ. Skor: ", round(çıktı,2))
    elif çıktı > 0.2 and çıktı < 0.4:
        print("\nMetni taradık, genel tutum İYİ. Skor: ", round(çıktı,2))
    elif çıktı > 0 and çıktı < 0.2:
        print("\nMetni taradık, genel tutum FENA DEĞİL. Skor: ", round(çıktı,2))
    elif çıktı < 0 and çıktı > -0.9:
        print("\nMetni taradık, genel tutum KÖTÜ. Skor: ", round(çıktı,2))
    elif çıktı < -0.9:
        print("\nMetni taradık, genel tutum BERBAT. Skor: ", round(çıktı,2))
    else:
        print("\nMetni taradık, genel tutum NÖTR. Skor: ", round(çıktı,2))
    return çıktı
