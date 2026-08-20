import numpy as np
import camb

xi = -0.1
pars = camb.set_params(
    H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,
    As=2.1e-9, ns=0.965, xi=xi,
    dark_energy_model='fluid', lmax=500,
)
r = camb.get_results(pars)

a = np.array([1.0, 0.5, 0.25, 0.1, 0.01, 0.001])
dens = r.get_background_densities(a, vars=['cdm', 'de'])
print(f"xi={xi}  (densities are 8πG·rho·a^4)")
print(f"{'a':>8} {'rho_cdm·a^4':>16} {'rho_de·a^4':>16} {'rho_cdm(phys)':>16} {'rho_de(phys)':>16}")
for i, ai in enumerate(a):
    rc4 = dens['cdm'][i]   # rho_cdm * a^4
    rd4 = dens['de'][i]    # rho_de * a^4
    rc = rc4 / ai**4       # fiziksel rho_cdm
    rd = rd4 / ai**4       # fiziksel rho_de
    print(f"{ai:>8.3f} {rc4:>16.6e} {rd4:>16.6e} {rc:>16.6e} {rd:>16.6e}")

# Beklenti (xi=-0.1, w=-1):
#   rho_de ~ a^(-xi) = a^(0.1)  -> a kuculdukce rho_de AZALIR
#   rho_cdm ~ a^-3 + ekstra terim
print()
print("Beklenti: rho_de ~ a^(0.1), yani a kuculdukce rho_de azalmali")
print("a=1 -> a=0.001 arasi rho_de orani:", end=" ")
