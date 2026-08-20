import numpy as np
import camb

xi = -0.1
pars = camb.set_params(
    H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,
    As=2.1e-9, ns=0.965, xi=xi,
    dark_energy_model='fluid', lmax=500,
)
r = camb.get_results(pars)

# Farkli a degerlerinde: kodun H(a)'si vs bilesenlerden hesaplanan H(a)
print(f"xi={xi}")
print(f"{'z':>8} {'H_code':>12} {'rho_tot^0.5 scaled':>18}")
for z in [0.0, 0.5, 1.0, 3.0, 10.0, 100.0, 1100.0]:
    a = 1.0/(1.0+z)
    H_code = r.hubble_parameter(z)
    # bilesenlerin yogunluklari (get_background_densities)
    dens = r.get_background_densities(np.array([a]), vars=['tot'])
    rho_tot = dens['tot'][0]
    print(f"{z:>8.1f} {H_code:>12.4f} {rho_tot:>18.6e}")
