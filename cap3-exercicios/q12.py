dist_km, dist_poste = map(float, input().split())
dist_m = dist_km * 1000
num_postes = int(dist_m // dist_poste + 1)
dist_ultimo = dist_m - dist_poste * (num_postes - 1)

print("poste(s):", num_postes, dist_ultimo, "metro(s)")
