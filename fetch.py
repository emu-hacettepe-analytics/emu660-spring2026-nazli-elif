from yokatlas_py import search_lisans_programs

raw = search_lisans_programs({"bolum": "Mühendis"})
raw = [p for p in raw if p.get("program_adi", "").endswith("lisliği") or
                         p.get("program_adi", "").endswith("hendisliği")]

print(f"Filtrelenmis program sayisi: {len(raw)}")
bolumler = sorted(set(p["program_adi"] for p in raw))
print(f"Benzersiz bolum sayisi: {len(bolumler)}")
